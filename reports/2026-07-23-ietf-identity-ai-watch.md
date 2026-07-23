# IETF Identity + AI Standards Watch

Date: 2026-07-23

## Read now

- **draft-fane-opena2a-aap-01** (new-version, score 28, core_identity) [none]: [OpenA2A Agent Authorization Protocol (AAP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aap/) — This document defines the OpenA2A Agent Authorization Protocol (AAP),
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
- **draft-fane-opena2a-aip-01** (new-version, score 26, adjacent_watchlist) [none]: [OpenA2A Agent Identity Protocol (AIP)](https://datatracker.ietf.org/doc/draft-fane-opena2a-aip/) — This document defines the OpenA2A Agent Identity Protocol (OpenA2A
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
- **draft-schrock-ep-architecture-02** (new-version, score 18, core_identity) [none]: [The EMILIA Protocol: An Evidence Architecture for Consequential Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-architecture/) — Consequential agent actions can cross operator and administrative
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
- **draft-sharif-x509-agent-identity-profile-01** (new-version, score 18, agent_identity) [none]: [X.509 Certificate Profile for Autonomous AI Agent Identity](https://datatracker.ietf.org/doc/draft-sharif-x509-agent-identity-profile/) — This document defines an X.509 certificate profile for identifying
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
- **draft-schrock-canonical-action-identifier-01** (new-version, score 14, core_identity) [none]: [The Canonical Action Identifier (CAID)](https://datatracker.ietf.org/doc/draft-schrock-canonical-action-identifier/) — Authorization, delegation, execution, and audit artifacts often
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
- **draft-schrock-ep-authorization-evidence-chain-04** (new-version, score 14, core_identity) [none]: [Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-evidence-chain/) — Consequential agent actions can produce heterogeneous identity,
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
- **draft-kavian-aep-oauth-session-credential-02** (new-draft, score 13, core_identity) [none]: [OAuth Bearer Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-oauth-session-credential/) — This document defines the OAuth Bearer session-credential grant type
   for the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an OAuth-style Bearer access token through the AEP
   Grant command while preserving baseline AEP client assertion
   authentication as the root of trust.
- **draft-morrison-consent-settlement-02** (new-version, score 13, core_identity) [none]: [Consent-Bound Identity Disclosure with Subject Settlement for HTTP-Native Agent Payments](https://datatracker.ietf.org/doc/draft-morrison-consent-settlement/) — This memo specifies an extension to HTTP-native agent payment
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
- **draft-morrison-mcp-dns-discovery-05** (new-draft, score 13, core_identity) [none]: [Discovery of Model Context Protocol Servers via DNS TXT Records](https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/) — This document defines a DNS-based mechanism for discovering Model
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

   This revision (v05) corrects earlier ones and introduces no new
   mechanism.  It withdraws several claims that v04 could not support,
   marks publication of a per-individual envelope in DNS as NOT
   RECOMMENDED on enumeration, size, and erasure grounds, and separates
   the agent protocol family from the transport binding in the _mcp
   record, aligning that vocabulary with neighbouring DNS agent-
   discovery drafts.  All three record formats and all three procedures
   are given here in full, so no earlier revision need be fetched.

   The mechanism complements HTTPS-based discovery, and follows the
   precedent set by DKIM, SPF, DMARC, and MTA-STS.  Provisional
   registration of a companion alter: URI scheme is requested of IANA,
   and is not yet granted.
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
- **draft-morrison-ot-command-authority-01** (new-version, score 12, core_identity) [none]: [Consented and Attributable Agent Authority for Operational-Technology Control Actions](https://datatracker.ietf.org/doc/draft-morrison-ot-command-authority/) — This memo specifies a binding profile by which a control action
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
- **draft-schrock-model-to-matter-01** (new-version, score 12, authorization) [none]: [Model-to-Matter: Authorization Evidence for Model-Directed Physical Execution](https://datatracker.ietf.org/doc/draft-schrock-model-to-matter/) — Advanced models and agents can propose experimental workflows and
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
- **draft-chueayen-attestation-receipts-00** (new-draft, score 11, adjacent_watchlist) [none]: [Enforcement Attestation Receipts for AI Inference Decisions](https://datatracker.ietf.org/doc/draft-chueayen-attestation-receipts/) — This document specifies the on-the-wire format of an attestation
   receipt produced by an AI enforcement gateway at the moment it
   decides whether a large-language-model (LLM) call is permitted.  A
   receipt binds that decision to a specific request under a published
   Ed25519 public key, so that a party who does not trust the gateway
   can still verify offline what was decided.  The format is
   deliberately minimal, a fixed set of fields and a version-selected
   signature suite, chosen for the smallest possible independent
   verifier.  It is intended for settings in which an operator-
   controlled log is not, on its own, sufficient evidence of the
   enforcement decision.
- **draft-ferro-apertomemory-02** (new-version, score 11, verifiable_claims) [none]: [The ApertoMemory Format: Portable, Client-Side-Encrypted AI Memory](https://datatracker.ietf.org/doc/draft-ferro-apertomemory/) — AI assistants and agents accumulate long-term memory about their
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

   This revision specifies format_version 2, which cryptographically
   binds every signature to the author it claims and to the cleartext
   envelope around it, and derives trust from which key verified an
   object rather than from a declared field. format_version 1, described
   by earlier revisions of this document, carries a known forgeable-
   provenance defect and MUST NOT be implemented for new deployments.
- **draft-gravit-gevp-03** (new-draft, score 11, trust_infrastructure) [none]: [Gravit Epistemic Verification Protocol (GEVP) v0.1](https://datatracker.ietf.org/doc/draft-gravit-gevp/) — Gravit Epistemic Verification Protocol (GEVP) defines minimal data
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

   This revision (-03) addresses minor editorial fixes on -02 for SCITT
   WG submission: removes workgroup tag to reflect Individual Internet-
   Draft status (IESG state I-D Exists, Stream None), normalizes Godel
   to ASCII for 0 idnits warnings, updated date to 23 Jul 2026, no
   normative changes from -02 Posted 22 Jul 19:27.  This revision (-02)
   addressed feedback on -01: pins reproducible trace commits, provides
   full confusion matrix, clarifies heuristic estimates, defines exact
   SCITT mappings, and adds Appendix B on Godel boundary.
- **draft-sabey-succession-receipts-02** (new-version, score 11, authorization) [none]: [Succession Receipts: Portable Signed Evidence of Authority Succession Between Autonomous Agents](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts/) — Autonomous agents are upgraded, replaced, suspended, and restored
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
- **draft-sabey-succession-receipts-sd-02** (new-version, score 11, verifiable_claims) [none]: [Selective Disclosure for Succession Receipts](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts-sd/) — A Succession Receipt proves one completed, policy-gated transfer of
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
- **draft-schrock-ep-authorization-receipts-08** (new-version, score 11, core_identity) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
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
- **draft-singh-apex-psi-03-01** (new-version, score 11, core_identity) [none]: [PSI-03: VPP Dispatch Conformance Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-03/) — PSI-03 specifies a portable, Ed25519-signed bond that anchors a
   registered NDIS practitioner's professional identity to a DID-
   compatible decentralised identifier without requiring a central
   registry.  The bond enables cross-provider, cross-border practice
   verification while preserving privacy and issuer sovereignty.
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
- **draft-bdnr-rats-trustworthy-credentials-02** (new-version, score 9, trust_infrastructure) [none]: [Trustworthy Enrollment of Secure Credentials](https://datatracker.ietf.org/doc/draft-bdnr-rats-trustworthy-credentials/) — There is a large class of "RATS-Unaware" Relying Parties (RUPs) that
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
- **draft-hezami-pulseproof-sentinel-00** (new-draft, score 9, core_identity) [none]: [PulseProof Sentinel Protocol Specification](https://datatracker.ietf.org/doc/draft-hezami-pulseproof-sentinel/) — This document specifies the PulseProof Sentinel Protocol (PPS), an
   experimental, technology-agnostic protocol for time-bound asymmetric
   authentication proofs.  PPS is not a new cryptographic primitive; it
   profiles established mechanisms -- Ed25519 signatures, SHA-256
   hashing, HKDF key derivation, and deterministic CBOR encoding --
   into a compact, interoperable verification model suited to offline,
   embedded, and non-browser environments where a full WebAuthn
   ceremony is unavailable.

   A PPS authentication event produces a Pulse: a signed statement
   bound to a relying-party identifier, time epoch, monotonic counter,
   expiration, and optional nonce, context, policy, and transaction
   data.  Because the verifier stores only public keys, PPS removes the
   shared-secret exposure problem inherent in TOTP.

   PulseProof Sentinel extends the basic Pulse model with several
   optional but interoperable security extensions:
- **draft-zundel-vdcarch-00** (new-draft, score 9, verifiable_claims) [spice]: [A reference architecture for direct presentation credential flows](https://datatracker.ietf.org/doc/draft-zundel-vdcarch/) — This document defines a reference architecture for direct
   presentation flows of digital credentials.  The architecture
   introduces the concept of a presentation mediator as the active
   component responsible for managing, presenting, and selectively
   disclosing credentials while preserving a set of security and privacy
   promises that will also be defined.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/leifj/wallet-refarch.
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
- **draft-kavian-agent-enrollment-protocol-02** (new-draft, score 8, core_identity) [none]: [The Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-agent-enrollment-protocol/) — The Agent Enrollment Protocol (AEP) defines an HTTP-based mechanism
   for autonomous agents to discover service enrollment requirements,
   enroll an agent identity, obtain optional session credentials, revoke
   those credentials, and query enrollment status.  AEP uses
   Decentralized Identifiers, client assertion JWTs, and HTTP Problem
   Details to provide a narrow machine-first enrollment and
   authentication substrate for agent-to-service interactions.
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
- **draft-ranjbar-dane-did-00** (new-draft, score 8, core_identity) [none]: [Rooting Decentralized Identifiers in DNSSEC: A DANE-EE Key-Binding Profile](https://datatracker.ietf.org/doc/draft-ranjbar-dane-did/) — Several Decentralized Identifier (DID) methods root trust in a DNS
   name: did:web binds an identifier to a domain and today verifies its
   keys over the Web PKI, did:dns serves DID data from DNS resource
   records, and did:webvh retrieves its history from an HTTPS location
   derived from a name.  Each either depends on the Web PKI, treats
   DNSSEC as an optional recommendation, or does not bind the
   verification-method key to the name at all.  This document defines a
   single, normative DANE-EE key-binding profile that any DNS-anchored
   DID method can point at rather than reinventing: a verification
   method's public key is published as a TLSA record with certificate
   usage DANE-EE(3), selector SubjectPublicKeyInfo(1), and matching type
   SHA-256(1) under a DNSSEC-signed name, so that a relying party can
   confirm the key from the DNS root of trust with no certificate
   authority and no fetch from the subject.  The profile binds a name to
   a key and the key to the specific DID document it signs, and no
   further; it states precisely what it does not cover, including
   continuity of holding, and points to where those answers live.
- **draft-thallapelly-oasnt-00** (new-draft, score 8, authorization) [none]: [OASNT: Attested Action Authorization Tokens](https://datatracker.ietf.org/doc/draft-thallapelly-oasnt/) — This document defines the OASNT token, a compact JWS-based credential
   in which a hardware-bound device key attests that a specific human,
   on a device whose runtime integrity was assessed, authorized one
   specific action whose human-readable disclosure is cryptographically
   bound to the token (What You See Is What You Sign).  Tokens are
   single-use, short-lived, and may additionally be bound to one
   concrete HTTP request.
- **draft-hwang-silp-protocol-02** (new-version, score 7, adjacent_watchlist) [none]: [Semantic Interlingua Layer Protocol (SILP): A Payload Codec for Cross-Model Agent Communication](https://datatracker.ietf.org/doc/draft-hwang-silp-protocol/) — This document specifies the Semantic Interlingua Layer Protocol
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
- **draft-kavian-aep-api-key-session-credential-02** (new-draft, score 7, core_identity) [none]: [API-Key Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-api-key-session-credential/) — This document defines the API-key session-credential grant type for
   the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an opaque API key through the AEP Grant command for
   deployments that already operate header-based API-key authentication.
- **draft-kavian-aep-basic-session-credential-02** (new-draft, score 7, core_identity) [none]: [Basic Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-basic-session-credential/) — This document defines the Basic session-credential grant type for the
   Agent Enrollment Protocol (AEP).  The grant type lets an AEP Service
   issue an HTTP Basic credential through the AEP Grant command for
   deployments that already integrate with Basic authentication
   middleware.
- **draft-kavian-aep-platform-hosted-identity-00** (new-draft, score 7, core_identity) [none]: [AEP Platform Hosted Identity](https://datatracker.ietf.org/doc/draft-kavian-aep-platform-hosted-identity/) — This document defines interoperable hosted identity behavior for
   Agent Enrollment Protocol (AEP) Platforms.  It lets a Platform
   provision Service-scoped Agent did:web identities, publish DID
   documents, custody signing keys, and produce AEP client assertion
   JWTs through delegated signing operations.
- **draft-morrison-binding-moment-envelope-01** (new-draft, score 7, adjacent_watchlist) [none]: [The Briefing-and-Binding Envelope: A Delivery Contract for Agent-to-Principal Decision Moments with Dual-Veto Reconciliation](https://datatracker.ietf.org/doc/draft-morrison-binding-moment-envelope/) — This memo specifies the briefing-and-binding envelope: a delivery
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
- **draft-ietf-dance-client-auth-13** (new-version, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document updates RFC 6698 and RFC 7671.  It describes how to use the
   TLSA record to publish client certificates or public keys, and also
   the rules and considerations for using them with TLS.  In addition,
   it defines a new TLS extension, DANE Client Identity, to convey the
   client's domain name identity to the server.
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
- **draft-sabey-refusal-transparency-02** (new-version, score 6, trust_infrastructure) [none]: [Refusal Transparency: Signed, Replay-Resistant Evidence of Refused Agent-System Transitions](https://datatracker.ietf.org/doc/draft-sabey-refusal-transparency/) — A governance system for autonomous agents is defined as much by what
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
- **draft-ietf-spice-oidc-cwt-06** (new-draft, score 5, adjacent_watchlist) [spice]: [OpenID Connect Standard Claims Registration for CBOR Web Tokens](https://datatracker.ietf.org/doc/draft-ietf-spice-oidc-cwt/) — This document registers OpenID Connect standard claims already used
   in JSON Web Tokens for use in CBOR Web Tokens.
- **draft-fane-ai-safety-txt-01** (new-version, score 4, adjacent_watchlist) [none]: [The ai-safety.txt Domain AI Safety Declaration](https://datatracker.ietf.org/doc/draft-fane-ai-safety-txt/) — This document defines ai-safety.txt, a plain-text declaration format
   that a domain publishes at a well-known location to communicate its
   AI-safety posture to autonomous agents and agent-driven browsers.
   Modeled on the robots.txt convention, an ai-safety.txt file lets a
   domain assert, in a machine-readable form, whether its content is
   authored by the domain rather than user-generated, whether that
   content is hardened against prompt injection, and whether it is
   rendered consistently to human and agent user agents.  The file also
   carries a security contact, a link to an external verification
   record, and the date the declaration was last verified.

   The declarations in an ai-safety.txt file are self-asserted by the
   publishing domain.  This document specifies the file format and its
   well-known location, and it is explicit that a consuming agent treats
   a declaration as a hint rather than as proof, verifying it against
   independent evidence where such evidence is available.
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

## Adjacent / watchlist

- **draft-doehle-company-certs-discovery-00** (new-draft, score 3, adjacent_watchlist) [none]: [A Well-Known URI for Discovery of Application-Specific Trust Anchors](https://datatracker.ietf.org/doc/draft-doehle-company-certs-discovery/) — This document defines the "company-certs" well-known URI in
   accordance with Request for Comments (RFC) 8615.  The URI provides a
   JSON metadata document that allows an organization to publish
   application-specific trust anchors and related revocation information
   for use by consuming applications.  The mechanism is intended for
   scoped trust bootstrapping, such as S/MIME, mutual TLS, or other
   application-local trust decisions, without modifying the global
   operating system trust store.
- **draft-grant-ntp-server-identifier-extension-00** (new-draft, score 3, core_identity) [none]: [NTP Server Identifier Extension](https://datatracker.ietf.org/doc/draft-grant-ntp-server-identifier-extension/) — This document defines an extension field that allows operators of NTP
   services the ability to provide additional information about their
   services to clients which request it.
- **draft-ietf-cose-c509-test-vectors-02** (new-draft, score 3, adjacent_watchlist) [cose]: [Test Vectors for CBOR-Encoded X.509 (C509) Certificates](https://datatracker.ietf.org/doc/draft-ietf-cose-c509-test-vectors/) — This document contains examples of CBOR-encoded X.509 (C509)
   certificates, certification requests, and certification request
   templates.
- **draft-ietf-httpbis-connect-tcp-12** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP proxying using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this proxying functionality has several
   important deficiencies in modern HTTP environments.  This
   specification defines an alternative HTTP proxy service configuration
   for TCP connections.  This configuration is described by a URI
   Template, similar to the CONNECT-UDP and CONNECT-IP protocols.
- **draft-ietf-lsr-isis-flex-algo-yang-21** (new-version, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for IS-IS Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-flex-algo-yang/) — This document defines a YANG data model to support IS-IS Application-
   Specific Link Attributes and Flexible Algorithm.
- **draft-ietf-lsr-ospf-flex-algo-yang-16** (new-version, score 3, adjacent_watchlist) [lsr]: [A YANG Data Model for OSPF Application-Specific Link Attributes and Flexible Algorithm](https://datatracker.ietf.org/doc/draft-ietf-lsr-ospf-flex-algo-yang/) — This document defines a YANG data model to support OSPF Application-
   Specific Link Attributes and Flexible Algorithm.  It also creates the
   initial version of IANA-maintained YANG modules for IGP Algorithm
   Types, IGP Metric-Types, and IGP Link Attribute Applications.

   This document updates RFCs 8665, 9350, and 9843.
- **draft-ietf-mailmaint-imap-objectid-bis-06** (new-version, score 3, core_identity) [mailmaint]: [IMAP Extension for Object Identifiers](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-imap-objectid-bis/) — This document defines the OBJECTID+ extension for IMAP, which
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
- **draft-ietf-masque-connect-udp-ecn-dscp-02** (new-version, score 3, adjacent_watchlist) [masque]: [ECN and DSCP support for HTTPS's Connect-UDP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp-ecn-dscp/) — HTTP's Extended Connect's Connect-UDP protocol enables a client to
   proxy a UDP flow from the HTTP server towards a specified target IP
   address and UDP port.  QUIC and Real-time transport protocol (RTP)
   are examples of transport protocols that use UDP and support Explicit
   Congestion Notification (ECN) and provide the necessary feedback.
   This document specifies how ECN and DSCP can be supported through an
   extension to the Connect-UDP protocol for HTTP without per-packet
   byte overhead, solely using Context IDs.
- **draft-ietf-opsawg-discardmodel-15** (new-draft, score 3, adjacent_watchlist) [opsawg]: [Information and Data Models for Packet Discard Reporting](https://datatracker.ietf.org/doc/draft-ietf-opsawg-discardmodel/) — This document defines an Information Model and specifies a
   corresponding YANG data model for packet discard reporting.  The
   Information Model provides an implementation-independent framework
   for classifying packet loss - both intended (e.g., due to policy) and
   unintended (e.g., due to congestion or errors) - to enable automated
   network mitigation of unintended packet loss.  The YANG data model
   specifies an implementation of this Information Model for network
   elements with a focus on interface, device, and control-plane
   discards.
- **draft-ietf-spice-glue-id-10** (new-draft, score 3, adjacent_watchlist) [spice]: [GLobal Unique Enterprise (GLUE) Identifiers](https://datatracker.ietf.org/doc/draft-ietf-spice-glue-id/) — This specification establishes a URI scheme for GLobal Unique
   Enterprise (GLUE) Identifiers.  This enables URI identifiers to be
   used for businesses and organizations.  It enables organizational
   identities from existing authorities to be represented within this
   URI scheme.
- **draft-ietf-suit-update-management-14** (new-version, score 3, core_identity) [suit]: [Update Management Extensions for Software Updates for Internet of Things (SUIT) Manifests](https://datatracker.ietf.org/doc/draft-ietf-suit-update-management/) — This document specifies extensions to the SUIT manifest format.
   These extensions allow an update author, update distributor or device
   operator to more precisely control the distribution and installation
   of updates to devices.  These extensions also provide a mechanism to
   inform a management system of Software Identifier and Software Bill
   Of Materials information about an updated device.
- **draft-ietf-uta-tls13-iot-profile-23** (new-version, score 3, adjacent_watchlist) [uta]: [TLS/DTLS 1.3 Profiles for the Internet of Things](https://datatracker.ietf.org/doc/draft-ietf-uta-tls13-iot-profile/) — RFC 7925 offers guidance to developers on using TLS/DTLS 1.2 for
   Internet of Things (IoT) devices with resource constraints.  This
   document is a companion to RFC 7925, defining TLS/DTLS 1.3 profiles
   for IoT devices.  Additionally, it updates RFC 7925 with respect to
   the X.509 certificate profile and ciphersuite requirements.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/thomas-fossati/draft-tls13-iot.
- **draft-li-coap-task-resources-01** (new-version, score 3, adjacent_watchlist) [none]: [CoAP Extensions for Asynchronous Task Resources](https://datatracker.ietf.org/doc/draft-li-coap-task-resources/) — Many operations on constrained devices cannot complete within a
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
- **draft-singh-apex-psi-07-01** (new-version, score 3, trust_infrastructure) [none]: [PSI-07: Organic Production Attestation](https://datatracker.ietf.org/doc/draft-singh-apex-psi-07/) — PSI-07 defines a standard signal format for regulatory events
   detected by automated monitoring systems.  The format is a signed
   JSON envelope carrying the event classification, evidence hash, and
   jurisdiction code, enabling autonomous reporting to one or more
   regulators without human intervention.
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
- **draft-alsahati-nhp-sba-nhp-protocol-01** (new-version, score 2, ignored_after_review) [none]: [Network Hiding Protocol (NHP) Extensions for 5G/6G Service-Based Architectures](https://datatracker.ietf.org/doc/draft-alsahati-nhp-sba-nhp-protocol/) — This document specifies a candidate implementation profile and
   extension to the evolving Network Hiding Protocol (NHP) standards,
   designed specifically for autonomous 5G/6G Service-Based
   Architectures (NHP-SBA).  It defines the payload schemas,
   cryptographic bindings, and state machine workflows necessary to
   address Policy Enforcement Point (PEP) interoperability surfaces in
   heterogeneous telecom environments.  By leveraging zero-copy
   FlatBuffers serialization and HTTP/2 Custom Frame Extensions, NHP-SBA
   enables deterministic, ultra-low-latency safety enforcement for
   agent-driven RF control loops.
- **draft-google-cfrg-libzk-02** (new-draft, score 2, ignored_after_review) [none]: [Longfellow ZK](https://datatracker.ietf.org/doc/draft-google-cfrg-libzk/) — This document defines an algorithm for generating and verifying a
   succinct non-interactive zero-knowledge argument that for a given
   input x and a circuit C, there exists a witness w, such that C(x,w)
   evaluates to 0.  The technique here combines the MPC-in-the-head
   approach for constructing ZK arguments described in Ligero [ligero]
   with a verifiable computation protocol based on sumcheck for proving
   that C(x,w)=0.
- **draft-ietf-dnsop-delext-09** (new-version, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895 and 9824.
- **draft-reilly-hdrp-00** (new-draft, score 2, ignored_after_review) [none]: [Hypercube Data Rotation Protocol (HDRP) for Distributed Integrity and Moving Target Defense](https://datatracker.ietf.org/doc/draft-reilly-hdrp/) — This document specifies the Hypercube Data Rotation Protocol (HDRP),
   an experimental protocol for distributing erasure-coded data shards
   across nodes arranged in an n-dimensional binary hypercube topology
   and periodically permuting shard placement through structured
   rotation operations.  Rotations are automorphisms of the hypercube
   graph, applied on a fixed epoch schedule and committed to a
   verifiable epoch ledger.  The design applies the established
   principles of hypercube interconnection networks, maximum distance
   separable (MDS) erasure coding, and moving target defense (MTD) to
   provide three properties in combination: storage-efficient fault
   tolerance, continuous cryptographic verifiability, and reduction of
   the value of static reconnaissance by an adversary.  HDRP is
   designed to integrate with autonomous self-healing pipelines and
   with dual-layer permanence anchoring (blockchain timestamping and
   DOI archival) as defined in related documents by the same author.
   Informally, the rotation mechanism may be visualized as the face
   turns of a combination puzzle applied to a data topology; this
   document defines that intuition as a precise algebraic operation.
- **draft-singh-apex-psi-05-01** (new-version, score 2, ignored_after_review) [none]: [PSI-05: Financial Disclosure Integrity](https://datatracker.ietf.org/doc/draft-singh-apex-psi-05/) — PSI-05 defines the royalty schedule that MAY be levied by a
   publishing foundation for commercial, litigation, regulatory, or AI-
   training reuse of PSI public ledger data above a threshold defined by
   the foundation's charter.  It establishes a flat-rate per-row fee
   schedule, exemption categories, and an audit protocol.

## Ignored after review

- **draft-abraitis-idr-maximum-paths-subcode-02** (new-draft, score 0, ignored_after_review) [none]: [Maximum Number of Paths Reached Notification for BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-maximum-paths-subcode/) — This document defines a new BGP Cease NOTIFICATION message subcode,
   "Maximum Number of Paths Reached", used when a BGP speaker terminates
   a peering because the number of paths received from a neighbor, as
   permitted by BGP ADD-PATH, exceeds a locally configured upper bound.
   That bound may be applied on a per-prefix basis or as an aggregate
   limit across an address family.
- **draft-becker-cnsa2-ssh-profile-05** (new-version, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
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
- **draft-cel-nfsv4-rpc-over-quicv1-06** (new-draft, score 0, ignored_after_review) [none]: [Remote Procedure Call over QUIC Version 1](https://datatracker.ietf.org/doc/draft-cel-nfsv4-rpc-over-quicv1/) — This document specifies a protocol for conveying Remote Procedure
   (RPC) messages via QUIC version 1 connections.  It requires no
   revision to application RPC protocols or the RPC protocol itself.
- **draft-cheng-rtgwg-srv6-multihome-egress-protection-12** (new-draft, score 0, ignored_after_review) [rtgwg]: [SRv6 Egress Protection in Multi-homed scenario](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-srv6-multihome-egress-protection/) — This document describes a SRv6 egress node protection mechanism in
   multi-homed scenarios.
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
- **draft-geng-savnet-inter-domain-spa-03** (new-draft, score 0, ignored_after_review) [none]: [Source Prefix Advertisement for Inter-domain SAVNET](https://datatracker.ietf.org/doc/draft-geng-savnet-inter-domain-spa/) — This document proposes a mechanism that enables a Source AS to
   actively advertise their locally observed Customer Cone and prefix
   information to the adjacent Validating AS via a new inter-domain
   message called Source Prefix Advertisement (SPA).  The Validating AS
   then combines this SPA-carried information with local source address
   validation-related information to construct more accurate prefix
   allowlists for interfaces connected to Source ASes.
- **draft-gondwana-email-header-maintenance-01** (new-draft, score 0, ignored_after_review) [none]: [Maintenance of the IANA Message Header Field Registries](https://datatracker.ietf.org/doc/draft-gondwana-email-header-maintenance/) — The IANA "Message Headers" registries record, for each registered
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
- **draft-hoflev-secure-smtp-01** (new-version, score 0, ignored_after_review) [none]: [Secure SMTP](https://datatracker.ietf.org/doc/draft-hoflev-secure-smtp/) — SMTP [RFC5321] uses opportunistic TLS to optionally protect transport
   sessions.  Secure SMTP uses mandatory TLS on all connections.  It
   also provides a method for SMTP clients to locate Secure SMTP
   servers.
- **draft-housley-asn1-layman-guide-01** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.
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
- **draft-ietf-anima-rfc8366bis-33** (new-version, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Bootstrapping Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
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
- **draft-ietf-bess-evpn-first-hop-security-01** (new-draft, score 0, ignored_after_review) [bess]: [EVPN First Hop Security](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-first-hop-security/) — The Dynamic Host Configuration Protocol (DHCP) snoop database stores
   valid IPv4-to-MAC and IPv6-to-MAC bindings by snooping on DHCP
   messages.  These bindings are used by security functions like Dynamic
   Address Resolution Protocol Inspection (DAI), Neighbor Discovery
   Inspection (NDI), IPv4 Source Guard, and IPv6 Source Guard to
   safeguard against traffic received with a spoofed address.  These
   functions are collectively referred to as First Hop Security (FHS).

   This document proposes BGP extensions and new Ethernet VPN (EVPN)
   procedures to distribute and synchronize the DHCP snoop database to
   support FHS.  Such synchronization is needed to support EVPN host
   mobility and multihoming.
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
- **draft-ietf-bier-frr-14** (new-version, score 0, ignored_after_review) [bier]: [A Framework for Fast Reroute with Bit Index Explicit Replication (BIER-FRR)](https://datatracker.ietf.org/doc/draft-ietf-bier-frr/) — This document provides a framework for the development of Fast
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
- **draft-ietf-ianabis-early-registries-02** (new-draft, score 0, ignored_after_review) [ianabis]: [Early IANA Registry Creation](https://datatracker.ietf.org/doc/draft-ietf-ianabis-early-registries/) — This memo describes the requirements for establishing an IANA
   registry before the IETF Stream document that creates the registry is
   approved for publication as an RFC.  This process can be used when an
   IETF working group needs to coordinate allocations among multiple
   documents or with an organization outside the IETF.
- **draft-ietf-idr-ts-flowspec-srv6-policy-11** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification defined in [RFC8955], [RFC8956] and [RFC9117]
   has been proposed to distribute BGP [RFC4271] FlowSpec NLRI to
   FlowSpec clients to mitigate (distributed) denial-of-service attacks,
   and to provide traffic filtering in the context of a BGP/MPLS VPN
   service.  Recently, traffic steering applications in the context of
   SR-MPLS and SRv6 using FlowSpec are being used in networks.  This
   document introduces the usage of BGP Flow Specification to steer
   packets into an SR Policy.
- **draft-ietf-mlcodec-opus-speech-coding-enhancement-04** (new-draft, score 0, ignored_after_review) [mlcodec]: [Integration of Speech Codec Enhancement Algorithms into the Opus Codec](https://datatracker.ietf.org/doc/draft-ietf-mlcodec-opus-speech-coding-enhancement/) — This document proposes a set of requirements for integrating a speech
   codec enhancement algorithm into the Opus codec [RFC6716].
- **draft-ietf-netmod-yang-semver-28** (new-version, score 0, ignored_after_review) [netmod]: [YANG Semantic Versioning](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-semver/) — This document specifies a YANG extension along with guidelines for
   applying an extended set of semantic versioning rules to revisions of
   YANG artifacts (e.g., modules and packages).  Additionally, this
   document defines a YANG extension for controlling module imports
   based on these modified semantic versioning rules.

   This document updates RFCs 7950, 9907, and 8525.
- **draft-ietf-nfsv4-nfs-acl-03** (new-draft, score 0, ignored_after_review) [nfsv4]: [The Network File System Access Control List Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-nfs-acl/) — This Informational document describes the NFS_ACL protocol.  NFS_ACL
   is a legacy member of the Network File System family of protocols
   that NFS clients use to view and update Access Control Lists stored
   on an NFS version 2 or version 3 server.
- **draft-ietf-roll-enrollment-priority-18** (new-version, score 0, ignored_after_review) [roll]: [Controlling Network Enrollment in RPL networks](https://datatracker.ietf.org/doc/draft-ietf-roll-enrollment-priority/) — The Routing Protocol for Low-Power and Lossy Networks (RPL) manages
   the routing topology but lacks a mechanism to globally regulate how
   many new nodes, known as Pledges, can join a node in a 6TiSCH network
   at any given time.  Currently, Join Proxies (6LowPAN Routers) make
   local decisions about whether to facilitate a Pledge's enrollment
   based only on their immediate resources.

   This document introduces RPL extensions to ensure that enrollment
   remains orderly, prevents localized congestion at specific Join
   Proxies, and allows the network to stay within its operational
   capacity limits.
- **draft-ietf-schc-over-networks-prone-to-disruptions-05** (new-draft, score 0, ignored_after_review) [schc]: [Static Context Header Compression and Fragmentation over networks prone to disruptions](https://datatracker.ietf.org/doc/draft-ietf-schc-over-networks-prone-to-disruptions/) — This document describes the use of SCHC over different network
   topologies and devices regardless of their capabilities and
   configurations.  The use of SCHC will bring connectivity to devices
   with disruptive connections caused by restrained use of battery and
   connectionless setups with long delays and latency.
- **draft-ietf-spring-stamp-srpm-mpls-04** (new-version, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for Performance Measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as defined in RFC 8762,
   along with its optional extensions defined in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm paths), as well as Layer-3
   and Layer-2 services over the SR-MPLS paths.
- **draft-ietf-sshm-strict-kex-02** (new-draft, score 0, ignored_after_review) [sshm]: [SSH Strict KEX extension](https://datatracker.ietf.org/doc/draft-ietf-sshm-strict-kex/) — This document describes a small set of modifications to the Secure
   Shell (SSH) protocol to fix the so-called Terrapin Attack on the
   initial key exchange.
- **draft-josefsson-sshsig-format-04** (new-draft, score 0, ignored_after_review) [sshm]: [Lightweight Secure Shell (SSH) Signature Format](https://datatracker.ietf.org/doc/draft-josefsson-sshsig-format/) — This document describes a lightweight SSH Signature format that is
   compatible with SSH keys and wire formats.
- **draft-koch-openpgp-webkey-service-22** (new-draft, score 0, ignored_after_review) [none]: [OpenPGP Web Key Directory](https://datatracker.ietf.org/doc/draft-koch-openpgp-webkey-service/) — This specification describes a service to locate OpenPGP and LibrePGP
   keys by mail address using a Web service and the HTTPS protocol.  It
   also provides a method for secure communication between the key owner
   and the mail provider to publish and revoke the public key.
- **draft-kriswamy-bess-evpn-perflow-df-02** (new-draft, score 0, ignored_after_review) [none]: [Per-Flow EVPN Designated Forwarder Election](https://datatracker.ietf.org/doc/draft-kriswamy-bess-evpn-perflow-df/) — The Ethernet Virtual Private Network (EVPN) solution offers
   procedures for electing a Designated Forwarder (DF) for multihomed
   Ethernet Segments.  In this context, the Provider Edge (PE) router is
   responsible for sending Broadcast, Unknown Unicast, and Multicast
   (BUM) traffic to a multihomed device or network.  This applies in
   cases of an all-active multihomed Ethernet Segment (ES) as well as
   for BUM and unicast traffic in the case of single-active multihoming.
   While the Default Algorithm provides an efficient and automated
   mechanism for selecting the DF across Ethernet Tags within an
   Ethernet Segment, it does not provide Per-flow DF selection within an
   EVPN Instance (EVI).

   This document defines a new DF Election Algorithm that performs Per-
   flow DF selection by defining a new DF Algorithm value.
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
- **draft-norton-sdlp-sec-arch-03** (new-version, score 0, ignored_after_review) [none]: [SDLP Security Architecture (SDLP RFC 4)](https://datatracker.ietf.org/doc/draft-norton-sdlp-sec-arch/) — Please let me know if this can not be manually posted for some reason. Thank you for your help.
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
- **draft-schinazi-httpbis-ohttp-pfs-01** (new-version, score 0, ignored_after_review) [none]: [A Perfect Forward Secure Extension to Oblivious HTTP](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-ohttp-pfs/) — Oblivious HTTP (OHTTP) is a protocol for forwarding encrypted HTTP
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
- **draft-smith-6man-accurate-ra-router-lifetime-01** (new-draft, score 0, ignored_after_review) [none]: [More Accurately Naming IPv6 RA Router Lifetime](https://datatracker.ietf.org/doc/draft-smith-6man-accurate-ra-router-lifetime/) — IPv6 Router Advertisements (RAs) have a "Router Lifetime" field,
   which specifies how long the advertising router will act as a default
   router for the receiving hosts, unless refreshed with another
   advertisement.  The field name "Router Lifetime" is quite general,
   and could easily be misunderstood to mean the bounded lifetime of all
   of the information contained in the RA.  This memo more accurately
   renames this field "Default Router Lifetime".
- **draft-tang-ipv4plus-17** (new-draft, score 0, ignored_after_review) [none]: [IPv4+ The Extended Protocol Based On IPv4](https://datatracker.ietf.org/doc/draft-tang-ipv4plus/) — This document specifies version 4+ of the Internet Protocol
    (IPv4+). IPv4 is very successful,simple and elegant.
    continuation and expansion of the IPv4 is necessary. Existing
    systems, devices only need to upgrade the software to support
    IPv4+, without the need to update new hardwares,saving
    investment costs. Ipv4+ is also an interstellar Protocol,
    so the Internet will evolve into a star Internet.
- **draft-test-psi-00** (new-draft, score 0, ignored_after_review) [none]: [Test PSI Submission](https://datatracker.ietf.org/doc/draft-test-psi/) — Test submission.
- **draft-uberti-tsvwg-warp-00** (new-draft, score 0, ignored_after_review) [none]: [WebRTC Abridged Roundtrip Protocol (WARP)](https://datatracker.ietf.org/doc/draft-uberti-tsvwg-warp/) — This document outlines a set of improvements to the WebRTC session
   setup protocols aimed at significantly reducing connection setup
   latency.  This improved setup mechanism is known as the WebRTC
   Abridged Roundtrip Protocol (WARP).  By addressing inefficiencies
   within the current multi-protocol handshake process, WARP can reduce
   setup latency from 6 RTTs to 2 RTTs when its optimizations are used
   together, with a direct impact on perceived performance and
   reliability.
- **draft-vanmook-expanse-problem-statement-00** (new-draft, score 0, ignored_after_review) [none]: [Extending Policy, Addressing and Numbering across Space Ecosystems (EXPANSE): Problem Statement](https://datatracker.ietf.org/doc/draft-vanmook-expanse-problem-statement/) — Ongoing IETF work on networking in non-terrestrial and deep-space
   environments treats addressing, numbering, and registry policy as a
   greenfield.  It is not.  Three decades of operational practice,
   registry governance, and routing security infrastructure exist, and
   any space-segment architecture that ignores them will recreate,
   badly, the coordination mechanisms the Internet already has.  This
   document describes the problem and motivates chartering a working
   group to address it.
- **draft-westerbaan-dnssec-mldsa-02** (new-version, score 0, ignored_after_review) [none]: [Module-Lattice Digital Signature Algorithm for DNSSEC](https://datatracker.ietf.org/doc/draft-westerbaan-dnssec-mldsa/) — This document describes how to specify Module-Lattice-Based Digital
   Signature Algorithm (ML-DSA) keys and signatures in DNS Security
   (DNSSEC).  It uses the ML-DSA-44 parameter set defined in FIPS 204.
   ML-DSA-44 is believed to be secure even against adversaries in
   possession of a cryptographically relevant quantum computer.
- **draft-wu-idr-flowspec-redirect-group-02** (new-draft, score 0, ignored_after_review) [none]: [BGP Flowspec Redirect Load Balancing Group Community](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-redirect-group/) — This document defines an extension to the BGP Community Container
   Attribute, which allows flowspec redirection to multiple paths.  This
   extended community serves to redirect traffic to a load balancing
   group and supports both equal-cost multi-path (ECMP) and unequal-cost
   multi-path (UCMP) scenarios.
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

## Errors / fetch failures

- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
- draft-singh-apex-psi: metadata fetch failed: 404 Client Error: Not Found for url: https://datatracker.ietf.org/doc/draft-singh-apex-psi/doc.json
