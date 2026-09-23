# IETF Identity + AI Standards Watch

Date: 2026-09-23

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
- **draft-seymour-wimse-connected-flight-01** (new-draft, score 23, authorization) [none]: [Zero Trust Fabric Layer Agent-to-Agent Chained Trust on a Connected Flight](https://datatracker.ietf.org/doc/draft-seymour-wimse-connected-flight/) — The Zero Trust Fabric Layer (ZTFL) verified a single autonomous agent
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
- **draft-carleton-workload-authz-grant-01** (new-draft, score 22, authorization) [none]: [Workload Authorization Grant](https://datatracker.ietf.org/doc/draft-carleton-workload-authz-grant/) — This document defines the Workload Authorization Grant (WAG), by
   which a workload hosted on a platform -- an AI agent is the
   motivating case -- obtains access tokens from a third party's OAuth
   authorization server without requiring an administrator to perform a
   per-workload provisioning step.  Each workload is identified by an
   opaque identifier that is never reassigned.  The platform signs a JWT
   authorization grant ([RFC7523]) that names one workload, and the
   workload presents it at the token endpoint of an authorization server
   that has been configured, once, to trust that platform.  The
   authorization server does not reject a workload because it has not
   seen it before.  The workload's access is determined by the
   authorization server's own policy, which may consult claims the
   platform asserts about the workload.  This document covers workloads
   acting on their own behalf.  Access on behalf of a user or other
   principal is out of scope, though the grant is intended to compose
   with delegation mechanisms in which the workload is the actor.
- **draft-das-agentic-adaptive-authorization-00** (new-draft, score 22, authorization) [none]: [Adaptive Authorization for Agentic AI: Graduated and Escalated Execution Control for Critical Infrastructure](https://datatracker.ietf.org/doc/draft-das-agentic-adaptive-authorization/) — AI agents are beginning to move money, release confidential data,
   change cloud privileges, and command industrial and other critical-
   infrastructure equipment.  Existing controls answer whether an actor
   or request may proceed.  These include authentication, OAuth scopes,
   conditional access, risk engines, and attestation.  None of them,
   alone, guarantees three things about the consequence that finally
   occurs: that it is the exact act that was evaluated, that it is still
   permitted under current state, and that it cannot be replayed,
   substituted, or routed around the check.  Risk engines that return
   ESCALATE widen this gap.  The escalation is a label, and nothing
   forces the stricter conditions it implies to reach the point where
   the effect actually happens.

   This document defines Graduated and Escalated Conditional Execution
   Finality.  Every AI-generated operation is held as a non-effective
   Candidate Act. It is classified into a graduated release class rather
   than a binary allow/deny: ordinary, reduced, escalated, canary,
   sandbox, review, quarantine, or deny.  For an elevated-risk act, the
   system first derives a narrower consequence boundary.  It then binds
   the required controls into an act-bound, sink-bound Execution Handle;
   examples include a lower value, one named recipient, protected
   approval, short validity, fresh attestation, and single use.  The
   Finality Sink at the last preventable boundary re-verifies those
   controls against current protected state, atomically with
   effectuation.

   The contribution is threefold.  First, escalation changes executable
   authority, not merely a decision record.  Second, escalation is
   monotonic: it cannot be laundered, fragmented, downgraded, or
   resubmitted away on its path to the sink.  Third, the Finality Sink
   is shown to be necessary but not sufficient, so finality is an end-
   to-end property rather than a gateway.  The document specifies
   nineteen testable enforcement points, from the base execution-
   dependency mechanism to proxy, hardware, escrow, rollback,
   inheritance, and path-closure requirements.  It also provides a
   comparison with conventional mechanisms, a security model with
   explicit assumptions and invariants, a latency model, escalation-
   specific attacks, and the problems it leaves open.
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
- **draft-das-execution-finality-deployment-01** (new-draft, score 19, authorization) [none]: [Execution-Finality Architecture for AI and Autonomous Critical Systems](https://datatracker.ietf.org/doc/draft-das-execution-finality-deployment/) — AI models, agents, and autonomous services increasingly initiate
   payments, communications, data releases, infrastructure changes, and
   physical actions in critical systems.  Authentication, authorization,
   human approval, proof of possession, attestation, policy evaluation,
   and audit are important, but none of them alone establishes that the
   exact operation becoming externally effective is the operation that
   was authorized and remains permitted under current protected state.

   This document defines an execution-finality architecture in which a
   proposed operation remains non-effective until a mandatory
   enforcement function controlling the effectuation boundary
   reconstructs the actual operation, verifies exact-act binding and
   current protected state, prevents replay or stale authority, and
   couples the decision to the resulting consequence through an atomic
   or equivalently crash-consistent transition.  The document explains
   why latency is only one engineering consideration and is often not
   the dominant problem.  Consequence-path completeness, deterministic
   act representation, protected state, atomicity, crash recovery, safe
   degraded operation, and legacy-system integration are usually harder
   requirements.

   A detailed FAQ addresses whether placing OAuth at the last
   irreversible execution boundary is the same architecture.  It is not
   automatically equivalent merely because a token, scope, or sender-
   constrained proof is checked at that location.  An OAuth-protected
   implementation is functionally equivalent only when it also
   exclusively mediates every consequence path, reconstructs and binds
   all consequence-relevant fields, revalidates authoritative current
   state, enforces replay and generation controls, atomically couples
   authorization consumption to the exact effect, and provides safe
   failure and recovery semantics.  In that case, the implementation is
   functioning as the Finality Sink, regardless of terminology.  The
   document also identifies the division of responsibility and possible
   relevance of OAuth, RATS, WIMSE, Web Bot Auth, other IETF
   communities, and longer-term IRTF research.  This document is
   architectural and informational; it does not define a wire protocol.
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
- **draft-mcewan-adkm-problem-statement-00** (new-draft, score 15, adjacent_watchlist) [none]: [Autonomous Decentralized Key Management (ADKM) Problem Statement](https://datatracker.ietf.org/doc/draft-mcewan-adkm-problem-statement/) — Many Internet applications require stable, long-lived identifiers
   whose controlling cryptographic keys evolve over time.  Existing
   standards provide mature mechanisms for certification, transparency,
   self-certifying identifiers, decentralized identifiers, and shared
   consensus over state.  However, these mechanisms address different
   trust and deployment models.

   This document identifies an interoperability gap in deployments that
   require stable identifier continuity, controller-authorized key-state
   evolution, independently verifiable event histories, and consistency
   evidence without requiring either a designated administrative issuer
   to authorize each state transition or participation in a global
   consensus system.

   The document defines the problem space for Autonomous Decentralized
   Key Management (ADKM), describes related approaches, and identifies
   requirements and scope boundaries for a possible application-
   independent key-state evolution architecture.
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
- **draft-ietf-wimse-workload-identity-practices-07** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
- **draft-gilda-wimse-agent-audit-record-00** (new-draft, score 13, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-wimse-agent-audit-record/) — This document defines a record format for AI agent authorization
   decisions.  The format is one in-toto predicate type, signed inside a
   DSSE envelope.  It carries the seven minimum audit fields that the
   WIMSE AI Identity Management System framework requires, and two
   properties that make those fields checkable: a canonicalization
   contract, and both the authorization decision and the observed effect
   with a derived three-valued agreement between them.  That framework
   places the record format out of scope and takes no IANA action.  This
   document supplies the format.  It defines no policy.
- **draft-atakora-wimse-sadp-delegation-01** (new-draft, score 12, agent_identity) [none]: [Capability-Bound Delegation Chains with Scoped Context Disclosure for AI Agents](https://datatracker.ietf.org/doc/draft-atakora-wimse-sadp-delegation/) — Autonomous AI agents increasingly act on behalf of users and of one
   another, passing tasks, documents, tool access, and authority across
   chains of delegation.  Existing delegation-token systems express and
   verify attenuated authority, but they assume the delegation evidence
   and the task content are visible to the infrastructure that carries
   them.  This document specifies a capability grant format, delegation-
   chain construction and verification rules, a caveat processing model,
   and a hash-linked audit record format designed to bind authority to
   end-to-end encrypted task capsules, so that authority can be verified
   and delegation lineage can be checked relative to an authenticated
   chain head without exposing task or context plaintext to brokers,
   queues, gateways, or orchestration services.  It further specifies
   scoped context disclosure: a model in which a delegatee receives
   cryptographic access to only the subset of task context that its
   capability names.  This mechanism complements, and is intended to be
   reconcilable with, the delegation chains defined in draft-asor-wimse-
   agent-delegation-chain.
- **draft-das-accountable-autonomous-effectuation-01** (new-draft, score 12, ai_infrastructure) [none]: [AI Safety and Accountability at the Effectuation Boundary: Protocol Requirements for Autonomous Actions](https://datatracker.ietf.org/doc/draft-das-accountable-autonomous-effectuation/) — Artificial intelligence and autonomous systems are increasingly
   moving from generating information to initiating actions that
   directly affect data, services, networks, infrastructure, and
   physical systems.  At the opening of the General Debate of the 81st
   Session of the United Nations General Assembly, UN Secretary-General
   Antonio Guterres warned of "technology without accountability,"
   describing the concern further as "capability without oversight" and
   "decision-making without transparency," and called for cooperation on
   AI safety risks, testing, evaluation, transparency, and common
   safeguards.

   This document examines that problem from governance intent to
   consequence-edge verification protocols: the corresponding technical
   question is how can accountability remain enforceable at the moment a
   machine-generated decision becomes an externally consequential
   action?  It defines an effectuation-boundary problem in which a
   proposed action may be correctly authenticated and authorized
   upstream, yet the operation ultimately presented for execution may
   differ because of substitution, redirection, replay, stale authority,
   changed state, compromised intermediaries, or other causes.

   An execution-finality architecture is presented as one possible
   technical response.  A proposed operation remains non-effective until
   applicable authority and protected-state conditions are satisfied,
   and the component controlling the external consequence verifies that
   the operation actually presented for effectuation corresponds to
   currently valid authority.

   This document does not define AI governance policy, and it does not
   imply endorsement of this architecture by the United Nations or any
   other institution.  It is intended to solicit IETF discussion about
   whether effectuation-boundary accountability constitutes an
   interoperability or protocol requirement, which existing mechanisms
   can provide the required properties, and whether any additional
   standardization is necessary.
- **draft-hamr-oauth-agent-delegation-02** (new-draft, score 12, core_identity) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document builds on HTTP Message Signatures (RFC 9421) for
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
   class, r, w, or x, with an optional count per class, and a signed
   menu gives the class of each call.  This document does not define a
   credential format, an identity system, or revocation.
- **draft-helmprotocol-tttps-11** (new-draft, score 12, adjacent_watchlist) [none]: [The TLS TimeToken Secure Protocol (TTTPS)](https://datatracker.ietf.org/doc/draft-helmprotocol-tttps/) — This document specifies TTTPS, an application-layer protocol for
   evaluating temporal evidence before an application accepts an event or
   performs a related state transition.  The protocol defines a fixed
   180-byte Proof-of-Time Record v2 containing context, freshness,
   integrity, issuer-authentication, and holder-authentication fields.

   When TLS 1.3 transport binding is selected, a separate holder binding
   proof is derived from TLS exporter output and holder key material.
   The proof is sent with, but is not part of, the 180-byte record.
   The fixed-record GRG admission path is bounded with respect to peer
   count under declared frame and correction limits.

   TTTPS returns an explicit admission result before application state
   mutation.  Confidence and propagation-aware profiles are optional.
   This document does not define agent intent, audit record schemas, or
   transparency-log operation.

Discussion Note

   This document is prepared for discussion in the AUDIT BOF and related
   IETF venues. Comments should be directed through the venue selected by
   the responsible IETF process.

   Changes from -10:

   *  Clarified the 180-octet v2 layout and removed the overlapping
      reserved field.

   *  Added issuer trust-anchor and certificate resolution before issuer
      signature verification.

   *  Kept confidence and propagation processing outside the core wire and
      cryptographic verification path.

   *  Clarified the separate TLS exporter binding proof and the scope of
      the bounded single-record processing claim.

   *  Limited this revision to the core protocol; profile mathematics and
      physical-context algorithms belong in companion drafts.
- **draft-chueayen-attestation-receipts-03** (new-draft, score 11, trust_infrastructure) [none]: [Enforcement Attestation Receipts for AI Inference Decisions](https://datatracker.ietf.org/doc/draft-chueayen-attestation-receipts/) — This document specifies a compact JSON attestation receipt for an AI
   inference decision.  A receipt binds an outcome to a request hash
   under a published Ed25519 public key, so a party that does not trust
   the issuer's infrastructure can still verify offline what the
   issuer's signing key attested was decided.  The format is
   intentionally small and version-selected, so independent verifiers
   stay easy to implement and audit.  It is intended for settings where
   an operator-controlled log is not, on its own, sufficient evidence of
   the decision.
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
- **draft-sabey-succession-receipts-05** (new-draft, score 11, authorization) [none]: [Succession Receipts: Portable Signed Evidence of Authority Succession Between Autonomous Agents](https://datatracker.ietf.org/doc/draft-sabey-succession-receipts/) — Autonomous agents are upgraded, replaced, suspended, and restored
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
- **draft-atakora-sadp-protocol-02** (new-draft, score 9, agent_identity) [none]: [The Secure Agent Delegation Protocol (SADP): End-to-End Encrypted Task Capsules for AI Agent Systems](https://datatracker.ietf.org/doc/draft-atakora-sadp-protocol/) — This document specifies the Secure Agent Delegation Protocol (SADP),
   an experimental end-to-end encrypted communication layer for user-to-
   agent and agent-to-agent workflows.  SADP defines task capsules:
   signed, encrypted, individually routable protocol objects that carry
   agent tasks, tool invocations, and results across untrusted brokers,
   queues, and orchestration infrastructure.  SADP provides asynchronous
   session establishment using signed prekey bundles, per-message
   forward secrecy and post-compromise recovery through a Double-
   Ratchet-style message ratchet, an optional hybrid post-quantum key-
   agreement profile based on ML-KEM-768, and an authenticated opaque-
   broker profile with replay protection.  SADP is transport agnostic
   and is designed to be carried over HTTP, message queues, and existing
   agent protocols such as A2A and MCP without requiring those systems
   to be trusted with plaintext task content.  Capability-based
   delegation semantics and scoped context disclosure are specified in a
   companion document.
- **draft-dogru-cedulon-core-01** (new-draft, score 9, verifiable_claims) [none]: [Spend Receipts and Payment Rail Reconciliation for AI Agents](https://datatracker.ietf.org/doc/draft-dogru-cedulon-core/) — This document addresses auditable payments for AI agents and builds
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
- **draft-ietf-rats-endorsements-11** (new-draft, score 9, trust_infrastructure) [rats]: [RATS Endorsements](https://datatracker.ietf.org/doc/draft-ietf-rats-endorsements/) — In the IETF Remote Attestation Procedures (RATS) architecture, a
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
- **draft-sergeev-claim-boundaries-01** (new-draft, score 9, trust_infrastructure) [none]: [Claim Boundaries for Execution Evidence](https://datatracker.ietf.org/doc/draft-sergeev-claim-boundaries/) — Systems that act in the world produce logs, receipts, approvals,
   traces, attestations, provenance statements, and transparency
   records.  These artifacts are routinely offered as evidence that an
   action was authorized, performed, or completed.  This document states
   a discipline for bounding such claims: the strength of an execution-
   related claim is limited by what the available evidence actually
   observed, constitutes, or proves, and by the control and observation
   topology at the boundary that produced it.  Message formats,
   signature validity, receipt validity, and registration do not create
   observation or independence that did not exist.  No message format
   can supply the independent enforcement or observation dependencies
   that a prevention or adversary-resistant detection-coverage guarantee
   requires.  An appendix works through a scenario in which one party
   creates another and may be able to act in its name.  The document
   defines no protocol, no record format, and no registry.  It collects
   non-inference rules, a control-topology test for prevention and
   detection claims, a worked example, and reporting distinctions for
   evidence that does not support the claim asserted over it.
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
- **draft-marques-asqav-compliance-receipts-09** (new-draft, score 8, core_identity) [none]: [Compliance Profile of Signed Action Receipts for AI Agents](https://datatracker.ietf.org/doc/draft-marques-asqav-compliance-receipts/) — This document defines a profile for signed action receipts and
   independently checkable evidence about agent activity.  It specifies
   versioned payload and signature semantics, hash-chain linkage,
   timestamp and witness policy, receipt verification and bounded
   regulatory-evidence mappings.  It draws on ACTA-RECEIPTS but states
   its profile-specific overrides explicitly.  A receipt supports checks
   about recorded bytes, identity, linkage and retained evidence; it
   does not by itself establish that an action occurred, that all
   actions were captured, or that an organization complies with a law.
   The profile supports retained historical receipts through explicit
   version and legacy rules rather than rewriting their committed bytes.
   Its intended core and implementation limitations are described in the
   body.
- **draft-sankarshan-agent-registry-protocol-02** (new-draft, score 8, core_identity) [none]: [Agent Registry Protocol](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/) — Software agents increasingly act on behalf of people and
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
- **draft-sibiryakov-ztds-protocol-00** (new-draft, score 8, ai_infrastructure) [none]: [The Zero-Trust Data Sanitization (ZTDS) Protocol for Frontier Artificial Intelligence Ingestion](https://datatracker.ietf.org/doc/draft-sibiryakov-ztds-protocol/) — This document specifies the Zero-Trust Data Sanitization (ZTDS)
   protocol, an endpoint-native architectural framework designed to
   eliminate personally identifiable information (PII), protected
   health information (PHI), and confidential corporate credentials
   from unstructured text payloads prior to ingestion by remote Large
   Language Models (LLMs) and autonomous agents.

   ZTDS enforces strict in-memory execution within volatile Random
   Access Memory (RAM), ephemeral surrogate tokenization, tab-isolated
   session mapping, and mathematically verifiable zero network egress of
   raw identifying data.  Reversible mapping is achieved exclusively on
   the client boundary using authenticated encryption with associated
   data (AEAD), precluding intermediate cloud proxy retention, prompt
   injection extraction, and persistent vector database poisoning.
- **draft-ahuja-agent-routing-policy-00** (new-draft, score 7, authorization) [none]: [A Policy Grammar for Inter-Domain Agent Routing](https://datatracker.ietf.org/doc/draft-ahuja-agent-routing-policy/) — Agent tasks are delegated across organizational boundaries.  Existing
   work specifies how agents are identified, discovered, and described,
   states requirements for cross-domain isolation and authorization, and
   identifies the absence of a mechanism for expressing capability
   policy as a gap.  This document defines four policy attributes for
   inter-domain agent delegation, the declarations each attribute
   carries, and a validity condition on delegation chains that no party
   establishes by observing the whole chain.  Whether independently
   chosen policies converge is analysed in separate work.
- **draft-sato-agent-accountability-refarch-01** (new-draft, score 7, adjacent_watchlist) [none]: [AI Audit Reference Architecture for Post-Hoc Agent Accountability](https://datatracker.ietf.org/doc/draft-sato-agent-accountability-refarch/) — This document defines a reference architecture for producing,
   protecting, and verifying post-hoc accountability records for the
   actions of autonomous and semi-autonomous software agents, built from
   evidence captured across an action's full lifecycle -- before,
   during, and after it executes -- but assessed after the fact.  It is
   scoped exclusively to post-hoc accountability, as distinct from real-
   time enforcement, and depends on no other individual submission's
   proposed architecture: everything it requires is either an already-
   settled standard, used as published, or intended to be specified and
   released openly as the author's own work, independent of this
   document's own adoption.  It defines seven ordered stages -- intent
   and mandate capture, the agent boundary, the record producer, the
   event log and its cryptographic anchoring, a composed trust fabric,
   the disclosed audit record, and third-party verification -- together
   with two branch conditions covering cross-principal transactions and
   external resource ingestion.
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
- **draft-ietf-emu-pqc-eap-tls-02** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Enhancements to TLS-Based EAP Methods](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eap-tls/) — This document specifies the use of post-quantum cryptography in TLS-
   based EAP methods, including the Extensible Authentication Protocol
   with Transport Layer Security (EAP-TLS), EAP Tunneled TLS (EAP-TTLS),
   Protected EAP (PEAP), and EAP Tunnel Method (TEAP).  It also
   addresses challenges related to large certificate sizes and long
   certificate chains, as identified in [RFC9191], and specifies a
   mechanism to reduce TLS handshake size.
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
- **draft-ietf-mailmaint-oauth-public-06** (new-draft, score 6, authorization) [mailmaint]: [OAuth Profile for Open Public Clients](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-oauth-public/) — This document specifies a profile of the OAuth authorization protocol
   to allow for interoperability between native clients and servers
   using open protocols, such as JMAP, IMAP, SMTP, POP, CalDAV, and
   CardDAV.  The profile is restricted to native clients, that is,
   applications installed and run on the end user's device.  It
   deliberately does not support web-based clients, which cannot
   complete the flow as specified.
- **draft-abak-ai-evaluation-claim-preservation-00** (new-draft, score 5, authorization) [none]: [Claim-Preserving Exchange of AI Evaluation Evidence](https://datatracker.ietf.org/doc/draft-abak-ai-evaluation-claim-preservation/) — AI evaluation records can pass through evaluation frameworks,
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
- **draft-bryce-cose-receipts-mmr-profile-03** (new-draft, score 5, verifiable_claims) [none]: [COSE Receipts for MMRs](https://datatracker.ietf.org/doc/draft-bryce-cose-receipts-mmr-profile/) — This document defines a new verifiable data structure type for COSE
   Receipts [I-D.ietf-cose-merkle-tree-proofs] specifically for use with
   ledgers based on post-order traversal binary Merkle trees and which
   are designed for high throughput, ease of replication and
   compatibility with commodity cloud storage.

   Post-order traversal binary Merkle trees, also known as history
   trees, are more commonly known as Merkle Mountain Ranges.
- **draft-intra-handshake-fail-41** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-92701 of CVSS 9.1, CVE-2026-92702 of CVSS 9.1, CVE-2026-33697 of CVSS 7.5, and 37 other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-33697],
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
   extensibility, and review.  In our analysis, the remaining
   implementations of early attestation -- Edgeless Systems Contrast and
   Meta's AI -- remain vulnerable.
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
- **draft-oliveira-ipv7-00** (new-draft, score 5, core_identity) [none]: [IPv7: Identity-Centric Network Protocol with Verifiable Origin and Rate-Limit Tokens](https://datatracker.ietf.org/doc/draft-oliveira-ipv7/) — This document specifies IPv7, an identity-centric network protocol
   that replaces purely numerical source addressing with a hierarchical
   identity string and a Variable-Length Identity Block (VLIB).  The
   VLIB carries an Ephemeral Identity Token (EIT), provider and tenant
   identifiers, role/policy signalling, and an Origin Signature
   verifiable by the originating provider.  Validation occurs in three
   layers at the first-hop router: Origin Verification, Identity
   Verification, and Policy Enforcement.  A quantum-resistant signature
   option using CRYSTALS-Dilithium (ML-DSA-65) is incorporated.  This
   document also describes an optional local extension for Rate-Limit
   Tokens issued by ISPs and enforced in hardware.  A reference
   implementation in Rust is available as the arkhe-ipv7 and arkhe-
   ipv7-cli crates.
- **draft-ietf-plants-merkle-tree-certs-06** (new-draft, score 4, trust_infrastructure) [plants]: [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) — This document describes Merkle Tree certificates, a new form of X.509
   certificates which integrate public logging of the certificate, in
   the style of Certificate Transparency.  The integrated design reduces
   logging overhead in the face of both shorter-lived certificates and
   large post-quantum signature algorithms, while still achieving
   comparable security properties to existing X.509 constructions and
   Certificate Transparency.  Merkle Tree certificates additionally
   admit an optional size optimization that avoids signatures
   altogether, at the cost of only applying to up-to-date relying
   parties and older certificates.

## Adjacent / watchlist

- **draft-carpenter-anima-otp-casa-02** (new-draft, score 3, core_identity) [none]: [One-time Pad for Authorizing Device Identity](https://datatracker.ietf.org/doc/draft-carpenter-anima-otp-casa/) — This document describes how devices joining an autonomic control
   plane as defined in RFC 8994 may use the BRSKI onboarding mechanism
   defined in RFC 8995, even if they cannot provide a manufacturer-
   installed X.509 IDevID certificate.  Instead, such devices may
   generate a self-signed certificate embedding a unique token selected
   from a one-time pad.
- **draft-claise-green-capability-discovery-02** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
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
- **draft-helmprotocol-deepspace-01** (new-draft, score 3, trust_infrastructure) [none]: [TTTPS Deep-space Profile: Propagation-Aware Time Attestation](https://datatracker.ietf.org/doc/draft-helmprotocol-deepspace/) — This document defines an experimental deep-space profile for the TLS
   TimeToken Secure Protocol (TTTPS).  The profile preserves the Proof-
   of-Time record and cryptographic verification boundary while adding
   propagation-aware context for long and intermittent links.  It
   specifies one-way-light-time handling, epoch- and frame-bound
   physical context, relative coordinate-time conversion, peer
   projection, conservative aggregation, and explicit HOLD and
   UNVERIFIABLE outcomes.  It does not claim flight measurements, a live
   interplanetary mesh, or a replacement for CCSDS, DTN, or navigation
   standards.
- **draft-ietf-acme-dns-persist-02** (new-draft, score 3, adjacent_watchlist) [acme]: [Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation](https://datatracker.ietf.org/doc/draft-ietf-acme-dns-persist/) — This document specifies "dns-persist-01", a new validation method for
   the Automated Certificate Management Environment (ACME) protocol.
   This method allows a Certification Authority (CA) to verify control
   over a domain by confirming the presence of a persistent DNS TXT
   record containing CA and account identification information.  This
   method is particularly suited for environments where traditional
   challenge methods are impractical, such as multi-tenant hosting
   platforms, enterprise DNS environments, and IoT deployments.  The
   validation method is designed with a strong focus on security and
   robustness, incorporating widely adopted industry best practices for
   persistent domain control validation.  This design aims to make it
   suitable for Certification Authorities operating under various policy
   environments, including those that align with the CA/Browser Forum
   Baseline Requirements.
- **draft-ietf-ccamp-flexe-yang-cm-11** (new-draft, score 3, adjacent_watchlist) [ccamp]: [YANG Data Model for FlexE Management](https://datatracker.ietf.org/doc/draft-ietf-ccamp-flexe-yang-cm/) — This document defines a service provider targeted YANG data model for
   the configuration and management of a Flex Ethernet (FlexE) network,
   including FlexE group and FlexE client.
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
- **draft-ietf-ivy-network-inventory-yang-19** (new-draft, score 3, adjacent_watchlist) [ivy]: [A Base YANG Data Model for Network Inventory](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-yang/) — This document defines a base YANG data model for reporting network
   inventory.  The scope of this base model is set to be application-
   and technology-agnostic.  The base data model can be augmented with
   application- and technology-specific details.
- **draft-ietf-lamps-cms-composite-kem-03** (new-draft, score 3, adjacent_watchlist) [lamps]: [Composite ML-KEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-kem/) — Composite ML-KEM defines combinations of Module-Lattice-based Key
   Encapsulation Mechanism (ML-KEM) with RSA-OAEP, ECDH, X25519, and
   X448.  This document specifies the conventions for using Composite
   ML-KEM algorithms with the Cryptographic Message Syntax (CMS) using
   the KEMRecipientInfo structure defined in “Using Key Encapsulation
   Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)”
   (RFC 9629).
- **draft-ietf-nmop-network-incident-yang-15** (new-draft, score 3, adjacent_watchlist) [nmop]: [A YANG Data Model for Network Incident Management](https://datatracker.ietf.org/doc/draft-ietf-nmop-network-incident-yang/) — This document defines a YANG data model for the network incident
   lifecycle management.  This YANG module provides a standard way to
   report, diagnose, and help reduce troubleshooting tickets and resolve
   network incidents for the sake of network service health and probable
   root cause analysis.
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
- **draft-koo-dtn-traceroute-eb-00** (new-draft, score 3, core_identity) [none]: [Traceroute Extension Block for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-koo-dtn-traceroute-eb/) — This document defines a Traceroute Extension Block for Bundle
   Protocol Version 7 (BPv7).  The extension block provides path
   discovery and per-hop performance measurement capabilities for Delay-
   Tolerant Networks (DTNs).  Each node along the bundle's path appends
   a hop record containing its endpoint identifier, timestamp, link
   characteristics, and convergence layer information.  This enables
   comprehensive network diagnostics including path verification, delay
   analysis, link type identification, and congestion monitoring without
   requiring status reports from every intermediate node.
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
- **draft-mcewan-adkm-requirements-00** (new-draft, score 3, core_identity) [none]: [Autonomous Decentralized Key Management (ADKM) Requirements](https://datatracker.ietf.org/doc/draft-mcewan-adkm-requirements/) — This document defines the high-level functional, operational,
   security, and protocol requirements for Autonomous Decentralized Key
   Management (ADKM).  The design goal is straightforward.
   Cryptographic key state bound to a stable identifier should be able
   to begin, evolve, and be independently verified without requiring a
   central administrative authority or globally ordered consensus ledger
   to remain online and authoritative.

   These requirements establish the minimum properties for key-state
   inception, forward commitment, local evidence verification, duplicity
   detection, cryptographic agility, and transport independence.  They
   are intended to guide the standardization of ADKM data models and
   exchange protocols without prescribing a single implementation.
- **draft-toutain-schc-toward-rfc9363bis-00** (new-draft, score 3, adjacent_watchlist) [none]: [Toward RFC 9363bis: Changes to the SCHC YANG Data Model](https://datatracker.ietf.org/doc/draft-toutain-schc-toward-rfc9363bis/) — This document is not a revision of RFC 9363, "A YANG Data Model for
   Static Context Header Compression (SCHC)": it identifies changes --
   additions to, and removals from, its YANG data model -- motivated by
   discussions in the SCHC working group and by drafts published since
   RFC 9363.  These changes include more flexible compression Rule
   entries through the use of Universal Options, which allow identifiers
   to be added to or removed from a Rule Description depending on the
   Universal Options in use; some new Field Length functions, and new
   Matching Operators (MOs) and Compression/Decompression Actions
   (CDAs); and a mechanism for the manual allocation of YANG Schema Item
   iDentifiers (SIDs).  Once the working group agrees on the resulting
   wording, these changes are intended to be incorporated into a future
   revision of RFC 9363.
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
- **draft-zhang-cats-clients-request-packet-01** (new-draft, score 3, core_identity) [none]: [Carriage of CATS Service Identification and Request Constraints](https://datatracker.ietf.org/doc/draft-zhang-cats-clients-request-packet/) — This document defines a common encoding for a CATS Service Identifier
   (CS-ID) and optional client-supplied request constraints, and
   specifies two ways to carry that encoding from a client to an ingress
   CATS-Forwarder.  Mode A carries the encoding in an IPv6 Destination
   Options or Hop-by-Hop Options header.  Mode B carries the same
   encoding in an application-layer envelope whose position is
   explicitly identified by an application, API, or transport mapping,
   and which can operate over IPv4 or IPv6.

   The document specifies how a service request is identified, either by
   the destination address (e.g., a Virtual Placeholder Address (VPA),
   an anycast address, or a dedicated service address), by an explicit
   CS-ID, or by both together.  It defines the CS-ID, Network
   Constraints, and Computing Constraints TLVs and their processing at
   an ingress CATS-Forwarder, and describes how the extracted
   information is provided to the CATS Path Selector (C-PS) for service
   selection.  The mechanisms are intended for limited domains in which
   clients and CATS nodes are provisioned to use the selected mode.
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
- **draft-filsfils-srv6ops-srv6-ai-backend-05** (new-draft, score 2, ignored_after_review) [none]: [SRv6 for Deterministic Path Placement in AI Backends](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/) — This document describes how SRv6 uSID (NEXT-CSID) enables
   deterministic path placement in AI backend fabrics through L3-L4
   integration: the transport stack on the NIC encodes each path as an
   ordered list of segments (a uSID network program) in the packet
   header, while the fabric forwards statelessly.  It explains
   operational benefits including deterministic probing and alignment
   with hyperscale production deployments.
- **draft-google-cfrg-libzk-03** (new-draft, score 2, ignored_after_review) [none]: [Longfellow ZK](https://datatracker.ietf.org/doc/draft-google-cfrg-libzk/) — This document defines an algorithm for generating and verifying a
   succinct non-interactive zero-knowledge argument that for a given
   input x and a circuit C, there exists a witness w, such that C(x,w)
   evaluates to 0.  The technique here combines the MPC-in-the-head
   approach for constructing ZK arguments described in Ligero [ligero]
   with a verifiable computation protocol based on sumcheck for proving
   that C(x,w)=0.
- **draft-ietf-dnsop-delext-11** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895 and 9824.
- **draft-jackson-wimse-evaluation-00** (new-draft, score 2, ignored_after_review) [none]: [Verifier-Side Evaluation Semantics for Delegated Authority Chains](https://datatracker.ietf.org/doc/draft-jackson-wimse-evaluation/) — Delegation chain specifications describe the shape of conveyed
   authority.  They leave the verifier's half of the exchange
   underdetermined.  Two verifiers can check the same chain, both report
   success, and enforce different policy.  This document states what a
   verifier MUST do: the explicit inputs evaluation depends on, and four
   rules that keep evaluation fail-closed.  The rules are drawn from
   shipped specification text ([GAL] 0.2.6-draft, [PTC] 0.2.5-draft) and
   a public reference implementation.
- **draft-xu-idr-fare-in-sun-00** (new-draft, score 2, ai_infrastructure) [none]: [Fully Adaptive Routing Ethernet in Scale-Up Networks](https://datatracker.ietf.org/doc/draft-xu-idr-fare-in-sun/) — The Mixture of Experts (MoE) has become a dominant paradigm in
   transformer-based artificial intelligence (AI) large language models
   (LLMs).  It is widely adopted in both distributed training and
   distributed inference.  To enable efficient expert parallelization
   and even tensor parallelization across dozens or even hundreds of
   Graphics Processing Units (GPUs) in MoE architectures, an ultra-high-
   throughput, ultra-low-latency AI scale-up network (SUN) is critical.
   This document describes how to extend the Weighted Equal-Cost Multi-
   Path (WECMP) load-balancing mechanism, referred to as Fully Adaptive
   Routing Ethernet (FARE), which was originally designed for scale-out
   networks, to scale-up networks.
- **draft-yao-dawn-agent-discovery-architect-01** (new-draft, score 2, ignored_after_review) [none]: [DNS-like Agent Discovery Architecture](https://datatracker.ietf.org/doc/draft-yao-dawn-agent-discovery-architect/) — This document defines a DNS-like three-tier agent-discovery
   architecture for the Internet of Agents (IoA).  It introduces three
   core functional roles: Agent Root, Agent Registry, and Agent
   Resolver.
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
- **draft-avrilionis-satp-artefacts-registry-01** (new-draft, score 0, ignored_after_review) [none]: [Artefacts Registry](https://datatracker.ietf.org/doc/draft-avrilionis-satp-artefacts-registry/) — This memo describes the Artefacts Registry for Asset Exchange API.
   The Registry is a component that exposes an API allowing gateways to
   fetch information related to the SAT protocol.  Examples information
   stored in the Artefacts Registry are network identifiers, entities
   identifiers, asset profiles, or asset instances.  Registries are are
   acting as persistent storage locations for records.  Once registered,
   records can be updated in an append-only manner.
- **draft-avrilionis-satp-setup-stage-05** (new-draft, score 0, ignored_after_review) [none]: [SATP Setup Stage](https://datatracker.ietf.org/doc/draft-avrilionis-satp-setup-stage/) — SATP Core defines an unidirectional transfer of assets in three
   stages, namely the Transfer Initiation stage (Stage-1), the Lock-
   Assertion stage (Stage-2) and the Commitment Establishment stage
   (Stage-3).  This document defines the Setup Phase, often called
   "Stage-0", prior to the execution of SATP Core.  During Setup, the
   two Gateways that would participate in the asset transfer are bound
   together via a "transfer context".  The transfer context conveys
   information regarding the assets to be exchanged.  Gateway can
   perform any kind of negotiation based on that transfer context,
   before entering into SATP Core
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
- **draft-bertoldi-regext-rdap-reliability-scoring-04** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Structured Reliability Assessment Metadata](https://datatracker.ietf.org/doc/draft-bertoldi-regext-rdap-reliability-scoring/) — This document defines an extension to the Registration Data Access
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
- **draft-camarillo-rtgwg-lsn-01** (new-draft, score 0, ignored_after_review) [none]: [Lightspeed Notification Protocol](https://datatracker.ietf.org/doc/draft-camarillo-rtgwg-lsn/) — This document defines the Lightspeed Notification Protocol (LSN), a
   hardware-accelerated signaling mechanism designed for sub-100
   microsecond network convergence in AI/ML data center fabrics.  By
   operating entirely within the forwarding plane, LSN bypasses
   traditional CPU-based latencies to propagate link failures and
   congestion via a hardware-efficient encoding.  It serves as a high-
   speed complement to routing protocols like BGP, providing an
   immediate hardware "veto" to prune congested/failed paths while
   maintaining control-plane stability for path recovery.
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
- **draft-chuang-dkim2-sender-policy-03** (new-draft, score 0, ignored_after_review) [none]: [DKIM2 Sender Policy](https://datatracker.ietf.org/doc/draft-chuang-dkim2-sender-policy/) — This document updates DMARC RFC9989 for DKIM2.  In particular DKIM2
   verification supports MTA relay forwarding with message modifications
   through multiple MTAs, so this updates DMARC to support those
   scenarios as well.  While DMARC defines a RFC5322 From alignment
   constraint with an enforcement policy if validation fails, this
   generalizes and separates enforcement policy from constraint
   validation policies.  This provides a mechanism for MTAs to declare
   support for DKIM2 through the DMARC DNS policy record that helps
   secure DKIM2 from downgrade attacks.
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
- **draft-dreibholz-taps-neat-socketapi-19** (new-draft, score 0, ignored_after_review) [none]: [NEAT Sockets API](https://datatracker.ietf.org/doc/draft-dreibholz-taps-neat-socketapi/) — This document describes a BSD Sockets-like API on top of the
   callback-based NEAT User API.  This facilitates porting existing
   applications to use a subset of NEAT's functionality.
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
- **draft-garg-change-01** (new-draft, score 0, ignored_after_review) [none]: [Extensible Provisioning Protocol (EPP) Change Mapping](https://datatracker.ietf.org/doc/draft-garg-change/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for provisioning and management of change request objects in
   a shared central repository, where a change request is one unit of
   work that is processed by submitting to a workflow to execute the
   linked EPP transform commands in order.  The change request is a
   container with meta-data to ensure that the contained commands are
   processed as a group.
- **draft-garg-change-ext-01** (new-draft, score 0, ignored_after_review) [none]: [Change Extension Mapping for the Extensible Provisioning Protocol](https://datatracker.ietf.org/doc/draft-garg-change-ext/) — This document describes an Extensible Provisioning Protocol (EPP)
   extension of the domain name mapping and the host mapping to link
   transform commands to a change request described in the EPP Change
   Mapping.
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
- **draft-gerke-publication-process-reform-08** (new-draft, score 0, ignored_after_review) [none]: [Publication Process Reform to prevent misuse of AUTH48 or equivalent states](https://datatracker.ietf.org/doc/draft-gerke-publication-process-reform/) — This document updates the AUTH48 or equivalent process by introducing
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
- **draft-goto-otp-token-01** (new-draft, score 0, ignored_after_review) [none]: [The `OTP-Token` Email Header Field](https://datatracker.ietf.org/doc/draft-goto-otp-token/) — This document defines the OTP-Token email header field, which can be
   used to deliver One-Time Passcodes (OTP) in a machine-readable and
   origin-bound manner alongside the human-readable message carrying
   that content today.  Recipient Message User Agents (rMUA) can
   collaborate with other entities in the ecosystem to assist in the
   delivery of these codes to the context which wishes to verify their
   successful delivery.
- **draft-he-idr-bgp-ec-sr-pm-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Extended Communities for SR Policy Performance Metrics](https://datatracker.ietf.org/doc/draft-he-idr-bgp-ec-sr-pm/) — Traffic scheduling and optimization have become routine network
   operation and maintenance tasks for operators.  The operators need to
   select a path that can meet the Qality of Service (QoS) reqiurements
   of the traffic to be scheduled.

   This document defines four BGP extended communities for Segment
   Routing (SR) candidate path performance metric: the Available
   Bandwidth Extended Community, the Unidirectional Delay Extended
   Community, the Unidirectional Delay Variation Extended Community and
   the Unidirectional Loss Extended Community, which carry SR Policy
   candidate path performance parameters for the operators to select a
   preferred path for traffic scheduling and optimization.  It also
   specifies the format and processing rules for these extended
   community types.
- **draft-helmprotocol-confidence-01** (new-draft, score 0, ignored_after_review) [none]: [Oracle Confidence Gating: G-Score, Correlation-Aware von Neumann Confidence, and AdaptiveSwitch](https://datatracker.ietf.org/doc/draft-helmprotocol-confidence/) — This document specifies an optional confidence layer for the TLS
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
- **draft-housley-asn1-layman-guide-02** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This memo offers tutorial information.
- **draft-ietf-avtcore-rtp-jpegxs-3ed-08** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for ISO/IEC 21122 (JPEG XS)](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-jpegxs-3ed/) — This document specifies a Real-Time Transport Protocol (RTP) payload
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
- **draft-ietf-bier-ping-29** (new-draft, score 0, ignored_after_review) [bier]: [Bit Index Explicit Replication (BIER) Ping and Trace](https://datatracker.ietf.org/doc/draft-ietf-bier-ping/) — Bit Index Explicit Replication (BIER) is a multicast forwarding
   architecture designed to simplify and optimize multicast delivery.

   This document specifies the mechanism and basic BIER OAM packet
   format that can be used to perform failure detection and isolation on
   the BIER data plane without any dependency on other layers, like the
   IP layer.
- **draft-ietf-bmwg-sr-bench-meth-09** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Segment Routing (SR) Forwarding](https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/) — This document defines a methodology for benchmarking Segment Routing
   (SR) forwarding performance for Segment Routing over IPv6 (SRv6) and
   MPLS (SR-MPLS).
- **draft-ietf-calext-icalendar-jscalendar-extensions-08** (new-draft, score 0, ignored_after_review) [calext]: [iCalendar Format Extensions for JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-icalendar-jscalendar-extensions/) — This document defines a set of new elements for iCalendar and extends
   the use of existing ones.  Their main purpose is to extend the
   semantics of iCalendar with elements defined in JSCalendar, but the
   new definitions also aim to be useful within just the iCalendar
   format.  This document updates RFC 5545 ("iCalendar") and its
   extension documents RFC 7986 and RFC 9073.
- **draft-ietf-grow-downgrade-bgp-community-00** (new-draft, score 0, ignored_after_review) [grow]: [The DOWNGRADE BGP Community for Denial-of-Service Attack Mitigation](https://datatracker.ietf.org/doc/draft-ietf-grow-downgrade-bgp-community/) — This document outlines a method to mitigate Denial of Service (DoS)
   attacks by using a well-known BGP community named "DOWNGRADE" as
   signal to neighboring networks to treat traffic destined towards
   "DOWNGRADE" tagged IP prefixes with low precedence.  The "downgrade"
   strategy offers an appealing alternative to Remote Triggered
   Blackhole (RTBH) filtering, because RTBH filtering completes the DoS
   attack and hampers the defender's ability to monitor whether the
   attack is still ongoing.
- **draft-ietf-idr-performance-routing-07** (new-draft, score 0, ignored_after_review) [idr]: [BGP Performance-aware Routing Mechanism](https://datatracker.ietf.org/doc/draft-ietf-idr-performance-routing/) — The current Border Gateway Protocol (BGP) specification does not
   incorporate network performance metrics, such as network latency,
   into its route selection process.  This document outlines a
   performance-aware BGP routing mechanism that integrates network
   latency as a critical criterion for route selection.  This innovative
   approach is particularly beneficial for server providers with a
   global presence, enabling them to offer low-latency network
   connectivity service as a value-added service to their customers.
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
- **draft-ietf-mpls-on-path-telemetry-flag-05** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS On-Path Telemetry Network Action Flag for OAM](https://datatracker.ietf.org/doc/draft-ietf-mpls-on-path-telemetry-flag/) — This document describes postcard-based on-path telemetry with packet
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
- **draft-ietf-nfsv4-rfc8881bis-11** (new-draft, score 0, ignored_after_review) [nfsv4]: [Network File System (NFS) Version 4 Minor Version 1 Protocol](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-rfc8881bis/) — This document describes the Network File System (NFS) version 4 minor
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
- **draft-ietf-openpgp-external-secrets-00** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP External Secret Keys](https://datatracker.ietf.org/doc/draft-ietf-openpgp-external-secrets/) — This document defines a standard wire format for indicating that the
   secret component of an OpenPGP asymmetric key is stored externally,
   for example on a hardware device or other comparable subsystem.
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
- **draft-ietf-pim-ipv6-zeroconf-assignment-12** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the criteria listed in RFC 10019.
- **draft-ietf-pim-rfc8059-9798bis-02** (new-draft, score 0, ignored_after_review) [pim]: [PIM Join Attributes for Locator/ID Separation Protocol (LISP) Environments](https://datatracker.ietf.org/doc/draft-ietf-pim-rfc8059-9798bis/) — This document defines two PIM Join/Prune attributes that support the
   construction of multicast distribution trees where the root and
   receivers are located in different Locator/ID Separation Protocol
   (LISP) sites.  These attributes allow the receiver site to select
   between unicast and multicast underlying transport, to convey the
   RLOC (Routing Locator) address of the receiver ETR (Egress Tunnel
   Router) to the control plane of the root ITR (Ingress Tunnel Router)
   and to signal the underlay multicast group to the control plane of
   the root ITR.  This document updates RFC 8059 and RFC 9798.
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
- **draft-lcurley-moq-cluster-01** (new-draft, score 0, ignored_after_review) [none]: [MoQ Cluster Extension](https://datatracker.ietf.org/doc/draft-lcurley-moq-cluster/) — This document defines a clustering extension for MoQ Transport
   [moqt], used to build a mesh of relays.  Each namespace advertisement
   carries the list of Hop IDs it has passed through, starting with the
   original publisher, and the accumulated cost of that path.  A
   receiver uses the list to detect loops and to tell which
   advertisements come from the same publisher, and the cost to choose
   between paths.  Each endpoint declares its own Hop ID at setup, so a
   peer never advertises or serves it a path that already passed through
   it.
- **draft-li-rttp-intent-addressing-01** (new-draft, score 0, ignored_after_review) [none]: [Intent Addressing in the rttp URI Scheme](https://datatracker.ietf.org/doc/draft-li-rttp-intent-addressing/) — This document specifies the "rttp" URI scheme.  An "rttp" URI names a
   claim of intent directed at an identified subject; the address of
   that subject is derived by computation from the URI authority, and no
   lookup service, registry, or name-resolution system is consulted at
   resolution time.  The document also states the requirements a client
   MUST satisfy when it handles such a URI, in order to avoid two
   failure modes that short, user-embeddable strings otherwise invite:
   using the authority as a navigation target (open redirect), and using
   a registered protocol handler as a general-purpose launcher.
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
- **draft-liu-add-dnssd-edns-04** (new-draft, score 0, ignored_after_review) [none]: [DNS-Based Service Discovery for Encrypted DNS Services](https://datatracker.ietf.org/doc/draft-liu-add-dnssd-edns/) — This document defines a DNS-Based Service Discovery (DNS-SD)
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
- **draft-liu-fann-srv6-cc-01** (new-draft, score 0, ignored_after_review) [none]: [Congestion Control Based on SRv6 Path](https://datatracker.ietf.org/doc/draft-liu-fann-srv6-cc/) — This document describes a congestion control solution based on SRv6.
   It defines mechanisms for congestion notification and flow control
   within an SRv6-based network, optimizing congestion handling through
   hierarchical congestion control messages along SRv6 paths.
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
- **draft-ramakrishna-satp-data-sharing-06** (new-draft, score 0, ignored_after_review) [none]: [Protocol for Requesting and Sharing Views across Networks](https://datatracker.ietf.org/doc/draft-ramakrishna-satp-data-sharing/) — With increasing use of DLT (distributed ledger technology) systems,
   including blockchain systems and networks, for virtual assets, there
   is a need for asset-related data and metadata to traverse system
   boundaries and link their respective business workflows.  Systems and
   networks can define and project views, or asset states, outside of
   their boundaries, as well as guard them using access control
   policies, and external agents or other systems can address those
   views in a globally unique manner.  Universal interoperability
   requires such systems and networks to request and supply views via
   gateway nodes using a request-response protocol.  The endpoints of
   this protocol lie within the respective systems or in networks of
   peer nodes, but the cross-system protocol occurs through the systems’
   respective gateways.  The inter-gateway protocol that allows an
   external party to request a view by an address and a DLT system to
   return a view in response must be DLT-neutral and mask the internal
   particularities and complexities of the DLT systems.  The view
   generation and verification modules at the endpoints must obey the
   native consensus logic of their respective networks.
- **draft-ramakrishna-satp-views-addresses-08** (new-draft, score 0, ignored_after_review) [none]: [Views and View Addresses for Secure Asset Transfer](https://datatracker.ietf.org/doc/draft-ramakrishna-satp-views-addresses/) — With increasing use of DLT (distributed ledger technology) systems,
   including blockchain systems and networks, for virtual assets, there
   is a need for asset-related data and metadata to traverse system
   boundaries and link their respective business workflows.  Core
   requirements for such interoperation between systems are the
   abilities of these systems to project views of their assets to
   external parties, either individual agents or other systems, and the
   abilities of those external parties to locate and address the views
   they are interested in.  A view denotes the complete or partial state
   of a virtual asset, or the output of a function computed over the
   states of one or more assets, or locks or pledges made over assets
   for internal or external parties.  Systems projecting these views
   must be able to guard them using custom access control policies, and
   external parties consuming them must be able to verify them
   independently for authenticity, finality, and freshness.  The end-to-
   end protocol that allows an external party to request a view by an
   address and a DLT system to return a view in response must be DLT-
   neutral and mask the interior particularities and complexities of the
   DLT systems.  The view generation and verification modules at the
   endpoints must obey the native consensus logic of their respective
   systems.
- **draft-rzz-rtgwg-inter-domain-ebr-00** (new-draft, score 0, ignored_after_review) [none]: [BGP-based Inter-domain Elastic Bandwidth-aware Routing Framework](https://datatracker.ietf.org/doc/draft-rzz-rtgwg-inter-domain-ebr/) — Although operators typically consider redundant capacity during
   network design, link congestion may still occur under specific
   scenarios, such as link degradation or traffic bursts.  Several
   congestion mitigation mechanisms have been proposed for intra-domain
   links, but congestion is not limited to intra-domain links, it can
   also occur on inter-domain links.

   Since changes of available bandwidth do not trigger updates to BGP
   route selection, BGP cannot alleviate inter-domain link congestion
   automatically, causing packet loss or increased delay.

   This document defines a BGP-based inter-domain elastic bandwidth-
   aware routing (BEBR) mechanism, to alleviate inter-domain link
   congestion.  To avoid the dependency on cross-domain deployment, this
   document proposes both inbound BEBR and outbound BEBR, designed to
   address inbound and outbound traffic congestion, respectively.  Thus,
   the congestion on both directions of inter-domain links can be
   mitigated by deploying BEBR on only one side of the inter-domain
   link.
- **draft-salaheldin-bcnp-00** (new-draft, score 0, ignored_after_review) [none]: [Brain Control Network Protocol (BCNP)](https://datatracker.ietf.org/doc/draft-salaheldin-bcnp/) — The Brain Control Network Protocol (BCNP) is a binary, TCP-based
   application-layer protocol for discovering, configuring, and
   commanding networked devices from a single controller using a small,
   fixed vocabulary of discrete control inputs, such as those produced
   by a brain-computer interface.  A Controller establishes a private
   wireless network that Devices join, discovers Devices and assigns
   each a persistent address, discovers and registers the Actions a
   Device can perform, and subsequently issues short, stateless
   commands, expressed through that same small input vocabulary, to
   elicit those Actions.  This document specifies BCNP's binary message
   formats, its Discovery, Pairing, and Command phases, and the
   reconciliation mechanism used to recover from lost acknowledgments
   and Devices that change network address.
- **draft-song-lamps-pq-composite-frodokem-00** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-song-lamps-pq-composite-frodokem/) — Composite FrodoKEM defines combinations of FrodoKEM with RSA-OAEP,
   ECDH, X25519, and X448.  This document specifies the algorithm
   definitions, key formats, and certificate conventions for using
   Composite FrodoKEM in the X.509 Public Key Infrastructure.
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
- **draft-tt-netmod-yang-config-templates-04** (new-draft, score 0, ignored_after_review) [none]: [YANG Configuration Templates](https://datatracker.ietf.org/doc/draft-tt-netmod-yang-config-templates/) — This document defines a YANG-based configuration template mechanism
   whereby repetitive configuration data can be factored out into
   templates and applied where needed.  This avoids the redundant
   definition of identical configuration and ensures the consistency of
   it, thus allowing configuration data to be managed more conveniently
   and efficiently.
- **draft-wang-idr-flowspec-dip-origin-as-filter-14** (new-draft, score 0, ignored_after_review) [none]: [Destination-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-dip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification (FlowSpec) to enable filtering based on the
   Origin Autonomous System (AS) of the destination IP address.  This
   extension is particularly useful in mitigating Distributed Denial of
   Service (DDoS) attacks or optimizing traffic redirection where the
   target IP addresses are numerous or rapidly changing, but belong to a
   specific destination Origin AS.
- **draft-wang-idr-flowspec-sip-origin-as-filter-02** (new-draft, score 0, ignored_after_review) [none]: [Source-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-sip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification (FlowSpec) to enable filtering based on the
   Origin Autonomous System (AS) of the source IP address.  This
   extension is particularly useful in mitigating Distributed Denial of
   Service (DDoS) attacks where the source IP addresses are dynamic or
   numerous but belong to a specific source AS.
- **draft-xiao-fann-fast-cnp-with-proxy-04** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification Packet (CNP) with Proxy](https://datatracker.ietf.org/doc/draft-xiao-fann-fast-cnp-with-proxy/) — This document describes the necessity and feasibility to introduce a
   proxy network node between the congested network node and the traffic
   sender.  The proxy network node is used to translate the congestion
   notification.  The congested network node sends the congestion
   notification to the proxy network node in a format defined in this
   document, and then the proxy network node translates the received
   congestion notification to a format known by the traffic sender and
   resends the translated congestion notification to the traffic sender.
- **draft-xsaopig-nmop-service-flow-modal-mapping-06** (new-draft, score 0, ignored_after_review) [none]: [Architecture for Service Flow Characteristics and Modal Mapping Based on SDN and ALTO Protocol](https://datatracker.ietf.org/doc/draft-xsaopig-nmop-service-flow-modal-mapping/) — This Internet-Draft specifies a comprehensive framework for mapping
   service flow characteristics to network modal resources in multi-
   modal intelligent computing networks.  It introduces the use of the
   ALTO protocol for collecting service flow data and leverages an SDN
   architecture to separate control and data planes.  The ALTO protocol
   facilitates the acquisition of diverse network state information,
   including data from several SDN domains and dynamic network
   environments, directly from controllers while keeping the provider's
   internal details confidential.  It then transmits the controller's
   decisions using a proven method.  The document details methods for
   characteristic identification, intelligent mapping, and continuous
   optimization, enabling dynamic resource allocation and improved
   network performance.  The framework is designed to support scalable,
   efficient, and secure operations in environments with complex network
   loads and diverse service requirements.
- **draft-xu-idr-neighbor-autodiscovery-14** (new-draft, score 0, ignored_after_review) [idr]: [BGP Neighbor Discovery](https://datatracker.ietf.org/doc/draft-xu-idr-neighbor-autodiscovery/) — BGP is being used as the underlay routing protocol in some large-
   scaled data centers (DCs).  Most popular design followed is to do
   hop-by-hop external BGP (EBGP) session configurations between
   neighboring routers on a per link basis.  The provisioning of BGP
   neighbors in routers across such a DC brings its own operational
   complexity.

   This document introduces a BGP neighbor discovery mechanism that
   greatly simplifies BGP operations in such DC and other networks by
   automatic setup of BGP sessions between neighbor routers using this
   mechanism.

## Errors / fetch failures

_None._
