# IETF Identity + AI Standards Watch

Date: 2026-09-15

## Read now

- **draft-das-execution-finality-enforcement-profiles-01** (new-draft, score 38, trust_infrastructure) [none]: [Execution Finality at External-Effect Boundaries: Enforcement Profiles for 6G, AI-Native RAN, RF, ISAC, Accelerated Compute, Devices, and Autonomous Systems](https://datatracker.ietf.org/doc/draft-das-execution-finality-enforcement-profiles/) — AI-native and autonomous infrastructure is increasingly able to
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
- **draft-das-rats-attestation-bnd-execution-finality-04** (new-draft, score 35, authorization) [none]: [Attestation-Bound Execution Finality for GPU, AI Accelerator, DPU, SmartNIC, and Confidential-Computing Infrastructure](https://datatracker.ietf.org/doc/draft-das-rats-attestation-bnd-execution-finality/) — Remote attestation can establish that a CPU, confidential virtual
   machine, GPU, AI accelerator, DPU, or SmartNIC is running expected
   firmware and software in an expected configuration.  However, an
   acceptable Attestation Result describes the execution environment,
   not the operations it later emits; it remains the same whether
   subsequent workload outputs arise from expected logic, prompt
   injection, or model error.  As AI workloads become agentic and move
   onto confidential accelerator infrastructure, they emit high-
   consequence operations, such as financial transfers, cloud-control
   mutations, database deletions, and external API invocations, where
   platform trustworthiness alone cannot determine whether a concrete
   operation is authorized to take effect.  OAuth access tokens,
   transaction tokens, and workload credentials do not close this gap on
   their own: they typically authorize by scope and by possession of a
   credential rather than by the exact content of one operation, and
   they do not require that the protected effect be unreachable except
   through a verifying boundary.

   This document describes an attestation-bound execution-finality
   architecture that bridges platform appraisal and consequence-bearing
   authorization.  A consequential operation originates in a non-
   effective state as a Candidate Act.  An Execution-Finality Validator
   evaluates the act's security-relevant arguments together with the
   platform's Attestation Result, workload identity, and policy, and
   issues an act-bound, single-use, non-bearer Execution Handle.  A
   Finality Sink verifies that handle at the non-bypassable boundary
   where the operation would first acquire external effect, so that an
   authorized act cannot be swapped, mutated, or replayed.

   The architecture requires no changes to silicon, microcode, firmware,
   drivers, or accelerator programming models, and it separates
   concerns: platforms such as NVIDIA confidential-computing GPUs and
   BlueField DPUs, Arm Confidential Compute Architecture (CCA), AMD SEV-
   SNP, and Intel TDX supply environment appraisal on the cold path,
   while enforcement is placed at the gateway, service-mesh, DPU or
   SmartNIC, network, or storage boundary.  On the hot path,
   verification uses local cryptographic bindings and single-use checks
   rather than repeated attestation round trips.  The document discusses
   its relationship to RATS, WIMSE, OAuth, and related IETF work, and
   its engineering FAQ addresses platform layering, DPU visibility under
   end-to-end encryption, tail latency, and other anticipated critical
   questions.  It is intentionally long because it is explanatory rather
   than a protocol specification.

   The architecture is implemented, not only described.  An executable
   reference implementation (GitHub: reference implementation, tests,
   benchmarks, and deployment materials, https://github.com/sangmdas/
   Execution-Finality-for-GPU-AI-Accelerators-and-Confidential-
   Workloads) demonstrates act binding, single-use enforcement, and
   replay rejection in running code.  It uses a software-only attester;
   it has not been run on any vendor's confidential-computing hardware
   and does not consume any vendor-issued attestation token, and vendor
   platforms are discussed on the basis of public documentation only.
   This document is vendor-neutral, neither claims nor implies review,
   adoption, endorsement, or affiliation by any named vendor, and
   complements rather than replaces existing attestation, workload-
   identity, and authorization mechanisms.
- **draft-das-eu-ai-act-execution-enforcement-02** (new-draft, score 31, adjacent_watchlist) [none]: [Technical Enforcement of the EU AI Act and Global AI Laws for High-Risk AI Systems Without Relying on Paper Policies](https://datatracker.ietf.org/doc/draft-das-eu-ai-act-execution-enforcement/) — This architecture is specifically designed for high-risk AI systems,
   where standard engineering priorities shift from speed and latency
   toward absolute determinism and safety.

   The European Union Artificial Intelligence Act establishes an
   extensive paper-based governance regime for artificial intelligence:
   risk-management documentation, data-governance records, conformity
   assessments, human-oversight instructions, transparency notices,
   logging obligations, and post-market monitoring plans.  These
   instruments are necessary, and this document does not propose to
   discard them.  They are not, however, sufficient by themselves once
   an AI system can autonomously or semi-autonomously act at machine
   speed, because a document can only describe what an operation should
   do; it cannot, by itself, make an operation technically incapable of
   doing otherwise.

   This is not a problem unique to the European Union.  South Korea's AI
   Basic Act regulates "high-impact AI" through comparable risk-
   management, human-oversight, and documentation duties.  Japan's AI
   Act, in force since September 2025, takes a lighter, more promotion-
   oriented approach but still assumes that written governance is the
   primary control.  China enforces a binding but differently structured
   set of algorithm-recommendation, deep-synthesis, generative-AI, and
   AI-content-labelling rules.  Texas and Colorado have each enacted
   state-level AI statutes in the United States with disclosure and
   consequential-decision obligations, and Brazil's PL 2338/2023 and
   Canada's lapsed AIDA proposal show the same EU-style risk-based model
   spreading, whether or not yet enacted.  Every one of these regimes,
   whatever their legal differences, shares the identical underlying
   engineering gap this document addresses: a written rule, however well
   drafted, does not by itself make a machine unable to break it before
   anyone can react.

   The gap is most consequential precisely where the stakes are highest.
   In defence-relevant AI, critical-infrastructure control systems, and
   satellite or space-system automation, an autonomous agent can select
   a target, reroute power or water, transfer control of a physical
   asset, or transmit a command to an orbital platform within a single
   inference cycle -- before any operator, reviewer, regulator, or
   after-the-fact investigation can intervene.  If that act causes harm,
   two questions follow immediately: who is liable, and at what cost.  A
   risk-management file, a conformity-assessment certificate, or an
   audit log written after the fact can show that a rule existed; none
   of them can show that the machine was technically incapable of
   breaking it, and none of them limits the cost already incurred by the
   time the record is examined.  For these classes of system, the
   appropriate default when an authorization cannot be verified is not
   "log it and investigate later"; it is fail-closed: the act simply
   does not occur.

   This document describes an execution-finality architecture that
   converts a selected, already-determined AI-governance requirement
   from a document into a mandatory, machine-verifiable precondition of
   the AI-generated operation itself.  A consequential AI-generated
   operation is first represented as a Candidate Act and is held in a
   Non-Effective State -- technically incapable of invoking a tool,
   actuating a device, transmitting a command, or otherwise causing an
   external consequence -- until a Protected Enforcement Domain
   validates the machine-readable constraints applicable to that exact
   act, including the AI system identity, permitted operation, target,
   recipient, destination, required human-oversight state, transparency
   marker, risk-control status, policy epoch, and revocation state.
   Successful validation produces narrowly scoped, act-bound
   effectuation authority; a Finality Sink positioned at the point of
   first usable external effect independently re-verifies that exact
   authority, and the current required state, immediately before the
   consequence is permitted to occur.  Absent, stale, revoked, or
   unverifiable authority results by default in no effect, not in a
   warning.  The same architecture accepts a jurisdiction-specific
   governance profile as an input, so that an EU AI Act profile, a
   Korean AI Basic Act profile, or another national profile can each
   supply the machine-readable constraints for the identical enforcement
   mechanism without this document taking a position on how those laws
   relate to one another.

   This document does not determine whether an AI system is legally
   high-risk under Annex III, whether a practice is prohibited under
   Article 5, whether a conformity assessment is valid, whether human
   oversight under Article 14 is legally sufficient, or whether an
   organisation complies with the Regulation as a whole, nor does it
   make any equivalent determination under another jurisdiction's law.
   Those determinations remain outside the protocol and must be made by
   the responsible legal, regulatory, or organisational authority.  This
   document addresses the narrower engineering problem that arises only
   after such a determination has already been made: once an applicable
   governance requirement has been translated into a machine-readable
   constraint, how can satisfaction of that constraint be made
   technically necessary before the corresponding AI-generated
   consequence becomes effective?

   This document does not advocate replacing paper-based AI governance
   for general-purpose or low-consequence AI applications, where the
   cost and rigidity of execution-level enforcement would be
   disproportionate to the risk.  The architecture is proposed
   specifically for high-criticality AI deployments -- defence and dual-
   use systems, critical infrastructure, satellite and space systems,
   and comparably consequential autonomous or agentic systems -- in
   which an unauthorised act is not merely a compliance finding but a
   matter of physical safety, national security, or irreversible loss,
   and in which liability and cost must be bounded by making the
   unauthorised act technically non-completable rather than merely
   detectable afterward.

   Cross-regime use is treated as a profile-input problem rather than as
   legal harmonisation.  An EU AI Act profile, a South Korean AI Basic
   Act profile, a Japanese AI Act profile, or another national,
   sectoral, or contractual profile can each supply machine-readable
   constraints to the same Candidate Act / Protected Enforcement Domain
   / Finality Sink mechanism.  Where profiles are compatible, the
   effective authority is their intersection; where they conflict, the
   act remains unauthorised by default pending an external legal or
   organisational determination.  That is the maximum interoperability
   claim this document makes: a shared enforcement substrate, not
   equivalence of laws, not a conflict-of-law solver, and not a finding
   that any listed regime is legally sufficient or interchangeable.

   A primary public reference implementation accompanies this document
   at https://github.com/sangmdas/Execution-Finality-Technical-
   Enforcement-for-EU-AI-Act-and-AI-Governance-Constraints
   (https://github.com/sangmdas/Execution-Finality-Technical-
   Enforcement-for-EU-AI-Act-and-AI-Governance-Constraints).  It is a
   runnable engineering reference for the substrate and selected AI-
   governance predicates (human-approval binding, runtime evidence,
   delegation bounds, bounded offline mode, policy-epoch revocation, and
   profile intersection).  It is not a legal-compliance product, not a
   certification, and not evidence that any deployment using it complies
   with the EU AI Act or another law.

   Reviewer questions that recur in this series -- cross-regime
   generalisation, deterministic runtime bounds for dynamic agentic
   plans, interaction with Article 14 human oversight, and audit
   responsibility -- are collected as frequently asked questions in
   Section 43.  Trust-boundary, insider-approval, sink-failure,
   delegation, liability, and residual-limitation questions are treated
   as a threat model and operational caveat set in Section 44 and
   Section 38.  Those sections state what the architecture can and
   cannot claim.  Independent technical and legal criticism is invited;
   the author would rather have the limits of execution-finality found
   in review than have them discovered after a protected effect has
   already occurred.
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
- **draft-helixar-hdp-agentic-delegation-02** (new-draft, score 27, agent_identity) [none]: [Human Delegation Provenance Protocol (HDP): Cryptographic Chain-of-Custody for Agentic AI Systems](https://datatracker.ietf.org/doc/draft-helixar-hdp-agentic-delegation/) — Agentic AI systems operate on behalf of human principals, often
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
   action as a signed hop in an append-only chain, and enables any
   participant to verify the full provenance record using only the
   issuer's Ed25519 public key and the current session identifier.
   Verification is fully offline.  No registry lookup, no network call,
   and no third-party trust anchor is required.

   HDP's distinguishing contribution is a signed, tamper-evident record
   of each agent's declared action at each hop, an execution audit trail
   that complements, rather than replaces, capability-based delegation
   formats such as UCAN and ZCAP-LD.  The underlying append-only,
   offline-verifiable chain-of-custody mechanism is payload-agnostic;
   human-authorized agentic delegation is the reference profile
   specified in this document.

   HDP is not an authorization protocol.  An HDP token confers no
   authority and its presentation entitles the presenter to nothing.  It
   is a record of who authorized a task and of what each agent declared
   it did with that authorization, carried with the task and read at
   audit.
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
- **draft-das-ai-factory-silicon-finality-01** (new-draft, score 24, trust_infrastructure) [none]: [Execution Finality for AI-Factory Silicon and Accelerated Infrastructure: Enforcement Profiles for GPUs, Chiplets, Memory Fabrics, DPUs, RDMA, CXL, and Photonic Boundaries](https://datatracker.ietf.org/doc/draft-das-ai-factory-silicon-finality/) — AI factories and AI-native network infrastructure are becoming
   heterogeneous hardware systems rather than isolated model-serving
   applications.  A single consequential operation may traverse CPU
   control planes, GPUs or NPUs, high-bandwidth memory, chiplets,
   coherent memory fabrics, CXL or PCIe paths, IOMMUs, DMA and RDMA
   engines, SmartNICs or DPUs, accelerator fabrics, model-serving
   runtimes, optical interconnects, storage systems, and physical power
   or cooling controllers.  At these layers, a computation can be valid
   and a component can be authenticated while the resulting tensor
   transfer, memory exposure, queue activation, model load, routing
   change, optical emission, partition transition, firmware update, or
   physical actuation is still not authorized to become effective.

   This document describes a silicon-oriented execution-finality
   architecture for preserving that distinction.  A consequential
   hardware or infrastructure operation is represented as a Candidate
   Act and remains in a Non-Effective State until a Protected
   Enforcement Domain establishes a machine-verifiable act descriptor,
   validates applicable authority predicates, updates or consumes
   protected state, and commits Protected Validation Evidence.  A scoped
   non-bearer capability is then bound to the exact Candidate Act,
   relevant descriptor or digest, protected evidence, protected state,
   freshness and policy conditions, permitted scope, execution-finality
   boundary, and applicable Finality Sink.  Possession of the capability
   alone is insufficient.

   The Finality Sink is the hardware, firmware, protected-runtime,
   fabric, controller, or adjacent enforcement role that has mandatory
   control over the consequence.  Depending on the profile, it may be a
   memory controller, HBM gate, GPU scheduler, accelerator partition
   controller, IOMMU or SMMU, DMA or RDMA engine, DPU or SmartNIC,
   fabric switch, chiplet link controller, CXL component, cache-
   coherence controller, model loader, token-emission gate, optical
   modulator or wavelength controller, eFPGA configuration gate, rack
   power controller, or another protected effectuation point.  The
   Candidate Act becomes effective only after sink-local verification
   confirms that the actual pending operation still corresponds to the
   validated act and current protected state.

   The document provides 83 detailed Enforcement Profiles.  Sixty-three
   translate the supplied GPU, silicon, chiplet, memory-fabric, and AI-
   factory source set; twelve supplementary profiles map the same
   execution-finality model onto current hyperscale and Arm-based
   infrastructure directions; and eight additional profiles selectively
   adapt non-duplicative mechanisms from the companion DAS Protocols V,
   VI, and VIII disclosures for silicon and AI-factory use.  The
   catalogue covers GPU and accelerator egress, rack-scale AI fabrics,
   sparse expert routing, coherent and disaggregated memory, collective
   communication, DPUs and SmartNICs, RDMA and GPU-direct access, model
   and KV-cache lifecycle state, accelerator partitioning, arithmetic-
   mode control, AI-factory scheduling, storage, telemetry, firmware,
   power and cooling, digital-twin actuation, in-network compute,
   federated-learning egress, neural-waveform release, silicon
   photonics, optical lanes and wavelengths, chiplet admission and UCIe
   control, CXL memory pools, RAS and memory quarantine, eFPGA
   configuration, reconfigurable optical accelerator topologies,
   accelerator-pod membership, compiler-to-silicon executable
   activation, confidential-realm memory ownership, secure device
   attachment, coherent-mesh admission, confidential offload-device
   attachment, network and storage offload queues, isolated management-
   controller actions, host-independent cloud-offload actions,
   UltraServer-scale accelerator-fabric membership, distributed EFA/RDMA
   endpoint admission, protected neural-state proofs, hardware-isolated
   shadow auditing, cross-committed collection-time and execution-time
   validation, attested measurement paths, distributed partial-share
   finality, separate compute-enable and produced-output authority,
   output-derived digest binding, and effectuation-enabling-resource
   withholding.  Profile identifiers retain the source numbering for
   traceability; gaps are intentional.

   The architecture is intended to complement, not replace, existing
   work in accelerated computing, AI networking, confidential computing,
   chiplet and coherent-memory systems, accelerator fabrics, optical I/
   O, attestation, authorization, and hardware isolation.  In
   particular, the profiles are directly relevant to public technology
   directions associated with NVIDIA, AMD, Intel, Google, Amazon Web
   Services (AWS), Microsoft, Broadcom, Marvell, and Arm, whose current
   infrastructure spans GPUs and AI accelerators, custom AI silicon,
   high-bandwidth memory, CPU-to-accelerator coherence, chiplets, CXL
   and PCIe-class fabrics, DPUs and infrastructure offload, RDMA and
   high-speed AI networking, rack-scale accelerator systems, optical and
   silicon-photonic interconnects, hardware roots of trust, and large-
   scale AI-factory orchestration.  Additional industry relationships
   with Qualcomm, Meta, Cisco, HPE, Nokia, Ericsson, Samsung, Huawei,
   AT&T, Verizon, Orange, and Deutsche Telekom are discussed in the body
   of the document where AI-native networking, RAN, 6G, edge compute,
   and operator-controlled infrastructure create related effectuation
   boundaries.  These references identify technical complementarity and
   possible enforcement locations; they do not imply that any named
   organization has reviewed, endorsed, adopted, or lacks equivalent
   mechanisms.

   The IETF relevance is principally the cross-layer security
   relationship among identity, attestation, evidence, cryptographic
   binding, workload authorization, protected state, replay resistance,
   delegation, and the final effectuation boundary.  The hardware
   protocols themselves remain within the remit of the appropriate
   hardware, semiconductor, telecommunications, optical, and system
   standards bodies.  The common invariant is: computation may produce a
   Candidate Act, but computation is not authority for consequence.
- **draft-das-execution-finality-protocol-layer-01** (new-draft, score 23, core_identity) [none]: [The Missing Protocol Layer for the Agentic Internet: Computation Is Not Authority](https://datatracker.ietf.org/doc/draft-das-execution-finality-protocol-layer/) — TLS tells you the channel is authentic.  OAuth tells you the caller
   holds a valid grant.  HTTPS tells you the origin is who it claims to
   be.  EMV tells you a payment cryptogram is transaction-specific.
   None of these mechanisms answer a question that autonomous, machine-
   speed systems now raise on every turn: is _this specific act_,
   generated by _this_ model, agent, or workload, at _this_ moment,
   actually authorized to become externally effective?

   Large language model agents, autonomous cloud workloads, and machine-
   to-machine network functions increasingly compute, decide, and act
   inside a single event loop, at latencies where no human, log
   reviewer, or downstream audit process can intervene before an API
   call fires, a payment settles, a file leaves the enterprise boundary,
   or a physical actuator moves.  Transport, authentication, and
   authorization protocols were designed for a world in which the gap
   between "this request was generated" and "this request had a chance
   to be reviewed" was measured in human-relevant time.  That gap has
   collapsed to milliseconds.  Existing protocol layers were never built
   to close it, because the question they answer -- identity, channel
   integrity, delegated scope -- is a necessary but categorically
   different question from whether _this act, right now, should be
   allowed to leave computation and become consequence_.

   This document specifies an architectural pattern, execution finality,
   that treats every machine-generated operation as a Candidate Act held
   in a Non-Effective State until a Protected Enforcement Domain
   validates act-specific authority -- purpose, destination,
   jurisdiction, freshness, revocation state, policy epoch, and runtime
   integrity -- and issues a narrowly scoped, non-bearer Execution
   Handle bound to that act and to a specific Finality Sink, the first
   boundary at which the act would otherwise become externally
   effective.  The document formalizes the vocabulary, a cold-path/hot-
   path split for latency-sensitive deployment, a structured threat
   model with adversary-facing pseudocode, an incremental migration path
   for coexistence with TLS, HTTPS, OAuth, and EMV rather than
   replacement of them, and worked examples spanning AI agents,
   payments, telecommunications, cloud infrastructure, satellite
   command, industrial control, and robotics.

   The central claim is narrow and falsifiable: _computation does not
   itself confer authority for consequence_, and no general, cross-
   domain Internet layer currently makes that separation a structural
   property of the release path rather than an application-specific
   convention.  This document is intended to solicit IETF community
   review of whether that gap is real, whether it is already covered by
   existing or in-progress work, and if not, which venue should take it
   up.

   This document describes a patent-pending architectural concept.  Any
   intellectual-property rights or disclosure obligations relating to
   implementation are outside the technical scope of this document and
   are subject to applicable IETF IPR procedures, including BCP 79.
- **draft-das-enterprise-ai-enforcement-profiles-00** (new-draft, score 21, authorization) [none]: [Securing the Enterprise Future: Technical Non-Joinability for Enterprise AI](https://datatracker.ietf.org/doc/draft-das-enterprise-ai-enforcement-profiles/) — Enterprise artificial-intelligence systems are increasingly connected
   to multiple organizational repositories, applications, tools, memory
   systems, and workflow interfaces.  Representative industrial
   deployment classes include OpenAI ChatGPT and ChatGPT Work, Anthropic
   Claude, Google Gemini Enterprise, xAI Grok for Business, Microsoft
   Copilot and Copilot Studio, Amazon Q Business, Salesforce Agentforce,
   ServiceNow AI Agents, and comparable enterprise or privately deployed
   AI systems.  These names are cited only as publicly described
   examples of the broader deployment class.  Their inclusion does not
   assert that any named product implements, lacks, requires, infringes,
   endorses, or is vulnerable to the mechanisms described here, does not
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
- **draft-mcgraw-httpapi-agent-budget-04** (new-draft, score 21, verifiable_claims) [none]: [The Delegation HTTP Authentication Scheme for Request-Bound Authority](https://datatracker.ietf.org/doc/draft-mcgraw-httpapi-agent-budget/) — Delegated software requesters increasingly make HTTP requests that
   spend, consume, disclose, mutate, invoke, or actuate on behalf of
   human or organizational principals.  Existing HTTP authentication
   mechanisms indicate whether a requester holds a credential.
   RateLimit fields communicate server-advertised quota and current
   service-limit information.  HTTP Message Signatures can protect
   selected components of an HTTP message.  None of these mechanisms
   directly defines a common origin-server challenge for a requester to
   present verifiable, bounded authority from its principal before the
   server performs protected processing.

   This document defines the "Delegation" HTTP authentication scheme,
   response semantics for delegated-authority challenges using existing
   HTTP status codes and Problem Details, the Delegation-Proof HTTP
   field, and a COSE/CBOR proof carriage model for request-bound
   delegated authority.  The initial authority profile is the Budget
   profile, which uses a CBOR/COSE Budget-Attestation envelope to prove
   bounded authority to spend, consume metered service units, or commit
   bounded resources.  The mechanism is algorithm-agile; the initial
   cose-ml-dsa proof profile uses existing JOSE and COSE serializations
   for ML-DSA, with ML-DSA-65 as the baseline algorithm and ML-DSA-87
   available as a high-assurance deployment policy option.  A dedicated
   4NN Delegated Authority Required status code remains an open design
   question for HTTP Working Group review; this revision does not depend
   on that status code and does not define payment semantics.  This
   revision also defines a mandatory-to-implement preflight flow for
   large proof profiles so that GET and HEAD requests do not depend on
   request content, and so that requests with application
   representations do not need to multiplex the application body and the
   proof body in a single content stream.

   For implementation experience, this individual draft also includes
   the initial Budget authority profile.  The HTTP authentication
   scheme, status-code semantics, Problem Details members, and field-
   carriage rules are intentionally separable from the COSE/CBOR Budget
   profile.  If a Working Group chooses to progress the HTTP mechanism
   independently, the Budget authority profile can be moved to a
   companion profile document without changing the Delegation challenge
   semantics defined here.
- **draft-watts-oauth-agent-revocation-closure-00** (new-draft, score 21, authorization) [none]: [Revocation Closure for Agentic Authorization Systems](https://datatracker.ietf.org/doc/draft-watts-oauth-agent-revocation-closure/) — Agentic systems can derive and distribute authority across delegated
   agents, workloads, credentials, queues, and long-running operations.
   Existing revocation mechanisms can invalidate a credential or
   authorization grant, but credential invalidation alone does not
   establish that every path from revoked authority to a consequential
   effect has been closed.

   This document defines a protocol-neutral model for revocation
   closure.  It introduces authority graphs, consequential sinks,
   revocation cut sets, closure states, closure budgets, and closure
   receipts.  The model is intended to complement OAuth 2.0, workload
   identity, transaction-token, and agent-authorization work.  It does
   not define a new authorization protocol, token format, or AI safety
   mechanism.
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
- **draft-das-agentic-execution-finality-02** (new-draft, score 20, authorization) [none]: [Tool Selection Is Not Execution: Finality for Agentic Tool Dispatch in High-Risk AI Systems](https://datatracker.ietf.org/doc/draft-das-agentic-execution-finality/) — This architecture is specifically designed for high-risk AI systems,
   where standard engineering priorities shift from speed and latency
   toward absolute determinism and safety.

   An agentic model can emit a tool call that today's runtimes treat as
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

   A runnable reference implementation for this dispatch-time gate is
   provided at tool_use Is Not invoke(): Binding Execution-Finality to
   Agentic Tool-Call Interfaces and MCP (https://github.com/sangmdas/
   tool_use-Is-Not-invoke-Binding-Execution-Finality-to-Agentic-Tool-
   Call-Interfaces-and-MCP).
- **draft-hillier-scitt-arp-04** (new-draft, score 20, trust_infrastructure) [none]: [Attestation Reconciliation Protocol](https://datatracker.ietf.org/doc/draft-hillier-scitt-arp/) — This document specifies the Attestation Reconciliation Protocol
   (ARP), a deterministic, bilateral, minimum-disclosure mechanism for
   reconciling verification claims against a plurality of sovereign
   authoritative registers without raw register records leaving their
   data-residency jurisdiction.  ARP extends the SCITT (Supply Chain
   Integrity, Transparency, and Trust) architecture to cross-sovereign
   claim reconciliation.  A reconciliation server canonicalises a
   structured claim, binds the identity of the requesting principal --
   including, where the requester is an autonomous agent, a friend-or-
   foe determination of that agent's verifiable principal binding --
   projects the claim through register-specific controlled projection
   functions producing the nearest permitted ancestor predicate
   supported by each addressed register, transmits register-specific
   ciphertexts, receives partial attestations whose payload discloses,
   of the subject, only a verdict, an optional divergence axis, the
   applied profile parameters and a query binding digest, aggregates
   those attestations under a verdict arithmetic the deployment's policy
   resolves, committing each register's contribution to a Merkle tree,
   and seals the resulting reconciliation output against a policy-
   version hash.  An append-only cross-jurisdictional settlement-layer
   ledger records digests and structural metadata, with no claim,
   register-record or principal content.  The protocol supports
   retroactive re-evaluation of historical reconciliations under updated
   pattern libraries or policy versions without bilateral renegotiation,
   and a cryptographic-primitive-upgrade path including post-quantum
   primitives.  This revision adds a normative binding to the SCITT
   Reference APIs, register data-format profiles for beneficial-
   ownership, corporate-registry, customs and consolidated-sanctions
   formats, and a source-data version binding that makes a change in a
   historical verdict attributable to a change in policy or to a change
   in the underlying published corpus.
- **draft-das-protocols-enterprise-ai-02** (new-draft, score 19, trust_infrastructure) [none]: [Assume the AI Server Is Already Compromised: Execution-Consequence Decoupling So a High-Risk Enterprise AI Cannot Join, Infer, or Send](https://datatracker.ietf.org/doc/draft-das-protocols-enterprise-ai/) — Start from the assumption that the attacker already controls the AI
   server — that the workload is fully compromised.  Not the perimeter,
   not a phished seat — the workload itself: its credentials, its
   connectors, its context window, its output path.  Nearly every
   enterprise control in use today has already failed by that point,
   because nearly every one of them is designed to keep the attacker out
   of the workload rather than to limit what the workload can do once it
   is theirs.

   Before anything else, the engineering posture: this architecture is
   specified for high-risk AI systems, where the standard priorities
   shift from speed and latency toward determinism, containment, and
   safety.  It is written for billion-dollar enterprise and mission-
   critical deployments — banking and treasury, defence and national
   security, critical infrastructure, and regulated enterprises holding
   unreleased material — and not for general day-to-day, consumer-grade,
   or low-stakes use.  It introduces evaluation on the join path and on
   the release path, and accepts that cost deliberately, because in
   these environments an unauthorized reconstruction or an unauthorized
   send is not recoverable by being fast.

   This document asks what is still denied to the attacker at that
   moment, and specifies an architecture in which two things are still
   denied: the attacker cannot cause independently held enterprise
   fragments to be bound into a map of the organization, and cannot
   cause any generated result to become externally effective.  Access to
   a store is not authority to join it to another store.  Finishing a
   generation is not authority to send it.

   The mechanism is Execution-Consequence Decoupling, enforced by three
   pillars: Decomposition of Authority (Technical Non-Joinability)
   across independently controlled identity, content, relationship-
   mapping, and cryptographic domains; Mandatory Mediation of every
   consequence-bearing Candidate Output; and Technical Non-
   Completability, so that computation can run to completion in a
   compromised environment without the ability to complete an external
   consequence.  Reconstruction is governed by a non-bearer
   Reconstruction Authorization Object bound to attested execution
   context, session, purpose, and Permitted Association Scope.
   Candidate Outputs are sealed, re-verified at output time, and
   committed to a Protected Output Validation Receipt before an output-
   specific Release Capability can be issued and exercised at a
   designated Output Release Boundary.

   The industrially relevant systems are the enterprise assistant and
   agent runtimes now deployed into exactly those environments,
   including those built on Anthropic Claude, OpenAI ChatGPT, Google
   Gemini, xAI Grok, and self-hosted Meta Llama models, together with
   the connector and Model Context Protocol fleets attached to them.
   These are named as publicly described deployment classes, because an
   architecture for high-risk enterprise AI should say plainly which
   systems it is about; nothing here characterizes any vendor's internal
   design or security posture, and no vendor has reviewed or endorsed
   this work.  It states the problem space, compares the architecture
   against representative conventional technologies (access control,
   bearer credentials, vaulting, TEEs, sandboxes, DLP, provenance, DRM,
   clean rooms, and information-flow control), gives a detailed
   technical description, and supplies JSON Schema definitions for the
   three protected objects.  A published runnable reference
   implementation [GITHUB-DAS-VII] executes the protected chain
   described here, so the architecture can be run and tested rather than
   only read; it is an architectural reference for the state machine and
   its failure states, not a claim of production isolation.

   This is the architecture and rationale document.  Its companion,
   draft-das-enterprise-ai-output-finality
   [I-D.das-enterprise-ai-output-finality], specifies the same split as
   a deployable protocol profile and metadata format for vendor
   assistant and agent seats.  The two are read together: this document
   explains why authority must be separated from computation; the
   companion specifies the objects, bindings, and boundary sequences
   that carry the separation on the wire.
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
- **draft-das-rats-frontier-model-extraction-04** (new-draft, score 18, trust_infrastructure) [none]: [An Execution-Finality Architecture for Controlling Release and Limiting Unauthorized Extraction and Distillation of Sensitive, High-Priority Frontier AI Model Information](https://datatracker.ietf.org/doc/draft-das-rats-frontier-model-extraction/) — This architecture is a hardware-rooted defense against intellectual-
   property theft of frontier AI models, intended for deployment by AI
   model creators themselves -- including trillion-dollar frontier-model
   providers such as OpenAI and Anthropic -- rather than for generic,
   day-to-day AI use by an end user.  It protects Sensitive Model
   Information that is high-priority and dual-use, with the specific
   purpose of preventing unauthorized extraction and distillation of the
   model itself.  The architecture introduces bounded, deterministic
   evaluation latency to intercept unauthorized release paths, a trade-
   off acceptable specifically for protecting highly valued dual-use
   assets where standard optimization for raw speed is subordinate to
   absolute asset security.

   Frontier and proprietary AI deployments may contain or expose model-
   related information substantially richer than ordinary final-answer
   text.  Depending on the deployment and interface, such Sensitive
   Model Information (SMI) can include detailed probability information,
   embeddings, cached intermediate state, hidden representations,
   intermediate activations, diagnostic information, model-related
   metadata, or other high-information artifacts.  Repeated unauthorized
   or excessive release of such information can increase the efficiency
   of model reconstruction, imitation, extraction, or distillation.

   Authentication establishes who is requesting an operation.
   Confidential computing and remote attestation can establish
   properties of the environment in which computation occurs.  Neither
   property alone determines whether a particular pending release of
   particular model information, to a particular destination, under the
   current extraction state and security epoch, remains authorized to
   become externally usable.

   This document describes an execution-finality architecture for that
   remaining problem.  Sensitive information may be computed while
   remaining a non-effective Candidate Release.  External release occurs
   only after release-specific protected validation, evaluation of
   rollback-resistant extraction state where required, atomic
   reservation or consumption of bounded authority, and verification at
   a controlled Finality Sink.  Release authority is bound to the
   applicable Candidate Release or bounded release class rather than
   operating as a generic transferable bearer credential.

   The architecture does not claim universal prevention of model
   extraction or distillation and does not restrict legitimately exposed
   ordinary model output.  Its narrower objective is to make
   unauthorized, excessive, replayed, rolled-back, or bypassed release
   of protected model information technically harder to complete through
   governed release paths.  RATS can complement this mechanism by
   allowing a Verifier or Relying Party to obtain machine-verifiable
   information about whether the expected release-control mechanism,
   protected state, security epoch, and Finality Sink are present and
   operating with the required assurance properties.

   To demonstrate that this architecture is practically achievable and
   not merely theoretical, a runnable reference implementation is
   provided at Execution-Finality for Protected AI Model-State Release
   -- RATS Reference Implementation (https://github.com/sangmdas/
   Execution-Finality-for-Protected-AI-Model-State-Release-RATS-
   Reference-Implementation).
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
- **draft-mcguinness-oauth-id-continuation-assertion-02** (new-draft, score 17, authorization) [none]: [Identity Continuation Assertion for OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-id-continuation-assertion/) — This document defines the Identity Continuation Assertion, a short-
   lived, sender-constrained JSON Web Token (JWT) used as an OAuth 2.0
   Token Exchange subject token.  It enables a workload acting on a
   user's behalf to obtain an Identity Assertion JWT Authorization Grant
   (ID-JAG) for another service when it lacks a suitable credential,
   including when the user is no longer present.

   A trusted issuer attests that a resource authorization server
   accepted an earlier ID-JAG and that the resulting authorization
   remains active and eligible for continuation.  The workload exchanges
   this assertion at the identity provider, which evaluates the
   requested access under the chain authorization and current policy
   before issuing an onward ID-JAG.  The profile supports multi-hop
   access across resource authorization servers that trust a common
   identity provider.
- **draft-watts-agent-evidence-boundary-00** (new-draft, score 17, core_identity) [none]: [Evidence-Bounded Authorization for Agentic Systems: Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-agent-evidence-boundary/) — Autonomous agents increasingly make or propose consequential actions
   using premises assembled from model outputs, memory, tools,
   telemetry, and external data.  Existing authentication and
   authorization mechanisms can establish who is acting, under whose
   delegation, and which operation is permitted, but they do not by
   themselves establish whether the proposition that triggered the
   operation has adequate support.  This document defines the Evidence
   Qualification Receipt (EQR), a transport-neutral JSON data model and
   fail-closed verification procedure for binding a proposition to a
   declared evidence profile, its supporting evidence digests,
   contradiction state, freshness, and evaluation result.  An EQR can be
   PASS, FAIL, or INDETERMINATE.  A PASS EQR is only an authorization
   input: it is never itself permission to execute.  The design is
   append-only: changed evidence produces a successor receipt rather
   than rewriting prior epistemic state.  The goal is to prevent
   evidence, provenance, or model confidence from silently acquiring
   authorization semantics.
- **draft-mih-sokolov-scitt-payload-binding-05** (new-draft, score 16, trust_infrastructure) [none]: [Canonicalization Declaration for SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-mih-sokolov-scitt-payload-binding/) — Independently written systems that anchor records to a SCITT
   Transparency Service repeatedly need the same construction: a
   canonical form of structured content, a content-addressed identifier
   derived from that form, binding to a SCITT Signed Statement and
   Receipt, and references that cite external artifacts by digest.  This
   document, referred to as CPB, specifies that construction as
   declarations rather than as a payload format.  A payload profile
   declares its canonicalization algorithm and exclusion set and thereby
   obtains a reproducible derived identifier.  A CPB Signed Statement
   carries either the complete statement content as specified by RFC
   9943 or a digest of content held elsewhere using the COSE Hash
   Envelope of RFC 9995.  CPB also defines an abstract typed digest
   reference information model and one optional protected-header
   encoding, cpb-refs; a payload profile may instead define its own
   reference serialization.  An IANA registry assigns the
   canonicalization algorithm identifiers that these declarations name.
   CPB does not define payload content formats, establish or require a
   universal artifact-type registry, or require either typed-reference
   carrier.
- **draft-pinto-agent-authz-contestability-01** (new-draft, score 16, core_identity) [none]: [Contestability Bindings for Authorized Agent Actions](https://datatracker.ietf.org/doc/draft-pinto-agent-authz-contestability/) — Authorization artifacts can provide signed evidence of a permission
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
   Trust Profile identifier pairs.  A deterministic verifier validates
   the binding, separately classifies evidence claiming pre-execution
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
- **draft-das-rats-openai-anthropic-extraction-03** (new-draft, score 15, trust_infrastructure) [none]: [An Execution-Finality Architecture Against Automated Extraction and Distillation of OpenAI and Anthropic Claude Model Information](https://datatracker.ietf.org/doc/draft-das-rats-openai-anthropic-extraction/) — High-capability AI models can expose commercially, strategically, or
   technically valuable model information through governed inference
   interfaces, including logits, log-probabilities, embeddings,
   intermediate representations, structured responses, and other
   protected outputs.  Repeated or automated access to such information
   can contribute to industrial-scale model extraction, unauthorized
   capability replication, or distillation, creating significant
   intellectual-property, commercial, security, or strategic risk for
   operators of high-value models.

   The problem addressed by this document is not whether a model is
   technically capable of computing such information, but whether
   computation itself should constitute authority to release it.  This
   document therefore separates model computation from external
   disclosure: successful inference does not, by itself, constitute
   release authority.  An output may be fully computed while remaining a
   non-effective Candidate Release that cannot yet cross the governed
   release boundary.

   A Candidate Release remains non-effective until the applicable
   release conditions have been independently satisfied.  The
   architecture can include release-specific protected validation,
   evaluation of rollback-resistant extraction state where required, and
   atomic reservation or consumption of bounded release authority.  A
   controlled Finality Sink verifies the required state at the boundary
   where the protected information would first become externally
   available.  Release authority is bound to the applicable Candidate
   Release or bounded release class rather than functioning as a generic
   transferable bearer credential.  The intended result is a technical
   separation between information that a model can compute and
   information that the governed system permits to become externally
   effective.

   This architecture is intended primarily for high-value or high-
   capability models and protected output classes where industrial-scale
   extraction or unauthorized capability replication creates sufficient
   risk to justify stronger release controls.  It is not intended to
   impose the same enforcement mechanism on every model, user request,
   or inference path.  Operators can apply execution-finality controls
   selectively according to model value, protected-output class,
   extraction risk, interface characteristics, or required assurance
   level.

   Such enforcement can introduce additional protected-state management,
   validation, synchronization, attestation, or Finality Sink
   verification overhead.  Latency is therefore an explicit deployment
   tradeoff rather than an assumption that every inference request
   should incur the same assurance cost.  For sufficiently valuable
   models or sensitive capabilities, an operator may determine that
   stronger protection against industrial-scale extraction justifies
   additional release-path processing, while ordinary or lower-risk
   output paths may use lighter controls.

   The architecture does not claim universal prevention of model
   extraction or distillation.  In particular, it does not claim to
   prevent all learning from ordinary outputs that have been
   legitimately released, nor does it claim control over information
   after valid disclosure beyond the governed boundary.  Its narrower
   objective is to constrain industrial-scale extraction conducted
   through governed release paths and to make unauthorized, excessive,
   replayed, rolled-back, or bypassed release of protected model
   information technically harder to complete.

   Remote Attestation Procedures (RATS) can complement this architecture
   by providing machine-verifiable evidence that the expected release-
   control mechanism, protected extraction state, security epoch, and
   Finality Sink are present and operating with the required assurance
   properties.  Attestation establishes evidence concerning the
   enforcement environment; it does not itself constitute authority to
   release a protected Candidate Release.
- **draft-fletcher-oauth-txn-token-chaining-profile-00** (new-draft, score 15, authorization) [none]: [Transaction Token Authorization Grant Profile for OAuth Identity and Authorization Chaining](https://datatracker.ietf.org/doc/draft-fletcher-oauth-txn-token-chaining-profile/) — This specification defines a profile of the OAuth Identity and
   Authorization Chaining Across Domains
   [I-D.ietf-oauth-identity-chaining] mechanism that uses a Transaction
   Token (Txn-Token) [I-D.ietf-oauth-transaction-tokens] as the subject
   token in a Token Exchange [RFC8693] request to obtain a JWT
   Authorization Grant for crossing a trust boundary.

   A Txn-Token is scoped to a single trust domain and represents the
   full authorization context of an in-progress transaction, regardless
   of whether that transaction was initiated by a human user calling an
   external API, by an internal system event, or by an automated
   workload.  This profile specifies how a service operating within that
   trust domain can present its Txn-Token to obtain a JWT Authorization
   Grant that carries the necessary context across a trust boundary,
   enabling an access token to be issued for a partner service, without
   exposing internal trust-domain credentials or token formats beyond
   the trust boundary.
- **draft-schrock-ep-authorization-receipts-13** (new-draft, score 15, adjacent_watchlist) [none]: [Authorization Receipts for High-Risk Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/) — This document defines the EMILIA Protocol (EP) authorization receipt,
   an evidence artifact binding an enrolled approver key to one
   canonical action before execution.  An approver-held key signs an
   Authorization Context containing the action hash, policy reference,
   shared authorization instance, per-signoff nonce, audience, and
   validity window.  A Trust Receipt carries the signed contexts,
   terminal consumption record, and Merkle inclusion material so a
   relying party can verify the recorded event offline under
   independently selected log, directory, policy, and approver trust
   inputs.

   The receipt establishes only the guarantees of the selected
   verification profile.  The mapping from an enrolled approver
   identifier to a natural person is asserted by the directory
   authority.  Offline verification does not establish current
   revocation status, global non-replay, comprehension, legality,
   safety, or execution.  Replay prevention requires an online atomic
   consumption store at the executor.  The state-machine invariants are
   machine-checked under the assumptions stated in this document.

   This revision defines the closed EP-AUTHORIZATION-BUNDLE-v1 pre-
   execution profile and its verification algorithm.  The bundle carries
   the Action Object, signed Authorization Contexts, signoffs, key
   proofs, and presentation evidence; it deliberately carries no
   terminal consumption or execution claim.  An optional, profile-
   identified authorization binding can commit the human evidence to an
   independently verified native authorization artifact without
   replacing that artifact or making this receipt format depend on its
   transport or trust model.

   A receipt is evidence, not authorization.  This document does not
   treat a local user interaction as an authorization decision.  It
   defines one evidence artifact that an authorization architecture can
   use in a human-confirmation flow: the signed Authorization Context is
   action-bound confirmation evidence an authorization server MAY
   validate and bind to the grant it issues.  The resulting Trust
   Receipt records terminal consumption and remains evidence; neither
   object makes the authorization decision.  That decision remains with
   the authorization server.
- **draft-sogomonian-aiip-core-00** (new-draft, score 15, core_identity) [none]: [AIIP Core: Agent Access Plane, AIID, Resolve, Invoke, and Receipt](https://datatracker.ietf.org/doc/draft-sogomonian-aiip-core/) — This document specifies the core of the AI Internet Protocol (AIIP)
   agent access plane: the AIID identity namespace, the aiip: URI
   scheme, Resolve, Invoke, Receipt, and delegation grants.  Underlay
   addresses are disposable locators only.  Agents MUST NOT use HTTP or
   HTTPS as their Invoke (or Resolve) path.  Independence doctrine:
   underlay pipes and platforms are never authority.  Mesh tip
   attestation is a trust layer, not a ledger.  Access Fabric punch ops
   are Experimental.  This revision (2026-09-08 wire harden) is derived
   from the running lab profile "aiip-wire-0".  It is an individual
   submission draft; it does not claim Working Group adoption or RFC
   publication.
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
- **draft-das-digital-sovereignty-finality-02** (new-draft, score 14, adjacent_watchlist) [none]: [When Data Leaves Its Originating Jurisdiction, Who Controls It? Digital Sovereignty Without Data Localisation by Separating the Compute Plane from the Authority Plane](https://datatracker.ietf.org/doc/draft-das-digital-sovereignty-finality/) — Consider a simple case: data concerning U.S. citizens is processed in
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
- **draft-das-payment-execution-finality-01** (new-draft, score 14, authorization) [none]: [A Signed Instruction Is Not Settlement: Finality for Agentic and API Payments](https://datatracker.ietf.org/doc/draft-das-payment-execution-finality/) — Payment rails already know how to move money.  They do not know
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
- **draft-das-protocols-candidate-act-finality-01** (new-draft, score 14, core_identity) [none]: [Stopping AI Hallucinations and Unsafe Acts from Becoming Real-World Consequences (DAS Protocols)](https://datatracker.ietf.org/doc/draft-das-protocols-candidate-act-finality/) — The internet has protocols for moving data, securing channels, naming
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
- **draft-wadkins-agentproto-action-determinability-00** (new-draft, score 14, core_identity) [none]: [Independent Determinability of Agent Actions](https://datatracker.ietf.org/doc/draft-wadkins-agentproto-action-determinability/) — Evidence that an agent was authorized to act does not establish that
   the authorization was enforced, that the action was executed, or that
   the intended effect occurred.  These are distinct transitions.

   This document defines requirements for making a claimed agent
   transition independently determinable after the original interaction
   has ended.  The requirements address binding the material action and
   governing conditions to the transition at decision time, identifying
   which revision of a mutable governing artifact was in force,
   preventing later substitution, and preserving enough information for
   an independent evaluator to establish the claimed transition after
   participants, sessions, credentials, keys, or agent instances are no
   longer available.

   This document defines no evidence format, token, action identifier,
   delegation protocol, audit system, registry, or transparency service.
- **draft-le-scitt-derived-subjects-01** (new-draft, score 13, trust_infrastructure) [none]: [SCITT Profile for Independently Derived Subjects](https://datatracker.ietf.org/doc/draft-le-scitt-derived-subjects/) — The Supply Chain Integrity, Transparency, and Trust (SCITT)
   architecture permits distinct Issuers to agree on a common CBOR Web
   Token (CWT) Subject Claim (sub).  This document specifies a profile
   for independently deriving that claim from shared application-defined
   Subject semantics without a shared assigning authority.

   An application maps its Subject description to a structured Value.
   This profile defines the derivation domain, deterministic binding
   encoding, SHA-256 construction, text syntax, and candidate-to-claim
   comparison requirements.  Optional JSON and Concise Binary Object
   Representation (CBOR) codecs exchange admitted Values.  Subject
   descriptions and Statement payloads have separate roles; the
   construction derives sub from the complete mapped Value, while SCITT
   provides the signed binding and transparency evidence.
- **draft-das-hardware-enforced-execution-finality-02** (new-draft, score 12, agent_identity) [none]: [Computation Is Not Authority: Hardware-Enforced Execution-Finality for Agentic AI, MCP Tool Calls, and Industrial Agents](https://datatracker.ietf.org/doc/draft-das-hardware-enforced-execution-finality/) — Neural AI systems -- large language models, vision-language models,
   and other learned decision systems -- now move directly from
   computation to consequence.  A model output becomes a tool call; a
   tool call becomes an API transaction, memory write, payment, file
   mutation, browser action, or actuator signal; an agent delegates to
   another agent.  Successful inference, sandbox containment, connector
   allowlisting, session permission, or upstream model approval does not
   by itself establish authority for that particular real-world
   consequence.  A model may be authorized to compute while remaining
   unauthorized to act.

   This document specifies a hardware-rooted execution-finality
   architecture for neural and agentic systems.  A proposed consequence-
   bearing operation is represented as a Candidate Act and held in a
   Non-Effective State until a Protected Enforcement Domain validates
   act-specific predicates and an independent Finality Sink verifies
   scoped, non-bearer finality authority immediately before the
   operation becomes externally effective.  If that authority is absent,
   stale, replayed, revoked, or mismatched to the act being attempted,
   the Candidate Act remains non-effective and the operation fails
   closed.

   The architecture is model- and vendor-neutral.  It is written for the
   industrial surfaces that now dominate production agent deployments:
   Model Context Protocol (MCP) tool dispatch, computer use, code
   execution, enterprise connectors, memory and knowledge-store writes,
   GPU and confidential-computing egress, and settlement.  The same
   invariant applies to those surfaces: computation is not authority;
   tool selection is not tool-effectuation; a connector allowlist is not
   per-act finality.
- **draft-ietf-acme-rats-02** (new-draft, score 12, trust_infrastructure) [acme]: [Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type](https://datatracker.ietf.org/doc/draft-ietf-acme-rats/) — This document describes an approach where an ACME Server can
   challenge an ACME Client to provide Evidence, Endorsements, or
   Attestation Result according to the Remote ATtestation procedureS
   (RATS) framework in any format supported by the Conceptual Message
   Wrapper (CMW).

   The ACME Server can optionally challenge the Client for specific
   claims that it wishes attestation for.
- **draft-ozturk-scitt-prml-profile-00** (new-draft, score 12, trust_infrastructure) [none]: [A SCITT Profile for Pre-Run Evaluation Criteria (PRML)](https://datatracker.ietf.org/doc/draft-ozturk-scitt-prml-profile/) — This document defines a profile for carrying pre-run evaluation
   criteria as a SCITT Signed Statement payload, using the architecture
   of RFC 9943.  It specifies the payload media type, the selection of
   the Issuer and Subject CWT claims, the encoding of hash-only
   statements for criteria that must remain confidential, a sequencing
   requirement that makes amendment order verifiable, and the semantics
   of amendment itself.  It does not define a new transparency
   architecture; it describes how an existing artefact type is carried
   by the one RFC 9943 already defines.
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
- **draft-das-enterprise-ai-output-finality-03** (new-draft, score 11, authorization) [none]: [The Missing Piece for High-Value Confidential Enterprise AI: Non-Joinable Vaults and Output-Release Finality for Banking, Defence, and Public-Sector Deployments](https://datatracker.ietf.org/doc/draft-das-enterprise-ai-output-finality/) — This profile is specified for high-risk, multi-system enterprise and
   public-sector AI — assistants and agents that can see several
   independently authorized stores and then send, write, or invoke.  It
   is not specified for consumer chat.  In industrial terms that
   describes enterprise assistant and agent seats of the kind offered by
   Anthropic, OpenAI, Google Gemini, and xAI Grok, together with self-
   hosted open-weight deployments; these names are used with respect, as
   publicly described deployment classes only, and imply no claim about
   any vendor's internals and no vendor endorsement of this profile.

   A 2020 breach stole what was already stored: a server image, a
   database dump, user rows.  After 2025 a compromised assistant can do
   what a dump cannot.  In minutes it can join mail, tickets, code,
   finance, and memory into a map of launch plans, targets, defects, and
   negotiation room — strategy that was never one record — and that map
   can be sold to a competitor.  There is no credential rotation for a
   future that has already been read.  Traditional access control still
   answers who may touch each store.  It does not answer whether those
   fragments may be joined into that meaning, or whether that meaning
   may leave.

   This document specifies an architectural framework and metadata
   profile for that gap.  Technical Non-Joinability is enforced by a
   session-bound Reconstruction Authorization Object (RAO) that limits
   relational binding.  Technical Non-Completability is enforced by an
   Output Release Boundary that requires committed validation evidence
   before a generated token or tool invocation can take external effect.
   The specification defines the authorization objects, cryptographic
   bindings, and boundary validation sequences required to isolate
   reconstruction domains without modifying the underlying datastores.

   A published runnable reference implementation is provided so that the
   profile can be executed and tested, not only read as theory.  That
   implementation is an architectural reference for the state machine,
   not a claim of production isolation.  The architecture introduces
   bounded evaluation on the path that can intercept unauthorized join
   or release.  That latency is accepted where the asset is high-
   consequence enterprise or public-sector intelligence and raw speed is
   subordinate to preventing reconstruction and release.  The author
   states that trade-off explicitly: this profile is for deployments
   that choose that priority.  It is not offered as a design for
   consumer chat or other paths that optimize only for speed.

   Readers are respectfully encouraged to review Section 4 and Section 5
   in full, as those sections set out the complete problem description
   and motivating scenarios and should not be skipped.
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
- **draft-novak-rats-tacra-01** (new-draft, score 11, trust_infrastructure) [none]: [Trustworthy Acquisition of Credentials via Remote Attestation](https://datatracker.ietf.org/doc/draft-novak-rats-tacra/) — There is a large class of "RATS-Unaware" Relying Parties (RUPs) that
   Attesters nevertheless need to interoperate with.  Existing deployed
   services, which precede the introduction of Remote Attestation, are
   often difficult to change/update in significant ways due to, among
   other reasons, organizational friction, technological inertia, and
   regulatory policies.  There are significant advantages if workloads
   can be incrementally updated in the trustworthiness of the platform,
   without disrupting their clients and servers.

   This document describes an architecture by which Remote Attestation
   is utilized for providing Attesters with Identity Documents (keys or
   credentials) to authenticate to RUPs.  This architecture is intended
   to work with common credential acquisition protocols and mechanisms
   such as EST, SPIFFE/SPIRE, ACMEv2, and many others.

   Another important but separate goal is to encapsulate the Attester-
   side complexity of Remote Attestation and credential acquisition
   similar to how Envoy does it.  This allows Attesters to be
   implemented in a way that abstracts away the details of credential
   acquisition: both the protocols used and the Credential Acquisition
   Mechanisms employed, whether minting new (Enrollment), or requesting
   existing (Retrieval) credentials.  Likewise, the choice between RATS
   Passport and Background Check models is made opaque to the Attester,
   further simplifying its development.
- **draft-das-cvid-enforcement-profiles-00** (new-draft, score 10, core_identity) [none]: [Capability-Validated Inbound Descriptors: Catalogue of Enforcement Profiles](https://datatracker.ietf.org/doc/draft-das-cvid-enforcement-profiles/) — A destination identifier, an API credential, a completed computation,
   and an attested execution environment are each routinely treated as
   if they carried authority for consequence.  This document argues that
   none of them does, and catalogues fifty-nine enforcement profiles of
   the Capability-Validated Inbound Descriptor (CVID) architecture, in
   which an attempted act is a Candidate Act with no external effect
   until a protected enforcement domain validates a conjunctive
   predicate set and releases the capability the effect requires.

   The profiles span inbound communication; network capability exposure
   and intent-driven network programming; AI-native radio access,
   network slicing and packet core; distributed inference and digital
   twins; ultra-reliable low-latency operation; cross-border and
   sovereignty-bound execution; satellite, non-terrestrial and direct-
   to-device networks; optical inter-satellite links; immersive and
   semantic media; machine swarms; ambient IoT and backscatter;
   reconfigurable intelligent surfaces; device paging and wake; offline
   central bank digital currency settlement; lawful disclosure through
   escrow; platform neutrality measurement; network energy expenditure;
   and enforcement in silicon at accelerator output paths, DMA and RDMA
   boundaries, interconnects, and die-to-die interfaces.

   Three authorities commonly conflated are separated: authority to
   consume resources, authority to compute, and authority to cause an
   external effect.  From that separation follows the treatment of
   energy as an enforceable security resource rather than only an
   efficiency metric, with a low-energy admission tier deciding whether
   a candidate may activate expensive baseband, accelerator, or radio
   paths at all.  The document compares this position with published 6G
   energy work from Ericsson, Nokia, Qualcomm, and Huawei, states what
   the author believes is new, and sets out the limitations of the
   approach.

   Profiles are reproduced in the structural form in which they were
   drafted, including system and method variants of the same mechanism.
   The architecture itself, its terminology, and its protocol mappings
   are described in a companion document.  This document is published
   for discussion and comment; it is not a product of an IETF Working
   Group, and corrections are invited.
- **draft-das-execution-finality-ai-interoperability-04** (new-draft, score 10, authorization) [none]: [Secure and Privacy-Preserving AI Interoperability under Article 6(7) of the European Digital Markets Act: An Execution-Finality Architecture](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-interoperability/) — This document presents a security- and privacy-preserving execution-
   finality architecture for third-party AI interoperability under the
   European Digital Markets Act (DMA).  It is designed to enable
   meaningful participation by external AI assistants while keeping
   consequential device actions under bounded, verifiable platform
   control.

   The architecture separates an AI-generated request from the authority
   to make that request externally effective.  A requested operation
   remains in a Non-Effective State until protected infrastructure
   validates the requester, intended resource, destination, user
   authorization or intent where required, purpose and scope, freshness,
   revocation state, runtime conditions, and other applicable policy
   predicates.

   After successful validation, the system creates narrowly scoped, non-
   bearer execution authority bound to the specific Candidate Act. At
   the Finality Sink—the first boundary at which the operation can
   become externally effective—the system independently verifies that
   the actual operation still matches the validated act and that the
   authority remains current and unused.

   This design is intended to address major security risks associated
   with AI interoperability, including prompt injection, compromised
   assistant or cloud infrastructure, confused-deputy behavior, replay,
   token theft or reuse, destination or parameter substitution, scope
   escalation, stale authorization, alternate-path bypass, and
   unauthorized consequential execution.

   It also supports privacy protections by limiting access and
   effectuation to the minimum act-specific scope, reducing dependence
   on broad reusable permissions, preserving revocation and user-control
   boundaries, and preventing data release or transmission when the
   protected validation conditions are not satisfied.

   The resulting model is open participation with bounded, verifiable
   authority: third-party AI systems may interoperate with device
   functions without receiving unrestricted final-effect authority,
   while the platform retains protected enforcement over whether a
   proposed action is permitted to become externally effective.

   The length of this document is intentional.  It aims to work through
   the major security- and privacy-related objections associated with
   third-party AI interoperability at a technical level of detail
   sufficient to show that they are addressed, rather than merely
   asserted, and reviewers are welcome to engage with any section on its
   own merits.

   In June 2026, Apple announced that it would not ship its new Siri AI
   on iOS 27 and iPadOS 27 in the European Union, stating that EU
   regulators had not accepted its proposed interoperability safeguards
   and that granting third-party assistants access equivalent to Siri's
   created unacceptable security and privacy exposure.  The European
   Commission responded that nothing in the DMA itself required Apple to
   withhold the feature, describing Apple's decision as a voluntary
   business choice rather than a legal necessity, and noting that Apple
   had requested a blanket exemption rather than submitting a compliant
   technical mechanism.  Both positions are correct within their own
   frame: Apple's underlying security concern about undifferentiated
   third-party system access is real, and the Commission is also correct
   that the DMA does not itself compel a trade-off between
   interoperability and security.  This document's execution-finality
   architecture is offered as the middle solution by which both can be
   satisfied simultaneously: third-party AI assistants gain the
   interoperability the DMA requires, while the platform retains the
   bounded, verifiable finality control that Apple's objection is
   actually about.  To show this is not only a theoretical proposal, a
   runnable reference implementation of this architecture has been
   published, demonstrating how the design behaves end to end in a
   virtual/test environment (note: behavior and measurements in an
   actual production environment may differ).

   A note for reviewers: the length of this document is deliberate.
   More than sixty technical questions are answered in question-and-
   answer form, covering anticipated security, privacy, deployment, and
   standardisation objections as well as performance, scalability, and
   hardware enforcement.  To show that the architecture is intended to
   be implementable and not only a paper proposal, two runnable open-
   source reference implementations are also referenced: the initial
   demonstrator, and an adversarially hardened follow-on that adds live
   challenge-bound finality, strict object verification, cross-object
   consistency checks, and 100 executable tests.  The latest
   implementation is available in the Hardened Challenge-Bound
   Execution-Finality Reference Implementation repository
   (https://github.com/sangmdas/Hardened-Challenge-Bound-Execution-
   Finality-for-AI-Interoperability).  Both implementations were
   exercised in a virtual/local test environment, and actual readings
   may vary in separate environments; they are offered as evidence of
   engineering feasibility rather than as production-certified software.
   Critical review of both the document and the code is sincerely
   welcomed.
- **draft-kondoju-evc-02** (new-draft, score 10, authorization) [none]: [An External Verifier Contract for Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-kondoju-evc/) — This document specifies the External Verifier Contract (EVC): a
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
- **draft-ross-mercurius-06** (new-draft, score 10, adjacent_watchlist) [none]: [Mercurius Window System (MWS)](https://datatracker.ietf.org/doc/draft-ross-mercurius/) — The Mercurius Window System (MWS) is a zero-trust, network-native
   window system for contemporary desktops. It combines persistent,
   detachable graphical Sessions with network transparency. MWS works
   on a workstation without requiring network connectivity. The same
   Session model allows users to start a new Session or resume a
   detached Session, either at the workstation itself or from another
   device across the network.

   MWS complements local display systems such as Wayland. Applications
   and their state remain on the workstation, while a Portal provides
   the user's display and input facilities. Modern graphics APIs and
   authenticated transport support this separation between where
   applications execute and where a user interacts with them. This
   document specifies the Session, Window, and communication behaviour
   needed for independent implementations to interoperate.
- **draft-schrock-ep-presentation-binding-01** (new-draft, score 10, authorization) [none]: [Binding Deterministic Rendering and Display Attestations to Human-Authorization Receipts](https://datatracker.ietf.org/doc/draft-schrock-ep-presentation-binding/) — A human-authorization receipt proves an enrolled key produced a user-
   verified signature over a digest that commits to an exact action.  It
   does not prove the signing surface DISPLAYED that action honestly.
   If a signing interface shows a benign summary while committing a
   different action, the resulting receipt is laundered authority:
   cryptographically valid and semantically false, which is worse than
   no receipt at all.  This is the presentation attack, and it is the
   deepest unsolved problem in authorization evidence, because a
   signature cannot attest to pixels.  This document narrows the gap
   with two additive, offline-checkable pieces that touch no existing
   receipt format: a DETERMINISTIC RENDERER, a pure function from the
   canonical action to a byte-identical human-readable rendering, so a
   verifier RE-DERIVES the rendering from the signed bytes and rejects a
   claimed rendering that does not match; and a DISPLAY ATTESTATION, a
   signed claim by the signing client binding the rendering it showed to
   the action it committed.  Neither eliminates the presentation attack
   (nothing purely digital can), but together they let a verifier check
   the claimed rendering against the signed action under relying-party-
   selected client trust inputs.  They make the residual risk explicit
   rather than hidden.
- **draft-zehavi-oauth-authz-req-del-chain-01** (new-draft, score 10, authorization) [none]: [OAuth Authorization Request Delegation Chain](https://datatracker.ietf.org/doc/draft-zehavi-oauth-authz-req-del-chain/) — Brokered OAuth redirect authorization requests involve intermediary
   authorization servers between a downstream client and the upstream
   authorization server that obtains user consent and issues tokens.
   Such deployments have security risks because the upstream
   authorization server sees only the immediate OAuth client and is
   unaware of the downstream client or intermediary brokers obtaining
   its response.

   This document defines an OAuth 2.0 profile for carrying a verifiable,
   signed authorization request delegation chain as a RAR
   authorization_details object [RFC9396].  Each node in the chain is a
   JSON object signed by an attesting authorization server using
   detached JWS [RFC7515], attesting its validated client, hash-linked
   to the previous node, allowing the upstream authorization server to
   validate the integrity of the visible delegation path and apply
   policy before issuing tokens.
- **draft-ietf-acme-authority-token-jwtclaimcon-07** (new-draft, score 9, core_identity) [acme]: [JWTClaimConstraints profile of ACME Authority Token](https://datatracker.ietf.org/doc/draft-ietf-acme-authority-token-jwtclaimcon/) — This document defines an authority token profile for the validation
   of JWTClaimConstraints and EnhancedJWTClaimConstraints certificate
   extensions within the Automated Certificate Management Environment
   (ACME) protocol.  This profile is based on the Authority Token
   framework and establishes the specific ACME identifier type,
   challenge mechanism, and token format necessary to authorize a client
   to request a certificate containing these constraints.
- **draft-ietf-cose-hpke-27** (new-draft, score 9, core_identity) [cose]: [Use of Hybrid Public-Key Encryption (HPKE) with CBOR Object Signing and Encryption (COSE)](https://datatracker.ietf.org/doc/draft-ietf-cose-hpke/) — This specification defines hybrid public-key encryption (HPKE) for
   use with CBOR Object Signing and Encryption (COSE).  HPKE offers a
   variant of public-key encryption of arbitrary-sized plaintexts for a
   recipient public key.

   HPKE is a general encryption framework utilizing an asymmetric key
   encapsulation mechanism (KEM), a key derivation function (KDF), and
   an Authenticated Encryption with Associated Data (AEAD) algorithm.

   This document defines the use of HPKE with COSE.  Authentication for
   HPKE in COSE is provided by COSE-native security mechanisms or by the
   pre-shared key authenticated variant of HPKE.
- **draft-ietf-jose-pq-composite-sigs-04** (new-draft, score 9, verifiable_claims) [jose]: [PQ/T Hybrid Composite Signatures for JOSE and COSE](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/) — This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for PQ/T
   hybrid composite signatures.  The composite algorithms described
   combine ML-DSA as the post-quantum component and either ECDSA or
   EdDSA as the traditional component.
- **draft-le-structured-value-model-01** (new-draft, score 9, adjacent_watchlist) [none]: [A Structured Value Model for Derived Identifiers](https://datatracker.ietf.org/doc/draft-le-structured-value-model/) — Derived identifier constructions that combine local material with
   identifiers from other systems need a defined comparison domain.
   This document defines a structured value model for such constructions
   and their profiles.  A Value contains exact context octets, exact
   content octets, and a finite set of scoped opaque identifiers.
   Structural admission and equivalence are independent of
   serialization.  Equality includes context, content, and complete
   identifier-set membership.

   The specification gives source mappings and profiles common
   obligations for fixed inputs, imported comparison adaptation, and
   preservation of participation distinctions.  Surrounding
   specifications define concrete mappings, representations, identifier
   derivations, and the shared interpretation needed for
   interoperability.  The model defines no global semantic namespace,
   wire format, cryptographic construction, or trust mechanism.
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
- **draft-das-execution-finality-ai-boundary-00** (new-draft, score 8, authorization) [none]: [An Execution Interlock at the AI Model-to-External-Effect Boundary](https://datatracker.ietf.org/doc/draft-das-execution-finality-ai-boundary/) — An AI system's ability to compute an operation is not the same as
   authorization for that operation to take effect outside the system.
   This document defines an enforcement boundary at which an operation
   produced by an AI system is verified against the effect it will
   actually produce, rather than against the effect that was requested
   or approved upstream, and specifies that the operation carries no
   external consequence until that verification succeeds.

   The boundary is complementary to alignment, sandboxing, monitoring,
   and interpretability, which reduce the likelihood that an unsafe
   operation is produced.  This document addresses the separate question
   of what prevents a produced operation from becoming effective.  The
   mechanism functions as a safety interlock: it does not restrict what
   the system may compute, only whether a specific computed operation
   may take effect.  The invariant is that computation is not authority.
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
- **draft-rosenberg-vcon-restructure-00** (new-draft, score 8, agent_identity) [none]: [Virtualized Conversations (VCON) Restructure to Facilitate AI Agent Use Cases](https://datatracker.ietf.org/doc/draft-rosenberg-vcon-restructure/) — The Virtualized Conversations (VCON) specification provides a
   structured format for storing recordings of conversations, including
   phone calls, email threads and multi-party chats.  VCONs also store
   metadata like call transcripts and mid-call events, like a call hold
   or addition of a party.  Its structure is well suited for 2-party and
   basic multiparty phone calls.  However, there is a need for the VCON
   format to also act as a record of AI Agent conversations, which are
   just another type of conversation.  This document proposes changes to
   the object model in VCON to make it a more suitable format for
   handling AI Agent conversations, as well as more complex conferencing
   use cases.
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
- **draft-das-purpose-execution-finality-03** (new-draft, score 7, adjacent_watchlist) [none]: [Data-Purpose Laundering Prevention: Execution-Finality for Preventing Cross-Domain Data Reuse](https://datatracker.ietf.org/doc/draft-das-purpose-execution-finality/) — Consider a concrete case: a user invokes a highly capable AI model
   under a declared purpose of education, but the resulting capability
   is in fact used for a military or terrorist end -- an illustrative
   example, not a claim about any real deployment.  When such misuse
   surfaces, an unresolved question follows: is the model provider
   liable, is the user liable, or is the jurisdiction that permitted the
   deployment liable?  This document does not answer that question --
   liability determination remains an external legal question for the
   responsible court, regulator, or contracting parties -- but it
   addresses the technical gap that makes the question unanswerable
   today.  Systems that collect data, or grant capability, for one
   stated purpose routinely permit that data or capability to be
   consumed for a different purpose, not because the second use was
   authorized, but because nothing in the protocol path was capable of
   refusing it or of recording what was actually authorized.  The most
   common technical control in deployment today is a self-asserted
   purpose string: a "purpose" claim in a token, a field in an API
   request, a comment in a data-sharing agreement.  A self-asserted
   string is evidence of intent, not proof of authority, and it fails
   precisely when it matters most -- when the requester lies.  This
   architecture addresses that loophole deterministically: it makes an
   undeclared or purpose-switched use technically detectable and
   refusable at the point of use, and it produces verifiable evidence of
   what was actually authorized, so that any subsequent liability
   determination can be argued from that evidence rather than from an
   unverifiable self-assertion.  Achieving that determinism introduces a
   bounded, measurable amount of evaluation latency at the point of use;
   this document treats that latency as an acceptable, secured trade-off
   for closing an otherwise unverifiable gap, not as a cost to be
   minimized at the expense of the guarantee.  The premise is not that
   AI innovation should slow down, any more than cars should be built
   slower; it is that innovation moving this fast needs the technical
   equivalent of a seat belt.

   A runnable reference implementation accompanies this document at
   Purpose Execution Finality Validator -- Runnable Reference
   Implementation (https://github.com/sangmdas/Purpose-Execution-
   Finality-Validator-to-Prevent-Data-Purpose-Laundering-in-AI-Systems).
- **draft-kay-dawn-use-cases-01** (new-draft, score 7, adjacent_watchlist) [none]: [Use Cases and Applicability for Discovery of Agents With Names](https://datatracker.ietf.org/doc/draft-kay-dawn-use-cases/) — This document describes use cases and applicability for Discovery of
   Agents With Names (DAWN).  It illustrates how clients discover AI
   resources and obtain the minimum information needed for subsequent
   interaction within a local network, within an organisation, or
   between cooperating organisations with trust relationships.

   This document does not define a discovery protocol, a registration
   procedure, a selection algorithm, or an agent-to-agent communication
   protocol.
- **draft-schrock-ep-bounded-capability-receipts-06** (new-draft, score 7, authorization) [none]: [Bounded Capability Receipts and Durable Spend Control for Agent Actions](https://datatracker.ietf.org/doc/draft-schrock-ep-bounded-capability-receipts/) — Agents sometimes need bounded authority to perform more than one
   consequential action without obtaining a new human approval for every
   operation.  A signed token alone cannot enforce a shared budget
   across replicas, survive retries safely, or distinguish an operation
   that never crossed an effect boundary from one whose outcome is
   unknown.

   This document defines a bounded capability receipt and a durable
   reserve-admit-reconcile protocol.  The receipt binds an issuance
   authorization, a closed action scope, a budget with explicit units, a
   holder proof, an expiry, and any parent capability.  The state
   protocol atomically refuses overspend and operation-key replay,
   fences concurrent owners, and charges an indeterminate operation when
   an external effect may have occurred.  Delegation transfers rather
   than copies authority: all direct child allocations are funded by
   committed parent operations before child registration, and their
   aggregate cannot exceed the parent balance within one authoritative
   atomic state domain.  It also defines narrowing-only delegation,
   explicit revocation inheritance for delegated authority, an optional
   admission-control epoch that can freeze new consequence admission,
   and evidence interfaces.  It does not make a bearer token into human
   approval, does not provide cross-domain or offline global double-
   spend prevention, and does not claim that an authorized action was
   safe, lawful, or successfully executed.
- **draft-steele-agent-considerations-01** (new-draft, score 7, ai_infrastructure) [none]: [Agent Considerations](https://datatracker.ietf.org/doc/draft-steele-agent-considerations/) — Artificial intelligence (AI) agents consume IETF specifications to
   generate and operate implementations.  This document defines an
   "Agent Considerations" subsection within the Operations and
   Management Considerations section described in RFC 5706 and its
   revision.  It provides guidance on schemas, examples, capability
   descriptions, and verification, with cross-references to agent-
   specific security and privacy analysis.

## Monitor

- **draft-cassandres-hacp-agency-core-00** (new-draft, score 6, trust_infrastructure) [none]: [Human Agency Continuity Protocol (HACP) Core](https://datatracker.ietf.org/doc/draft-cassandres-hacp-agency-core/) — This document specifies the HACP-Core decision contract:
   IntentEnvelope, ProposedAction, AgencyDecision, DecisionToken,
   provenance events, revocation, and the ordered evaluate() algorithm.
   Implementations MUST fail closed.  Decisions MUST be deterministic
   and MUST NOT require a language model on the evaluation path.

   The published executable baseline is the 38-vector HACP-Core v0.9.2
   suite.  Wire object field hacp_version remains "0.9".  Specification
   release 1.0.0 does not change that field.
- **draft-dnoveck-nfsv4-security-16** (new-draft, score 6, authorization) [none]: [Security for the NFSv4 Protocols](https://datatracker.ietf.org/doc/draft-dnoveck-nfsv4-security/) — This document describes the core security features of the NFSv4
   family of protocols, applying to all minor versions.  The discussion
   includes the use of security features provided by RPC on a per-
   connection basis.  Important aspects of the authorization model,
   related to the use of Access Control Lists, will be specified in a
   separate document.

   The current version of the document is intended, in large part, to
   result in working group discussion regarding existing NFSv4 security
   issues and to provide a framework for addressing these issues and
   obtaining working group consensus regarding necessary changes.

   When the resulting documents (i.e. this document and one derived from
   the separate ACL specification) are eventually published as RFCs,
   they will, by updating these documents, supersede the description of
   security appearing in existing minor version specification documents
   such as RFC 7530 and RFC 8881.
- **draft-ietf-dance-client-auth-14** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document updates RFC 6698 and RFC 7671.  It describes how to use the
   TLSA record to publish client certificates or public keys, and also
   the rules and considerations for using them with TLS.  In addition,
   it defines a new TLS extension, DANE Client Identity, to convey the
   client's domain name identity to the server.
- **draft-ietf-lamps-rfc6211-update-01** (new-draft, score 6, core_identity) [lamps]: [Update to the Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute](https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6211-update/) — This document updates RFC 6211.  It corrects an error in the
   definition of the id-aa-CMSAlgorithmProtect ASN.1 object identifier.
   The IANA registry entry has always been correct.
- **draft-ietf-tls-mldsa-06** (new-draft, score 6, core_identity) [tls]: [Use of ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mldsa/) — This memo specifies how the post-quantum signature scheme ML-DSA
   (FIPS 204) is used for authentication in TLS 1.3.
- **draft-ietf-tls-trust-anchor-ids-05** (new-draft, score 6, adjacent_watchlist) [tls]: [TLS Trust Anchor Identifiers](https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/) — This document defines the TLS Trust Anchors extension, a mechanism
   for a TLS client or server to select a certificate to present based
   on the peer's trusted certification authorities.  It describes
   certification authorities more succinctly than the TLS Certificate
   Authorities extension.
- **draft-vicente-oauth-apm-05** (new-draft, score 6, authorization) [none]: [Authorization Posture Mechanism (APM): Per-Transaction Consistency for OAuth 2.0](https://datatracker.ietf.org/doc/draft-vicente-oauth-apm/) — This document describes the Authorization Posture Mechanism (APM), a
   method by which an OAuth 2.0 [RFC6749] authorization server, or a
   resource server acting on its behalf, re-evaluates the mutual
   consistency of three bound factors -- the client certificate, the
   access token, and the device posture -- on a per-request basis for
   privileged operations, rather than only at session establishment.
   When re-evaluated posture degrades relative to the posture under
   which the token was issued, APM defines deterministic, least-
   privilege Graduated Outcomes including scope reduction and method
   restriction, rather than a binary allow or deny.
- **draft-arsentev-agent-run-metrics-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Run Metrics: A JSON Interchange Format for Resource Accounting of Language-Model Agent Runs](https://datatracker.ietf.org/doc/draft-arsentev-agent-run-metrics/) — Autonomous software agents driven by large language models execute
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
   excludes prompt and completion content.  This document also registers
   the associated media type and creates IANA registries for extensible
   enumerations.
- **draft-arsentev-llm-context-discovery-00** (new-draft, score 5, adjacent_watchlist) [none]: [Discovery and Retrieval of Publisher-Curated Context Files for Large Language Model Consumers](https://datatracker.ietf.org/doc/draft-arsentev-llm-context-discovery/) — Publishers have begun to serve a curated, plain-text summary of a web
   origin intended for consumption by large language models and by the
   crawlers that feed them, most visibly under the de facto file name
   "llms.txt".  The practice has no specification, no media type, and —
   of direct operational consequence — no discovery mechanism: a
   consumer that does not already guess the path cannot learn that such
   a file exists.

   This document specifies discovery and retrieval for publisher-curated
   context files.  It defines the well-known URI "llm-context", the link
   relation type "llm-context", and an extension record for the robots
   exclusion protocol, so that a publisher may advertise a context file
   by three independent paths and a consumer may find it without
   guessing.  It specifies a two-tier arrangement of an index resource
   and optional detail resources, states conditional-request and size
   requirements that keep retrieval affordable for both parties, and
   describes the relationship of this mechanism to the robots exclusion
   protocol, to sitemaps, and to work in progress on expressing AI usage
   preferences.

   This document also reports measurements from an operational
   deployment in which twenty crawlers operated by search and language-
   model providers issued 44,005 requests to a host over fifteen days
   without once retrieving the context file the host was serving, while
   the same crawlers retrieved that host's robots.txt 577 times in the
   three days after the context file was deployed.  The absence of a
   discovery mechanism, rather than the absence of interest, is the
   hypothesis this document acts upon.
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
- **draft-chowdhury-terms-txt-00** (new-draft, score 5, core_identity) [none]: [terms.txt: Machine Access Terms and an Origin-Enforced Consent and Compensation Exchange](https://datatracker.ietf.org/doc/draft-chowdhury-terms-txt/) — The Robots Exclusion Protocol lets an origin ask automated clients
   not to fetch certain paths.  It cannot express who is asking, for
   what purpose, under what terms, or at what price, and it provides no
   server-side enforcement.  This document specifies terms.txt, a file
   at a well-known location in the style of robots.txt that states, per
   path and per purpose, whether automated access is allowed, charged,
   or denied, at what use level, at what price, and whether a user's
   delegation is required.  It also specifies the HTTP exchange that
   enforces the file at the origin: requests signed with Web Bot Auth, a
   signed declaration of intent, delegation tokens and payment vouchers
   bound to the authenticated identifier, payment negotiation signaled
   with Problem Details, and origin-signed receipts.  The document
   states which properties the exchange enforces before delivery, which
   it can only audit afterward, and which remain contractual.
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
- **draft-intra-handshake-fail-31** (new-draft, score 5, trust_infrastructure) [none]: [Intra-handshake (aka Early) Attestation Considered Harmful (CVE-2026-33697 of CVSS 7.5 and several other CVEs of up to expected CVSS 10.0 upcoming)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of CVE-2026-33697
   (https://www.cve.org/CVERecord?id=CVE-2026-33697), EUVD-2026-16488
   (https://euvd.enisa.europa.eu/enisa/EUVD-2026-16488), and several
   GitHub Security Advisories (GHSAs) which provide substantial
   technical evidence of how *intra*-handshake (aka early) attestation
   fails in practice, even _without physical access_. Moreover, since
   continuous attestation is generally required [CSA-eBPF]
   [MITRE-Continuous-Attestation], *intra*-handshake attestation adds
   *unnecessary complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA] and the artifacts
   [Intra-handshake.fail-repo] in state-of-the-art formal analysis tool,
   ProVerif, under Apache-2.0 license for reproducibility and review,
   and have been acknowledged by the relevant stakeholders.  Currently,
   there are *two CVEs of CVSS 7.5, one GHSA of 9.0-10.0, two GHSAs of
   CVSS 9.1, one GHSA of CVSS 7.8, seven GHSAs of CVSS 7.4, and one GHSA
   of CVSS 6.3 published against the broader intra-handshake (aka early)
   attestation covering all layers of the ecosystem up to the
   application*. The research papers on these are currently either under
   submission or being prepared for submission.  The artifacts of these
   papers will be shared with the community under Apache-2.0 license for
   reproducibility and review.  In our analysis, the remaining
   implementations of early attestation -- Edgeless Systems Contrast and
   Meta's AI -- remain vulnerable.
- **draft-moonesamy-authorship-ietf-00** (new-draft, score 5, ai_infrastructure) [none]: [Reflections on IETF Authorship](https://datatracker.ietf.org/doc/draft-moonesamy-authorship-ietf/) — [RFC825] was intended to provide guidance to authors of future RFCs.
   The memo also listed several reasons for publishing a memo as an RFC.
   It did not discuss who would be listed as author.

   This memo discusses authorship within the IETF and the use of
   generative Artificial Intelligence for IETF RFCs.
- **draft-jwang-dnsop-dns-latency-measurement-00** (new-draft, score 4, authorization) [none]: [A Framework for DNS Resolution Latency Measurement](https://datatracker.ietf.org/doc/draft-jwang-dnsop-dns-latency-measurement/) — DNS resolution latency is widely used as an operational metric for
   evaluating recursive resolvers, authoritative servers, and DNS
   infrastructure.  However, current implementations employ different
   definitions, measurement scopes, and testing methodologies, making
   latency results difficult to compare across deployments.

   This document identifies common sources of inconsistency, proposes a
   conceptual latency decomposition model, and provides measurement
   considerations intended to improve comparability of DNS latency
   measurements.  This document does not define protocol behavior nor
   introduce new protocol mechanisms.
- **draft-tempobono-protectchain-00** (new-draft, score 4, adjacent_watchlist) [none]: [ProtectChain: An Anchored Permissioned Ledger for Proof of Anteriority of Authored Works](https://datatracker.ietf.org/doc/draft-tempobono-protectchain/) — This document specifies ProtectChain, a permissioned, hash-chained
   and cryptographically signed ledger whose purpose is to produce
   verifiable evidence that a given digital work already existed no
   later than a given point in time, under an authorship claim made by
   an identified account.

   ProtectChain records only cryptographic digests and pseudonymous
   identifiers; the work itself never enters the ledger.  Because all
   initial authorities may be operated by a single organization, every
   block is also anchored to independent public time references, so that
   the upper bound on a record's date does not rest on the operator's
   assertion.

   This document is deliberately explicit about the limits of the
   evidence produced: an anchor establishes that data existed _no later
   than_ a given instant; it does not establish the exact instant of
   creation, nor does it establish authorship or originality.
- **draft-vicente-lamps-rotation-envelope-03** (new-draft, score 4, adjacent_watchlist) [none]: [CA-Side Post-Quantum Rotation Envelope for X.509 Issuance Continuity](https://datatracker.ietf.org/doc/draft-vicente-lamps-rotation-envelope/) — This document defines the X.509 Post-Quantum Rotation Envelope
   extension, a Certification Authority (CA) side commitment mechanism
   that allows an issuing CA to publish, sign, and bind to its issued
   certificates a machine-verifiable guarantee of post-quantum (PQ) or
   PQ/T hybrid issuance continuity across the CA's own key-rotation
   boundaries.  The mechanism is complementary to, and does not overlap
   with, subject-side commitments such as the continuityPeriod field
   defined in [I-D.reddy-lamps-x509-pq-commit]: where that draft
   captures the CA's continuity obligation to continue presenting PQ or
   composite certificates after the current certificate's notAfter, this
   document captures the issuing CA's parallel obligation to remain
   capable of issuing such certificates across its own root and
   intermediate key rotations during the same migration window.

   The Rotation Envelope extension carries a SHA-384 hash of a CA-
   published, signed JSON manifest hosted at a stable /.well-known/pki-
   rotation-envelope URI under the issuer's authorityInfoAccess host.
   The manifest enumerates: (a) the algorithm identifiers the CA commits
   to continue supporting for issuance through a stated envelopeNotAfter
   date, (b) the successor-CA SubjectPublicKey hashes already
   provisioned for the next CA key generation, and (c) the OCSP and CRL
   distribution endpoints that will remain authoritative through the
   envelope window.  Relying parties that understand the extension can
   verify, at any time during the current certificate's lifetime, that
   the CA's published continuity posture matches what was bound at
   issuance, detecting silent CA-side degradation, unannounced CA
   replacement, or rollback of PQ-capable issuance commitments.

   This document is filed independently and is intended to be considered
   alongside, not in place of, [I-D.reddy-lamps-x509-pq-commit].  The
   two mechanisms address orthogonal sides of the same PQ migration
   window: subject-side declaration of intent (Reddy et al.) and CA-side
   guarantee of issuance capability (this document).
- **draft-woodcock-faltstrom-external-registry-rrtypes-01** (new-draft, score 4, verifiable_claims) [none]: [External-Registry DNS Resource Record Types: UNECE and ISO](https://datatracker.ietf.org/doc/draft-woodcock-faltstrom-external-registry-rrtypes/) — This document defines two DNS resource record types, UNECE and ISO,
   which convey numeric values paired with codes drawn from registries
   maintained by external standards organizations: the United Nations
   Economic Commission for Europe (UNECE) and the International
   Organization for Standardization.  Neither proposed RRTYPE duplicates
   the external registries into IANA registries; each carries codes
   verbatim and uses the semantics defined by the external maintainer.
   The document specifies presentation and wire formats for both types,
   records the assignment of two decimal RRTYPE identifiers under the
   Expert Review process of BCP 42, and suggests a common design pattern
   that may serve as a model for future RRTYPEs seeking to make external
   registries usable from the DNS without duplication.

## Adjacent / watchlist

- **draft-chen-sidrops-sispi-06** (new-draft, score 3, trust_infrastructure) [none]: [A Profile of Signed SAVNET-Peering Information (SiSPI) Object for Deploying Inter-domain SAVNET](https://datatracker.ietf.org/doc/draft-chen-sidrops-sispi/) — This document defines a "Signed SAVNET-Peering Information" (SiSPI)
   object, a Cryptographic Message Syntax (CMS) protected content type
   included in the Resource Public Key Infrastructure (RPKI).  A SiSPI
   object is a digitally signed object that carries an attestation for a
   single Autonomous System (AS) participating in inter-domain SAVNET.
   A valid SiSPI object confirms that the holder of the listed AS number
   has published the attestation indicating its participation in inter-
   domain SAVNET and its willingness to establish SAVNET peering
   relationships.
- **draft-claise-green-capability-discovery-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
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
- **draft-das-ntn-rf-execution-finality-01** (new-draft, score 3, core_identity) [none]: [RF Enable Is Not Transmit Authority: Finality for LEO/NTN and Inter-Satellite Control](https://datatracker.ietf.org/doc/draft-das-ntn-rf-execution-finality/) — A LEO constellation computer can compute a transmit burst, a beam
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
- **draft-dong-sidrops-rpki-rtr-moa-pdu-01** (new-draft, score 3, authorization) [none]: [IPv6 Mapping Prefix PDU for the RPKI-Router Protocol](https://datatracker.ietf.org/doc/draft-dong-sidrops-rpki-rtr-moa-pdu/) — This document defines a new Protocol Data Unit (PDU) type for the
   RPKI to Router Protocol to convey Mapping Origin Authorization (MOA)
   information from RPKI caches to routers.  The new PDU, named the
   "IPv6 Mapping Prefix" PDU, carries the authorization mapping between
   one or more IPv4 prefix and their corresponding authorized IPv6
   mapping prefix.  This extension enables routers to perform Mapping
   Origin Validation (MOV) for IPv4-to-IPv6 address mapping
   announcements in IPv6-only underlay networks.
- **draft-gai-intarea-ip-tunnel-node-security-01** (new-draft, score 3, authorization) [none]: [Security Requirements for IP Tunnel Nodes](https://datatracker.ietf.org/doc/draft-gai-intarea-ip-tunnel-node-security/) — IP tunnels conceal passenger-packet fields from devices on the
   delivery path and create a new forwarding and policy boundary at
   decapsulation.  If a tunnel node accepts delivery packets from an
   unauthorized source, or if it forwards a decapsulated passenger
   packet without applying the policy for the exposed packet and
   forwarding domain, the node can enable source-address spoofing,
   unauthorized transit, policy bypass, or resource-exhaustion attacks.

   This document specifies generic security requirements for IP tunnel
   ingress, egress, and relay nodes.  The requirements cover explicit
   enablement, peer and passenger-packet authorization, source and
   forwarding-scope validation, nested tunneling, IPv6 extension
   headers, ICMP and Path MTU Discovery, resource controls, and
   telemetry.  They apply to configured IP-in-IP, IPv6 tunneling, GRE,
   and enabled IPv4/IPv6 transition mechanisms.  This document does not
   define a new encapsulation or replace protocol-specific processing
   rules.
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
- **draft-hi-ccamp-cmis-control-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for CMIS Access and Control](https://datatracker.ietf.org/doc/draft-hi-ccamp-cmis-control-yang/) — This document provides YANG data models for accessing and controlling
   CMIS in order to manage pluggable Digital Coherent Optics
   transceivers equipped in a router or a switch from outside the
   platform device.  CMIS provides custom pages that can be defined by
   the module vendor for its own usage, allowing the capabilities of the
   optics devices to be extended.  These YANG modules also allow the
   utilization of CMIS custom pages as a generic control mechanism.  The
   models complement abstracted data models for coherent pluggables:
   they provide governed access to opaque, vendor-specific attributes
   (e.g., those exposed via CMIS custom pages) and a transitional path
   for standardized features that the host NOS does not yet support.
- **draft-httpauth-payment-01** (new-draft, score 3, core_identity) [none]: [The "Payment" HTTP Authentication Scheme](https://datatracker.ietf.org/doc/draft-httpauth-payment/) — This document defines the "Payment" HTTP authentication scheme,
   enabling HTTP resources to require a payment challenge to be
   fulfilled before access.  The scheme extends HTTP Authentication,
   using the HTTP 402 "Payment Required" status code.

   The protocol is payment-method agnostic, supporting any payment
   network or currency through registered payment method identifiers.
   Specific payment methods are defined in separate payment method
   specifications.
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
- **draft-ietf-dkim-dkim2-bcp-01** (new-draft, score 3, core_identity) [dkim]: [DKIM2 Best Practices](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-bcp/) — [DKIM2] and its associated documents describe the DomainKeys
   Identified Mail v2 (DKIM2) email authentication protocol.  DKIM2 is
   designed to address shortcomings in email authentication protocols
   and mechanisms released prior to DKIM2, specifically SPF [RFC7208],
   DKIM [RFC6376], DMARC [RFC9989], and ARC [RFC8617].  This document
   discusses best practices for signing, handling, and validating
   messages that carry DKIM2 signatures, and for interoperating with the
   authentication protocols and mechanisms that preceded DKIM2.
- **draft-ietf-green-power-and-energy-yang-04** (new-draft, score 3, adjacent_watchlist) [green]: [Power and Energy YANG Module](https://datatracker.ietf.org/doc/draft-ietf-green-power-and-energy-yang/) — This document defines the YANG data model for Power and Energy
   monitoring of devices within or connected to communication networks.
- **draft-ietf-httpbis-pre-denied-01** (new-draft, score 3, adjacent_watchlist) [httpbis]: [The Purpose Declined HTTP Status Code](https://datatracker.ietf.org/doc/draft-ietf-httpbis-pre-denied/) — This specification defines an HTTP status code to indicate that the
   server is denying a request based upon its declared purpose.
- **draft-ietf-ipsecme-sha3-02** (new-draft, score 3, core_identity) [ipsecme]: [Use of KMAC and SHAKE in the Internet Key Exchange Protocol Version 2 (IKEv2) and IPsec](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-sha3/) — This document specifies the use of KMAC128 and KMAC256 within the
   Internet Key Exchange Version 2 (IKEv2), Encapsulating Security
   Payload (ESP), and Authentication Header (AH) protocols.  These
   algorithms can be used as integrity protection algorithms for ESP, AH
   and IKEv2, and as Pseudo-Random Functions (PRFs) for IKEv2.
   Requirements for supporting signature algorithms in IKEv2 that use
   SHA3-256, SHA3-384, SHA3-512, SHAKE128 and SHAKE256 are also
   specified.
- **draft-ietf-ivy-network-inventory-topology-11** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Network Data Model for Inventory Topology Mapping](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-topology/) — This document specifies a YANG data model that extends the network
   topology data model (RFC 8345) to map network topologies with
   inventories.  The data model introduces the "inventory-topology"
   network type and augmentations for physical entity mappings and
   capabilities, which may be used by any overlay network topology for
   service provisioning validation, network maintenance, and capacity
   planning.
- **draft-ietf-ivy-passive-network-inventory-01** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Data Model for Passive Network Inventory](https://datatracker.ietf.org/doc/draft-ietf-ivy-passive-network-inventory/) — This document presents a YANG data model for tracking and managing
   passive network inventory.  The model augments the base network
   inventory model.
- **draft-ietf-lamps-cms-euf-cma-signeddata-03** (new-draft, score 3, adjacent_watchlist) [lamps]: [Best Practices for Signed Attributes in CMS SignedData](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-euf-cma-signeddata/) — The Cryptographic Message Syntax (CMS) has different signature
   verification behaviour based on whether signed attributes are present
   or not.  This results in a potential existential forgery
   vulnerability in CMS and protocols which use CMS.  This document
   describes the vulnerability and lists mitigations and best practices
   to avoid it.  This document updates RFC 5652 by prohibiting the use
   of the id-data content type for new uses of the CMS SignedData type.
- **draft-ietf-mpls-stamp-pw-21** (new-draft, score 3, core_identity) [mpls]: [Encapsulation of Simple Two-Way Active Measurement Protocol for LSPs and Pseudowires in MPLS Networks](https://datatracker.ietf.org/doc/draft-ietf-mpls-stamp-pw/) — This document specifies encapsulations for the Simple Two-Way Active
   Measurement Protocol (STAMP), defined in RFC 8762, and its optional
   extensions, defined in RFC 8972, in MPLS networks.  It specifies the
   encapsulation of STAMP test packets for point-to-point Label Switched
   Paths (LSPs) and point-to-point single-segment Pseudowires (PWs),
   with or without an IP/UDP header, so that the test packets experience
   the same forwarding and Equal-Cost Multi-Path (ECMP) behavior as the
   data traffic being measured.  In addition, two new MPLS Generic
   Associated Channel (G-ACh) types are defined.  The procedures
   specified in this document are intended for deployment in a single
   network administrative domain.

   This document updates RFC 8762 and RFC 8972 to allow STAMP to operate
   without an IP/UDP header when STAMP test packets are carried over
   MPLS LSPs and PWs, and specifies the resulting changes to the
   processing of the STAMP session identifier, the IPv4 TTL and IPv6 Hop
   Limit, and the STAMP TLV extensions.
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
- **draft-ietf-ocm-integration-protocol-00** (new-draft, score 3, adjacent_watchlist) [ocm]: [Open Cloud Mesh Integration Protocol](https://datatracker.ietf.org/doc/draft-ietf-ocm-integration-protocol/) — The Open Cloud Mesh Integration Protocol (OCM-IP) defines how an Open
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
- **draft-ietf-openpgp-persistent-symmetric-keys-04** (new-draft, score 3, core_identity) [openpgp]: [Persistent Symmetric Keys in OpenPGP](https://datatracker.ietf.org/doc/draft-ietf-openpgp-persistent-symmetric-keys/) — This document defines a new packet and algorithm for the OpenPGP
   standard (RFC 9580) to support persistent symmetric keys, for message
   encryption using authenticated encryption with additional data (AEAD)
   and for message authentication using AEAD authentication tags.  This
   enables the use of symmetric cryptography for data storage (and other
   contexts that do not require asymmetric cryptography), for improved
   performance, smaller keys, and improved resistance to quantum
   computing.
- **draft-ietf-opsawg-collected-data-manifest-15** (new-draft, score 3, adjacent_watchlist) [opsawg]: [A Data Manifest for Contextualized Telemetry Data](https://datatracker.ietf.org/doc/draft-ietf-opsawg-collected-data-manifest/) — Network platforms use Network Telemetry, such as YANG-Push, to
   continuously stream information, including both counters and state
   information.  This document describes the metadata that ensure that
   the collected data can be interpreted correctly.  This document
   specifies the Data Manifest, composed of two YANG data models (the
   Platform Manifest and the non-normative Data Collection Manifest).
   These YANG modules are specified at the network level (e.g., network
   controllers) to provide a model that encompasses several network
   platforms.  The Data Manifest must be streamed and stored along with
   the data, up to the collection and analytics systems to keep the
   collected data fully exploitable by the data scientists and relevant
   tools.  Additionally, this document specifies an augmentation of the
   YANG-Push model to include the actual collection period, in case it
   differs from the configured collection period.
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
- **draft-ietf-tls-tlsflags-18** (new-draft, score 3, adjacent_watchlist) [tls]: [A Flags Extension for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-tlsflags/) — A number of extensions are proposed in the TLS working group that
   carry no interesting information except the 1-bit indication that a
   certain optional feature is supported.  Such extensions take 4 octets
   each.  This document defines a flags extension that can provide such
   indications at an average marginal cost of 1 bit each.  More
   precisely, it provides as many flag extensions as needed at 4 + the
   order of the last set bit divided by 8.
- **draft-irtf-cfrg-rsa-guidance-10** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Implementation Guidance for the PKCS #1 RSA Cryptography Specification](https://datatracker.ietf.org/doc/draft-irtf-cfrg-rsa-guidance/) — This document lists additions to RFC 8017.  Specifically, it provides
   guidance to implementers of the standard to protect against side-
   channel attacks.  It also recommends against the RSAES-PKCS-v1_5
   encryption scheme, and provides an alternative depadding algorithm
   that protects against side-channel attacks raising from users of
   vulnerable APIs.  The purpose of this specification is to increase
   security of RSA implementations.  The document is a product of the
   Crypto Forum Research Group (CFRG).
- **draft-sardar-rats-sec-cons-05** (new-draft, score 3, trust_infrastructure) [none]: [Guidelines for Security Considerations of RATS](https://datatracker.ietf.org/doc/draft-sardar-rats-sec-cons/) — This document aims to provide guidelines and best practices for
   writing security considerations for technical specifications for RATS
   targeting the needs of implementers, researchers, and protocol
   designers.  In particular, it discusses some of the 'bottom turtle'
   issues.  This is a work-in-progress, and the current version mainly
   presents an outline of the topics that future versions will cover in
   more detail.

   *  Corrections in published RATS RFCs

   *  Security concerns in two RATS drafts

   *  General security guidelines, baseline, or template for RATS
- **draft-vitap-ml-dsa-webauthn-05** (new-draft, score 3, core_identity) [none]: [ML-DSA for Web Authentication](https://datatracker.ietf.org/doc/draft-vitap-ml-dsa-webauthn/) — This document describes implementation of Passwordless authentication
   in Web Authentication (WebAuthn) using Module-Lattice-Based Digital
   Signature Standard (ML-DSA), a Post-Quantum Cryptography (PQC)
   digital signature scheme defined in FIPS 204.
- **draft-zheng-ccamp-client-pm-yang-16** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Client Signal Performance Monitoring](https://datatracker.ietf.org/doc/draft-zheng-ccamp-client-pm-yang/) — A transport network is a server-layer network to provide connectivity
   services to its client.  Given the client signal is configured, the
   followup function for performance monitoring, such as latency and bit
   error rate, would be needed for network operation.

   This document describes the data model to support the performance
   monitoring functionalities.
- **draft-ietf-aipref-vocab-08** (new-draft, score 2, ignored_after_review) [aipref]: [A Vocabulary For Expressing AI Usage Preferences](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/) — This document defines a vocabulary for expressing preferences
   regarding how digital assets are used by automated processing
   systems.  This vocabulary allows for the declaration of restrictions
   or permissions for use of digital assets by such systems.
- **draft-jacobs-web4-evidence-receipts-00** (new-draft, score 2, ignored_after_review) [none]: [Web4 Evidence Receipts](https://datatracker.ietf.org/doc/draft-jacobs-web4-evidence-receipts/) — This document defines durable, cryptographically verifiable receipts
   for assessment, authority, policy, claim, and node-lifecycle events
   without requiring publication of protected evidence.
- **draft-sweetser-bcp-rpki-ca-02** (new-draft, score 2, ignored_after_review) [none]: [Operational Guidelines for RPKI Delegated Certification Authorities](https://datatracker.ietf.org/doc/draft-sweetser-bcp-rpki-ca/) — This document provides operational guidelines for Resource Public Key
   Infrastructure (RPKI) delegated Certification Authorities (CAs) and
   registry operators managing such delegations.  It addresses common
   operational issues including CA availability problems, publication
   quality issues, and lifecycle management.  The guidelines aim to
   improve the overall health and efficiency of the RPKI ecosystem by
   establishing best practices for CA operations and delegation
   management.
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
- **draft-jacobs-web4-federation-policy-00** (new-draft, score 1, core_identity) [none]: [Web4 Federation Policy Advertisement](https://datatracker.ietf.org/doc/draft-jacobs-web4-federation-policy/) — This document defines machine-readable advertisements for federation
   policies, including authority, versions, profiles, evidence formats,
   retention, challenges, appeals, revocation, disclosure, jurisdiction,
   proof, and status.

## Ignored after review

- **draft-abinabraham-vrrp-unicast-03** (new-draft, score 0, ignored_after_review) [none]: [Unicast Support for the Virtual Router Redundancy Protocol (VRRP)](https://datatracker.ietf.org/doc/draft-abinabraham-vrrp-unicast/) — The Virtual Router Redundancy Protocol (VRRP) Version 3 as specified
   in RFC 9568 assumes multicast operation on a shared LAN.  Some
   deployments require the VRRP first-hop redundancy function but cannot
   use multicast delivery for VRRP advertisements.  This document
   updates RFC 9568 by defining an optional configured unicast mode for
   VRRP Version 3 in which advertisements are sent to configured peer
   addresses rather than to the VRRP multicast group.  The VRRP packet
   format, state machine, protocol number, virtual IP semantics, and
   Virtual Router MAC behavior remain unchanged from RFC 9568.
- **draft-admnr-lsr-igp-measurement-group-04** (new-draft, score 0, ignored_after_review) [none]: [Advertising IGP Active Measurement Groups in Router Capabilities](https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/) — This document defines IGP capability advertisements for measurement
   group membership for Active Measurement Protocols (AMPs) such as
   TWAMP and STAMP.  An IS-IS capability sub-TLV is defined for IS-IS
   and an OSPF Router Information (RI) LSA TLV is defined for OSPFv2 and
   OSPFv3.  The mechanism allows IGP routers to discover other routers
   participating in different measurement groups, enabling automatic
   discovery of measurement endpoints throughout an IS-IS or OSPF
   routing domain.  The solution uses a Group ID to identify measurement
   group membership, where the same interface address (IPv4 or IPv6) may
   be used for multiple measurement groups.  A corresponding BGP - Link
   State (BGP-LS) node-level attribute is defined to distribute
   measurement group membership beyond a single IGP domain.
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
- **draft-besleaga-sustainability-wellknown-06** (new-draft, score 0, ignored_after_review) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI.  This
   URI provides a uniform, out-of-band convention for web servers and
   digital services to publish aggregated environmental impact, energy
   consumption, and carbon footprint metrics for a declared reporting
   subject -- typically the publishing origin itself.

   The convention publishes a single, cacheable JSON document per
   origin, described by formal schemas and discoverable at a fixed
   location without prior arrangement, so that environmental disclosures
   can be located, validated, and ingested automatically.  Publication
   is voluntary, and the metrics are self-asserted claims of the
   publisher, linked to the publisher's methodology and supporting
   evidence.
- **draft-bruhns-securitytxt-product-security-00** (new-draft, score 0, ignored_after_review) [none]: [Product Security Fields for security.txt](https://datatracker.ietf.org/doc/draft-bruhns-securitytxt-product-security/) — This document registers two new fields for the security.txt file
   format defined in RFC 9116: "Product-Security" and "Product-Security-
   Policy".  They allow an organisation to publish a dedicated contact
   and disclosure policy for vulnerabilities in the products it
   manufactures, distinct from the contact for vulnerabilities in its
   own web presence and infrastructure.  The fields are optional and
   fully backward compatible with existing security.txt parsers.
- **draft-buckeyne-jsox-format-01** (new-draft, score 0, ignored_after_review) [none]: [The JavaScript Object eXchange (JSOX) Data Interchange Format](https://datatracker.ietf.org/doc/draft-buckeyne-jsox-format/) — JavaScript Object eXchange (JSOX) is a lightweight, text-based,
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
- **draft-carpenter-gendispatch-anachronisms-07** (new-draft, score 0, ignored_after_review) [none]: [Some Anachronisms and Gaps in IETF Standards Process Documents](https://datatracker.ietf.org/doc/draft-carpenter-gendispatch-anachronisms/) — This document discusses some aspects of documents describing the IETF
   standards process that have been overtaken by events, as well as
   identifying some gaps.  It covers the six-month expiry of Internet-
   Drafts, the reality of the two-stage standards process, and various
   other issues.  This draft is posted only to open a discussion.
- **draft-chuang-dkim2-sender-policy-01** (new-draft, score 0, ignored_after_review) [none]: [DKIM2 Sender Policy](https://datatracker.ietf.org/doc/draft-chuang-dkim2-sender-policy/) — This document updates DMARC RFC9989 for DKIM2.  In particular DKIM2
   verification supports MTA relay forwarding with message modifications
   through multiple MTAs, so this updates DMARC to support those
   scenarios as well.  While DMARC defines a RFC5322 From alignment
   constraint with an enforcement policy if validation fails, this
   generalizes and separates enforcement policy from constraint
   validation policies.  This provides a mechanism for MTAs to declare
   support for DKIM2 through the DMARC DNS policy record that helps
   secure DKIM2 from downgrade attacks.
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
- **draft-codere-ldapsyntax-11** (new-draft, score 0, ignored_after_review) [none]: [Lightweight Directory Access Protocol (LDAP): Additional Syntaxes](https://datatracker.ietf.org/doc/draft-codere-ldapsyntax/) — This document registers additional syntax definitions for use in
   Lightweight Directory Access Protocol (LDAP) directory and Directory
   services series X.500.  This includes widely used datatypes and
   syntaxes.
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
- **draft-demos-ra-mtsv-00** (new-draft, score 0, ignored_after_review) [none]: [Multi-Sheet Tab-Separated Values (MTSV)](https://datatracker.ietf.org/doc/draft-demos-ra-mtsv/) — This document defines Multi-Sheet Tab-Separated Values (MTSV), a text
   format that carries one or more sheets of tab-separated values in a
   single file.  MTSV is TSV with one additional dimension: sheets are
   separated by the ASCII form feed (FF) character.  A TSV file that
   contains no FF, and no CR other than in CRLF line breaks, is an MTSV
   file.  This document also registers the text/prs.mtsv media type.
- **draft-grimminck-safe-ioc-sharing-14** (new-draft, score 0, ignored_after_review) [none]: [Safe and Reversible Sharing of Malicious URLs and Indicators](https://datatracker.ietf.org/doc/draft-grimminck-safe-ioc-sharing/) — This document codifies a consistent and reversible convention used in
   the threat intelligence and security communities for sharing
   potentially malicious indicators of compromise (IOCs), such as URLs,
   IP addresses, email addresses, and domain names.  It describes an
   obfuscation format that reduces the risk of accidental execution or
   activation when IOCs are displayed or transmitted.  The
   transformation renders an indicator syntactically invalid as a URI
   while keeping it recognizable to a human reader, and the original
   value can be recovered deterministically.  Safe-IOC strings are a
   textual rendering convention, not URIs, and are not intended to be
   processed by generic URI parsers.  These conventions aim to improve
   interoperability among tools and feeds that exchange threat
   intelligence data.
- **draft-hoffman-rootcache-02** (new-draft, score 0, ignored_after_review) [none]: [RootCache: Filling Resolver Caches with Root Zone Records](https://datatracker.ietf.org/doc/draft-hoffman-rootcache/) — Some DNS recursive resolver operators want to prevent snooping by
   third parties of requests sent to DNS root servers.  Resolvers can
   reduce the number of queries sent to root server, and thus prevent
   observation of requests, by caching a copy of the full root zone.
   This document shows how a resolver can securely receive the full root
   zone and put it into the resolver's cache.

   This document obsoletes RFC 8806.
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
- **draft-ietf-anima-rfc8366bis-36** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Onboarding Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
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
- **draft-ietf-asdf-sdf-nonaffordance-05** (new-draft, score 0, ignored_after_review) [asdf]: [Semantic Definition Format (SDF) Extension for Non-Affordance Information](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-nonaffordance/) — This document describes an extension to the Semantic Definition
   Format (SDF) for representing non-affordance information of Things,
   such as physical, contextual, and descriptive metadata.  This
   extension introduces a new class keyword, sdfContext, that enables
   comprehensive modeling of Things and improves semantic clarity.
- **draft-ietf-avtcore-rtcp-green-metadata-17** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Control Protocol (RTCP) Messages for Temporal-Spatial Resolution](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtcp-green-metadata/) — The RTCP messages specified in this document enable receivers to
   provide feedback to the senders and thus allow for short-term
   adaptation and feedback-based energy efficient mechanisms to be
   implemented.  The messages have broad applicability in point-to-point
   real-time video communication services.  Specifically, the messages
   can be used to convey the video decoder feedback metadata to the
   encoder to adapte the decoder energy consumption as defined in the
   ISO/IEC International Standard 23001-11, known as Energy Efficient
   Media Consumption (Green metadata), developed by the ISO/IEC JTC
   1/SC29/WG3 MPEG Systems.
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
- **draft-ietf-bess-evpn-l3mh-proto-01** (new-draft, score 0, ignored_after_review) [bess]: [EVPN multi-homing support for L3 services](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-l3mh-proto/) — This document describes the use of EVPN Ethernet Segment Link
   Aggregation Group (ES-LAG) technology to provide multi-homing
   redundancy for Layer 3 services.  The solution synchronizes ARP/ND,
   multicast state, and IGP routes between redundant PEs without
   requiring Layer 2 constructs or proprietary Inter-Chassis
   Communication protocols.
- **draft-ietf-bmwg-savnet-sav-benchmarking-04** (new-draft, score 0, ignored_after_review) [bmwg]: [Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation](https://datatracker.ietf.org/doc/draft-ietf-bmwg-savnet-sav-benchmarking/) — This document defines methodologies for benchmarking the performance
   of intra-domain and inter-domain source address validation (SAV)
   mechanisms.  SAV mechanisms are utilized to generate SAV rules that
   prevent source address spoofing.  The methodology treats a SAV device
   as a black box and is therefore agnostic to the specific SAV
   mechanism and implementation used by the device.  This document
   defines test setups, performance indicators, and test cases for SAV
   accuracy, control-plane and data-plane performance, and resource
   utilization.
- **draft-ietf-calext-jscalendar-icalendar-27** (new-draft, score 0, ignored_after_review) [calext]: [JSCalendar: Converting from and to iCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-jscalendar-icalendar/) — This document defines how to convert calendaring information between
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
- **draft-ietf-dtn-bp-sand-04** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle Protocol (BP) Secure Advertisement and Neighborhood Discovery (SAND)](https://datatracker.ietf.org/doc/draft-ietf-dtn-bp-sand/) — This document defines the Secure Advertisement and Neighborhood
   Discovery (SAND) protocol for Bundle Protocol version 7 (BPv7) within
   a delay-tolerant network (DTN).  This protocol defines a general
   purpose advertisement mechanism with an initial set of message and
   data types able to be advertised by participating nodes in a BPv7
   network.  The focus of this document is for advertisement to
   topological neighbors about local neighborhoods but can be expanded
   upon in the future through extension points.
- **draft-ietf-grow-bmp-stats-informational-tlv-01** (new-draft, score 0, ignored_after_review) [grow]: [BMP Statistics Information TLV](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-stats-informational-tlv/) — The BGP Monitoring Protocol (BMP) defines statistics reports that
   provide periodic snapshots of various BGP-related metrics.  When
   statistics are reported periodically, the snapshot values may not
   reflect the variations that occurred between reporting intervals.
   This document defines a Statistics Information TLV that can be used
   to convey additional statistical information about BMP gauge-type
   statistics during the reporting period.  This TLV reports the minimum
   and maximum values observed (with timestamps indicating when they
   occurred), along with additional statistical measures such as
   average, percentiles, or snapshot values.  This enables BMP
   collectors to better understand the dynamics of monitored statistics
   even when the reported snapshot values appear constant.
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
- **draft-ietf-intarea-legacy-registries-00** (new-draft, score 0, ignored_after_review) [intarea]: [Updates to Legacy IANA Registries](https://datatracker.ietf.org/doc/draft-ietf-intarea-legacy-registries/) — IANA maintains several registries that were created for IPv4.  As the
   IPv4 core specification is no longer being extended and as some other
   registries do not have a defined IANA registration procedure, these
   registries need to be updated to indicate a registration procedure or
   to reflect the current practice that defining such extensions is not
   recommended.
- **draft-ietf-intarea-rfc8335bis-06** (new-draft, score 0, ignored_after_review) [intarea]: [PROBE: A Utility for Probing Interfaces](https://datatracker.ietf.org/doc/draft-ietf-intarea-rfc8335bis/) — This document specifies a network diagnostic tool called PROBE.
   PROBE is similar to PING in that it can be used to query the status
   of a probed interface, but it differs from PING in that it does not
   require bidirectional connectivity between the probing and probed
   interfaces.  Instead, PROBE requires bidirectional connectivity
   between the probing interface and a proxy interface.  The proxy
   interface can reside on the same node as the probed interface, or it
   can reside on a node to which the probed interface is directly
   connected.  This document updates RFC 4884 and obsoletes RFC 8335.
- **draft-ietf-ippm-alt-mark-deployment-09** (new-draft, score 0, ignored_after_review) [ippm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
- **draft-ietf-ippm-stamp-ext-hdr-13** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet IP Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ext-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
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
- **draft-ietf-mailmaint-smtputf8-syntax-05** (new-draft, score 0, ignored_after_review) [mailmaint]: [SMTPUTF8 Email Addresses](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-smtputf8-syntax/) — RFC 6532 extends the internet email format to allow UTF8 in many
   contexts.  This document restricts the set of allowed addresses in
   header fields slightly, and thereby simplifies use of these
   addresses.

   This is one of a pair of documents.  This one is simple to implement
   and contains only globally viable rules.  Its companion has more
   complex rules, takes regional usage into account, and describes
   addresses that can be read by some community and cut-and-pasted in
   some locale.
- **draft-ietf-mediaman-6838bis-10** (new-draft, score 0, ignored_after_review) [mediaman]: [Media Type Specifications and Registration Procedures](https://datatracker.ietf.org/doc/draft-ietf-mediaman-6838bis/) — This document defines procedures for the specification and
   registration of media types for use in HTTP, MIME, and other Internet
   protocols.

   It obsoletes [RFC6838] and [RFC9694].  Note that [RFC4289] is also
   part of BCP 13, and addresses registration of MIME External Body
   Access Types and Transfer Encodings.
- **draft-ietf-moq-transport-21** (new-draft, score 0, ignored_after_review) [moq]: [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) — This document defines Media over QUIC Transport (MOQT), a publish/
   subscribe protocol that runs over QUIC and WebTransport.  MOQT
   leverages the features of these transports, such as streams,
   datagrams, priorities, and partial reliability.  MOQT operates both
   point-to-point and through intermediate relays, enabling scalable
   low-latency delivery.  Despite its name, MOQT is media agnostic and
   can be used for a wide range of use cases.
- **draft-ietf-mpls-mna-ioam-14** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Actions for In Situ Operations, Administration, and Maintenance](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
   in RFC 9197, collects operational and telemetry information in the
   packet using IOAM-Data-Fields while the packet traverses a path
   between two points in the network.  Several IOAM Option-Types are
   available, for example, Pre-allocated Trace, Proof of Transit (POT),
   Edge-to-Edge (E2E), and Incremental Trace, that can be used to
   collect information for calculating various performance metrics.  RFC
   9326 defines the IOAM Direct Export (IOAM-DEX) Option-Type, which is
   used as a trigger for IOAM data to be directly exported or locally
   aggregated without being pushed into in-flight data packets.

   MPLS Network Action (MNA) mechanisms indicate actions to be performed
   on any combination of Label Switched Paths, MPLS packets, and the
   node itself, and to transport data needed for these actions.  This
   document defines MNAs to collect and transport the operational state
   and telemetry information using IOAM-Data-Fields as well as IOAM-DEX.
- **draft-ietf-netconf-quic-call-home-01** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Call Home and RESTCONF Call Home Using QUIC](https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-call-home/) — This RFC extends NETCONF Call Home and RESTCONF Call Home [RFC 8071]
   to support the QUIC protocol [RFC 9000].
- **draft-ietf-netconf-yang-notifications-versioning-15** (new-draft, score 0, ignored_after_review) [netconf]: [Support of Versioning in YANG Notifications Subscription](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-notifications-versioning/) — This document defines a YANG module which extends the YANG-Push
   Subscription mechanism to enforce that particular revisions or
   semantic versions are used when configuring or establishing a
   Subscription.  It also extends the YANG-Push Subscription state
   change Notifications to include additional context about the YANG
   schema associated with the Subscription.
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
- **draft-ietf-nfsv4-uncacheable-files-14** (new-draft, score 0, ignored_after_review) [nfsv4]: [Adding an Uncacheable File Data Attribute to NFSv4.2](https://datatracker.ietf.org/doc/draft-ietf-nfsv4-uncacheable-files/) — Network File System version 4.2 (NFSv4.2) clients commonly perform
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
- **draft-ietf-nvo3-rfc7348bis-08** (new-draft, score 0, ignored_after_review) [nvo3]: [Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks](https://datatracker.ietf.org/doc/draft-ietf-nvo3-rfc7348bis/) — This document specifies Virtual eXtensible Local Area Network
   (VXLAN), which is used to address the need for overlay networks
   within virtualized data centers accommodating multiple tenants.  The
   scheme and the related protocols can be used in networks for cloud
   service providers and enterprise data centers.  This document
   obsoletes RFC 7348, which documented the deployed VXLAN protocol for
   the benefit of the Internet community, and moves the VXLAN
   specification to the IETF document stream, allowing for the creation
   of extensions to VXLAN that require additions to the VXLAN header and
   their registration with IANA.  The format and processing described
   here are fully compatible with those in RFC7348.
- **draft-ietf-ocm-mls-federated-groups-00** (new-draft, score 0, ignored_after_review) [ocm]: [Federated Groups in Open Cloud Mesh using Messaging Layer Security](https://datatracker.ietf.org/doc/draft-ietf-ocm-mls-federated-groups/) — This document defines an extension to the Open Cloud Mesh (OCM)
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
- **draft-ietf-opsawg-ipfix-quic-header-00** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of QUIC Information in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-quic-header/) — This document introduces new IP Flow Information Export (IPFIX)
   Information Elements to identify a set of QUIC related information,
   which contained in QUIC Header, QUIC Frame and Stream that traffic is
   being forwarded along with.
- **draft-ietf-pce-flexible-grid-17** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-pce-sr-p2mp-policy-21** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable an architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
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
- **draft-ietf-scone-protocol-08** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-sidrops-publication-server-bcp-11** (new-draft, score 0, ignored_after_review) [sidrops]: [Best Practices for Operating Resource Public Key Infrastructure (RPKI) Publication Services](https://datatracker.ietf.org/doc/draft-ietf-sidrops-publication-server-bcp/) — This document describes best current practices for operating an RFC
   8181 (A Publication Protocol for the Resource Public Key
   Infrastructure (RPKI)) publication engine and its associated publicly
   accessible rsync (RFC 5781) and RPKI Repository Delta Protocol (RRDP)
   (RFC 8182) repositories.
- **draft-ietf-spring-stamp-srpm-mpls-07** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SR-MPLS networks using the Simple Two-
   Way Active Measurement Protocol (STAMP), as specified in RFC 8762,
   along with its optional extensions specified in RFC 8972 and further
   augmented in RFC 9503.  The described procedures are used for SR-MPLS
   paths (including Segment Lists of SR-MPLS Policies, SR-MPLS IGP best
   paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo) paths), as well
   as Layer-3 and Layer-2 services carried over the SR-MPLS paths.
- **draft-ietf-spring-stamp-srpm-srv6-04** (new-draft, score 0, ignored_after_review) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
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
- **draft-ietf-tiptop-quic-profile-00** (new-draft, score 0, ignored_after_review) [tiptop]: [QUIC Profile for Deep Space](https://datatracker.ietf.org/doc/draft-ietf-tiptop-quic-profile/) — Deep space communications involve long delays (e.g., the Earth to
   Mars one-way delay is ~4-20 minutes) and often intermittent
   communications.  In this context, the default transport parameters of
   QUIC stacks, tuned for the terrestrial Internet, are not suitable for
   deep space.  This document defines a QUIC profile for deep space.  It
   provides guidance on how to estimate and set transport parameters,
   advice to space mission operators and application developers on how
   to configure QUIC for the deep space use case, and guidance to QUIC
   stack developers on properly exposing the required transport
   parameters in their API.
- **draft-ietf-v6ops-6mops-10** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (network segment, VLAN, SSID etc).  The proposed
   approach enables smooth and incremental transition from dual-stack to
   IPv6-only network by allowing IPv6-capable devices to remain
   IPv6-only while the network is seamlessly supplying IPv4 to those
   that require it.
- **draft-ietf-v6ops-ipv6-only-02** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-Only and IPv6-Mostly Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  The goal is
   that a reference to "IPv6-Only" describes the actual functionality
   being used in a given scope, not the installed protocol support.
- **draft-iplir-protocol-10** (new-draft, score 0, ignored_after_review) [none]: [IPlir network layer security protocol](https://datatracker.ietf.org/doc/draft-iplir-protocol/) — This document specifies the IPlir network layer security protocol.
   It describes how to provide a set of security services for traffic
   over public and corporate networks using the TCP/IP stack.
- **draft-jacobs-web4-assessment-assertions-00** (new-draft, score 0, ignored_after_review) [none]: [Web4 Assessment Assertions](https://datatracker.ietf.org/doc/draft-jacobs-web4-assessment-assertions/) — This document defines an implementation-neutral envelope for
   externally presented assessment results, including subject, issuer,
   policy, result, validity, evidence commitments, proof, and current
   status, while protected methods remain confidential.
- **draft-jacobs-web4-claims-verification-00** (new-draft, score 0, ignored_after_review) [none]: [Web4 Claims and Verification](https://datatracker.ietf.org/doc/draft-jacobs-web4-claims-verification/) — This document distinguishes claims, evidence, assessments,
   assertions, verification events, challenges, supersession,
   suspension, expiration, revocation, and receipts without
   standardizing private scoring internals.
- **draft-jacobs-web4-delegated-authority-00** (new-draft, score 0, ignored_after_review) [none]: [Web4 Delegated Authority](https://datatracker.ietf.org/doc/draft-jacobs-web4-delegated-authority/) — This document defines signed, bounded, time-limited, and revocable
   authority mandates for agents and nodes and links governed actions to
   their authority.
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
- **draft-ma-v6ops-5g-ipv6only-04** (new-draft, score 0, ignored_after_review) [none]: [Considerations of IPv6-only Deployment in 5G Mobile Networks](https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/) — This document describes a practical guide of deploying 464XLAT based
   IPv6-only technology on user plane in 3GPP 5G networks.  It also
   covers key 5G concepts and architectures, configuration methods and
   operational challenges.
- **draft-many-teas-power-steering-02** (new-draft, score 0, ignored_after_review) [teas]: [A Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-many-teas-power-steering/) — This document introduces a Power Conserving Path Placement Strategy
   (PCPPS).  During periods of low demand, PCPPS concentrates traffic
   onto a small set of network resources.  This causes other network
   resources to become idle or nearly idle.  When demand increases,
   PCPPS redistributes traffic as required.
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
- **draft-nir-ipsecme-big-payload-08** (new-draft, score 0, ignored_after_review) [ipsecme]: [A Larger Internet Key Exchange version 2 (IKEv2) Payload](https://datatracker.ietf.org/doc/draft-nir-ipsecme-big-payload/) — The messages of the Internet Key Exchange version 2 (IKEv2) protocol
   are made up of payloads.  The current protocol limits each of these
   payloads to 64KB by having a 2-byte length field.  While this is
   usually enough, several of the payloads may need to be larger.

   This document updates RFC 7296 by defining an extension that allows
   larger payloads.
- **draft-parsons-opsawg-security-operations-02** (new-draft, score 0, ignored_after_review) [none]: [Security Operations Fundamentals and Guidance](https://datatracker.ietf.org/doc/draft-parsons-opsawg-security-operations/) — Security operators are responsible for detecting malicious activity,
   responding to threats and defending their networks and systems from
   cyber attacks.  Security operations are commonly entwined with other
   operational and management priorities to ensure that both security
   and operational priorities are considered holistically.

   With security operators being a crucial part of operation, management
   and security of the network, it is valuable to give consideration to
   them during the design of new protocols.  This document builds upon
   draft-ietf-opsawg-rfc5706bis, describing the fundamentals of security
   operations to provide a foundation for considerations for protocol
   design and guidance.  This document also describes how security
   operations considerations can be most usefully included in other IETF
   documents.
- **draft-pignataro-icmp-enviro-info-03** (new-draft, score 0, ignored_after_review) [none]: [ICMP Extensions for Environmental Information](https://datatracker.ietf.org/doc/draft-pignataro-icmp-enviro-info/) — This document defines a data structure that can be appended to
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
- **draft-prz-lsr-ash-packets-02** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
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
- **draft-sparks-test-async-submission-07** (new-draft, score 0, ignored_after_review) [none]: [Testing async submission](https://datatracker.ietf.org/doc/draft-sparks-test-async-submission/) — This draft is submitted only to test the async api submission
   endpoint
- **draft-templin-6man-aero-omni-amen-15** (new-draft, score 0, ignored_after_review) [none]: [AERO/OMNI Base Specification Amendments (Volume 1)](https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/) — The Automatic Extended Route Optimization (AERO) and Overlay
   Multilink Network (OMNI) Interface functional specifications have
   reached a level of maturity ready for advancement in the RFC
   publication process.  Updates to the base specifications are
   documented in this first amendment and any additional future
   amendments as necessary.
- **draft-traviss-evil-byte-00** (new-draft, score 0, ignored_after_review) [none]: [The Evil Byte: A Security Octet for the IPv4 and IPv6 Headers](https://datatracker.ietf.org/doc/draft-traviss-evil-byte/) — Firewalls, intrusion detection systems, and similar devices continue
   to have difficulty distinguishing packets that have malicious intent
   from those that are merely unusual.  RFC 3514 addressed this problem
   by defining a security flag in the IPv4 header, the "evil bit", to be
   set by the sender of any packet with malicious intent.  Twenty-four
   years of operational experience have shown that senders cannot be
   relied upon to set it, and that a single bit cannot express the range
   of Evil now observed on the Internet.

   This document obsoletes RFC 3514, replacing the evil bit with the
   Evil Byte: an eight-bit Evil Rating carried in every IPv4 and IPv6
   packet, computed and set not by the sender but by a Morality-
   Inspecting Trusted Middleman (MITM) on the path, from a weighted
   product of the sender's Autonomous System, choice of protocols,
   content, name, and the time of day.  Servers reject requests from
   Evil clients; clients discard responses from Evil servers; and the
   Evil of every Autonomous System is continuously re-estimated by an
   Elo rating system operated by a central Evil Rating Authority.  The
   document also specifies the carriage of the octet over avian
   carriers.
- **draft-vicente-acme-pqc-agility-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Cryptographic Agility Profile for ACME](https://datatracker.ietf.org/doc/draft-vicente-acme-pqc-agility-profile/) — This document defines an Automated Certificate Management Environment
   (ACME) [RFC8555] profile extension that enables ACME servers and
   clients to express per-account and per-order post-quantum
   cryptographic (PQC) posture.  The extension introduces a pqcAgility
   metadata object in the ACME directory, an optional pqcAgility member
   in order objects, and a server-side adequacy scoring mechanism that
   determines whether a given order satisfies an account's declared PQC
   readiness threshold.

   The profile is designed for both public and private ACME deployments
   and does not modify the core ACME state machine: it adds discoverable
   capability metadata and per-order policy directives that servers MAY
   enforce.  Multi-tenant ACME servers MUST implement tenant-isolation
   controls that prevent cross-account PQC posture leakage.

   This document is distinguished from draft-giron-acme-pqcnegotiation
   [I-D.giron-acme-pqcnegotiation], which defines algorithm negotiation
   at the ACME protocol level.  This profile operates above the
   negotiation layer: it defines per-account posture scoring, adequacy
   thresholds, hybrid policy bits, rotation epoch anchoring, and tenant-
   isolation requirements that apply regardless of which negotiation
   mechanism is used.
- **draft-vicente-pquip-multitenant-pki-requirements-05** (new-draft, score 0, ignored_after_review) [none]: [PQC Certificate Rotation Requirements for Multi-Tenant PKI Environments](https://datatracker.ietf.org/doc/draft-vicente-pquip-multitenant-pki-requirements/) — This document specifies requirements for post-quantum cryptography
   (PQC) certificate rotation in multi-tenant public key infrastructure
   (PKI) environments.  Multi-tenant PKI deployments — in which a single
   PKI platform issues and manages certificates for multiple distinct
   tenant organizations — face coordination challenges that single-
   tenant PKI deployments do not encounter during PQC migration.
- **draft-vicente-pquip-pqc-readiness-gaps-05** (new-draft, score 0, ignored_after_review) [none]: [PQC Readiness Observability Gaps in Networked Computing Environments](https://datatracker.ietf.org/doc/draft-vicente-pquip-pqc-readiness-gaps/) — This document identifies observability gaps that prevent network
   operators and security teams from determining the post-quantum
   cryptography (PQC) readiness state of networked computing
   environments.  PQC readiness requires knowing which cryptographic
   algorithms are in use across the environment, which are vulnerable to
   quantum attack, and which have been or are being migrated to NIST-
   approved PQC algorithms.  Current network protocols and management
   frameworks do not provide sufficient visibility to answer these
   questions at scale.
- **draft-yan-spring-srv6-int-resource-control-00** (new-draft, score 0, ignored_after_review) [none]: [SRv6-INT: Protocol Extensions to Segment Routing over IPv6 for In-Band Network Telemetry in Support of Closed-Loop Resource Control](https://datatracker.ietf.org/doc/draft-yan-spring-srv6-int-resource-control/) — This document defines SRv6-INT, a protocol extension that integrates
   In-band Network Telemetry (INT) with Segment Routing over IPv6 (SRv6)
   packet processing.  The extension reuses the Segment List entry
   associated with each SRv6-INT endpoint to carry an equal-length
   telemetry record, thereby preventing telemetry collection along the
   path from further increasing the packet header length.  A collector
   obtains the resulting telemetry and provides it to local and global
   controllers for closed-loop resource control.
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
- **draft-zwg-rtgwg-enhanced-bgp-resilience-02** (new-draft, score 0, ignored_after_review) [none]: [Enhanced BGP Resilience](https://datatracker.ietf.org/doc/draft-zwg-rtgwg-enhanced-bgp-resilience/) — According to the base BGP specification, a BGP speaker that receives
   an UPDATE message containing a malformed attribute is required to
   reset the session over which the offending attribute was received.
   RFC7606 revises the error handling procedures for a number of
   existing attributes.  The use of the "treat-as-withdraw" and
   "attribute discard" approaches significantly reduces the likelihood
   of BGP sessions being reset when receiving malformed BGP update
   messages, thereby greatly enhancing network stability.  However, in
   practical applications, there are still numerous instances where BGP
   session oscillations occur due to the receipt of malformed BGP update
   messages, unrecognized attribute fields, or routing rules generated
   by a certain BGP AFI/SAFI that affect the forwarding of BGP messages.

   This document introduces some approaches to enhance the stability of
   BGP sessions.

## Errors / fetch failures

_None._
