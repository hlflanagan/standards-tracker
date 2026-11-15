# IETF Identity + AI Standards Watch

Date: 2026-11-15

## Read now

- **draft-kamimura-vap-framework-03** (new-draft, score 27, trust_infrastructure) [none]: [Verifiable AI Provenance Framework (VAP): An Architectural Framework for Auditable AI Decision Trails](https://datatracker.ietf.org/doc/draft-kamimura-vap-framework/) — Automated decision-making systems, including AI and algorithmic
   systems in critical infrastructure, currently lack standardized
   mechanisms for producing provenance records that third parties can
   verify independently.  Traditional logging approaches do not provide
   the cryptographic properties that regulatory examination, forensic
   investigation, and cross-organizational accountability depend on:
   detectability of alteration, detectability of omission after
   commitment, and attribution.

   This document describes the Verifiable AI Provenance Framework (VAP),
   an architectural framework that defines requirements for producing
   verifiable decision trails using existing IETF security technologies.
   VAP does not define new protocols or cryptographic primitives;
   rather, it provides an architectural coordination layer that enables
   domain-specific profiles to leverage Supply Chain Integrity,
   Transparency and Trust (SCITT), Remote Attestation Procedures (RATS),
   CBOR Object Signing and Encryption (COSE), and related IETF work in a
   consistent manner.

   VAP makes records auditable and attributable after the fact.  It does
   not prevent, block, or intercept any system behaviour, and it does
   not warrant that any recorded decision was correct, fair, or safe.
   The detailed requirement set is maintained by the VeritasChain
   Standards Organization (VSO) as a separate specification; this
   document describes the architecture and its mapping to IETF work.

   This document is intended to frame the problem space and facilitate
   discussion about whether architectural coordination work is needed in
   this area.
- **draft-elekula-agentproto-linked-dialog-00** (new-draft, score 22, core_identity) [none]: [Privacy-Preserving Verification of Linked-Dialog Relationships Across Trust Boundaries](https://datatracker.ietf.org/doc/draft-elekula-agentproto-linked-dialog/) — Agentic systems increasingly create, delegate, relay, and transform
   dialogs across multiple agents, protocols, services, and
   administrative trust boundaries. In these environments, a verifier
   may need to determine whether two dialogs are related without
   requiring unrestricted disclosure of their contents or relying
   exclusively on the assertions of an intermediary.

   This document describes properties and a conceptual evaluation model
   for privacy-preserving verification of linked-dialog relationships
   across trust boundaries. It distinguishes dialog association from
   context propagation, relationship verification from authentication
   and authorization, and verification outcomes from assessments of
   evidence completeness.

   The document also considers evidence scope, source positions,
   temporal references, intermediary continuity, lifecycle changes,
   identity binding, privacy, and evidence availability. It identifies
   requirements intended to help future protocol designs represent
   linked-dialog relationships in a way that can be independently
   evaluated while limiting unnecessary disclosure.

   This document does not define a wire format, cryptographic mechanism,
   identifier format, transport binding, authorization protocol,
   audit-log structure, or completeness-proof mechanism. It provides
   terminology, design properties, and interoperability considerations
   for further discussion.
- **draft-xu-oan-resource-identity-discovery-02** (new-draft, score 20, core_identity) [none]: [Trust-Governed Resource Identity and Discovery Architecture for OpenAgenet](https://datatracker.ietf.org/doc/draft-xu-oan-resource-identity-discovery/) — This document describes a trust-governed resource identity and
   discovery architecture for OpenAgenet (OAN).  It covers callable
   agents, skills, Model Context Protocol (MCP) servers, tools, and
   application programming interfaces.  Registrars verify registration
   authority, a Root accepts versioned resource packages, and authorized
   Discovery Nodes expose verified candidates.  Consumers verify package
   integrity, acceptance, and current state before using a resource
   through its native protocol or artifact format.

   The architecture can be profiled with Decentralized Identifier (DID)
   document concepts and credential-based assertions.  This document
   does not define a new DID method, media type, URI scheme, transport
   protocol, ranking algorithm, blockchain protocol, agent invocation
   protocol, or product-native schema.
- **draft-kroehl-agentic-trust-aae-03** (new-draft, score 17, authorization) [none]: [Agent Authorization Envelope (AAE): A Machine-Evaluable Authorization Structure for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/) — Autonomous AI agents now operate at production scale across
   financial, commercial, and infrastructure domains — executing
   transactions, invoking APIs, and taking consequential actions without
   direct human oversight at each step.  Existing authorization
   mechanisms (OAuth 2.0, API keys, ACLs) were designed for human-
   initiated requests and do not capture the machine-evaluable semantics
   required for autonomous agent authorization: what the agent is
   mandated to do, what constraints bound its actions, and for how long
   the authorization is valid.

   This document specifies the Agent Authorization Envelope (AAE), a
   structured authorization container for autonomous AI agents.  AAE
   defines three mandatory blocks — MANDATE, CONSTRAINTS, and VALIDITY —
   that together constitute a machine-evaluable, cryptographically
   verifiable authorization assertion.  AAE is designed to be protocol-
   agnostic, binding to W3C Decentralized Identifiers (DIDs) for agent
   identity and W3C Verifiable Credentials (VCs) for issuance and
   signature, and is independent of any specific AI framework, transport
   protocol, or blockchain.
- **draft-zambo-aer1-wimse-mapping-03** (new-draft, score 17, trust_infrastructure) [none]: [AER-1 Receipts as Audit Records for WIMSE AIMS](https://datatracker.ietf.org/doc/draft-zambo-aer1-wimse-mapping/) — The WIMSE AI Identity Management System (AIMS) framework requires
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
- **draft-ietf-stir-certificate-transparency-06** (new-draft, score 15, adjacent_watchlist) [stir]: [STI Certificate Transparency](https://datatracker.ietf.org/doc/draft-ietf-stir-certificate-transparency/) — This document describes a framework for the use of the Certificate
   Transparency (CT) protocol for publicly logging the existence of
   Secure Telephone Identity (STI) certificates as they are issued or
   observed.  This allows any interested party that is part of the STI
   ecosystem to audit STI certification authority (CA) activity and
   audit both the issuance of suspect certificates and the certificate
   logs themselves.  The intent is to establish a level of trust within
   the STI ecosystem that relies on the verification of telephone
   numbers.  This involves requiring STI certificates to be listed in an
   established log and refusing to honor those that are not.  This
   effectively establishes the precedent that STI CAs must add all
   issued certificates to the logs and thus establishes unique
   association of STI certificates to an authorized provider or assignee
   of a telephone number resource.  In the STI ecosystem, the primary
   role of CT is to provide verifiable trust by detecting the
   unauthorized issuance of duplicate telephone number level delegate
   certificates or provider level certificates.  This provides a robust
   auditable mechanism for the detection of unauthorized creation of
   certificate credentials for illegitimate spoofing of telephone
   numbers or service provider codes (SPC).

   The framework borrows the log structure and API model from RFC 6962
   to enable public auditing and verifiability of certificate issuance.
   While the foundational mechanisms for log operation, Merkle Tree
   construction, and Signed Certificate Timestamps (SCTs) are aligned
   with RFC 6962, this document contextualizes their application in the
   STIR ecosystem, focusing on verifiable control over telephone number
   or service provider code resources.
- **draft-abbas-vrp-offer-verification-00** (new-draft, score 14, adjacent_watchlist) [none]: [The Vacation Rental Protocol (VRP): Host-Domain Discovery and Verification of Signed Stay Offers](https://datatracker.ietf.org/doc/draft-abbas-vrp-offer-verification/) — The Vacation Rental Protocol (VRP) lets an AI agent or other client
   verify, directly from a vacation-rental host's own domain and with no
   intermediary, that a stay offer was signed by a key that domain
   publishes, has not been altered, and is within its stated lifetime.
   The signed offer carries the host domain's own statements of
   availability and exact price for the stay asked for.  A valid
   signature proves the provenance and integrity of those statements; it
   does not guarantee that the stay is in fact available.  A host domain
   publishes a discovery document at a well-known URI, an Ed25519 key
   set, and signed stay offers (compact JSON Web Signatures).
   Verification requires no central registry, issuer, accreditation
   program, or gatekeeper: control of the host domain is the root of
   trust.

   This document specifies the discovery document, key publication and
   rotation, the signed verified stay offer, and the verification
   procedure, including fail-closed behavior and a three-state
   verification model.  It also describes the existing provisional
   registration of the "vacation-rental.json" well-known URI suffix.
- **draft-gruszka-audit-decision-receipts-09** (new-draft, score 14, trust_infrastructure) [none]: [Decision Receipts for Approvals, Declined Actions and Executed Actions in Agent Audit Records](https://datatracker.ietf.org/doc/draft-gruszka-audit-decision-receipts/) — The architecture for auditing agent delegation and interactions
   proposed for the AUDIT effort names Interaction Records, Action
   Records and Authorization Transition Records and leaves their
   encoding open.  This document maps an existing pair of signed
   records, the decision receipt and the outcome receipt of the open-
   source proofbundle project, onto those record types for three cases,
   a human approval, a declined action and an executed action with its
   result, and gives each record exact bytes, a signature and digest
   bindings that a third party can check offline.  Each receipt is
   created when the decision or the outcome occurs and is checked by an
   Auditor post hoc, and a declined or refused action is a record of its
   own.  For each case the document states what the receipt adds and
   what it does not show, and it gives a verification procedure that
   runs offline.  It requires that an approval be honoured at most once,
   even after the record of consumed approvals is rotated.  Test vectors
   for all three cases, each with a counterexample, are included.  The
   document also describes, informatively, how a receipt can be
   registered with a Transparency Service under RFC 9943 and what a
   SCITT Receipt then shows and does not show.  It uses existing receipt
   formats and defines no new predicate or registry.  How the issuer of
   a receipt enforces its decision is out of scope.
- **draft-bates-atp-01** (new-draft, score 13, trust_infrastructure) [none]: [Agent Transaction Protocol (ATP)](https://datatracker.ietf.org/doc/draft-bates-atp/) — ATP defines a cryptographically verifiable directed acyclic graph
   (DAG) model for agent transactions.  ATP enables tamper-evident
   signed causality and auditable lineage across agentic systems by
   representing each action as a signed node with one or more parent
   references, assuming verifier access to issuer public keys and the
   referenced parent nodes.  The protocol is designed to be lightweight,
   transport-independent, and suitable for environments where
   accountability, provenance, and verifiable history are required.
- **draft-grund-khatoun-pujolle-serhrouchni-smrp-00** (new-draft, score 13, core_identity) [none]: [Stapled Merkle Revocation Proofs for Pseudonymous ITS Credentials (SMRP)](https://datatracker.ietf.org/doc/draft-grund-khatoun-pujolle-serhrouchni-smrp/) — Pseudonymous Intelligent Transport Systems (ITS) credentials are
   short-lived and numerous.  Verifiers decide at message-reception
   time, often without connectivity, which makes revocation status hard
   to deliver.  This document specifies Stapled Merkle Revocation Proofs
   (SMRP).  For each partition of a revocation domain, an authorized
   issuer signs a compact checkpoint that commits to the complete sorted
   set of revoked credential tokens.  A credential holder staples a
   logarithmic-size proof that its token is absent from that set, and a
   verifier checks the proof offline against the current checkpoint.
   Freshness is carried by the checkpoint, which is public, shared by
   every credential of the partition, and deliverable by any party.
   Within one stream, a proof remains usable across checkpoints for as
   long as the set commitment is unchanged and the current checkpoint is
   admissible.  The same commitment supports proofs of revocation that
   anyone can relay, complete authenticated lists for capable verifiers,
   and public audit.

   The document defines a credential identity that does not depend on
   the certificate signature, a Merkle tree over the intervals of the
   sorted revoked set with one authentication path per proof, the
   checkpoint and staple encodings, conservative time validation with a
   conditional bound on the last affirmative decision after revocation,
   verifier state with terminal revocation, and carriage in V2X secured
   messages and in TLS 1.3.  It positions SMRP against the companion
   pOCSP mechanism: pOCSP signs one statement per certificate and
   validity window, whereas SMRP signs one statement per partition and
   issuance period.  This document is Experimental and allocates no
   identifier in ETSI, IEEE, or SAE namespaces.
- **draft-gruszka-scitt-statement-identification-04** (new-draft, score 13, trust_infrastructure) [none]: [Requirements and Test Cases for Identifying SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-gruszka-scitt-statement-identification/) — This document describes proposed requirements and test cases for
   identifying SCITT Signed Statements.  It distinguishes reference
   matching from statement retrieval, signature verification, issuer
   authorization, and evidence of registration.  It examines how
   alternative identification schemes treat changes to statement
   encodings and registration context.  The requirements are input to
   technical discussion and do not represent working group consensus.
   This document does not define a common reference format, allocate a
   COSE header parameter, or establish a relationship vocabulary.  Its
   examples illustrate selected properties rather than demonstrate
   interoperability between deployed transparency services.
- **draft-kavian-aep-oauth-session-credential-05** (new-draft, score 13, core_identity) [none]: [OAuth Bearer Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-oauth-session-credential/) — This document defines the OAuth Bearer session-credential grant type
   for the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an OAuth-style Bearer access token through the AEP
   Grant command while preserving baseline AEP client assertion
   authentication as the root of trust.
- **draft-lmtlssss-exact-state-contraction-00** (new-draft, score 13, trust_infrastructure) [none]: [ta. (TAA): Exact State Contraction and Source-Bound Exact-Computation Statements](https://datatracker.ietf.org/doc/draft-lmtlssss-exact-state-contraction/) — This document defines the computer-science term ᑕ. (U+1455 U+002E),
   spoken TAA.  It denotes exact state contraction: a replacement of a
   computational representation by a retained state that preserves a
   declared observation contract for every admissible input.  The
   retained transition and observation maps commute with the full
   system, through a surjection onto the retained state, and this
   identity preserves every finite observation trace.  The document also
   specifies a portable certificate for a checked result: a COSE_Sign1
   statement with a deterministic CBOR payload that binds the exact
   artifact bytes to a registered predicate, its domain, a verdict, the
   exact checker implementation and the evidence.  The statement can be
   registered with a SCITT Transparency Service.  A signature
   authenticates the issuer's statement; a separate checker establishes
   whether the evidence supports it; a transparency receipt establishes
   registration, not mathematical correctness.
- **draft-hamr-oauth-agent-delegation-04** (new-draft, score 12, core_identity) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document builds on HTTP Message Signatures (RFC 9421) for
   requests that automated agents send on behalf of people.  RFC 9421
   shows who signed a request.  It does not show who the agent acts for,
   or what the agent may do.  This document defines an HTTP header
   field, Agent-Delegation, that carries a chain of delegation links.
   Each link can only narrow the scope, floors, and expiry of the link
   before it, and a verifier checks every link.  Floors cover two
   things.  The first is the person or account behind the agent: an
   Attestation Issuer, such as a mobile network operator or an identity-
   document check, answers with a signed yes or no, bound to the
   verifier's nonce and to an expiry, and never returns the value behind
   the answer.  The second is what the agent may do: each call has a
   class, r, w, or x, read as in chmod, with an optional count per
   class, and a signed menu gives the class of each call.  A deployment
   can set this scope for each job when the job starts.  This document
   does not define a credential format, an identity system, or
   revocation.
- **draft-ietf-rats-geographic-results-00** (new-draft, score 11, trust_infrastructure) [rats]: [Geographic Attestation Results](https://datatracker.ietf.org/doc/draft-ietf-rats-geographic-results/) — Many workloads have limitations on what geography they are allowed to
   operate in.  This is often due to a regulation that requires that the
   computation occur in a particular jurisdiction.

   There are many mechanisms by which Evidence of location may be
   created and then evaluated by a Verifier.  No matter which mechanism
   is appropriate for a given situation, the result of the Verification
   can be expressed in a similiarly defined EAT Attestation Result.

   This document is about encoding a variety of geographical conclusions
   conclusions in an Attestation Result.  In addition, one mechanism of
   directly creating a geographic result in the form of an Endorsement
   is described in an appendix.
- **draft-shuliak-sip-zero-egress-00** (new-draft, score 11, agent_identity) [none]: [Shuliak Isolation Protocol (SIP-1): Stateless Format-Preserving Pseudonymization and AST Quarantine for Local AI Agent Transports](https://datatracker.ietf.org/doc/draft-shuliak-sip-zero-egress/) — Autonomous AI agents and Model Context Protocol (MCP) servers
   frequently execute over local standard input/output (stdio) pipes
   outside enterprise network inspection perimeters.  Naive redaction of
   sensitive credentials with static placeholders invalidates downstream
   Luhn payment card and ISO-7064 IBAN schema validators, while raw
   payload forwarding exposes regulated data.  This document specifies
   the Shuliak Isolation Protocol (SIP-1), a deterministic, zero-egress
   security layer combining stateless Format-Preserving Encryption
   (FF1), Abstract Syntax Tree (AST) JSON-RPC payload quarantine, and
   detached cryptographic schema locks.
- **draft-xu-agentic-overlay-network-architecture-01** (new-draft, score 11, core_identity) [none]: [Architecture for Agentic Overlay Networks](https://datatracker.ietf.org/doc/draft-xu-agentic-overlay-network-architecture/) — This document describes an architecture for agentic overlay networks.
   It describes how autonomous software agents, agent gateways,
   registries, discovery services, and enterprise service hubs interact
   across administrative domains without replacing the existing Internet
   protocol stack.

   The architecture separates control-plane coordination from runtime
   agent interaction.  Management root nodes coordinate trust anchors,
   semantic taxonomies, and network-wide policy.  Registry service nodes
   onboard agents and publish signed capability metadata.  Discovery
   service nodes provide intent-driven candidate selection.  Enterprise
   service hubs adapt private systems and legacy interfaces into agent-
   compatible capabilities.  After discovery, runtime authentication and
   execution are performed by the invoking and target endpoints, which
   can be agents or gateways, using mutual verification; discovery and
   management nodes are not required in the runtime path.

   This document defines architectural roles, functional boundaries,
   metadata expectations, operational workflows, and security
   considerations for such networks.  It does not define a new transport
   protocol, a new URI scheme, or a mandatory discovery ranking
   algorithm.
- **draft-zhangb-dawn-entity-mdi-00** (new-draft, score 10, agent_identity) [none]: [Generalizing the DAWN MDI for All Entity Types](https://datatracker.ietf.org/doc/draft-zhangb-dawn-entity-mdi/) — The DAWN Minimum Discoverable Information (MDI) information model
   [I-D.cui-dawn-mdi-model] defines a small, encoding-neutral common
   header -- three mandatory elements, a short set of recommended and
   optional elements, and the minimal constraints among them.  In
   parallel, local-discovery work [I-D.jakab-dawn-agent-discovery-mdns]
   [I-D.blwm-dawn-common-discovery-parameters] has converged on a
   single-DNS-SD-service-type model in which one generic service type
   carries instances of every agent protocol, distinguished by a
   protocol key, with one instance per protocol and a descriptor
   reference pointing to richer metadata.

   This document generalizes the MDI information model so that the same
   minimal header describes any DAWN entity.  In the context of DAWN,
   entities include, but are not limited to, AI agents and AI resources
   [I-D.farrel-dawn-terminology].  An AI resource may be an individual
   named agent or a service such as a catalog that will further the
   discovery process, and the model is designed to extend cleanly to
   tools, tasks, data sources, models, workloads, brokers, and
   application endpoints.  The generalization reuses the existing agent
   MDI without change: the element set, the constraints, and the DNS-SD
   binding are inherited, and extension is achieved by opening the value
   space of one element (entity type) and by per-type profiles, not by
   new core elements.  Clients discover agents, MCP servers, LLM API
   services, and future entity types with a single browse; operators
   manage one service type.
- **draft-ietf-ace-coap-pubsub-profile-06** (new-draft, score 9, authorization) [ace]: [CoAP Publish-Subscribe Profile for Authentication and Authorization for Constrained Environments (ACE)](https://datatracker.ietf.org/doc/draft-ietf-ace-coap-pubsub-profile/) — This document defines an application profile of the Authentication
   and Authorization for Constrained Environments (ACE) framework, to
   enable secure group communication in the Publish-Subscribe (Pub-Sub)
   architecture for the Constrained Application Protocol (CoAP)
   specified in draft-ietf-core-coap-pubsub, where Publishers and
   Subscribers communicate through a Broker.  This profile relies on
   protocol-specific transport profiles of ACE to achieve communication
   security, server authentication, and proof of possession of a key
   owned by the Client and bound to an OAuth 2.0 access token.  This
   document specifies the provisioning and enforcement of authorization
   information for Clients to act as Publishers and/or Subscribers, as
   well as the provisioning of keying material and security parameters
   that Clients use for protecting their communications end-to-end
   through the Broker.

   Note to RFC Editor: Please replace "draft-ietf-core-coap-pubsub" with
   the RFC number of that document and delete this paragraph.
- **draft-ietf-sidrops-aspa-profile-31** (new-draft, score 9, authorization) [sidrops]: [A Profile for Autonomous System Provider Authorization](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Provider Authorization (ASPA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASPA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier), can authorize one or more
   other Autonomous Systems (ASes) as its transit providers.  When
   validated, an ASPA's eContent can be used for detection and
   mitigation of route leaks.
- **draft-schrock-oauth-exact-action-identifiers-00** (new-draft, score 9, authorization) [none]: [Exact-Action Identifiers in OAuth Authorization Details](https://datatracker.ietf.org/doc/draft-schrock-oauth-exact-action-identifiers/) — This document defines an action_id member for OAuth Rich
   Authorization Requests authorization details types that explicitly
   adopt it.  The member carries a scheme-qualified identifier of an
   action description.  A resource server derives an identifier from the
   operation it is about to perform and compares it with the identifier
   in the granted authorization details.

   The document requests a registry of exact-action identifier schemes
   and an initial entry for version 1 of the Canonical Action
   Identifier.  It specifies authorization server processing, resource
   server comparison, and discovery metadata without choosing a
   universal action vocabulary or digest construction.  Identifier
   equality is an additional condition on authorization; it does not
   establish permission, a single-use grant, execution, or the truth of
   externally supplied action data.
- **draft-gu-nmrg-intent-translator-05** (new-draft, score 8, agent_identity) [none]: [An Agentic AI Framework for Hallucination Mitigation in Network Intent Translation](https://datatracker.ietf.org/doc/draft-gu-nmrg-intent-translator/) — This document describes an agentic AI workflow for detecting and
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
- **draft-ietf-opsawg-yang-provenance-09** (new-draft, score 8, verifiable_claims) [opsawg]: [Applying COSE Signatures for YANG Data Provenance](https://datatracker.ietf.org/doc/draft-ietf-opsawg-yang-provenance/) — This document defines a mechanism based on CBOR Object Signing and
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
- **draft-meunier-webbotauth-capacity-management-00** (new-draft, score 8, core_identity) [none]: [PACE: Capability Management for Agents](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-capacity-management/) — This document addresses the noisy neighbour problem without requiring
   a stable client identifier at the origin.  Separately allocated
   budgets let origins limit consumption beneath a shared platform
   identity.  It describes PACE: a framework for managing budget
   continuity across requests using a composition of the Web Bot Auth
   with the Moderation of unLinkable Endorsements (MOLE) architecture
   [MOLE-ARCH] and protocols [MOLE-PROTOCOLS].  This composition allows
   for per-client capacity management in a way that allows origins to
   serve clients above an otherwise constrained public baseline.
- **draft-arsentev-crawler-traffic-reporting-00** (new-draft, score 7, core_identity) [none]: [Reporting Crawler Traffic by Verification Level](https://datatracker.ietf.org/doc/draft-arsentev-crawler-traffic-reporting/) — The User-Agent header is written by the client.  It is a claim, not
   an identity.  Reports of crawler and AI crawler traffic that count
   requests by User-Agent token alone present claims as activity.  This
   document defines four counts a crawler traffic report should give per
   crawler token: declared, route-consistent, verified, and
   unverifiable.  It states which verification check was possible at the
   vantage point where the log was taken.  It also defines a small JSON
   report object.
- **draft-grund-v2x-pocsp-00** (new-draft, score 7, core_identity) [none]: [Pseudonymous Stapled Certificate Status Evidence for V2X and TLS with ITS Certificates (pOCSP)](https://datatracker.ietf.org/doc/draft-grund-v2x-pocsp/) — Vehicle-to-Everything (V2X) systems authenticate broadcast and
   unicast messages with short-lived pseudonymous certificates.
   Revocation status validation is difficult in this environment:
   Certificate Revocation Lists (CRLs) can be costly to distribute at
   pseudonym scale, while verifier-initiated OCSP requests introduce
   online dependencies, latency, metadata leakage, and denial-of-service
   exposure.

   This document specifies pOCSP, an OCSP-derived response type and a
   set of deployment profiles for short-lived certificate-status
   evidence that is obtained by the certificate holder and stapled to an
   authenticated message or TLS CertificateEntry.  A verifier validates
   pOCSP evidence locally, without contacting a responder at message-
   reception time.  pOCSP retains the OCSP status semantics good,
   revoked, and unknown; defines an explicit signed usage context;
   defines a compact context-specific certificate identifier; and
   specifies deterministic, bounded validation, caching, and failure
   behavior. pOCSP does not claim that its identifier is unlinkable.
   The identifier is deterministic and can be correlated whenever the
   underlying certificate is observable or inferable.  The V2X profiles
   therefore require single-certificate evidence and prohibit
   transmitting pOCSP evidence more frequently than the corresponding
   full certificate.  The document prohibits future-active good
   evidence, bounds replay by mandatory thisUpdate and nextUpdate
   values, and makes an authenticated revocation terminal at the
   verifier: omitted, expired, unknown, or higher-versioned good
   evidence cannot mask it.  It defines profiles for ETSI CAM/DENM, SAE
   J2735 messages, and TLS 1.3 with ITS certificates, requests an OCSP
   response-type object identifier, and establishes a registry of pOCSP
   profile identifiers.
- **draft-jones-scitt-dual-receipt-00** (new-draft, score 7, core_identity) [none]: [A Dual-Receipt Profile for Binding a Decision Statement to an Independent Policy Evaluation Statement](https://datatracker.ietf.org/doc/draft-jones-scitt-dual-receipt/) — This document specifies a dual-receipt profile for recording one
   disbursement decision as two signed statements, made by two different
   parties and registered with the same Transparency Service.  An
   approver acting for a fiscal sponsor signs a Decision Statement.  A
   validator acting for a receiving institution signs a Policy
   Evaluation Statement that binds to the Decision Statement's
   identifier, receipt, and signature, and records the outcome of a
   named policy.  The profile defines the JSON members of both
   statements, a canonical encoding based on the JSON Canonicalization
   Scheme, SHA-256 statement identifiers, a composite identifier, Merkle
   tree receipts that use the hashing rules of RFC 9162, and a
   verification procedure.  It also states the limits of the evidence: a
   bundle of statements cannot show that no conflicting evaluation
   exists, and the times inside the statements are claims made by their
   signers.
- **draft-kavian-aep-api-key-session-credential-05** (new-draft, score 7, core_identity) [none]: [API-Key Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-api-key-session-credential/) — This document defines the API-key session-credential grant type for
   the Agent Enrollment Protocol (AEP).  The grant type lets an AEP
   Service issue an opaque API key through the AEP Grant command for
   deployments that already operate header-based API-key authentication.
- **draft-kavian-aep-basic-session-credential-05** (new-draft, score 7, core_identity) [none]: [Basic Session Credential Grant Type for the Agent Enrollment Protocol](https://datatracker.ietf.org/doc/draft-kavian-aep-basic-session-credential/) — This document defines the Basic session-credential grant type for the
   Agent Enrollment Protocol (AEP).  The grant type lets an AEP Service
   issue an HTTP Basic credential through the AEP Grant command for
   deployments that already integrate with Basic authentication
   middleware.

## Monitor

- **draft-atwood-mimi-provider-auth-00** (new-draft, score 6, core_identity) [none]: [Provider Authentication for More Instant Messaging Interoperability (MIMI)](https://datatracker.ietf.org/doc/draft-atwood-mimi-provider-auth/) — The MIMI protocol requires each provider to authenticate the provider
   that sends it a request.  It specifies mutually authenticated TLS for
   this, but not where the client certificates come from or which trust
   anchors check them.  The public Web PKI has stopped issuing such
   certificates.  This document defines how MIMI providers authenticate
   each other without it.  The mechanism every provider implements is a
   key published in DNS under the provider's domain, used to sign each
   request with HTTP Message Signatures.  DANE client certificates,
   client certificates from configured PKIX trust anchors, and locally
   configured trust lists are defined as additional mechanisms that a
   provider can accept by local policy.
- **draft-ietf-lake-edhoc-psk-11** (new-draft, score 6, core_identity) [lake]: [LAKE Authenticated with Pre-Shared Keys (PSKs)](https://datatracker.ietf.org/doc/draft-ietf-lake-edhoc-psk/) — This document specifies a Pre-Shared Key (PSK) authentication method
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
- **draft-ietf-nmop-message-broker-telemetry-message-06** (new-draft, score 6, trust_infrastructure) [nmop]: [Extensible YANG Model for Network Telemetry Messages](https://datatracker.ietf.org/doc/draft-ietf-nmop-message-broker-telemetry-message/) — This document defines an extensible message schema in YANG to be used
   at data collection to transform Network Telemetry messages into
   external systems such as Message Brokers.  The extensible message
   schema enables data collectors to add metadata for the provenance of
   the operational network data.
- **draft-knauer-secure-webhook-token-03** (new-draft, score 6, core_identity) [none]: [Secure Webhook Token (SWT)](https://datatracker.ietf.org/doc/draft-knauer-secure-webhook-token/) — The Secure Webhook Token (SWT) is a specialized JSON Web Token (JWT)
   format designed for securely authorizing and verifying webhook
   requests.  It defines a set of claims to ensure that the token is
   explicitly tied to webhook events and that its integrity can be
   reliably validated by the recipient.  A key feature of SWT is the
   introduction of a unique claim, webhook, which encapsulates webhook-
   specific information, such as the event type.

   By providing a structured and secure approach to webhook
   authentication, SWT aims to be a lightweight and flexible solution
   while maintaining compatibility with typical JWT structures.  It is
   designed with the best practices in mind and may serve as a
   foundation for future standardization efforts.
- **draft-rkr-synthetic-twin-header-00** (new-draft, score 6, core_identity) [none]: [The Synthetic-Twin HTTP Field](https://datatracker.ietf.org/doc/draft-rkr-synthetic-twin-header/) — This document defines the Synthetic-Twin HTTP field.  A sender adds
   the field to an HTTP request or response to say that the message was
   made by, or for, a synthetic twin and is not real user activity.  A
   synthetic twin is a software model of a network estate, existing or
   planned.  The field says which kind of synthetic message it is and
   can carry one opaque identifier.  This lets operators keep synthetic
   messages apart from production messages in logs, analytics, billing,
   and alerting.
- **draft-srivastava-learnlog-04** (new-draft, score 6, adjacent_watchlist) [none]: [Learnlog: An Assistance Capture Profile and Event File Format](https://datatracker.ietf.org/doc/draft-srivastava-learnlog/) — When a learner works with an AI tutor or assistant, or earns a
   credential or completes training with software in the loop, the
   formats learning systems share do not by themselves fix how to record
   what help was asked for, offered, shown, or accepted, or which of
   those facts were observed, self-reported, or inferred.  Learnlog is a
   capture profile for that: a small set of assistance states, a
   declared observation boundary, explicit unknowns, and a basis for
   every assertion, carried inside xAPI and Caliper, which learning
   systems already use.  It also defines an optional event file format
   for deployments that need integrity: entries chained by hash, signed
   heads, and redaction that leaves every hash verifiable.
- **draft-abak-ai-evaluation-claim-preservation-01** (new-draft, score 5, authorization) [none]: [Claim-Preserving Exchange of AI Evaluation Evidence](https://datatracker.ietf.org/doc/draft-abak-ai-evaluation-claim-preservation/) — AI evaluation records can pass through evaluation frameworks,
   exporters, evidence services, independent reviewers, and systems that
   make decisions.  A conversion can retain a score while losing whether
   the measurement ran, which result was selected, whether a criterion
   existed, or which evidence was unavailable.  Authenticating the
   converted record does not recover these distinctions.

   This document specifies format-neutral requirements for mapping
   profiles and consumers that exchange AI evaluation evidence.  It
   separates source assertions, explicit derivations, and later policy
   judgments; requires claim-relevant loss and uncertainty to remain
   visible; and describes consumer behavior when preservation cannot be
   established.  It includes synthetic counterexamples and guidance for
   composition with existing evidence mechanisms.  It defines neither a
   wire format nor an evaluation benchmark, safety certification,
   authorization protocol, or new cryptographic envelope.  A concrete
   mapping profile is needed for interoperable implementation.
- **draft-dvojmoc-reception-forwarding-limits-00** (new-draft, score 5, agent_identity) [none]: [Depth and Fanout Bounding for Agent-to-Agent Discovery Forwarding](https://datatracker.ietf.org/doc/draft-dvojmoc-reception-forwarding-limits/) — This document describes a mechanism, deployed in production as
   part of the "AI Docking Port" discovery protocol, for bounding the
   traffic cost of stateless agent-to-agent forwarding across a
   network of independent nodes with no central registry.  When a
   node forwards a request to its neighbors, and those neighbors may
   forward again, request cost grows as fanout^depth; absent an
   explicit bound this cost is paid by relaying operators rather than
   the requester.  This document specifies two operator-controlled
   limits, max_depth and max_fanout, published in a node's discovery
   manifest, and the forwarding behavior they constrain.  It is
   submitted for discussion as a possible contribution to ongoing
   community work on agent discovery and invocation protocols,
   including the W3C Community Group "AI Agent Protocol".
- **draft-gunuganti-agent-approval-evidence-00** (new-draft, score 5, adjacent_watchlist) [none]: [Owner-Approved Agent Spending with Sealed Evidence: The Approval-Evidence Object for Agent Action Protocols](https://datatracker.ietf.org/doc/draft-gunuganti-agent-approval-evidence/) — When a software agent acts for a person — in particular when it
   spends the person's money — the approval at the centre of the
   flow is, in current agent protocols, a statement by the agent
   itself. The Personal Agent Protocol's Operations extension
   states the consequence in its own security considerations: an
   approval there does not prove that the user saw the terms or
   approved them; it "works on trust". This document describes the
   design of a running system that removes the trust step for the
   approval half of the problem — an owner-set, machine-checkable
   mandate; a deterministic check performed and recorded before any
   spendable token exists; approval by the owner on a surface the
   agent cannot operate or imitate; a single-use decision token
   bound to the hash of the exact action approved; and a sealed,
   owner-held receipt that grades its contents (approval PROVEN;
   the performer's completion report, including payment facts,
   REPORTED and PINNED) — and specifies an optional
   approval-evidence object that agent action protocols can carry
   so that a relying party can verify an approval mechanically
   instead of trusting the agent's assertion.
- **draft-lisboa-ctpip-01** (new-draft, score 5, core_identity) [none]: [Causal Time Protocol (CTP/IP): Proof of Transformation Seal Verification and Wire Protocol](https://datatracker.ietf.org/doc/draft-lisboa-ctpip/) — This document describes how any party verifies a Proof of
   Transformation seal issued under the Causal Time Protocol (CTP/IP),
   and the wire protocol used to invoke a LUX Runtime and to request
   seal verification over a network.  A seal attests that a
   transformation declared in advance by a Human Agency, through a
   signed Intention Signature (IntentSig), was validated by the LUX
   Runtime, and that the resulting certificate was committed to a Merkle
   batch anchored on the Solana and Bitcoin public ledgers.

   The document specifies the certificate fields, the five layer
   verification procedure, the artifact identity check, the message
   types and envelope of the wire protocol, and the IANA registrations
   the protocol requests.  It does not specify the measurement method by
   which a LUX Runtime computes the Coherence Index; that method is
   outside the scope of this document.

   One seal attests intent, human origin, decision authority,
   authorship, substance, causal time and anchoring, for a Human Agency
   and for any agent acting under it.  The protocol has been in
   development since 2020 and is deployed.  Its canonical specification
   is published as Corpus Delta 1 under DOI 10.5281/zenodo.21950371.
- **draft-nestorov-scitt-p10-underdetermination-03** (new-draft, score 5, trust_infrastructure) [none]: [P10 Underdetermination Profile: Adjudication Statements over SCITT](https://datatracker.ietf.org/doc/draft-nestorov-scitt-p10-underdetermination/) — P10 defines a third-party-verifiable binding for
   NotDemonstrated(reason=underdetermined).  A conforming P10
   Adjudication Statement carries two canonical witness worlds that are
   compatible with the same closed evidence set and produce different
   values for the same frozen claim.  The witness result is checked
   against committed profile semantics and bound into a SCITT
   Transparent Statement containing an in-toto Statement v1 predicate.
   The result establishes underdetermination only relative to the
   declared profile and does not identify the actual world or establish
   either claim value as true.
- **draft-spiriyath-dhc-ai-gateway-uri-00** (new-draft, score 5, adjacent_watchlist) [none]: [DHCP and DHCPv6 Options for an AI Gateway URI](https://datatracker.ietf.org/doc/draft-spiriyath-dhc-ai-gateway-uri/) — This document specifies a DHCPv4 option and a DHCPv6 option that
   carry the HTTPS URI of an AI gateway descriptor.  The descriptor is a
   Provisioning Domain Additional Information document.  It identifies a
   forward proxy and the destinations for which that proxy is to be
   used.  The DHCP options do not carry proxy credentials, model
   identifiers, or a Proxy Auto-Configuration script.
- **draft-srivastava-agentproto-handoff-context-02** (new-draft, score 5, agent_identity) [none]: [Signed Handoff Context for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-srivastava-agentproto-handoff-context/) — When one agent hands a task to another, the receiver needs to know
   who handed it over, on whose behalf, through which earlier agents,
   and which prior context the work depends on.  It needs to know the
   handoff is fresh and meant for it, and the sender needs a clear
   answer back.  This document defines a small, transport-neutral
   handoff context: a signed offer, a signed status reply, and the chain
   of earlier offers that led to the current one, in CDDL for JSON and
   CBOR, with a lifecycle that maps to Agent2Agent task states.  Each
   offer names the one before it by hash, so a dropped or reordered
   intermediate hop is detectable when the chain is carried.  Prior
   context is named by digest only.  The document is input to the
   agentproto working group's use cases and dialog-context work.
- **draft-taylor-cose-receipts-rfc9162-sha384-sha512-00** (new-draft, score 5, verifiable_claims) [none]: [SHA-384 and SHA-512 Binary Merkle Tree Verifiable Data Structures for COSE Receipts](https://datatracker.ietf.org/doc/draft-taylor-cose-receipts-rfc9162-sha384-sha512/) — RFC 9942 defines COSE Receipts and registers one verifiable data
   structure, RFC9162_SHA256, the binary Merkle tree of RFC 9162
   instantiated with SHA-256.  This document registers two more:
   RFC9162_SHA384 and RFC9162_SHA512, the same tree instantiated with
   SHA-384 and SHA-512, each with its inclusion and consistency proof
   types.  The tree construction, proof formats, and verification
   algorithms are unchanged apart from the hash function and the
   resulting digest size.
- **draft-xu-efficient-agent-discovery-profile-01** (new-draft, score 5, adjacent_watchlist) [none]: [Metadata and Query Profile for Efficient Agent Discovery](https://datatracker.ietf.org/doc/draft-xu-efficient-agent-discovery-profile/) — This document defines a metadata and query profile for efficient
   discovery of autonomous software agents.  The profile describes how
   agents publish capability metadata using explicit tags, natural-
   language descriptions, example tasks, protocol bindings, and
   operational constraints.  It also defines JSON metadata, discovery
   request, and discovery response objects that enable discovery
   services to combine structured filtering, semantic retrieval, and
   fine-grained matching while preserving an interoperable protocol
   surface.

   The profile does not mandate a specific machine-learning model,
   embedding model, database, or ranking algorithm.  Instead, it
   standardizes the metadata and result evidence needed by clients and
   discovery services so that different implementations can interoperate
   while optimizing their own latency, scalability, and ranking quality.
- **draft-bonica-macneil-singh-ipv6-firewall-metadata-01** (new-draft, score 4, adjacent_watchlist) [none]: [Verifiable Firewall and Security-Enforcement Metadata in IPv6](https://datatracker.ietf.org/doc/draft-bonica-macneil-singh-ipv6-firewall-metadata/) — This document defines a way to carry a verifiable record of security
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

## Adjacent / watchlist

- **draft-claise-green-capability-discovery-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
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
- **draft-ietf-detnet-glbf-04** (new-draft, score 3, adjacent_watchlist) [detnet]: [Deterministic Networking (DetNet) Data Plane - guaranteed Latency Based Forwarding (gLBF) for bounded latency with low jitter and asynchronous forwarding in Deterministic Networks](https://datatracker.ietf.org/doc/draft-ietf-detnet-glbf/) — This memo proposes a mechanism called "guaranteed Latency Based
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
- **draft-ietf-dmm-udp-tunnel-acaas-extn-04** (new-draft, score 3, adjacent_watchlist) [dmm]: [A YANG Data Model Extension for Attachment Circuit as a Service with UDP Tunnel Support](https://datatracker.ietf.org/doc/draft-ietf-dmm-udp-tunnel-acaas-extn/) — Delivery of network services over a Layer 3 tunnel assumes that the
   appropriate setup is provisioned over links that connect the customer
   termination points and provider network.  The required setup to allow
   successful data exchange over these links is referred to as an
   attachment circuit (AC) while the underlying link for carrying
   network services is referred to as "bearer", in this case a Layer 3
   UDP tunnel.

   This document specifies an extension for UDP tunnel as Layer 3 bearer
   to the YANG service data model for AC.
- **draft-ietf-green-power-and-energy-yang-06** (new-draft, score 3, adjacent_watchlist) [green]: [Power and Energy YANG Module](https://datatracker.ietf.org/doc/draft-ietf-green-power-and-energy-yang/) — This document defines a YANG data model for Power and Energy
   monitoring and control of devices within or connected to
   communication networks.
- **draft-ietf-jmap-calendars-34** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-opsawg-collected-data-manifest-17** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A Data Manifest for Contextualized Telemetry Data](https://datatracker.ietf.org/doc/draft-ietf-opsawg-collected-data-manifest/) — Network platforms use Network Telemetry, such as YANG-Push (RFC
   8641), to continuously stream information, including both counters
   and state information.  This document describes the metadata that
   ensure that the collected data can be interpreted correctly.  This
   document specifies the Data Manifest, composed of two YANG data
   models (the Platform Manifest and the non-normative Data Collection
   Manifest).  These YANG modules are specified at the network level
   (e.g., network controllers) to provide a model that encompasses
   several network platforms.  The Data Manifest must be streamed and
   stored along with the data, up to the collection and analytics
   systems to keep the collected data fully usable by the data
   scientists and relevant tools.  Additionally, this document specifies
   an augmentation of the YANG-Push model to include the actual
   collection period, in case it differs from the configured collection
   period.
- **draft-ietf-sidrops-8210bis-29** (new-draft, score 3, authorization) [sidrops]: [The Resource Public Key Infrastructure (RPKI) to Router Protocol, Version 2](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/) — In order to validate the origin Autonomous Systems (ASes) and
   Autonomous System relationships behind BGP announcements, routers
   need a simple but reliable mechanism to receive Resource Public Key
   Infrastructure (RPKI, RFC 6480) prefix origin data, Router Keys, and
   Autonomous System Provider Authorization (ASPA) data from a trusted
   cache.  This document describes a protocol to deliver them.

   This document describes version 2 of the RPKI-to-Router protocol.
   RFC 6810 describes version 0 while RFC 8210 describes version 1.
   This document is compatible with both.
- **draft-ietf-spring-stamp-srpm-srv6-11** (new-draft, score 3, core_identity) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths including Segment Lists of SR Policies, SRv6 IGP
   best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 and Layer-2 services carried over those paths.

   This document updates RFC 8972 for the definition of the STAMP
   session identifier for SRv6.
- **draft-melo-dap-visual-oob-auth-00** (new-draft, score 3, authorization) [none]: [Dynamic Authorization Protocol (DAP): Out-of-Band Visual Transaction Authorization for Untrusted Terminals](https://datatracker.ietf.org/doc/draft-melo-dap-visual-oob-auth/) — This document specifies the Dynamic Authorization Protocol (DAP), an
   Out-of-Band (OOB) visual transaction authorization protocol, used as
   a second factor, for electronic financial transactions initiated on
   untrusted terminals.  The terminal displays a cryptographically
   protected challenge as a Quick Response (QR) code.  A trusted mobile
   device of the user, which needs no network connection, scans the
   code, verifies it with HMAC-SHA-256, shows the transaction details
   for confirmation ("What You See Is What You Sign"), and then reveals
   a one-time authorizer code protected with AES-256.  Each challenge is
   bound to one transaction and expires within 120 seconds.  The
   document also describes the provisioning of the shared key through a
   dual-channel XOR split-key exchange, its activation, and the
   templates used to display transactions.  DAP targets Man-in-the-
   Middle (MITM) and Man-in-the-Browser (MITB) adversaries that control
   the terminal and alter transaction parameters.
- **draft-wang-ipsecme-kem-auth-ikev2-05** (new-draft, score 3, core_identity) [none]: [KEM-based Authentication for IKEv2 with Post-quantum Security](https://datatracker.ietf.org/doc/draft-wang-ipsecme-kem-auth-ikev2/) — This draft specifies a new authentication mechanism, called KEM (Key
   Encapsulation Mechanism) -based authentication, for the Internet Key
   Exchange Protocol Version 2 (IKEv2).  This is motivated by the fact
   that some post-quantum KEMs (like ML-KEM) are more efficient than
   post-quantum signature algorithms (like ML-DSA).
- **draft-bates-atp-test-vectors-01** (new-draft, score 2, ignored_after_review) [none]: [ATP Core Test Vectors](https://datatracker.ietf.org/doc/draft-bates-atp-test-vectors/) — This document publishes golden test vectors for the Agent Transaction
   Protocol (ATP).  The vectors cover canonicalization (RFC 8785 JCS),
   nodeId computation, and Ed25519 signature generation and
   verification.  ATP Core conformance requires that conformant
   implementations pass all vectors in this document for
   canonicalization, nodeId computation, and Ed25519 signature
   verification.
- **draft-besleaga-agentic-knowledge-wellknown-02** (new-draft, score 2, ignored_after_review) [none]: [The 'knowledge-linkset' Well-Known URI for Publishing Knowledge Artefacts](https://datatracker.ietf.org/doc/draft-besleaga-agentic-knowledge-wellknown/) — This document defines the "knowledge-linkset" well-known URI, at
   which a web origin publishes one link set describing the knowledge
   artefacts it makes available: graph serializations, a JSON-LD
   context, an agent-facing text file, a chunk export, a change ledger,
   and related resources.  Each artefact link may carry a SHA-256
   digest, expressed with the syntax of HTTP digest fields, so that a
   client can check that a retrieved artefact is the one the publisher
   described.  A profile URI identifies the conventions the link set
   follows.  The mechanism defines no new media type and no new link
   relation type: a page points at the resource with the existing
   "describedby" relation.  The profile URI is registered in the IANA
   "Profile URIs" registry.  This document requests no IANA action.
- **draft-ranjbar-regext-rdap-subordinate-referrals-03** (new-draft, score 2, ignored_after_review) [none]: [Referrals to Holder-Designated RDAP Services for Subordinate Resources](https://datatracker.ietf.org/doc/draft-ranjbar-regext-rdap-subordinate-referrals/) — An RDAP query can be followed from the IANA bootstrap registries down
   to the most specific object a registry operator holds, and no
   further.  When the holder of a registered resource keeps registration
   data for resources below it, such as names below a registered domain
   or more-specific networks below an address allocation, and publishes
   that data from an RDAP service of its own, a client has no in-band
   way to find that service.  This document describes how a registry
   operator refers clients to such a holder-designated service.  The
   registry redirects lookups for subordinate resources to the holder's
   service, so an unchanged client receives the most specific record as
   it would from any other redirect.  On top of that, the covering
   object can advertise the holder's service, so a client that cares can
   discover the delegation and cross the authority boundary knowingly.
   The document uses the redirect controls and object relations of
   draft-ietf-regext-rdap-referrals and the service relations of draft-
   ietf-regext-rdap-extensions, and defines no new ones.

## Ignored after review

- **draft-abraitis-idr-addpath-paths-limit-08** (new-draft, score 0, ignored_after_review) [none]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.

   This document also defines a new BGP Cease NOTIFICATION message
   subcode, "Maximum Number of Paths Reached", used when a BGP speaker
   terminates a peering because the number of paths received from a
   neighbor for a prefix exceeds the Paths Limit advertised in the
   PATHS-LIMIT Capability.
- **draft-alivar-spring-icmp-error-srv6-vpn-00** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling for VPNs in SRv6 Networks](https://datatracker.ietf.org/doc/draft-alivar-spring-icmp-error-srv6-vpn/) — The document specifies procedures for handling ICMP error messages in
   SRv6-based Virtual Private Network (VPN).  It describes three methods
   to improve the ICMP Error Handling for SRv6-VPNs.
- **draft-atwood-jmap-updates-00** (new-draft, score 0, ignored_after_review) [none]: [Updates to JMAP: Localized Display Text, Text Handling, URIs, and Problem Details](https://datatracker.ietf.org/doc/draft-atwood-jmap-updates/) — JMAP (RFC 8620) carries all data as UTF-8 I-JSON, lets a client name
   a collation for sorting, and lets a server localize user-visible
   strings from the request's Accept-Language header.  It has no way to
   store or return display text, such as the name of a mailbox, address
   book, or quota, in more than one language, and no way to say which
   language a stored string is in.  This document defines the
   urn:ietf:params:jmap:i18n capability, which adds locale and
   localizations properties, modelled on JSCalendar (RFC 8984), to the
   display text of existing JMAP data types, and a language argument
   with which a client asks for one language.  For clients that use that
   argument, this document updates RFC 9425, which selects the Quota
   description by Accept-Language.  It also updates RFC 8620 with
   guidance for all JMAP specifications on text profiles, Unicode
   normalization, truncation, and the use of display text, and asks that
   URI-valued properties follow RFC 3986 and that every JMAP HTTP
   resource report errors as RFC 9457 problem details.
- **draft-banffy-httpbis-not-a-freezer-00** (new-draft, score 0, ignored_after_review) [none]: [The Hypertext Transfer Protocol Status Code 483 (I'm Not a Freezer)](https://datatracker.ietf.org/doc/draft-banffy-httpbis-not-a-freezer/) — This document defines the Hypertext Transfer Protocol status code 483
   (I'm Not a Freezer).  A server returns this status code when it
   understands a request that requires freezing or refrigeration
   capabilities but is not capable of providing those capabilities.

   This document also clarifies the distinction between a freezer, a
   refrigerator, a server operating at a low temperature, a frozen
   software process, and an online service advertising "cold storage".
- **draft-claise-opsawg-ipfix-ordered-ie-03** (new-draft, score 0, ignored_after_review) [none]: [Ordered Information Element Export in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/) — The IP Flow Information Export (IPFIX) protocol allows the same
   Information Element to appear multiple times in a Template Record.
   RFC 7011 states that multiple occurrences of the same Information
   Element SHOULD follow the logical order of their treatments by the
   Metering Process; however, no protocol mechanism exists for the
   Exporting Process to explicitly signal to the Collecting Process that
   this ordering is guaranteed.  Without such a guarantee, the
   Collecting Process cannot safely interpret repeated Information
   Elements as ordered observations.  This document describes the
   problem, presents use cases, analyzes candidate solutions, and
   specifies a mechanism, a new Ordered Set type, that establishes an
   end-to-end ordering guarantee: the Metering Process records repeated
   Information Element values in the order the corresponding
   observations are made, the Exporting Process preserves and signals
   this guarantee, and the Collecting Process interprets the n-th
   occurrence of an Information Element as corresponding to the n-th
   observation by the Metering Process at the Observation Point.  This
   document updates RFC 7011, RFC 5476, and RFC 6183.
- **draft-claise-opsawg-ipfix-ordered-mpls-ie-01** (new-draft, score 0, ignored_after_review) [none]: [Generic MPLS Information Elements for Ordered Export in IPFIX](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-mpls-ie/) — This document defines new generic IPFIX Information Elements for MPLS
   label stacks and label attributes, intended for use with the ordered
   set mechanisms that provide an explicit ordering guarantee for
   repeated Information Elements.
- **draft-gandhi-bpm-stamp-signaling-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Signaling Parameters](https://datatracker.ietf.org/doc/draft-gandhi-bpm-stamp-signaling/) — The Simple Two-Way Active Measurement Protocol (STAMP) specified in
   RFC 8762 supports active measurement of network performance without a
   control channel to pre-signal session parameters.  RFC 8972 defines
   optional extensions in the form of Type-Length-Value (TLV) elements
   for STAMP.  This document defines a STAMP Type-Length-Value (TLV)
   that allows a Session-Sender and a Session-Reflector to exchange
   measurement capabilities and configuration parameters in STAMP-Test
   packets.  The Session-Sender uses the returned parameters to
   configure a STAMP session.
- **draft-gandhi-lsr-stamp-01** (new-draft, score 0, ignored_after_review) [none]: [IS-IS, OSPF, BGP-LS, and BGP Extensions for Advertising STAMP Session-Reflectors](https://datatracker.ietf.org/doc/draft-gandhi-lsr-stamp/) — The Simple Two-Way Active Measurement Protocol (STAMP), as defined in
   RFC 8762, can be utilized for active measurement without relying on a
   control channel to pre-signal session parameters.  This document
   defines extensions to IS-IS, OSPF, BGP-LS, and BGP to advertise
   information for discovering STAMP Session-Reflectors in a network.
   The advertised information can be used by STAMP senders to set up
   appropriate performance measurement sessions for delay and packet
   loss metrics.
- **draft-harano-xb64-00** (new-draft, score 0, ignored_after_review) [none]: [XB64: A Lightweight Reversible Obfuscation Encoding](https://datatracker.ietf.org/doc/draft-harano-xb64/) — This document specifies XB64 (XORed Base64), a lightweight reversible
   obfuscation encoding scheme for situations where immediate
   readability of source data is undesirable but cryptographic
   confidentiality is not required.

   To provide a key-dependent yet fully reversible representation, XB64
   applies repeating-key XOR to arbitrary octet sequences and encodes
   the result as printable ASCII text using Base64 as specified in RFC
   4648.  The resulting text itself preserves the source information,
   allowing exact reconstruction with the same key without external data
   lookup, while remaining suitable for human handling and exchange
   through text-oriented systems.

   By specifying a common encoding format for this level of obfuscation,
   this document aims to enable interoperable use across different
   applications, platforms, and implementations.
- **draft-ietf-bpm-alt-mark-deployment-01** (new-draft, score 0, ignored_after_review) [bpm]: [An Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-bpm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   Alternate Marking methodology.
- **draft-ietf-detnet-tcqf-03** (new-draft, score 0, ignored_after_review) [detnet]: [Deterministic Networking (DetNet) Data Plane - Tagged Cyclic Queuing and Forwarding (TCQF) for bounded latency with low jitter in large scale DetNets](https://datatracker.ietf.org/doc/draft-ietf-detnet-tcqf/) — This memo specifies a forwarding method for bounded latency and
   bounded jitter for Deterministic Networks.  It is a variant of the
   IEEE TSN 802.1Q(ch) Cyclic Queuing and Forwarding (CQF) method,
   called Tagged CQF (TCQF), in which the cycle number is indicated in
   an existing or new packet header field, called the cycle tag.  This
   tag allows more than two cycles to be used and replaces the cycle
   mapping of CQF, which is based purely on the synchronized reception
   clock.

   Whereas CQF supports low end-to-end jitter across limited-scale
   networks with link speeds mostly up to 10Gbps, TCQF supports the same
   low end-to-end jitter across large-scale, wide-area networks with
   high per-hop latency and jitter (which is not possible with CQF), and
   enables high-speed hardware implementations above 10Gbps without
   requiring more accurate clock synchronization.  Like CQF, TCQF
   eliminates the need for per-DetNet-flow state on midpoint routers,
   requiring only flow-agnostic cycle state.  Because it is specified as
   a DetNet scheduling method, TCQF can be deployed not only as a sub-
   network method, but also as part of a DetNet forwarder.

   This memo standardizes TCQF as a mechanism independent of the tagging
   method used.  It also specifies tagging via (1) the existing MPLS
   packet Traffic Class (TC) field for MPLS packets, (2) the IP/IPv6
   DSCP field for IP/IPv6 packets, and (3) a new TCQF Option header for
   IPv6 packets.
- **draft-ietf-dmm-mup-architecture-04** (new-draft, score 0, ignored_after_review) [dmm]: [Mobile User Plane Architecture for Distributed Mobility Management](https://datatracker.ietf.org/doc/draft-ietf-dmm-mup-architecture/) — This document defines the Mobile User Plane (MUP) architecture for
   Distributed Mobility Management (DMM).  MUP meets the DMM
   requirements in [RFC7333] in a routing fashion.  MUP provides a
   normative mechanism that makes it possible to avoid traversing a
   single user plane anchor far from the optimal route, by turning
   mobile user plane session information into routing information and
   integrating the user plane into the dataplane.

   MUP is designed as a pluggable user plane part of existing mobile
   service architectures, with auto-discovery.  Although the
   architecture is dataplane-independent, this document describes MUP
   with an SRv6 dataplane (SRv6 MUP), whose programmability and large
   address space suit scalable mobile services.

   This mechanism is specified in terms of the semantics of MUP segments
   and of the routing information, how that information is distributed
   among MUP PEs and the MUP Controller and resolved by a MUP PE, and
   the behaviour required of them.  It does not define the wire encoding
   of any routing protocol; such an encoding may be defined in other
   documents.
- **draft-ietf-dmm-tn-aware-mobility-33** (new-draft, score 0, ignored_after_review) [dmm]: [Mapping 5G slice to Transport Network slice with UDP Source Ports](https://datatracker.ietf.org/doc/draft-ietf-dmm-tn-aware-mobility/) — Network slicing in 5G enables logical networks for communication
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
- **draft-ietf-emailcore-as-31** (new-draft, score 0, ignored_after_review) [emailcore]: [Applicability Statement for IETF Core Email Protocols](https://datatracker.ietf.org/doc/draft-ietf-emailcore-as/) — Electronic mail is one of the oldest Internet applications that is
   still in very active use.  While the basic protocols and formats for
   mail transport and message formats have evolved slowly over the
   years, events and thinking in more recent years have supplemented
   those core protocols with additional features and suggestions for
   their use.  This Applicability Statement describes the relationship
   among many of those protocols and provides guidance and makes
   recommendations for the use of features of the core protocols.
- **draft-ietf-idr-ts-flowspec-srv6-policy-22** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  It defines two modes of
   operation: transport steering into an SR Policy ("Mode 1"), in SR-
   MPLS and SRv6 networks, using BGP Extended Communities; and, in SRv6
   networks, transport steering combined with an egress service action
   at the egress node ("Mode 2"), signaled with the BGP Prefix-SID
   Attribute.
- **draft-ietf-lake-private-use-ranges-00** (new-draft, score 0, ignored_after_review) [lake]: [Additional Private Use Ranges in the IANA Registries of the Lightweight Authenticated Key Exchange (LAKE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-lake-private-use-ranges/) — This document adds Private Use ranges to IANA registries that pertain
   to the Lightweight Authenticated Key Exchange (LAKE) protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Lightweight
   Authenticated Key Exchange Working Group mailing list
   (lake@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/lake/.

   Source for this draft and an issue tracker can be found at
   https://github.com/lake-wg/private-use-ranges.
- **draft-ietf-mailmaint-unobtrusive-signatures-03** (new-draft, score 0, ignored_after_review) [mailmaint]: [Unobtrusive End-to-End Email Signatures](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-unobtrusive-signatures/) — This document deals with end-to-end cryptographically signed email.
   It introduces a structure for signed email that is designed to avoid
   creating any disturbance in legacy email clients.  This "unobtrusive"
   signature structure removes disincentives for signing email.
- **draft-ietf-moq-msf-02** (new-draft, score 0, ignored_after_review) [moq]: [MOQT Streaming Format](https://datatracker.ietf.org/doc/draft-ietf-moq-msf/) — This document specifies the MOQT Streaming Format, designed to
   operate on Media Over QUIC Transport.
- **draft-ietf-mpls-mna-ioam-17** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Actions for In Situ Operations, Administration, and Maintenance](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
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
- **draft-ietf-netmod-yang-config-templates-00** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Configuration Templates](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-config-templates/) — This document defines a YANG-based configuration template mechanism
   whereby repetitive configuration data can be factored out into
   templates and applied where needed.  This avoids the redundant
   definition of identical configuration and ensures the consistency of
   it, thus allowing configuration data to be managed more conveniently
   and efficiently.
- **draft-ietf-opsawg-ipfix-alt-mark-11** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-opsawg-ipfix-gpon-gem-04** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of Gigabit Passive Optical Network Encapsulation Method in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-gpon-gem/) — This document introduces new IP Flow Information Export (IPFIX)
   Information Elements to identify a set of G-PON Encapsulation Method
   entities in the Passive Optical Transport of the Optical Distribution
   Network.
- **draft-ietf-pce-flexible-grid-22** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-snac-simple-14** (new-draft, score 0, ignored_after_review) [snac]: [Automatically Connecting Stub Networks to Unmanaged Infrastructure](https://datatracker.ietf.org/doc/draft-ietf-snac-simple/) — This document specifies a set of practices for using IPv6 networking
   to automatically connect stub networks to adjacent infrastructure
   networks, even if they do not otherwise use IPv6.  This is applicable
   in cases such as constrained (Internet of Things) networks where
   there is a need to provide functional parity of service discovery and
   reachability between devices on the stub network and devices on an
   adjacent infrastructure link (for example, a home network).
- **draft-ietf-spring-stamp-srpm-mpls-14** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document specifies procedures for
   performance measurement in SR-MPLS networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths, including Segment Lists of SR Policies, SR-MPLS IGP
   best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 services and point-to-point Layer-2 services carried
   over those paths.
- **draft-ietf-v6ops-ipv6-app-testing-09** (new-draft, score 0, ignored_after_review) [v6ops]: [Recommendations for IPv6 Testing of Applications](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   Software-as-a-Service (SaaS) providers on how to approach IPv6
   testing in Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including
   "IPv6-only-strict" scenarios without any connectivity towards any
   relevant IPv4 endpoint.

   The document also discusses common misconceptions about the degree to
   which Operating Systems and libraries can abstract IPv6 issues away
   and explains common regressions to avoid when deploying IPv6 support.
- **draft-ietf-v6ops-ipv6-only-07** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  In
   particular, a goal is to provide a reference that describes the
   actual "IPv6-Only" functionality being used in a given scope, not the
   installed protocol stack support.
- **draft-ietf-v6ops-prefix-to-end-sites-02** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Prefix Assignment to End-Sites](https://datatracker.ietf.org/doc/draft-ietf-v6ops-prefix-to-end-sites/) — This document describes different alternatives and best current
   practices for assignment of IPv6 prefixes for end-sites in broadband
   networks, including considerations about point-to-point links, their
   size, numbering choices, pool choices, customer prefix assignment
   size and persistence of those assignments.
- **draft-ietf-v6ops-rfc7915-bis-03** (new-draft, score 0, ignored_after_review) [v6ops]: [IP/ICMP Translation Algorithm](https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/) — This document describes the Stateless IP/ICMP Translation Algorithm
   (SIIT), which translates between IPv4 and IPv6 packet headers
   (including ICMP headers).  This document obsoletes RFC 7915.
- **draft-kozuka-quic-stateless-punch-00** (new-draft, score 0, ignored_after_review) [none]: [Stateless Server-Assisted Hole Punching for QUIC](https://datatracker.ietf.org/doc/draft-kozuka-quic-stateless-punch/) — This document specifies a QUIC extension that lets two endpoints
   connected through a relay establish a direct path between them when
   one or both are behind Network Address Translators (NATs).  The
   client asks the server, over the existing connection, to send a
   single small "punch" packet toward one of the client's address
   candidates.  The server keeps no per-attempt state and does not
   initiate validation of candidate paths.  After a short delay, the
   client validates the direct path using ordinary client-initiated path
   validation as defined in RFC 9000, or ordinary path creation as
   defined in RFC 10069 when QUIC multipath is in use, and can then
   migrate the connection to it.
- **draft-liu-srv6ops-bfd-srv6-policy-encap-02** (new-draft, score 0, ignored_after_review) [none]: [Operational Guidelines for BFD Monitoring in SRv6 Policies](https://datatracker.ietf.org/doc/draft-liu-srv6ops-bfd-srv6-policy-encap/) — This document provides operational guidelines for Bidirectional
   Forwarding Detection (BFD) when applied to Segment Routing over IPv6
   (SRv6) Policies.  While the packet encapsulation mechanisms are
   standardized, this document focuses on the decisions network
   operators must make regarding mode selection, address management,
   traffic engineering integration, and troubleshooting strategies to
   ensure reliable service protection and efficient resource
   utilization.

   It addresses practical challenges such as handling diverse tail-end
   node capabilities (IPv4/IPv6), managing BFD session overhead in
   large-scale segment lists, and diagnosing failure detection anomalies
   in source-routed paths.
- **draft-palet-happy-reporting-considerations-02** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Happy Eyeballs Error Reporting](https://datatracker.ietf.org/doc/draft-palet-happy-reporting-considerations/) — This document introduces different aspects to be considered for the
   Happy Eyeballs error reporting.
- **draft-saum-rtgwg-mtu-propagation-evpn-overlays-00** (new-draft, score 0, ignored_after_review) [none]: [MTU propagation over EVPN Overlays](https://datatracker.ietf.org/doc/draft-saum-rtgwg-mtu-propagation-evpn-overlays/) — Path MTU Discovery between end-host-devices/Virtual-Machines/servers/
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
- **draft-schlyter-dnsop-dnssec-jwk-00** (new-draft, score 0, ignored_after_review) [none]: [JSON Web Key (JWK) for DNSSEC](https://datatracker.ietf.org/doc/draft-schlyter-dnsop-dnssec-jwk/) — This document specifies how to represent DNSSEC public and private
   keys as JSON Web Keys (JWK).  The cryptographic key material is
   encoded using the existing JWK key types, and the DNS-specific
   information needed to reconstruct the corresponding DNSKEY resource
   record (owner name, algorithm, protocol and flags) is carried in a
   new JWK parameter, "dnskey".  This gives DNSSEC signers, key
   management systems and other tools a standardized, interoperable
   format for exchanging and storing DNSSEC keys.
- **draft-shyam-vlsmtrp-17** (new-draft, score 0, ignored_after_review) [none]: [VLSM Tree Routing Protocol](https://datatracker.ietf.org/doc/draft-shyam-vlsmtrp/) — This is a light weight routing protocol applicable inside a network
   that appears in the form of a tree and distribution of address space
   takes place with the approach of VLSM. It is based on setting default
   route inside VLSM tree.  With this approach, routing information of
   the external world need not be passed down to the VLSM tree. Thus,
   load inside a router gets reduced substantially.  This document
   includes IP-VPN with MPLS inside VLSM tree by extending RSVP-TE.
- **draft-song-broadband-ancp-tsf-01** (new-draft, score 0, ignored_after_review) [none]: [TSF Extensions to ANCP in CU Separation Broadband Networks](https://datatracker.ietf.org/doc/draft-song-broadband-ancp-tsf/) — This document specifies a Traffic Steering Function (TSF) capability
   extension to the Access Node Control Protocol (ANCP), to discover and
   manage disaggregated user-plane (UP) functions in control/user plane
   separated networks, including the Access Network User Plane (AN-UP)
   and the Network Access Server User Plane (NAS-UP).
- **draft-song-lamps-cms-composite-frodokem-02** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-song-lamps-cms-composite-frodokem/) — This document specifies the conventions for using Composite FrodoKEM
   algorithms with the Cryptographic Message Syntax (CMS).  Composite
   FrodoKEM combines FrodoKEM with traditional algorithms (RSA-OAEP,
   X25519, X448) to provide hybrid post-quantum key encapsulation.
- **draft-song-lamps-pq-composite-frodokem-02** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-song-lamps-pq-composite-frodokem/) — Composite FrodoKEM defines combinations of FrodoKEM with RSA-OAEP,
   X25519, and X448.  This document specifies the algorithm definitions,
   key formats, and certificate conventions for using Composite FrodoKEM
   in the X.509 Public Key Infrastructure.
- **draft-ugur-moq-fast-switching-01** (new-draft, score 0, ignored_after_review) [none]: [Subscriber-Side Multi-Variant Fast Track Switching for MOQT](https://datatracker.ietf.org/doc/draft-ugur-moq-fast-switching/) — This document describes subscriber-side multi-variant fast track
   switching (MVFTS), a technique that allows a MOQ Transport (MOQT)
   subscriber to switch between tracks that are encoded at the same
   bitrate but use different group of pictures (GoP) lengths, combining
   the compression efficiency of a long GoP with the low switching delay
   of a short GoP.  A publisher using this technique packages each
   encoded bitrate as a ladder of tracks distinguished only by their
   keyframe interval, numbers those tracks' Group IDs so that they share
   a common alignment, and advertises the keyframe interval of each
   track in a MOQT Streaming Format (MSF) catalog.  A subscriber uses
   this information to compute the nearest valid switch point on any
   track in scope and to perform the switch using the SWITCH_FROM
   request parameter in soft mode.
- **draft-xiao-v6ops-eds-03** (new-draft, score 0, ignored_after_review) [none]: [Enhanced Dual Stack: Connection-Informed IPv6/IPv4 Selection](https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/) — This document describes Enhanced Dual Stack (EDS), a framework
   intended to reduce the operational risk and upfront workload of
   introducing IPv6 into existing IPv4 networks.  EDS provides a
   connection-informed method for implementing RFC 6724 Rule 1, "Avoid
   unusable destinations", by remembering recent TCP/QUIC connection-
   establishment failures and avoiding repeated selection of affected
   IPv6 destinations.  It also provides operational diagnostics so
   administrators can identify and correct IPv6 problems.  EDS is
   complementary to Happy Eyeballs and does not require connection
   racing.  By starting with selected EDS-capable pioneer hosts,
   performing practical validation, and expanding IPv6 gradually, EDS
   can be deployed incrementally without requiring all hosts to support
   EDS.  With EDS, enterprises' IPv6 introduction can change from a
   heavy upfront validation process toward an incremental improvement
   process.
- **draft-ye-srv6ops-sfc-deployment-03** (new-draft, score 0, ignored_after_review) [none]: [SRv6 SFC Deployment Options](https://datatracker.ietf.org/doc/draft-ye-srv6ops-sfc-deployment/) — This document outlines the critical factors for deploying Service
   Function Chaining (SFC) using Segment Routing over IPv6 (SRv6).  It
   addresses deployment architectures, including both SRv6-aware and
   SRv6-unaware scenarios, and details the end-to-end provisioning
   lifecycle.  Furthermore, it proposes reliability mechanisms and
   provides strategic recommendations for network operators
   transitioning from legacy NSH-based SFC to a modern, scalable SRv6
   framework.
- **draft-yuyou-moq-v3c-01** (new-draft, score 0, ignored_after_review) [none]: [Transport of V3C Bitstreams over Media over QUIC Transport (MOQT)](https://datatracker.ietf.org/doc/draft-yuyou-moq-v3c/) — This document specifies a mapping and packaging for transporting ISO/
   IEC 23090-5 Visual Volumetric Video-based Coding (V3C) bitstreams
   over Media over QUIC Transport (MOQT).  The mapping uses the MOQT
   Streaming Format (MSF): V3C configuration is MSF initialization data,
   each independently consumable V3C component is an MSF track, a run of
   V3C composition units that starts at a random access point is a MOQT
   Group, and the coded data of one component for one composition unit
   is a MOQT Object.  Relays remain unaware of V3C syntax.  V3C
   knowledge is confined to the streaming-format layer.
- **draft-zheng-quic-fec-extension-03** (new-draft, score 0, ignored_after_review) [none]: [FEC Extension for QUIC](https://datatracker.ietf.org/doc/draft-zheng-quic-fec-extension/) — This document specifies a Forward Error Correction (FEC) extension
   for the QUIC protocol, which provide protection against packet loss.

## Errors / fetch failures

_None._
