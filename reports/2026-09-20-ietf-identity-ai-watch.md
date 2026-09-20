# IETF Identity + AI Standards Watch

Date: 2026-09-20

## Read now

- **draft-das-execution-handle-02** (new-draft, score 50, trust_infrastructure) [none]: [Possession Is Not Authority: Execution Handle, Sink Verification, Atomic Consumption, and Finality Receipt](https://datatracker.ietf.org/doc/draft-das-execution-handle/) — Across agentic AI, payments, cloud control planes, industrial
   actuation, and cross-border processing, a machine can prepare a
   concrete operation long before that operation is allowed to become
   externally effective.  Existing protocols already move identity,
   authorization data, attestation results, and signed statements.  They
   do not, by themselves, define the small set of interoperable objects
   required at the effectuation boundary: a canonical Candidate Act
   Descriptor, a scoped non-bearer Execution Handle bound to that exact
   act and to a designated Finality Sink, a verify operation that
   reconstructs the pending effect, an atomic consume that prevents
   replay, and a Finality Receipt that records what was actually
   permitted.

   The residual failure is familiar and does not require token forgery.
   An access token, capability, session cookie, SPIFFE SVID, WIMSE
   credential, OAuth grant, attestation result, or signed mandate can
   remain cryptographically valid while being presented for a different
   tool call, a substituted beneficiary, a second sink, a replayed
   payment, a migrated region, or an alternate administrative path.
   Bearer possession then becomes mistaken for current, act-specific
   authority to effectuate.

   Existing mechanisms already address important adjacent problems.
   OAuth 2.0 and OAuth Rich Authorization Requests can express fine-
   grained authorization data [RFC6749] [RFC9396].  DPoP and
   certificate-bound tokens constrain sender possession [RFC9449]
   [RFC8705].  JWT and CWT carry signed claims [RFC7519] [RFC8392].
   HTTP Message Signatures authenticate individual requests [RFC9421].
   WIMSE addresses workload identity in multi-system environments
   [WIMSE-ARCH].  RATS supplies Evidence and Attestation Results
   [RFC9334].  SCITT supplies signed statements, transparency, and
   receipts [RFC9943].  MCP and similar tool interfaces dispatch agent-
   selected functions.  None of these objects is specified as a non-
   bearer, exact-act, sink-bound, single-use-or-bounded effectuation
   authority whose verification is serialized with protected commit.

   This document specifies those wire objects and the verify/consume/
   receipt exchange.  A Candidate Act remains in a Non-Effective State
   until a Finality Sink reconstructs the security-relevant pending
   operation, verifies that a current Execution Handle authorizes that
   exact operation at that sink, consumes or reserves the handle
   according to its reuse policy, and optionally emits a Finality
   Receipt.  The Execution Handle is not a session token and is not
   valid merely because the caller can present it.

   Prevention is claimed only when exact-act binding, sink binding,
   currentness, reuse policy, consequence-path coverage, and
   verification-to-commit serialization are load-bearing.  If a
   deployment uses ordinary bearer tokens, advisory act identifiers,
   post-hoc logs, or a gateway that can be routed around, the result is
   mitigation or evidence rather than the same prevention guarantee.
   Encoding profiles are provided for JSON and COSE/CWT; the
   architecture requires the semantics, not one exclusive encoding.

   In conventional engineering terms, the architecture is a consequence-
   bound policy enforcement point or reference monitor placed at the
   command/transaction/actuation gate.  It combines cryptographic
   parameter binding, sink or destination binding, freshness and
   fencing/generation checks, protected anti-replay state, and a TOCTOU-
   resistant verify-consume-commit step.  Aerospace and control
   engineers may recognize the role as a safety interlock or command
   gate; payment and distributed-systems engineers may recognize
   transactional authorization plus idempotency/anti-replay state; cloud
   and hardware-security engineers may recognize a protected reference
   monitor or egress enforcement boundary.  Different component names or
   protocol packaging do not change the pattern when the same
   enforcement sequence and failure semantics are implemented.

   Three rejections are expected and are addressed in the body rather
   than dismissed here.  First, a saga, 2PC, or workflow plus ordinary
   tokens already coordinates steps; that coordinator is complementary,
   and is enough only if each sink also reconstructs the live act and
   consumes act-bound authority.  Second, atomic consume is not a
   process-wide lock: SINGLE_USE is per handle, COUNTED and ENVELOPE
   exist for high-QPS classes, and rails that already keep idempotency
   keys already pay this cost.  Third, reconstruction is required only
   at the component that would first make the effect real, over fields
   that sink can observe — not at every mesh hop, and not as blind trust
   in a caller digest.  Reviewers who hold any of those objections are
   asked to read those sections and to supply a counterexample if the
   residual gap is already closed.  Criticism, prior art, and a
   recommendation to stop the work remain invited.
- **draft-das-jurisdiction-bound-execution-finality-00** (new-draft, score 40, trust_infrastructure) [none]: [Authorized Here, Not Authorized There: Jurisdiction-Bound Execution Finality for Cross-Border and Sovereign Systems](https://datatracker.ietf.org/doc/draft-das-jurisdiction-bound-execution-finality/) — Modern cloud, AI, financial, telecom, and critical-infrastructure
   systems increasingly operate across regions, sovereign clouds, multi-
   cloud environments, and distributed workload chains.  A high-
   consequence authorization failure can occur even when identity,
   cryptography, policy evaluation, and platform attestation all
   succeed: the same Candidate Act can become effective under a
   jurisdictional or governance context different from the one under
   which it was authorized.  Workload migration, disaster-recovery
   failover, cross-region queues, service rerouting, remote
   administration, control-plane changes, destination substitution, key-
   control changes, or downstream processing can convert an
   authorization that was valid under context J1 into an effect
   occurring under context J2.  No token forgery or cryptographic break
   is required.

   Existing mechanisms already address important parts of this problem.
   OAuth Rich Authorization Requests [RFC9396] can carry fine-grained
   authorization details; OAuth Resource Indicators [RFC8707] bind
   authorization requests to protected resources; JWT [RFC7519] can
   carry signed application claims; WIMSE [WIMSE-ARCH] provides
   workload-identity and security-context architecture for multi-system
   environments; RATS [RFC9334] provides Evidence, Verifiers, and
   Attestation Results; and SCITT [RFC9943] provides signed statements,
   transparency, and receipts.  Industry systems also provide concrete
   sovereignty and data-boundary controls: Microsoft documents its EU
   Data Boundary [MS-EUDB], AWS operates the European Sovereign Cloud
   [AWS-ESC], and Google Cloud provides Sovereign Controls by Partners
   [GOOGLE-SOV].

   The residual gap exists only where jurisdiction is treated as
   descriptive metadata, inferred from weak location signals, enforced
   only at deployment time, or checked at an upstream boundary while the
   actual consequence can later move through another region, operator,
   administrative path, processing service, destination, failover route,
   or control domain.  A workload can be correctly authenticated and a
   platform correctly attested while the current effectuation context no
   longer satisfies the deployment's sovereignty rule.  Likewise,
   storing data in one region does not by itself prove where it is
   processed, remotely administered, decrypted, transmitted, or finally
   disclosed.

   This document proposes a jurisdiction-bound execution-finality
   invariant.  A Candidate Act remains in a Non-Effective State until
   the Finality Sink establishes a current, authoritative Jurisdiction
   Execution Context (JEC) for the exact act and verifies that the
   present effectuation environment satisfies the deployment-defined
   Jurisdiction Policy.  The JEC can combine workload identity, compute
   and processing domain, storage location, destination, operator/
   control domain, key-control domain, remote-access state, attested
   trust state, and policy generation.  JEC is an architectural role,
   not a mandated token format.

   Prevention is claimed only when the jurisdiction policy, evidence
   sources, current effectuation context, exact-act binding, state
   continuity, and consequence path are load-bearing and non-bypassable.
   If the deployment relies only on GeoIP, region labels, advisory
   metadata, best-effort routing, post-hoc audit, or incomplete path
   coverage, the result is mitigation or evidence rather than the same
   prevention guarantee.  The architecture enforces machine-readable
   jurisdiction or compliance policy supplied by an authoritative
   deployment source; it does not determine what law applies or provide
   a legal conclusion.

   Microsoft, AWS, Google Cloud, NVIDIA, and Arm are discussed only as
   complementary industrial examples or potential integration points.
   The document does not assert vulnerability, deficiency, non-
   conformance, affiliation, or endorsement by any named organization.
   A deployment that already makes its required jurisdictional
   constraints current, non-bypassable, and mandatory at the actual
   consequence boundary already satisfies the core property.  Criticism,
   corrections, counterexamples, prior-art pointers, implementation
   experience, and evidence of equivalent existing mechanisms are
   explicitly invited.
- **draft-das-execution-finality-enforcement-profiles-02** (new-draft, score 38, trust_infrastructure) [none]: [Execution Finality at External-Effect Boundaries: Enforcement Profiles for 6G, AI-Native RAN, RF, ISAC, Accelerated Compute, Devices, and Autonomous Systems](https://datatracker.ietf.org/doc/draft-das-execution-finality-enforcement-profiles/) — AI-native and autonomous infrastructure is increasingly able to
   generate, optimize, schedule, route, transmit, disclose, render,
   allocate, encrypt, modify network state, control radio resources, and
   initiate physical or machine actions without a human decision at
   every step.  An agentic AI system may generate a tool call or machine
   instruction; an AI-native RAN may compute a beam, handover, power,
   spectrum, routing, slicing, or topology change; an integrated sensing
   and communication (ISAC) system may generate sensing information for
   release or fusion; an O-RAN xApp or rApp may generate a network-
   control instruction; an accelerator may produce a routing,
   scheduling, inference, or resource-allocation result; or an
   autonomous controller may prepare a cyber-physical actuation.
   Successful computation, authentication, attestation, access
   authorization, credential possession, or execution inside a trusted
   environment does not, by itself, establish authority for the
   resulting operation to become externally effective.

   This document describes a protected execution-finality architecture
   in which that distinction is machine-enforced.  A proposed
   consequential operation is represented as a Candidate Act and remains
   in a Non-Effective State while a Protected Enforcement Domain
   establishes a machine-verifiable act descriptor, validates applicable
   machine-verifiable authority predicates, and performs, consumes,
   advances, or references applicable protected state.  The resulting
   state is represented by an applicable protected-state representation,
   and Protected Validation Evidence is committed before, or atomically
   with, authorization of availability of a scoped non-bearer
   capability.  The capability is machine-verifiably or
   cryptographically bound to the specific Candidate Act, the act
   descriptor or its digest, the committed validation evidence,
   applicable protected state, freshness constraints, permitted
   effectuation scope, the relevant execution-finality boundary, and the
   applicable Finality Sink.

   The Finality Sink is positioned at or before the point at which the
   Candidate Act would first acquire an externally meaningful
   consequence.  Before effectuation, the Finality Sink performs a
   machine-enforced capability-validity check and permits the Candidate
   Act to cross the execution-finality boundary only when the required
   bindings, protected state, validation evidence, freshness conditions,
   and effectuation scope remain valid.  Absence, expiry, revocation,
   exhaustion, replay, staleness, mismatch, timeout, unverifiability,
   indeterminacy, scope failure, binding failure, or failure of a
   required preceding protected operation causes the architecture to
   fail closed, leaving the Candidate Act non-effective.

   The document provides 132 detailed Enforcement Profiles that
   instantiate this common architecture at materially different
   consequence boundaries.  The profiles cover agentic AI tool calls and
   machine instructions; AI-native RAN and RF control; integrated
   sensing and communication (ISAC); sensing-result, location,
   telemetry, and metadata release; restricted-content delivery,
   decryption, decoding, recommendation, and rendering; derivative,
   transformed, synthetic, and AI-modified content; VPN, proxy,
   encrypted-DNS, encrypted-session, and tunnel establishment; cyber-
   physical, robotic, vehicle, industrial, and actuator control; network
   exposure, CAPIF, northbound APIs, and operator-controlled
   capabilities; distributed, edge, joint communication-compute, and in-
   network compute; shared AI-RAN accelerators and deterministic
   resource isolation; O-RAN xApp, rApp, A1, E2, and O1 control paths;
   cloud-native and virtualized RAN; network slicing, routing, topology,
   service-function-chain, and autonomous-network operations; ambient,
   passive, batteryless, backscatter, and zero-energy IoT; device wake
   and RF-energy admission; dynamic spectrum occupancy and spectrum
   authorization; RF, millimetre-wave, sub-THz, and future-band
   emission; reconfigurable intelligent surfaces; cooperative and
   distributed radio; post-quantum and hybrid cryptographic activation;
   RAN AI-model mutation; hardware-controlled location release;
   speculative decoding and target-model reconciliation; persistent and
   vector memory; deferred, scheduled, recurring, and trigger-
   conditioned acts; tool, plug-in, MCP-server, and external-agent
   supply-chain re-attestation; neural-state descriptors and privacy-
   preserving neural proofs; neural Candidate Act fragments; neural
   trust segmentation and influence-threshold enforcement; hardware-
   isolated neural-influence shadow auditing; multimodal sensory
   provenance; distributed multi-GPU neural execution and secure
   interconnect binding; unknown-agent marketplace recruitment and trust
   establishment; two-instance collection-time and execution-time cross-
   committed validation with independent protected enforcement domains;
   boundary-local reconstruction of the actual pending operation;
   attested measurement paths; atomic verify-and-effectuate and compare-
   and-commit enforcement; distributed partial-share finality without
   centralized authority reconstruction; sink-rooted finality evidence
   for dependent operations; readable-data operational inertness; cross-
   committed multi-agent delegation chains; autonomous cloud-control-
   plane and telco-cloud commit control; AI-mediated voice, video,
   recording, call-transfer, and communication-response control;
   separate computation authority and produced-output finality
   authority; produced-output canonicalization and output-derived digest
   binding; effectuation-enabling-resource withholding and execution-
   substrate technical non-completability; first-usable, location-
   neutral effectuation-boundary control; output grounding-to-
   effectuation correspondence; and accelerator, DMA, RDMA, memory,
   interconnect, SmartNIC, DPU, and other hardware-egress boundaries.
   Each profile identifies the relevant Candidate Act, authority
   predicates, protected state, capability scope, Finality Sink,
   execution-finality boundary, and externally effective consequence
   while inheriting the common execution-finality model.

   The architectural question addressed here is complementary to, rather
   than a replacement for, current industry work on AI-native and future
   communications.  Publicly described work from Qualcomm, Nokia,
   NVIDIA, Samsung, Ericsson, and Huawei is relevant to areas covered by
   these profiles, including AI-native 6G, AI-RAN, accelerated and
   shared compute, programmable and autonomous RAN control, RF and
   spectrum operation, ISAC, cloud-native networking, energy
   optimization, and increasingly autonomous network-management loops.
   The present document addresses a narrower enforcement question that
   arises at or immediately before consequence: after an AI model,
   network function, accelerator, application, controller, or autonomous
   agent has successfully computed or prepared an operation, what
   machine-verifiable authority must exist at the exact external-effect
   boundary before that specific operation is allowed to take effect?
   The named organizations are referenced solely to identify publicly
   relevant technical directions; no affiliation, review, adoption,
   approval, endorsement, or participation by any named organization is
   implied.

   The common invariant across all profiles is therefore: computation
   may produce a Candidate Act, but computation is not authority for
   consequence.

   In conventional engineering terminology, the architecture can be
   understood as a consequence-side policy-enforcement point or
   reference monitor combined, where appropriate, with a safety
   interlock or command/actuation gate, exact-parameter cryptographic
   binding, anti-replay and monotonic protected state, fencing or
   generation epochs, bounded capability semantics, and a time-of-check/
   time-of-use-resistant verify-and-commit transition.  These terms are
   functional analogues rather than required component names: an
   implementation can use different protocol names, packaging, hardware
   blocks, control-plane terminology, or industry vocabulary and still
   implement the same technical pattern when the same enforcement
   sequence and invariants are present.

   Profiles 184 through 213 add package-interconnect acceptance,
   exception-path and fault-report egress, transmission-quota grant,
   asserted-prior-authorization, non-transfer coherence visibility,
   runtime capacity arrival, PHY link-state, in-path component, post-
   attestation interface-protection, test-path egress, electrical and
   clock prerequisite, and virtual-channel admission finality, together
   with commercially mapped profiles for multi-accelerator tensor
   egress, CXL extent assign-and-reclaim, DPU host-bypass denial,
   produced-inference-output release, accelerator tenant rebind,
   destination-jurisdiction egress, agentic tool-call dispatch, key-
   value-cache admission, model-weight activation, co-packaged optical-
   lane enablement, training-contribution admission, secret unwrap,
   streaming-token release, retrieved-context admission, on-device
   sensor binding, radio and UPF emission, cross-application on-device
   assistant capability, and telemetry or debug egress.  The silicon-
   layer extension profiles additionally cover CXL-class coherent memory
   pooling and ownership transitions; UCIe-class chiplet attach and die-
   to-die manageability; accelerator scale-up-fabric remote load, store,
   atomic, and route operations; confidential accelerator contexts and
   secret provisioning; IOMMU/SMMU, PASID, ATS, DMA-aperture, and peer-
   to-peer translation state; HBM4-class memory-region reassignment and
   residual-state control; DPU/SuperNIC host-independent network and
   storage data paths; co-packaged optics and silicon-photonics optical
   egress; silicon-root-of-trust firmware, microcode, and bitstream
   activation; and on-die memory-system, NoC, cache, and bandwidth
   partition state.
- **draft-mnki-agent-trust-profile-00** (new-draft, score 34, core_identity) [none]: [The Agent Trust Profile: Verifiable Authority for Autonomous Agents](https://datatracker.ietf.org/doc/draft-mnki-agent-trust-profile/) — Autonomous AI agents act on behalf of people and organizations across
   system and organizational boundaries.  Existing credentials establish
   that a token is valid; they do not express which agent is acting, for
   whom, under what delegated authority, within which constraints, and
   whether that authority is still current.  This document profiles
   existing standards — JWS, OAuth/OIDC, SPIFFE/WIMSE workload identity,
   DPoP-style proof of possession, OpenID AuthZEN and OpenID Federation
   — to carry those semantics: agent identity and principal binding,
   delegation with authority attenuation, capability-based authorization
   with constraints, request proof of possession, authorization
   attestations, tamper-evident provenance, revocation, and cross-
   organization trust.  It defines no new cryptography, transport or
   token format.
- **draft-das-third-party-decision-binding-00** (new-draft, score 32, trust_infrastructure) [none]: [Trust Me, I Checked: Verifiable Third-Party Decision Binding at the Execution-Finality Boundary](https://datatracker.ietf.org/doc/draft-das-third-party-decision-binding/) — High-consequence distributed systems frequently allow one component
   to act based on a decision produced by another component, such as an
   authorization server, policy engine, risk service, attestation
   Verifier, compliance service, workload-identity authority, or safety
   controller.  The vulnerability is not limited to forged credentials:
   a compromised or incorrectly designed intermediary can claim that a
   required third-party check succeeded, replay an earlier decision,
   substitute evidence from a different act or context, suppress a
   required DENY, or retain evidence only for audit while the protected
   effect remains technically independent of that evidence.  The issue
   deserves high attention where the downstream consequence is
   financial, administrative, privacy-sensitive, safety-relevant,
   infrastructure-changing, or otherwise difficult to reverse.

   Existing mechanisms solve important parts of this problem.  OAuth
   Token Introspection [RFC7662] lets a protected resource query token
   state; HTTP Message Signatures [RFC9421] provide integrity and
   authenticity for selected HTTP message components; RATS [RFC9334]
   provides Evidence, Verifiers, and Attestation Results; Transaction
   Tokens [TXN-TOKENS] propagate identity and authorization context
   through trusted call chains; SCITT [RFC9943] provides signed
   statements, transparency, and verifiable receipts; and current
   authorization- evidence work [MUNOZ-EVIDENCE] [MUNOZ-SCITT] defines
   signed pre-execution Permits bound to canonical request material.
   Where one of these mechanisms is verified by the actual non-
   bypassable effectuation boundary and already proves the required
   decision for the exact act, current context, and authorized use, that
   deployment can already satisfy the property described here.

   The residual gap arises only where the consequential component
   receives an upstream claim such as "the external check passed", where
   authentic evidence is bound to the wrong act, authority, tenant,
   purpose, generation, or sink, where valid evidence has become stale
   or replayable, where only a subset of required authorities is
   represented, or where evidence exists but is not a load-bearing
   prerequisite of effectuation.  This document introduces an
   architectural role called External Decision Evidence (EDE).  EDE is
   not a new wire format: an existing Permit, SCITT statement or
   receipt, Attestation Result, live authenticated decision response, or
   other protected result can instantiate EDE when its semantics satisfy
   the deployment profile.

   The proposed invariant is that a Candidate Act remains non-effective
   until the Finality Sink independently establishes that every required
   external decision authority issued an applicable decision for the
   concrete act, under the required decision basis and current state,
   with freshness, audience or sink binding, and authorized-use
   semantics appropriate to the deployment.  Prevention is claimed only
   when the protected consequence cannot occur without successful
   verification of the required evidence and alternate effectuation
   paths cannot bypass that verification.  Otherwise the mechanism
   provides auditability, accountability, detection, or mitigation
   rather than the same prevention guarantee.

   The model is intended to complement, not criticize or replace, OAuth,
   WIMSE, SCITT, RATS, externalized policy systems such as Amazon
   Verified Permissions/Cedar, continuous-access systems such as
   Microsoft Entra Continuous Access Evaluation, Google Cloud IAM
   controls, and protected-compute technologies such as NVIDIA
   attestation and Arm CCA.  The proposed delta is not the invention of
   signatures, authorization evidence, receipts, or attestation results;
   it is the effectuation-time requirement that independently verifiable
   required decisions become load-bearing for the exact protected act.
   Criticism, corrections, counterexamples, implementation experience,
   prior-art pointers, and evidence that existing mechanisms already
   provide the full invariant are explicitly invited.
- **draft-das-actuation-bound-execution-finality-00** (new-draft, score 29, authorization) [none]: [Command Accepted Is Not Actuation Authorized: Execution Finality for Cyber-Physical and Industrial Control Systems](https://datatracker.ietf.org/doc/draft-das-actuation-bound-execution-finality/) — Cyber-physical and industrial systems increasingly accept commands
   from cloud services, AI agents, remote operators, enterprise
   applications, and distributed control software.  A high-consequence
   failure can occur even when identity, authorization, message
   integrity, platform attestation, and functional-safety mechanisms are
   individually correct: a digitally valid command can remain apparently
   acceptable while the target actuator, command parameters, machine
   mode, process state, safety/interlock state, authority state, or
   effectuation path has changed.  The consequence is no longer merely
   an incorrect API call.  It can be drive energization, robotic motion,
   valve or pump actuation, material release, process transition, or
   another physical effect.  No token forgery, cryptographic break, or
   defeat of the safety protocol is necessarily required; the failure
   can be a loss of continuity between earlier digital authority and the
   exact physical act that becomes effective.

   Existing industrial mechanisms already solve major parts of this
   problem.  IEC 61508 and IEC 61511 define mature functional-safety
   engineering and Safety Instrumented Systems; IEC 62443 defines
   cybersecurity requirements for industrial automation and control
   components; OPC UA provides industrial security mechanisms, while OPC
   UA Safety defines a functional-safety communication layer; ACE-OAuth
   [RFC9200] provides authorization for constrained IoT environments;
   RATS [RFC9334] provides trusted platform Evidence and Attestation
   Results; and existing safety PLCs/controllers from Siemens, Rockwell
   Automation, Schneider Electric, ABB, and other vendors provide mature
   safety logic and output control.  These are complementary precedents,
   not examples of missing safety engineering.  Where an existing safety
   controller or protected actuator boundary already makes exact command
   authority, current safety/process state, and final output mediation
   non-bypassable, that deployment already satisfies the core property
   described here.

   The residual gap exists only where one of those mechanisms stops at a
   boundary upstream of the first physical effect or does not carry the
   complete cyber-authority predicate required by the deployment.  IEC
   functional-safety mechanisms can correctly enforce safety functions
   without necessarily expressing the provenance and exact scope of an
   AI-, cloud-, or enterprise-originated command.  IEC 62443 controls
   can correctly protect identity, use, integrity, and information flow
   without by themselves defining the final application's exact
   actuation predicate.  OPC UA Safety can correctly deliver SafetyData
   while the receiving safety application still determines whether a
   cyber-originated act is applicable.  ACE can correctly authorize a
   constrained resource while current machine/process/safety state may
   be evaluated later.  RATS can correctly attest the controller while
   platform trust is not authorization for a particular torque, motion,
   valve transition, or output.  Current application-layer action-
   evidence work [SOKOLOV-AEP] can strengthen accountability while
   remaining distinct from pre-actuation non-completability.  If any
   existing deployment already composes these properties at the true
   output boundary, no residual gap remains for that deployment.

   This document therefore proposes a narrower actuation-bound
   execution-finality invariant.  A Candidate Act remains in a Non-
   Effective State until a protected Actuation Finality Boundary (AFB)
   verifies the exact pending command, current execution authority,
   target actuator identity, freshness and replay state, required
   current machine/process/safety predicates, and authorized
   effectuation path immediately before or atomically with the physical
   output becoming effective.  The AFB is an architectural role, not a
   mandatory new appliance: an existing safety PLC, safety controller,
   protected drive, robot controller, SIS function, secure I/O stage, or
   device controller can already be the AFB when it enforces the
   required invariant.

   Prevention is claimed only where the protected physical effect cannot
   occur without those checks and where existing functional-safety
   controls remain authoritative rather than being bypassed or replaced.
   Execution-finality logic MUST NOT convert an existing safety DENY
   into ALLOW.  If enforcement is upstream-only, mutable context is
   stale, path coverage is incomplete, or the mechanism merely records
   what occurred, the result is mitigation, detection, or auditability
   rather than the same prevention guarantee.  The architecture
   complements functional safety; it does not replace hazard analysis,
   define a safe state, certify an unsafe controller, or claim that an
   IETF mechanism establishes SIL or PL.

   The problem is industrially relevant to robotics and motion control,
   process plants, manufacturing and warehouse automation, power and
   critical infrastructure, and other systems where remote or AI-
   generated commands can cross several cyber layers before becoming
   physical.  Siemens Safety Integrated, Rockwell GuardLogix, Schneider
   Electric Modicon M580 Safety, ABB AC500-S, and OPC UA Safety are
   cited politely as mature safety precedents and potential integration
   points.  No vulnerability, deficiency, non-conformance, affiliation,
   or endorsement is asserted.  Criticism, corrections, counterexamples,
   prior art, real-time implementation experience, and evidence that
   existing safety or authorization mechanisms already provide the full
   invariant are explicitly invited.
- **draft-das-finality-bound-revocation-00** (new-draft, score 28, authorization) [none]: [Revoked but Still Executable: Closing the Authorization-to-Effect Gap with Finality-Bound Revocation](https://datatracker.ietf.org/doc/draft-das-finality-bound-revocation/) — Revocation is often treated as a property of a credential, token,
   session, grant, policy, or identity record.  In consequence-bearing
   systems, however, an authorization can be completely legitimate when
   issued and still become unsafe before the authorized operation
   becomes externally effective.  The security question is therefore not
   only whether revocation exists, but whether a revocation that becomes
   authoritative before a protected commit is guaranteed to control that
   commit.  The severity is deployment- dependent, but can be high in
   financial, administrative, AI-agent, cloud-control, confidential-
   compute, device, industrial, or other environments where a stale-but-
   valid authorization can produce an irreversible or externally
   consequential effect.

   This document describes a finality-bound revocation model.  A
   Candidate Act remains in a Non-Effective State after upstream
   authorization.  The authorization is bound to an act-specific
   revocation basis, such as a protected revocation generation, epoch,
   status root, or equivalent authority state.  Immediately before the
   protected consequence is committed, a Finality Sink verifies that no
   applicable revocation, suspension, narrowing, or superseding
   authorization state has become load-bearing.  Where the revocation
   state changed, the act is rejected, re-authorized, or explicitly
   shown to survive the change under an authoritative rule.  With
   authoritative current state, atomic check-and-commit semantics, and
   complete mediation of all effectuation paths, this is intended as a
   prevention property for the protected stale act; deployments that
   permit bounded staleness or incomplete path coverage obtain
   mitigation rather than the same prevention guarantee.

   The model complements existing mechanisms rather than replacing them.
   OAuth Token Revocation [RFC7009] and Token Introspection [RFC7662]
   provide standardized token-state mechanisms; Microsoft Entra
   Continuous Access Evaluation [MS-CAE] demonstrates event-driven
   rejection of otherwise unexpired tokens; Amazon Verified Permissions
   and Cedar [AWS-VERIFIED-PERMISSIONS] provide fine-grained policy-
   evaluation mechanisms; Google Cloud IAM [GOOGLE-IAM-DENY] provides
   centrally managed deny-policy controls; and confidential-computing
   and attestation platforms such as NVIDIA attestation [NVIDIA-ATTEST]
   and Arm CCA [ARM-CCA] can provide protected execution and trust
   inputs.  These technologies are cited as industrial alignment and
   integration points, not as assertions of vulnerability, deficiency,
   non-conformance, affiliation, or endorsement.

   The proposed delta is an effectuation-bound invariant: if revocation
   becomes authoritative before an act crosses the protected
   effectuation boundary, a previously valid permit must not remain
   sufficient merely because its signature, expiry, sender constraint,
   earlier authorization decision, or cached status result is still
   valid.  The document therefore focuses on the ordering and binding
   between revocation state and the exact protected commit, including
   queued work, multi-hop delegation, alternate effectuation paths,
   rollback, crash recovery, and TOCTOU races.

   The document asks the IETF community whether existing standards or
   deployed mechanisms already provide this invariant in full, where the
   correct effectuation boundary lies, and what interoperability work,
   if any, is justified.  Criticism, corrections, counterexamples,
   implementation experience, and pointers to existing equivalent
   mechanisms are explicitly invited.
- **draft-watts-agent-authority-transition-receipts-00** (new-draft, score 28, authorization) [none]: [Agent Authority Transition Receipts for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-authority-transition-receipts/) — Autonomous agents increasingly act across administrative and security
   domains using workload identities, OAuth credentials, delegated
   authorization, attestations, and policy engines.  Existing mechanisms
   can establish identity, delegation, or access rights, but deployments
   still lack a common artifact that records which policy and which
   evidence were evaluated when an operation moved into an authorized,
   denied, revoked, or expired authority state.

   This document defines an Agent Authority Transition Receipt (AATR), a
   signed, non-bearer receipt that cryptographically binds an agent
   operation to the principal, policy, evidence set, decision, audience,
   validity interval, and predecessor authority state used for that
   decision.  AATR intentionally separates evidence from authorization
   and authorization from execution.  Missing or indeterminate required
   evidence fails closed.  AATR is designed to compose with OAuth,
   workload identity, remote attestation, transparency services, and
   agent-specific delegation protocols rather than replace them.
- **draft-das-consequence-path-completeness-00** (new-draft, score 27, authorization) [none]: [When the Gate Can Be Bypassed: Consequence-Path Completeness for Execution Finality](https://datatracker.ietf.org/doc/draft-das-consequence-path-completeness/) — A perfectly correct authorization or security gate does not prevent a
   protected consequence if the same effect remains technically
   reachable through another path.  High-consequence systems commonly
   place authentication, authorization, policy, attestation, or
   execution-finality checks at identified API, gateway, Resource
   Server, operating-system, service-perimeter, or hardware boundaries.
   The vulnerability examined here is therefore a coverage failure: the
   protected gate can be sound while the effect can go around it.  This
   deserves high attention where the bypass can produce irreversible,
   financial, safety-relevant, privacy-sensitive, sovereign, or mission-
   critical consequences.

   Existing security architecture already addresses important parts of
   this problem.  The reference-monitor concept requires complete
   mediation, tamper resistance, and verifiability; OAuth Resource
   Servers validate authorization for requests they receive; gateways,
   service meshes, cloud policy systems, and service perimeters mediate
   configured flows; RATS provides trust evidence for components; and
   confidential-computing or hardware isolation can provide protected
   enforcement locations.  If any existing mechanism actually mediates
   every route capable of producing the defined consequence under the
   stated threat model, that deployment already satisfies the core
   property described here and no additional component is required
   merely for duplication.

   The residual problem arises when enforcement coverage is narrower
   than the consequence: for example, when an approved API hands work to
   a queue or database with other ingress paths, a service perimeter
   covers selected services while another interface remains effect-
   capable, or a software gate coexists with administrative, recovery,
   device, DMA, storage, or management-plane routes.  This document
   introduces a consequence-oriented execution-finality formulation: a
   Protected Consequence K, an Effectuation Domain D, a generation-
   indexed directed Effectuation Graph G_g, an Effectuation Path Set
   P_g(K,D), a Finality Cut Set F, and a protected Path-Set Generation
   g.  Prevention is claimed only when removal of the valid enforcement
   set F disconnects every admissible source from the consequence node,
   every member of F enforces an equivalent load-bearing finality
   predicate, and topology changes cannot silently inherit an older
   completeness claim.

   Where path discovery is incomplete, enforcement is bypassable,
   topology state is stale, or only selected interfaces are covered, the
   mechanism is mitigation or detection rather than the same prevention
   guarantee.  The model is relevant to AI-agent tool execution, cloud
   authorization, service meshes, financial and database commits,
   operating-system and device actions, confidential computing,
   accelerator/DPU/SmartNIC infrastructure, and industrial control.
   Microsoft Azure Policy, Amazon Verified Permissions/Cedar, Google
   Cloud VPC Service Controls, NVIDIA attestation, and Arm CCA are cited
   only as complementary industrial comparison or integration points,
   not as assertions of vulnerability, deficiency, non-conformance,
   affiliation, or endorsement.

   The proposed delta is not invention of complete mediation.  It is an
   explicit, testable mapping of complete-mediation reasoning to a
   protected consequence across heterogeneous distributed software and
   hardware paths, with coverage bound to a topology generation and to
   effectuation-time finality.  Criticism, corrections, counterexamples,
   prior-art pointers, evidence of equivalent existing mechanisms, and
   cases where path completeness cannot be established at acceptable
   cost are explicitly invited.
- **draft-das-ai-factory-silicon-finality-02** (new-draft, score 25, core_identity) [none]: [Execution Finality for AI-Factory Silicon and Accelerated Infrastructure: Enforcement Profiles for GPUs, Chiplets, Memory Fabrics, DPUs, RDMA, CXL, and Photonic Boundaries](https://datatracker.ietf.org/doc/draft-das-ai-factory-silicon-finality/) — AI factories and AI-native infrastructure are heterogeneous control
   systems in which CPUs, GPUs, NPUs, memory controllers, CXL and PCIe
   paths, DMA and RDMA engines, DPUs, SmartNICs, accelerator fabrics,
   chiplets, storage, optical interconnects, model-serving runtimes,
   schedulers, firmware, and physical power or cooling controllers can
   all participate in one consequential operation.  Existing industry
   mechanisms such as authentication, access control, workload identity,
   attestation, confidential computing, IOMMU/SMMU isolation, memory
   protection, transport security, scheduler policy, safety logic, and
   hardware roots of trust are necessary building blocks, but they do
   not by themselves define one common rule for whether the exact
   pending operation is still authorized at the instant and location
   where it becomes effective.

   This document describes that missing effectuation-boundary rule.  In
   plain engineering terms, the architecture holds a consequential
   operation in a pending or inhibited state, identifies the exact
   command, transfer, route, memory range, output, configuration change,
   or actuation request, validates current authority and protected
   state, binds a narrowly scoped authorization artifact to those exact
   parameters and to the intended enforcement boundary, and requires the
   boundary that physically or logically controls the consequence to
   verify the binding before commit.  The boundary therefore acts like a
   policy enforcement point, reference monitor, transaction-commit gate,
   command gate, safety interlock, actuation gate, output-release gate,
   or hardware admission controller, depending on the deployment domain.

   The document uses the specialized terms Candidate Act, Non-Effective
   State, Protected Enforcement Domain, Protected Validation Evidence,
   scoped non-bearer capability, and Finality Sink.  These terms name
   functions rather than required products or protocol objects.
   Equivalent implementations may instead use concepts such as a staged
   transaction, command descriptor, authorization decision record,
   sender-constrained or context-bound permit, anti-replay state,
   generation or fencing epoch, compare-and-swap style commit, fail-safe
   inhibit, or transactional check-and-commit.  The functional
   requirement is that the actual pending effect cannot complete through
   the protected path unless the exact act, current state, freshness,
   scope, destination, and effectuation boundary still correspond.

   The Finality Sink is the component with mandatory control over the
   consequence.  Depending on the profile, it may be a memory
   controller, HBM gate, GPU scheduler, accelerator partition
   controller, IOMMU or SMMU, DMA or RDMA engine, DPU or SmartNIC,
   fabric switch, chiplet link controller, CXL component, cache-
   coherence controller, model loader, token-emission gate, optical
   modulator or wavelength controller, eFPGA configuration gate, rack
   power controller, radio-control path, or another protected commit
   point.  Physical separation from the compute component is not
   required; mandatory mediation and protected verification are
   required.

   The document provides 98 detailed Enforcement Profiles.  Sixty-three
   translate the supplied GPU, silicon, chiplet, memory-fabric, and AI-
   factory source set; twelve supplementary profiles map the same
   execution-finality model onto current hyperscale and Arm-based
   infrastructure directions; eight additional profiles selectively
   adapt non-duplicative mechanisms from companion DAS Protocols
   disclosures for silicon and AI-factory use; and fifteen profiles
   address electrical package-I/O, sideband, error, test, and coherence-
   transition boundaries.  Profile identifiers retain source numbering
   for traceability, so gaps are intentional.

   The architecture is intended to complement, not replace, accelerated
   computing, confidential computing, chiplet and coherent-memory
   protocols, accelerator fabrics, optical I/O, attestation, identity,
   authorization, hardware isolation, safety engineering, and existing
   control systems.  The IETF relevance is principally the cross-layer
   relationship among identity, evidence, attestation, cryptographic
   binding, protected state, replay resistance, delegation, and the
   final effectuation boundary.  Hardware-specific wire protocols remain
   within the remit of the appropriate hardware, semiconductor,
   telecommunications, optical, automotive, aerospace, and control-
   system standards bodies.  The common invariant is: computation may
   produce a proposed act, but computation alone is not authority for
   consequence.
- **draft-das-ef-registries-01** (new-draft, score 25, trust_infrastructure) [none]: [Illustrative Codes Are Not a Namespace: Registries for Execution-Finality Consequence Classes, Sink Types, Act Types, Failure Codes, Profiles, and Media Types](https://datatracker.ietf.org/doc/draft-das-ef-registries/) — The execution-finality family uses a shared vocabulary: Candidate
   Act, Execution Handle, Finality Sink, consume, and Finality Receipt
   [DAS-HANDLE] [DAS-PROTOCOL].  Each profile currently invents
   overlapping labels for the same ideas — FINANCIAL, SETTLEMENT, EF-
   005, SINGLE_USE — and then states that the codes are illustrative and
   not IANA assignments.  Two implementations can therefore emit the
   same token string with different meaning, or different strings for
   the same deny reason.

   Existing IANA registries already name adjacent objects.  JWT and CWT
   claim names [RFC7519] [RFC8392], OAuth parameters [RFC6749]
   [RFC7591], HTTP problem types [RFC9457], media types, RATS EAT
   claims, and SCITT statement types [RFC9943] solve identity, token,
   and transparency naming.  They do not allocate consequence class,
   sink type, act type, handle reuse policy, execution-finality failure
   code, or finality-profile identifiers.

   This document proposes those registries and an initial allocation
   drawn from the family drafts.  It does not decide which acts should
   be authorized.  It does not replace OAuth error codes, HTTP status
   codes, or application problem types.  A registered code is a shared
   name for a machine-readable condition; it is not a legal
   classification and not evidence that any named product implements the
   condition.

   Until IANA action occurs, codes in this document and in companion
   drafts remain provisional.  Implementations MUST treat foreign
   namespaces as distinct.  Criticism of the registry split, the initial
   code list, the registration policy, and the claim that a new
   namespace is required at all is explicitly invited.
- **draft-ietf-wimse-aims-00** (new-draft, score 25, core_identity) [wimse]: [AI Identity Management System](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/) — This document proposes best practices for authentication and
   authorization of AI agent interactions.  It leverages existing
   standards such as the Workload Identity in Multi-System Environments
   (WIMSE) architecture and OAuth 2.0 family of specifications.  Rather
   than defining new protocols, this document describes how existing and
   widely deployed standards can be applied or extended to establish
   agent authentication and authorization.  By doing so, it aims to
   provide a framework within which to use existing standards, identify
   gaps and guide future standardization efforts for agent
   authentication and authorization.
- **draft-das-drip-uas-act-finality-01** (new-draft, score 24, trust_infrastructure) [none]: [Cleared to Fly or Drive Is Not Cleared to Act: Actuator-Level Execution Finality and Compact Act Evidence for UAS and Autonomous Vehicles](https://datatracker.ietf.org/doc/draft-das-drip-uas-act-finality/) — Problem: Unmanned Aircraft System (UAS) trust infrastructure answers
   two questions well.  Remote Identification (RID), strengthened by the
   Drone Remote ID Protocol (DRIP), answers "who is this aircraft?", and
   UAS Traffic Management (UTM), U-space, and geo-awareness answer "may
   this flight take place here and now?".  Neither answers the question
   that decides physical consequence: may this specific act -- arming
   motors, crossing into a newly restricted volume, releasing a delivery
   payload, activating a camera over a protected area, emitting on a
   radio band, or joining a coordinated multi-aircraft manoeuvre --
   become effective at this actuator, at this instant, under the
   airspace and revocation state that is current now?  Authorizations
   are granted before or at take-off, while acts are executed
   continuously by mission computers and autonomy stacks that can be
   compromised, misled, coerced with validly signed commands, or cut off
   from their authorities.  Observers on the ground, in turn, can verify
   an aircraft's identity but not whether what it is doing was
   authorized before it happened.

   Solution: The IETF-facing contribution of this document is Compact
   Broadcast Act Evidence: 16-octet per-act decision records
   authenticated with a TESLA-style one-way key chain sealed inside a
   Protected Enforcement Domain and anchored to the aircraft's DRIP
   identity.  This lets an Observer verify, after a short disclosure
   delay and within the 25-octet Broadcast RID message budget, that the
   protected enforcement domain made an allow, deny, or safe-state
   decision before the corresponding evidence key was disclosed, without
   requiring a public-key signature on every act.  The evidence
   mechanism is coupled to an execution-finality profile in which each
   safety-significant or externally consequential act remains non-
   effective as a Candidate Act until the Protected Enforcement Domain
   verifies an act-bound, sink-bound Execution Handle against live
   trusted context, consumes current authority state atomically, commits
   a Finality Receipt, and only then releases the physical enablement
   condition at the Finality Sink.  The profile also specifies act
   classes and sinks, self-contained object fields, sink processing
   pseudocode, envelope handles for high-rate control, a boundary-
   proximity revalidation policy, bounded offline operation, and
   composite multi-aircraft semantics.  For constrained onboard, air-to-
   air, telemetry, or other small-frame links, the profile also defines
   an optional Beacon Proof Capsule (BPC): a compact act-bound and sink-
   bound execution-proof representation using an Authority Reference,
   freshness and generation state, a context commitment, a keyed binding
   commitment, explicit truncation-risk sizing, authenticated multi-
   frame reconstruction when necessary, and fail-closed resolver
   semantics.  A BPC is an input to execution verification; the AER/KDR/
   Anchor mechanism is output evidence of the PED decision, and the two
   roles are intentionally non-interchangeable.

   Additional profiles: This document also describes three narrowly
   scoped execution-finality embodiments: conflict-set-bound Detect-and-
   Avoid (DAA) resolution finality for UAS, emergency-scene temporary
   authority finality for autonomous road vehicles as an informative
   cross-domain application, and atomic control-authority handover with
   monotonic authority epochs for autonomous motion platforms.  These
   profiles preserve the same rule: an authenticated or correctly
   computed instruction remains a Candidate Act until the current
   effectuation boundary independently verifies the state on which that
   instruction depends.  In an autonomous road vehicle, that boundary
   may be a protected motion-admission gate rather than a motor or ESC
   gate, so the architecture can coexist with the vehicle's existing
   perception, planning, braking, steering, and minimal-risk-control
   functions.

   Industrial context and complementarity: The mechanism complements,
   and does not replace, Broadcast and Network RID, DRIP Entity Tags and
   authentication, DET resolution through DNS, UTM and U-space services,
   geo-awareness, Detect-and-Avoid, flight-control safety logic,
   automotive ADAS/autonomy stacks, remote-assistance systems, and
   authenticated command channels.  Publicly described examples of the
   kinds of software-defined or autonomy-enabled platforms to which this
   boundary can be complementary include Tesla driver-assistance
   systems, BYD DiPilot and related intelligent-driving platforms, DJI
   enterprise drone automation, Boeing autonomous and uncrewed aircraft
   systems, and Lockheed Martin/Sikorsky autonomous aircraft systems.
   These names are illustrative only: this document does not state or
   imply that any named organization uses, endorses, requires, or has
   evaluated this profile.  Their existing perception, planning,
   stabilization, DAA, ADAS, command-and-control, and safety mechanisms
   remain in place; the proposed finality layer operates later, at a
   protected motion-admission or actuator boundary, to verify the
   concrete pending act against current protected authority and state
   before effectuation.  The scope of this document remains strictly
   civil and excludes weapon release, targeting, and counter-UAS
   engagement.  This is an individual Informational Internet-Draft, not
   a DRIP WG work item.  In short, its IETF/IRTF relevance is to DRIP
   (DET-anchored compact act evidence for Observers), RATS (attestation
   of the protected enforcement domain), COSE/CBOR (deterministic
   compact objects), ACE (constrained scoped authorization as input
   rather than effectuation), SCITT (later audit of receipts), and T2TRG
   (constrained Things with multiple authorities).  No WG adoption or
   code-point allocation is requested in this version; the draft is
   offered for technical discussion in those communities and in UAS,
   Remote ID, constrained-security, autonomous-vehicle, and aviation
   standards forums.
- **draft-das-agentic-effectuation-boundary-00** (new-draft, score 23, trust_infrastructure) [none]: [When AI Agents Hold the Keys: Threat Model and Execution-Finality Requirements for Autonomous High-Consequence Systems](https://datatracker.ietf.org/doc/draft-das-agentic-effectuation-boundary/) — AI agents are increasingly being delegated authority to invoke APIs,
   move money, modify enterprise state, operate infrastructure, and
   trigger physical actions.  Existing mechanisms for authentication,
   authorization, proof-of-possession, attestation, request
   preconditions, and authorization-context propagation are necessary
   building blocks, but they do not by themselves establish a universal
   invariant that the exact consequential act approved earlier is the
   exact act permitted to become effective now.

   This document defines a threat model for autonomous high-consequence
   agents and identifies an effectuation-boundary gap: a request can be
   correctly authenticated, correctly authorized, correctly attested,
   and still be unsafe to execute because parameters, policy state,
   external prerequisites, delegation state, lineage, or the execution
   path changed after the earlier decision.  The document describes an
   execution-finality architecture in which a proposed act remains non-
   effective until a protected enforcement point verifies exact-act
   binding, freshness, current policy state, anti-replay state, required
   provenance, and path completeness immediately before effectuation,
   with authority consumed in coordination with the consequential
   commit.
- **draft-das-execution-finality-ai-interoperability-05** (new-draft, score 23, authorization) [none]: [Secure and Privacy-Preserving AI Interoperability under Article 6(7) of the European Digital Markets Act: An Execution-Finality Architecture](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-interoperability/) — AI assistants increasingly interoperate with operating-system
   functions, applications, cloud services, payments, files, messaging,
   sensors, network interfaces, and device controls.  In that
   environment, authenticating an assistant or granting it a broad
   permission does not by itself answer the final security question:
   whether this exact pending operation, with these exact parameters and
   this current system state, is authorized to become externally
   effective.

   Existing mechanisms such as operating-system permissions and
   sandboxing, application intents and typed APIs, OAuth delegated
   authorization, Rich Authorization Requests, sender-constrained
   tokens, trusted execution environments, attestation, hardware-backed
   keys, transaction preconditions, and audit logs address important
   parts of that problem.  They can also be composed with the
   architecture described here.  However, those mechanisms do not
   inherently require the complete sequence defined in this document:
   keep the proposed act non-effective, bind authority to the exact act
   and current protected state, re-derive the actual pending consequence
   at a mandatory effectuation boundary, consume freshness or budget
   state in a TOCTOU-resistant manner, and deny any alternate path that
   could cause the same protected effect without the final check.

   This document calls the staged operation a Candidate Act and the pre-
   effect condition the Non-Effective State.  A Protected Execution
   Domain performs protected validation and may commit pre-effect
   validation evidence, including a LAVR.  It then makes available
   narrowly scoped, non-bearer execution authority bound to the exact
   act, requester, resource, destination, policy and revocation epoch,
   freshness state, Finality Sink, and Effectuation Boundary.  The
   Finality Sink is the mandatory policy-enforcement or command/commit
   gate that independently reconstructs the actual operation immediately
   before the consequence can occur.

   In conventional security and control terminology, the architecture
   combines properties associated with a reference monitor, policy
   enforcement point, safety interlock, command gate, actuation gate,
   transactional authorization check, cryptographic parameter binding,
   proof-of-possession or sender-constrained authority, anti-replay
   state, fencing or generation epochs, bounded capabilities, and a
   TOCTOU-resistant check-and-commit operation.  The terminology is not
   intended to require one component name, protocol, hardware block, or
   packaging model; functional equivalence depends on the enforcement
   sequence and invariants.

   The design addresses prompt injection, compromised assistants or
   cloud infrastructure, confused-deputy behavior, replay, token theft
   or reuse, destination and parameter substitution, scope escalation,
   stale authorization, policy or revocation changes, wrong-sink
   presentation, alternate-path bypass, crash ambiguity, persistent-
   state rollback, and unauthorized consequential execution.  It also
   supports privacy minimization by allowing a platform to expose a
   narrow act without granting reusable authority over an entire
   application or data class.

   For interoperability deployments, the intended result is open
   participation with bounded, verifiable effectuation authority: a
   third-party or first-party AI may propose the same class of device or
   service action, while the platform or service independently enforces
   whether the concrete action may cross the protected consequence
   boundary.  This document describes a technical architecture and does
   not determine whether a particular deployment satisfies the Digital
   Markets Act, GDPR, the EU AI Act, or any other legal requirement.

   The same engineering question is relevant beyond any single assistant
   or mobile platform.  Representative current interoperability contexts
   include Google Gemini on Android, where Gemini can operate as a
   default digital assistant and Android exposes device-assistance
   functions and AppFunctions-style application capabilities for use by
   agents and assistants, including MCP-oriented integrations; Apple's
   iOS and iPadOS interoperability-request process in the European Union
   under DMA Article 6(7), together with the public Siri AI
   interoperability and security discussion; European AI-assistant and
   agent ecosystems including Mistral Vibe in France, Deutsche Telekom's
   Magenta AI Call Assistant in Germany, Proton Lumo in Switzerland, and
   Infomaniak Euria in Switzerland; and public agent and tool ecosystems
   associated with OpenAI, Anthropic, Microsoft, and Amazon Web Services
   (AWS), which connect AI systems to external tools, applications,
   APIs, data sources, cloud services, communications, or other agents
   through mechanisms such as tool calling, agent frameworks, the Model
   Context Protocol (MCP), Agent2Agent (A2A), and related integration
   interfaces.  The named systems are not asserted to provide identical
   capabilities: some are operating-system or device assistants, some
   are communications-integrated assistants, and others are broader
   conversational or agent platforms.  They are referenced only as
   representative industry contexts in which act-specific authority and
   effectuation-boundary enforcement may be relevant; no review,
   endorsement, adoption, affiliation, or absence of equivalent
   safeguards is implied.

   The June 2026 Siri AI dispute provides one public example of the
   underlying engineering tension.  Apple stated
   (https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-
   in-eu-for-ios-27-and-ipados-27/) that Siri AI would not initially
   ship on iOS 27 and iPadOS 27 in the European Union and attributed the
   delay to DMA interoperability and privacy/security concerns.  The
   European Commission publicly stated (https://digital-markets-
   act.ec.europa.eu/citizens-and-whistleblower-portal/eu-citizens-qa_en)
   that the DMA does not prohibit the product launch and that
   interoperability may be implemented subject to applicable
   requirements and user consent.  This document does not resolve those
   legal or policy positions; it uses the dispute as a concrete
   interoperability threat-model example and proposes one technical
   pattern for separating access to request functionality from authority
   to create the final effect.

   Two runnable reference implementations are linked in this document.
   The second is an adversarially hardened follow-on that adds a fresh
   Finality-Sink challenge, challenge-bound proof of possession, strict
   object validation, cross-object consistency checks, explicit temporal
   enforcement, exact-effect binding, and an expanded executable test
   suite.  These implementations are engineering demonstrations in
   virtual/local environments, not production certification or
   regulatory-conformance determinations.
- **draft-seymour-wimse-connected-flight-00** (new-draft, score 23, authorization) [none]: [Zero Trust Fabric Layer Agent-to-Agent Chained Trust on a Connected Flight](https://datatracker.ietf.org/doc/draft-seymour-wimse-connected-flight/) — The Zero Trust Fabric Layer (ZTFL) verified a single autonomous agent
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
   containment at the boundary itself.
- **draft-sharif-agent-audit-trail-04** (new-draft, score 23, core_identity) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
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
- **draft-das-cvid-enforcement-profiles-01** (new-draft, score 21, authorization) [none]: [Capability-Validated Inbound Descriptors: Catalogue of Enforcement Profiles](https://datatracker.ietf.org/doc/draft-das-cvid-enforcement-profiles/) — Modern networks, AI systems, cloud platforms, vehicles, radios,
   accelerators, and control systems often authenticate a requester,
   authorize access, attest a workload, or complete a computation before
   the resulting operation reaches the component that can make it
   externally effective.  Those checks are necessary, but an earlier
   approval can become stale, be replayed, be applied to changed
   parameters, or be exercised through a different consequence path.
   This document describes seventy-seven enforcement profiles for a
   common engineering pattern: keep a pending operation in a non-
   effective or inhibited state until a mandatory enforcement point at
   the actual consequence boundary verifies that the exact live
   operation still matches current bounded authority.

   The document uses the term Capability-Validated Inbound Descriptor
   (CVID) for one representation of that bounded machine-verifiable
   authority.  In ordinary industry terminology, the same function may
   be implemented as an act-specific authorization descriptor,
   constrained capability, one-shot permit, transaction authorization,
   command permit, or protected release token.  The final enforcement
   role may be implemented as a policy enforcement point, reference
   monitor, safety interlock, command gate, actuation gate, transaction
   commit guard, packet-egress gate, RF enable gate, secure resolver,
   hardware release controller, or another mandatory control point.
   Functional equivalence depends on the enforced sequence and failure
   behavior, not on use of a particular name.

   The common sequence is: identify the exact pending act or output;
   keep it non-effective; bind authority to effect-determining
   parameters, destination or sink, current generation or policy state,
   freshness, and bounded-use state; reconstruct or observe the live
   operation at the consequence boundary; recheck current revocation,
   replay, quota, and fencing state; and serialize final verification
   and authority consumption with the consequence-bearing commit.
   Missing, stale, revoked, replayed, mismatched, exhausted,
   unavailable, or indeterminate required state leaves the protected
   consequence unavailable unless an explicitly defined fail-safe
   profile authorizes a narrower safe action.

   The profiles span inbound communication; network capability exposure
   and intent-driven network programming; AI-native radio access,
   network slicing and packet core; distributed inference and digital
   twins; ultra-reliable low-latency operation; cross-border and
   sovereignty-bound execution; satellite, non-terrestrial and direct-
   to-device networks; optical inter-satellite links; immersive and
   semantic media; machine swarms; ambient IoT and backscatter;
   reconfigurable intelligent surfaces; device paging and wake; offline
   central-bank-digital-currency settlement; lawful disclosure through
   escrow; platform-neutrality measurement; network energy expenditure;
   accelerator output paths; DMA and RDMA boundaries; interconnects and
   die-to-die interfaces; eSIM/eUICC activation; subscriber rebinding;
   roaming; UPF egress; break-glass operation; key use; firmware and
   model activation; AI memory and vector persistence; agent and tool
   dispatch; streaming release; cumulative budgets; failover; and
   maintenance or debug paths.

   Three authorities are deliberately separated: authority to consume
   resources, authority to perform computation, and authority to cause
   an external effect.  The document is an individual technical
   submission offered for engineering review.  Existing authentication,
   authorization, attestation, safety, transaction, and hardware-
   isolation mechanisms can supply parts of the required enforcement;
   the architectural delta is the explicit consequence-bound check that
   keeps the exact pending operation non-effective until current
   authority is verified at the last mandatory point before effect.
- **draft-das-enterprise-ai-enforcement-profiles-01** (new-draft, score 21, authorization) [none]: [Securing the Enterprise Future: Technical Non-Joinability for Enterprise AI](https://datatracker.ietf.org/doc/draft-das-enterprise-ai-enforcement-profiles/) — Enterprise artificial-intelligence systems are increasingly connected
   to multiple organizational repositories, applications, tools, memory
   systems, and workflow interfaces.  Representative industrial
   deployment classes include OpenAI ChatGPT and ChatGPT Work, Anthropic
   Claude, Google Gemini Enterprise, xAI Grok for Business, Microsoft
   Copilot and Copilot Studio, Amazon Q Business, Salesforce Agentforce,
   ServiceNow AI Agents, and comparable enterprise or privately deployed
   AI systems.  These names are cited only as publicly described
   examples of the broader deployment class.  Their inclusion does not
   assert that any named product implements, lacks, requires, endorses,
   or is vulnerable to the mechanisms described here, does not
   characterize undisclosed internal architectures, and does not imply
   that equivalent functionality is absent from an existing product or
   specification.

   The security problem considered here is not limited to theft of a
   pre-existing database.  An enterprise-AI workload may be individually
   authorized to retrieve information from customer, engineering,
   financial, source-code, supplier, scheduling, communication, memory,
   and operational systems while the combination of those sources
   reveals a sensitive relationship or future enterprise state that no
   single repository contains.  Conventional access control, encryption,
   network segmentation, database separation, confidential computing,
   and source-level authorization remain important, but storage
   separation alone does not prevent such reconstruction where the same
   effective authority can obtain the constituent values and freely
   resolve the relationships among them.

   The mechanism described here therefore separates not only protected
   data but also the authority required to create protected semantic
   relationships among that data.  Identity components, substantive
   content, relationship-mapping information, reconstruction-enablement
   state, and authorization state may be maintained under independently
   controlled protection domains.  A processing request establishes a
   bounded reconstruction authorization tied to the actual workload,
   execution context, session, permitted fields, permitted
   relationships, processing purpose, and output conditions.  Each
   required protection domain independently determines whether its
   component may participate.  Approved components may remain session
   bound, cryptographically wrapped, capability restricted, opaque, or
   accessible only through a mandatory mediated path.  Only the
   specifically authorized relationships are resolved inside a protected
   reconstruction environment, which constructs a temporary minimum-
   necessary view without providing the AI workload with unrestricted
   authority over the underlying stores.

   This creates a technical distinction between authority to access
   information and authority to associate information.  Access to an
   identity component and access to a content component do not, by
   themselves, authorize every relationship between them.  The same
   distinction applies after computation: successful reconstruction,
   inference, or generation does not automatically authorize disclosure,
   persistence, transmission, tool invocation, database modification,
   payment, downstream-model use, or another external consequence.  A
   resulting output or proposed act can remain technically non-
   releasable while current session, execution, association, provenance,
   destination, recipient, policy, revocation, and disclosure conditions
   are verified.  Protected evidence of successful verification is
   committed before scoped release authority is created and checked at
   the actual consequence boundary.

   This document presents 79 Enforcement Profiles that apply the same
   underlying architecture to different enterprise-AI enforcement
   points, including multi-domain information separation, independent
   association authority, session-bound reconstruction, protected
   provenance, runtime behavioral verification, agentic tool invocation,
   prompt and input mediation, streaming disclosure, lifecycle
   restrictions, distributed policy enforcement, and multi-authority
   consequence control.  Each profile is expressed in terms of the
   problem being addressed, the technical enforcement mechanism, and its
   relationship to existing technology so that the underlying
   engineering concept can be evaluated independently of specialized
   terminology.

   This document is related to the earlier [DAS-ENTERPRISE-OUTPUT],
   which introduced the broader enterprise-future-reconstruction threat,
   protected reconstruction, and output-finality architecture.  The
   principal new contribution here is the systematic decomposition of
   that architecture into 79 concrete enforcement profiles, together
   with a more explicit treatment of Technical Non-Joinability as a
   separately enforceable property governing when independently
   accessible enterprise information may be semantically associated.

   The common engineering principle is that access to components is not
   necessarily authority to join them, and completion of computation is
   not necessarily authority to make the resulting consequence
   externally effective.
- **draft-wilder-scitt-physical-site-engage-receipt-04** (new-draft, score 21, trust_infrastructure) [none]: [A SCITT Profile for Physical-Site Engagement Receipts](https://datatracker.ietf.org/doc/draft-wilder-scitt-physical-site-engage-receipt/) — This document defines a SCITT profile for _Physical-Site Engagement
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
   registered every receipt it issued.

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
- **draft-das-state-policy-continuity-finality-00** (new-draft, score 20, authorization) [none]: [When Valid Authorization Becomes Stale: State and Policy Continuity at the Execution-Finality Boundary](https://datatracker.ietf.org/doc/draft-das-state-policy-continuity-finality/) — Security decisions are frequently made against mutable state.  An
   authorization decision may depend on a policy bundle, mapping table,
   reference-value set, ownership record, revocation state, risk
   classification, purpose grant, account state, or other data that can
   change between evaluation and effectuation.  A cryptographically
   authentic permit can therefore remain valid as an object while
   becoming stale as authority.

   Existing freshness, replay-protection, sender-constraining,
   attestation, and anti-rollback mechanisms solve important parts of
   this problem.  They do not by themselves establish that the exact
   policy and state basis used to approve an act is still the applicable
   basis when that act becomes externally effective.

   This document describes a state- and policy-continuity model for
   execution finality.  A Candidate Act remains non-effective until a
   protected Finality Sink verifies the concrete act, the identity of
   the evaluated policy or mapping content, protected generations or
   epochs, relevant mutable state, freshness, and authorized-use
   constraints immediately before effectuation.

   The model treats revision identity as content-bound rather than
   merely name- or location-bound.  A change from one mapping or policy
   revision to another is a state transition that requires re-evaluation
   unless an authoritative mechanism explicitly establishes
   applicability across revisions.  The Finality Sink is not expected to
   infer semantic equivalence dynamically.

   The model complements, rather than replaces, mechanisms such as RATS,
   Entity Attestation Tokens, SUIT anti-rollback controls, OAuth fine-
   grained authorization, sender-constrained tokens, and application
   policy engines.  Its central invariant is that authorization valid at
   evaluation time is not automatically authority at effectuation time.

   The problem is industrially relevant to systems that already combine
   continuously evaluated access, fine-grained policy decisions,
   attestation, and confidential computing.  Examples of complementary
   industry directions include Microsoft Entra Continuous Access
   Evaluation, Amazon Verified Permissions and Cedar, Google Cloud IAM
   policy enforcement, NVIDIA GPU and switch attestation, and Arm
   Confidential Compute Architecture.  These names identify useful
   integration and comparison points; they are not assertions of
   vulnerability, deficiency, non-conformance, or endorsement by any
   named organization.
- **draft-hardt-httpbis-signature-key-09** (new-draft, score 19, core_identity) [none]: [HTTP Signature Keys](https://datatracker.ietf.org/doc/draft-hardt-httpbis-signature-key/) — This document defines five HTTP header fields for use with HTTP
   Message Signatures as defined in RFC 9421.  The Signature-Key request
   header distributes public keys used to verify signatures, with eight
   initial key distribution schemes: pseudonymous inline keys (hwk),
   self-issued key delegation via JWK Thumbprint JWTs (jkt-jwt),
   identified signers with JWKS URI discovery (jwks_uri), direct JWKS
   fetch (jwks), JWT-based delegation (jwt), self-issued JWTs (self-
   jwt), X.509 certificate chains (x509), and references to previously
   cached assertions (cached).  The Accept-Signature-Scheme and Accept-
   Signature-Alg response headers state the schemes and algorithms a
   server accepts, so a client can select both before it signs.  The
   Signature-Error response header provides structured error information
   when signature verification fails, and the Signature-Key-Cache
   response header issues a cache identifier by which a caller can
   reference a previously presented assertion instead of resending it.
   Together, these mechanisms enable flexible trust models ranging from
   privacy-preserving pseudonymous verification to horizontally-scalable
   delegated authentication and PKI-based identity chains.
- **draft-tanase-ain-authoritative-resolution-00** (new-draft, score 19, adjacent_watchlist) [none]: [Authoritative Resolution and Pre-Interaction Verification of Persistent Digital Agent Identities](https://datatracker.ietf.org/doc/draft-tanase-ain-authoritative-resolution/) — This document specifies AIN-WRP, a protocol-independent mechanism for
   authoritative resolution of persistent digital agent identities and
   for verification of relationship-specific state before a digital
   agent begins a protected operational interaction with another agent
   or with a non-agent service or system.  An Agent Identity Number
   (AIN) acts as a stable lookup anchor.  The protocol resolves current
   identity, lifecycle, operator or authority, endpoint, mandate,
   restriction, provenance, and cryptographic verification information
   from sources competent to make the corresponding assertions.

   AIN-WRP separates persistent identity from credentials, proof of
   control, delegated authority, operational eligibility, policy
   decision, and execution.  For participants operating under
   independent administrative domains, the protocol performs logically
   independent resolution, validates source competence and evidence
   freshness, correlates the resulting assertions for the proposed
   relationship, and produces a Pre-Interaction Trust State.  A signed,
   time-limited State Proof may convey that state to a gateway or
   relying party.  The gateway applies local policy and controls whether
   an A2A, MCP, API, messaging, transactional, or proprietary protocol
   begins.

   This version defines the protocol model and the initial requirements
   for future interoperable profiles.  It does not require all AIN
   registration, resolution, assertion issuance, policy evaluation, or
   operational enforcement to be performed by a single central service,
   a mandatory Regional Network Operator (RNO), or a particular gateway,
   identity provider, authorization framework, or execution protocol.
- **draft-das-composite-execution-finality-01** (new-draft, score 18, trust_infrastructure) [none]: [Partial Commit Is Not Finality: Composite Candidate Acts Across Multiple Finality Sinks](https://datatracker.ietf.org/doc/draft-das-composite-execution-finality/) — An agent, a payment orchestrator, or a control-plane applicator often
   intends one Candidate Act that would become real only as several
   consequences: a settlement post, a ledger write, a tool invoke, a
   notification, a radio enable.  [DAS-HANDLE] specifies verify,
   consume, and receipt at one Finality Sink.  It does not say what "the
   act was permitted" means when sink S1 has consumed and posted and
   sink S2 has rejected, timed out, or committed a different digest.

   Existing distributed-transaction tools already address adjacent
   problems.  Two-phase commit, XA, sagas, TCC, transactional outbox,
   and workflow engines coordinate steps.  OAuth, WIMSE, RATS, and SCITT
   still name identity, environment, and signed statements.  None of
   them, by themselves, bind N sink-local Execution Handles to one
   composite Act Digest and require that no child consequence become
   externally effective unless every required child reaches a defined
   terminal state.

   This document specifies Composite Candidate Acts, child handles, a
   coordinator that may only prepare, a two-phase consume rule, and the
   distinction between prevention (no child commits unless the composite
   closes) and mitigation (compensate after a partial post).
   Compensation is itself a Candidate Act.  It is not a silent undo and
   not a license to skip verify on the original child.

   The join is closed by a durable, linearizable Composite Decision Log
   holding one value per composite: empty, COMMIT, or ABORT, written
   only by compare-and-swap so that the first writer wins.  The
   coordinator MUST win the log before sending a decision to any child.
   A prepared child whose reservation timer expires MUST consult the
   log: it commits if COMMIT is recorded, releases if ABORT is recorded,
   attempts its own compare-and-swap of ABORT if the log is empty, and
   holds its reservation (HOLD) only if the log is unreachable.  No
   child acts on silence alone.

   This is not a new consensus protocol and not a claim that XA is
   obsolete.  Profiles that cannot obtain prepare-from-every-sink, or
   cannot reach a durable linearizable decision log, MUST NOT claim all-
   or-none prevention.

   Three rejections are expected and are treated as design constraints.
   "Saga plus handle is enough" is accepted when each saga step already
   reconstructs the live child, consumes a child handle, and cannot log
   SUCCESS after a required child rejects; this draft then shrinks to
   join fields.  Prepare across N sinks is a latency tax only if
   consume-state is global; it is per child handle, and a no_prepare
   mail or MCP child must use the mitigation profile rather than pretend
   2PC.  Child sinks reconstruct only their own pending effect, not a
   mesh-wide CAD.  Reviewers who would reject on saga, performance, or
   reconstruction grounds are asked to read those sections before
   discarding the document.  Criticism, including "this should stay a
   note in the handle draft," remains invited.
- **draft-das-satellite-orbital-finality-profiles-00** (new-draft, score 17, trust_infrastructure) [none]: [Execution-Finality Profiles for LEO/NTN Satellites, Orbital AI, Optical ISLs, Spacecraft Autonomy, and Cybersecurity](https://datatracker.ietf.org/doc/draft-das-satellite-orbital-finality-profiles/) — Satellite and non-terrestrial networks are becoming programmable
   compute, routing, sensing, radio, and AI infrastructures.  In such
   systems, successful authentication, attestation, routing, scheduling,
   inference, fault recovery, or protocol processing does not
   necessarily establish authority for the resulting operation to become
   externally effective.

   This document describes an execution-finality architecture in which a
   consequence-bearing operation is represented as a Candidate Act and
   may remain in a Non-Effective State after computation.  A Protected
   Enforcement Domain validates act-bound predicates and protected
   state, commits protected validation evidence, and permits release of
   scoped non-bearer authority.  A Finality Sink at or before the
   relevant consequence boundary verifies that authority before an
   operation becomes routing-effective, radiative-effective, storage-
   effective, control-effective, disclosure-effective, or otherwise
   externally effective.

   Sixty satellite and NTN enforcement profiles are provided, covering
   orbital AI output release, model-state transfer, Earth observation,
   power- and thermal-bounded compute, radiation recovery, optical
   inter-satellite links, onboard gNB and user-plane functions, delay-
   tolerant delivery, emergency services, firmware and microcode
   activation, privileged maintenance, orbital maneuver and collision-
   avoidance authority, proximity operations, propulsion and attitude
   actuation, hosted-payload control, sensing activation, end-of-life
   decommissioning, manufacturing and launch-preparation component
   admission, and high-consequence command release.  Each profile states
   a concrete problem space and the corresponding execution-finality
   solution.

   Publicly described work from SpaceX / Starlink, Blue Origin, Northrop
   Grumman / SpaceLogistics, Rocket Lab, Airbus Defence and Space, and
   Thales Alenia Space illustrates industry directions involving direct-
   to-device connectivity, optical inter-satellite networking, orbital
   mobility, hosted and software-defined payloads, onboard processing,
   rendezvous and proximity operations, and in-orbit servicing.  These
   references identify technical complementarity and possible
   enforcement locations; they do not imply that any named organization
   has reviewed, endorsed, adopted, or lacks equivalent mechanisms.

   The proposal does not replace 3GPP NTN, IETF routing or Time-Variant
   Routing, DTN, RATS/attestation, ACE authorization, SUIT update
   mechanisms, optical-link protocols, spacecraft fault detection,
   isolation and recovery, or cryptographic authentication.  Those
   mechanisms can provide inputs to the finality decision.  The
   additional question is whether a specific Candidate Act is permitted
   to cross the boundary at which it first acquires external effect.
   Technical corrections and references to equivalent existing
   mechanisms are expressly invited.
- **draft-senarath-a2wp-00** (new-draft, score 16, verifiable_claims) [none]: [Agent-to-Wallet Protocol for Digital Credentials (A2WP)](https://datatracker.ietf.org/doc/draft-senarath-a2wp/) — This document defines the Agent-to-Wallet Protocol (A2WP), an
   interface through which a software Agent requests digital credential
   operations from a Wallet.  A2WP supports credential acquisition,
   presentation, and optional queries for authorized credential
   metadata.  The Wallet controls credential selection, disclosure,
   approval, and cryptographic execution.

   A2WP defines an information model, observable operation behavior, and
   an HTTPS binding.  Credential formats, Agent identity schemes,
   delegation mechanisms, policy languages, and Wallet internals are
   outside its scope.  External credential protocols are integrated
   through protocol mappings.
- **draft-bu-agentproto-security-principal-binding-07** (new-draft, score 15, core_identity) [none]: [Security Principal and Verifier Binding for Agent Communication Protocols](https://datatracker.ietf.org/doc/draft-bu-agentproto-security-principal-binding/) — Agent communication protocols often carry claims about user
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

   The document also defines row-outcome semantics and dependency-
   closure rules for composed mappings.  These rules prevent a composite
   result from becoming stronger than its verified inputs, distinguish
   failed checks, unsupported verifier capabilities, checks skipped
   after a failed prerequisite, and unavailable or ambiguous inputs,
   propagate transitive dependency failures, and make cyclic, stale,
   downgraded, or revision-incoherent dependencies visible to reviewers.
- **draft-bormann-jwp-modular-bbs-03** (new-draft, score 14, verifiable_claims) [none]: [BBS and Modular Sub-proofs with JSON Web Proofs](https://datatracker.ietf.org/doc/draft-bormann-jwp-modular-bbs/) — This document defines a digital credential format that uses JSON Web
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
- **draft-das-attestation-interconnect-finality-00** (new-draft, score 14, authorization) [none]: [When Attestation Is Not Enough: Execution Finality for High-Assurance Resource Transitions](https://datatracker.ietf.org/doc/draft-das-attestation-interconnect-finality/) — Modern infrastructure increasingly allows memory, accelerators,
   device interfaces, storage regions, and other resources to move
   dynamically between hosts, tenants, virtual machines, and security
   domains.  Existing mechanisms can authenticate devices, attest
   software and firmware state, protect communication, and authorize
   resource operations.  However, these properties do not necessarily
   establish that the exact resource transition that becomes effective
   is still the transition that was evaluated and authorized.

   This distinction becomes security-critical when a change in
   addressability, ownership, routing, or device assignment itself
   exposes protected state.  For example, a dynamically reassigned
   memory extent may become accessible to a new tenant even though the
   device is authentic and the transport is protected, if sanitization,
   ownership state, allocation generation, destination binding, or other
   required conditions are no longer valid at the moment of
   reassignment.

   This document describes an execution-finality model in which a
   proposed transition remains non-effective until a protected
   enforcement boundary verifies the concrete operation immediately
   before effectuation.  Authorization is bound to the exact resource,
   source, destination, generation, security state, freshness
   conditions, and required preconditions, with replay and alternate-
   path protections.

   The problem is particularly relevant to high-assurance AI and
   composable-compute environments, including NVIDIA NVLink-based
   confidential multi-GPU systems, Arm Confidential Compute Architecture
   (CCA) and Realm Management Extension (RME) systems, UALink
   accelerator fabrics, CXL pooled-memory systems, and confidential-
   computing deployments operated by cloud providers.  These names
   identify published industry directions and alignment points; they are
   not assertions that any named implementation is vulnerable or non-
   conformant.

   The model complements attestation, confidential computing, secure
   transport, and device-assignment mechanisms rather than replacing
   them.  Its central security invariant is that a trusted component
   does not, by itself, imply a trusted transition.
- **draft-helmprotocol-tttps-10** (new-draft, score 14, adjacent_watchlist) [none]: [The TLS TimeToken Secure Protocol (tttps://)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies the TLS TimeToken Secure Protocol (tttps://),
   a protocol extension that augments TLS 1.3 with cryptographically
   verifiable temporal ordering.  TTTPS introduces Proof-of-Time (PoT):
   a multi-source synthesised timestamp bound to a holder identity and
   to a live TLS session through an explicit holder-proof construction,
   verified in constant time independent of network size.

   Internet infrastructure conventionally assumes ordering-neutral
   channels.  NTP servers, BGP routing authorities, DNS resolvers, and
   transaction sequencers all have an operational incentive to
   misrepresent event ordering; this document formalises that condition
   as the Strategic Channel Controller Problem (SCCP).  PoT detects
   Byzantine time-source manipulation with probability at least 1 minus
   2 to the negative 61st power, and an AdaptiveSwitch mechanism makes
   sustained ordering manipulation economically self-defeating; the
   equilibrium threshold is derived in closed form and empirically
   calibrated from deployed auction data.

   This document has Experimental status.  A reference deployment has
   produced over 70,000 verified records, 55 percent of which were
   generated by autonomous AI agents.  The mandatory-to-implement
   integrity mode (SHA-256) is completely and publicly specified in
   Appendix B; the optional GRG integrity mode is specified only through
   an abstract interface and is not required for conformance.

Discussion Note

   This note is to be removed before publishing as an RFC.

   This document is being discussed on the dispatch@ietf.org mailing
   list.  Comments and participation are welcome.

   Changes from -09:

   *  draft-10 integrates the Confidence and Deep-space companion
   profiles
      as optional, informative extensions without changing the PoT wire
      record or core integrity boundary.

   *  Added the seven-layer verification pipeline: PKI admission,
   physical
      deduplication, D-chain freshness, unique effective quorum,
   Byzantine
      aggregation, optional VN correlation, and read-only Epi-Entropy
   shadow.

   *  Added admissible density-bundle semantics, epistemic entropy
   interval,
      certified purity lower bound, identity ambiguity diameter, AHE
   bounded
      holdover, and explicit HOLD/CONSTRAINT_INCONSISTENCY outcomes.

   *  Added conservative claims and evidence boundaries: Epi-Entropy is a
      read-only shadow analysis; sparse peers do not create a quorum; simulated or
   offline
      evidence is not flight validation; universal Sybil prevention is
   not
      claimed.

   *  Header: revision -06 -> -07; submissionType corrected from "IETF"
      to "independent" (this document is an Independent Submission, not
      an IETF Working Group product); dates updated.

   *  Section 2 / Section 6.1 (the former binding_key construction): the
      -06 construction let any participant in the TLS session --
      including an attacker in its own session with the Issuer --
      recompute binding_key and pass verification without proving
      possession of any holder key material, because binding_key was
      derived solely from public TLS Exporter output and the public PoT
      bytes.  This is replaced with a PoT Record v2 (180 octets)
      carrying an explicit holder_auth_type (Ed25519 public key, MTI, or
      a pre-shared secret, OPTIONAL) and a binding_proof computed by the
      holder over the TLS Exporter output at binding time.  Verification
      now performs integrity-tag interpretation first, in a single
      fixed-cost pass with a three-way intact/resolved/unresolvable
      verdict; in -06 the equivalent check was ordered after five other
      checks.  The full 8-step order is specified in Section 2.5.

   *  Appendix B: removed the "(Placeholder)" designation.  Appendix B
      now specifies a public Integrity Algorithm Registry: alg_id 0x0001
      (SHA-256, detection-only) is the Mandatory-to-Implement algorithm
      and is completely and publicly specified. Optional profile
   algorithms
      are maintained outside the core; this revision does not assign or
      define GRG.

   *  IANA Considerations, HTTP/3 Stream Types: renamed from "HTTP/3 and
      QUIC Stream Types".  The "QUIC Stream Types" registry entry is
      removed; no such IANA registry exists, and QUIC stream
      identification for TTTPS is carried entirely by the HTTP/3-layer
      frame registration.

   *  Abstract: shortened from six paragraphs to three; removed inline
      document citations (an abstract is conventionally self-contained
      and does not carry bracketed references).

   *  Scope reduced to the core protocol: satellite communication, SS7
      legacy infrastructure, 5G/6G core network ordering, and deep-
      space/SAGIN deployment material are removed from this revision as
      out of scope; see 3GPP and CCSDS/TIPTOP for domain-specific
      profiles.  The former Appendix E (a regulated therapeutic-design
      motivating scenario) is removed as non-normative and out of scope
      for a protocol specification.

   *  Sections 1 through 4 of -06 (Introduction, Use Cases, Requirements
      Language, Problem Statement) are consolidated into a single
      Section 1, removing a duplicated BCP 14 paragraph and shortening
      the document.

   *  The former Section 4.3 (Shannon Gap / SCCP) and Section 7.4 (V*
      equilibrium) are shortened; the full economic and information-
      theoretic derivations remain in the companion paper [POT2026],
      which this document now points to rather than reproduces.

   *  IANA Time Source Type Registry: named operators (NIST, Google,
      Cloudflare, Apple) are replaced with source classes (national
      metrology laboratory, GNSS-disciplined, Roughtime-authenticated,
      NTS-authenticated, PTP grandmaster); the same replacement is
      applied to the worked examples in Sections 1.3, 2.2, and 7.1.
      This document does not depend on, or endorse, any specific named
      operator.

   *  References [NTS], [RFC5705], and [RFC8126] are unchanged from
      -06.

   Changes from -02 through -05 (compressed; see prior revisions of this
   draft for the full itemised changelog): -03 added Use Cases, the SS7/
   SCCP instance analysis, path manipulation scenarios, the trust model,
   and the Implementation Status section (RFC 7942). -04 added the
   Formal Verification Artifacts subsection and the former Appendix E.
   -05 is not separately archived. -06 added Oracle Confidence Gating
   (the G-Score), corrected IPR licensing language per ISE guidance, and
   recorded the provisional "tttps" URI scheme registration.
- **draft-ietf-wimse-http-signature-07** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload-to-Workload Authentication with HTTP Signatures](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document defines one of the mechanisms to provide
   workload authentication, using HTTP Signatures.  While only
   applicable to HTTP traffic, the protocol provides end-to-end
   protection of requests (and optionally, responses), even when service
   traffic is not end-to-end encrypted, that is, when TLS proxies and
   load balancers are used.  Authentication is based on the Workload
   Identity Token (WIT).
- **draft-laurie-tmif-02** (new-draft, score 14, trust_infrastructure) [none]: [A Standard for Claiming Transparency and Falsifiability](https://datatracker.ietf.org/doc/draft-laurie-tmif/) — This document specifies a Transparency Metadata Interchange Format
   (TMIF) that allows a distributed or confidential computing system to
   make standardized, verifiable claims about its levels of transparency
   and falsifiability.  Modeled as a structured Endorsement within the
   Remote Attestation Procedures (RATS) architecture, TMIF provides an
   agnostic, schema-defined communication vehicle for claimants to
   declare how their security mitigations and policy governance controls
   can be independently inspected, reproduced, and verified by third-
   party evaluators.
- **draft-sato-agent-accountability-refarch-00** (new-draft, score 12, adjacent_watchlist) [none]: [AI Audit Reference Architecture for Post-Hoc Agent Accountability](https://datatracker.ietf.org/doc/draft-sato-agent-accountability-refarch/) — This document defines a reference architecture for producing,
   protecting, and verifying post-hoc accountability records for the
   actions of autonomous and semi-autonomous software agents.  It is
   scoped exclusively to post-hoc accountability, as distinct from real-
   time enforcement, and elaborates rather than replaces the role and
   record-type model described in an existing individual submission on
   auditing agent delegation and interactions.  It defines seven ordered
   stages -- intent and mandate capture, the agent boundary, the record
   producer, the event log and its cryptographic anchoring, a composed
   trust fabric, the disclosed audit record, and third-party
   verification -- together with two branch conditions covering cross-
   principal transactions and external resource ingestion.
- **draft-chueayen-attestation-receipts-03** (new-draft, score 11, trust_infrastructure) [none]: [Enforcement Attestation Receipts for AI Inference Decisions](https://datatracker.ietf.org/doc/draft-chueayen-attestation-receipts/) — This document specifies a compact JSON attestation receipt for an AI
   inference decision.  A receipt binds an outcome to a request hash
   under a published Ed25519 public key, so a party that does not trust
   the issuer's infrastructure can still verify offline what the
   issuer's signing key attested was decided.  The format is
   intentionally small and version-selected, so independent verifiers
   stay easy to implement and audit.  It is intended for settings where
   an operator-controlled log is not, on its own, sufficient evidence of
   the decision.
- **draft-correctover-ccs-09** (new-draft, score 11, core_identity) [none]: [Correctover Conformance Shape (CCS): Runtime Verification for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-correctover-ccs/) — This document defines the Correctover Conformance Shape (CCS), a
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
- **draft-crovia-tacet-00** (new-draft, score 11, trust_infrastructure) [none]: [TACET: Verifiable Silence Proofs over a Sparse Merkle Transparency Map, with the PNX Profile for Proof of Non-Exfiltration](https://datatracker.ietf.org/doc/draft-crovia-tacet/) — Existing transparency logs prove presence: a certificate was logged,
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
- **draft-ietf-seat-use-cases-01** (new-draft, score 11, core_identity) [seat]: [Security Goals and Use Cases for Integrating Remote Attestation with Secure Channel Protocols](https://datatracker.ietf.org/doc/draft-ietf-seat-use-cases/) — This document outlines desirable security goals and use cases for
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
- **draft-sabey-succession-receipts-03** (new-draft, score 11, authorization) [none]: [Succession Receipts: Portable Signed Evidence of Authority Succession Between Autonomous Agents](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts/) — Autonomous agents are upgraded, replaced, suspended, and restored
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
- **draft-sergeev-claim-boundaries-00** (new-draft, score 11, trust_infrastructure) [none]: [Claim Boundaries for Execution Evidence](https://datatracker.ietf.org/doc/draft-sergeev-claim-boundaries/) — Systems that act in the world produce logs, receipts, approvals,
   traces, attestations, provenance statements, and transparency
   records.  These artifacts are routinely offered as evidence that an
   action was authorized, performed, or completed.  This document states
   a discipline for bounding such claims: the strength of an execution-
   related claim is limited by what the available evidence actually
   observed and by the control and observation topology at the boundary
   that produced it.  Message formats, signature validity, receipt
   validity, and registration do not create observation or independence
   that did not exist.  The control-topology test was prompted by a
   scenario Stephen Farrell posed in the IETF agent-protocol discussion
   of July 2026: one party creates another and may be able to act in its
   name.  The tension is general, since no message format can supply the
   independent enforcement or observation dependencies required by a
   prevention or adversary-resistant detection-coverage guarantee, and
   the scenario is worked through in an appendix.  The document defines
   no protocol, no record format, and no registry.  It collects non-
   inference rules, a control-topology test for prevention and detection
   claims, a worked example, and reporting distinctions for evidence
   that does not support the claim asserted over it.
- **draft-sirkkavaara-vaara-receipt-11** (new-draft, score 11, trust_infrastructure) [none]: [The Vaara Receipt: A Recomputable Receipt Format for Decisions About Autonomous Actions](https://datatracker.ietf.org/doc/draft-sirkkavaara-vaara-receipt/) — This document specifies vaara.receipt/v1, a signed and independently
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
- **draft-dogru-cedulon-checkpoint-00** (new-draft, score 10, trust_infrastructure) [none]: [Cedulon Checkpoints: Epoch Witnesses and Transparency](https://datatracker.ietf.org/doc/draft-dogru-cedulon-checkpoint/) — This document specifies epoch checkpoints, the transparency witness
   and the anchoring of checkpoints as SCITT Signed Statements for the
   Cedulon audit layer.  The spend receipt, rail-extract reconciliation
   and trust-root rules live in the companion Cedulon Core document.  A
   verifier that pins a witness key can detect a withheld or rolled-back
   checkpoint; without that pin the suppression guarantee is
   conditional.
- **draft-dogru-cedulon-core-00** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
   upon state-of-the-art HTTP 402, AP2 and credit card systems.  We
   specify a cryptographically secured payment reconciliation protocol
   using a Trade Manifest (a signed offer before payment), a Policy
   Decision Point with default deny, a Spend Receipt (a COSE/CWT claim
   set issued after a gated payment), and rail-extract reconciliation.
- **draft-fossati-seat-expat-04** (new-draft, score 9, trust_infrastructure) [none]: [Remote Attestation with Exported Authenticators](https://datatracker.ietf.org/doc/draft-fossati-seat-expat/) — This specification defines a method for two parties in a
   communication interaction to exchange Evidence and Attestation
   Results using exported authenticators, as defined in [RFC9261].
   Additionally, it introduces the cmw_attestation extension, which
   allows attestation credentials to be included directly in the
   Certificate message sent during the Exported Authenticator-based
   post-handshake authentication.  The approach supports both the
   passport and background check models from the RATS architecture while
   ensuring that attestation remains bound to the underlying
   communication channel.
- **draft-ietf-oauth-deferred-token-response-00** (new-draft, score 9, authorization) [oauth]: [Deferred Token Response](https://datatracker.ietf.org/doc/draft-ietf-oauth-deferred-token-response/) — This document defines the Deferred Token Response (DTR) extension for
   OAuth 2.1.  In existing OAuth grants, the token endpoint either
   issues an access token or returns an error.  DTR establishes a
   generic asynchronous token request mechanism that any OAuth grant may
   plug into.  In DTR-aware flows, the authorization server returns a
   deferral_code and a polling interval, indicating that the final token
   response will be available at a later time.  The client retrieves the
   eventual response by polling the token endpoint, or by receiving a
   callback from the authorization server when one is configured.
- **draft-ietf-rats-endorsements-10** (new-draft, score 9, trust_infrastructure) [rats]: [RATS Endorsements](https://datatracker.ietf.org/doc/draft-ietf-rats-endorsements/) — In the IETF Remote Attestation Procedures (RATS) architecture, a
   Verifier accepts Evidence and uses Appraisal Policy for Evidence,
   typically with additional input from Endorsements and Reference
   Values, to generate Attestation Results in formats that are useful
   for Relying Parties.  This document illustrates the purpose and role
   of Endorsements and discusses some considerations in the choice of
   message format for Endorsements in the scope of the RATS
   architecture.

   This document does not aim to define a conceptual message format for
   Endorsements and Reference Values.  Instead, it extends RFC9334 to
   provide further details on Reference Values and Endorsements, as
   these topics were outside the scope of the RATS charter when RFC9334
   was developed.
- **draft-ietf-rats-reference-interaction-models-18** (new-draft, score 9, trust_infrastructure) [rats]: [Reference Interaction Models for Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/) — This document describes interaction models for remote attestation
   procedures (RATS) [RFC9334].  Three conveying mechanisms --
   Challenge/Response, Uni-Directional, and Streaming Remote Attestation
   -- are illustrated and defined.  Analogously, a general overview
   about the information elements typically used by corresponding
   conveyance protocols are highlighted.
- **draft-mih-agent-bilateral-attestation-02** (new-draft, score 9, trust_infrastructure) [none]: [Bilateral Attestation of Cross-Organization Agent Actions](https://datatracker.ietf.org/doc/draft-mih-agent-bilateral-attestation/) — When an agent operated by one organization requests a consequential
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
- **draft-moskowitz-ads-b-auth-04** (new-draft, score 9, core_identity) [none]: [ADS-B Authentication](https://datatracker.ietf.org/doc/draft-moskowitz-ads-b-auth/) — Automatic Dependent Surveillance – Broadcast (ADS-B) is a
   surveillance technology mandated in many airspaces.  It is now widely
   deployed but suffers from a lack of security and privacy.  From a
   security point of view, it is relatively easy to spoof ADS-B messages
   with readily available hardware and software.  From a privacy point
   of view, every ADS-B message contains the aircraft's assigned 24-bit
   ICAO address, a unique identifier that can be cross-referenced with
   external databases (e.g. aircraft registries) to reveal the owner,
   and can be used to track when and where a specific aircraft has
   flown.  In addition, the main transmission medium used for ADS-B, the
   1090 MHz frequency, on which messages are broadcast using the
   Extended Squitter (1090ES) format, is approaching saturation in some
   parts of the world due to the volume of ADS-B and other protocol
   messages, resulting in packet loss in certain areas.

   This paper presents the IETF TESLA protocol along with X.509
   certificates issued by ICAO member states for each aircraft to
   authenticate all ADS-B messaging.  It leverages the 8PSK phase
   overlay (PO) scheme proposed in the Minimum Operational Performance
   Standards (MOPS) for ADS-B (RTCA [DO-260C]), which enables 1090ES
   ADS-B transmissions to convey three times more information, to
   support the transmission of the extra security information required
   by the authentication scheme.  By doing so, the impact of
   authentication on channel usage is negligible.  Beyond message
   authentication, this scheme protocol has two important additional
   benefits: 1) the possibility to implement a Flight Authorization
   scheme, allowing ATC and intercepting aircraft to not only
   authenticate an aircraft but to verify that it is authorizes to
   conduct that flight and 2) a privacy-preserving methodology that
   assigns random 24-bit identifiers to designated aircraft while still
   enabling blind authentication of their ADS-B transmissions.
- **draft-sogomonian-aiip-aiid-00** (new-draft, score 9, core_identity) [none]: [AIIP/AIID: No-Surprise Autonomous Action, Identity, Access Plane, Receipt, and Revocation](https://datatracker.ietf.org/doc/draft-sogomonian-aiip-aiid/) — This document wraps the AIIF model for governing autonomous systems
   in one architecture: AIID (durable principal identity) and AIIP (the
   agents-only access plane).  The primary rule is no surprise:
   autonomous systems MUST NOT act outside their authorized task and
   grant.  Consequential action is carried on AIIP only (Resolve,
   Invoke, signed Receipt of execution).  HTTPS remains the human plane;
   agents MUST NOT use HTTP/HTTPS as their consequential action path
   (this does not forbid TLS or underlay transport).  Controls include
   Monitor freeze, HQ set-active, network-wide freeze, and revocation.
   Companion work already on the Datatracker includes the AIID
   namespace, AIIP architecture, AIIP core, native-access exploration,
   and execution- outcome attestation.  This is regulation by channel,
   not a ban on intelligence.  This document is an individual
   Experimental Internet- Draft; it does not claim Working Group
   adoption or RFC status.
- **draft-efstathiou-samp-agent-management-02** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
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
- **draft-gersch-sidrops-sovereign-roots-00** (new-draft, score 8, authorization) [none]: [Route Origin Authorization via Protected Delegation of Internet Number Resources](https://datatracker.ietf.org/doc/draft-gersch-sidrops-sovereign-roots/) — The Resource Public Key Infrastructure (RPKI) provides cryptographic
   route-origin authorization, but its hierarchical authority model does
   not provide a way for a superior authority to permanently divest
   itself of control over a delegated resource.  Even after delegation,
   superior authority remains part of the authorization hierarchy.  This
   document explores a different property: an address-space holder may
   elect a protected delegation boundary beyond which superior
   authorities can no longer reclaim the resource, suppress the holder's
   effective origin authorizations, or create competing allocation or
   route-origin authority.

   The document specifies a hierarchical IPv4 and IPv6 resource registry
   that enforces this property at the state-transition boundary and
   derives Validated ROA Payloads (VRPs) for conventional Route Origin
   Validation (ROV).  It also defines conflict and precedence rules that
   permit protected resources to coexist with RPKI-derived authority
   while leaving routers and the RPKI itself unchanged.  The mechanism
   can provide origin authorization for resources not currently
   protected by RPKI, including legacy resources, but does not depend on
   such resources remaining outside RPKI.  It is intended for
   experimental deployment alongside RPKI rather than as a replacement
   for RPKI or the Regional Internet Registry system.
- **draft-pinto-cbap-1-00** (new-draft, score 8, authorization) [none]: [Contestability Binding Application Profile 1 (CBAP-1)](https://datatracker.ietf.org/doc/draft-pinto-cbap-1/) — Signed authorization records can show that an action was authorized
   under specified rules, but they do not by themselves establish a
   stable or verifiable path for an Affected Party to contest that
   action.

   This document defines Contestability Binding Application Profile 1
   (CBAP-1), a closed application profile that binds an Authorization
   Artifact to signed contestation terms before execution.  CBAP-1
   specifies deterministic CBOR and COSE encoding, fixed artifact
   formats, executor-verification and execution records, by-value policy
   material, a half-open filing window, a closed structured result, and
   deterministic first-failure reason codes.

   CBAP-1 does not define contestation notices, active execution-state
   effects, network reachability checks, policy-freshness evaluation,
   dispute adjudication, or remedy.  It reports authenticated protocol
   facts and signed claims without asserting forum independence, legal
   validity, physical execution order, or fairness.
- **draft-sankarshan-agent-registry-protocol-00** (new-draft, score 8, core_identity) [none]: [Agent Registry Protocol](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/) — Software agents increasingly act on behalf of people and
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
- **draft-schrock-agent-operation-continuity-00** (new-draft, score 8, core_identity) [none]: [Agent Operation Continuity Across Executor Replacement](https://datatracker.ietf.org/doc/draft-schrock-agent-operation-continuity/) — An agent executor can fail or be replaced after a consequential
   provider request may have crossed an effect boundary but before the
   outcome is known.  Native authorization, succession, evidence-
   boundary, and bounded-capability mechanisms address parts of this
   interval, but they do not by themselves define how a replacement
   executor preserves the same provider operation and its unresolved
   evidence.

   This document defines a composition profile for one authoritative
   coordination domain.  The profile preserves stable operation-
   occurrence identity, immutable provider bindings, authority
   accounting, uncertain evidence, and stale-executor fences across
   replacement.  It defines no new receipt, identity, authority,
   provider, or ledger-migration format, and it does not require any
   particular evidence envelope.
- **draft-toutain-t2trg-coreconf-m2m-01** (new-draft, score 8, agent_identity) [none]: [CORECONF for Machine-to-Machine Communication](https://datatracker.ietf.org/doc/draft-toutain-t2trg-coreconf-m2m/) — The document addresses the specific challenges of M2M interactions
   where both endpoints may be constrained nodes, and explores the use
   of CORECONF primitives.

   This document describes the use of CORECONF (CoAP Management
   Interface) for Machine-to-Machine (M2M) communication in constrained
   IoT environments.  It defines a YANG data model enabling remote
   management and configuration of constrained devices using CoAP, CBOR,
   and YANG SID identifiers.  The serialization in CBOR of this data
   model limits the payload size.  It documents also how the YANG data
   model can interact with common IoT ontologies such as SOSA or SAREF.
   The same CORECONF/SID serialization also enables full
   interoperability between constrained devices and AI agents, by
   exposing device actions and data through an MCP (Model Context
   Protocol) server without requiring an intermediate, device-specific
   translation layer.
- **draft-ahuja-agent-routing-policy-00** (new-draft, score 7, authorization) [none]: [A Policy Grammar for Inter-Domain Agent Routing](https://datatracker.ietf.org/doc/draft-ahuja-agent-routing-policy/) — Agent tasks are delegated across organizational boundaries.  Existing
   work specifies how agents are identified, discovered, and described,
   states requirements for cross-domain isolation and authorization, and
   identifies the absence of a mechanism for expressing capability
   policy as a gap.  This document defines four policy attributes for
   inter-domain agent delegation, the declarations each attribute
   carries, and a validity condition on delegation chains that no party
   establishes by observing the whole chain.  Whether independently
   chosen policies converge is analysed in separate work.
- **draft-son-potus-00** (new-draft, score 7, adjacent_watchlist) [none]: [Presidential Oversight and Trust for Uncontrolled Swarms (POTUS): GIF-Carried Containment](https://datatracker.ietf.org/doc/draft-son-potus/) — This document specifies an experimental binding of a signed
   containment instruction and a Presidential Capability Advertisement
   to a GIF89a image.  An operator can deliver the same object for
   inspection, capability-claim presentation, and machine enforcement.
   The presidential presentation profile uses an operator-selected
   depiction of Donald J.  Trump.  The advertisement carries the
   issuer's declared basis for intervention, with fields for attributed
   numerical strength and intelligence claims.  A receiving enforcement
   point authenticates the issuer and installs a persistent hold on the
   named workload's access to protected resources.

   The specification defines the container, signature profile, anti-
   replay state, delivery interface, enforcement receipts, and recovery
   requirements.  It defines no image-carried release operation.  Its
   protection boundary is the managed resource interface, not the
   recipient model's willingness to obey the image.  The experiment
   concerns authenticated artifact delivery and observable containment,
   not the defensive effect of a portrait.

## Monitor

- **draft-cassandres-hacp-agency-core-00** (new-draft, score 6, trust_infrastructure) [none]: [Human Agency Continuity Protocol (HACP) Core](https://datatracker.ietf.org/doc/draft-cassandres-hacp-agency-core/) — This document specifies the HACP-Core decision contract:
   IntentEnvelope, ProposedAction, AgencyDecision, DecisionToken,
   provenance events, revocation, and the ordered evaluate() algorithm.
   Implementations MUST fail closed.  Decisions MUST be deterministic
   and MUST NOT require a language model on the evaluation path.

   The published executable baseline is the 38-vector HACP-Core v0.9.2
   suite.  Wire object field hacp_version remains "0.9".  Specification
   release 1.0.0 does not change that field.
- **draft-fossati-seat-early-attestation-07** (new-draft, score 6, core_identity) [none]: [Using Attestation in Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://datatracker.ietf.org/doc/draft-fossati-seat-early-attestation/) — The TLS handshake protocol allows authentication of one or both peers
   using static, long-term credentials.  In some cases, it is also
   desirable to ensure that the peer runtime environment is in a secure
   state.  Such an assurance can be achieved using remote attestation
   which is a process by which an entity produces Evidence about itself
   that another party can use to appraise whether that entity is found
   in a secure state.  This document describes a TLS extension that
   enables the negotiation and binding of the TLS authentication key to
   a remote attestation session.  This enables an entity capable of
   producing attestation Evidence, such as a confidential workload
   running in a Trusted Execution Environment (TEE), or an IoT device
   that is trying to authenticate itself to a network access point, to
   present a more comprehensive set of security metrics to its peer.
   This extension has been designed to allow the peers to use any
   attestation technology, in any remote attestation topology, and to
   use them mutually.
- **draft-ietf-lake-pqsuites-01** (new-draft, score 6, core_identity) [lake]: [Quantum-Resistant Cipher Suites for LAKE](https://datatracker.ietf.org/doc/draft-ietf-lake-pqsuites/) — The Lightweight Authenticated Key Exchange (LAKE) protocol, formerly
   known as Ephemeral Diffie-Hellman over COSE (EDHOC), as originally
   specified in RFC 9528, relies on Elliptic Curve Cryptography (ECC)
   for key exchange and authentication.  This document specifies how the
   LAKE protocol operates in a post-quantum setting by defining new
   cipher suites using quantum-resistant algorithms, such as ML-DSA for
   digital signatures and ML-KEM for key exchange.  This document also
   updates RFC 9528 by changing the name of the protocol from EDHOC to
   LAKE and updating the EDHOC Method Types and Cipher Suites registries
   to add columns indicating, respectively, whether a method requires
   and whether a cipher suite supports Diffie-Hellman or Non-Interactive
   Key Exchange (NIKE) primitives.
- **draft-ietf-lamps-rfc6211-update-03** (new-draft, score 6, core_identity) [lamps]: [Update to the Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6211-update/) — This document updates RFC 6211.  It corrects errors in the definition
   of the id-aa-CMSAlgorithmProtect ASN.1 object identifier.  The IANA
   registry entry has always been correct.
- **draft-ietf-mailmaint-oauth-public-06** (new-draft, score 6, authorization) [mailmaint]: [OAuth Profile for Open Public Clients](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-oauth-public/) — This document specifies a profile of the OAuth authorization protocol
   to allow for interoperability between native clients and servers
   using open protocols, such as JMAP, IMAP, SMTP, POP, CalDAV, and
   CardDAV.  The profile is restricted to native clients, that is,
   applications installed and run on the end user's device.  It
   deliberately does not support web-based clients, which cannot
   complete the flow as specified.
- **draft-ietf-tls-trust-anchor-ids-05** (new-draft, score 6, adjacent_watchlist) [tls]: [TLS Trust Anchor Identifiers](https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/) — This document defines the TLS Trust Anchors extension, a mechanism
   for a TLS client or server to select a certificate to present based
   on the peer's trusted certification authorities.  It describes
   certification authorities more succinctly than the TLS Certificate
   Authorities extension.
- **draft-bryce-cose-receipts-mmr-profile-03** (new-draft, score 5, verifiable_claims) [none]: [COSE Receipts for MMRs](https://datatracker.ietf.org/doc/draft-bryce-cose-receipts-mmr-profile/) — This document defines a new verifiable data structure type for COSE
   Receipts [I-D.ietf-cose-merkle-tree-proofs] specifically for use with
   ledgers based on post-order traversal binary Merkle trees and which
   are designed for high throughput, ease of replication and
   compatibility with commodity cloud storage.

   Post-order traversal binary Merkle trees, also known as history
   trees, are more commonly known as Merkle Mountain Ranges.
- **draft-cassandres-hacp-agency-arch-00** (new-draft, score 5, authorization) [none]: [Human Agency Continuity Protocol (HACP) Architecture](https://datatracker.ietf.org/doc/draft-cassandres-hacp-agency-arch/) — This document describes the architecture of the Human Agency
   Continuity Protocol (HACP): a pre-execution authorization contract
   for tool-using agents.  HACP separates human intent, deterministic
   evaluation, cryptographic decision binding, and enforcement so that
   an agent cannot silently reinterpret authorized action after a
   decision is issued.

   This document is Informational.  It is not an Internet Standard.  It
   does not activate Enforcement revision 2 and does not claim general
   URI-normalization conformance.

   The acronym HACP in this series means Human Agency Continuity
   Protocol.  A separately posted individual Internet-Draft, draft-
   sunyi-hacp-protocol, uses the same four letters for a different
   protocol (Hardware Agent Capability Protocol) by a different author.
   The present author has no affiliation with that document.
- **draft-cmcc-tcp-sro-02** (new-draft, score 5, core_identity) [none]: [The Session Recovery (SR) Option for TCP](https://datatracker.ietf.org/doc/draft-cmcc-tcp-sro/) — This document defines the Session Recovery (SR) option for TCP.  The
   option lets the endpoints of a connection exchange identifiers:
   during the handshake each endpoint carries its own identifier, and
   designated segments afterwards carry the identifier of the peer.
   This places the knowledge of which endpoint a connection belongs to
   inside the TCP header, where network functions on the path - load
   balancers, NAT gateways, firewalls - can read it without per-flow
   state and without payload inspection.  The primary use is session
   recovery in SNAT and load-balancing clusters; further uses include
   reduced-state forwarding, connection-tracking recovery, and per-
   backend telemetry.  The option is carried in the SYN, the SYN-ACK,
   and retransmitted segments, or in every segment when so configured;
   the default adds no overhead to normal data segments.  Endpoints that
   do not support it behave as if the option did not exist.
- **draft-intra-handshake-fail-36** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Harmful (CVE-2026-92701 of CVSS 9.1, CVE-2026-92702 of CVSS 9.1, CVE-2026-33697 of CVSS 7.5, and 37 other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-33697],
   [EUVD-2026-16488], [CVE-2026-92701], [EUVD-2026-83194],
   [CVE-2026-92702], [EUVD-2026-83192] and several GitHub Security
   Advisories (GHSAs) which provide substantial technical evidence of
   how early attestation fails in practice, even *without physical
   access* to the desired machine.  Moreover, since continuous
   attestation is generally required [CSA-eBPF]
   [MITRE-Continuous-Attestation], early attestation adds *unnecessary
   complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art formal analysis tool,
   ProVerif, under Apache-2.0 license for reproducibility,
   extensibility, and review, and have been acknowledged by the relevant
   stakeholders.  Currently, there are *two CVEs of CVSS 9.1, one CVE of
   CVSS 7.5, one GHSA of 9.0-10.0, one GHSA of CVSS 7.8, seven GHSAs of
   CVSS 7.4, and one GHSA of CVSS 6.3 published against the broader
   early attestation covering all layers of the ecosystem up to the
   application*. The research papers on these are currently either under
   submission or being prepared for submission.  The artifacts of these
   papers will be shared with the community under Apache-2.0 license for
   reproducibility, extensibility, and review.  In our analysis, the
   remaining implementations of early attestation -- Edgeless Systems
   Contrast and Meta's AI -- remain vulnerable.
- **draft-li-iqa-subject-attestation-00** (new-draft, score 5, trust_infrastructure) [none]: [Subject Attestation in the iqa URI Scheme](https://datatracker.ietf.org/doc/draft-li-iqa-subject-attestation/) — This document specifies the "iqa" URI scheme, a subject-attestation
   scheme in which an "iqa" URI names the attestation standing of an
   identified subject, as reported by one of three named authority
   organs; the URI carries no proof and no credential, and no lookup
   service or name-resolution system is consulted when the URI is used.
   The document also states the requirements a client MUST satisfy when
   it handles such a URI, in order to avoid two failure modes that
   short, user-embeddable strings otherwise invite: using the authority
   as a navigation target (open redirect), and using a registered
   protocol handler as a general-purpose launcher.  A third failure mode
   specific to this scheme is addressed as well: a parse that looks like
   a certification.

## Adjacent / watchlist

- **draft-carpenter-anima-otp-casa-02** (new-draft, score 3, core_identity) [none]: [One-time Pad for Authorizing Device Identity](https://datatracker.ietf.org/doc/draft-carpenter-anima-otp-casa/) — This document describes how devices joining an autonomic control
   plane as defined in RFC 8994 may use the BRSKI onboarding mechanism
   defined in RFC 8995, even if they cannot provide a manufacturer-
   installed X.509 IDevID certificate.  Instead, such devices may
   generate a self-signed certificate embedding a unique token selected
   from a one-time pad.
- **draft-geng-sidrops-regionalized-roa-00** (new-draft, score 3, adjacent_watchlist) [none]: [AS Hijacking Detection and Mitigation in the Presence of Regionalized ROAs](https://datatracker.ietf.org/doc/draft-geng-sidrops-regionalized-roa/) — Resource Public Key Infrastructure (RPKI) Route Origin Validation
   (ROV) verifies whether an Autonomous System (AS) is authorized to
   originate a given IP prefix.  However, multi-national or
   geographically dispersed ASes often hold IP prefix allocations from
   different Regional Internet Registries (RIRs) or announce specific
   prefixes only within designated geographic regions under a single
   Origin AS.  An attacker located in a different region can maliciously
   announce an authorized prefix under the same legitimate Origin AS,
   effortlessly bypassing standard RPKI ROV.  This document defines the
   concept of "Regionalized ROA" (R-ROA), specifies protocol
   enhancements to convey regional scope metadata from Trust Anchors
   down to routers via RPKI-Router protocol extensions, and outlines
   enhanced validation procedures to detect and mitigate intra-AS cross-
   regional route hijacking.
- **draft-greicodex-fidex-protocol-01** (new-draft, score 3, verifiable_claims) [none]: [FideX Application Statement 5 (AS5) Protocol](https://datatracker.ietf.org/doc/draft-greicodex-fidex-protocol/) — This document specifies the FideX Protocol (AS5), a modern
   application-layer protocol for secure Business-to-Business (B2B)
   message exchange.  FideX provides cryptographic non-repudiation, data
   integrity, and confidentiality using JOSE (JSON Object Signing and
   Encryption) over HTTPS, replacing legacy AS2 and AS4 standards with a
   REST-oriented approach accessible to modern web developers.

   FideX adopts the "AS" naming lineage: AS2 ([RFC4130]) used S/MIME
   over HTTP; AS4 ([OASIS-ebMS]) used SOAP/WS-Security; AS5 (FideX) uses
   REST/JSON/JOSE over HTTPS.  This document defines the message format,
   cryptographic operations, partner discovery, state management,
   acknowledgment receipts (J-MDN), and error handling.
- **draft-gueron-cfrg-dndkgcm-05** (new-draft, score 3, core_identity) [none]: [Double Nonce Derive Key AES-GCM (DNDK-GCM)](https://datatracker.ietf.org/doc/draft-gueron-cfrg-dndkgcm/) — This document specifies an authenticated encryption algorithm called
   Double Nonce Derive Key AES-GCM (DNDK-GCM). It operates with a 32-
   byte root key and is designed to encrypt with a 24-byte random nonce
   and optionally to provide for key commitment.

   Encryption takes the root key and a 15-byte portion of the random
   nonce, and derives a fresh 32-byte encryption key and (optionally) a
   key commitment value. Then, it invokes AES-GCM with the derived key
   and the remaining bytes of the nonce, and outputs the ciphertext,
   authentication tag and the key commitment value.

   Although this is not the primary use case, it is also possible to use
   DNDK-GCM with a non-repeating but non-random nonce (i.e., a "counter-
   based nonce").

   The low collision probability in a collection of 24-byte random
   nonces and the per-nonce derivation of an encryption key extend the
   lifetime of the root key, and the scheme can support processing up to
   2^64 bytes under a given root key.

   DNDK-GCM introduces a relatively small overhead compared to using
   AES-GCM directly, and its security relies only on the standard
   assumption that AES acts as a pseudorandom permutation.
- **draft-helmprotocol-deepspace-00** (new-draft, score 3, trust_infrastructure) [none]: [TTTPS Deep-space Profile: Propagation-Aware Time Attestation](https://datatracker.ietf.org/doc/draft-helmprotocol-deepspace/) — This document defines an experimental deep-space profile for the TLS
   TimeToken Secure Protocol (TTTPS).  The profile preserves the Proof-
   of-Time record and cryptographic verification boundary while adding
   propagation-aware context for long and intermittent links.  It
   specifies one-way-light-time handling, epoch- and frame-bound
   physical context, relative coordinate-time conversion, peer
   projection, conservative aggregation, and explicit HOLD and
   UNVERIFIABLE outcomes.  It does not claim flight measurements, a live
   interplanetary mesh, or a replacement for CCSDS, DTN, or navigation
   standards.
- **draft-ietf-asdf-digital-twin-05** (new-draft, score 3, adjacent_watchlist) [asdf]: [Semantic Definition Format (SDF) Modeling for Digital Twin](https://datatracker.ietf.org/doc/draft-ietf-asdf-digital-twin/) — This memo specifies SDF modeling for digital twins, i.e., digital
   twin systems, and their things.  An SDF is a format that is used to
   create and maintain data and interaction, and to represent the
   various kinds of data that is exchanged for these interactions.  The
   SDF format can be used to model the characteristics, behavior and
   interactions of things, i.e. physical objects, in digital twins that
   contain things as components.
- **draft-ietf-asdf-nipc-22** (new-draft, score 3, adjacent_watchlist) [asdf]: [An Application Layer Interface for Non-Internet-connected Physical Components (NIPC)](https://datatracker.ietf.org/doc/draft-ietf-asdf-nipc/) — This document describes an API that allows applications to perform
   operations against a gateway serving one or more devices described by
   an SDF model.  The API consists of a RESTful application layer
   interface that performs operations on those devices, as well as a
   CBOR-based publish-subscribe interface for streaming data.
- **draft-ietf-asdf-sdf-protocol-mapping-12** (new-draft, score 3, adjacent_watchlist) [asdf]: [SDF Protocol Mapping](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-protocol-mapping/) — This document defines protocol mapping extensions for the Semantic
   Definition Format (SDF) to enable mapping of protocol-agnostic SDF
   affordances to protocol-specific operations.  The protocol mapping
   mechanism allows SDF models to specify how properties, actions, and
   events should be accessed using a specific protocol.  This document
   defines protocol mappings for Bluetooth Low Energy and Zigbee, and
   the mechanism can be extended to other protocols such as HTTP and
   CoAP.  This document also describes a method to extend SCIM with an
   SDF model mapping.
- **draft-ietf-calext-jscalendarbis-20** (new-draft, score 3, adjacent_watchlist) [calext]: [JSCalendar 2.0: A JSON Representation of Calendar Data](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendarbis/) — This specification defines version "2.0" of JSCalendar, a data model
   and JSON representation of calendar data that can be used for storage
   and data exchange in a calendaring and scheduling environment.  This
   document obsoletes RFC 8984, also referred to as version "1.0" in
   this document.  The newly defined version "2.0" aims to improve
   interoperability with existing iCalendar-based systems.  It also
   aligns its definitions with JSContact, such as the IANA registry
   policy, validation requirements, and versioning scheme.
- **draft-ietf-ccamp-layer1-types-20** (new-draft, score 3, adjacent_watchlist) [ccamp]: [Common YANG Data Types for Layer 1 Networks](https://datatracker.ietf.org/doc/draft-ietf-ccamp-layer1-types/) — This document defines a collection of common data types, identities,
   and groupings in the YANG data modeling language.  These derived
   common data types, identities, and groupings are intended to be
   imported by modules that model Layer 1 configuration and state
   capabilities.  The Layer 1 types are representative of Layer 1 client
   signals applicable to transport networks, such as Optical Transport
   Networks (OTN).  The Optical Transport Network (OTN) data structures
   are included in this document as Layer 1 types.
- **draft-ietf-ediint-rfc4130bis-03** (new-draft, score 3, core_identity) [ediint]: [AS2 Specification Modernization](https://datatracker.ietf.org/doc/draft-ietf-ediint-rfc4130bis/) — This document provides an applicability statement (RFC 2026,
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
- **draft-ietf-httpbis-connect-tcp-14** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP proxying using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this proxying functionality has several
   important deficiencies in modern HTTP environments.  This
   specification defines an alternative HTTP proxy service configuration
   for TCP connections.  This configuration is described by a URI
   Template, similar to the CONNECT-UDP and CONNECT-IP protocols.
- **draft-ietf-idr-flowspec-srv6-10** (new-draft, score 3, core_identity) [idr]: [BGP Flow Specification for SRv6](https://datatracker.ietf.org/doc/draft-ietf-idr-flowspec-srv6/) — This document specifies extensions to BGP Flow Specification (BGP-FS)
   to enable filtering of IPv6 packets based on the structural
   components of an SRv6 Segment Identifier (SID) present in the IPv6
   Destination Address (representing the active segment of an SRv6
   path).
- **draft-ietf-idr-sdwan-edge-discovery-31** (new-draft, score 3, core_identity) [idr]: [SD-WAN Edge and Underlay Tunnel Discovery Using BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-sdwan-edge-discovery/) — This document specifies BGP mechanisms for SD-WAN (Software-Defined
   Wide Area Network) edge node attribute discovery.  These mechanisms
   comprise a new tunnel type and associated Sub-TLVs for the BGP Tunnel
   Encapsulation Attribute, and a new Subsequent Address Family
   Identifier (SAFI) carrying a typed NLRI for advertising SD-WAN
   underlay tunnel information.
- **draft-ietf-ivy-network-inventory-yang-19** (new-draft, score 3, adjacent_watchlist) [ivy]: [A Base YANG Data Model for Network Inventory](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-yang/) — This document defines a base YANG data model for reporting network
   inventory.  The scope of this base model is set to be application-
   and technology-agnostic.  The base data model can be augmented with
   application- and technology-specific details.
- **draft-ietf-jmap-calendars-29** (new-draft, score 3, adjacent_watchlist) [jmap]: [JSON Meta Application Protocol (JMAP) for Calendars](https://datatracker.ietf.org/doc/draft-ietf-jmap-calendars/) — This document specifies a data model for synchronizing calendar data
   with a server using JMAP.  Clients can use this to efficiently read,
   write, and share calendars and events, receive push notifications for
   changes or event reminders, and keep track of changes made by others
   in a multi-user environment.
- **draft-ietf-lamps-cms-composite-kem-03** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-kem/) — Composite ML-KEM defines combinations of Module-Lattice-based Key
   Encapsulation Mechanism (ML-KEM) with RSA-OAEP, ECDH, X25519, and
   X448.  This document specifies the conventions for using Composite
   ML-KEM algorithms with the Cryptographic Message Syntax (CMS) using
   the KEMRecipientInfo structure defined in “Using Key Encapsulation
   Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)”
   (RFC 9629).
- **draft-ietf-lamps-cms-euf-cma-signeddata-03** (new-draft, score 3, adjacent_watchlist) [lamps]: [Best Practices for Signed Attributes in CMS SignedData](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-euf-cma-signeddata/) — The Cryptographic Message Syntax (CMS) has different signature
   verification behaviour based on whether signed attributes are present
   or not.  This results in a potential existential forgery
   vulnerability in CMS and protocols which use CMS.  This document
   describes the vulnerability and lists mitigations and best practices
   to avoid it.  This document updates RFC 5652 by prohibiting the use
   of the id-data content type for new uses of the CMS SignedData type.
- **draft-ietf-netconf-notif-envelope-06** (new-draft, score 3, adjacent_watchlist) [netconf]: [Extensible YANG Model for YANG-Push Notifications](https://datatracker.ietf.org/doc/draft-ietf-netconf-notif-envelope/) — This document defines a new extensible Notification structure,
   defined in YANG, for use in YANG-Push Notification messages, both for
   NETCONF and RESTCONF, enabling any YANG-compatible encodings such as
   XML, JSON, or CBOR.  Additionally, it defines two essential
   extensions to this structure, the support of a hostname and a
   sequence number and the support of a timestamp characterizing the
   moment when the data was observed.
- **draft-ietf-nfsv4-acls-update-05** (new-draft, score 3, authorization) [nfsv4]: [ACLs within the NFSv4 Protocols](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-acls-update/) — This document is part of the set of documents intended to update the
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
- **draft-ietf-nmop-network-incident-yang-15** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG data model for the network incident
   lifecycle management.  This YANG module provides a standard way to
   report, diagnose, and help reduce troubleshooting tickets and resolve
   network incidents for the sake of network service health and probable
   root cause analysis.
- **draft-ietf-openpgp-persistent-symmetric-keys-04** (new-draft, score 3, core_identity) [openpgp]: [Persistent Symmetric Keys in OpenPGP](https://datatracker.ietf.org/doc/draft-ietf-openpgp-persistent-symmetric-keys/) — This document defines a new packet and algorithm for the OpenPGP
   standard (RFC 9580) to support persistent symmetric keys, for message
   encryption using authenticated encryption with additional data (AEAD)
   and for message authentication using AEAD authentication tags.  This
   enables the use of symmetric cryptography for data storage (and other
   contexts that do not require asymmetric cryptography), for improved
   performance, smaller keys, and improved resistance to quantum
   computing.
- **draft-ietf-opsawg-scheduling-oam-tests-09** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A YANG Data Model for Network Diagnosis using Scheduled Sequences of OAM Tests](https://datatracker.ietf.org/doc/draft-ietf-opsawg-scheduling-oam-tests/) — This document defines two YANG data models to support scheduled
   network diagnosis using Operations, Administration, and Maintenance
   (OAM) tests.  This document defines both 'oam-unitary-test' and 'oam-
   test-sequence' YANG modules to manage the lifecycle of network
   diagnosis procedures, intended for use by external management and
   orchestration systems (including SDN controllers and network
   orchestrators), rather than by individual network nodes.
- **draft-ietf-satp-architecture-10** (new-draft, score 3, adjacent_watchlist) [satp]: [Secure Asset Transfer (SAT) Interoperability Architecture](https://datatracker.ietf.org/doc/draft-ietf-satp-architecture/) — This document proposes an interoperability architecture for the
   secure transfer of assets between two networks or systems based on
   the gateway model.
- **draft-ietf-sidrops-constraining-rpki-trust-anchors-02** (new-draft, score 3, adjacent_watchlist) [sidrops]: [Constraining RPKI Trust Anchors](https://datatracker.ietf.org/doc/draft-ietf-sidrops-constraining-rpki-trust-anchors/) — This document describes an approach for Resource Public Key
   Infrastructure (RPKI) Relying Parties (RPs) to impose locally
   configured Constraints on cryptographic products subordinate to Trust
   Anchors (TAs).  The ability to constrain a Trust Anchor operator's
   effective signing authority to a limited set of Internet Number
   Resources (INRs) allows Relying Parties to enjoy the potential
   benefits of assuming trust - within a bounded scope.  The specified
   approach and configuration format allow RPKI operators to communicate
   efficiently about observations related to Trust Anchor operations.
- **draft-ietf-tls-mlkem-11** (new-draft, score 3, adjacent_watchlist) [tls]: [ML-KEM Post-Quantum Key Agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) — This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as
   NamedGroups and registers IANA values in the TLS Supported Groups
   registry for use in TLS 1.3 to achieve post-quantum (PQ) key
   establishment.
- **draft-liao-cose-c509-additions-00** (new-draft, score 3, core_identity) [none]: [Additions to C509 Structures](https://datatracker.ietf.org/doc/draft-liao-cose-c509-additions/) — This document defines additions to CBOR Encoded X.509 Certificates
   (C509).

   This document defines a new C509SubjectPublicKeyInfo type, a CBOR
   representation of the X.509 SubjectDirectoryAttributes extension, and
   a mechanism that allows organizations assigned a Private Enterprise
   Number (PEN) to define organization-specific integer identifiers
   without registering each identifier in the C509 RDN attribute type,
   CR attribute type, extension ID, certificate policy, or extended key
   usage registries.

   This document also defines textual encoding labels for C509 objects
   using the textual encoding conventions specified in RFC 7468.
- **draft-liu-add-ppp-edns-negotiation-03** (new-draft, score 3, core_identity) [none]: [PPP IPCP Extensions for Encrypted DNS Server Negotiation](https://datatracker.ietf.org/doc/draft-liu-add-ppp-edns-negotiation/) — This document defines extensions to the Point-to-Point Protocol (PPP)
   Internet Protocol Control Protocol (IPCP) for negotiating encrypted
   DNS resolver configurations.  Two IPCP Configuration Options are
   defined for primary and secondary encrypted DNS resolvers.  Each
   option carries an Authentication Domain Name (ADN), an explicit list
   of resolver IP addresses, and Service Parameters (SvcParams) using
   the wire format defined by RFC 9460.  The design supports DNS over
   TLS (DoT), DNS over HTTPS (DoH), and DNS over QUIC (DoQ), while
   maintaining coexistence with the plaintext DNS configuration
   mechanism defined by RFC 1877.
- **draft-rich-radext-wlan-security-profile-01** (new-draft, score 3, core_identity) [none]: [RADIUS Attribute for IEEE 802.11 WLAN Security Profiles](https://datatracker.ietf.org/doc/draft-rich-radext-wlan-security-profile/) — IEEE 802.11, as amended, defines security profiles, and several of
   those profiles can share the same AKM suite and pairwise cipher, so
   WLAN-AKM-Suite and WLAN-Pairwise-Cipher no longer tell a RADIUS
   server which profile is in effect.

   This document defines the WLAN-Security-Profile RADIUS attribute,
   which reports the security profile the responder accepted.  A Network
   Access Server includes it in the Access-Requests it generates for an
   IEEE 802.1X authentication so the server can make policy decisions
   based on the value.  The attribute complements the IEEE 802
   attributes defined in RFC 7268.
- **draft-vitap-ml-dsa-webauthn-05** (new-draft, score 3, core_identity) [none]: [ML-DSA for Web Authentication](https://datatracker.ietf.org/doc/draft-vitap-ml-dsa-webauthn/) — This document describes implementation of Passwordless authentication
   in Web Authentication (WebAuthn) using Module-Lattice-Based Digital
   Signature Standard (ML-DSA), a Post-Quantum Cryptography (PQC)
   digital signature scheme defined in FIPS 204.
- **draft-xie-qosformer-qos-assurance-00** (new-draft, score 3, adjacent_watchlist) [none]: [QoSformer: A Framework for Learning-Based QoS Prediction and Policy Evaluation](https://datatracker.ietf.org/doc/draft-xie-qosformer-qos-assurance/) — Network operators need to assess how changes to quality-of-service
   (QoS) policies may affect individual traffic flows and shared network
   resources.  Measurements describe observed behavior, but policy
   evaluation also requires predictions under candidate configurations.
   This document describes a framework that combines heterogeneous
   network measurements and configuration data in a Multiple Flow
   Snapshot (MFS), learns representations through masked reconstruction,
   and uses a Transformer-based model called QoSformer to predict
   throughput, delay, and resource utilization.  It describes offline
   model preparation, online candidate evaluation, and feedback after
   authorized policy changes.  A 5G core network use case illustrates
   the mapping to analytics and policy-control functions.  The framework
   is informational: it defines neither a new wire protocol nor
   extensions to existing 3GPP interfaces.
- **draft-zhangb-cats-service-metrics-op-05** (new-draft, score 3, adjacent_watchlist) [none]: [Computing Service Metrics Operation and Joint Service Selection under CATS](https://datatracker.ietf.org/doc/draft-zhangb-cats-service-metrics-op/) — Computing-Aware Traffic Steering (CATS) optimizes traffic forwarding
   by considering both computing and networking metrics.  The CATS
   framework and metric-definition documents provide valuable
   theoretical models, yet they face challenges in achieving direct
   operational execution in real-world deployments: normalization
   methods vary across providers, and aggregated unitless scores often
   lose the operational information that routers need for precise
   steering decisions.

   This document provides a self-contained, executable operational model
   for a core class of CATS deployment scenarios: latency-sensitive,
   compute-intensive services whose steering decisions are made in real
   time at the forwarding node.  Instead of disseminating low-level raw
   hardware metrics, service sites dynamically evaluate and report
   service-oriented metrics (e.g., Global Available Slots and Computing
   Time) to the control plane.  The document clarifies how these metrics
   are derived from basic resource information, service reference
   information, and local policy.  It also specifies how the CATS Path
   Selector (C-PS) combines the Computing Service Table (populated from
   C-SMA reports) with the Network Service Table to make joint traffic-
   steering decisions, and defines update-control and fallback
   mechanisms suitable for large-scale deployments.

   Within the unified CATS architecture, the service-oriented
   operational model defined in this document coexists with the general-
   purpose L1/L2 normalized metric framework: a deployment MAY use
   either model, or run both pipelines in parallel for different service
   classes, without embedding metric fields across frameworks.  This
   document does not negate the value of normalized metrics; it focuses
   on the service-level abstractions and runtime operations required for
   direct traffic steering.
- **draft-zheng-ccamp-client-pm-yang-16** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Client Signal Performance Monitoring](https://datatracker.ietf.org/doc/draft-zheng-ccamp-client-pm-yang/) — A transport network is a server-layer network to provide connectivity
   services to its client.  Given the client signal is configured, the
   followup function for performance monitoring, such as latency and bit
   error rate, would be needed for network operation.

   This document describes the data model to support the performance
   monitoring functionalities.
- **draft-bernardos-cats-anchoring-aiml-selection-01** (new-draft, score 2, ignored_after_review) [none]: [AI/ML-Enabled Computing Aware Traffic Steering using IP address anchoring](https://datatracker.ietf.org/doc/draft-bernardos-cats-anchoring-aiml-selection/) — The IETF CATS WG addresses the problem of how the network
   infrastructure can steer traffic between clients of a service and
   sites offering the service, considering both network metrics (such as
   bandwidth and latency), and compute metrics (such as processing,
   storage capabilities, and capacity).

   This document describes solutions to enable the network to select the
   best site to instantiate a processing service (using distributed
   sensing as an application example), augmenting CATS enabled solutions
   that consider both connectivity and computing, to also consider AI/ML
   and data capabilities and governance policies.
- **draft-bernardos-nmrg-agentic-network-optimization-01** (new-draft, score 2, agent_identity) [none]: [Solutions for enabling agentic sensing with network optimization](https://datatracker.ietf.org/doc/draft-bernardos-nmrg-agentic-network-optimization/) — Integrated Sensing and Communications (ISAC) represents a paradigm
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
- **draft-effortel-pulse-00** (new-draft, score 2, ignored_after_review) [none]: [Pulse: Real-Time Online Charging for AI Services](https://datatracker.ietf.org/doc/draft-effortel-pulse/) — This document specifies Pulse, version 1.1 — the AI online charging
   protocol: the interface between an AI Gateway (the client) and the
   Charging Server (the server) by which AI service usage is authorised
   in real time, supervised under a granted budget, and settled.  The
   spend guarantee is precisely stated: *settled spend never exceeds the
   reported meter or the plan's ceiling*, and serving exposure is
   bounded by the granted pool plus the completion of Calls already in
   flight when a stop lands.  The protocol consists of two request/
   response operations over HTTPS with JSON bodies: *Authorise* and
   *Report*. It follows the reserve-then-settle discipline of telecom
   online charging (cf. Diameter Credit-Control, RFC 4006) applied to AI
   workloads.
- **draft-ietf-aipref-vocab-08** (new-draft, score 2, ignored_after_review) [aipref]: [A Vocabulary For Expressing AI Usage Preferences](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/) — This document defines a vocabulary for expressing preferences
   regarding how digital assets are used by automated processing
   systems.  This vocabulary allows for the declaration of restrictions
   or permissions for use of digital assets by such systems.
- **draft-ietf-dnsop-delext-11** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895 and 9824.
- **draft-sweetser-bcp-rpki-ca-02** (new-draft, score 2, ignored_after_review) [none]: [Operational Guidelines for RPKI Delegated Certification Authorities](https://datatracker.ietf.org/doc/draft-sweetser-bcp-rpki-ca/) — This document provides operational guidelines for Resource Public Key
   Infrastructure (RPKI) delegated Certification Authorities (CAs) and
   registry operators managing such delegations.  It addresses common
   operational issues including CA availability problems, publication
   quality issues, and lifecycle management.  The guidelines aim to
   improve the overall health and efficiency of the RPKI ecosystem by
   establishing best practices for CA operations and delegation
   management.
- **draft-yao-dawn-agent-discovery-architect-01** (new-draft, score 2, ignored_after_review) [none]: [DNS-like Agent Discovery Architecture](https://datatracker.ietf.org/doc/draft-yao-dawn-agent-discovery-architect/) — This document defines a DNS-like three-tier agent-discovery
   architecture for the Internet of Agents (IoA).  It introduces three
   core functional roles: Agent Root, Agent Registry, and Agent
   Resolver.
- **draft-ye-problems-and-requirements-of-dns-for-ioa-03** (new-draft, score 2, ignored_after_review) [none]: [Problems Statement and Requirements Analysis of DNS for Internet of Agents (IoA)](https://datatracker.ietf.org/doc/draft-ye-problems-and-requirements-of-dns-for-ioa/) — In the AI-driven era, DNS is supposed to evolve with technological
   advancements to accommodate the complex and diverse requirements of
   the IoA.  This draft analyzes the issues surrounding DNS in
   supporting agents collaboration and explores corresponding technical
   requirements.
- **draft-zhang-aiproto-svcb-mapping-for-agents-02** (new-draft, score 2, ignored_after_review) [none]: [Service Binding Mapping for Agents](https://datatracker.ietf.org/doc/draft-zhang-aiproto-svcb-mapping-for-agents/) — With the continuous introduction of intelligent agent communication
   and interaction protocols, the current DNS cannot adequately meet the
   requirements for agent service resolution.  This document defines a
   new DNS resource record type, AGENT, which is a SVCB-compatible RR
   type, and specifies the mapping specifications.
- **draft-zhangb-cats-sci-implementation-01** (new-draft, score 2, ignored_after_review) [none]: [CATS Service Contact Instance Functional Implementation](https://datatracker.ietf.org/doc/draft-zhangb-cats-sci-implementation/) — The Computing-Aware Traffic Steering (CATS) framework
   [I-D.ietf-cats-framework] introduces the concept of a Service Contact
   Instance (SCI) as the client-facing entity responsible for receiving
   and dispatching service requests.  While the framework and the CATS
   metric documents define the components and the metrics, the concrete
   observable behavior of a Service Contact Instance - in particular,
   what it reports to the CATS Service Metric Agent (C-SMA), when it
   reports, and how service-instance health changes are reflected in the
   reported metrics - remains underspecified.

   This document fills that gap.  It specifies the functional behavior
   of a CATS Service Contact Instance in terms of observable behavior
   and reporting semantics: how an SCI aggregates instance-level
   information into service-oriented metrics (e.g., Global Available
   Slots and Computing Time) as defined in
   [I-D.zhangb-cats-service-metrics-op]; how it monitors the health and
   status of underlying service instances and adjusts reported metrics
   accordingly; how it maintains affinity and handles failure scenarios;
   and how it reports metrics and status updates to the C-SMA, including
   update policies and threshold-based triggers.  A decomposition of the
   SCI into internal functional components is provided as illustrative
   implementation guidance, not as a mandated software architecture.

   This document complements [I-D.ietf-cats-framework],
   [I-D.ietf-cats-metric-definition-11], and
   [I-D.zhangb-cats-service-metrics-op] by providing the operational
   execution layer for the SCI within the unified CATS architecture.
- **draft-ietf-6man-sub-link-scope-multicast-01** (new-draft, score 1, authorization) [6man]: [Sub-Link Scoped IPv6 Multicast Addressing](https://datatracker.ietf.org/doc/draft-ietf-6man-sub-link-scope-multicast/) — The IPv6 addressing architecture for multicast has the scope of a
   multicast group embedded in its address, with the smallest non-
   reserved scopes being interface-local and link-local, numbered 1 and
   2.  This document suggests the introduction of a scope inbetween
   these two, for use with lower-layer transport multicast that reaches
   parts of a link.  Since there is no room to insert a scope value for
   this, a separate address block is used.  A mapping for Ethernet as
   lower-layer transport is provided.
- **draft-mk-dnsop-svcb-well-known-00** (new-draft, score 1, verifiable_claims) [none]: [An SVCB Service Parameter for Well-Known URI Paths](https://datatracker.ietf.org/doc/draft-mk-dnsop-svcb-well-known/) — This document defines the "well-known" Service Parameter Key
   (SvcParamKey) for SVCB and HTTPS resource records.  It carries one or
   more well-known URI suffixes, identifying resources under "/.well-
   known/" that are available at the service endpoint.  It specifies the
   presentation and wire formats and requests registration of the key
   with IANA.

## Ignored after review

- **draft-augustyn-intarea-ipref-08** (new-draft, score 0, ignored_after_review) [none]: [IP Addressing with References (IPREF)](https://datatracker.ietf.org/doc/draft-augustyn-intarea-ipref/) — IP addressing with references, or IPREF for short, is a method for
   end-to-end communication across different address spaces normally not
   reachable through native means.  IPREF uses references to addresses
   instead of real addresses.  It allows to reach across NAT/NAT6 and
   across protocols IPv4/IPv6.  It is a pure layer 3 addressing feature
   that works with existing network protocols.

   IPREF forms addresses (IPREF addresses) made of context addresses and
   references.  These IPREF addresses are publishable in Domain Name
   System (DNS).  Any host in any address space, including behind NAT/
   NAT6 or employing different protocol IPv4/IPv6, may publish IPREF
   addresses of its services in DNS.  These services will be reachable
   from any address space, including those running different protocol
   IPv4/IPv6 or behind NAT/NAT6, provided both ends support IPREF.

   IPREF provides much needed IPv4/IPv6 compatibility for the de facto
   mixed protocol Internet.
- **draft-bernardos-cats-anchoring-service-mobility-05** (new-draft, score 0, ignored_after_review) [none]: [Service Mobility-Enabled Computing Aware Traffic Steering using IP address anchoring](https://datatracker.ietf.org/doc/draft-bernardos-cats-anchoring-service-mobility/) — The IETF CATS WG addresses the problem of how the network
   infrastructure can steer traffic between clients of a service and
   sites offering the service, considering both network metrics (such as
   bandwidth and latency), and compute metrics (such as processing,
   storage capabilities, and capacity).

   This document defines new extensions and procedures for a terminal
   connected to a network infrastructure, to benefit from transparent
   service migration adapting to specific connectivity and computing
   requirements, so traffic is always steered to an instance meeting
   both requirements.  Both CATS-aware and -unaware terminals are
   considered.  Exemplary signaling control messages and operation
   extending the well-known Proxy Mobile IPv6 protocol are also defined.
- **draft-bernardos-cats-anchoring-terminal-mobility-02** (new-draft, score 0, ignored_after_review) [none]: [Terminal Mobility-Enabled Computing Aware Traffic Steering using IP address anchoring](https://datatracker.ietf.org/doc/draft-bernardos-cats-anchoring-terminal-mobility/) — The IETF CATS WG addresses the problem of how the network
   infrastructure can steer traffic between clients of a service and
   sites offering the service, considering both network metrics (such as
   bandwidth and latency), and compute metrics (such as processing,
   storage capabilities, and capacity).

   This document defines new extensions and procedures for a terminal
   connected to a network infrastructure, to benefit from transparent
   mobility management adapting to specific connectivity and computing
   requirements, so traffic is always steered to an instance meeting
   both requirements.  Both CATS-aware and -unaware terminals are
   considered.
- **draft-bernardos-cats-ip-address-anchoring-05** (new-draft, score 0, ignored_after_review) [none]: [Computing Aware Traffic Steering using IP address anchoring](https://datatracker.ietf.org/doc/draft-bernardos-cats-ip-address-anchoring/) — The IETF CATS WG addresses the problem of how the network
   infrastructure can steer traffic between clients of a service and
   sites offering the service, considering both network metrics (such as
   bandwidth and latency), and compute metrics (such as processing,
   storage capabilities, and capacity).

   This document defines new extensions for a terminal connected to a
   network infrastructure, to request a service with specific
   connectivity and computing requirements, so traffic is steered to an
   instance meeting both requirements.  Both CATS-aware and -unaware
   terminals are considered.  Exemplary signaling control messages and
   operation extending the well-known Proxy Mobile IPv6 protocol are
   also defined.
- **draft-bertoldi-regext-rdap-reliability-scoring-03** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Structured Reliability Assessment Metadata](https://datatracker.ietf.org/doc/draft-bertoldi-regext-rdap-reliability-scoring/) — This document proposes an extension to the Registration Data Access
   Protocol (RDAP) that enables the representation and exchange of
   structured reliability assessment metadata for registrars and domain
   names.  The extension defines a structured assessment envelope
   through which an RDAP server can expose assessment results produced
   by a registry, registrar, or third-party assessor in a common,
   machine-readable format within RDAP responses.

   The extension standardizes how assessment results are transported and
   referenced, not how they are computed.  Scoring methodologies,
   thresholds, criteria, and governance frameworks are intentionally
   left to the operational and policy layer.  This document does,
   however, place requirements on the specification of any scheme whose
   results are intended for publication through RDAP, because publishing
   an evaluative judgement about an identified party without safeguards
   for notification, remediation, and contestation is not a safe
   practice.
- **draft-besleaga-sustainability-wellknown-07** (new-draft, score 0, ignored_after_review) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI, at
   which a web origin publishes a single JSON document declaring the
   energy consumption, carbon footprint, and related environmental
   metrics of a reporting subject, typically the origin itself.  The
   declaration is described by formal schemas and located at a fixed
   path, so that it can be retrieved, validated, and ingested
   automatically.  It carries an optional embedded signature, may
   reference the declarations of upstream providers from which its
   figures derive, links to a methodology, and may link to third-party
   attestations.  The metrics are self-asserted claims of the publisher.
   This document registers the well-known URI and the media type
   application/sustainability-data+json.
- **draft-cao-savnet-ipfix-sav-00** (new-draft, score 0, ignored_after_review) [none]: [Export of Source Address Validation (SAV) Information in IPFIX](https://datatracker.ietf.org/doc/draft-cao-savnet-ipfix-sav/) — This document specifies the IP Flow Information Export Information
   Elements to export the context and outcome of Source Address
   Validation enforcement data.  These SAV-specific Information Elements
   provide detailed insight into why packets are identified as spoofed
   by capturing the specific SAV rules that triggered validation
   decisions.  This operational visibility is essential for network
   operators to observe SAV enforcement behavior and analyze source
   address spoofing events detected by SAV.
- **draft-carpenter-anima-quads-grasp-04** (new-draft, score 0, ignored_after_review) [none]: [Quick and Dirty Secure Autonomic Control Plane for GRASP](https://datatracker.ietf.org/doc/draft-carpenter-anima-quads-grasp/) — A secure substrate known as the Autonomic Control Plane (ACP) is
   required by the Generic Autonomic Signaling Protocol (GRASP) used by
   Autonomic Service Agents.  This document describes QUADS, a QUick And
   Dirty Secure ACP using symmetric cryptography and preconfigured key
   material.  It also describes a secure mechanism for providing the
   prefconfigured key material to enrolled ACP nodes via EST.
- **draft-cmcc-asrp-08** (new-draft, score 0, ignored_after_review) [none]: [Available Session Recovery Protocol](https://datatracker.ietf.org/doc/draft-cmcc-asrp/) — This document describes an experimental protocol named the Available
   Session Recovery Protocol (ASRP).  The protocol is designed to
   optimize high-availability network cluster architectures, providing a
   superior high-availability solution for clusters offering stateful
   network services such as load balancing and Network Address
   Translation (NAT [RFC4787]).  ASRP defines the procedures for session
   backup and recovery, as well as the message formats used during these
   interactions, enabling efficient and streamlined session state
   management.

   In contrast to traditional high-availability techniques that back up
   session state within the cluster itself, the core innovation of ASRP
   lies in its distributed backup of state information to the client or
   server side.  This approach offers multiple advantages: theoretically
   unlimited elastic scaling capacity; support for rapid recovery from
   multi-point failures; reduction of resource redundancy through the
   elimination of centralized backup nodes; and significant
   simplification of cluster implementation complexity.

   The ASRP protocol provides a standardized method for constructing
   elastic service clusters, facilitating broader participation from
   software and hardware developers in building elastic cloud network
   service clusters.
- **draft-decraene-idr-nlri-error-handling-03** (new-draft, score 0, ignored_after_review) [none]: [The Key List BGP Attribute for NLRI Error handling](https://datatracker.ietf.org/doc/draft-decraene-idr-nlri-error-handling/) — RFC 7606 partially revises the error handling for BGP UPDATE
   messages.  It reduces the cases of BGP session reset by defining and
   using less impactful error handling approaches, such as attribute
   discard and treat-as-withdraw when applicable.  The treat-as-withdraw
   approach requires that the entire NLRI field of the MP_REACH_NLRI
   attribute be successfully parsed.  This typically means parsing
   errors in MP_REACH_NLRI cannot be handled by any means short of
   session reset.  This is exacerbated by the use of non-key data within
   NLRI, which introduces parsing complexity and additional error cases.

   This specification defines a non-transitive BGP attribute, the
   "NLRI_KEY_LIST attribute", to encode NLRIs as per the format of
   MP_UNREACH_NLRI.  This attribute is used to allow the treat-as-
   withdraw error-handling approach to be used in case an error in the
   MP_REACH_NLRI attribute prevents the parsing of its NLRIs.

   This document updates RFC 7606 by mandating that the NLRI_KEY_LIST
   attribute appear before the MP_REACH_NLRI (or any other) attribute in
   an UPDATE message.
- **draft-demosra-mtsv-01** (new-draft, score 0, ignored_after_review) [none]: [Multi-Sheet Tab-Separated Values (MTSV)](https://datatracker.ietf.org/doc/draft-demosra-mtsv/) — This document defines Multi-Sheet Tab-Separated Values (MTSV), a text
   format that carries one or more sheets of tab-separated values in a
   single file.  MTSV is TSV with one additional dimension: sheets are
   separated by the ASCII form feed (FF) character.  A TSV file that
   contains no FF, and no CR other than in CRLF line breaks, is an MTSV
   file.  This document also registers the text/prs.mtsv media type.
- **draft-denis-tls-aegis-07** (new-draft, score 0, ignored_after_review) [none]: [AEGIS-based Cipher Suites for TLS 1.3, DTLS 1.3, and QUIC](https://datatracker.ietf.org/doc/draft-denis-tls-aegis/) — This document proposes new cipher suites based on the AEGIS family of
   authenticated encryption with associated data (AEAD) algorithms.  The
   suites integrate AEGIS into TLS 1.3, DTLS 1.3, and QUIC.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-denis-tls-aegis/.

   Source for this draft and an issue tracker can be found at
   https://github.com/jedisct1/draft-denis-tls-aegis.
- **draft-dogru-cedulon-threats-00** (new-draft, score 0, ignored_after_review) [none]: [Cedulon Threat Narratives](https://datatracker.ietf.org/doc/draft-dogru-cedulon-threats/) — This document records the threat narratives and attack paths that sit
   behind the Cedulon core requirements.  It does not define those
   requirements.  T11 (checkpoint suppression) is recorded in the
   checkpoint companion, not here.
- **draft-dreibholz-rserpool-applic-distcomp-41** (new-draft, score 0, ignored_after_review) [none]: [Applicability of Reliable Server Pooling for Real-Time Distributed Computing](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-applic-distcomp/) — This document describes the applicability of the Reliable Server
   Pooling architecture to manage real-time distributed computing pools
   and access the resources of such pools.
- **draft-dreibholz-rserpool-applic-mobility-40** (new-draft, score 0, ignored_after_review) [none]: [Applicability of Reliable Server Pooling for SCTP-Based Endpoint Mobility](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-applic-mobility/) — This document describes a novel mobility concept based on a
   combination of SCTP with the Dynamic Address Reconfiguration
   extension and Reliable Server Pooling (RSerPool).
- **draft-dreibholz-rserpool-asap-hropt-39** (new-draft, score 0, ignored_after_review) [none]: [Handle Resolution Option for ASAP](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-asap-hropt/) — This document describes the Handle Resolution option for the ASAP
   protocol.
- **draft-dreibholz-rserpool-delay-38** (new-draft, score 0, ignored_after_review) [none]: [Definition of a Delay Measurement Infrastructure and Delay-Sensitive Least-Used Policy for Reliable Server Pooling](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-delay/) — This document contains the definition of a delay measurement
   infrastructure and a delay-sensitive Least-Used policy for Reliable
   Server Pooling.
- **draft-dreibholz-rserpool-enrp-takeover-36** (new-draft, score 0, ignored_after_review) [none]: [Takeover Suggestion Flag for the ENRP Handle Update Message](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-enrp-takeover/) — This document describes the Takeover Suggestion Flag for the
   ENRP_HANDLE_UPDATE message of the ENRP protocol.
- **draft-dreibholz-rserpool-nextgen-ideas-26** (new-draft, score 0, ignored_after_review) [none]: [Ideas for a Next Generation of the Reliable Server Pooling Framework](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-nextgen-ideas/) — This document collects ideas for a next generation of the Reliable
   Server Pooling framework.
- **draft-dreibholz-rserpool-score-39** (new-draft, score 0, ignored_after_review) [none]: [Reliable Server Pooling (RSerPool) Bakeoff Scoring](https://datatracker.ietf.org/doc/draft-dreibholz-rserpool-score/) — This memo describes some of the scoring to be used in the testing of
   Reliable Server Pooling protocols ASAP and ENRP at upcoming bakeoffs.
- **draft-dreibholz-taps-neat-socketapi-19** (new-draft, score 0, ignored_after_review) [none]: [NEAT Sockets API](https://datatracker.ietf.org/doc/draft-dreibholz-taps-neat-socketapi/) — This document describes a BSD Sockets-like API on top of the
   callback-based NEAT User API.  This facilitates porting existing
   applications to use a subset of NEAT's functionality.
- **draft-dreibholz-tsvwg-sctp-nextgen-ideas-24** (new-draft, score 0, ignored_after_review) [none]: [Ideas for a Next Generation of the Stream Control Transmission Protocol (SCTP)](https://datatracker.ietf.org/doc/draft-dreibholz-tsvwg-sctp-nextgen-ideas/) — This document collects ideas for a next generation of the Stream
   Control Transmission Protocol (SCTP) for further discussion.  It is a
   result of lessons learned over more than two decades of SCTP
   deployment.
- **draft-dreibholz-tsvwg-sctpsocket-multipath-33** (new-draft, score 0, ignored_after_review) [none]: [SCTP Socket API Extensions for Concurrent Multipath Transfer](https://datatracker.ietf.org/doc/draft-dreibholz-tsvwg-sctpsocket-multipath/) — This document describes extensions to the SCTP sockets API for
   configuring the CMT-SCTP and CMT/RP-SCTP extensions.
- **draft-dreibholz-tsvwg-sctpsocket-sqinfo-33** (new-draft, score 0, ignored_after_review) [none]: [Sender Queue Info Option for the SCTP Socket API](https://datatracker.ietf.org/doc/draft-dreibholz-tsvwg-sctpsocket-sqinfo/) — This document describes an extension to the SCTP sockets API for
   querying information about the sender queue.
- **draft-editorial-rswg-mathinrfcs-04** (new-draft, score 0, ignored_after_review) [none]: [Mathematical notation in RFCs](https://datatracker.ietf.org/doc/draft-editorial-rswg-mathinrfcs/) — This document defines policy and allows new technology for the
   representation of mathematical content in RFCXML and relevant
   publication formats.  After implementation of this policy, the chosen
   mathematical notation format should be used in RFCXML and the HTML
   publication format.
- **draft-gandhi-ippm-stamp-mpls-hdr-09** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet MPLS Network Action Headers](https://datatracker.ietf.org/doc/draft-gandhi-ippm-stamp-mpls-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect MPLS Network Action Sub-Stacks and
   Post-Stack MPLS Headers, for HBH and E2E active measurements, for
   example, by using the IOAM data fields.
- **draft-geng-sidrops-bgp-drip-00** (new-draft, score 0, ignored_after_review) [none]: [Dynamic Risk Indication and Propagation in BGP (DRIP)](https://datatracker.ietf.org/doc/draft-geng-sidrops-bgp-drip/) — This document specifies a framework and associated protocol
   extensions for dynamic routing risk propagation and automated
   mitigation in BGP networks.  Building upon Resource Public Key
   Infrastructure (RPKI) Route Origin Validation (ROV), this
   specification defines mechanisms to associate abnormal or hijacked
   routes with related routing entities (e.g., ASes or BGP peers) to
   dynamically depreference associated paths.  Furthermore, it
   introduces extensions to the RPKI-to-Router (RTR) protocol and BGP
   Path Attributes to feedback, distribute, and signal ROA risk
   indicators across Relying Parties (RPs) and BGP Routers, enabling
   proactive and coordinated threat mitigation across network
   boundaries.
- **draft-gerke-publication-process-reform-06** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
   deterministic state-integrity constraints within the IETF Datatracker
   architecture.  It establishes automated validation milestones and
   explicit access controls to prevent late technical modifications
   after the Working Group Last Call, thereby safeguarding the Rough
   Consensus.

   This document updates RFC 7841.
- **draft-gondwana-dkim2-debug-header-00** (new-draft, score 0, ignored_after_review) [none]: [A Diagnostic Header Field for DKIM2 Implementations](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-debug-header/) — Implementations of DomainKeys Identified Mail Signatures v2 (DKIM2)
   benefit from seeing extra debug information during the early
   deployment phase.

   This document is intended to help testers, and unlikely to be
   published.
- **draft-goto-otp-token-00** (new-draft, score 0, ignored_after_review) [none]: [The `OTP-Token` Email Header Field](https://datatracker.ietf.org/doc/draft-goto-otp-token/) — This document defines the OTP-Token email header field, which can be
   used to deliver One-Time Passcodes (OTP) in a machine-readable and
   origin-bound manner alongside the human-readable message carrying
   that content today.  Recipient Message User Agents (rMUA) can
   collaborate with other entities in the ecosystem to assist in the
   delivery of these codes to the context which wishes to verify their
   successful delivery.
- **draft-guthrie-ipsecme-aes-gcm-siv-01** (new-draft, score 0, ignored_after_review) [none]: [Using AES-GCM-SIV in the Internet Protocol Version 2 (IKEv2) and Encapsulating Security Payload (ESP) Protocols](https://datatracker.ietf.org/doc/draft-guthrie-ipsecme-aes-gcm-siv/) — This document specifies the use of AES-GCM-SIV in the Internet Key
   Exchange Protocol version 2 (IKEv2) and the Encapsulating Security
   Payload (ESP) protocols.  This document also adds AES-GCM-SIV to the
   IANA IKEv2 registry for "Transform Type 1 - Encryption Algorithm
   Transform IDs."  AES-GCM-SIV is a nonce misuse-resistant
   authenticated encryption with associated data (AEAD) algorithm based
   on AES-GCM.
- **draft-helmprotocol-confidence-00** (new-draft, score 0, ignored_after_review) [none]: [Oracle Confidence Gating: G-Score, Correlation-Aware von Neumann Confidence, and AdaptiveSwitch](https://datatracker.ietf.org/doc/draft-helmprotocol-confidence/) — This document specifies an optional confidence layer for the TLS
   TimeToken Secure Protocol (TTTPS).  It defines the G-Score, a
   normalized entropy measure of agreement concentration; an optional
   correlation-aware von Neumann extension; the InsufficientKnowledge
   signal; and the AdaptiveSwitch state machine over TURBO and FULL.
   The confidence layer qualifies whether evidence justifies action.  It
   does not replace cryptographic integrity, define a wire format,
   allocate a codepoint, establish source independence, or require any
   core TTTPS implementation to compute confidence.
- **draft-herdes-idr-otc-rs-verification-01** (new-draft, score 0, ignored_after_review) [none]: [Strict Only to Customer (OTC) Verification on Route Server Sessions](https://datatracker.ietf.org/doc/draft-herdes-idr-otc-rs-verification/) — RFC 9234 specifies how an AS receiving a route from a lateral Peer
   can check if a route was leaked, but doesn't specify any checks for
   routes received from a Route Server (RS).  This makes the quality of
   filtering dependent on whether the RS implements RFC 9234.

   This document updates RFC 9234 by adding a complementary ingress
   check by an RS-Client.
- **draft-hoffman-rootcache-02** (new-draft, score 0, ignored_after_review) [none]: [RootCache: Filling Resolver Caches with Root Zone Records](https://datatracker.ietf.org/doc/draft-hoffman-rootcache/) — Some DNS recursive resolver operators want to prevent snooping by
   third parties of requests sent to DNS root servers.  Resolvers can
   reduce the number of queries sent to root server, and thus prevent
   observation of requests, by caching a copy of the full root zone.
   This document shows how a resolver can securely receive the full root
   zone and put it into the resolver's cache.

   This document obsoletes RFC 8806.
- **draft-hohendorf-secure-sctp-42** (new-draft, score 0, ignored_after_review) [none]: [Secure SCTP](https://datatracker.ietf.org/doc/draft-hohendorf-secure-sctp/) — This document explains the reason for the integration of security
   functionality into SCTP, and gives a short description of S-SCTP and
   its services.  S-SCTP is fully compatible with SCTP, it is designed
   to integrate cryptographic functions into SCTP.
- **draft-housley-asn1-layman-guide-02** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This memo offers tutorial information.
- **draft-huang-idr-color-time-schedule-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Extension for Time-Scheduled Color based SR Policy Selection](https://datatracker.ietf.org/doc/draft-huang-idr-color-time-schedule/) — Segment Routing (SR) Policy is identified by a tuple of Color and
   Endpoint.  In BGP/MPLS IP VPN and EVPN services, the egress PE
   attaches a Color Extended Community to the advertised VPN route so
   that the ingress PE can steer the traffic into a corresponding SR
   Policy.

   In many deployment scenarios, the same customer may require different
   Service Level Agreements (SLAs) during different time periods of a
   day.  For example, a customer may require a high- bandwidth SLA
   during the off-peak hours (e.g., 02:00-06:00) and a low-cost SLA
   during the daytime.  Such time-variant SLA requirements imply that
   the ingress PE should select different SR Policies (i.e., different
   Colors) for the same VPN route at different times.

   This document defines a new BGP Extended Community, called the
   Schedule Extended Community, to be used together with the Color
   Extended Community.  Two sub-types of the Schedule Extended Community
   are defined: a Daily Schedule sub-type for recurring time-of-day
   periods, and a Day Schedule sub-type for specific dates.  The
   Schedule Extended Community carries the time period during which the
   associated Color is valid.  Based on the current time and the
   received Schedule Extended Communities, the ingress PE can
   dynamically select the appropriate SR Policy for a VPN route, thereby
   realizing time-scheduled SLA switching.
- **draft-huang-spring-time-scheduled-color-behavior-00** (new-draft, score 0, ignored_after_review) [none]: [Headend Behavior for Time-Scheduled Color based SR Policy Selection](https://datatracker.ietf.org/doc/draft-huang-spring-time-scheduled-color-behavior/) — This document specifies the normative behavior of the ingress
   Provider Edge (PE) router (headend) when selecting a Segment Routing
   (SR) Policy for VPN traffic based on time-scheduled Color values.

   In the time-scheduled Color mechanism, the egress PE advertises
   multiple (Color, Schedule) groups for the same VPN routes.  The
   headend evaluates the schedule associated with each Color based on
   the current time, selects a currently valid Color, and steers the
   traffic into the corresponding SR Policy.

   This document defines the requirements for parsing the Color and
   Schedule Extended Communities, evaluating schedule validity,
   selecting among multiple valid Colors, performing schedule-boundary
   timer-based re-evaluation, handling switchover with make-before-
   break, and falling back when no Color is valid.

   This document updates RFC 9256 by replacing the multiple-Color
   selection rule specified in Section 8.4.1 with a Schedule-based
   selection rule.
- **draft-huang-spring-time-scheduled-color-framework-00** (new-draft, score 0, ignored_after_review) [none]: [Framework for Time-Scheduled Color based SR Policy Selection](https://datatracker.ietf.org/doc/draft-huang-spring-time-scheduled-color-framework/) — In Segment Routing (SR) based VPN services, the BGP Color Extended
   Community is used by the egress Provider Edge (PE) router to steer
   VPN traffic into an SR Policy at the ingress PE.  In many deployment
   scenarios, a customer requires different Service Level Agreements
   (SLAs) during different time periods of a day.  For example, during
   business hours (e.g., 06:00 to 02:00 the next day) a best-effort,
   lower-cost SLA is sufficient for normal office traffic, while during
   the early morning hours (e.g., 02:00 to 06:00) a high-bandwidth,
   low-latency SLA is required for massive data transmission such as
   scientific computing.

   This document presents a framework for time-scheduled Color based SR
   Policy selection.  The mechanism allows the egress PE to advertise
   multiple (Color, Color Schedule) pairs for the same VPN routes,
   enabling the ingress PE to select the appropriate SR Policy based
   on the current time.  The time-to-Color mapping is configured per
   VPN instance (VRF/VSI), so each customer can have an independent
   time-varying SLA policy.

   This document is an Informational framework that describes the
   problem and the overall architecture.  The advantages of the
   proposed mechanism and the comparison with alternative approaches
   are provided in Appendix A.  The normative specifications of the
   protocol extensions, data models, and other components are
   described in Appendix B.
- **draft-ietf-6man-ieee80211-dms-00** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 wants 802.11 Directed Multicast Service](https://datatracker.ietf.org/doc/draft-ietf-6man-ieee80211-dms/) — There is consensus for switching this document from Flexible
   Multicast Service (FMS) to Directed Multicast Service (DMS).  This
   version has not been edited over yet and is being uploaded to check
   if/how the name can be changed.

   IEEE 802.11 Flexible Multicast Service (FMS) addresses reliability
   issues in IPv6 due to aggressive powersave optimizations in 802.11
   client devices.

   The intent of this document is to collect consensus in the IETF 6man
   (IPv6 Maintenance) working group to request either/both the IEEE
   802.11 Working Group and/or the Wifi Alliance's certification process
   to make implementing FMS a requirement.
- **draft-ietf-asdf-sdf-nonaffordance-05** (new-draft, score 0, ignored_after_review) [asdf]: [Semantic Definition Format (SDF) Extension for Non-Affordance Information](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-nonaffordance/) — This document describes an extension to the Semantic Definition
   Format (SDF) for representing non-affordance information of Things,
   such as physical, contextual, and descriptive metadata.  This
   extension introduces a new class keyword, sdfContext, that enables
   comprehensive modeling of Things and improves semantic clarity.
- **draft-ietf-avtcore-rtp-jpegxs-3ed-07** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for ISO/IEC 21122 (JPEG XS)](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-jpegxs-3ed/) — This document specifies a Real-Time Transport Protocol (RTP) payload
   format for transport of a video signal encoded with JPEG XS (ISO/IEC
   21122).  JPEG XS is a low-latency and low-complexity video coding
   system.  Employing this format allows achieving encoding-decoding
   latencies confined to a fraction of a video frame.

   This document revises RFC 9134 to incorporate support for new
   features introduced in the third edition of JPEG XS.  Most notably,
   it contains the necessary provisions to support the TDC coding mode.
   This document obsoletes RFC 9134; however, the revised payload format
   is designed to ensure that existing conforming implementations of RFC
   9134 remain valid under the updated specification.  Additionally,
   this document consolidates the errata of RFC 9134 and includes
   improvements and clarifications for implementers and users.
- **draft-ietf-avtcore-rtp-vdmc-03** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for V-DMC](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-vdmc/) — This memo outlines RTP payload formats for the Video-based Dynamic
   Mesh Coding (V-DMC), which comprises several types of components,
   such as a basemesh, AC-based displacements, 2D representations of
   attributes, and an atlas.  This document focuses on describing the
   basemesh and displacement, while the RTP payload formats for the
   atlas and attributes are addressed in other documents.  The RTP
   payload header formats enable the packetization of a basemesh or
   displacement Network Abstraction Layer (NAL) unit in an RTP packet
   payload as well as fragmentation of a NAL unit into multiple RTP
   packets.
- **draft-ietf-bess-evpn-l3mh-proto-01** (new-draft, score 0, ignored_after_review) [bess]: [EVPN multi-homing support for L3 services](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-l3mh-proto/) — This document describes the use of EVPN Ethernet Segment Link
   Aggregation Group (ES-LAG) technology to provide multi-homing
   redundancy for Layer 3 services.  The solution synchronizes ARP/ND,
   multicast state, and IGP routes between redundant PEs without
   requiring Layer 2 constructs or proprietary Inter-Chassis
   Communication protocols.
- **draft-ietf-bier-ping-29** (new-draft, score 0, ignored_after_review) [bier]: [Bit Index Explicit Replication (BIER) Ping and Trace](https://datatracker.ietf.org/doc/draft-ietf-bier-ping/) — Bit Index Explicit Replication (BIER) is a multicast forwarding
   architecture designed to simplify and optimize multicast delivery.

   This document specifies the mechanism and basic BIER OAM packet
   format that can be used to perform failure detection and isolation on
   the BIER data plane without any dependency on other layers, like the
   IP layer.
- **draft-ietf-bmwg-savnet-sav-benchmarking-04** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-bmwg-savnet-sav-benchmarking/) — This document defines methodologies for benchmarking the performance
   of intra-domain and inter-domain source address validation (SAV)
   mechanisms.  SAV mechanisms are utilized to generate SAV rules that
   prevent source address spoofing.  The methodology treats a SAV device
   as a black box and is therefore agnostic to the specific SAV
   mechanism and implementation used by the device.  This document
   defines test setups, performance indicators, and test cases for SAV
   accuracy, control-plane and data-plane performance, and resource
   utilization.
- **draft-ietf-calext-icalendar-jscalendar-extensions-08** (new-draft, score 0, ignored_after_review) [calext]: [iCalendar Format Extensions for JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-icalendar-jscalendar-extensions/) — This document defines a set of new elements for iCalendar and extends
   the use of existing ones.  Their main purpose is to extend the
   semantics of iCalendar with elements defined in JSCalendar, but the
   new definitions also aim to be useful within just the iCalendar
   format.  This document updates RFC 5545 ("iCalendar") and its
   extension documents RFC 7986 and RFC 9073.
- **draft-ietf-calext-jscalendar-icalendar-28** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
   the JSCalendar and iCalendar data formats.  It considers every
   JSCalendar and iCalendar element registered at IANA at the time of
   publication.  It defines conversion rules for all elements that are
   common to both formats, as well as how convert arbitrary or unknown
   JSCalendar and iCalendar elements.  This document updates RFC 5545
   ("iCalendar") and jscalendarbis ("JSCalendar") by defining new
   properties and parameters for JSCalendar and iCalendar conversion.
- **draft-ietf-core-conditional-attributes-14** (new-draft, score 0, ignored_after_review) [core]: [Conditional Query Parameters for CoAP Observe](https://datatracker.ietf.org/doc/draft-ietf-core-conditional-attributes/) — This specification defines Conditional Notification and Control Query
   Parameters compatible with CoAP Observe (RFC7641).
- **draft-ietf-detnet-scaling-requirements-11** (new-draft, score 0, ignored_after_review) [detnet]: [Requirements for Scaling Deterministic Networks](https://datatracker.ietf.org/doc/draft-ietf-detnet-scaling-requirements/) — To support the scaling of deterministic networks, this document
   describes the technical and operational requirements for networks
   that exhibit large hop-to-hop latency variation, a large number of
   flows, and/or multiple domains that do not share a common time
   source.  Applications with varying levels of determinism coexist and
   are transported in such a network.  This document also describes the
   corresponding Deterministic Networking (DetNet) data plane
   enhancement requirements.
- **draft-ietf-idr-bgp-bestpath-selection-criteria-13** (new-draft, score 0, ignored_after_review) [idr]: [BGP Bestpath Selection Criteria Enhancement](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-bestpath-selection-criteria/) — BGP specification (RFC4271) prescribes 'BGP next-hop reachability'
   as one of the key 'Route Resolvability Condition' that must be
   satisfied before the BGP bestpath candidate selection. This
   condition, however, may not be sufficient (as explained in the
   Appendix section) and would desire further granularity.

   This document defines enhances the "Route Resolvability Condition"
   to facilitate the next-hop to be resolved in the chosen data plane.
- **draft-ietf-idr-bgpls-inter-as-topology-ext-44** (new-draft, score 0, ignored_after_review) [idr]: [BGP-LS Extensions for Inter-AS Topology Retrieval](https://datatracker.ietf.org/doc/draft-ietf-idr-bgpls-inter-as-topology-ext/) — This document specifies the procedures for distributing Border
   Gateway Protocol-Link State (BGP-LS) key parameters for inter-domain
   links between two Autonomous Systems (ASes).  It defines a new type
   within the BGP-LS Network Layer Reachability Information (NLRI) for
   an Inter-AS Link, along with three new Type-Length-Values (TLVs)
   descriptors for the BGP-LS Inter-AS Link.

   These extensions and procedures allow network operators to collect
   inter-domain interconnect information and automatically compute the
   inter-AS topology using information provided by the BGP-LS protocol.
- **draft-ietf-ippm-alt-mark-deployment-09** (new-draft, score 0, ignored_after_review) [ippm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
- **draft-ietf-ippm-stamp-ext-hdr-14** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet IP Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ext-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect IP headers as well as IPv6
   extension headers for HBH and E2E active measurements, for example,
   using the IOAM data fields.

   This document specifies the requirements for IPv6 STAMP in
   unauthenticated mode using UDP zero-checksum, which deviates from the
   integrity requirement in RFC 6936.
- **draft-ietf-jmap-conditional-00** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Conditional Set](https://datatracker.ietf.org/doc/draft-ietf-jmap-conditional/) — The JMAP base protocol ([JMAP-CORE]) provides the Foo/set method for
   creating, updating, and destroying objects.  It offers a single
   concurrency control, the "ifInState" argument, which guards an entire
   object type: if any object of that type has changed, the whole method
   is rejected.

   This extension adds a finer, per-object conditional mechanism.  A
   client may require that an individual update or destroy proceed only
   if the target object still matches a set of expected property values,
   expressed using the JMAP PatchObject already defined for updates.
   This provides optimistic concurrency control scoped to a single
   object — the equivalent of an HTTP "If-Match" precondition — for any
   JMAP data type.

   This extension also defines an optional "atomic" argument that
   applies an entire Foo/set as a single unit: either every change it
   requests takes effect, or none does.  Combined with the per-object
   precondition, this lets a client express a multi-object change that
   is safe only when applied together — such as an atomic rename that
   exchanges two names.
- **draft-ietf-jmap-object-history-00** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Object History](https://datatracker.ietf.org/doc/draft-ietf-jmap-object-history/) — The JMAP base protocol (RFC8620) provides methods for synchronizing
   the current state of data objects between client and server.  This
   extension adds the ability to retrieve historical versions of
   objects, including objects that have been destroyed, by extending the
   standard Foo/get method.
- **draft-ietf-lisp-rfc6831bis-08** (new-draft, score 0, ignored_after_review) [lisp]: [The Locator/ID Separation Protocol (LISP) for Multicast Environments](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc6831bis/) — This document specifies the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP) architecture
   and protocols.  The document specifies how LISP multicast overlays
   operate over multicast and unicast underlays.  The mechanisms in this
   specification indicate how a signal-based approach using the PIM
   protocol can be used to program LISP encapsulators with a replication
   list in a locator-set, where the replication list can be a mix of
   multicast and unicast locators.  This document when approved
   obsoletes RFC6831
- **draft-ietf-lsr-srv6-mirror-sid-igp-encoding-00** (new-draft, score 0, ignored_after_review) [lsr]: [IGP Encoding for SRv6 Mirror SID in Egress Protection](https://datatracker.ietf.org/doc/draft-ietf-lsr-srv6-mirror-sid-igp-encoding/) — This document specifies the IGP protocol extensions required to
   support SRv6 path egress protection using the Mirror SID (End.M)
   mechanism.  It reuses the existing SRv6 End SID sub-TLV defined in
   [RFC9352] (IS-IS, Section 7.2) and [RFC9513] (OSPFv3, Section 8) with
   the End.M endpoint behavior (74) to advertise the Mirror SID and the
   set of protected locators, and defines a new Protected Locators
   sub-(sub-)TLV, enabling a backup egress node (protector) to signal
   its capability to protect a primary egress node within a single link-
   state IGP area.

   This document is a companion to
   [I-D.ietf-rtgwg-srv6-egress-protection], which specifies the overall
   SRv6 path egress protection mechanism and the End.M behavior.  The
   IGP encoding defined herein provides the signaling substrate for that
   mechanism.
- **draft-ietf-mailmaint-pdparchive-02** (new-draft, score 0, ignored_after_review) [mailmaint]: [Personal Data Portability Archive](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-pdparchive/) — This document proposes the Personal Data Portability Archive format
   (PDPA), suitable for import/export, backup/restore, and data transfer
   scenarios for personal data.
- **draft-ietf-mpls-on-path-telemetry-flag-04** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes postcard-based on-path telemetry with packet
   marking (PBT-M) using an MPLS Network Actions (MNA) flag to support
   Operations, Administration, and Maintenance (OAM) in MPLS networks.
   The scheme uses a single flag bit carried in a Flag-Based Network
   Action Indicator (Opcode 1) of the MNA Sub-Stack as defined in RFC
   9994.  In addition to addressing the protocol requirements for
   applying PBT-M, this document provides comprehensive operational,
   manageability, and security considerations.
- **draft-ietf-netconf-restconf-trace-ctx-headers-11** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extension to Support Trace Context Headers](https://datatracker.ietf.org/doc/draft-ietf-netconf-restconf-trace-ctx-headers/) — This document defines an extension to the RESTCONF protocol to
   support Trace Context propagation as defined by the W3C.
- **draft-ietf-netconf-trace-ctx-extension-09** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extension to support Trace Context propagation](https://datatracker.ietf.org/doc/draft-ietf-netconf-trace-ctx-extension/) — This document defines how to propagate trace context information
   across the Network Configuration Protocol (NETCONF), enabling
   distributed tracing scenarios.  It is an adaptation of the HTTP-based
   W3C specification and defines three YANG modules.
- **draft-ietf-netconf-yang-notifications-versioning-16** (new-draft, score 0, ignored_after_review) [netconf]: [Support of Versioning in YANG Notifications Subscription](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-notifications-versioning/) — This document defines a YANG module which extends the YANG-Push
   Subscription mechanism to enforce that particular revisions or
   semantic versions are used when configuring or establishing a
   Subscription.  It also extends the YANG-Push Subscription state
   change Notifications to include additional context about the YANG
   schema associated with the Subscription.
- **draft-ietf-nfsv4-nfs-acl-05** (new-draft, score 0, ignored_after_review) [nfsv4]: [The Network File System Access Control List Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-nfs-acl/) — This Informational document describes the NFS_ACL protocol.  NFS_ACL
   is a legacy member of the Network File System family of protocols
   that NFS clients use to view and update Access Control Lists stored
   on an NFS version 2 or version 3 server.
- **draft-ietf-nfsv4-rfc8881bis-10** (new-draft, score 0, ignored_after_review) [nfsv4]: [Network File System (NFS) Version 4 Minor Version 1 Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-rfc8881bis/) — This document describes the Network File System (NFS) version 4 minor
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
- **draft-ietf-nfsv4-uncacheable-files-16** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable File Data Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-files/) — Network File System version 4.2 (NFSv4.2) clients commonly perform
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
- **draft-ietf-nvo3-rfc7348bis-10** (new-draft, score 0, ignored_after_review) [nvo3]: [Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks](https://datatracker.ietf.org/doc/draft-ietf-nvo3-rfc7348bis/) — This document specifies Virtual eXtensible Local Area Network
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
- **draft-ietf-opsawg-pcap-09** (new-draft, score 0, ignored_after_review) [opsawg]: [PCAP Capture File Format](https://datatracker.ietf.org/doc/draft-ietf-opsawg-pcap/) — This document describes the format used by the libpcap library to
   record captured packets to a file.  Programs using the libpcap
   library to read and write those files, and thus reading and writing
   files in that format, include tcpdump.
- **draft-ietf-opsawg-pcapng-06** (new-draft, score 0, ignored_after_review) [opsawg]: [PCAP Now Generic (pcapng) Capture File Format](https://datatracker.ietf.org/doc/draft-ietf-opsawg-pcapng/) — This document describes a format to record captured packets to a
   file.  This format is extensible; Wireshark can currently read and
   write it, and libpcap can currently read some pcapng files.
- **draft-ietf-pce-flexible-grid-19** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-pce-pcep-ls-optical-00** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extensions for Distribution of Link-State and TE Information for Optical Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-ls-optical/) — In order to compute and provide optimal paths, Path Computation
   Elements (PCEs) require an accurate and timely Traffic Engineering
   Database (TED).  This Link State and TE information has previously
   been obtained from a link state routing protocol that supports
   traffic engineering extensions.

   Link-State (LS) and Traffic Engineering (TE) information can also be
   carried in the Path Computation Element Communication Protocol (PCEP)
   using experimental exensions to PCEP known as Link-State PCEP (PCEP-
   LS).  This document provides further experimental extensions to
   collect Link-State and TE information for optical networks.
- **draft-ietf-pce-pcep-pmtu-10** (new-draft, score 0, ignored_after_review) [pce]: [Support for Path MTU (PMTU) in the Path Computation Element (PCE) Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-pmtu/) — The Path Computation Element (PCE) provides path computation
   functions in support of traffic engineering in Multiprotocol Label
   Switching (MPLS) and Generalized MPLS (GMPLS) networks.

   The Source Packet Routing in Networking (SPRING) architecture
   describes how Segment Routing (SR) can be used to steer packets
   through an IPv6 or MPLS network using the source routing paradigm.  A
   Segment Routed Path can be derived from a variety of mechanisms,
   including an IGP Shortest Path Tree (SPT), explicit configuration, or
   a Path Computation Element (PCE).

   Since the SR does not require signaling, the path maximum
   transmission unit (MTU) information for the SR path is unavailable at
   the headend.  This document specifies the extension to PCE
   Communication Protocol (PCEP) to carry path MTU as a new metric type
   in the PCEP messages for SR, but not limited to it.

   This document also updates RFC 5440 to allow metric bounds to be
   minimum as needed in the case of path MTU.
- **draft-ietf-pim-gaap-24** (new-draft, score 0, ignored_after_review) [pim]: [Group Address Allocation Protocol (GAAP)](https://datatracker.ietf.org/doc/draft-ietf-pim-gaap/) — This document describes a design for a lightweight decentralized
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
- **draft-ietf-pim-rfc8059-9798bis-02** (new-draft, score 0, ignored_after_review) [pim]: [PIM Join Attributes for Locator/ID Separation Protocol (LISP) Environments](https://datatracker.ietf.org/doc/draft-ietf-pim-rfc8059-9798bis/) — This document defines two PIM Join/Prune attributes that support the
   construction of multicast distribution trees where the root and
   receivers are located in different Locator/ID Separation Protocol
   (LISP) sites.  These attributes allow the receiver site to select
   between unicast and multicast underlying transport, to convey the
   RLOC (Routing Locator) address of the receiver ETR (Egress Tunnel
   Router) to the control plane of the root ITR (Ingress Tunnel Router)
   and to signal the underlay multicast group to the control plane of
   the root ITR.  This document updates RFC 8059 and RFC 9798.
- **draft-ietf-rtgwg-atn-bgp-33** (new-draft, score 0, ignored_after_review) [rtgwg]: [A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/) — The International Civil Aviation Organization (ICAO) is investigating
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
- **draft-ietf-rtgwg-dst-src-routing-revive-06** (new-draft, score 0, ignored_after_review) [rtgwg]: [Destination/Source Routing](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-dst-src-routing-revive/) — This document specifies using packets' source addresses in route
   lookups as additional qualifier to be used in hop-by-hop routing
   decisions.  The proposed mechanism applies to IPv6 [RFC8200] in
   general with specific considerations for routing protocols.
- **draft-ietf-sfc-nsh-ecn-support-18** (new-draft, score 0, ignored_after_review) [none]: [Explicit Congestion Notification (ECN) and Congestion Feedback Using the Network Service Header (NSH) and IPFIX](https://datatracker.ietf.org/doc/draft-ietf-sfc-nsh-ecn-support/) — Explicit Congestion Notification (ECN) allows a forwarding element to
   notify downstream devices of the onset of congestion without having
   to drop packets.  Coupled with a means to feed information about
   congestion back to upstream nodes, this can improve network
   efficiency through better congestion control, frequently without
   packet drops.  This document specifies ECN and congestion feedback
   support within a Service Function Chaining (SFC) enabled domain
   through use of the Network Service Header (NSH, RFC 8300) and IP Flow
   Information Export (IPFIX, RFC 7011) protocol.
- **draft-ietf-sidrops-publication-server-bcp-11** (new-draft, score 0, ignored_after_review) [sidrops]: [Best Practices for Operating Resource Public Key Infrastructure (RPKI) Publication Services](https://datatracker.ietf.org/doc/draft-ietf-sidrops-publication-server-bcp/) — This document describes best current practices for operating an RFC
   8181 (A Publication Protocol for the Resource Public Key
   Infrastructure (RPKI)) publication engine and its associated publicly
   accessible rsync (RFC 5781) and RPKI Repository Delta Protocol (RRDP)
   (RFC 8182) repositories.
- **draft-ietf-spring-stamp-srpm-mpls-08** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as specified in RFC 8762,
   along with its optional extensions specified in RFC 8972 and further
   augmented in RFC 9503.  The procedures described in this document are
   used for SR-MPLS paths (including Segment Lists of SR-MPLS Policies,
   SR-MPLS IGP best paths, and SR-MPLS IGP Flexible Algorithm (Flex-
   Algo) paths), as well as Layer-3 and Layer-2 services carried over
   the SR-MPLS paths.
- **draft-ietf-spring-stamp-srpm-srv6-05** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and further
   augmented in RFC 9503.  The procedures described in this document are
   used for links and SRv6 paths (including Segment Lists of SRv6
   Policies, SRv6 IGP best paths, and SRv6 IGP Flexible Algorithm (Flex-
   Algo) paths), as well as Layer-3 and Layer-2 services carried over
   the SRv6 paths.
- **draft-irtf-iccrg-pacing-04** (new-draft, score 0, ignored_after_review) [iccrg]: [Pacing in Transport Protocols](https://datatracker.ietf.org/doc/draft-irtf-iccrg-pacing/) — Applications or congestion control mechanisms can produce bursty
   traffic, which can cause unnecessary queuing and packet loss.  To
   reduce the burstiness of traffic, the concept of evenly spacing out
   the traffic from a data sender over a round-trip time known as
   "pacing" has been used in many transport protocol implementations.
   This document gives an overview of pacing and how some known pacing
   implementations work.
- **draft-laxsharma-pact-02** (new-draft, score 0, ignored_after_review) [none]: [PACT: Co-Signed Task Contracts, Delivery and Verdict Records, and Outcome Records for Autonomous Agents](https://datatracker.ietf.org/doc/draft-laxsharma-pact/) — Autonomous agents can already prove who they are, show whose
   authority they act under, find and call one another, and pay.  What
   no existing specification lets them do is agree on a task in a form a
   third party can check, deliver against it, have the delivery judged
   by someone other than the performer, and carry away a record of the
   outcome that a stranger can verify.  This document specifies PACT, a
   set of signed JSON records that closes that gap.

   PACT defines four things: a co-signed task contract whose digest
   covers its signature set; a Verdict record bound by digest to the
   Delivery it judges; a Facilitator-signed event trace and Outcome
   Record for every contract, recorded once, in one order, by a party
   other than the performer; and a Merkle commitment from a parent's
   Outcome Record to its subcontracts' Outcome Records.

   Settlement terms are carried by reference to a profile defined
   outside this document.  This document specifies no escrow, custody or
   release of value, and takes no position on the legal effect of any
   record it defines.
- **draft-li-rttp-intent-addressing-01** (new-draft, score 0, ignored_after_review) [none]: [Intent Addressing in the rttp URI Scheme](https://datatracker.ietf.org/doc/draft-li-rttp-intent-addressing/) — This document specifies the "rttp" URI scheme.  An "rttp" URI names a
   claim of intent directed at an identified subject; the address of
   that subject is derived by computation from the URI authority, and no
   lookup service, registry, or name-resolution system is consulted at
   resolution time.  The document also states the requirements a client
   MUST satisfy when it handles such a URI, in order to avoid two
   failure modes that short, user-embeddable strings otherwise invite:
   using the authority as a navigation target (open redirect), and using
   a registered protocol handler as a general-purpose launcher.
- **draft-limarsjenwar-tiptop-address-space-00** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Address Space for Space](https://datatracker.ietf.org/doc/draft-limarsjenwar-tiptop-address-space/) — Without a structured address allocation plan, early space missions
   risk creating an unaggregated patchwork of prefixes, repeating the
   historical operational scaling issues seen in terrestrial networks.

   This document requests that the IANA allocate address space
   specifically for use in space environments and manages suballocations
   from that block for and within celestial bodies, as needed.  The
   Number Resource Organization (NRO) will determine how to allocate and
   assign address resources for and within the celestial bodies , with
   the understanding that topological address aggregation is critical
   for routing scalability and operational efficiency.
- **draft-lin-idr-distribute-service-metric-07** (new-draft, score 0, ignored_after_review) [none]: [Distribute Service Metric by BGP](https://datatracker.ietf.org/doc/draft-lin-idr-distribute-service-metric/) — When calculating the path selection for service traffic, it is
   important to consider not only network metrics, but also the impact
   of service Metric. Therefore, it is necessary to transmit service
   Metric information from the service site to the user access site, in
   order to facilitate path selection for service traffic at the access
   router.

   This document describes an approach for using the BGP Control Plane
   to steer traffic based on a set of metrics that reflect the
   underlying network conditions and other service-specific state
   collected from available service locations.
- **draft-liu-add-dnssd-edns-03** (new-draft, score 0, ignored_after_review) [none]: [DNS-Based Service Discovery for Encrypted DNS Services](https://datatracker.ietf.org/doc/draft-liu-add-dnssd-edns/) — This document defines a DNS-Based Service Discovery (DNS-SD)
   mechanism for discovering encrypted DNS services in local networks.
   It specifies new service types (_dot._tcp, _doh._tcp, _doq._udp) and
   associated service parameters to enable zero-configuration discovery
   of DNS over TLS (DoT), DNS over HTTPS (DoH), and DNS over QUIC (DoQ)
   resolvers.  This mechanism is defined for use with multicast DNS
   (mDNS), addressing critical privacy gaps in local networks while
   maintaining backward compatibility with RFC 6763.  This document
   leverages SVCB and HTTPS resource records (RFC 9460) for parameter
   negotiation, with TXT records provided for compatibility with legacy
   implementations.
- **draft-ma-v6ops-5g-ipv6only-04** (new-draft, score 0, ignored_after_review) [v6ops]: [Considerations of IPv6-only Deployment in 5G Mobile Networks](https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/) — This document describes a practical guide of deploying 464XLAT based
   IPv6-only technology on user plane in 3GPP 5G networks.  It also
   covers key 5G concepts and architectures, configuration methods and
   operational challenges.
- **draft-martin-ipv6-addr-selection-updates-00** (new-draft, score 0, ignored_after_review) [none]: [Updates to IPv6 Default Address Selection](https://datatracker.ietf.org/doc/draft-martin-ipv6-addr-selection-updates/) — This document updates RFC 6724 with three improvements to IPv6
   destination address selection.  The updates allow recent IPv6
   connection or service failures to influence IPv6/IPv4 ordering,
   incorporate likely source/destination address pairs when sorting
   candidates, and let ISP and enterprise operators preserve DNS load-
   balancing order where Rule 9 would otherwise override it.  The
   updates are intended to be implementable inside getaddrinfo() or an
   equivalent system mechanism, without requiring changes to existing
   application-facing socket APIs.
- **draft-navarre-quic-flexicast-03** (new-draft, score 0, ignored_after_review) [none]: [Flexicast QUIC: combining unicast and multicast in a single QUIC connection](https://datatracker.ietf.org/doc/draft-navarre-quic-flexicast/) — This document proposes Flexicast QUIC, a simple extension to
   Multipath QUIC that enables a source to send the same information to
   a set of receivers using a combination of unicast paths and IP
   multicast distribution trees.
- **draft-pardue-moq-qlog-moq-events-08** (new-draft, score 0, ignored_after_review) [none]: [MoQ qlog event definitions](https://datatracker.ietf.org/doc/draft-pardue-moq-qlog-moq-events/) — This document defines a qlog event schema containing concrete events
   for MoQ.
- **draft-prz-lsr-ash-packets-03** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
- **draft-rosomakho-tls-ecdhe-mlkem512-01** (new-draft, score 0, ignored_after_review) [none]: [Post-quantum hybrid ECDHE-MLKEM512 Key Agreement for TLSv1.3](https://datatracker.ietf.org/doc/draft-rosomakho-tls-ecdhe-mlkem512/) — This document defines two post-quantum hybrid key exchange groups for
   TLS 1.3 that combine ML-KEM-512 with ECDHE: MLKEM512X25519 and
   SecP256r1MLKEM512.  These groups provide lower-overhead hybrid key
   exchange options for deployments where ClientHello size,
   fragmentation risk, constrained-device performance, or compatibility
   with existing network infrastructure are important considerations.
   The groups defined in this document are intended for use with TLS 1.3
   and DTLS 1.3 and follow the hybrid key exchange construction used by
   ECDHE-MLKEM key agreement for TLS 1.3.
- **draft-sharma-moq-atomic-subscription-bundles-00** (new-draft, score 0, ignored_after_review) [none]: [Atomic Subscription Bundles for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-sharma-moq-atomic-subscription-bundles/) — This document defines a Media over QUIC Transport (MOQT) extension
   for atomically changing the Forward State of a set of established
   subscriptions.  It allows a subscriber to replace one set of Tracks
   with another without an intermediate partially switched state at its
   peer.
- **draft-sharma-moq-cache-signaling-00** (new-draft, score 0, ignored_after_review) [none]: [Cache Signaling for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-sharma-moq-cache-signaling/) — This document defines optional hop-by-hop cache signaling for Media
   over QUIC Transport (MOQT).  A subscriber can query the cache status
   of a finite Track range or request the cache status of a FETCH.
   Responses report a hit, miss, or partial hit and can identify locally
   cached ranges.
- **draft-templin-6man-aero-omni-amen-16** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-tiloca-lake-private-use-ranges-00** (new-draft, score 0, ignored_after_review) [none]: [Additional Private Use Ranges in the IANA Registries of the Lightweight Authenticated Key Exchange (LAKE) Protocol](https://datatracker.ietf.org/doc/draft-tiloca-lake-private-use-ranges/) — This document adds Private Use ranges to IANA registries that pertain
   to the Lightweight Authenticated Key Exchange (LAKE) protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the Lightweight
   Authenticated Key Exchange Working Group mailing list
   (lake@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/lake/.

   Source for this draft and an issue tracker can be found at
   https://gitlab.com/crimson84/draft-tiloca-lake-private-use-ranges.
- **draft-tuexen-tsvwg-sctp-multipath-32** (new-draft, score 0, ignored_after_review) [none]: [Load Sharing for the Stream Control Transmission Protocol (SCTP)](https://datatracker.ietf.org/doc/draft-tuexen-tsvwg-sctp-multipath/) — The Stream Control Transmission Protocol (SCTP) supports multi-homing
   for providing network fault tolerance.  However, mainly one path is
   used for data transmission.  Only timer-based retransmissions are
   carried over other paths as well.

   This document describes how multiple paths can be used simultaneously
   for transmitting user messages.
- **draft-xiao-fann-fast-cnp-with-proxy-04** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node between the congested network node and the traffic
   sender.  The proxy network node is used to translate the congestion
   notification.  The congested network node sends the congestion
   notification to the proxy network node in a format defined in this
   document, and then the proxy network node translates the received
   congestion notification to a format known by the traffic sender and
   resends the translated congestion notification to the traffic sender.
- **draft-yuyou-moq-conditional-filtering-01** (new-draft, score 0, ignored_after_review) [none]: [Conditional Range Filters for Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-yuyou-moq-conditional-filtering/) — In Media over QUIC Transport (MOQT), subscribers can use Range
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

## Errors / fetch failures

_None._
