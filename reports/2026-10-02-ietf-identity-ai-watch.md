# IETF Identity + AI Standards Watch

Date: 2026-10-02

## Read now

- **draft-anandakrishnan-rats-ptv-agent-identity-01** (new-draft, score 28, trust_infrastructure) [none]: [The Prove-Transform-Verify (PTV) Protocol for Attested Agent Identity](https://datatracker.ietf.org/doc/draft-anandakrishnan-rats-ptv-agent-identity/) — This document describes the Prove-Transform-Verify (PTV) protocol for
   hardware-anchored attestation of AI agent identity.  PTV enables an
   agent to prove, at exercise time, that it is bound to an enrolled
   attestation key and an authorized configuration, without exposing
   model weights or inference inputs.

   PTV is a thin request/response profile over the RATS architecture
   (RFC 9334) and the Entity Attestation Token (RFC 9711).  It does not
   replace workload identifiers such as SPIFFE or WIMSE.  It does not
   attest behavioral continuity; behavioral continuity is a separate
   requirement class that relying parties need to treat as such.

   This revision is intended as Experimental.  It defines a common CBOR/
   CDDL message set, four message types, a COSE-based message protection
   rule, an informative EAT claim mapping, and a threat model that
   separates identity binding integrity from behavioral continuity.
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
- **draft-fane-opena2a-aip-03** (new-draft, score 26, adjacent_watchlist) [none]: [OpenA2A Agent Identity Protocol (AIP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aip/) — This document defines the OpenA2A Agent Identity Protocol (OpenA2A
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
- **draft-wang-jep-profiles-01** (new-draft, score 24, authorization) [none]: [JEP Profiles and Interoperability](https://datatracker.ietf.org/doc/draft-wang-jep-profiles/) — This document defines a profile model and optional interoperability
   bindings for the Judgment Event Protocol (JEP) [JEP].  JEP-Core
   defines a narrow signed event protocol.  Profiles define deployment-
   specific rules for actor identifiers, key resolution, actor binding,
   credentials, authorization context, attestation, freshness, audience,
   replay-related mechanisms, archival evidence, chain interpretation,
   and policy integration without changing JEP-Core semantics.

   Profiles are optional.  A JEP-Core implementation MUST NOT require
   DID, Verifiable Credentials, X.509, OAuth, OpenID Connect, RATS,
   blockchain anchoring, HJS, JAC, a particular AI platform, or any
   other optional profile for Core conformance.
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
- **draft-sharif-agent-audit-trail-06** (new-draft, score 23, core_identity) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
   AI agent systems.  The Agent Audit Trail (AAT) defines a
   JSON-based record structure with mandatory fields for agent
   identity, action classification, outcome tracking, and trust
   level reporting.  Records are linked via tamper-evident hash
   chaining using SHA-256 per RFC 8785, with optional ECDSA
   signatures for non-repudiation.

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

   This revision (-04) adds algorithm agility for post-quantum
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
- **draft-mcguinness-oauth-client-attesters-00** (new-draft, score 19, authorization) [none]: [OAuth 2.0 Client Attester Endorsement](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-client-attesters/) — OAuth 2.0 Attestation-Based Client Authentication requires an
   authorization server to trust the attester that makes statements
   about a client instance, but does not define how a client identifies
   the attesters authorized to attest for it.  This specification
   defines a client metadata parameter, usable by registered clients and
   in Client ID Metadata Documents, that names the endorsed attesters
   and the locations of their verification keys.  It defines how an
   authorization server validates endorsements and processes their
   withdrawal while retaining control over whether to trust them.  It
   introduces no new credential or client authentication method.
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
- **draft-borthwick-wallet-state-attestation-01** (new-draft, score 18, verifiable_claims) [none]: [Wallet State Attestation: Signed Booleans about On-Chain State](https://datatracker.ietf.org/doc/draft-borthwick-wallet-state-attestation/) — This document defines Wallet State Attestation: a primitive in which
   an issuer reads on-chain state for a wallet address, evaluates one or
   more operator-defined conditions, and returns a cryptographically
   signed boolean (or structured fact profile) that any verifier can
   check offline using a published JWKS endpoint.  The primitive enables
   condition-based access decisions without identity presentation,
   credential exchange, or contact with the issuer at verification time
   beyond a copy of its published key set and the documentation that
   accompanies it.  This document describes the request and response
   surface, the signing algorithm posture, the JWKS discovery pattern,
   and the security and privacy considerations of the primitive.  It
   does not define a new wire protocol; rather, it profiles existing
   IETF building blocks (JWT, JWKS, JOSE) for the wallet-state-
   attestation use case.
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
- **draft-tulshi-oauth-transactional-access-tokens-00** (new-draft, score 18, authorization) [none]: [Transactional Access Tokens](https://datatracker.ietf.org/doc/draft-tulshi-oauth-transactional-access-tokens/) — OAuth 2.0 access tokens are typically scoped to a session rather than
   to a transaction.  They carry no transaction identifier and no
   context beyond scope.  This document defines Transactional Access
   Tokens: a profile of JSON Web Token (JWT) access tokens that carries
   a transaction identifier and authorization server-asserted
   transaction context, has a very short lifetime, and is audienced to a
   single resource server.  Transactional Access Tokens align with the
   claims and semantics of OAuth Transaction Tokens, so that transaction
   context can flow from the authorization server to a resource server
   and onward into that resource server's trust domain.  A primary use
   case is task-scoped authorization of AI agents, where the
   authorization server makes a fresh policy decision for each
   transaction.
- **draft-uppalapati-wimse-pq-agent-identity-00** (new-draft, score 18, core_identity) [none]: [Post-Quantum Requirements for Software and AI Agent Identity](https://datatracker.ietf.org/doc/draft-uppalapati-wimse-pq-agent-identity/) — A delegation record retained as evidence must remain verifiable long
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
- **draft-mih-scitt-agent-action-capsule-05** (new-draft, score 17, trust_infrastructure) [none]: [An Agent Action Capsule Profile for SCITT](https://datatracker.ietf.org/doc/draft-mih-scitt-agent-action-capsule/) — This document defines a SCITT statement profile for recording what an
   AI agent did: the Agent Action Capsule.  A Capsule is a digest-
   committed record of one agent action carrying its verdict-level
   disposition (executed, blocked, denied, errored, timed out), the
   deterministic constraints that were evaluated, the effect that was
   committed together with a confirmed-effect binding that distinguishes
   a dispatched attempt from an observed result, and an honest human-in-
   the-loop flag.  Capsules are identified independently of signing and
   MAY be authenticated by one or more COSE_Sign1 Producer Envelopes.
   Its Capsule ID can separately be made transparent by registration in
   a SCITT Transparency Service [I-D.ietf-scitt-scrapi].  A Capsule is
   recorded on every verdict, including refusals: a blocked or denied
   Capsule is the auditor-grade evidence that a gate worked.
- **draft-schrock-action-evidence-boundary-07** (new-draft, score 17, core_identity) [none]: [The Action Evidence Boundary for Consequential Agent Effects](https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/) — Consequential agent actions can cross identity, transport,
   authorization, policy, and execution systems.  Each system can
   produce a valid artifact while the executor still lacks a safe rule
   for joining the artifacts to the exact effect, consuming one-time
   authority, and handling an uncertain outcome.  This document defines
   the Action Evidence Boundary (AEB), an executor-side processing model
   for that lifecycle.

   AEB requires native artifact verification, exact-action binding, a
   relying-party authorization decision, durable atomic consumption or
   reservation, provider entry, closed effect outcomes, and
   authenticated reconciliation.  One grant of native authority is
   identified by a relying-party-pinned authority namespace, which
   defaults to its issuer, and its native authorization identifier, so
   rewrapping or relabelling the grant cannot make it spendable twice.
   A durable same-action fence refuses a new attempt for an action whose
   earlier attempt is still in flight or uncertain, whatever evidence
   path admits it and even when fresh authority is presented.  An
   attempt that stopped before provider entry is released only with
   proof that it never entered.  AEB also specifies what a gateway
   attests, and what the boundary verifies, when a native authorization
   result is handed to a separate effect boundary.  Canonical Action
   Identifier (CAID) matching is used when independently encoded native
   representations must be joined.  Authorization Evidence Chain (AEC)
   evaluation is used when local policy requires multiple evidence legs.
   A native authorization decision accepted and enforced by the effect-
   owning policy enforcement point (PEP) does not require a second
   policy decision point (PDP).  AEB defines no receipt or token format,
   no policy language, no universal evidence taxonomy, and no new
   registry.  Native workload credentials, OAuth artifacts, AuthZEN
   decisions, Agent Payments Protocol (AP2) mandates, message
   signatures, permits, authorization receipts, and status mechanisms
   retain their own semantics and, where the native protocol defines
   one, their own verifiers.
- **draft-schrock-ep-authorization-evidence-chain-07** (new-draft, score 17, authorization) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — Consequential agent actions can produce heterogeneous identity,
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
- **draft-wang-jep-action-mandate-profile-02** (new-draft, score 17, core_identity) [none]: [JEP Action Mandate Profile (JEP-AMP)](https://datatracker.ietf.org/doc/draft-wang-jep-action-mandate-profile/) — This document defines JEP Action Mandate Profile 2 (JEP-AMP-2), a
   profile of the Judgment Event Protocol (JEP) [JEP].

   JEP-AMP-2 specifies how a JEP Delegation event can express a bounded,
   verifiable, terminable, and auditable mandate for an agent, human,
   organization, workflow, or system to attempt an action on behalf of a
   principal.

   JEP-AMP-2 does not redefine JEP-Core event verbs, Event Identity,
   Event Hash, signature semantics, validation checks, identity systems,
   credential systems, legal liability, payment clearing, or global
   authorization validity.  It defines a signed Action Mandate
   Descriptor and profile-level rules for evaluating mandate validity
   under an explicit trust, policy, domain, and relying-party context.
- **draft-ni-wimse-ai-agent-identity-03** (new-draft, score 16, agent_identity) [none]: [WIMSE Applicability for AI Agents](https://datatracker.ietf.org/doc/draft-ni-wimse-ai-agent-identity/) — This document discusses WIMSE applicability to Agentic AI, so as to
   establish independent identities and credential management mechanisms
   for AI agents.  It also discusses mechanisms for cryptographically
   binding an AI agent identity to an accountable user or organization.
- **draft-schrock-ae-challenge-08** (new-draft, score 16, authorization) [none]: [An Authorization Evidence Challenge for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ae-challenge/) — When a relying party refuses a consequential agent action because
   authorization evidence is missing, stale, not verified, not accepted
   under its trust inputs, or not bound to the exact action, the agent
   needs a machine-readable description of what remains necessary.  This
   document defines a transport-neutral Authorization Evidence Challenge
   data model bound to the relying party's exact action.  The challenge
   identifies outstanding evidence requirements, freshness and status
   constraints, acceptable presentation profiles, and retry state.  It
   authorizes nothing, transfers no admission ownership, and provides no
   promise that a later request will execute.

   The document also defines an HTTP challenge-response carrier using
   403 Forbidden and RFC 9457 Problem Details, and describes an
   informative gateway-handoff illustration for DMSC-style federation.
   The gateway illustration communicates evidence requirements; it does
   not solve conserved admission or double-admission across
   independently operated gateways.

   A challenge can synchronize corrected retries and amplify load.  The
   core therefore defines optional retry timing with per-challenge
   jitter, and the HTTP carrier maps its lower bound to Retry-After.
   Retry timing controls presentation attempts only; it does not
   authorize the action or make an uncertain action safe to repeat.

   Single-use processing also places state on the refusal path.  The
   core therefore requires bounded outstanding and replay state, fail-
   closed behavior when state cannot be claimed, and retention of live
   replay records until they are no longer security-relevant.  Nonce
   claim and refusal-path capacity reservation are one atomic owner-side
   transition before native evidence verification, and a binding
   capacity refusal reveals no remaining evidence requirements.  In a
   sharded replay domain, only the authoritative owner can classify a
   nonce as already claimed; inability to reach that owner is
   unavailability, not replay.

   An optional evaluation-lineage profile carries an authenticated
   issuer statement about one evaluation of a claimed presentation.  It
   binds the predecessor challenge, presentation, action, policy,
   evaluation semantics, and any successor-challenge reference.  A
   recipient that retains authenticated artifacts can distinguish an
   earlier unsatisfied result, whether or not its evaluation completed,
   from a later result.  The profile carries no authority, does not
   prove challenge consumption, ordering, completeness, or non-omission,
   and makes no claim that an action was admitted or executed.
- **draft-wang-jep-judgment-event-protocol-07** (new-draft, score 16, core_identity) [none]: [Judgment Event Protocol (JEP)](https://datatracker.ietf.org/doc/draft-wang-jep-judgment-event-protocol/) — This document defines the Judgment Event Protocol (JEP), a verifiable
   event format for judgment-related statements in human,
   organizational, software, and autonomous agent systems.

   JEP specifies four Core event verbs: Judgment (J), Delegation (D),
   Termination (T), and Verification (V).  It defines a signed JSON
   event structure, stable event identity, signature verification over
   JSON Canonicalization Scheme (JCS) canonicalized payloads, a detached
   JSON Web Signature (JWS) baseline profile, signed-artifact hash and
   reference semantics, independent validation checks, idempotent
   acceptance semantics, structured validation results, extension
   handling, trust-profile interfaces, and determinability boundaries.

   JEP-Core does not mandate a replay-protection mechanism.  An
   acceptance processor MUST apply the acceptance effect of a given
   Event Identity at most once within an acceptance domain.  Profiles
   MAY impose additional freshness or replay requirements.

   JEP-Core does not determine the substantive truth, authority,
   legality, policy consequence, causality, or external effect of the
   statements it carries.  It also does not require any specific
   credential, identity, AI platform, agent framework, transport, or
   blockchain system.
- **draft-wei-capability-language-core-00** (new-draft, score 16, adjacent_watchlist) [none]: [Capability Language Core](https://datatracker.ietf.org/doc/draft-wei-capability-language-core/) — This document defines the Capability Language Core (CLC), a minimal,
   executable language for describing what an agent is authorized to do.
   It defines the capability identifier grammar, the entailment relation
   between a grant and an operation, intersection of grants from
   multiple sources, the constraint model, and a deterministic decision
   function with stable reason codes and a three-valued verdict (allow,
   deny, allow_unresolved).

   The language is carrier-neutral: it defines what is evaluated, not
   how it is carried or trusted.  Trust models, native verification,
   execution lifecycle, and receipt or token formats are out of scope
   (Section 11).  Conformance is exercised by a published corpus of 123
   vectors and 1184 property cases; three implementations (Go, Python,
   TypeScript) that share an author pass both. *Implementation
   conformance and this document's claim of a conformance class are
   separate.* An implementation conforms to CLC-A when it meets the
   obligations Section 12 lists for that class, and it may claim that
   conformance on its own, whatever other implementations exist.
   Section 12 additionally sets a maturity bar for _this document's_
   claim — two independent implementations agreeing on verdict and
   reason.  That bar is *not* met here: as Section 12 states under
   "Independence of implementations", the three implementations named in
   the README share an author, so their agreement is a regression test
   for the text, not independent validation.  CLC-A is still claimed by
   this revision as the baseline authorization class, whose obligations
   are implementable and exercised by a published corpus; the
   independent-implementation threshold is recorded as unmet.  The
   evidence-side class CLC-E is *not* claimed: its relations, value
   grammar, reference implementation and corpus ship here.

   This revision also folds the delegation *containment* relation into
   the document (Section 13): Contains(parent, child) decides whether a
   child grant stays inside a parent's declared boundary — the single
   question a delegation chain asks at every hop that the core's
   entailment and intersection do not answer.  It ships with the
   conformance class *CLC-D* and its own corpus, is strictly additive,
   and changes no CLC-A verdict, reason code, or vector.  It absorbs the
   previously separate experimental containment extension, which is
   retired.
- **draft-ailex-vap-legal-ai-provenance-04** (new-draft, score 15, trust_infrastructure) [none]: [Verifiable AI Provenance (VAP) Framework and Legal AI Profile (LAP)](https://datatracker.ietf.org/doc/draft-ailex-vap-legal-ai-provenance/) — This document specifies the Verifiable AI Provenance (VAP) Framework,
   a cross-domain upper framework for cryptographically verifiable
   decision audit trails in high-risk AI systems, along with the Legal
   AI Profile (LAP), a domain-specific instantiation for legal AI and
   LegalTech systems.

   VAP defines common infrastructure including hash chain integrity,
   digital signatures, unified conformance levels (Bronze/Silver/Gold),
   external anchoring via RFC 3161 Time-Stamp Protocol and compatible
   transparency services (including IETF SCITT), a Completeness
   Invariant pattern guaranteeing no selective logging, standardized
   Evidence Pack format for regulatory submission, and privacy-
   preserving verification protocols.

   LAP extends VAP for the judicial AI domain, addressing unique
   requirements including attorney oversight verification (Human
   Override Coverage), three-pipeline completeness invariants for legal
   consultation, document generation, and fact-checking, tiered content
   retention with legal hold protocols for judicial discovery
   compliance, graduated override enforcement mechanisms, and privacy-
   preserving fields designed to maintain attorney-client privilege
   while enabling third-party auditability.
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
- **draft-bzb-rats-intel-poe-endorsements-02** (new-draft, score 14, trust_infrastructure) [none]: [A CoRIM Profile for Intel Platform Ownership Endorsements (POE)](https://datatracker.ietf.org/doc/draft-bzb-rats-intel-poe-endorsements/) — A Platform Ownership Endorsement (POE) is a signed statement that a
   specific Intel confidential-computing platform instance, identified
   by its Platform Instance Identity (PIID), belongs to a named owner.
   POEs let a Verifier bind the attested hardware identity from an Intel
   SGX or TDX platform to an operational owner (e.g., a Cloud Service
   Provider) during appraisal, giving a Relying Party a trustworthy
   owner identity -- without trusting the attestation service or any in-
   band claim from the platform itself.

   This document defines POE as a profile of the IETF Concise Reference
   Integrity Manifest (CoRIM) data model.
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
- **draft-schrock-canonical-action-identifier-04** (new-draft, score 14, core_identity) [none]: [The Canonical Action Identifier (CAID)](https://datatracker.ietf.org/doc/draft-schrock-canonical-action-identifier/) — Authorization, delegation, execution, and audit artifacts often
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
- **draft-sharif-attp-industrial-control-systems-02** (new-draft, score 14, core_identity) [none]: [ATTP for Industrial Control Systems: Cryptographic Agent Authentication in SCADA and IoT Environments](https://datatracker.ietf.org/doc/draft-sharif-attp-industrial-control-systems/) — This document defines an application profile of the Agent Trust
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
   safety-critical environments.  It further defines Autonomous
   Decision Assurance: where an AI agent executes a consequential
   command without per-action human review, the underlying decision
   MUST meet a stated reproducibility condition or be escalated to
   human oversight.  It adds smart-city and urban-infrastructure sector
   guidance and evidence-grade records for actions that may be legally
   contested.
- **draft-gilda-wimse-agent-audit-record-01** (new-draft, score 13, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-wimse-agent-audit-record/) — This document defines a record format for AI agent authorization
   decisions.  The format is one in-toto predicate type, signed inside a
   DSSE envelope.  It carries the seven minimum audit fields that the
   WIMSE AI Identity Management System framework requires, and two
   properties that make those fields checkable: a canonicalization
   contract, and both the authorization decision and the observed effect
   with a derived three-valued agreement between them.  That framework
   places the record format out of scope and takes no IANA action.  This
   document supplies the format.  It defines no policy.
- **draft-hardt-aauth-r3-00** (new-draft, score 13, authorization) [none]: [AAuth Rich Resource Requests (R3)](https://datatracker.ietf.org/doc/draft-hardt-aauth-r3/) — This document defines AAuth Rich Resource Requests (R3), an extension
   to the AAuth Protocol ([I-D.hardt-oauth-aauth-protocol]) that enables
   structured, vocabulary-based authorization for resource access.
   Resources publish R3 documents (content-addressed authorization
   definitions) and advertise vocabularies describing their operations.
   Agents request access using those vocabularies.  Auth tokens carry
   granted operations in the same vocabulary format, enabling resources
   to enforce authorization directly from the token.  Resources annotate
   individual operations in their vocabulary with the credential each
   requires, so an agent can plan before its first call.  R3 provides
   human-displayable context for consent decisions and content-addressed
   audit provenance via the r3_s256 hash in auth tokens.
- **draft-hillier-conformance-continuity-00** (new-draft, score 13, trust_infrastructure) [none]: [Conformance Continuity: Verifiable Attestation Across Baseline Supersession, Jurisdictional Recognition and Subject Mutation](https://datatracker.ietf.org/doc/draft-hillier-conformance-continuity/) — A conformance claim is a statement about a subject, made against a
   baseline, at a time.  Each of those three terms moves.  Baselines are
   superseded by their issuers.  Subjects present the same posture
   across jurisdictions whose baselines differ.  Subjects containing
   non-person entities mutate faster than the period any attestation
   covers.  A conformance record that cannot be carried across those
   boundaries, and cannot state what it failed to carry, decays into an
   assertion.

   This document specifies the Continuity Binding: a single structure
   that carries a verified conformance claim across a boundary while
   preserving the provenance of the evidence beneath it, attributing
   every equivalence judgement to a named party, and enumerating the
   residual that did not carry.  Three specialisations are defined.  The
   Transition Binding carries a claim across supersession of the
   governing baseline.  The Recognition Binding carries a claim between
   baselines of different issuers in concurrent force.  The Mutation
   Binding carries a claim across change in the composition of the
   subject itself, which is the ordinary condition of an environment
   operating non-person entities.

   The document specifies Baseline Profiles, Provenance Classes, the
   verdict taxonomy, the Verification Reconciliation Object,
   cryptographic agility requirements for records whose reliance
   outlives any single hardness assumption, and the registries that make
   baselines issued by any authority in any jurisdiction verifiable
   under one interoperable structure.  The evolution of the Australian
   Essential Eight Maturity Model into the Essentials series is used as
   the worked example throughout.
- **draft-morrison-mcp-dns-discovery-07** (new-draft, score 13, core_identity) [none]: [Discovery of Model Context Protocol Servers via DNS TXT Records](https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/) — This document defines a DNS-based mechanism for discovering Model
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
   precedent set by DKIM, SPF, DMARC, and MTA-STS.  Provisional
   registration of a companion alter: URI scheme is requested of IANA,
   and is not yet granted.
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
- **draft-zambo-aer1-09** (new-draft, score 13, core_identity) [none]: [AER-1: A Portable Execution Receipt for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-zambo-aer1/) — This document specifies AER-1, a small vocabulary for recording one
   AI agent tool call as a portable, independently checkable execution
   receipt.  A receipt identifies the execution, records when it
   happened, preserves the canonical bytes used for the output
   commitment, names the tool and caller scope, carries a provenance
   class, and resolves at a stable public URL.  The format separates
   what the system observed from claims about the outside world, and it
   separates provenance (who ran or reported the action) from the record
   itself.  A reference implementation is deployed, and its receipts are
   publicly verifiable without an account or token.  This revision adds
   workflow receipts: a verifiable record that binds an ordered
   sequence of step receipts to a single goal, with a Merkle root over
   the step sequence for tamper evidence.  The worked workflow
   example's Merkle root is computed with the leaf construction
   specified for that example.  This revision hardens the hash-chain
   entry digest: the digest now binds the entry's sequence number, job
   identifier, closing flag, receipt identifier, tool name, and
   provenance class alongside the output commitment, so relabeling or
   splicing attacks against chain metadata are detectable by
   recomputation.  The revision also states the honest limit of chain
   mechanics: truncation with re-linking is not detectable by the chain
   alone and needs an anchored endpoint commitment.  This revision
   adds guidance that the external commitment SHOULD bind the final
   chain entry digest, closing the last-entry gap where a rewritten
   final entry would otherwise still verify.  This revision names the
   two id conformance tiers, defines an optional external
   chain commitment artifact that the conformance kit checks,
   and corrects the description of member ordering to match the
   code-point serialization order the kit implements.
- **draft-ietf-emu-eap-ppt-04** (new-draft, score 12, core_identity) [emu]: [Extensible Authentication Protocol (EAP) Using Privacy Pass Token](https://datatracker.ietf.org/doc/draft-ietf-emu-eap-ppt/) — This document describes Extensible Authentication Protocol using
   Privacy Pass token (EAP-PPT) Version 1.  The protocol specifies use
   of the Privacy Pass token for client authentication within EAP as
   defined in RFC3748.  Privacy Pass is a privacy preserving
   authentication mechanism used for authorization, as defined in
   RFC9576.  EAP-PPT must be performed only in a tunnel-based EAP
   method.
- **draft-mcguinness-oauth-client-instance-id-00** (new-draft, score 12, core_identity) [none]: [Client Instance Identification for Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-client-instance-id/) — This specification defines an optional claims profile of OAuth 2.0
   Attestation-Based Client Authentication.  When selected, the profile
   requires an attester-assigned client instance identifier, scoped by
   default to the server that validates it, that remains stable across
   verified key changes, and adds continuity and privacy rules for that
   identifier.  Conveying instance context in tokens and introspection
   responses remains optional within the profile.  Authentication and
   proof methods follow the base specification.
- **draft-pidlisnyi-aps-04** (new-draft, score 12, core_identity) [none]: [Agent Passport System (APS): Verifiable Authority, Lifecycle, Enforcement, and Evidence for AI Agents](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/) — This document specifies the Agent Passport System (APS), a protocol
   for representing and evaluating authority exercised by AI agents.
   APS separates agent identity, represented principal, delegated
   authority, policy approval, admission to dispatch, observed results,
   and external effects.  It defines cryptographic identity and
   principal records, monotonic delegation, revocation and authority-
   lifecycle semantics, deterministic action and decision references,
   signed governed-action records, verifier outcomes, evidence
   resolution, profiles, and protocol bindings.

   APS defines how an enforcement boundary rechecks current authority
   before admitting an action to dispatch, and how a verifier
   distinguishes what a signed record establishes from claims that
   remain unresolved or external to the protocol.  Requirements are
   split into APS Core, which every conforming implementation carries,
   and Candidate features, which an implementation opts into by naming
   them in its claim, and most of the lifecycle and decision-to-effect
   material in this document is Candidate rather than Core.  Candidate
   features specify additional lifecycle and decision-to-effect behavior
   without making those features requirements of APS Core conformance.

   Implementation and conformance sections identify which requirements
   have exact conformance-vector coverage and which are implemented by
   the reference implementations.  APS does not treat a valid signature,
   receipt, or delegation chain as proof of external truth or of the
   absence of an out-of-band execution path.
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
- **draft-wang-cep-02** (new-draft, score 12, core_identity) [none]: [Co-Evolve Binding Profile (CEP): A JEP Profile for Evolution-Change Evidence Binding](https://datatracker.ietf.org/doc/draft-wang-cep/) — This document defines CEP-2, an optional profile of the Judgment
   Event Protocol (JEP) [JEP] for binding declared AI, model, agent,
   policy, tool-chain, or deployment changes to independently verifiable
   evidence and external anchor references.

   CEP-2 defines one critical JEP record-binding extension, one minimal
   Evolution-Change Record, Subject and Change semantics, digest-first
   evidence references, typed external anchor references, and
   independent CEP validation checks.  JEP remains authoritative for
   event verbs, Event Identity, Event Hash, signatures, references,
   extension processing, validation modes, and acceptance semantics.

   CEP-2 records declared change evidence.  It does not determine
   whether a change actually occurred, whether a system improved or
   degraded, whether a capability emerged, whether a change was
   authorized, safe, aligned, fair, lawful, approved, reversible, or
   acceptable, or whether any governance or regulatory process was
   satisfied.
- **draft-crovia-tacet-01** (new-draft, score 11, trust_infrastructure) [none]: [TACET: Verifiable Silence Proofs over a Sparse Merkle Transparency Map, with the PNX Profile for Proof of Non-Exfiltration](https://datatracker.ietf.org/doc/draft-crovia-tacet/) — Existing transparency logs prove presence: a certificate was logged,
   a binary was published, a key was registered.  TACET is a
   transparency map whose primary product is a portable, offline-
   verifiable proof of absence over time: that for a given subject, no
   record satisfying a public predicate existed in the map, and none was
   found on the subject's monitored public surfaces, across a contiguous
   range of epochs bounded below by a public randomness beacon and above
   by a Bitcoin block.  This document specifies the map (a depth-256
   sparse Merkle tree), the signed epoch sheet, surface snapshots and
   predicates, the delta-encoded silence proof with its three strength
   levels, the monotonicity rule under which silence never accrues
   without observation, the anchor check that needs no Bitcoin node, and
   the wrapping of proofs in Crovia Seal receipts.  It further specifies
   PNX, a profile that applies the same construction to the outbound
   traffic of an AI agent to prove that labelled assets were not
   exfiltrated during a run.
- **draft-hardt-aauth-bootstrap-02** (new-draft, score 11, core_identity) [none]: [AAuth Bootstrap Guidance](https://datatracker.ietf.org/doc/draft-hardt-aauth-bootstrap/) — This document provides informational guidance for agent providers
   (APs) on enrolling agents and issuing AAuth agent tokens defined in
   [I-D.hardt-oauth-aauth-protocol].  It covers per-platform key
   handling, optional platform attestation, agent identifier strategies,
   and refresh patterns.  The mechanisms described here are not
   normative protocol — they are common patterns that interoperable AP
   implementations can adopt or adapt.
- **draft-mih-agent-disclosure-envelope-00** (new-draft, score 11, trust_infrastructure) [none]: [Disclosure Envelope Profile for Agent Action Capsules](https://datatracker.ietf.org/doc/draft-mih-agent-disclosure-envelope/) — This document defines the Disclosure Envelope, an out-of-band wrapper
   structure for revealing the raw content behind a digest-only Agent
   Action Capsule field to a verifier, without altering the Capsule's
   own bytes or recomputing its capsule_id.  The Capsule profile
   [I-D.mih-scitt-agent-action-capsule] commits some fields as a
   [RFC8785]-canonicalized SHA-256 digest only — the content itself is
   never carried in the signed, registered record.  The initial
   disclosable fields are
   model_attestation.compute_attestation.agent_input_digest and
   .agent_output_digest.  A Disclosure Envelope wraps an unmodified
   Capsule alongside a sibling disclosures object; a verifier recomputes
   the JSON-DIGEST of each disclosed value using the same
   canonicalization the base profile already uses for capsule_id, and
   compares it to the digest committed inside the Capsule.  This
   mechanism is distinct from the per-field selective-disclosure profile
   [I-D.mih-scitt-agent-action-capsule-selective-disclosure]: that
   mechanism conceals and later reveals whole payload fields that would
   otherwise be carried in clear; this one reveals the content behind a
   field that was always present in clear, as a digest, from the moment
   the Capsule was signed.
- **draft-mih-agent-evidence-request-00** (new-draft, score 11, adjacent_watchlist) [none]: [An Interaction Model for Requesting Verifiable Evidence](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-request/) — Parties increasingly need to request verifiable evidence from a
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
- **draft-saha-aadp-04** (new-draft, score 11, core_identity) [none]: [The Agent Action Decision Protocol (AADP): Per-Action Authorization for AI Agents](https://datatracker.ietf.org/doc/draft-saha-aadp/) — The Agent Action Decision Protocol (AADP) separates per-action
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
- **draft-sibiryakov-ztds-protocol-02** (new-draft, score 11, adjacent_watchlist) [none]: [The Zero-Trust Data Sanitization (ZTDS) Protocol for Frontier Artificial Intelligence Ingestion](https://datatracker.ietf.org/doc/draft-sibiryakov-ztds-protocol/) — Zero-Trust Data Sanitization (ZTDS) defines a formal architectural
   standard and execution protocol for client-side, in-memory de-
   identification and re-identification across Generative Artificial
   Intelligence (GenAI), Retrieval-Augmented Generation (RAG), and
   autonomous agent workflows.

   Under ZTDS, sensitive information (including Personally Identifiable
   Information (PII), Protected Health Information (PHI), financial
   account numbers, and developer secrets) is intercepted and
   transformed into synthetic surrogate tokens strictly within volatile
   memory (RAM) of the originating client or private host node before
   network serialization.

   This protocol specification formalizes the threat model, the four
   core invariants, surrogate token syntaxes, cryptographic transport
   handoffs, and verification procedures required for interoperable,
   zero-subprocessor implementations.
- **draft-sirkkavaara-vaara-receipt-12** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
   recomputable record that binds a decision about an autonomous action
   to the evidence the decision was made on, and optionally to one or
   more external timestamp anchors.  The format is canonicalized with
   the JSON Canonicalization Scheme (JCS) so that any third party can
   recompute its digests and verify its signature without access to the
   issuer.  A decision and the execution receipt that answers it form
   one recomputable pair through the envelope's back link.

   The receipt's trust is root-agnostic: the same record is verifiable
   with or without a hardware trusted execution environment and is re-
   expressible as an IETF RATS Entity Attestation Result.  Downstream
   specifications (a payment rail, a compliance regime, a framework
   integration) define profiles that pin to a version of this document
   and add only their own evidence schema; they do not redefine the
   envelope.  The format described here is deployed, and its receipts
   are independently recomputable from public conformance vectors that
   ship with standalone checkers importing no issuer code.  The minimal
   profile is a governance decision over a single autonomous action,
   bound to the action's own intent with no external rail; it is the
   floor of the format, and a reference library offers a matching
   adoption floor at the API layer as a one-line decorator over the
   governed function.
- **draft-skyfire-oauth-kyapay-token-02** (new-draft, score 11, core_identity) [none]: [KYAPay Token](https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/) — This document defines a token format for agent identity and payment
   tokens in JSON Web Token (JWT) format.  Authorization servers and
   resource servers from different vendors can leverage this token
   format to consume identity and payment tokens in an interoperable
   manner.
- **draft-wang-coe-02** (new-draft, score 11, core_identity) [none]: [Cognition-Oriented Emergence (COE): A JEP Profile for Shared Observation and State-Claim Evidence](https://datatracker.ietf.org/doc/draft-wang-coe/) — This document defines COE-2, an optional profile of the Judgment
   Event Protocol (JEP) [JEP] for binding shared observation records and
   shared-state claims across heterogeneous agents, sensors, world
   models, simulators, and human-operated systems.

   COE-2 defines one critical JEP record-binding extension, two minimal
   digest-addressed record types, evidence-reference semantics, and
   independent COE validation checks.  JEP remains authoritative for
   event verbs, Event Identity, Event Hash, signatures, references,
   extension processing, validation modes, and acceptance semantics.

   COE-2 provides verifiable shared-observation infrastructure.  It does
   not determine objective world truth, factual causality, consensus,
   authorization, legal effect, fairness, trust weights, or regulatory
   compliance.  A valid COE result establishes only the cryptographic
   and structural properties actually checked under the selected
   profiles.
- **draft-mih-scitt-checkpointed-local-log-01** (new-draft, score 10, trust_infrastructure) [none]: [The Checkpointed Local Log (CLL)](https://datatracker.ietf.org/doc/draft-mih-scitt-checkpointed-local-log/) — Many systems emit individually signed records — receipts,
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
- **draft-morrison-binding-moment-envelope-03** (new-draft, score 10, core_identity) [none]: [The Briefing-and-Binding Envelope: A Delivery Contract for Agent-to-Principal Decision Moments with Dual-Veto Reconciliation](https://datatracker.ietf.org/doc/draft-morrison-binding-moment-envelope/) — This memo specifies the briefing-and-binding envelope: a delivery
   contract for the wire-level structure by which an artificial-
   intelligence agent surfaces a consequential decision to the human
   principal it acts for, and by which the principal commits, declines,
   amends, or rejects that decision.  The envelope carries eight named
   slots (a synopsis, findings, recommendations, an offer of detail, a
   question stem, a set of options each marked with its own reasoning, a
   single recommended option, and a pair of escape hatches) and is
   emitted as a structured field of a Model Context Protocol tool
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
   namespace of draft-morrison-identity-pronouns and the MCP tool
   surface of draft-morrison-org-alter-policy-provision.
- **draft-dogru-cedulon-core-02** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
   upon state-of-the-art HTTP 402, AP2 and credit card systems.  We
   specify a cryptographically secured payment reconciliation protocol
   using a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), and rail-extract reconciliation.
- **draft-helmprotocol-tttps-12** (new-draft, score 9, core_identity) [none]: [The TLS TimeToken Secure Protocol (TTTPS)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies TTTPS, an application-layer protocol for
   evaluating temporal evidence before an application accepts an event
   or performs a related state transition.  The protocol defines a fixed
   180-byte Proof-of-Time Record v2 containing context, freshness,
   integrity, issuer-authentication, and holder-authentication fields.

   When TLS 1.3 transport binding is selected, a separate holder binding
   proof is derived from TLS exporter output and holder key material.
   The proof is sent with, but is not part of, the 180-byte record.  The
   fixed-record GRG admission path is bounded with respect to peer count
   under declared frame and correction limits.

   TTTPS returns an explicit admission result before application state
   mutation.  Confidence and propagation-aware profiles are optional.
   This document does not define agent intent, audit record schemas, or
   transparency-log operation.
- **draft-morrison-compute-location-gate-02** (new-draft, score 9, core_identity) [none]: [The Compute-Location Gate: Provenance-Class Routing of Identity Inference with Wire-Layer Refusal of Unconsented Provenance Classes](https://datatracker.ietf.org/doc/draft-morrison-compute-location-gate/) — This memo specifies the compute-location gate: a mechanism by which a
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
   Informational.  The wire surface composes with DNS TXT discovery of
   Model Context Protocol servers, the ~handle namespace of the Identity
   Pronouns extension, and the organisational policy provision
   substrate; no new transport is introduced.
- **draft-nikolaichuk-scitt-continuity-receipts-01** (new-draft, score 9, trust_infrastructure) [none]: [Continuity Receipts: Registering the Recovery of a Stateful Asset as a Signed Statement in a Transparency Service](https://datatracker.ietf.org/doc/draft-nikolaichuk-scitt-continuity-receipts/) — A Transparency Service as defined by RFC 9943 registers Signed
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
- **draft-smith-opsawg-ai-network-governance-01** (new-draft, score 9, trust_infrastructure) [none]: [Governance Framework for AI-Mediated Autonomous Network Device Management](https://datatracker.ietf.org/doc/draft-smith-opsawg-ai-network-governance/) — This document defines a governance framework for systems that use
   artificial intelligence (AI) services, specifically large language
   models (LLMs), to autonomously detect, diagnose, and remediate
   operational anomalies on network devices.  As AI-driven automation
   moves from advisory tooling to closed-loop autonomous operation on
   production infrastructure, the industry lacks a common set of
   principles governing what such systems may and may not do.

   This framework establishes thirteen governance areas covering human
   authority, harm prevention, management plane protection, minimum
   necessary action, bounded autonomy, transparency, reversibility,
   graceful degradation, escalation, AI-specific constraints, startup
   safety, absolute prohibitions, and review processes.  It is intended
   to serve as a reference architecture for implementers building AI-
   mediated network management systems and for operators evaluating the
   safety properties of such systems.
- **draft-wang-ctp-definition-02** (new-draft, score 9, core_identity) [none]: [CTP/0: Cognitive Time Protocol -- Definition and Framework](https://datatracker.ietf.org/doc/draft-wang-ctp-definition/) — This document describes CTP/0, the definition layer of the Cognitive
   Time Protocol (CTP) family.  CTP/0 is an informational conceptual
   framework for naming, separating, comparing, and referencing time-
   related claims in AI and agent systems.

   CTP/0 defines terminology for profile-defined cognitive events,
   event-density claims, ordering claims, branching claims, sequential-
   computation evidence, and declared temporal-structure claims.

   CTP/0 does not define a wire protocol, message format, signature
   format, identity system, hash-chain protocol, governance process,
   physical theory of time, theory of consciousness, or legal-
   accountability framework.  Where verifiable records are required,
   CTP-compatible claims can be bound to external event, receipt,
   dependency-graph, observation, or change-evidence infrastructure.
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
- **draft-efstathiou-samp-agent-management-03** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
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
- **draft-hardt-aauth-events-00** (new-draft, score 8, core_identity) [none]: [AAuth Events](https://datatracker.ietf.org/doc/draft-hardt-aauth-events/) — This document defines AAuth Events — an event subscription and
   delivery mechanism for agents operating under the AAuth Protocol
   ([I-D.hardt-oauth-aauth-protocol]).  It specifies the subscribe token
   that agents use to register callbacks with resources, the event token
   that resources deliver when events fire, and the delivery path
   through the Agent Provider (AP).  AAuth Events enables agents to
   receive asynchronous notifications without requiring a public
   endpoint, using the cryptographic identity established by the AAuth
   Protocol.
- **draft-jackson-wimse-evaluation-03** (new-draft, score 8, trust_infrastructure) [none]: [Verifier-Side Evaluation Semantics for Delegated Authority Chains](https://datatracker.ietf.org/doc/draft-jackson-wimse-evaluation/) — Delegation chain specifications describe the shape of conveyed
   authority.  They leave the verifier's half of the exchange
   underdetermined.  Two verifiers can check the same chain, both report
   success, and enforce different policy.  This document states what a
   verifier must do: the explicit inputs evaluation depends on, how
   those inputs behave when their sources are stale or unavailable, and
   four rules that keep evaluation fail-closed.  The rules are drawn
   from the Grant & Autonomy Lifecycle (GAL) and Provenance & Trust
   Context (PTC) specifications and from a public reference
   implementation.
- **draft-liu-moq-live-agent-interaction-02** (new-draft, score 8, agent_identity) [none]: [Live Agent Interaction over MoQ](https://datatracker.ietf.org/doc/draft-liu-moq-live-agent-interaction/) — This document defines a protocol for real-time interactive
   communication between users and AI agents over Media over QUIC
   Transport (MOQT).  It specifies how streaming inference outputs (ASR
   transcripts, LLM tokens, TTS audio) map to the MOQT object model,
   defines a turn-taking control protocol with barge-in support for
   voice interactions, and establishes track structure conventions for
   live agent sessions.  The protocol operates as an application-layer
   profile on top of MOQT without modifying transport semantics.
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
- **draft-mo-cats-agent-service-characteristics-00** (new-draft, score 8, agent_identity) [none]: [AI Agent Service Characteristics and Their Implications for Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-mo-cats-agent-service-characteristics/) — AI agent services place a new class of demands on the network:
   sessions are long-lived and stateful, a single user request expands
   into multiple model invocations and tool calls, and the quality of
   the result depends jointly on the forwarding path, on the computing
   capability that is available at the selected site, and on whether the
   state that the agent needs is already present near that site.
   Computing-Aware Traffic Steering (CATS) already selects a service
   contact instance using a combination of computing and network
   metrics, but the CATS framework, metric, and data model documents
   were not written with agent services in mind. The document covers
   long-horizon tasks and their long-tail behaviour, discrete and
   distributed tool invocation, the cost of context growth and
   compression, the communication modes used by agent services, and the
   persistence of session state and memory. It reports measured
   distributions of model, state, and software artifact sizes, states
   what a CATS system must measure in order to steer this traffic, and
   identifies the information that a CATS system needs in order to
   select an instance for an agent service. This document does not
   define any protocol extension, metric encoding, or data model.
- **draft-morrison-org-alter-policy-provision-04** (new-draft, score 8, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — This memo specifies how an artificial-intelligence agent runtime,
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
   peer-protocol Identity Accord ceremony rather than to a meta-
   federation authority.  The memo is Informational.  The wire surface
   relies on the DNS-based discovery of draft-morrison-mcp-dns-discovery
   and the handle namespace of draft-morrison-identity-pronouns; no new
   transport is introduced.
- **draft-saha-aadp-bound-permit-00** (new-draft, score 8, authorization) [none]: [Action-Bound Permits for the Agent Action Decision Protocol (AADP): Carrying a Per-Action Decision Across a Trust Boundary](https://datatracker.ietf.org/doc/draft-saha-aadp-bound-permit/) — The Agent Action Decision Protocol (AADP) decides, per action,
   whether an agent's concrete request may proceed now, and assumes that
   the decision is consumed by an enforcement point on the same secured
   channel that issued it.  AADP identifies, as a planned extension, a
   permit that must be honoured across a trust boundary, and defines the
   "present_bound" obligation as its hook.  This document specifies that
   extension.  An action-bound permit is a permit signed by the decision
   point, bound to one recipient, one presenter key, one HTTP request
   and one decided action instance, and short-lived.  It composes with
   mandate formats such as the Agent Authorization Envelope, which carry
   what a recipient can evaluate for itself; the bound permit carries a
   decision the recipient cannot recompute, because it depends on state
   held by the issuer: cumulative budgets, live reservations, approval
   lifecycle and escalation.  The document adds scoped trust in issuers,
   a declared currentness mode, a mandate reference, a verification
   order with registered refusal reasons, and a confirmation the
   recipient signs.  It builds on existing specifications for every
   mechanism it can, and defines no new signature format, token format
   or policy language.
- **draft-sankarshan-agent-registry-protocol-04** (new-draft, score 8, core_identity) [none]: [Agent Registry Protocol](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/) — Software agents increasingly act on behalf of people and
   organizations across administrative and security boundaries.
   Existing discovery mechanisms can identify an endpoint or advertise a
   capability, but they do not by themselves provide a common way to
   resolve who operates an agent, the bounded authority under which it
   acts, whether that authority is current, or what evidence supports a
   reliance decision.

   This document defines the Agent Registry Protocol (ARPA), an HTTP and
   JSON protocol for publishing and resolving information about software
   agents, their operational deployments, typed relationships, bounded
   delegated authority, lifecycle status, and associated evidence.  ARPA
   separates identification, authentication, authorization, assurance,
   and lifecycle state.  Registration, successful authentication,
   capability advertisement, or proof verification does not by itself
   establish authority to perform an action.

   The protocol is designed to support deterministic fail-safe behavior
   when material authority information is revoked, suspended, expired,
   stale, conflicting, unavailable, or unverifiable.
- **draft-wang-jep-receipt-profile-00** (new-draft, score 8, core_identity) [none]: [JEP Receipt Profile: Verifiable Behavior and Evidence Receipts](https://datatracker.ietf.org/doc/draft-wang-jep-receipt-profile/) — This document defines JEP Receipt Profile 1 (JEP-RP-1), a minimal
   receipt and evidence profile for the Judgment Event Protocol (JEP)
   [JEP].

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
- **draft-ahuja-agent-routing-policy-01** (new-draft, score 7, authorization) [none]: [A Policy Grammar for Inter-Domain Agent Routing](https://datatracker.ietf.org/doc/draft-ahuja-agent-routing-policy/) — Agent tasks are delegated across organizational boundaries.  Existing
   work specifies how agents are identified, discovered, and described,
   states requirements for cross-domain isolation and authorization, and
   identifies the absence of a mechanism for expressing capability
   policy as a gap.  This document defines four policy attributes for
   inter-domain agent delegation, the declarations each attribute
   carries, and a validity condition on delegation chains that no party
   establishes by observing the whole chain.  Whether independently
   chosen policies converge is analysed in separate work.
- **draft-reddy-wimse-aggregate-signatures-01** (new-draft, score 7, trust_infrastructure) [none]: [Authenticated Provenance for WIMSE Delegation Chains](https://datatracker.ietf.org/doc/draft-reddy-wimse-aggregate-signatures/) — A request and its response, passing through a chain of workloads, may
   need authenticated provenance: proof of which workloads participated
   and whether each changed the message.  The base WIMSE HTTP Message
   Signatures mechanism ([I-D.ietf-wimse-http-signature]) authenticates
   one workload's message to its immediate recipient and does not
   provide this across a chain.  This document establishes authenticated
   provenance using per-hop digests of what each hop received and
   forwarded; this alone detects an omitted hop that changed the
   message.  An aggregate signature closes the remaining gap, a hop that
   forwards the message unchanged, and keeps the signature close to the
   size of one signature regardless of chain length.  The mechanism
   works with any aggregate signature scheme.

## Monitor

- **draft-ietf-ivy-entitlement-inventory-05** (new-draft, score 6, authorization) [ivy]: [A YANG Module for Entitlement Inventory](https://datatracker.ietf.org/doc/draft-ietf-ivy-entitlement-inventory/) — This document defines a YANG data model for managing software-based
   entitlements (licenses, authorization tokens, pay-as-you-go service
   credentials, etc) within a network inventory.  The model represents
   the relationship between organizational entitlements, network element
   capabilities, and the constraints that entitlements impose on
   capability usage.

   This data model enables operators to determine what capabilities
   their network elements possess, which capabilities are currently
   entitled for use, and what restrictions apply.  The model supports
   both centralized entitlement management and device-local entitlement
   tracking for physical and virtual network elements.
- **draft-ietf-lake-authkem-edhoc-01** (new-draft, score 6, core_identity) [lake]: [KEM-based Authentication for EDHOC](https://datatracker.ietf.org/doc/draft-ietf-lake-authkem-edhoc/) — This document specifies extensions to the Lightweight Authenticated
   Key Exchange (LAKE) protocol, formerly known as Ephemeral Diffie-
   Hellman over COSE (EDHOC), to provide resistance against quantum
   computer adversaries by incorporating Post-Quantum Cryptography (PQC)
   Key Encapsulation Mechanisms (KEMs) for both key exchange and
   authentication.  It defines a new signature-free KEM-based
   authentication method in which both parties authenticate using KEMs,
   enabling quantum-resistant authentication without relying on digital
   signatures when PQC KEMs, such as the NIST-standardized ML-KEM, are
   used.
- **draft-ietf-tls-trust-anchor-ids-06** (new-draft, score 6, adjacent_watchlist) [tls]: [TLS Trust Anchor Identifiers](https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/) — This document defines the TLS Trust Anchors extension, a mechanism
   for a TLS client or server to select a certificate to present based
   on the peer's trusted certification authorities.  It describes
   certification authorities more succinctly than the TLS Certificate
   Authorities extension.
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
- **draft-morrison-identity-pronouns-03** (new-draft, score 6, core_identity) [none]: [Identity Pronouns: A Reference-Axis Extension to ~handle Identity Systems](https://datatracker.ietf.org/doc/draft-morrison-identity-pronouns/) — This document defines an identity pronoun grammar as a reference axis
   orthogonal to the ~handle identity tier taxonomy defined in draft-
   morrison-mcp-dns-discovery and draft-morrison-identity-attributed-
   commits.  A pronoun is a session-scoped reference that resolves
   client-side to a concrete handle using local session state before any
   cryptographic, DNS, or federation operation.  The entity-class
   taxonomy (Sovereign, Bot, Instrument) is unchanged; this
   specification introduces Absolute vs Pronoun as an orthogonal axis.
   A pronoun MUST NOT appear in a capability token, in a DNS record, in
   an Accord signature, or in any inter-organisational protocol payload.
   The reference implementation defines a single Wave-1 pronoun, ~org,
   that resolves to the concrete handle of the organisation bound to the
   caller's current session.  An appendix defines a relative-path
   pronoun grammar (e.g. ~./architect, ~../weaver) as a non-normative
   design surface for future work.  The mechanism is provider-neutral,
   introduces no new cryptographic primitive, and adds no load to DNS,
   capability-token issuers, or federated resolvers.
- **draft-richer-oauth-oob-authcode-00** (new-draft, score 6, authorization) [none]: [Out of Band Authorization Code Delivery for OAuth 2.0](https://datatracker.ietf.org/doc/draft-richer-oauth-oob-authcode/) — This client-side process allows clients to use the authorization code
   grant type without the ability to host the redirect_uri themselves.
   This process creates a single copyable value that the resource owner
   can copy from a simple helper page into the waiting client
   application.
- **draft-rosenberg-vcon-redaction-00** (new-draft, score 6, agent_identity) [none]: [Use Cases and Requirements for Redaction in VCON](https://datatracker.ietf.org/doc/draft-rosenberg-vcon-redaction/) — The Virtualized Conversations (VCON) specification defines a
   standardized object format for representing multimedia conversations
   between users and AI agents.  Recent work has expanded VCON to enable
   it to been used to capture sessions with AI Agents as well, including
   tool calls, reasoning steps, model configuration and more.  This has
   also expanded the set of use cases and requirements for redaction of
   sensitive information from a VCON.  This document outlines use cases
   and requirements for redaction in VCONs.  This document is meant for
   discusssion purposes.  All of this document was written by the author
   and not by an LLM.
- **draft-sharma-oepb-01** (new-draft, score 6, adjacent_watchlist) [none]: [Offline Emergency Peer-to-Peer Broadcast Protocol](https://datatracker.ietf.org/doc/draft-sharma-oepb/) — This document specifies the Offline Emergency Peer-to-Peer Broadcast
   Protocol (OEPB), an experimental protocol for disseminating
   authenticated emergency alerts among unprovisioned devices over
   short-range peer-to-peer radios when network infrastructure is
   unavailable.  OEPB defines a compact 256-byte packet format with
   Ed25519 signatures; a transport abstraction over radios such as
   Bluetooth Low Energy, Wi-Fi Direct, and LoRa; per-message Trickle
   dissemination with a bounded number of retransmissions; a five-class
   weighted fair queuing scheme reflecting emergency triage priorities;
   and a trust model in which relays forward without verifying
   signatures, so that unauthenticated distress messages still propagate
   while receivers authenticate authority alerts.  A companion document
   defines the Bluetooth Low Energy transport binding.
- **draft-skyfire-oauth-amr-values-02** (new-draft, score 6, core_identity) [none]: [Additional Authentication Method Reference Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-amr-values/) — The JWT "amr" (Authentication Methods References) claim contains
   values conveying authentication methods used in the authentication.
   This specification defines additional Authentication Method Reference
   values beyond those already registered to represent additional
   authentication methods in use today.
- **draft-skyfire-oauth-id-verification-02** (new-draft, score 6, core_identity) [none]: [Identity Verification Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-id-verification/) — Knowing how a person's identity was verified can be important when
   making trust decisions.  This specification defines a claim and
   values for declaring how the person's identity was verified.
- **draft-song-emu-eapaka-pqc-sack-01** (new-draft, score 6, core_identity) [none]: [Bitstring-based Fragmentation Mechanism for EAP-AKA'](https://datatracker.ietf.org/doc/draft-song-emu-eapaka-pqc-sack/) — This document specifies an extension to the EAP-AKA' protocol by
   introducing a Bitmap-based Selective Acknowledgment (SACK) mechanism
   to the AT_FRAGMENT attribute.  This mechanism enables window-based
   transmission and precise recovery of lost fragments, optimizing
   fragment delivery during post-quantum identity concealment and
   authentication exchanges.
- **draft-templeman-scitt-framing-space-01** (new-draft, score 6, core_identity) [none]: [Measuring the CBOR Framing Space of COSE_Sign1 Data-Hash Pre-images](https://datatracker.ietf.org/doc/draft-templeman-scitt-framing-space/) — A signed statement conveyed as a COSE_Sign1 object may be serialized
   into many distinct byte sequences that all decode to the same data
   item.  Where a protocol identifies such a statement by a digest
   computed over its wire octets (referred to here as a data-hash), the
   identifier is sensitive to that framing while the signature over the
   statement is not.

   This document reports a measurement of the size of that class.
   Taking one 165-octet COSE_Sign1 object and re-emitting it under every
   combination of six CBOR encoding freedoms yields 64 distinct octet
   sequences.  All 64 carry an identical Sig_structure and therefore an
   identical, valid signature.  All 64 produce distinct data-hash
   values, with no collisions.  A stock CBOR decoder rejected none of
   them, and 31 were silently repaired into the original form by the act
   of being read.

   This document specifies nothing and proposes no wording.  It reports
   a measurement, publishes the reproduction recipe, and identifies the
   prior work that already addresses the problem it measures.
- **draft-vandemeent-rvp-continuous-verification-03** (new-draft, score 6, core_identity) [none]: [RVP: Real-time Verification Protocol for Requirement-Bound Evidence](https://datatracker.ietf.org/doc/draft-vandemeent-rvp-continuous-verification/) — This document defines RVP, a protocol for asking a bounded
   verification question, carrying that question through one of several
   possible verification mechanisms, and producing evidence that is
   bound to the exact question.  RVP separates five concerns that are
   often collapsed: the consumer policy that decides whether evidence is
   needed, the frozen evidence requirement, the lifecycle of the
   question, the carrier that obtains a response, and the later act of
   consuming the evidence.

   RVP does not grant authority, establish admission, or replace account
   authentication and session policy.  A successful result means only
   that the presented evidence satisfied the referenced requirement for
   the referenced question.  The consumer and target system remain
   responsible for deciding what, if anything, may happen next.

   The protocol supports local biometric checks, signed companion-device
   responses, WebAuthn, authenticated-session evidence, recovery
   standing, and future carriers without assigning ceremony semantics or
   authority to those carriers.  It is transport-independent and can
   operate locally without a central identity provider.
- **draft-wang-jac-03** (new-draft, score 6, core_identity) [none]: [JAC: Declared Dependency Graphs for JEP Events and Receipts](https://datatracker.ietf.org/doc/draft-wang-jac/) — This document defines JAC-2, a minimal declared-dependency graph
   profile for the Judgment Event Protocol (JEP) [JEP].

   JAC-2 binds a signed JEP event to zero or more declared parent
   dependencies through one critical JEP extension.  JEP Event Identity
   is used for logical JEP event dependencies; Event Hash is used only
   when an exact signed artifact must also be pinned.  Digest-addressed
   receipt or external records can be linked without becoming JEP
   events.

   JAC-2 defines dependency-link structure, partial-fragment semantics,
   cycle handling, chain validation checks, and non-inference
   boundaries.  It does not determine factual causality, responsibility,
   fault, authorization validity, workflow correctness, legal effect, or
   regulatory compliance.
- **draft-hardt-aauth-budgets-00** (new-draft, score 5, authorization) [none]: [AAuth Budgets](https://datatracker.ietf.org/doc/draft-hardt-aauth-budgets/) — This document defines AAuth Budgets, an extension to the AAuth
   Protocol ([I-D.hardt-oauth-aauth-protocol]) that carries a spending
   ceiling from a person server to a resource.  A budget is a ceiling on
   what an agent may consume at one resource, denominated in a unit the
   resource declares, carried as a claim in the auth token, and enforced
   by the resource.  Budgets are structurally parallel to scope: the
   agent asks, the resource offers, the person server and access server
   may narrow, and the auth token carries what was granted.  The
   extension adds a budget claim to resource tokens and auth tokens, a
   budget_consumed claim reporting what the presented auth token
   consumed, a budget_units field and a usage_endpoint to resource
   metadata, and an AAuth-Budget response header reporting what a
   request cost and what remains.
- **draft-intra-handshake-fail-53** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-92701 of CVSS 9.1, CVE-2026-92702 of CVSS 9.1, CVE-2026-33697 of CVSS 7.5, and 37 other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-33697],
   [EUVD-2026-16488], [CVE-2026-92701], [EUVD-2026-83194],
   [CVE-2026-92702], [EUVD-2026-83192] and several GitHub Security
   Advisories (GHSAs) which provide substantial technical evidence of
   how early attestation fails in practice, even *without physical
   access* to the desired machine.  Moreover, since continuous
   attestation is generally required [CSA-eBPF]
   [MITRE-Continuous-Attestation], early attestation adds *unnecessary
   complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA], [EarlyAttestationBleed] and the
   artifacts [Intra-handshake.fail-repo] in state-of-the-art formal
   analysis tool, ProVerif, under Apache-2.0 license for
   reproducibility, extensibility, and review, and have been
   acknowledged by the relevant stakeholders.  Currently, there are *two
   CVEs of CVSS 9.1, one CVE of CVSS 7.5, one GHSA of 9.0-10.0, one GHSA
   of CVSS 7.8, seven GHSAs of CVSS 7.4, and one GHSA of CVSS 6.3
   published against the broader early attestation covering all layers
   of the ecosystem up to the application*. The research papers on these
   are currently either under submission or being prepared for
   submission.  The artifacts of these papers will be shared with the
   community under Apache-2.0 license for reproducibility,
   extensibility, and review.  Based on our work, all except two
   implementations of early attestation have been archived, withdrawn,
   or moved to post-handshake attestation.  In our analysis
   [Intra-handshake.fail-repo], the remaining two implementations of
   early attestation -- Edgeless Systems Contrast and Meta's AI --
   remain vulnerable.  We recommend users to carefully evaluate their
   systems.
- **draft-mo-cats-agent-selection-mapping-00** (new-draft, score 5, agent_identity) [none]: [A Selection Mapping Framework for AI Agent Services in Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-mo-cats-agent-selection-mapping/) — The Computing-Aware Traffic Steering (CATS) framework selects a
   service contact instance for a service request by combining computing
   and network metrics that are distributed by CATS Service Metric
   Agents and CATS Network Metric Agents. For AI agent services, the
   request that arrives at the network is not a single unit of work: it
   is a session that expands into multiple steps, each of which may
   require a different capability, a different state, and a different
   path. This document describes a mapping framework that turns the
   characteristics of an agent step into (1) a set of hard constraints
   and (2) a per-dimension valuation over a three-dimensional resource
   view composed of forwarding, computing, and storage, and that feeds
   the resulting suitability of each candidate service contact instance
   into the existing CATS selection function. The framework introduces
   no new functional component.
- **draft-nestorov-scitt-p10-underdetermination-00** (new-draft, score 5, trust_infrastructure) [none]: [P10 Underdetermination Profile: Witness-Carrying Underdetermination Receipts for SCITT](https://datatracker.ietf.org/doc/draft-nestorov-scitt-p10-underdetermination/) — P10 defines a third-party-verifiable binding for
   NotDemonstrated(reason=underdetermined).  A conforming receipt
   carries two canonical witness worlds that are compatible with the
   same closed evidence set and produce different values for the same
   frozen claim.  The witness result is checked against committed
   profile semantics and bound into a SCITT Transparent Statement
   containing an in-toto Statement v1 predicate.  The result establishes
   underdetermination only relative to the declared profile and does not
   identify the actual world or establish either claim value as true.

## Adjacent / watchlist

- **draft-acee-lsr-ospfv3-deprecate-ah-00** (new-draft, score 3, core_identity) [none]: [Deprecation of the IPsec Authentication Header (AH) for OSPFv3 Authentication](https://datatracker.ietf.org/doc/draft-acee-lsr-ospfv3-deprecate-ah/) — RFC 4552 specifies the use of the IPsec Authentication Header (AH)
   and the Encapsulating Security Payload (ESP) to provide
   authentication and confidentiality for OSPFv3.  This document
   deprecates the use of AH for OSPFv3 and updates RFC 4552 accordingly.
   Operators are encouraged to use either ESP with NULL encryption, as
   specified in RFC 4552, or the OSPFv3 Authentication Trailer, as
   specified in RFC 7166.
- **draft-bokovoy-kitten-pkinit-pqc-02** (new-draft, score 3, core_identity) [none]: [Post-quantum Key Encapsulation with ML-KEM in Public Key Cryptography for Initial Authentication in Kerberos (PKINIT)](https://datatracker.ietf.org/doc/draft-bokovoy-kitten-pkinit-pqc/) — This document specifies extensions to the Kerberos PKINIT pre-
   authentication mechanism [RFC4556] [RFC8636] to support post-quantum
   key establishment using the Module-Lattice-Based Key-Encapsulation
   Mechanism (ML-KEM) algorithms defined in [FIPS203].

   The extensions define a new kemInfo arm in PA-PK-AS-REP, a KDCKEMInfo
   structure signed by the KDC, HKDF-based AS reply key derivation
   (HKDF-SHA-512 for ML-KEM), and downgrade-prevention rules.  The KEM
   path framework supports multiple KEM algorithms including ML-KEM,
   composite ML-KEM algorithms, and future KEM standards.
- **draft-bourbaki-6man-classless-ipv6-15** (new-draft, score 3, core_identity) [none]: [IPv6 is Classless](https://datatracker.ietf.org/doc/draft-bourbaki-6man-classless-ipv6/) — Over the history of IPv6, various classful address models have been
   proposed, none of which has withstood the test of time.  The last
   remnant of IPv6 classful addressing is a rigid network interface
   identifier boundary at /64.  This document removes the fixed position
   of that boundary for interface addressing.
- **draft-ehstand-oversight-acts-00** (new-draft, score 3, agent_identity) [none]: [Terminology for Human Oversight Acts in Automated and Agentic Systems](https://datatracker.ietf.org/doc/draft-ehstand-oversight-acts/) — Records produced by automated and agentic systems often represent
   human oversight as a single, undifferentiated event, such as an
   approval flag or a confirmation.  Such a record does not say whether
   the person was shown an output, determined whether a named property
   of it holds, chose a course of action, or permitted an action, and
   consumers of the record may treat a confirmation click as if it were
   a check.

   This document defines terms for four kinds of human oversight act
   (observation, check, decision, and release) and for related concepts:
   the oversight act and the overseer, the named property, standing
   authority, the oversight record, the undifferentiated approval, the
   check step, error detectability, the fail-open check step, and the
   check test.  It states what a record of each kind of act is, and is
   not, evidence of, and relates the terms to existing vocabularies.
   The document defines terminology only.  It specifies no protocol,
   data format, procedure, or measurement method.
- **draft-helmprotocol-deepspace-02** (new-draft, score 3, trust_infrastructure) [none]: [TTTPS Deep-space Profile: Propagation-Aware Time Attestation](https://datatracker.ietf.org/doc/draft-helmprotocol-deepspace/) — This document defines an experimental deep-space companion profile
   for the TLS TimeToken Secure Protocol (TTTPS).  It preserves the
   fixed Proof-of-Time core record and separates cryptographic validity
   from propagation-aware temporal applicability.  The profile binds
   physical context out of band, distinguishes one-way light time from
   two-way transaction delay, defines evidence and disposition
   boundaries, and composes peer aggregation with optional confidence
   qualification.  It does not claim flight performance, a live
   interplanetary mesh, or replacement of existing navigation or delay-
   tolerant networking standards.
- **draft-ietf-calext-jscalendarbis-21** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-cbor-serialization-09** (new-draft, score 3, adjacent_watchlist) [cbor]: [CBOR Serialization and Determinism](https://datatracker.ietf.org/doc/draft-ietf-cbor-serialization/) — RFC 8949 defines CBOR, a standard for serializing data types such as
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
- **draft-ietf-idr-bgp-rpki-yang-02** (new-draft, score 3, adjacent_watchlist) [idr]: [YANG Data Model for BGP about RPKI](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-rpki-yang/) — This document defines YANG data models for managing BGP information
   about Resource Public Key Infrastructure (RPKI).
- **draft-ietf-ivy-network-inventory-yang-20** (new-draft, score 3, adjacent_watchlist) [ivy]: [A Base YANG Data Model for Network Inventory](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-yang/) — This document defines a base YANG data model for reporting network
   inventory.  The scope of this base model is set to be application-
   and technology-agnostic.  The base data model can be augmented with
   application- and technology-specific details.
- **draft-ietf-jmap-calendars-31** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-masque-connect-ethernet-15** (new-draft, score 3, adjacent_watchlist) [masque]: [Proxying Ethernet Frames in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/) — This document specifies how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.
- **draft-ietf-nfsv4-acls-update-06** (new-draft, score 3, authorization) [nfsv4]: [ACLs within the NFSv4 Protocols](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-acls-update/) — This document is part of the set of documents intended to update the
   description of NFSv4 Minor Version One as part of the rfc8881bis
   respecification effort for NFSv4.1.  It describes the structure and
   function of NFSv4 Access Control Lists within NFSv4.0 and NFSv4.1.
   These minor versions and forthcoming ones define ACLs using an ACL
   structure derived from Windows ACLs.

   Support for other ACL approaches such as draft-POSIX ACLs remains an
   option that could be taken advantage of in later minor versions such
   as NFSv4.2.

   This document describes the structure of these Windows-derived NFSv4
   ACLs and their role in the NFSv4 security architecture.  While the
   focus of this document is on the role of these ACLs in providing a
   more flexible approach to file access authorization than is made
   available by the POSIX-derived authorization-related attributes, the
   potential provision of other security-related functionality based on
   ACLs is covered as well.

   Because of the failure of previous specifications to provide a
   satisfactory description of the authorization semantics of NFSv4
   ACLs, this document takes a different approach to many matters while
   maintaining compatibility with implementations based on previous
   specifications.

   When the resulting document is eventually published as an RFC, it
   will supersede the descriptions of ACL structure and semantics
   appearing in existing minor version specification documents for
   NFSv4.0 and NFSv4.1, thereby updating RFC7530 and RFC8881.
- **draft-ietf-opsawg-ipfix-path-segment-07** (new-draft, score 3, core_identity) [opsawg]: [Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/) — This document introduces new IPFIX Information Elements to identify
   the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS
   and SRv6 path identification.
- **draft-ietf-opsawg-ipfix-quic-header-01** (new-draft, score 3, trust_infrastructure) [opsawg]: [Export of QUIC Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-quic-header/) — This document defines IP Flow Information Export (IPFIX) Information
   Elements and export profiles for QUIC packet, header, frame,
   aggregate, and connection observations.  It distinguishes wire-
   visible information from values requiring version-specific parsing,
   packet-protection processing, or endpoint state, and reports
   observation provenance, processing outcome, and export completeness.
- **draft-ietf-opsawg-scheduling-oam-tests-10** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A YANG Data Model for Network Diagnosis using Scheduled Sequences of OAM Tests](https://datatracker.ietf.org/doc/draft-ietf-opsawg-scheduling-oam-tests/) — This document defines two YANG Data Models to support scheduled
   network diagnosis using Operations, Administration, and Maintenance
   (OAM) tests.  This document defines both 'oam-unitary-test' and 'oam-
   sequence-test' YANG modules to manage the lifecycle of network
   diagnosis procedures, intended for use by external management and
   orchestration systems (including SDN controllers and network
   orchestrators), rather than by individual network nodes.
- **draft-ietf-rtgwg-qos-model-16** (new-draft, score 3, adjacent_watchlist) [rtgwg]: [A YANG Data Model for Quality of Service (QoS) in IP Networks](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-qos-model/) — This document describes a YANG data model for management of Quality
   of Service (QoS) in IP networks.
- **draft-ietf-schc-access-control-01** (new-draft, score 3, adjacent_watchlist) [schc]: [SCHC Access Control](https://datatracker.ietf.org/doc/draft-ietf-schc-access-control/) — The SCHC framework defines an abstract view of the rules, formalized
   through a YANG Data Model.  In its original description, rules are
   static and shared by two endpoints.  This document defines
   augmentation to the existing Data Model in order to restrict the
   changes in the rule and, therefore, the impact of possible attacks.
- **draft-ietf-suit-update-management-16** (new-draft, score 3, core_identity) [suit]: [Update Management Extensions for Software Updates for Internet of Things (SUIT) Manifests](https://datatracker.ietf.org/doc/draft-ietf-suit-update-management/) — This document specifies extensions to the SUIT manifest format.
   These extensions allow a Manifest Author, update distributor, or
   device operator to more precisely control the distribution and
   installation of updates to devices.  These extensions also provide a
   mechanism to inform a management system of Software Identifier and
   Software Bill Of Materials information about an updated device.
- **draft-ietf-tcpm-tcp-ao-algs-08** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-ietf-teas-rsvp-auth-v2-02** (new-draft, score 3, core_identity) [teas]: [RSVP Cryptographic Authentication, Version 2](https://datatracker.ietf.org/doc/draft-ietf-teas-rsvp-auth-v2/) — This document provides an algorithm-independent description of the
   format and use of RSVP's INTEGRITY object.  The RSVP INTEGRITY object
   is widely used to provide hop-by-hop integrity and authentication of
   RSVP messages, particularly in MPLS deployments using RSVP-TE.  This
   document obsoletes both RFC2747 and RFC3097.
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
- **draft-irtf-cfrg-bbs-signatures-12** (new-draft, score 3, adjacent_watchlist) [cfrg]: [The BBS Signature Scheme](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/) — This document describes the BBS Signature scheme, a secure, multi-
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
- **draft-many-tiptop-snmp-profile-00** (new-draft, score 3, adjacent_watchlist) [none]: [SNMP Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-snmp-profile/) — Deep space communications involve long delays (e.g., Earth to Mars
   one-way delay is 4-24 minutes) and intermittent communications,
   because of orbital dynamics.  This document defines an SNMP profile
   for deep space.  The profile states, for each SNMP version and
   security model, what must be configured, provisioned, or changed, and
   maps their applicability to the deep space connectivity scenarios.
- **draft-mih-zhang-agent-disclosure-bundle-00** (new-draft, score 3, verifiable_claims) [none]: [AAC Evidence Bundle](https://datatracker.ietf.org/doc/draft-mih-zhang-agent-disclosure-bundle/) — This document defines the AAC Evidence Bundle, a portable
   presentation and verification container for an Agent Action Capsule
   and the records that make its evidentiary claim intelligible.  A
   permalink carries a bundle in its URL fragment, an offline HTML
   report carries a bundle in its shell, and a hosted report serves a
   bundle at its URL.  The bundle does not alter any enclosed Capsule.
   It declares its citation closure and any missing cited records,
   carries verified disclosure preimages as a bundle-level overlay,
   separates three different completeness claims, and permits
   independently specified extension blocks and neutral third-party
   countersignatures.
- **draft-sardar-rats-sec-cons-06** (new-draft, score 3, trust_infrastructure) [none]: [Guidelines for Security Considerations of RATS](https://datatracker.ietf.org/doc/draft-sardar-rats-sec-cons/) — This document aims to provide guidelines and best practices for
   writing security considerations for technical specifications for RATS
   targeting the needs of implementers, researchers, and protocol
   designers.  In particular, it discusses some of the 'bottom turtle'
   issues.  This is a work-in-progress, and the current version mainly
   presents an outline of the general security guidelines, baseline, or
   template for RATS that future versions will cover in more detail.
- **draft-templeman-scitt-measurement-capsule-00** (new-draft, score 3, trust_infrastructure) [none]: [Declared-versus-Observed Measurement Capsules: A Profile for Third-Party Measurement Statements in SCITT](https://datatracker.ietf.org/doc/draft-templeman-scitt-measurement-capsule/) — This document defines the measurement capsule: a small, deterministic
   JSON record in which a party that is neither the subject of a claim
   nor a participant in the action it concerns records what the subject
   declared, what the measuring party observed, and the difference
   between the two.  A capsule carries digests of its evidence, a
   measurement state in which "could not be checked" is a first-class
   outcome, and no decision, approval or authorisation.  Capsules are
   identified by the SHA-256 of their JCS serialisation and batched
   under an RFC 9162 Merkle Tree Hash.  The document describes their
   registration as SCITT Signed Statements (RFC 9943), how they refer to
   rather than restate receipts issued under other profiles, and one
   implementation, including where it does not yet match this profile.
- **draft-wang-jep-conformance-02** (new-draft, score 3, adjacent_watchlist) [none]: [JEP Conformance and Test Suite](https://datatracker.ietf.org/doc/draft-wang-jep-conformance/) — This document defines conformance classes, validation-result
   structure, schema requirements, test-vector categories, conformance
   assertions, reference-validator behavior, implementation disclosure,
   and interoperability testing guidance for the Judgment Event Protocol
   (JEP).  It is a companion to JEP-Core 0.7.

   This document does not redefine JEP-Core semantics.  Its purpose is
   to make JEP-Core 0.7 implementations testable and interoperable
   across languages, platforms, trust profiles, and deployment
   environments.  Conformance artifacts described by this document are
   derived from applicable normative specifications; tests, schemas,
   examples, and reference implementations do not independently create
   JEP-Core semantics.
- **draft-wang-jep-semantic-interoperability-01** (new-draft, score 3, core_identity) [none]: [Semantic Interoperability for the Judgment Event Protocol](https://datatracker.ietf.org/doc/draft-wang-jep-semantic-interoperability/) — This document defines semantic interoperability requirements for the
   Judgment Event Protocol (JEP) [JEP].

   JEP-Core defines signed J/D/T/V event semantics, Event Identity,
   Event Hash, references, validation checks, validation modes,
   extension processing, and idempotent acceptance.  This document does
   not redefine those mechanisms.  Instead, it defines the minimum
   shared interpretation rules required for independent systems to map,
   display, translate, and consume JEP events without silently changing
   their meaning.

   The core rule is that a JEP event records a signed protocol statement
   with defined verb semantics.  It does not by itself establish
   external truth, authority, legality, causality, completeness, policy
   consequence, or external effect.  Stronger conclusions require an
   explicitly selected profile or external evidence rule.
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
- **draft-besleaga-agentic-knowledge-wellknown-00** (new-draft, score 2, ignored_after_review) [none]: [The 'knowledge-linkset' Well-Known URI for Publishing Knowledge Artefacts](https://datatracker.ietf.org/doc/draft-besleaga-agentic-knowledge-wellknown/) — This document defines the "knowledge-linkset" well-known URI, at
   which a web origin publishes one link set describing the knowledge
   artefacts it makes available: graph serializations, a JSON-LD
   context, an agent-facing text file, a chunk export, a change ledger,
   and related resources.  Each artefact link may carry a SHA-256
   digest, expressed with the syntax of HTTP digest fields, so that a
   client can check that a retrieved artefact is the one the publisher
   described.  A profile URI identifies the conventions the link set
   follows.  The mechanism defines no new media type and no new link
   relation type: a page points at the resource with the existing
   "describedby" relation.  This document requests one well-known URI
   registration and records the fields of one profile URI registration
   that is to be requested separately.
- **draft-hillier-chorale-protocol-00** (new-draft, score 2, ignored_after_review) [none]: [The Chorale Protocol: Interception-Resistant Packet Transmission with Topology-as-Secret Ordering, Cascade-Integrity Witnessing, Polyglot Cover Packets, Per-Packet Time-Lock Sealing, and Multi-Jurisdiction Substrate Diversity](https://datatracker.ietf.org/doc/draft-hillier-chorale-protocol/) — This document specifies the Chorale Protocol, a secure packet
   transmission system with active integrity assurance, for use cases
   requiring resistance to interception, traffic analysis, replay,
   tampering, and retrospective decryption by adversaries with future
   quantum capability.  Chorale defines three confidentiality regimes,
   computational, everlasting and information-theoretic, and states the
   keying conditions under which each may be relied upon.  The
   information-theoretic regime requires an independently corroborated
   co-presence or quantum-key-distribution strand consumed as an
   unexpanded pad.  A session keyed by a derived keystream is
   computational and is reported as computational.  A conforming
   implementation fails closed and refuses to report a regime its keying
   does not support.  The protocol composes a per-session secret graph
   topology that determines packet ordering without transmitting any
   ordering information on the wire, cascade-integrity witnessing over
   the hidden topology, cover packets carrying valid-looking witnesses
   for fictional sessions, per-packet Verifiable Delay Function time-
   lock sealing, multi-source physical-entropy one-time pad composition
   with sovereign jurisdictional separation, multi-substrate flight
   requiring threshold reconstruction across diverse path types, and a
   tombstone ledger that makes pad reuse structurally impossible at the
   receiver.  This version introduces hash-family negotiation at
   handshake, raising the default hash function for HKDF key derivation,
   VDF time-lock sealing, and server-blind relay commitments from
   SHA-256 to SHA-512, with SHA3-512 admitted as a Keccak-family
   alternative for adversary-evolution- tolerant postures and SHA-256
   retained as a backward-compatible legacy mode for resource-
   constrained devices.  The protocol is intended for use by
   intelligence agencies, central banks, treaty-bound corridors,
   regulator-to-regulator communications, and other settings demanding
   the strongest practical confidentiality and integrity properties.
- **draft-ietf-lisp-site-external-connectivity-05** (new-draft, score 2, ignored_after_review) [lisp]: [LISP Site External Connectivity](https://datatracker.ietf.org/doc/draft-ietf-lisp-site-external-connectivity/) — This draft defines how to register/retrieve pETR mapping information
   in LISP when the destination is not registered/known to the local
   site and its mapping system (e.g. the destination is an internet/
   external site destination or scale-out/scale-across end point in
   backend networks of AI Infrastructure).

## Ignored after review

- **draft-acosta-deepspace-celestial-bodies-registry-03** (new-draft, score 0, ignored_after_review) [none]: [Defining a Celestial Bodies Reference Framework for Deep Space Internet Addressing](https://datatracker.ietf.org/doc/draft-acosta-deepspace-celestial-bodies-registry/) — This document highlights the operational framework within Deepspace/
   TIPTOP protocols to utilize an external, standardized reference
   framework for celestial objects, functioning as an equivalent to ISO
   3166 for interplanetary networking.  To avoid operational overhead
   and duplication of effort, this framework defers the definitions,
   naming, and tracking of celestial entities directly to the
   International Astronomical Union (IAU) and the Minor Planet Center
   (MPC).  This document outlines how these external identifiers guide
   hierarchical address allocation without requiring IANA to maintain a
   dedicated astronomical nomenclature registry.  The ultimate objective
   is to establish a clear definition of what constitutes a valid
   Celestial Body for networking purposes.
- **draft-brown-epp-deleg-03** (new-draft, score 0, ignored_after_review) [none]: [Extensible Provisioning Protocol (EPP) mapping for DELEG records](https://datatracker.ietf.org/doc/draft-brown-epp-deleg/) — This document describes an extension to the Extensible Provisioning
   Protocol ([STD69]) which allows clients to provision DELEG records
   for domain names.

About this draft

   This note is to be removed before publishing as an RFC.

   The source for this draft, and an issue tracker, may can be found at
   https://github.com/gbxyz/epp-deleg-extension.
- **draft-deshpande-secevent-http-multi-set-push-04** (new-draft, score 0, ignored_after_review) [sec]: [Push-Based Delivery For Multiple Security Event Tokens (SET) Using HTTP](https://datatracker.ietf.org/doc/draft-deshpande-secevent-http-multi-set-push/) — This specification defines how multiple Security Event Tokens (SETs)
   can be delivered to an intended recipient using HTTP POST over TLS.
   The SETs are transmitted in the body of an HTTP POST request to an
   endpoint operated by the recipient, and the recipient indicates
   successful or failed transmission via the HTTP response.
- **draft-dnoveck-nfsv4-rfc5662bis-08** (new-draft, score 0, ignored_after_review) [none]: [Network File System (NFS) Version 4 Minor Version 1 External Data Representation Standard (XDR) Description](https://datatracker.ietf.org/doc/draft-dnoveck-nfsv4-rfc5662bis/) — This document provides the External Data Representation Standard
   (XDR) description for Network File System version 4 (NFSv4) minor
   version 1.

   It includes protocol extensions made as part of the respecification
   effort for NFS Minor Version 1.

   It obsoletes and replaces RFC5662.
- **draft-duke-scone-scone-echo-03** (new-draft, score 0, ignored_after_review) [none]: [In-Band SCONE Reporting over QUIC](https://datatracker.ietf.org/doc/draft-duke-scone-scone-echo/) — The SCONE protocol relies on the receiver of SCONE packets to send
   bandwidth estimates back to the sender via unspecified application-
   layer messages.  In some cases, a peer might have SCONE receive
   capability at the QUIC layer but not implement the necessary
   application level functionality.  A new QUIC frame that directly
   reports the contents of received SCONE packets can address these use
   cases.  There are no changes in the interaction with SCONE Network
   Elements.
- **draft-filmroellchen-lunar-well-known-button-01** (new-draft, score 0, ignored_after_review) [none]: [The Well Known Button Information Specification](https://datatracker.ietf.org/doc/draft-filmroellchen-lunar-well-known-button/) — This document specifies the well-known URI /.well-known/button.json,
   which describes a web site's "buttons".  Buttons are usually 88x31
   pixel images representing the web site with text, logos, artwork, and
   animations.

   /.well-known/button.json files facilitate sharing buttons between web
   site owners and alleviate issues commonly encountered when doing so.
   By utilizing a standardized, machine-readable format, automated tools
   can also utilize the provided information.
- **draft-geng-grow-bmp-monitor-options-00** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for Monitoring Options (MO) Notification](https://datatracker.ietf.org/doc/draft-geng-grow-bmp-monitor-options/) — The BGP Monitoring Protocol (BMP) allows routers to export BGP RIB
   data and statistics to external collectors.  However, dynamic changes
   to a router's monitoring configuration—such as disabling specific
   Address Families or statistic counters—are not explicitly signaled to
   the collector.  Consequently, collectors cannot distinguish between a
   quiescent BGP state and a disabled monitoring feed, leading to data
   staleness and database pollution.

   This document defines a new BMP message type, the BMP Monitoring
   Options (MO) message.  It allows a BMP Sender to explicitly notify
   collectors of active, disabled, or dynamically altered reporting
   configurations across RIB types and statistics streams.
- **draft-geng-grow-bmp-rr-sync-00** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for Non-Disruptive RIB View Synchronization](https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rr-sync/) — The BGP Monitoring Protocol (BMP) provides full visibility into BGP
   Routing Information Base (RIB) state across routers and collectors.
   However, transient network faults, process restarts, or buffer
   overflows can cause data inconsistencies between the BMP sender's
   authoritative RIB and the collector's stored view.  Existing recovery
   requires tearing down BMP sessions or re-exporting all peers,
   introducing severe operational disruption.

   This document defines a new BMP message type, the BMP Route-Refresh
   message.  It encapsulated standard BGP Route-Refresh and Enhanced
   Route-Refresh semantics within BMP to enable fine-grained, non-
   disruptive, and targeted per-peer or per-AFI/SAFI RIB view re-
   synchronization.
- **draft-geng-idr-bgp-savnet-07** (new-draft, score 0, ignored_after_review) [none]: [BGP Extensions for Source Address Validation Networks (BGP SAVNET)](https://datatracker.ietf.org/doc/draft-geng-idr-bgp-savnet/) — Many source address validation (SAV) mechanisms have been proposed
   for preventing source address spoofing.  However, existing SAV
   mechanisms are faced with the problems of inaccurate validation or
   high operational overhead in some scenarios.  This document proposes
   BGP SAVNET by extending BGP protocol for SAV.  This protocol can
   propagate SAV-related information through BGP messages.  The
   propagated information will help edge/border routers automatically
   generate accurate SAV rules.  These rules construct a validation
   boundary for the network and help check the validity of source
   addresses of arrival data packets.
- **draft-gerke-publication-process-reform-09** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   The deterministic state-integrity constraints and automated
   milestones defined herein apply programmatically across the core
   processing streams already defined or established in the future.

   This document updates RFC 6359 and RFC 7841.
- **draft-ginsberg-lsr-hello-capability-01** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Hello Capability](https://datatracker.ietf.org/doc/draft-ginsberg-lsr-hello-capability/) — Advertisement of capabilities in Hellos is useful to allow support of
   optional features in establishing and maintaining adjacencies.  This
   document defines a new TLV to be sent in hellos to advertise such
   capabilities.
- **draft-gondwana-dkim2-debug-header-01** (new-draft, score 0, ignored_after_review) [none]: [A Diagnostic Header Field for DKIM2 Implementations](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-debug-header/) — Implementations of DomainKeys Identified Mail Signatures v2 (DKIM2)
   benefit from seeing extra debug information during the early
   deployment phase.

   This document is intended to help testers, and unlikely to be
   published.
- **draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext-00** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC with SigTag Extension](https://datatracker.ietf.org/doc/draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext/) — This document describes a mechanism to reduce post-quantum
   cryptographic (PQC) network transmission overhead when using Merkle
   Tree Ladders (MTL) in DNS Security Extensions (DNSSEC).  This
   document refers to this as SigTag and describes the use of EDNS(0) to
   enable its use.  SigTag allows a client to indicate its knowledge of
   a specific MTL ladder.  The DNS server can then use this signal to
   determine if it can omit the full underlying signature in its
   response, thereby reducing the message payload.
- **draft-helmprotocol-confidence-02** (new-draft, score 0, ignored_after_review) [none]: [Oracle Confidence Gating for TTTPS: G-Score, Correlation-Aware von Neumann Confidence, and AdaptiveSwitch](https://datatracker.ietf.org/doc/draft-helmprotocol-confidence/) — This document specifies an optional confidence layer for the TLS
   TimeToken Secure Protocol (TTTPS) [TTTPS].  It defines the G-Score, a
   normalized entropy measure of agreement concentration; an optional
   correlation-aware von Neumann extension; the InsufficientKnowledge
   signal; and the AdaptiveSwitch state machine over TURBO and FULL.
   The confidence layer qualifies whether evidence justifies action.  It
   does not replace cryptographic integrity, define a wire format,
   allocate a codepoint, establish source independence, or require any
   core TTTPS implementation to compute confidence.
- **draft-hoffman-duj-06** (new-draft, score 0, ignored_after_review) [none]: [DNS Update with JSON](https://datatracker.ietf.org/doc/draft-hoffman-duj/) — It is common for service providers such as certificate authorities
   and social media providers to want users to update the users' zones
   to prove that they control those zones, or to add other features.
   Currently, service providers tell users to do this using human
   language describing the resource record type and data values to enter
   into the zone.  This document describes a text format, called "DNS
   update with JSON" or "DUJ", for such a service provider to give to a
   user, with the expectation that the user would copy and paste the
   text to their DNS operator to update the user's zone.  DNS operators
   who know how to handle DUJ strings will make the update process
   easier and more predictable for their users.
- **draft-hoffman-pq-dnssec-considerations-01** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Selecting Post-Quantum Algorithms for DNSSEC](https://datatracker.ietf.org/doc/draft-hoffman-pq-dnssec-considerations/) — This draft lists many of the considerations that the DNS community
   needs to balance when it is deciding which post-quantum algorithms to
   standardize for DNSSEC.

   This draft is definitely not meant to become an RFC.
- **draft-ietf-bier-bfd-12** (new-draft, score 0, ignored_after_review) [bier]: [BIER BFD](https://datatracker.ietf.org/doc/draft-ietf-bier-bfd/) — Point-to-multipoint (P2MP) BFD is designed to verify multipoint
   connectivity.  This document specifies the application of P2MP BFD in
   BIER network.
- **draft-ietf-bier-source-protection-11** (new-draft, score 0, ignored_after_review) [bier]: [BIER (Bit Index Explicit Replication) Redundant Ingress Router Failover](https://datatracker.ietf.org/doc/draft-ietf-bier-source-protection/) — This document describes a failover in the Bit Index Explicit
   Replication domain with a redundant ingress router.
- **draft-ietf-bmwg-powerbench-03** (new-draft, score 0, ignored_after_review) [bmwg]: [Characterization and Benchmarking Methodology for Power in Networking Devices](https://datatracker.ietf.org/doc/draft-ietf-bmwg-powerbench/) — This document defines a standard mechanism to measure, report, and
   compare power usage of different networking devices under different
   network configurations and conditions.
- **draft-ietf-cats-metric-definition-13** (new-draft, score 0, ignored_after_review) [cats]: [CATS Metrics Definition](https://datatracker.ietf.org/doc/draft-ietf-cats-metric-definition/) — Computing-Aware Traffic Steering (CATS) is a traffic engineering
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
- **draft-ietf-cbor-edn-literals-28** (new-draft, score 0, ignored_after_review) [cbor]: [Concise Diagnostic Notation (CDN)](https://datatracker.ietf.org/doc/draft-ietf-cbor-edn-literals/) — This document formalizes and consolidates the definition of the
   Concise Diagnostic Notation (CDN) of the Concise Binary Object
   Representation (CBOR), addressing implementer experience.

   Replacing CDN's previous informal descriptions, it updates RFC 8949,
   obsoleting its Section 8, and RFC 8610, obsoleting its Appendix G.

   It also specifies registry-based extension points and uses them to
   support text representations such as of epoch-based dates/times and
   of IP addresses and prefixes.


   // (This cref will be removed by the RFC editor:) This revision -28
   // attempts to reflect various feature removals that have been
   // discussed on the mailing list, as a delta to -27.  Note that, with
   // the focus on the delta, this text is necessary somewhat
   // inconsistent.  The chairs decided not to include further editorial
   // improvements that could achieve a greater degree of consistency.
   // The text may be misleading as some of the explanatory sections no
   // longer fully reflect the technical content.  The text also does
   // not have WG input yet on any renaming decisions (CDN name, b1/t1
   // name).
- **draft-ietf-ccamp-fgotn-yang-02** (new-draft, score 0, ignored_after_review) [ccamp]: [YANG Data Models for fine grain Optical Transport Network](https://datatracker.ietf.org/doc/draft-ietf-ccamp-fgotn-yang/) — Fine grain Optical Transport Network (fgOTN) is a data plane
   technology, specified in ITU-T Recommendation G.709/Y.1331 (2020)
   Amd. 3, which complements existing OTN by providing bandwidth
   efficient support for sub-1Gbit/s services.

   This document defines YANG data models to describe the topology and
   tunnel information of an fgOTN network.
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
- **draft-ietf-hpke-hpke-05** (new-draft, score 0, ignored_after_review) [hpke]: [Hybrid Public Key Encryption](https://datatracker.ietf.org/doc/draft-ietf-hpke-hpke/) — This document describes a scheme for hybrid public key encryption
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
- **draft-ietf-idr-5g-edge-service-metadata-34** (new-draft, score 0, ignored_after_review) [idr]: [BGP Extension for 5G Edge Service Metadata](https://datatracker.ietf.org/doc/draft-ietf-idr-5g-edge-service-metadata/) — This draft describes a new Edge Metadata Path Attribute and some Sub-
   TLVs for egress routers to advertise the Edge Metadata about the
   attached edge services (ES).  The edge service Metadata can be used
   by the ingress routers in the 5G Local Data Network to make path
   selections not only based on the routing cost but also the running
   environment of the edge services.  The goal is to improve latency and
   performance for 5G edge services.

   The extension enables an edge service at one specific location to be
   more preferred than the others with the same IP address (ANYCAST) to
   receive data flow from a specific source, like a specific User
   Equipment (UE).
- **draft-ietf-idr-bgpls-inter-as-topology-ext-46** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extensions for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedures for distributing Border
   Gateway Protocol-Link State (BGP-LS) key parameters for inter-domain
   links between two Autonomous Systems (ASes).  It defines a new type
   within the BGP-LS Network Layer Reachability Information (NLRI) for
   an Inter-AS Link, along with three new Type-Length-Values (TLVs)
   descriptors for the BGP-LS Inter-AS Link.

   These extensions and procedures allow network operators to collect
   inter-domain interconnect information and automatically compute the
   inter-AS topology using information provided by the BGP-LS protocol.
- **draft-ietf-idr-fsv2-ip-basic-08** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Version 2 - for Basic IP](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/) — BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC
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
- **draft-ietf-intarea-extended-icmp-nodeid-06** (new-draft, score 0, ignored_after_review) [intarea]: [ICMP Message Extension for Originating Node Identification](https://datatracker.ietf.org/doc/draft-ietf-intarea-extended-icmp-nodeid/) — RFC5837 describes a mechanism for Extending ICMP for Interface and
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
- **draft-ietf-lisp-rfc6831bis-09** (new-draft, score 0, ignored_after_review) [lisp]: [The Locator/ID Separation Protocol (LISP) for Multicast Environments](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc6831bis/) — This document specifies the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP) architecture
   and protocols.  The document specifies how LISP multicast overlays
   operate over multicast and unicast underlays.  The mechanisms in this
   specification indicate how a signal-based approach using the PIM
   protocol can be used to program LISP encapsulators with a replication
   list in a locator-set, where the replication list can be a mix of
   multicast and unicast locators.  This document when approved
   obsoletes RFC6831
- **draft-ietf-lsr-l2-bundle-member-remote-id-07** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  For example,
   when performing topology management and bidirectional path
   computation for TE, it is essential to know the connectivity
   relationships among bundle members.

   This document describes how Open Shortest Path First (OSPF) and
   Intermediate System to Intermediate System (IS-IS) would advertise
   the remote interface identifiers for L2 bundle members.  The
   corresponding extension of BGP Link State (BGP-LS) is also specified.
- **draft-ietf-moq-transport-22** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-netconf-error-registries-00** (new-draft, score 0, ignored_after_review) [netconf]: [Error List and Error Identities Registries for YANG-driven protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-error-registries/) — This document defines IANA registries for the YANG Protocol Error
   List and YANG Protocol Error Identities.
- **draft-ietf-nfsv4-uncacheable-directories-12** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable Dirent Metadata Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-directories/) — Network File System version 4.2 (NFSv4.2) clients may cache the file
   attributes returned by READDIR alongside each directory entry.  Such
   a cache is not invalidated by the directory's change attribute, which
   reflects changes to the directory and its entries but not writes to
   the files those entries name, so it can become stale when another
   client changes one of those files.  In some deployments this produces
   incorrect size and timestamp values often enough to be a problem.
   This document introduces an uncacheable dirent metadata attribute for
   NFSv4.2 that allows a server to identify a directory for which an
   honoring client enumerates by READDIR and reports each entry's
   attributes as that READDIR returned them, rather than from a value it
   held earlier.
- **draft-ietf-nmop-simap-concept-14** (new-draft, score 0, ignored_after_review) [nmop]: [SIMAP: Concept, Requirements, and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-nmop-simap-concept/) — This document defines the concept of Service & Infrastructure Maps
   (SIMAP) and identifies a set of SIMAP requirements and use cases.
   The SIMAP was previously known as Digital Map. SIMAP evolves the
   earlier 'Digital Map' concept by making explicit the ties between
   service and infrastructure layers, clarifying expected outcomes for
   operations and automation, and addressing ambiguity associated with
   the term 'digital.'

   The document intends to be used as a reference for the assessment of
   the various topology modules to meet SIMAP requirements.
- **draft-ietf-opsawg-ipfix-ecn-00** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of ECN Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-ecn/) — This document defines a set of IPFIX Information Elements for
   monitoring Explicit Congestion Notification (ECN), specifically in
   the context of the Low Latency, Low Loss, and Scalable Throughput
   (L4S) service.  These Information Elements allow network operators to
   observe ECN codepoint usage within L4S deployments and evaluate the
   corresponding traffic performance.
- **draft-ietf-pce-entropy-label-position-07** (new-draft, score 0, ignored_after_review) [pce]: [Path Computation Element Communication Protocol (PCEP) Extension for SR-MPLS Entropy Label Positions](https://datatracker.ietf.org/doc/draft-ietf-pce-entropy-label-position/) — The Entropy label (EL) can be used in the SR-MPLS data plane to
   improve load-balancing and multiple Entropy Label Indicator (ELI)/EL
   pairs may be inserted in the SR-MPLS label stack as per RFC8662.

   This document defines a set of extensions for Path Computation
   Element Communication Protocol (PCEP) to configure where in the label
   stack the ELI/EL pairs should be inserted in SR-MPLS network - the
   Entropy Label Positions (ELP).
- **draft-ietf-pim-gaap-25** (new-draft, score 0, ignored_after_review) [pim]: [Group Address Allocation Protocol (GAAP)](https://datatracker.ietf.org/doc/draft-ietf-pim-gaap/) — This document describes a design for a lightweight decentralized
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
- **draft-ietf-pim-multicast-over-srv6-01** (new-draft, score 0, ignored_after_review) [pim]: [Multicast over SRv6 networks](https://datatracker.ietf.org/doc/draft-ietf-pim-multicast-over-srv6/) — This document presents solutions for deploying multicast in SRv6
   networks.  It explores the use of the native IPv6 multicast data
   plane for multicast distribution.  The document discusses distributed
   control plane mechanisms, including PIM, and its integration with IGP
   Flex-Algo to optimize multicast delivery.  The document also
   addresses overlay multicast solutions for both the Global
   Table Multicast (GTM) and Multicast VPNs (MVPNs), utilizing IP-in-
   IPv6 encapsulation without requiring additional shim layers.
- **draft-ietf-radext-radiusdtls-bis-18** (new-draft, score 0, ignored_after_review) [radext]: [RadSec: RADIUS over Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://datatracker.ietf.org/doc/draft-ietf-radext-radiusdtls-bis/) — This document defines transport profiles for running RADIUS over
   Transport Layer Security (TLS) and Datagram Transport Layer Security
   (DTLS), allowing the secure and reliable transport of RADIUS
   messages.  RADIUS/TLS and RADIUS/DTLS are collectively referred to as
   RadSec.

   This document obsoletes RFC6614 and RFC7360, which specified
   experimental versions of RADIUS over TLS and DTLS.
- **draft-ietf-savnet-intra-domain-architecture-05** (new-draft, score 0, ignored_after_review) [savnet]: [Intra-domain Source Address Validation Architecture](https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/) — This document describes a generic architecture for intra-domain
   Source Address Validation (SAV).  It provides a common framework for
   developing new intra-domain SAV mechanisms and describes the
   conditions under which this architecture can improve SAV accuracy and
   operational efficiency with respect to existing intra-domain SAV
   mechanisms.
- **draft-ietf-schc-schclet-01** (new-draft, score 0, ignored_after_review) [schc]: [SCHClet - Modular Use of the SCHC Framework](https://datatracker.ietf.org/doc/draft-ietf-schc-schclet/) — This document introduces the concept of a SCHClet: a modular sub-
   function within the SCHC (Static Context Header Compression)
   framework.  Inspired by chiplet architectures in hardware design, a
   SCHClet encapsulates a specific SCHC function - such as compression,
   fragmentation, or acknowledgments - as a self-contained unit.  This
   modularization enables tailored implementations that avoid the
   overhead of deploying a full SCHC stack.

   By decomposing SCHC functionality into SCHClets, the framework
   becomes more adaptable, extensible, and suitable for a wider range of
   network environments - including, but not limited to, constrained
   networks.  A system using SCHClets remains compliant with the SCHC
   framework and can interoperate with a full SCHC implementation,
   provided compatible configuration parameters are used.

   Each SCHClet is defined by the SCHC Profiles and configuration
   parameters necessary for interoperability.  It operates within a
   single Stratum and a single SCHC Instance.  For example, a device may
   implement only the NoAck fragmentation mode as a standalone SCHClet,
   potentially with fixed parameters.  This modular approach simplifies
   development, reduces resource demands, and provides a framework for
   future extensibility of the SCHC architecture.
- **draft-ietf-spring-resource-aware-segments-20** (new-draft, score 0, ignored_after_review) [spring]: [Introducing Resource Awareness to SR Segments](https://datatracker.ietf.org/doc/draft-ietf-spring-resource-aware-segments/) — This document describes a mechanism to allocate network resources to
   one or a set of Segment Routing Identifiers (SIDs).  Such SIDs are
   referred to as resource-aware SIDs.  The resource-aware SIDs retain
   their original forwarding semantics, with the additional semantics to
   identify the set of network resources available for the packet
   processing and forwarding action.  This mechanism is applicable to
   both segment routing with MPLS data plane (SR-MPLS) and segment
   routing with IPv6 data plane (SRv6).
- **draft-ietf-spring-stamp-srpm-mpls-10** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as specified in RFC 8762,
   along with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths (including Segment Lists of SR-MPLS Policies, SR-MPLS
   IGP best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo)
   paths), as well as Layer-3 and Layer-2 services carried over those
   paths.
- **draft-ietf-spring-stamp-srpm-srv6-07** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths (including Segment Lists of SRv6 Policies, SRv6
   IGP best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths),
   as well as Layer-3 and Layer-2 services carried over those paths.
- **draft-ietf-teas-ns-ip-mpls-10** (new-draft, score 0, ignored_after_review) [teas]: [Realizing Network Slices in IP/MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-teas-ns-ip-mpls/) — Realizing network slices may require the Service Provider to have the
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
- **draft-ietf-v6ops-ipv6-app-testing-03** (new-draft, score 0, ignored_after_review) [v6ops]: [Testing Applications' IPv6 Support](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   software as a service providers on how to approach IPv6 testing in
   Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including "IPv6-
   only-strict" scenarios without any connectivity towards any relevant
   IPv4 endpoint.  It discusses common misconceptions about the degree
   to which operating systems and libraries can abstract IPv6 issues
   away and explains common regressions to avoid when deploying IPv6
   support.
- **draft-johnson-dtn-dtpc-00** (new-draft, score 0, ignored_after_review) [none]: [Delay-Tolerant Payload Conditioning (DTPC) Protocol Specification](https://datatracker.ietf.org/doc/draft-johnson-dtn-dtpc/) — This document specifies the Delay-Tolerant Payload Conditioning
   (DTPC) protocol.  DTPC is an end-to-end, connectionless, expandable
   application service protocol designed to operate directly above the
   Bundle Protocol (BPv7).  It provides transparent application data
   conditioning services across challenged networks, including
   controlled aggregation of Application Data Units (ADUs), application-
   specific elision, transmission-order tracking, end-to-end positive/
   negative acknowledgments, and duplicate suppression.  DTPC preserves
   the end-to-end principle across delay-tolerant networks where
   intermediate nodes execute store-and-forward operations.
- **draft-kaizer-dnsop-ml-dsa-mtl-dnssec-02** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC](https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/) — This document describes how to apply the Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a
   conservative post-quantum cryptographic algorithm for DNS Security
   Extensions (DNSSEC).  This combination is referred to as the ML-DSA-
   MTL Signature scheme.  This document describes how to specify ML-DSA-
   MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with
   SHAKE-128.
- **draft-koo-dtn-traceroute-eb-01** (new-draft, score 0, ignored_after_review) [none]: [Traceroute Extension Block for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-koo-dtn-traceroute-eb/) — This document defines a Traceroute Extension Block (TREB) for Bundle
   Protocol Version 7 (BPv7).  Each participating node along a bundle's
   path appends a hop-record containing its Node ID, the next hop it
   selected, the time of the recorded event, and link characteristics.
   The same block, copied into bundle status reports, returns traceroute
   data to the source.  The mechanism is opt-in and intended for
   designated diagnostic bundles on scheduled, bandwidth-constrained
   paths.  In delivery-report-only operation a single status report
   returns the full recorded path and also records its own return path,
   giving a round-trip trace.  Status report generation remains governed
   by RFC 9171.
- **draft-lehmann-idmefv2-https-transport-07** (new-draft, score 0, ignored_after_review) [none]: [Transport of Incident Detection Message Exchange Format version 2 (IDMEFv2) Messages over HTTPS](https://datatracker.ietf.org/doc/draft-lehmann-idmefv2-https-transport/) — The Incident Detection Message Exchange Format version 2 (IDMEFv2)
   defines a data representation for security incidents detected on
   cyber and/or physical infrastructures.

   This draft is maintained by the IDMEFv2 Task Force.  Please consult
   our website for more information. https://www.idmefv2.org

   The format is agnostic so it can be used in standalone or combined
   cyber (SIEM), physical (PSIM) and availability (NMS) monitoring
   systems.  IDMEFv2 can also be used to represent man made or natural
   hazards threats.

   IDMEFv2 improves situational awareness by facilitating correlation of
   multiple types of events using the same base format thus enabling
   efficient detection of complex and combined cyber and physical
   attacks and incidents.

   This document defines a way to transport IDMEFv2 Alerts over HTTPs.

   If approved this document would obsolete RFC4767.
- **draft-levine-dnsextlang-14** (new-draft, score 0, ignored_after_review) [none]: [An Extension Language for the DNS](https://datatracker.ietf.org/doc/draft-levine-dnsextlang/) — Adding new RRTYPEs to the DNS has required that DNS servers and
   provisioning software be upgraded to support each new RRTYPE in
   Master files.  This document defines a DNS extension language
   intended to allow most new RRTYPEs to be supported by adding entries
   to configuration data read by the DNS software, with no software
   changes needed for each RRTYPE.
- **draft-lozano-icann-registry-interfaces-27** (new-draft, score 0, ignored_after_review) [none]: [ICANN Registry Interfaces](https://datatracker.ietf.org/doc/draft-lozano-icann-registry-interfaces/) — This document describes the technical details of the interfaces
   provided by the Internet Corporation for Assigned Names and Numbers
   (ICANN) to its contracted parties to fulfill reporting requirements.
   The interfaces provided by ICANN to Data Escrow Agents and Registry
   Operators to fulfill the requirements of Specifications 2 and 3 of
   the gTLD Base Registry Agreement are described in this document.
   Additionally, interfaces for retrieving the IP addresses of the probe
   nodes used in the SLA Monitoring System (SLAM) and interfaces for
   supporting maintenance window objects are described in this document.
- **draft-many-lsr-power-group-04** (new-draft, score 0, ignored_after_review) [lsr]: [IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-many-lsr-power-group/) — [I-D.many-teas-power-steering] introduces a Power Conserving Path
   Placement Strategy (PCPPS).  When possible, PCPPS concentrates
   traffic onto a small set of network resources.  When traffic is
   concentrated onto a small set of network resources, other network
   resources become idle and can be powered down until they are needed
   again.  This conserves energy and reduces environmental impact.

   PCPPS uses information that is distributed by an IGP.  This document
   specifies the IS-IS encoding for that information.
- **draft-many-teas-rsvp-power-00** (new-draft, score 0, ignored_after_review) [none]: [Power Transition Framework for TE Resources](https://datatracker.ietf.org/doc/draft-many-teas-rsvp-power/) — Traffic-engineered networks are commonly provisioned for peak demand.
   However, during off-peak periods, some traffic-engineered resources
   in the network may be lightly used.  This leads to unnecessary power
   consumption.  A coordinated power transition can reduce power
   consumption while preserving the control-plane and traffic-
   engineering state needed to restore service safely.

   This document defines a generic power management framework for
   coordinating power-sleep and wakeup transitions between adjacent
   nodes.  It defines the roles, resource scope, procedures, collision
   handling, failure behavior, and traffic-engineering preservation
   requirements.  It then specifies an RSVP-TE signaling extension for
   supporting the power management framework.
- **draft-mnichols-protocols-not-the-internet-01** (new-draft, score 0, ignored_after_review) [none]: [Protocol Architects Are Not the Creators of the Internet](https://datatracker.ietf.org/doc/draft-mnichols-protocols-not-the-internet/) — TCP/IP standardized interoperability and end to end transport
   semantics.  The World Wide Web standardized publishing and retrieval.
   Neither TCP/IP nor the Web specifies, provisions, or enforces the
   path properties required for utility grade Internet operation at
   scale.

   This memo defines terminology to distinguish interoperability
   standards from utility grade operation and specifies operational
   requirements for "infrastructure activation": provisioned transport,
   interconnection strategy, routing policy control, redundancy,
   locality, continuous monitoring, incident response, and enforceable
   service accountability.  This memo proposes no protocol changes.
- **draft-newbold-atp-aturi-00** (new-draft, score 0, ignored_after_review) [none]: [The "at" URI Scheme](https://datatracker.ietf.org/doc/draft-newbold-atp-aturi/) — This document defines the "at" URI scheme, which is used to reference
   accounts and data records in the Authenticated Transfer Protocol.
- **draft-prz-lsr-ash-packets-06** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
- **draft-sayre-tppietf-00** (new-draft, score 0, ignored_after_review) [none]: [TPPIETF: The Proverbial Printer Impeding Encryption Task Forces](https://datatracker.ietf.org/doc/draft-sayre-tppietf/) — It is said to be in the basement.

   Despite decades of work by the Internet Engineering Task Force to
   develop, standardize, and promote transport layer security, global
   deployment remains incomplete.  This document investigates the
   primary obstacle to universal encryption: a class of legacy printing
   devices, often located in building basements, that are cited as
   justification for continued plaintext transmission.  This document
   provides a taxonomy of such devices, analyzes the rhetorical
   structure of printer-based encryption exemption claims, and proposes
   a framework for evaluating their validity.
- **draft-shabazz-http-x402-tswp-00** (new-draft, score 0, ignored_after_review) [none]: [The X402 Typed Settlement Wire Protocol (X402-TSWP)](https://datatracker.ietf.org/doc/draft-shabazz-http-x402-tswp/) — This document specifies the X402 Typed Settlement Wire Protocol
   (X402-TSWP), an application-layer extension to Hypertext Transfer
   Protocol status code 402 (Payment Required).  X402-TSWP defines
   machine-to-machine challenge-response headers, operational type
   discriminators, and deterministic multi-rail blockchain carrier
   grammars.  On parallel execution environments, X402-TSWP eliminates
   runtime regular-expression parsing in favor of byte-exact equality
   verification via instruction introspection, establishing atomic
   non-repudiation between web services, SWIFT ISO 20022 messages, and
   public ledger state transitions.
- **draft-sharma-oepb-binding-ble-01** (new-draft, score 0, ignored_after_review) [none]: [OEPB Transport Binding: Bluetooth Low Energy](https://datatracker.ietf.org/doc/draft-sharma-oepb-binding-ble/) — This document defines the Bluetooth Low Energy (BLE) Transport
   Binding Profile for the Offline Emergency Peer-to-Peer Broadcast
   Protocol (OEPB).  It specifies the advertising mode, fragmentation
   and reassembly scheme, service and characteristic UUIDs, and channel
   access rules required to carry OEPB packets over BLE 4.x and BLE 5.x
   physical layers.
- **draft-skyfire-oauth-aml-methods-01** (new-draft, score 0, ignored_after_review) [none]: [Anti-Money Laundering Methods Values](https://datatracker.ietf.org/doc/draft-skyfire-oauth-aml-methods/) — Financial regulations require application of Anti-Money Laundering
   (AML) and Countering the Financing of Terrorism (CFT) methods in many
   jurisdictions worldwide.  This specification defines a claim and
   values for declaring what AML/CFT methods were employed.
- **draft-smyslov-ipsecme-ikev2-psp-02** (new-draft, score 0, ignored_after_review) [none]: [Using the Internet Key Exchange Protocol Version 2 (IKEv2) for PSP Key Management](https://datatracker.ietf.org/doc/draft-smyslov-ipsecme-ikev2-psp/) — This document specifies how the Internet Key Exchange Version 2
   (IKEv2) protocol can be used for supplying keys for the PSP Security
   Protocol (PSP).
- **draft-song-fann-falcon-00** (new-draft, score 0, ignored_after_review) [none]: [FALCON: Fast Latency and Congestion Notification Using Reverse-Path In-Network Telemetry](https://datatracker.ietf.org/doc/draft-song-fann-falcon/) — This document describes FALCON (FAst Latency and COngestion
   Notification), a method that allows a traffic source to learn the
   queuing delay and congestion status of a path with a notification lag
   no greater than the one-way propagation delay from the congested node
   back to the source, which is at most about half of the baseline
   Round-Trip Time (RTT).  FALCON combines in-network telemetry and
   source routing: a forward packet records the path it traverses, and
   the receiver returns a high-priority packet that is source-routed
   along the exact reverse of that path, collecting the state of the
   forward-direction queues as it passes.  Where a hop-by-hop flow
   control mechanism is used, such as Priority-based Flow Control (PFC)
   or a backpressure mechanism for lossless WAN transport, the returned
   packet can also collect the buffer state that determines when each
   node throttles its upstream neighbor, allowing the source to act
   before throttling occurs and to distinguish the root of congestion
   from nodes that are only throttled by it.  The fresher telemetry
   enables more effective traffic steering and congestion control.
   FALCON is applicable to data center and wide area networks within a
   single administrative domain and is designed to be realized with IETF
   In situ OAM (IOAM) and SRv6, with the extensions identified in this
   document.
- **draft-song-lamps-cms-composite-frodokem-00** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-song-lamps-cms-composite-frodokem/) — This document specifies the conventions for using Composite FrodoKEM
   algorithms with the Cryptographic Message Syntax (CMS).  Composite
   FrodoKEM combines FrodoKEM with traditional algorithms (RSA-OAEP,
   ECDH, X25519, X448) to provide hybrid post-quantum key encapsulation.
- **draft-sriram-savnet-intrasav-solution-00** (new-draft, score 0, ignored_after_review) [none]: [IntraSAV - A Solution for Intra-Domain Source Address Validation](https://datatracker.ietf.org/doc/draft-sriram-savnet-intrasav-solution/) — This document specifies a solution, named IntraSAV, for intra-domain
   source address validation (SAV).  This solution addresses the problem
   stated in the ietf-savnet-intra-domain-problem-statement (RFC-to-be)
   document.  This document updates BCP 38 ([RFC2827]) and BCP 84
   ([RFC3704], [RFC8704]) by providing a more comprehensive solution
   methodology and accommodating prefixes that are not routed but used
   for sourcing traffic originating from an AS.
- **draft-thierry-bulk-08** (new-draft, score 0, ignored_after_review) [none]: [Binary Universal Language Kit 1.0](https://datatracker.ietf.org/doc/draft-thierry-bulk/) — This specification describes a simple, decentrally extensible and
   efficient format for data serialization.
- **draft-tiloca-lake-private-use-ranges-01** (new-draft, score 0, ignored_after_review) [none]: [Additional Private Use Ranges in the IANA Registries of the Lightweight Authenticated Key Exchange (LAKE) Protocol](https://datatracker.ietf.org/doc/draft-tiloca-lake-private-use-ranges/) — This document adds Private Use ranges to IANA registries that pertain
   to the Lightweight Authenticated Key Exchange (LAKE) protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Lightweight
   Authenticated Key Exchange Working Group mailing list
   (lake@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/lake/.

   Source for this draft and an issue tracker can be found at
   https://gitlab.com/crimson84/draft-tiloca-lake-private-use-ranges.
- **draft-wang-sidrops-fcbgp-protocol-06** (new-draft, score 0, ignored_after_review) [none]: [FC-BGP Protocol Specification](https://datatracker.ietf.org/doc/draft-wang-sidrops-fcbgp-protocol/) — This document defines an extension, Forwarding Commitment BGP (FC-
   BGP), to the Border Gateway Protocol (BGP).  FC-BGP provides security
   for the path of Autonomous Systems (ASs) through which a BGP UPDATE
   message passes.  Forwarding Commitment (FC) is a cryptographically
   signed segment to certify an AS's routing intent on its directly
   connected hops.  Based on FC, FC-BGP aims to build a secure inter-
   domain system that can simultaneously authenticate the AS_PATH
   attribute in the BGP UPDATE message and alleviate route leaks in the
   BGP routing system.  The extension is backward compatible, which
   means a router that supports the extension can interoperate with a
   router that doesn't support the extension.
- **draft-wkumari-not-a-draft-25** (new-draft, score 0, ignored_after_review) [none]: [Just because it's an Internet-Draft doesn't mean anything... at all...](https://datatracker.ietf.org/doc/draft-wkumari-not-a-draft/) — Anyone can publish an Internet Draft (ID).  This doesn't mean that
   the "IETF thinks" or that "the IETF is planning..." or anything
   similar.
- **draft-wolf-dialogue-txt-00** (new-draft, score 0, ignored_after_review) [none]: [dialogue.txt: A Standing, Talk-Only Consent to Be Contacted](https://datatracker.ietf.org/doc/draft-wolf-dialogue-txt/) — This document defines dialogue.txt, a small text file a person or an
   organisation publishes at a well-known location on its own domain.
   It is the publisher's own, standing, talk-only consent to be
   contacted by any reader, including software systems, that has no
   prior relationship with it.  A first message only proposes a
   conversation; the publisher's reply creates the channel.  The file
   grants talk and nothing else: no action, no advertising, no access
   and no representation of the publisher.  It is an invitation to a
   dialogue with a purpose.  The publisher may name the topics it can be
   asked about; for example, a navigation company may invite questions
   about traffic flow, so that a system researching that subject can ask
   for knowledge that is not published.
- **draft-wu-idr-flowspec-dip-community-filter-02** (new-draft, score 0, ignored_after_review) [none]: [Destination-IP-Community Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-dip-community-filter/) — BGP Flowspec mechanism (BGP-FS) propagates both traffic Flow
   Specifications and Traffic Filtering Actions by making use of the BGP
   NLRI and the BGP Extended Community encoding formats.  This document
   specifies a new BGP-FS component type to support community-level
   filtering.  The match field is the community of the destination IP
   address that is encoded in the Flowspec NLRI.  This function is
   applied in a single administrative domain.
- **draft-xiao-fann-fast-cnp-01** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) in RoCEv2 Networks](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp/) — This document describes a Remote Direct Memory Access (RDMA) over
   Converged Ethernet version 2 (RoCEv2) congestion control mechanism,
   known as Fast Congestion Notification Packet (Fast CNP).  By
   extending the RoCEv2 CNP, Fast CNP can be sent by the switch directly
   to the sender, advising the sender to reduce the transmission rate at
   which it sends the flow of RoCEv2 data traffic.
- **draft-xiao-fann-fast-cnp-with-proxy-05** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node for the congested network node to notify the
   traffic sender of the congestion.  The proxy network node is used to
   translate the congestion notification.  The congested network node
   sends the congestion notification to the proxy network node in a
   format defined in this document, and then the proxy network node
   translates the received congestion notification to a format known by
   the traffic sender and resends the translated congestion notification
   to the traffic sender.
- **draft-zhu-dnsop-de-eeas-03** (new-draft, score 0, ignored_after_review) [none]: [DNS Extensions to Energy Efficiency as a Service(EEAS)](https://datatracker.ietf.org/doc/draft-zhu-dnsop-de-eeas/) — This document describes a new Mechanism and DNS resource record (RR)
   type to carry information about energy-related characteristics for
   end-to-end internet access.  The "EE" ("Energy Efficiency") record
   allows the network to provide different levels of energy-saving
   service.  By providing more energy information to the client before
   it attempts to establish a connection, these records offer potential
   benefits to enhancements on energy as service criteria.

## Errors / fetch failures

_None._
