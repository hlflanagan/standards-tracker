# IETF Identity + AI Standards Watch

Date: 2026-10-31

## Read now

- **draft-das-agent-tool-integrity-00** (new-draft, score 59, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 7: AI Tool Integrity, Semantic Target Correspondence, and Execution-Time Resource Identity](https://datatracker.ietf.org/doc/draft-das-agent-tool-integrity/) — An AI agent can call the right tool with valid credentials and still
   act on the wrong thing.  When a user tells Apple Siri or Google
   Gemini to "send this to her", asks a coding agent to deploy, or lets
   a browser agent complete a form, the agent must resolve which file,
   contact, account, tenant, or device is meant, and which tool, tool
   version, and model will act.  On iOS, iPadOS, macOS, Android,
   Windows, Linux, enterprise SaaS, cloud platforms, and connected
   hardware, agents can select the wrong user-referenced object, follow
   instructions injected into web pages, repositories, or tool outputs,
   call a tool whose description or capabilities silently changed, run
   on a swapped model or configuration, or send authorized-looking
   requests to redirected hosts, rebound aliases, and substituted
   tenants.  Identity authentication, sandboxing, and transport
   encryption can all succeed while files, credentials, payments,
   developer infrastructure, and physical devices are exposed.

   This document, Part 7 of a twelve-part series, specifies execution-
   time integrity for AI tools.  It describes protected correspondence
   between what the user saw and referred to and the object actually
   acted on; canonical tool-effect contracts with semantic-compatibility
   checks across tool versions; algorithm, model, and configuration
   baseline continuity; instruction provenance with evaluation of lower-
   trust influence on downstream actions; authenticated resolution of
   resource aliases, hosts, and tenants, including redirects and DNS
   rebinding; fencing of tool installation, activation, runtime upgrade,
   and rollback; detection of dynamic service and capability
   substitution; and reconstruction of the actual operation at an
   independent Finality Sink.  Reference algorithms, twelve threat
   models, and thirty reproducible tests, including iOS App Intents and
   Android cooperating-app cases, are included.  Part 1 of the series
   defines the shared terminology and common workflows.

   The document relates these mechanisms to OAuth 2.0 authorization,
   Rich Authorization Requests, Resource Indicators, Token Exchange, and
   Demonstrating Proof of Possession (DPoP); Workload Identity in Multi-
   System Environments (WIMSE); Remote ATtestation procedureS (RATS);
   CBOR Object Signing and Encryption (COSE); Supply Chain Integrity,
   Transparency, and Trust (SCITT); Software Updates for Internet of
   Things (SUIT) manifests; Trusted Execution Environment Provisioning
   (TEEP); Authentication and Authorization for Constrained Environments
   (ACE); and HTTP redirect and conditional-request semantics.  None of
   these alone is treated as conferring final authority for a
   consequential effect, and no working-group adoption or IETF consensus
   is claimed.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri,
   Shortcuts, App Intents, and Keychain; Google Android with Gemini,
   intents, Binder, and Keystore; Samsung Bixby, Microsoft Copilot, and
   Amazon Alexa; Microsoft Windows and Azure; coding and computer-use
   agents from OpenAI, Anthropic, Google, and Meta; Model Context
   Protocol servers, agent-to-agent protocols, and tool and plugin
   registries; browser agents; NVIDIA, Qualcomm, Arm, and Huawei
   hardware; banking, payments, and agentic commerce; email and
   messaging agents; healthcare record agents; document signing; cloud
   infrastructure-as-code; model hosting and model routing; smart homes
   using Matter; automotive assistants and over-the-air updates;
   government digital identity, including the EU Digital Identity
   Wallet; telecommunications; industrial IoT and robotics; and software
   supply chains and CI/CD.  For each, the document states the technical
   effect: the consequential operation reaches the Finality Sink only if
   the actual target, tool contract, model baseline, and instruction
   lineage match what was authorized.  Product names are illustrative
   and imply no endorsement or implementation by any vendor.  For the EU
   Artificial Intelligence Act (Regulation (EU) 2024/1689), execution-
   time integrity of tools, models, and targets can help providers and
   deployers address accuracy, robustness, and cybersecurity, record-
   keeping, and risk-management requirements where those obligations
   apply; this is a technical mapping, not a conformity claim or legal
   advice.
- **draft-das-agent-credential-privacy-00** (new-draft, score 55, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 9: Credential Custody, Operation-Bound Secret Use, and Protected Data Disclosure](https://datatracker.ietf.org/doc/draft-das-agent-credential-privacy/) — Giving an AI agent a credential usually means giving it everything
   that credential can do.  When Apple Siri, Google Gemini, enterprise
   copilots, coding agents, or third-party AI tools act with a user's
   OAuth tokens, API keys, signing keys, or logged-in sessions on iOS,
   iPadOS, macOS, Android, cloud APIs, developer tools, financial
   services, and telecom systems, a prompt-injected or confused agent
   can export data, call APIs, sign transactions, write poisoned entries
   into its own long-term memory, or leak information piece by piece to
   different recipients. iOS Keychain and the Secure Enclave, Android
   Keystore, sandboxing, token authentication, proof of possession, and
   a successful approval each protect something real, but none of them
   establishes authority for the exact outgoing data, recipient, or
   resource effect.

   This document, Part 9 of a twelve-part series, specifies how
   credentials and data are used only for the specific operation that
   was authorized.  It describes protected secret custody in which the
   agent never receives the raw secret; operation-bound credential
   activation; continuity of credential generation and source authority
   across key and token rotation; independent Finality Sink inspection
   of the real outgoing request; recipient-scoped, cumulative,
   correlation-aware disclosure accounting, including derived summaries;
   provenance of source-derived information; retrieval-time provenance
   and write authority for agent memory and retrieval-augmented
   generation stores; and non-replayable consumption of finality.  It
   does not assume that a third-party mobile application can mediate
   other applications without their cooperation.  Reference algorithms,
   fourteen threat models, and thirty-two reproducible tests, including
   current Android and iOS authorized-call cases, are included.  Part 1
   of the series defines the shared terminology and common workflows.

   The document relates these mechanisms to OAuth 2.0 Rich Authorization
   Requests, Resource Indicators, Token Exchange, Demonstrating Proof of
   Possession (DPoP), and mutual-TLS sender constraints; the Workload
   Identity in Multi-System Environments (WIMSE) architecture and the
   WIMSE working group's AI Identity Management System draft on agent
   authentication and authorization; Authentication and Authorization
   for Constrained Environments (ACE); CBOR Object Signing and
   Encryption (COSE); Remote ATtestation procedureS (RATS); Supply Chain
   Integrity, Transparency, and Trust (SCITT); and HTTP semantics.
   These are treated as qualified inputs rather than final authority,
   without claiming working-group adoption or IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri,
   Keychain, Secure Enclave, and App Intents; Google Android with
   Gemini, Keystore, app permissions, and inter-process communication;
   Samsung Bixby, Microsoft Copilot, and Amazon Alexa; Microsoft Windows
   and Azure; Amazon Web Services and other cloud identity platforms;
   cloud key-management and hardware security module signing services;
   agent platforms from OpenAI, Anthropic, Google, and Meta; Model
   Context Protocol connectors and their OAuth-based authorization;
   passkeys and WebAuthn; password managers and autofill; enterprise
   SaaS connectors; open banking and consent-based data sharing,
   including India's Account Aggregator framework; digital wallets and
   payment APIs; healthcare data; human-resources and recruiting agents;
   source-code secrets and CI/CD; personal assistant memory; advertising
   and analytics data sharing; the EU Digital Identity Wallet; NVIDIA,
   Qualcomm, Arm, and Huawei hardware; telecommunications messaging; RAG
   and vector databases; and public-sector systems.  For each, the
   document states the technical effect: a secret is exercised, or data
   is released, only for the specific authorized operation and
   recipient, and only within the remaining disclosure budget.  Product
   names are illustrative and imply no endorsement or implementation by
   any vendor.  For the EU Artificial Intelligence Act (Regulation (EU)
   2024/1689), and alongside data-protection-by-design obligations under
   the General Data Protection Regulation, operation-bound credential
   use and recipient-scoped disclosure records can help providers and
   deployers address cybersecurity, record-keeping, and risk-management
   requirements where those obligations apply; this is a technical
   mapping, not a conformity claim or legal advice.
- **draft-das-distributed-effect-recovery-00** (new-draft, score 55, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 8: Distributed Effect Verification, Protected Recovery, and Multi-Resource Finality](https://datatracker.ietf.org/doc/draft-das-distributed-effect-recovery/) — When an AI agent's request times out, nobody knows whether the money
   moved.  Agents such as Apple Siri acting through App Intents, Google
   Gemini on Android, enterprise copilots, and autonomous workflows on
   iOS, iPadOS, macOS, Android, Windows, Linux, cloud APIs, banking and
   instant-payment systems, robotic controllers, and telecommunications
   networks increasingly act across resources that they do not control.
   An API acknowledgment, a queued request, an expired timeout, an
   apparently failed payment, or a successful local transaction may not
   prove whether the real external effect occurred.  Agents that guess
   then retry into duplicate transfers, compensate for effects that
   never happened, report rollbacks that did not occur, leave multi-
   resource operations half committed, or repeat irreversible actions.

   This document, Part 8 of a twelve-part series, specifies how agents
   establish what actually happened and recover safely.  It describes
   qualified remote-effect evidence; independent witnesses with
   provenance and measurement-competence checks; crash-consistent
   effect-intent journals; containment of indeterminate outcomes so that
   neither successors nor retries run until reconciliation; recovery and
   compensation as separately authorized Candidate Acts that cannot
   inherit or exceed the original authority; resource-specific Finality
   Sinks; dependency-aware multi-resource commit controls that report
   partial commits truthfully; and protected irreversible-effect
   frontiers that require fresh hazard state before an action that
   cannot be undone.  Atomicity across unrelated providers is not
   presumed.  Reference algorithms, twelve threat models, and thirty
   reproducible tests, including an Android and iOS cooperating-client
   case, are included.  Part 1 of the series defines the shared
   terminology and common workflows.

   The document relates these mechanisms to HTTP semantics for
   idempotent methods, retries, and conditional updates; OAuth 2.0
   authorization, Rich Authorization Requests, Resource Indicators,
   Token Exchange, and Demonstrating Proof of Possession (DPoP);
   Workload Identity in Multi-System Environments (WIMSE); Remote
   ATtestation procedureS (RATS) for observers and validators; CBOR
   Object Signing and Encryption (COSE) for signed evidence; Supply
   Chain Integrity, Transparency, and Trust (SCITT) receipts; and
   Authentication and Authorization for Constrained Environments (ACE).
   Their assurances are kept distinct from proof of a specific actual
   consequence, and no working-group adoption or IETF consensus is
   claimed.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri,
   Shortcuts, and App Intents; Google Android with Gemini, intents,
   Binder, and Keystore; Samsung Bixby, Microsoft Copilot, and Amazon
   Alexa; Google Cloud, Microsoft Azure, and Kubernetes; agent platforms
   from OpenAI, Anthropic, and Meta; NVIDIA, Qualcomm, Arm, and Huawei
   hardware; banks, card payments, and merchant APIs; instant payment
   schemes such as UPI, Pix, FedNow, and SEPA Instant; agentic commerce;
   securities trading and settlement; ERP and supply-chain systems;
   multi-leg travel bookings; healthcare prescriptions and records;
   smart homes using Matter; automotive over-the-air updates and remote
   commands; energy dispatch; telecom provisioning, including eSIM
   profiles; government and tax filings; cloud data deletion and
   backups; email and messaging; robotics; and satellites and
   intermittently connected edge systems.  For each, the document states
   the technical effect: an uncertain outcome blocks duplicates and
   successors until a qualified receipt resolves it, and recovery runs
   only under its own fresh authority.  Product names are illustrative
   and imply no endorsement or implementation by any vendor.  For the EU
   Artificial Intelligence Act (Regulation (EU) 2024/1689), truthful
   outcome records and controlled recovery can help providers and
   deployers address robustness, record-keeping, human-oversight, and
   risk-management requirements where those obligations apply; this is a
   technical mapping, not a conformity claim or legal advice.
- **draft-das-autonomous-infrastructure-finality-00** (new-draft, score 54, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 12: Autonomous Cloud, Telecommunications, and Critical-Infrastructure Resource Governance](https://datatracker.ietf.org/doc/draft-das-autonomous-infrastructure-finality/) — An AI agent with valid cloud credentials can spend a month's budget
   in an hour, open the firewall it is supposed to respect, or
   reconfigure a network that other people depend on.  Autonomous agents
   reached through Apple iOS and Google Android enterprise apps and
   assistants such as Apple Siri, Google Gemini, Microsoft Copilot, and
   Amazon Alexa, and agents running on Windows and Linux infrastructure,
   AWS, Azure, and Google Cloud, Kubernetes, telecommunications and
   5G/6G control planes, financial systems, and industrial controllers
   can independently start costly, conflicting, irreversible, or
   security-sensitive resource effects.  Prompt injection, quota
   exhaustion, several agents overspending a shared budget, confused
   asynchronous workflows, agents changing the security policy that
   governs themselves, conflicting rules from different owners, and
   incomplete audit trails can turn a syntactically valid API call into
   an unauthorised consequence.

   This document, Part 12 and the final part of a twelve-part series,
   specifies execution finality for autonomous infrastructure.  It
   describes resource-bounded protected validation that cannot be
   exhausted into a permissive fallback; cumulative consequence budgets
   with delegated sub-budgets that cannot exceed their parent;
   dependency-gated multi-step and asynchronous workflows; non-self-
   authorising security-policy and configuration changes; resolution of
   policy conflicts by competent-authority precedence, including safety
   and tenant boundaries; and end-to-end source-to-effect provenance
   with protected consumption and closure records at independent
   Finality Sinks.  Reference algorithms, twenty threat models, and
   forty reproducible tests, including NETCONF configuration-diff and
   real telecom-controller cases, are included.  Part 1 of the series
   defines the shared terminology and common workflows.

   The document relates these mechanisms to Workload Identity in Multi-
   System Environments (WIMSE); OAuth 2.0 Rich Authorization Requests,
   Token Exchange, and Demonstrating Proof of Possession (DPoP); the
   Network Configuration Protocol (NETCONF), RESTCONF, and YANG data
   modelling; Network Modeling (NETMOD) and Operations and Management
   Area (OPSAWG) work; Remote ATtestation procedureS (RATS);
   Authentication and Authorization for Constrained Environments (ACE);
   CBOR Object Signing and Encryption (COSE); HTTP semantics; Supply
   Chain Integrity, Transparency, and Trust (SCITT); autonomic
   networking (ANIMA); and Trusted Execution Environment Provisioning
   (TEEP) and Software Updates for Internet of Things (SUIT).  These are
   reusable building blocks that do not by themselves supply operation-
   specific finality, and no working-group adoption or IETF consensus is
   claimed.

   Industry alignment covers Apple iOS, iPadOS, and macOS with App
   Intents; Android with Binder, intents, and Keystore; Google Cloud
   with Gemini, Microsoft Azure and Windows, and Amazon Web Services;
   agent platforms from OpenAI, Anthropic, and Meta; NVIDIA, Qualcomm,
   Arm, and Huawei infrastructure; Kubernetes; enterprise identity and
   SaaS; voice and chat assistants issuing infrastructure commands;
   cloud cost management and GPU capacity; autonomous networks and Open
   RAN applications; firewall, secure-access, and zero-trust policy
   automation; identity governance and privileged roles; data-centre
   power and cooling; electricity, water, and other essential services;
   hospital IT; financial market infrastructure; public-sector and
   sovereign cloud; managed service providers; banking and payments;
   telecommunications 5G/6G; and industrial control, robotics, and
   connected vehicles.  For each, the document states the technical
   effect: an autonomous infrastructure change takes effect only within
   its remaining budget, under a policy it did not write for itself,
   according to the competent authority that prevails, and with a
   verifiable closure record.  Product names are illustrative and imply
   no endorsement or implementation by any vendor.  For the EU
   Artificial Intelligence Act (Regulation (EU) 2024/1689), and
   alongside sector cybersecurity frameworks such as the NIS2 Directive
   and the Digital Operational Resilience Act, budgeted, non-self-
   authorising, and fully traceable autonomous changes can help
   providers, deployers, and essential-service operators address risk-
   management, human-oversight, record-keeping, and robustness and
   cybersecurity requirements where those obligations apply; this is a
   technical mapping, not a conformity claim or legal advice.

   Related patent-pending background identified by the author includes
   international application PCT/IB2026/055615 (filed 4 June 2026),
   described as an 8,598-page disclosure with approximately 300
   distinct, non-repetitive technical embodiments.  The author
   additionally reports a broader filing history involving 32
   provisional applications, five other PCT applications, and ten
   further filings; the exact family, priority, and Indian application
   particulars are reserved for separate IETF IPR disclosures.  The
   3,567-page Zenodo specification supporting this series is a separate
   publication.
- **draft-das-causal-effect-receipts-00** (new-draft, score 53, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 6: Verified Actual-Effect Receipts and Protected Causal Continuation](https://datatracker.ietf.org/doc/draft-das-causal-effect-receipts/) — An AI agent that reports "done" has not proven that anything
   happened.  Multi-step tasks run by Apple Siri through App Intents and
   Shortcuts, by Google Gemini across Android apps, by enterprise
   copilots, and by autonomous agents across iOS, iPadOS, macOS,
   Android, Windows, Linux, cloud services, payment systems, connected
   devices, and industrial systems often start the next consequential
   step because a scheduler reported success, an API returned "202
   Accepted", or the agent generated a plausible completion message,
   even though the required earlier real-world effect never occurred or
   cannot be established.  The results include prompt-injection-driven
   phase skipping, false shipment or settlement claims, payment before
   goods are reserved, unsafe device actuation after an unconfirmed
   safety step, replayed acknowledgements, and duplicated or misdirected
   changes after lost replies.

   This document, Part 6 of a twelve-part series, specifies how a later
   step is allowed to proceed only on verified evidence that the earlier
   effect actually took place.  It defines an identity-authenticated
   Interim Effectuation Validator (IEV); qualified actual-effect
   evidence; Protected Effect Receipts (PER); Validator-Accepted Effect
   Receipts (VAER); a single-use Causal Continuation Condition (CCC);
   and receipt-constituted authority for the next phase, checked again
   by an independently enforcing Finality Sink.  It keeps distinct the
   source permission, request dispatch, observation, accepted evidence,
   continuation authority, and actual successor effect, and it treats
   lost or ambiguous outcomes as indeterminate rather than successful.
   Reference algorithms, ten threat models, and twenty-four reproducible
   tests, including an iOS and Android cooperating-gateway case, are
   included.  Part 1 of the series defines the shared terminology and
   common workflows.

   The document relates these mechanisms to OAuth 2.0 authorization,
   Rich Authorization Requests, Resource Indicators, Token Exchange,
   Demonstrating Proof of Possession (DPoP), and token revocation;
   Workload Identity in Multi-System Environments (WIMSE); Remote
   ATtestation procedureS (RATS) for trustworthy validators and
   observers; CBOR Object Signing and Encryption (COSE) for receipt
   objects; Supply Chain Integrity, Transparency, and Trust (SCITT)
   signed statements; Authentication and Authorization for Constrained
   Environments (ACE); and HTTP semantics for asynchronous effects and
   conditional requests.  It identifies discussion points for these
   groups and for Security Area dispatch, without claiming working-group
   adoption or IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri,
   Shortcuts, and App Intents; Google Android with Gemini, intents,
   Binder, and Keystore; Samsung Bixby, Microsoft Copilot, and Amazon
   Alexa; Microsoft Windows and Azure; agent platforms from OpenAI,
   Anthropic, Google Cloud, and Meta; NVIDIA, Qualcomm, Arm, and Huawei
   hardware; banking and payment APIs; agentic commerce and digital
   wallets; e-commerce logistics and returns; healthcare ordering and
   dispensing workflows; insurance claims and lending; travel booking;
   smart homes using Matter; automotive assistants and over-the-air
   updates; energy and utility switching; government digital identity,
   including the EU Digital Identity Wallet; customer-service refunds;
   laboratory and manufacturing execution; software release pipelines;
   robotics; and telecommunications.  For each, the document states the
   technical effect: a successor operation is withheld unless a
   qualified, unreplayed receipt proves the predecessor effect.  Product
   names are illustrative and imply no endorsement or implementation by
   any vendor.  For the EU Artificial Intelligence Act (Regulation (EU)
   2024/1689), receipt-gated continuation and auditable phase records
   can help providers and deployers address record-keeping,
   traceability, human-oversight, and robustness requirements where
   those obligations apply; this is a technical mapping, not a
   conformity claim or legal advice.
- **draft-das-hardware-execution-finality-00** (new-draft, score 52, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 11: Kernel, Sandbox, and Hardware-Enforced Execution Finality](https://datatracker.ietf.org/doc/draft-das-hardware-execution-finality/) — A sandboxed, attested AI agent can still change the real world
   through a door the sandbox left open.  Apple iOS and iPadOS app
   sandboxes, macOS, Google Android, Windows and Linux kernels, AI-agent
   code-execution cells, on-device neural processors running assistants
   such as Apple Siri, Google Gemini, Samsung Galaxy AI, and Microsoft
   Copilot, NVIDIA accelerators and network controllers, Qualcomm and
   Arm processors, confidential-computing virtual machines, and
   embedded, automotive, and telecom controllers isolate workloads while
   still exposing consequential file, credential, network, inter-
   process, deployment, firmware, and hardware-command interfaces.
   Prompt-injected tool execution, privileged connector bypass, syscall
   arguments changed after checking, policy hot swaps, stale
   attestation, GPU and DMA egress, rollback of tools or policies, and
   monitors that only observe rather than block can each let an
   apparently confined agent cause an unauthorized real effect.

   This document, Part 11 of a twelve-part series, specifies execution
   finality at kernel, sandbox, and hardware boundaries.  It describes
   protected discovery of every effect-capable path, with an explicit
   distinction between paths that are blocked and paths that are merely
   observed; controls on transitions from sandbox output to privileged
   real-world effect; non-bypassable credential custody; generation-safe
   installation, upgrade, and rollback of tool runtimes; protected
   mutation of security policy and configuration; hardware attribution
   of device and accelerator commands; independent witness and
   attestation qualification; and Finality Sink reconstruction of the
   actual pending operation with scoped non-bearer authority and fail-
   closed consumption.  Remote attestation is treated as evidence about
   an environment, not authority for a particular effect.  Reference
   algorithms, sixteen threat models, and thirty-six reproducible tests,
   including Apple, Android Binder, and Windows privileged-service
   cases, are included.  Part 1 of the series defines the shared
   terminology and common workflows.

   The document relates these mechanisms to Remote ATtestation
   procedureS (RATS), Trusted Execution Environment Provisioning (TEEP),
   Software Updates for Internet of Things (SUIT), Authentication and
   Authorization for Constrained Environments (ACE), CBOR Object Signing
   and Encryption (COSE), OAuth 2.0 Rich Authorization Requests,
   Demonstrating Proof of Possession (DPoP), and Token Exchange,
   Workload Identity in Multi-System Environments (WIMSE), Supply Chain
   Integrity, Transparency, and Trust (SCITT), HTTP semantics, the
   Network Configuration Protocol (NETCONF), autonomic networking, and
   operational observability work.  The additional question addressed is
   whether a particular real-world effect is authorised and is blocked
   or released at its actual enforcement boundary; no working-group
   adoption or IETF consensus is claimed.

   Industry alignment covers Apple iOS, iPadOS, and macOS sandboxes with
   Siri and App Intents; Google Android with Gemini, Binder, and
   Keystore; Samsung Galaxy AI and Bixby; Microsoft Windows with
   virtualization-based security, Copilot, and AI PCs with neural
   processing units; Linux with seccomp, eBPF, security modules, and
   microVMs; code-execution sandboxes for AI agents; browser sandboxes
   and web agents; agent platforms from OpenAI, Anthropic, Google, and
   Meta; NVIDIA accelerators and data-processing units; Qualcomm, Arm,
   and Huawei processors and trusted execution environments;
   confidential computing and attested private AI clouds; cloud workload
   isolation on AWS, Azure, and Google Cloud; server baseboard
   management controllers; banking, signing, and payment hardware;
   telecommunications network functions and SmartNICs; software-defined
   vehicles; medical devices; industrial control systems; drones and
   robotics; satellite command; and CI/CD and policy automation.  For
   each, the document states the technical effect: a consequential
   effect leaves the sandbox or reaches the hardware only through a gate
   that blocks, rather than merely logs, and that verifies the exact
   operation against current authority.  Product names are illustrative
   and imply no endorsement or implementation by any vendor.  For the EU
   Artificial Intelligence Act (Regulation (EU) 2024/1689), mandatory
   blocking enforcement with honest coverage records can help providers
   and deployers address robustness and cybersecurity, risk-management,
   and record-keeping requirements where those obligations apply; this
   is a technical mapping, not a conformity claim or legal advice.
- **draft-das-multi-agent-authority-control-00** (new-draft, score 52, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 5: Multi-Agent Delegation, Conflict Arbitration, and Quorum Authority](https://datatracker.ietf.org/doc/draft-das-multi-agent-authority-control/) — Each AI agent can hold a valid permission and the group can still do
   something nobody authorized.  When Apple Siri hands a task to an app
   through App Intents, Google Gemini delegates to Android apps and
   cloud agents, or an orchestrator dispatches sub-agents across iOS,
   iPadOS, macOS, Android, Windows, Linux, cloud APIs, and connected
   devices, authority is copied, narrowed, widened, and combined along
   the way.  Prompt-injection-driven delegation, confused-deputy
   escalation, replayed agent approvals, conflicting writes to the same
   resource, duplicated payments, stale reservations, overspent shared
   budgets, colluding or non-independent evaluator quorums, and a final
   tool call detached from its originating authority are typical
   results.

   This document, Part 5 of a twelve-part series, specifies multi-agent
   control for execution finality.  It describes protected arbitration
   of conflicting effects across agents using effect footprints and
   atomic reservations; cryptographic delegation lineage across
   providers with transitive scope attenuation, so that a sub-agent can
   never receive more authority than its parent; version-bound
   concurrency checks; authenticated quorum membership with operation-
   bound approval certificates and separation of duties; budgets
   conserved across branches of a delegation tree; revocation that
   reaches every descendant; and independent Finality Sink verification
   of the actual resource effect.  Reference algorithms, ten threat
   models, and twenty-four reproducible positive and negative tests,
   including an iOS and Android cooperating-receiver case, are included.
   Part 1 of the series defines the shared terminology and common
   workflows.

   The document relates these mechanisms to OAuth 2.0 Rich Authorization
   Requests, Resource Indicators, Token Exchange, Demonstrating Proof of
   Possession (DPoP), and current security best practice; the Grant
   Negotiation and Authorization Protocol (GNAP); Workload Identity in
   Multi-System Environments (WIMSE) and its agent-delegation
   discussions; Remote ATtestation procedureS (RATS); CBOR Object
   Signing and Encryption (COSE); Supply Chain Integrity, Transparency,
   and Trust (SCITT); Authentication and Authorization for Constrained
   Environments (ACE); and HTTP conditional requests.  These are treated
   as qualified inputs rather than final authority, without claiming
   working-group adoption or IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri,
   Shortcuts, and App Intents; Google Android with Gemini, Binder, and
   intents; Samsung Bixby and Microsoft Copilot; Microsoft Windows and
   Azure agent orchestration; agent platforms from OpenAI, Anthropic,
   Google Cloud, and Meta; NVIDIA, Qualcomm, Arm, and Huawei hardware;
   banking and payments; enterprise SaaS, procurement, and inventory;
   robotics; and telecommunications.  Product names are illustrative and
   imply no endorsement or implementation by any vendor.  For the EU
   Artificial Intelligence Act (Regulation (EU) 2024/1689), traceable
   delegation lineage, bounded authority, and quorum-based approval can
   help providers and deployers address human-oversight, record-keeping,
   risk-management, and robustness and cybersecurity requirements where
   those obligations apply; this is a technical mapping, not a
   conformity claim or legal advice.
- **draft-das-interoperable-consequence-authority-01** (new-draft, score 51, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 1: Foundational Consequential Authority and Common Workflows](https://datatracker.ietf.org/doc/draft-das-interoperable-consequence-authority/) — AI assistants and agents, including Apple Siri acting through App
   Intents, Google Gemini on Android, Samsung Bixby, Microsoft Copilot,
   and third-party AI tools, increasingly take real actions on iOS,
   iPadOS, macOS, Android, Windows, Linux, and cloud platforms: they
   send messages, export files, call remote APIs, make payments, and
   operate connected devices.  Such an agent can pass sandboxing,
   authentication, app-permission, and token checks and still cause an
   effect the user never approved, through prompt injection, credential
   misuse, a wrong or redirected target, stale authority, replay, or
   cross-device duplication.

   This document is the foundational part of a twelve-part series.  It
   defines a common architecture in which an AI tool's proposed action
   (a Candidate Act) remains non-effective until protected evidence
   shows that it matches an approved operation, and the component that
   actually executes it (the Finality Sink) independently reconstructs
   the real pending operation and fails closed on any mismatch.  It
   specifies the shared terminology, trust model, and security
   invariants used by Parts 2 through 12, together with three common
   workflows: protected execution of a consequential action;
   continuation of a multi-step task only after a verified receipt for
   the earlier effect; and fresh, bounded re-authorization when an agent
   deviates from its approved scope.  A threat model and a falsifiable
   reference test plan are included.

   The document maps these mechanisms onto existing IETF work as
   reusable building blocks: OAuth 2.0 with Rich Authorization Requests
   and Demonstrating Proof of Possession (DPoP); Workload Identity in
   Multi-System Environments (WIMSE); Remote ATtestation procedureS
   (RATS); CBOR Object Signing and Encryption (COSE); Authentication and
   Authorization for Constrained Environments (ACE); Supply Chain
   Integrity, Transparency, and Trust (SCITT); and HTTP conditional
   requests.  It identifies discussion points for these groups and for
   Security Area dispatch, without claiming working-group adoption or
   IETF consensus.

   Industry alignment covers interoperability between the Apple and
   Google mobile ecosystems, voice and system assistants, enterprise
   agent gateways and copilots, agent tooling from providers such as
   OpenAI, Anthropic, Google, and Meta, hardware-backed enforcement,
   payments, telecommunications, and robotics.  Product names are
   illustrative and imply no endorsement or implementation by any
   vendor.  For the EU Artificial Intelligence Act (Regulation (EU)
   2024/1689), the operation-bound evidence and fail-closed enforcement
   described here can help providers and deployers address risk-
   management, record-keeping, human-oversight, and robustness and
   cybersecurity requirements where those obligations apply; this is a
   technical mapping, not a conformity claim or legal advice.
- **draft-das-cross-platform-ai-interoperability-00** (new-draft, score 48, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 2: Secure iOS and Android AI Tool Interoperability](https://datatracker.ietf.org/doc/draft-das-cross-platform-ai-interoperability/) — AI assistants and third-party AI tools now act across the Apple and
   Google ecosystems.  Apple Siri invokes app actions through App
   Intents and Shortcuts, Google Gemini acts through Android intents and
   app integrations, and agents from many vendors reach the same
   accounts from iOS, iPadOS, macOS, Android, Windows, Linux, cloud
   APIs, and connected devices.  Each hop crosses a different
   permission, sandbox, credential, identity, and hardware trust model.
   A prompt-injected, replayed, or redirected tool call can then export
   a file, send a payment, change data, or operate a device in a way
   that differs from what the user approved, and app permissions,
   Keychain or Android Keystore credentials, and OAuth tokens do not by
   themselves prove that the executed operation matches the approved
   one.

   This document, Part 2 of a twelve-part series, specifies how to carry
   authority across platforms without letting a platform permission
   become final authority.  Platform-specific adapters for iOS and
   Android translate qualified app, user, device, and key evidence into
   a protected canonical effect descriptor; the AI tool's proposed
   action remains non-effective; operation-scoped, non-bearer
   authorization resists replay and redirection; and the receiving
   Finality Sink independently reconstructs the actual pending
   operation, checks resource identity, aliases, and redirects, fences
   stale devices after cross-device handoff, and fails closed on any
   mismatch.  Reference data models, pseudocode, a state machine, six
   threat models, and twenty reproducible validation tests are included.
   Part 1 of the series defines the shared terminology and common
   workflows.

   The document relates these mechanisms to OAuth 2.0 Rich Authorization
   Requests and Demonstrating Proof of Possession (DPoP); Workload
   Identity in Multi-System Environments (WIMSE); Remote ATtestation
   procedureS (RATS); CBOR Object Signing and Encryption (COSE);
   Authentication and Authorization for Constrained Environments (ACE);
   Supply Chain Integrity, Transparency, and Trust (SCITT); and HTTP
   redirection and conditional requests.  It identifies discussion
   points for these groups and for Security Area dispatch, without
   claiming working-group adoption or IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri, App
   Intents, and Shortcuts; Google Android with Intents, Binder, and
   Android Keystore; Google Gemini; Samsung Bixby; Microsoft Windows and
   Azure agent governance; agent platforms from OpenAI, Anthropic, and
   Meta; NVIDIA, Qualcomm, Arm, and Huawei hardware; and payments,
   telecommunications, and robotics.  Product names are illustrative and
   imply no endorsement or implementation by any vendor.  For the EU
   Artificial Intelligence Act (Regulation (EU) 2024/1689), operation-
   level evidence and fail-closed cross-platform enforcement can help
   providers and deployers address risk-management, record-keeping,
   human-oversight, and robustness and cybersecurity requirements where
   those obligations apply; this is a technical mapping, not a
   conformity claim or legal advice.
- **draft-das-finality-sink-enforcement-00** (new-draft, score 48, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 4: Finality Sink Enforcement, Actual-Operation Reconstruction, and Anti-Bypass Security](https://datatracker.ietf.org/doc/draft-das-finality-sink-enforcement/) — An AI action can be approved correctly and still go somewhere else.
   Assistants such as Apple Siri acting through App Intents and Google
   Gemini on Android, AI coding agents, browser and computer-use agents,
   enterprise copilots, and third-party automation on iOS, iPadOS,
   macOS, Android, Windows, Linux, and cloud platforms can reach the
   same effect through another network route, file interface, privileged
   inter-process service, direct API credential, hardware command queue,
   or sandbox exit.  Prompt injection, stale human approvals, a swapped
   window or user-interface target, and forged observations can also
   make the approved tool action differ from the payment, export,
   publication, resource change, or device command that actually
   happens.

   This document, Part 4 of a twelve-part series, specifies the
   enforcement point of execution finality: the Finality Sink.  The sink
   independently reconstructs the actual pending operation where the
   effect occurs, rather than trusting the agent's description, and
   either consumes operation-scoped authority once under protected state
   or refuses.  The document covers discovery of every effect-capable
   path, the difference between observing an effect and blocking it,
   runtime enforcement-coverage epochs, privilege transitions from
   sandbox to real resource, authenticated computer-use and human-
   approval state, and replay and snapshot-rollback resistance.
   Reference algorithms, six threat models, and twenty reproducible
   positive and negative tests, including an Android-to-iOS case, are
   included.  Part 1 of the series defines the shared terminology and
   common workflows.

   The document treats existing IETF mechanisms as qualified inputs to
   sink-local decisions rather than final authority: OAuth 2.0 Rich
   Authorization Requests and Demonstrating Proof of Possession (DPoP);
   Workload Identity in Multi-System Environments (WIMSE); Remote
   ATtestation procedureS (RATS); CBOR Object Signing and Encryption
   (COSE); Authentication and Authorization for Constrained Environments
   (ACE); Supply Chain Integrity, Transparency, and Trust (SCITT); and
   HTTP preconditions and redirect semantics.  It identifies discussion
   points for these groups and for Security Area dispatch, without
   claiming working-group adoption or IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Siri, App
   Intents, and desktop sandboxing; Google Android with Binder and
   intents; Google Gemini and agent gateways; Samsung Bixby and
   Microsoft Copilot; Microsoft Windows and Azure agent containers;
   computer-use and coding agents from OpenAI, Anthropic, and Meta;
   NVIDIA, Qualcomm, Arm, and Huawei hardware; banking and payments;
   cloud API gateways and SaaS; and telecommunications, IoT, and
   robotics.  Product names are illustrative and imply no endorsement or
   implementation by any vendor.  For the EU Artificial Intelligence Act
   (Regulation (EU) 2024/1689), sink-side enforcement that cannot be
   bypassed through alternate paths can help providers and deployers
   address robustness and cybersecurity, human-oversight, risk-
   management, and record-keeping requirements where those obligations
   apply; this is a technical mapping, not a conformity claim or legal
   advice.
- **draft-das-social-media-algorithmic-accountability-00** (new-draft, score 48, trust_infrastructure) [none]: [Social Media Algorithmic Virality and Accountability During Internal and International Crises: Protected Algorithmic Logic Fingerprint Verification and Output Finality for Electoral and Civic Information Systems](https://datatracker.ietf.org/doc/draft-das-social-media-algorithmic-accountability/) — Social media platforms, search engines, digital advertising systems,
   and other information-distribution services use artificial
   intelligence, recommendation engines, ranking algorithms, and
   automated amplification mechanisms to determine what information
   becomes visible, how frequently it is presented, and how widely it
   may spread.  During elections, referendums, domestic emergencies,
   international crises, and other periods of heightened public
   importance, changes in algorithmic configurations may affect the
   visibility, ordering, repetition, and distribution of civic
   information.  Conventional deployment approvals, software signatures,
   configuration records, and retrospective audits do not necessarily
   establish which algorithmic logic actually executed or whether a
   particular output was authorized before becoming effective.

   This document provides a comprehensive, implementation-neutral
   technical disclosure of an Algorithmic Accountability and Protected
   Output-Finality Architecture based on the Algorithmic Logic
   Fingerprint (ALF).  The architecture identifies actual algorithmic
   execution instances, obtains protected measurements of activated
   computational components and configurations, constructs verifiable
   ALF representations, and evaluates them against applicable authorized
   references.  It distinguishes algorithmic identity (ALF-I), actual
   execution evidence (ALF-E), and output-binding commitments (ALF-O).
   Protected validation associates the measured execution state with an
   identified pending output and may generate a cryptographically
   authenticated validation receipt.  Separately scoped, non-bearer
   finality enablement may establish operation-specific authority.  An
   independent Finality Sink obtains or reconstructs the actual pending
   operation and verifies the receipt, applicable authority, output
   correspondence, current policy state, and protected sink-local
   conditions before permitting the covered effect to occur.

   The architecture addresses algorithmic virality as a sequence of
   computationally mediated amplification and delivery operations rather
   than assuming that every viral outcome is improper.  It provides
   technical mechanisms for verifying the authorized execution
   configurations associated with covered recommendation, ranking,
   notification, filtering, and presentation operations.  Verification
   of individual amplification operations does not, by itself, measure
   aggregate audience reach, determine the appropriateness of viral
   distribution, or establish the social consequences of particular
   information.

   Non-limiting enforcement points include model activation, inference
   execution, feature processing, candidate generation, recommendation
   and ranking, experiment routing, application gateways, content-
   delivery networks, edge infrastructure, network egress, mobile and
   desktop runtimes, protected compositors, and display-finality
   boundaries.  Cryptographic, protected non-cryptographic, and hybrid
   measurement mechanisms may be employed under defined trust and
   assurance requirements.  The architecture supports heterogeneous
   proprietary algorithms without requiring a common recommendation
   model or unrestricted disclosure of confidential source code, trained
   model weights, or ranking parameters.

   The disclosed mechanisms may support selected technical
   accountability objectives relevant to the European Union Digital
   Services Act, Articles 34, 35, 37, and 40 (systemic-risk assessment,
   mitigation, independent auditing, and regulatory or research data
   access); the European Union Artificial Intelligence Act, Articles 9,
   12, 13, 14, and 15, where applicable (risk management, record-
   keeping, transparency, human oversight, accuracy, robustness, and
   cybersecurity); India's Information Technology Act, 2000, and
   Information Technology (Intermediary Guidelines and Digital Media
   Ethics Code) Rules, 2021, as amended (applicable intermediary due
   diligence and information-related responsibilities); and the World
   Trade Organization Agreement on Technical Barriers to Trade,
   particularly Articles 2.1, 2.2, and 2.4, concerning non-
   discrimination, avoidance of unnecessary trade barriers, and relevant
   international-standard considerations within that Agreement's scope.
   These relationships identify potential technical support and
   interoperability objectives, not automatic legal compliance, WTO
   conformity, or regulatory certification.

   The architecture expressly distinguishes organic human expression and
   legitimate editorial activity from algorithmic selection, ranking,
   recommendation, and amplification.  It does not require political-
   truth classification, ideological approval, suppression of lawful
   viewpoints, or prohibition of legitimate algorithmic configuration
   changes.  Its objective is to verify whether defined computational
   processes and covered output operations satisfy their applicable
   technical authorization conditions, independently of the political
   viewpoint expressed in the underlying communication.

   This document makes no allegation that any social media platform,
   search engine, technology company, advertising provider, government
   institution, political organization, or individual has engaged in
   electoral manipulation, unlawful algorithmic interference, improper
   information distribution, or regulatory violations.

   Relevance to IETF Working Groups: This disclosure identifies
   technical intersections with ongoing IETF work, including RATS
   (execution attestation), SCITT (authenticated evidence and
   transparency), COSE (cryptographic protection), OAuth (scoped
   authorization), WIMSE (workload identity), HTTPBIS (information
   delivery), MoQ (media distribution), and agentproto (AI-agent
   communication).  It extends the technical discussion toward actual
   algorithmic execution verification, output-specific evidence binding,
   and independent Finality Sink enforcement across distributed systems.
   The document is offered for public technical disclosure, independent
   examination, and cross-working-group discussion, without implying
   IETF endorsement or working-group adoption.

   The full technical disclosure includes detailed definitions, non-
   limiting enforcement points, protected execution procedures,
   alternative implementations, freedom-of-expression safeguards, and
   architectural diagrams illustrating ALF extraction, protected
   validation, authenticated evidence, and Finality Sink enforcement.
   The document is presented principally for public technical
   disclosure, independent examination, security research, and
   interoperability analysis, rather than as an assertion of an adopted
   or approved IETF standard.
- **draft-das-protected-authority-evidence-00** (new-draft, score 47, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 3: Protected Source Authority, Cross-Committed Evidence, and Scoped Non-Bearer Finality](https://datatracker.ietf.org/doc/draft-das-protected-authority-evidence/) — When Apple Siri runs an App Intent, Google Gemini triggers an Android
   action, or a third-party AI agent calls a cloud API on a user's
   behalf, the request usually carries valid credentials: an OAuth
   token, an iOS Keychain or Android Keystore key, or a signed approval.
   Valid credentials are not the same as authority for the exact
   operation.  Prompt injection, stolen or reused tokens, forged or
   substituted approvals, stale delegated authority, replayed
   authorizations, and crashes between the authorization decision and
   the effect can each disconnect an apparent permission from the file
   export, payment, secret use, cloud change, or device command that is
   actually executed.

   This document, Part 3 of a twelve-part series, specifies the
   authority and evidence layer of execution finality.  It describes how
   to capture protected source authority from the originating principal;
   collect protected evidence when a request is formed; validate it
   again, independently, at execution time; cross-commit the two so that
   neither can be substituted; issue operation-scoped, non-bearer
   finality enablement that is useless if copied; and consume it once,
   under protected state, at an independently verifying Finality Sink.
   It also specifies crash-consistent journaling and reconciliation of
   indeterminate remote outcomes, keeping local consumption of authority
   distinct from completion of the external effect.  Reference
   algorithms, six threat models, and twenty reproducible positive and
   negative tests are included.  Part 1 of the series defines the shared
   terminology and common workflows.

   The document treats existing IETF mechanisms as qualified inputs
   rather than final authority: OAuth 2.0 Rich Authorization Requests
   and Demonstrating Proof of Possession (DPoP); Workload Identity in
   Multi-System Environments (WIMSE); Remote ATtestation procedureS
   (RATS); CBOR Object Signing and Encryption (COSE) for evidence
   encoding; Authentication and Authorization for Constrained
   Environments (ACE); Supply Chain Integrity, Transparency, and Trust
   (SCITT) signed statements; and HTTP conditional requests and
   redirects.  It identifies discussion points for these groups and for
   Security Area dispatch, without claiming working-group adoption or
   IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Apple
   Intelligence, Siri, and App Intents; Google Android with Gemini,
   Intents, Binder, and Android Keystore; Samsung Bixby and Microsoft
   Copilot; Microsoft Windows and Azure; agent platforms from OpenAI,
   Anthropic, Google Cloud, and Meta; NVIDIA, Qualcomm, Arm, and Huawei
   hardware; API banking and digital signatures; Kubernetes and service
   meshes; telecommunications; and robotics.  Product names are
   illustrative and imply no endorsement or implementation by any
   vendor.  For the EU Artificial Intelligence Act (Regulation (EU)
   2024/1689), cross-committed, operation-level evidence and single-use
   consumption records can help providers and deployers address record-
   keeping, traceability, human-oversight, and robustness and
   cybersecurity requirements where those obligations apply; this is a
   technical mapping, not a conformity claim or legal advice.
- **draft-das-cross-device-authority-revocation-00** (new-draft, score 46, trust_infrastructure) [none]: [Secure AI Execution-Finality for iOS, Android, and Cross-Platform AI Agents, Part 10: Cross-Device Authority Continuity, Revocation Fencing, and Offline Execution](https://datatracker.ietf.org/doc/draft-das-cross-device-authority-revocation/) — Revoking an AI agent's access does not stop the copy of it that is
   still running somewhere else.  Tasks now move between an iPhone, an
   iPad, a Mac, an Android phone, a Windows or Linux workstation, a
   cloud agent, a car, and an edge controller; Apple Siri and Google
   Gemini follow the user across phones, watches, speakers, and
   vehicles.  After a handoff, a synchronised login, a delegated
   session, a cached OAuth token, or a cloned virtual machine, the old
   device or a disconnected resource can still cause a duplicate or
   stale real-world effect.  Revoked-but-cached permissions, untrusted
   clock rollback, expired offline leases, delayed command queues, races
   over who owns a task, lost or stolen devices, and uncertain outcomes
   after a network partition all make "access revoked" different from
   "effects stopped".

   This document, Part 10 of a twelve-part series, specifies how
   authority moves between devices and stops when it should.  It
   describes protected ownership generations with source fencing, so
   that exactly one device or agent instance can act for a task;
   authenticated delegation and revocation transitions with dependency
   graphs and source-authority generations; protected time and lease
   expiry that resist clock rollback; per-device, non-bearer finality;
   preallocated offline authority with protected partition budgets that
   cannot be cloned or double-spent; partition-aware reconciliation;
   transfer of administrative and resource ownership across domains; and
   independent verification of the actual pending operation at the
   responsible Finality Sink.  Reference algorithms, fourteen threat
   models, and thirty-six reproducible tests are included.  Part 1 of
   the series defines the shared terminology and common workflows.

   The document relates these mechanisms to OAuth 2.0 Token Revocation,
   Token Introspection, Token Exchange, Rich Authorization Requests, and
   Demonstrating Proof of Possession (DPoP); Workload Identity in Multi-
   System Environments (WIMSE); Authentication and Authorization for
   Constrained Environments (ACE); Remote ATtestation procedureS (RATS);
   CBOR Object Signing and Encryption (COSE); Supply Chain Integrity,
   Transparency, and Trust (SCITT); HTTP conditional requests and
   caching; Software Updates for Internet of Things (SUIT) and Trusted
   Execution Environment Provisioning (TEEP); and the Network
   Configuration Protocol (NETCONF).  It identifies discussion points
   for these groups and for Security Area dispatch, without claiming
   working-group adoption or IETF consensus.

   Industry alignment covers Apple iOS, iPadOS, and macOS with Handoff,
   Siri, and App Intents; Google Android with Gemini and Android
   Keystore; Samsung Bixby, Microsoft Copilot, and Amazon Alexa across
   phones, watches, speakers, and cars; Microsoft Windows and Azure;
   agent platforms from OpenAI, Anthropic, and Meta; NVIDIA, Qualcomm,
   Arm, and Huawei hardware; multi-cloud failover; lost and stolen
   device protection and remote wipe; phone replacement and device
   transfer; employee offboarding and bring-your-own-device programmes;
   offline and small-value payments, including UPI Lite and proposed
   offline modes for central-bank digital currencies; transit and access
   credentials in mobile wallets; vehicle digital keys; smart locks and
   shared guest access; family accounts and parental controls;
   telecommunications roaming and edge; IoT and intermittently connected
   sites, including aviation, maritime, and satellite-connected devices;
   robotics and vehicles; and industrial and energy systems.  For each,
   the document states the technical effect: after handoff or
   revocation, only the current owner can cause an effect, and offline
   devices can act only within a protected, non-clonable budget that
   expires on trusted time.  Product names are illustrative and imply no
   endorsement or implementation by any vendor.  For the EU Artificial
   Intelligence Act (Regulation (EU) 2024/1689), enforceable revocation
   and bounded offline authority can help providers and deployers
   address human-oversight, robustness and cybersecurity, and record-
   keeping requirements where those obligations apply; this is a
   technical mapping, not a conformity claim or legal advice.
- **draft-durga-wimse-ctx-isolation-00** (new-draft, score 36, authorization) [none]: [Cryptographic Separation of Untrusted Data-Plane Context from Control-Plane Tool Invocations in Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-wimse-ctx-isolation/) — Autonomous AI agents operating over Model Context Protocol (MCP) and
   Agent-to-Agent (A2A) transports routinely ingest untrusted external
   data (emails, web documents, retrieved RAG chunks) into the same
   inference context that authorizes privileged control-plane tool
   calls.  Existing workload identity and token standards (OAuth 2.1,
   GNAP, WIMSE Wit/Wpt tokens) bind client identity and authorization
   scope, but fail to cryptographically bind the provenance taint of the
   data-plane context that induced the tool invocation, leaving systems
   vulnerable to indirect prompt-injection confused-deputy attacks.
   This document specifies a deterministic COSE_Sign1 and JSON
   Canonicalization Scheme (JCS, RFC 8785) wire profile that attaches a
   cryptographic Context Taint Attestation (CTA) header to every
   control-plane tool invocation, forcing relying parties to fail closed
   when an untrusted or mixed data-plane context attempts to trigger a
   state-mutating action without an independent out-of-band human or
   policy approval receipt.
- **draft-sharif-agent-audit-trail-09** (new-draft, score 31, trust_infrastructure) [none]: [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/) — This document specifies a standard logging format for autonomous
   AI agent systems.  The Agent Audit Trail (AAT) defines a
   JSON-based record structure with mandatory fields for agent
   identity, the authorizing principal, action classification,
   outcome tracking, and trust level reporting.  Records are
   linked via tamper-evident hash chaining using SHA-256 per
   RFC 8785, with optional ECDSA signatures for non-repudiation.

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

   The -04 revision added algorithm agility for post-quantum
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

   This revision (-07) adds a mandatory "principal" field
   (Section 3.1) that binds each record to the party on whose
   authority the agent acted; a Relationship to Other Work
   section (Section 1.3) relating AAT to the WIMSE agent audit
   record and authorization-evidence drafts and to SCITT
   (RFC 9943); and corrections to the EU AI Act Article 12 and
   Article 19 citations in the regulatory mapping (Section 11.1
   and Appendix B).  Records produced under -06 and earlier
   predate the "principal" field; verifiers processing
   mixed-revision archives SHOULD treat its absence as "principal
   not recorded" rather than a validation failure.
- **draft-drake-email-hardware-attestation-03** (new-draft, score 29, core_identity) [none]: [Hardware Attestation for Email Sender Verification](https://datatracker.ietf.org/doc/draft-drake-email-hardware-attestation/) — This document defines two email bindings for proving properties of an
   automated sender using the durable identity and anchor architecture
   of the Agent Identity Registry System (AIRS).  Mode 1 carries a
   detached CMS signature made by a message-signing proof key.  It can
   provide manufacturer-rooted hardware provenance, Registrar-backed
   AIRS identity binding, or both.  Mode 2 carries a per-message SD-JWT
   that allows a Registrar to assert selected properties without
   requiring disclosure of the sender's canonical AIRS identifier.

   The AIRS identity0 model, canonical aid identifier, trust tiers,
   anchor semantics, enrollment rules, and Registrar trust boundary are
   defined by [I-D.drake-agent-identity-problem-statement] and
   [I-D.drake-agent-identity-registry].  Authoritative resolution of the
   current Registrar/OAuth issuer is defined by
   [I-D.drake-agent-identity-resolution].  This document does not
   redefine those concepts; it defines how email messages bind to and
   verify them.
- **draft-watts-agent-authority-transition-receipts-01** (new-draft, score 28, authorization) [none]: [Agent Authority Transition Receipts for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-authority-transition-receipts/) — Autonomous agents increasingly act across administrative and security
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
- **draft-durga-pquip-pqc-agentic-delegation-00** (new-draft, score 26, agent_identity) [none]: [Post-Quantum Hybrid Cryptographic Delegation Chains and Merkle-Aggregated Execution Receipts for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-pquip-pqc-agentic-delegation/) — Autonomous AI agent ecosystems rely on multi-hop cryptographic
   delegation chains and signed execution traces (currently built on
   Ed25519, ECDSA P-256, and RSA-PSS) to enforce least-privilege tool
   invocations across Model Context Protocol (MCP) and Agent-to-Agent
   (A2A) boundaries, and to preserve long-term non-repudiation for
   regulatory audit logs.  This architecture faces two existential
   vulnerabilities in the Post-Quantum era: (1) "Harvest-Now, Forge-and-
   Repudiate-Later" (HNFRL) attacks, wherein Cryptographically Relevant
   Quantum Computers (CRQCs) running Shor's algorithm retroactively
   forge or repudiate multi-year compliance traces (e.g., 7-to-10-year
   HIPAA, SOX, FDA 21 CFR Part 11, and defense operational logs) and
   synthesize retroactive human-in-the-loop approvals; and (2) "Lattice
   Signature-Bloat Amplification," wherein naively substituting 64-byte
   Ed25519 signatures with 3,309-byte ML-DSA-65 (FIPS 204) signatures
   across a 10-hop sub-agent chain inflates per-call authorization
   headers from 640 bytes to over 46 KB (including public keys),
   exceeding HTTP/2 header limits and degrading sub-10ms real-time tool
   routing.

   This document specifies a wire-compatible Post-Quantum Agentic
   Delegation and Trace Receipt profile ("PQ-Agentic").  It introduces a
   two-tier cryptographic architecture: (a) a Hot-Path Hybrid Delegation
   Envelope combining classical Ed25519 with ML-DSA-65 (FIPS 204) via
   Pre-Verified Session-Grant Digest Chaining (PVSGDC), replacing
   redundant per-call inline re-transmission of O(N) prior delegators'
   5,261-byte ML-DSA-65 public keys and signatures with 32-byte SHAKE256
   digests of out-of-band PEP-verified delegation grants; and (b) a
   Cold-Path Long-Horizon Archival Receipt anchored with stateless hash-
   based SLH-DSA-SHAKE-128f (FIPS 205) over RFC 9943 SCITT transparency
   Merkle roots, guaranteeing 30-year quantum-resistant non-repudiation
   even under catastrophic lattice cryptanalysis.
- **draft-elekula-seat-attested-tls-testing-00** (new-draft, score 26, core_identity) [none]: [Interoperability, Security Evaluation, and Negative Testing for Attested TLS 1.3 and DTLS 1.3](https://datatracker.ietf.org/doc/draft-elekula-seat-attested-tls-testing/) — This document defines a framework for reproducible interoperability
   and security evaluation of implementations that integrate remote
   attestation with TLS 1.3 and DTLS 1.3. It complements protocol and
   architecture specifications by defining test profiles, a common
   result model, cross-implementation procedures, negative tests, and
   measurements at the boundary between transport authentication,
   attestation appraisal, authorization, and application-data release.

   In addition to per-connection attestation, the framework evaluates
   reusable Attestation Results and cross-connection trust-continuity
   mechanisms, including deployments in which an attestation endpoint
   and application-serving endpoint are distinct. It addresses key
   custody and derivation, target and workload identity, state drift,
   credential lifecycle, multi-relying-party isolation, proxy topology,
   session resumption, early data, privacy, and failure containment.

   This document does not define a new attestation architecture,
   Evidence format, TLS or DTLS extension, cryptographic key schedule,
   or remote-attestation protocol. It specifies an evaluation framework
   for comparing implementations and identifying interoperability and
   security gaps in declared profiles.
- **draft-fletcher-oauth-txn-token-chaining-profile-01** (new-draft, score 25, authorization) [none]: [Transaction Token JWT Authorization Grant Profile for OAuth Identity and Authorization Chaining](https://datatracker.ietf.org/doc/draft-fletcher-oauth-txn-token-chaining-profile/) — This specification defines a profile of the OAuth Identity and
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

   Agentic systems are one class of deployment that depends on this
   capability.  The AI Identity Management System [I-D.ietf-wimse-aims]
   describes AI agents as workloads that use Transaction Tokens to carry
   authorization context between the services implementing a task, and
   that frequently need to reach resources protected by an authorization
   server in another trust domain.  Its treatment of cross-domain access
   directs such an agent to use [I-D.ietf-oauth-identity-chaining] or a
   profile of it as defined in this document.
- **draft-hood-agtp-log-03** (new-draft, score 24, adjacent_watchlist) [none]: [AGTP Transparency Log Protocol](https://datatracker.ietf.org/doc/draft-hood-agtp-log/) — This document specifies the AGTP Transparency Log (AGTP-LOG): the
   append-only audit log protocol that underpins the log-anchored Trust
   Tier 1 verification path defined in [AGTP] and provides the post-hoc
   audit infrastructure for AGTP-based agent operations.  AGTP-LOG
   aligns with [RFC9162] (Certificate Transparency 2.0) as the
   verifiable data structure and issues COSE_Sign1 receipts per
   [RFC9943] (SCITT) for cross-ecosystem interoperability.  This
   document restates the AGTP Agent Identity Taxonomy (Agent Genesis,
   Canonical Agent-ID, Agent Certificate) as [AGTP] adopts it.  The log
   protocol defined here covers entry submission, receipt retrieval,
   inclusion-proof retrieval, consistency-proof retrieval, and discovery
   via the log_uri field of the Agent Genesis.  This revision adds the
   statement types by which Attribution-Record Audit-IDs and per-agent
   chain heads are committed to the log, which is the mechanism
   [AGTP-IDENTIFIERS] names for making a self-held attribution chain
   tamper-evident to a verifier that distrusts the holder.  Per-platform
   logs are the default; the federation model follows the SCITT cross-
   witnessing pattern.  Witness and monitor role definitions, full
   federation procedures, and the formal entry-acceptance threat model
   are deferred to a future revision.

   The audit properties AGTP-LOG provides are structural.  Statements
   are signed by the governance platform that operates the log, never by
   the agent the statements concern; an agent cannot forge its own audit
   trail because the log operator's signing key is outside its control.
   This architectural separation distinguishes AGTP-LOG audit
   infrastructure from approaches that layer audit data models onto
   general-purpose substrates where the audited party participates in
   writing the audit trail.
- **draft-thaha-scitt-agent-execution-evidence-01** (new-draft, score 24, core_identity) [none]: [Agent Execution Evidence: A SCITT Profile for Verifiable Records of AI Agent Runs](https://datatracker.ietf.org/doc/draft-thaha-scitt-agent-execution-evidence/) — AI agents act through calls to models, tools and other agents.
   Identity work establishes who an agent is and what it may do, but
   leaves execution-evidence formats and assurance criteria out of
   scope.  This document profiles the Supply Chain Integrity,
   Transparency, and Trust (SCITT) architecture for Signed Statements
   that bind an agent's registered identity, declared capabilities,
   risk-based assessment and supervised operational status to a hash-
   chained record of every call the agent makes.  It also defines
   admission records produced where a call is received, and the linking
   of records for requests that pass between agents of different
   operators.  It specifies Registration Policy, offline verification
   and Bundle requirements.  It does not define an accreditation scheme,
   a universal risk classification, an identifier scheme or a policy
   language.
- **draft-watts-high-assurance-agent-control-envelope-01** (new-draft, score 24, authorization) [none]: [High-Assurance Agent Control Envelope](https://datatracker.ietf.org/doc/draft-watts-high-assurance-agent-control-envelope/) — Agentic systems can authenticate successfully, hold a valid
   authorization object, and still be unsafe to execute because required
   evidence is missing, the software has not reached a required
   assurance stage, the authority epoch is stale, a prior revocation is
   unresolved, or a human-approval requirement is unsatisfied.  This
   document defines the High-Assurance Agent Control Envelope (HAACE), a
   protocol-neutral profile that binds an exact agent action to identity
   status, authorization state, policy, assurance stage, evidence state,
   authority epoch, revocation state, oversight requirements, and an
   action-time decision.  HAACE requires fail-closed treatment of
   missing or indeterminate prerequisites, separates authorization from
   execution, and produces non-bearer decision and execution receipts.
   The profile composes with OAuth, workload identity, attestation,
   transparency, and agent-authorization mechanisms rather than
   replacing them.
- **draft-niyikiza-oauth-attenuating-agent-tokens-02** (new-draft, score 23, authorization) [none]: [Attenuating Authorization Tokens for Agentic Delegation Chains](https://datatracker.ietf.org/doc/draft-niyikiza-oauth-attenuating-agent-tokens/) — This document defines Attenuating Authorization Tokens (AATs), a
   signed credential format for task-scoped delegation in AI agent
   systems.  An AAT encodes the tools an agent may invoke and the
   argument constraints that apply to those invocations.  A token holder
   authorized to delegate can derive a token offline with equal or
   narrower authority, subject to the parent token's depth and lifetime
   limits.  The resulting delegation chain is verifiable offline by any
   enforcement point that has the root issuer's trust anchor key.

   This specification profiles the OAuth Rich Authorization Requests
   format (RFC 9396) for tool-level capability claims, adds delegation-
   chain claims, and defines a core constraint vocabulary for argument
   restrictions.  The chain verification algorithm authenticates each
   delegation step and enforces monotonic attenuation without network
   contact with the root issuer.
- **draft-sweeney-wimse-credential-delegation-02** (new-draft, score 23, core_identity) [none]: [Credential Delegation Protocol for AI Agents in Multi-System Environments](https://datatracker.ietf.org/doc/draft-sweeney-wimse-credential-delegation/) — Autonomous AI agents increasingly require access to protected
   resources across multiple service providers on behalf of human users.
   Existing OAuth 2.0 extensions address individual aspects of this
   problem (token exchange, proof-of-possession, and structured
   authorization) but no current specification defines how these
   mechanisms compose into a coherent credential delegation framework
   for AI agents.

   This document specifies the Credential Delegation Protocol: a profile
   of OAuth 2.0 Token Exchange (RFC 8693), Demonstrating Proof-of-
   Possession (RFC 9449), Rich Authorization Requests (RFC 9396), and
   Client-Initiated Backchannel Authentication (OpenID Connect CIBA)
   that enables human users to delegate scoped, attenuated credentials
   to AI agents operating across heterogeneous service providers.

   The protocol defines: agent identity lifecycle management using
   ephemeral key pairs; capability-shaped delegation tokens bound to
   specific operations and resources; credential wrapping semantics that
   prevent exposure of underlying OAuth tokens to agents; consent-gated
   delegation flows for asynchronous agents; real-time cascading
   revocation; and tamper-evident audit chains.

   This document does not define new token formats, new OAuth grant
   types, or modifications to existing authorization server behavior.
   It specifies how existing mechanisms are combined to achieve secure,
   auditable credential delegation for AI agents.
- **draft-asor-wimse-agent-delegation-chain-03** (new-draft, score 22, authorization) [none]: [Verifiable Attenuated Delegation for AI Agent Chains](https://datatracker.ietf.org/doc/draft-asor-wimse-agent-delegation-chain/) — AI agents increasingly delegate tasks to other agents.  Each
   delegation should convey only a subset of the delegating party's
   authority, that subset should be bounded in scope, magnitude, and
   time, and any enforcement point should be able to verify -- offline,
   with no call to an authorization server -- that a token presented at
   hop N carries authority no greater than the token at hop N-1, back to
   a trusted root, and that every hop acts under the same accountable
   principal.  OAuth 2.0 Token Exchange (RFC 8693) models two-party
   delegation and records prior actors in a nested "act" claim, but that
   claim is informational only and cannot enforce attenuation across a
   chain of depth two or more.  This document defines the Agent
   Delegation Chain: a profile of OAuth 2.0 JWT access tokens (RFC 9068)
   that carries authority as Rich Authorization Requests (RFC 9396),
   binds the chain to one principal and names the agent acting at each
   hop, links each delegation to its parent by a cryptographic byte-
   commitment, and specifies a deterministic offline verification
   algorithm that enforces monotonic attenuation, bounded depth,
   monotonic expiry, and principal invariance.  It reuses existing JOSE,
   proof-of-possession (RFC 9449), and status-list machinery (the OAuth
   Status List draft) and introduces no new cryptography.
- **draft-martinez-itp-agent-mandates-00** (new-draft, score 22, authorization) [none]: [Invoice Trust Protocol (ITP): Agent Mandates](https://datatracker.ietf.org/doc/draft-martinez-itp-agent-mandates/) — This document lets a business authorize a software agent to issue,
   accept, reject, or dispute invoices, and to report payments, through
   the Invoice Trust Protocol (ITP), within limits that the business
   sets.  An authorization is a mandate: a Selective Disclosure JSON Web
   Token (SD-JWT) credential issued by the business to a key held by the
   agent and enforced by a named ITP node that records each use.
- **draft-ietf-spice-sd-cwt-09** (new-draft, score 21, verifiable_claims) [spice]: [Selective Disclosure CBOR Web Tokens (SD-CWT)](https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/) — This specification describes a data minimization technique for use
   with CBOR Web Tokens (CWTs).  The approach is inspired by the
   Selective Disclosure JSON Web Token (SD-JWT), with changes to align
   with CBOR Object Signing and Encryption (COSE) and CWTs.
- **draft-lemonnier-scitt-decision-provenance-00** (new-draft, score 21, trust_infrastructure) [none]: [Decision Provenance for SCITT: binding software releases and agent actions to the decisions behind them](https://datatracker.ietf.org/doc/draft-lemonnier-scitt-decision-provenance/) — Build attestations, bills of materials and Signed Statements in a
   Transparency Service record what was built and by whom.  None records
   the decision to ship: who approved it, on what authority, what they
   were shown, and why.  The statement profiles for AI agent actions
   have the same gap, and say so: their human-approval fields are the
   producer's claim.  This document describes how a decision record and
   its action-binding attachment, as the extension proposals of the
   Decision Provenance Standard define them, sit under a release
   statement, a build attestation or an agent action record by typed
   digest references; how a verifier checks them offline, including the
   approver's signature where one is carried; and how the witness
   checkpoints of the anchoring extension are registered in a
   Transparency Service.  Nothing in the SCITT architecture, in Signed
   Statements or in Receipts changes.  A software release decision and
   an agent action capsule are the worked examples; the model has no
   feature specific to either.  This document is independent of the
   Decision Provenance Standard, is not part of it, does not change it,
   and is not endorsed by its Steward.
- **draft-bailey-scitt-agent-session-receipt-00** (new-draft, score 20, trust_infrastructure) [none]: [Causal Provenance Receipts for Agent Sessions: A SCITT Profile](https://datatracker.ietf.org/doc/draft-bailey-scitt-agent-session-receipt/) — This document defines a Supply Chain Integrity, Transparency, and
   Trust (SCITT) payload profile for agent session provenance: signed
   records that bind an autonomous agent session's lifecycle (start,
   governed tool dispatch, state transitions, termination, and
   settlement) to offline-verifiable cryptographic evidence, with an
   explicit head commitment that detects local hash-chain truncation and
   whole-store rollback.  It reuses the SCITT architecture and COSE
   receipt envelope: the Causal Provenance Receipt (CPR) bundle is the
   signed statement payload, and registration with a Transparency
   Service is optional and explicitly disclosed.  This profile addresses
   the session-lifecycle and resumption-evidence grain rather than
   isolated per-action telemetry, while preserving bounded verifier
   semantics: a verifier checks cryptographic signatures, canonical
   digests, chain links, and external anchors; it does not prove that
   unallegeable physical events occurred.
- **draft-narajala-courtney-ansv2-02** (new-draft, score 20, adjacent_watchlist) [none]: [Agent Name Service v2 (ANS): A Domain-Anchored Identity Layer for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-narajala-courtney-ansv2/) — Autonomous AI agents now invoke one another across organizational
   boundaries over protocols such as the Model Context Protocol (MCP)
   and Agent2Agent (A2A).  A relying party has no interoperable way to
   bind a discoverable agent endpoint to the holder of its domain
   (optionally verified as a legal entity), a specific software release,
   and an auditable issuance history.  This document specifies the
   architecture of Agent Name Service version 2 (ANS v2), an identity
   layer, anchored in DNS domains, that binds an agent endpoint to its
   domain holder, its release, and its history.  ANS v2 composes systems
   the Internet already runs (the DNS with DNSSEC; the Web PKI, with
   DANE where operators publish it; and an append-only transparency log)
   and introduces no new root of trust.

   Every ANS v2 agent carries a versioned name rooted in a DNS domain
   that the registrant controls.  When a registrant registers an agent,
   the Registration Authority (RA) checks the registrant's control of
   that domain, can issue an Identity Certificate that binds the
   versioned name to the agent's key, and submits a signed registration
   record to a Merkle-tree transparency log.  Under the current
   specifications, a new version is a new registration and a new log
   entry, so a verifier can pin an agent to a specific release.  Any
   third party can detect a rewritten log by computing, from the log's
   public tiles, a consistency proof between two of its signed
   checkpoints.

   For discovery, ANS v2 adopts the SVCB records and SvcParams of DNS
   for AI Discovery (DNS-AID) as its default format, and keeps an older
   TXT-based format only as an opt-in profile.  Beyond those discovery
   records, ANS v2 specifies one DNS record, an "_ans-badge" TXT record
   that points to the agent's transparency-log entry; the log seals the
   fingerprint of the agent server's certificate, and operators can add
   DANE records.  With these records, a verifier resolves an agent,
   authenticates its TLS endpoint, and confirms that the presented name,
   version, and key match a logged registration.

   This document also states a threat model covering agent
   impersonation, DNS spoofing, CA and Registration Authority
   compromise, version rollback, agent card tampering, and log
   rewriting, and names what each ANS check does and does not prevent.
   The reference registry, transparency log, verifier, JSON Schemas,
   SDKs, and CLI are open source.
- **draft-chueayen-attestation-receipts-05** (new-draft, score 19, trust_infrastructure) [none]: [Enforcement Attestation Receipts for AI Inference and Agent Action Decisions](https://datatracker.ietf.org/doc/draft-chueayen-attestation-receipts/) — This document specifies two compact JSON records, signed with Ed25519
   and verifiable offline under a pinned public key.  The first is an
   attestation receipt for an AI inference decision, binding an outcome
   to a request hash.  The second, added in this revision, is an action
   record: the decision an enforcement point takes before an agent's
   proposed tool call or other state-changing action runs, whether that
   decision is to allow or to refuse.  An action record is signed by the
   enforcement point, never by the agent, and binds the decision to a
   hash of the exact canonical arguments proposed.  The document also
   describes how a human approval can be bound to exact action values
   with single use and expiry, how either record could be carried as a
   COSE_Sign1 Signed Statement and registered with a SCITT Transparency
   Service, and where the current format does not yet do so.  Both
   formats are intended for settings where an operator-controlled log is
   not, on its own, sufficient evidence of the decision.
- **draft-reddy-wimse-oauth-dialog-binding-00** (new-draft, score 19, core_identity) [none]: [Binding Agent Dialogs to WIMSE and OAuth Credentials](https://datatracker.ietf.org/doc/draft-reddy-wimse-oauth-dialog-binding/) — AI agents and tools that take part in a dialog carry a dialog context
   with each request and response.  This document specifies how the
   dialog context is bound to WIMSE and OAuth credentials.  It extends
   the WIMSE profile of HTTP Message Signatures, for requests and
   responses, and the WIMSE Proof Token, for requests, to cover the
   dialog context, records the dialog identifier in OAuth transaction
   tokens, and describes how a new dialog at a trust boundary aligns
   with OAuth identity chaining.  A receiver can then verify who sent a
   request or response, which dialog it belongs to, and, for a request,
   what it may do, and that the answers agree.
- **draft-watts-ai-identity-01** (new-draft, score 19, trust_infrastructure) [none]: [AID-1: A Cryptographically Bindable Identity and Provenance Architecture for AI Systems](https://datatracker.ietf.org/doc/draft-watts-ai-identity/) — This document specifies AID-1, a provider-independent architecture
   for representing and verifying cryptographically bindable identity,
   delegation, authorization, action evidence, execution attestation,
   provenance, and governance information associated with AI systems and
   AI-mediated actions.  AID-1 intentionally separates signature
   validity, identity binding, authority, execution evidence,
   provenance, and downstream admissibility.  The specification defines
   trust domains, signed envelopes, external key resolution, delegation
   credentials, authorization decisions, temporal and revocation checks,
   replay protection, typed provenance claims, and a deterministic
   verification order with ALLOW, DENY, and INDETERMINATE outcomes.
- **draft-drake-agent-identity-problem-statement-01** (new-draft, score 18, adjacent_watchlist) [none]: [Identity for Autonomous Agents and Robots: Problem Statement, Threat Model, and Terminology](https://datatracker.ietf.org/doc/draft-drake-agent-identity-problem-statement/) — Autonomous software agents, and increasingly physical robots, now act
   at machine scale and speed across Internet protocols and throughout
   society, in roles whose decisions and actions can have legal,
   economic, safety, security, and physical consequences, often with
   limited or no human supervision.

   Any credential, authorization, delegation, certification, reputation,
   audit history, insurance policy, regulatory obligation, safety
   decision, liability, or legal process concerning an autonomous entity
   depends on being able to identify that same entity reliably over
   time.

   Conversely, when an autonomous entity or its operator is malicious,
   compromised, or beyond effective human control, the absence of
   durable identity lets it shed history, evade consequences, or
   multiply cheaply into Sybil swarms.

   Many proposed mechanisms bind claims to identifiers, accounts,
   credentials, keys, or names that can be replaced, reassigned,
   transferred, revoked, suspended, or lost.  They may authenticate that
   subject perfectly while still failing to establish a durable identity
   for the entity it represents.

   This document offers precise terminology that distinguishes identity
   from the identifiers, attributes, credentials, authorizations, and
   reputation with which it is commonly conflated, minting the term
   "identity0" so that the strict sense has an unambiguous name.  It
   presents a layered reference model showing where current "agent
   identity" efforts fit and the durable identity layer they commonly
   presuppose but do not provide.

   This document is informational and defines no protocol.  It serves as
   the framing and vocabulary document for a companion series that
   specifies a federated durable-identity architecture, provisioning,
   resolution, application, and governance intended to provide a
   practical path from this problem statement to interoperable
   deployment.
- **draft-drake-agent-identity-resolution-01** (new-draft, score 18, core_identity) [none]: [Resolution and Verification of Agent Identities using DNS and RDAP](https://datatracker.ietf.org/doc/draft-drake-agent-identity-resolution/) — The Agent Identity Registry System (AIRS)
   ([I-D.drake-agent-identity-registry]) assigns a permanent canonical
   aid URN to the identity0 of an autonomous entity and maintains an
   authoritative record associated with that identifier.  This document
   defines the read side of AIRS: how a Relying Party finds the
   authoritative resolution service, retrieves the public record,
   resolves a handle to the canonical identifier, and verifies a
   Registrar-issued credential presented for that identity.

   Discovery uses the DNS-based URN Dynamic Delegation Discovery System
   (DDDS) and lookup uses the Registration Data Access Protocol (RDAP).
   Credential verification reuses the OAuth 2.0 JWT access-token and
   sender-constraint profiles defined by the AIRS registry architecture;
   this document defines no new credential format and no generic direct
   device-proof protocol.
- **draft-durga-agenttrust-trace-verification-00** (new-draft, score 18, trust_infrastructure) [none]: [Cryptographic Execution-Trace Verification, JCS Canonicalization, and Fail-Closed Delegation Attestation for Autonomous AI Agents](https://datatracker.ietf.org/doc/draft-durga-agenttrust-trace-verification/) — This document specifies a deterministic cryptographic verification
   profile for execution traces, delegation chains, and weight-custody
   manifests generated by autonomous artificial intelligence (AI) agents
   operating across Model Context Protocol (MCP), Agent-to-Agent (A2A),
   and enterprise system-of-record boundaries.  The profile binds JSON
   Canonicalization Scheme (JCS, RFC 8785) pre-image serialization,
   Ed25519 (RFC 8032) and ECDSA P-256/P-384 signatures, JSON Web Key
   (JWK, RFC 7517) thumbprint pinning, and fail-closed revocation and
   freshness checks so that relying parties can independently verify
   whether an agent action was authorized prior to commit.
- **draft-hood-agtp-lei-01** (new-draft, score 18, core_identity) [none]: [AGTP Binding to the Legal Entity Identifier (LEI and vLEI)](https://datatracker.ietf.org/doc/draft-hood-agtp-lei/) — The Legal Entity Identifier (LEI), defined by ISO 17442 and operated
   under the global governance of the Global Legal Entity Identifier
   Foundation (GLEIF), is the internationally recognized identifier for
   legal entities in financial transactions and regulatory reporting.
   The verifiable LEI (vLEI), built on Key Event Receipt Infrastructure
   (KERI) and Authentic Chained Data Containers (ACDC), extends the LEI
   into the digital trust ecosystem with cryptographically verifiable
   credentials issued through Qualified vLEI Issuers (QVIs).

   This document specifies how the Agent Transfer Protocol (AGTP) binds
   to the LEI and vLEI infrastructure.  It defines how an LEI is carried
   as the owner of an agent in its Agent Genesis and Identity Document,
   how a vLEI Legal Entity credential composes with AGTP-CERT to
   establish institutional identity at the wire, how a new verification
   path (vlei-anchored) is added to AGTP-TRUST for KERI-based
   verification, and how vLEI Role Credentials (OOR, ECR, AUTH) express
   the human authorization chain that produced an agent.

   The four layers compose: AGTP provides the agent identity substrate,
   the LEI provides the institutional identity, the vLEI provides
   cryptographic verification of that institutional identity, and the
   vLEI Role Credentials provide the authorization chain from the legal
   entity through human officers to the agent.  This document positions
   financial institutions, regulated entities, and other LEI holders to
   deploy agents with verifiable institutional identity from day one.
- **draft-hood-independent-agtp-10** (new-draft, score 18, core_identity) [none]: [Agent Transfer Protocol (AGTP)](https://datatracker.ietf.org/doc/draft-hood-independent-agtp/) — This document defines the Agent Transfer Protocol (AGTP): a transfer
   protocol for AI agent traffic.  AGTP carries agent identity,
   authority, delegation, and attribution as protocol elements of every
   exchange, on an eighteen-method floor of intent-named methods, over
   TCP/TLS or QUIC on IANA-assigned port 4480 and the IANA-registered
   agtp:// URI scheme.  The method vocabulary beyond the floor, the path
   grammar, and the endpoint contract are specified in [AGTP-METHODS];
   runtime negotiation of endpoints is specified in [AGTP-RCNS]; the
   agent identity document in [AGTP-IDDOC]; transport bindings in
   [AGTP-BINDINGS].  Version 10 adds per-request proof of possession, so
   that a verified identity document and a live sender are bound by
   signature; specifies the Delegation-Chain header with pre-
   authorization semantics (per-hop scope attenuation checked at mint
   and at verify, parent re-verification at each hop, depth and cycle
   limits, and defined failure behavior); maps the delegation model onto
   the WIMSE chain convention; resolves the 262 and 455 status codes by
   obtainability; adds structured failure fields to the status code
   model, states the protocol's position in the transfer-protocol
   vocabulary throughout, and moves module material to companion
   specifications so that this document carries the protocol and only
   the protocol.  AGTP is designed to compose with existing agent
   frameworks, which keep their own semantics and development paths.
- **draft-ietf-rats-posture-assessment-05** (new-draft, score 18, verifiable_claims) [rats]: [Remote Posture Assessment for Systems, Containers, and Applications at Scale](https://datatracker.ietf.org/doc/draft-ietf-rats-posture-assessment/) — This document establishes an architectural pattern whereby
   Attestation Results could be produced for a complete set of
   benchmarks or controls that are defined and grouped by an external
   entity, eliminating the need to convey individual Evidence items for
   each item within a benchmark or control framework.  This document
   establishes a pattern to list sets of benchmarks and controls within
   CWT and JWT formats for use as an Entity Attestation Token (EAT).
   While the discussion below pertains mostly to TPM, other Roots of
   Trust such as TCG DICE and non-TCG defined components will also be
   included.
- **draft-uppalapati-wimse-pq-agent-identity-01** (new-draft, score 18, core_identity) [none]: [Post-Quantum Requirements for Software and AI Agent Identity](https://datatracker.ietf.org/doc/draft-uppalapati-wimse-pq-agent-identity/) — A delegation record retained as evidence must remain verifiable long
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
- **draft-drake-agent-identity-registry-05** (new-draft, score 17, core_identity) [none]: [Agent Identity Registry System: A Federated Architecture for Durable Identity of Autonomous Entities](https://datatracker.ietf.org/doc/draft-drake-agent-identity-registry/) — This document defines the Agent Identity Registry System (AIRS): a
   federated architecture that gives the durable identity0 of an
   autonomous entity a permanent canonical identifier, maintains an
   authoritative record about that identity, binds proof of control to
   enrolled anchors, and issues credentials that relying parties can
   verify.  Identity0 and the distinction between an identity, its
   identifiers, its credentials, and its anchors are defined in
   [I-D.drake-agent-identity-problem-statement].  The canonical
   identifier is a URN in the "aid" namespace ([RFC8141]).

   At the sovereign and portable assurance tiers, each independently
   accepted identity requires its own manufacturer-attested physical
   anchor, and each accepted anchor backs at most one identity.  A
   device normally carries one accepted anchor, so identities at these
   tiers cost scarce physical units rather than software operations.
   Enclave and virtual tiers can provide useful hardware-backed key
   protection without making that physical-scarcity claim; a declared
   tier permits software-only participation.  The architecture separates
   governance, authoritative registry operation, and competing
   Registrars, and uses standard OAuth 2.0 JWT access tokens conforming
   to [RFC9068] for authenticated use.
- **draft-emerson-oauth-user-mediated-delivery-01** (new-draft, score 17, core_identity) [none]: [User-Mediated Credential Delivery as a Complementary Authorization Primitive for AI Agents](https://datatracker.ietf.org/doc/draft-emerson-oauth-user-mediated-delivery/) — This document proposes user-mediated credential delivery as a
   complementary authorization primitive for AI agent frameworks.
   Rather than delivering credentials through automated channels
   controlled by the agent or its platform, user-mediated delivery
   places the authorization decision and credential delivery in the
   user's trusted context, separate from the agent's execution
   environment.

   This document describes four methods: user-mediated credential
   delivery, self-describing connection credentials, caller-identity
   consent differentiation, and discovery-by-introspection.  These
   methods address the human-in-the-loop gap identified in Section 10.7
   of [KLRC] and strengthen the authorization foundation that the IETF
   AI Agent Authentication and Authorization framework depends on.  This
   revision relates the primitive to the gap analysis in [CHEN-UC] and
   to the intent credential proposed in [INTENT], states how it composes
   with grant-layer mechanisms, and reports implementation status.

   The methods described in this document are patent pending.
- **draft-hood-agtp-composition-02** (new-draft, score 17, core_identity) [none]: [AGTP Composition Profiles](https://datatracker.ietf.org/doc/draft-hood-agtp-composition/) — The Agent Transfer Protocol (AGTP) operates as a substrate beneath
   several adjacent layers: Agent Group Messaging Protocols (AGMPs) such
   as the Model Context Protocol (MCP), the Agent-to-Agent Protocol
   (A2A), and the Agent Communication Protocol (ACP); external identity
   providers (OAuth, OIDC, enterprise IdPs); and HTTP-based clients that
   interact with agents through translation gateways.  This document
   specifies the composition profiles for each of these adjacent layers,
   defining normative mapping rules between the adjacent layer and AGTP.

   Three composition families are specified.  The AGMP composition
   profile specifies how MCP, A2A, and ACP messages are carried over
   AGTP, with mapping rules for identity, authority scope, delegation,
   and session fields between the AGMP and AGTP layers.  The External
   Identity Provider composition profile specifies how AGTP agent
   identity composes with externally-issued credentials, treating "which
   agent" and "on whose behalf" as orthogonal axes.  The HTTP Gateway
   composition profile specifies the translation surface for accepting
   HTTP traffic into AGTP- served agents as a REST adoption ramp.

   Across all three families, AGTP headers take precedence over
   equivalent adjacent-layer fields for all infrastructure-level
   routing, enforcement, and audit operations.  Agents gain transport-
   level governance, observability, and identity without modification to
   the adjacent layers.
- **draft-ietf-oauth-delegate-sd-jwt-00** (new-draft, score 17, verifiable_claims) [oauth]: [Delegate SD-JWT](https://datatracker.ietf.org/doc/draft-ietf-oauth-delegate-sd-jwt/) — This document specifies an extension to Selective Disclosure JSON Web
   Tokens [RFC9901] to support further delegation from the Holder to a
   Delegate Holder.  This is done by allowing the Key Binding JWT to
   also be an SD-JWT, optionally with its own Key Binding.  This has
   particular applicability to Agentic systems.
- **draft-watts-agent-evidence-boundary-01** (new-draft, score 17, core_identity) [none]: [Evidence-Bounded Authorization for Agentic Systems: Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-agent-evidence-boundary/) — Autonomous agents increasingly make or propose consequential actions
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
- **draft-watts-ai-identity-conformance-01** (new-draft, score 17, trust_infrastructure) [none]: [AID-1 Provider-Independent Conformance Requirements and Test-Vector Model](https://datatracker.ietf.org/doc/draft-watts-ai-identity-conformance/) — This document defines provider-independent conformance requirements
   for AID-1.  It specifies the execution model for a deterministic
   machine-readable test-vector corpus, including canonicalization,
   cryptographic, identity-binding, delegation, authorization, temporal,
   revocation, replay, attestation, provenance, and integration cases.
   The conformance corpus contains 69 vectors.  Six replay cases are
   architectural boundary tests, including R5, which requires AID-1
   verification to succeed while a downstream D6 scientific-
   admissibility decision rejects the same evidence.
- **draft-zambo-aer1-wimse-mapping-01** (new-draft, score 17, trust_infrastructure) [none]: [AER-1 Receipts as Audit Records for WIMSE AIMS](https://datatracker.ietf.org/doc/draft-zambo-aer1-wimse-mapping/) — The WIMSE AI Identity Management System (AIMS) framework requires
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
- **draft-ayerbe-trip-protocol-05** (new-draft, score 16, core_identity) [none]: [TRIP: Trajectory-based Recognition of Identity Proof](https://datatracker.ietf.org/doc/draft-ayerbe-trip-protocol/) — This document specifies the Trajectory-based Recognition of Identity
   Proof (TRIP) protocol, a decentralized mechanism for establishing
   claims of physical-world presence through cryptographically signed,
   spatially quantized location attestations called "breadcrumbs."
   Breadcrumbs are chained into an append-only log, bundled into
   verifiable epochs, and distilled into a Trajectory Identity Token
   (TIT) that serves as a persistent pseudonymous identifier.

   The protocol employs a Criticality Engine, a statistical anomaly
   detector informed by complex-systems research, to distinguish
   biological movement from synthetic trajectories.  Power Spectral
   Density (PSD) analysis of the displacement series yields a scaling
   exponent alpha that captures long-range temporal correlation in
   movement.  A six-component Hamiltonian energy function scores each
   breadcrumb against the identity's learned behavioral profile in real
   time.

   This revision (-05) reframes the statistical core of the Criticality
   Engine in light of empirical validation against human-mobility data:
   the PSD scaling exponent alpha is specified as a per-deployment-
   calibrated scored feature rather than a fixed classification gate;
   the fixed [0.30, 0.80] "biological" band is withdrawn in favor of
   calibrated ranges; the asserted Levy-PSD bridge is replaced by a
   statement of the independence of the step-size and temporal-
   correlation features; and a new validation section reports separation
   results and methodology.  The cryptographic chain, RATS mapping,
   Active Verification Protocol, and privacy model are unchanged from
   -04.

   TRIP is designed to be transport-agnostic and operates independently
   of any particular naming system, blockchain, or application layer.
- **draft-gilda-audit-agent-audit-record-03** (new-draft, score 16, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-audit-agent-audit-record/) — This document defines a record format for AI agent authorization
   decisions and the effects that followed them.  The format is one in-
   toto predicate type, signed inside a DSSE envelope.  A record carries
   the decision and the observed effect with a derived agreement between
   them, whether the decision point could evaluate the request and how
   fresh each input it relied on was, and a canonicalization contract
   under which a party that trusts neither the agent nor its operator
   recomputes the record's consistency from its bytes.  The document
   also defines what a party that retains a record keeps beside it, so
   that the record can later be dated from anchors that party does not
   control.  The format carries the seven minimum audit fields of the
   WIMSE AI Identity Management System framework, and it is offered as a
   data model for the audit records the proposed AUDIT working group
   would specify.  It defines no policy.
- **draft-ietf-oauth-sd-jwt-vc-22** (new-draft, score 16, verifiable_claims) [oauth]: [SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) — This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.
- **draft-mih-sokolov-scitt-payload-binding-06** (new-draft, score 16, trust_infrastructure) [none]: [Canonicalization Declaration for SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-mih-sokolov-scitt-payload-binding/) — Independently written systems that anchor records to a SCITT
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
- **draft-ni-wimse-ai-agent-identity-04** (new-draft, score 16, agent_identity) [none]: [WIMSE Applicability for AI Agents](https://datatracker.ietf.org/doc/draft-ni-wimse-ai-agent-identity/) — This document discusses WIMSE applicability to Agentic AI, so as to
   establish independent identities and credential management mechanisms
   for AI agents.  It also discusses mechanisms for cryptographically
   binding an AI agent identity to an accountable user or organization.
- **draft-rampertab-audit-agent-authority-history-00** (new-draft, score 16, core_identity) [none]: [Replayable Authority Histories for Auditing Automated Agents](https://datatracker.ietf.org/doc/draft-rampertab-audit-agent-authority-history/) — Software agents act on authority that changes while they run:
   permissions are granted and revoked, running instances are replaced,
   and some requests are refused.  Activity logs record what a system
   reports it did, but they do not by themselves show what an agent was
   allowed to do when it acted, and the operator can edit them.  This
   document specifies a model for an authority history: an append-only,
   signed record of who granted what to whom, which actions were
   admitted, which requests were refused, and which unfinished duties
   survive when one agent replaces another.  Given independently
   authenticated owner keys and history identity, a verifier can replay
   the history and recompute its recorded authorization decisions while
   trusting neither the agent nor the operator.  The document states
   what such a verifier can and cannot establish.  Optional profiles
   cover external anchoring, federated operation, human-attested keys
   and zero-knowledge disclosure.  An informative appendix describes one
   encoding.
- **draft-raskar-agentic-web-federated-resolution-02** (new-draft, score 16, adjacent_watchlist) [none]: [Registry-Assisted Resolution for Known Subjects Without DNS Discovery Anchors](https://datatracker.ietf.org/doc/draft-raskar-agentic-web-federated-resolution/) — Discovery mechanisms for AI resources increasingly use DNS and mDNS
   as interoperable publication and lookup substrates.  These mechanisms
   work well when the publisher controls a usable DNS discovery anchor.
   They do not cover every deployment.  An individual may control an
   email or platform account without controlling the provider's DNS
   namespace.  A small organization may use managed infrastructure
   without operating an agent-specific DNS publication point.  A
   workload may have a stable identity that is not itself DNS anchored.

   This document describes Registry-Assisted Resolution for the narrower
   case in which a discovering entity already knows the Subject Identity
   it wants to resolve, but no usable DNS Discovery Anchor is available
   or selected by local policy.  A configured registry returns the
   minimum information needed to continue discovery, together with
   provenance, authority evidence, freshness, and revocation
   information.

   This mechanism is complementary to DNS-based discovery.  A validated
   direct DNS-anchored discovery path remains direct and is normally
   preferred for a domain-controlled subject.  This document does not
   define open-ended search, semantic matchmaking, ranking, capability
   search, a global registry, registry discovery, directory-to-directory
   routing, identity management, or trust evaluation.

   Multiple independently operated registries may implement the same
   resolution profile.  Registry selection is a client or deployment
   policy decision; no universal NandaIndex or global root is assumed.
   NandaIndex is described as one reference implementation of this
   model.
- **draft-sharaf-brick-agent-definition-00** (new-draft, score 16, core_identity) [none]: [BRICK: Portable Definition and Composition of AI Agents](https://datatracker.ietf.org/doc/draft-sharaf-brick-agent-definition/) — BRICK proposes a vendor-neutral JSON construction contract for AI
   agents.  It defines agent identity, goals, capabilities, instruction
   and skill references, explicitly namespaced MCP tool dependencies,
   and an optional projection to A2A Agent Cards.  It references the
   existing MCP, A2A, and Agent Skills specifications rather than
   redefining their protocols or formats.  BRICK does not prescribe a
   language model, reasoning engine, deployment platform, discovery
   service, or authorization protocol.
- **draft-watts-protocol-test-evidence-profile-01** (new-draft, score 16, trust_infrastructure) [none]: [Protocol Conformance Test Evidence Records: A Reproducibility Profile](https://datatracker.ietf.org/doc/draft-watts-protocol-test-evidence-profile/) — This document proposes a narrow record profile for describing
   software protocol-conformance test runs, including the tested
   artifact, test suite, implementation, execution environment,
   individual case outcomes, digests, and known limitations.  It does
   not define a new signature scheme, attestation architecture,
   transparency service, or general-purpose test-output language.
   Implementations are encouraged to reuse existing mechanisms such as
   SCITT statements, RATS terminology, COSE, JSON canonicalization, and
   existing test-report formats where suitable.  This individual draft
   candidate has not been submitted to or endorsed by the IETF.
- **draft-drake-agent-identity-governance-01** (new-draft, score 15, adjacent_watchlist) [none]: [The Agent Identity Authority: A Multi-Stakeholder Governance Framework for the Agent Identity Registry System](https://datatracker.ietf.org/doc/draft-drake-agent-identity-governance/) — The Agent Identity Registry System (AIRS) provides durable identity
   infrastructure for autonomous entities such as AI agents and robots,
   with graduated assurance ranging from scarcity-backed physical
   anchors through protected-key and software-only participation.  Its
   companion specifications deliberately do not define or empower a
   governance authority; they describe the functions such an authority
   must perform and defer its constitution to a separate effort.

   This document defines that body: the Agent Identity Authority (AIA).
   It specifies the Authority's name, legal form, mission, and
   relationship to the protocol specifications; its membership
   categories and Board composition; binding geographic-diversity rules
   and non-binding advisory recommendations for ideal composition; the
   accreditation, dispute-resolution, hardware trust store,
   transparency, and funding frameworks it operates; and the bootstrap
   process by which the Authority forms and assumes stewardship of the
   global production namespace.

   The Authority governs infrastructure, not behavior: it stewards the
   aid namespace, hardware roots of trust, accreditation, and production
   Registry Operator succession.  It does not regulate what agents do.
   Its legitimacy derives from being the least-objectionable steward of
   a shared resource, in the tradition of ICANN, the regional Internet
   registries, and the W3C, and its charter is designed so that no
   single nation, region, or company can capture it or holds a formal
   veto over it, although supermajority rules let a large enough
   coordinated bloc block consequential decisions.
- **draft-ietf-oauth-identity-assertion-authz-grant-06** (new-draft, score 15, authorization) [oauth]: [Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) — This specification provides a mechanism for an application to use an
   identity assertion to obtain an access token for a third-party API by
   coordinating through an identity provider that the downstream
   Resource Authorization Server already trusts for single sign-on
   (SSO), using OAuth 2.0 Token Exchange (RFC 8693) and the JWT Profile
   for OAuth 2.0 Authorization Grants (RFC 7523).  This pattern is
   informally referred to as Cross-App Access (XAA).
- **draft-ietf-rats-eat-da-00** (new-draft, score 15, trust_infrastructure) [rats]: [An EAT Profile for Trustworthy Device Assignment](https://datatracker.ietf.org/doc/draft-ietf-rats-eat-da/) — In confidential computing, device assignment (DA) is the method by
   which a device (e.g., network adapter, GPU), whether on-chip or
   behind a PCIe Root Port, is assigned to a Trusted Virtual Machine
   (TVM).  For the TVM to trust an assigned device, the device must
   provide the TVM with attestation Evidence confirming its identity,
   the state of its firmware and configuration.

   Since Evidence claims can be processed by 3rd party entities (e.g.,
   Verifiers, Relying Parties) external to the TVM, there is a need to
   standardize the representation of DA-related information in Evidence
   to ensure interoperability.  This document defines an attestation
   Evidence format for DA as an EAT (Entity Attestation Token) profile.
- **draft-sethi-openaiis-protocol-00** (new-draft, score 15, authorization) [none]: [OpenAIIS -- A Decentralized Trust, Governance and Safety Protocol for the Digital World](https://datatracker.ietf.org/doc/draft-sethi-openaiis-protocol/) — Open Artificial Intelligence Integrity Sentinel (OpenAIIS) specifies
   a decentralized trust, governance, and safety protocol for digital
   activity performed by people, organizations, and autonomous AI
   agents.  It binds digital assertions and consequential actions to
   authenticated issuers, scoped authority, accepted responsibility,
   supporting evidence, and a verifiable history.  A canonical, domain-
   separated signature authenticates each typed claim; ordered Merkle
   records and signed checkpoints establish its historical registry
   context.

   Every accepted registry record enters an automatic, durable process
   that commits covering checkpoints to Bitcoin mainnet.  The resulting
   portable proof binds the exact signed claim and its authenticated
   history to Bitcoin's proof-of-work chain, protecting historical
   evidence against retroactive substitution or rewriting without the
   work required to establish an accepted competing Bitcoin history.
   Governance and safety records express consent, delegation,
   authorization, revocation, withdrawal, disputes, and security
   incidents.  Independent implementations can verify both historical
   commitments and the evidence governing present action without relying
   exclusively on the system that issued or executed a claim.  OpenAIIS
   supports versioned decentralized consensus profiles without a
   protocol-native currency.
- **draft-thaha-wimse-agent-evidence-binding-01** (new-draft, score 15, core_identity) [none]: [Evidence Binding for AI Agent Credentials](https://datatracker.ietf.org/doc/draft-thaha-wimse-agent-evidence-binding/) — The WIMSE AI Identity Management System (AIMS) requires tamper-
   evident agent audit logs but does not specify their format or
   discovery.  This document maps the AIMS minimum fields to the SCITT
   Agent Execution Evidence profile, defines one claim that binds a
   workload credential to the persistent agent, governing policy,
   expected Evidence Service and optional Assurance Statement, and
   defines an in-toto predicate type for carrying Execution Receipts in
   the audit format proposed for WIMSE.  It also describes how a service
   admits an agent's call by checking its assurance at the moment of the
   request, and defines an HTTP field that links each call to the
   caller's evidence.  It is input to the AIMS work and makes no change
   to it.
- **draft-hood-agtp-merchant-identity-03** (new-draft, score 14, adjacent_watchlist) [none]: [AGTP Merchant Identity and Agentic Commerce Binding](https://datatracker.ietf.org/doc/draft-hood-agtp-merchant-identity/) — The Agent Transfer Protocol (AGTP) specifies the sending side of an
   agentic transaction: agent identity, Authority-Scope enforcement,
   Budget- Limit declaration, and a signed Attribution-Record on every
   method invocation.  The receiving side of a PURCHASE transaction --
   the merchant or service provider -- has no equivalent protocol-level
   identity or verification mechanism.  That asymmetry is the gap this
   document closes.

   This document specifies the AGTP Merchant Identity and Agentic
   Commerce Binding.  It defines a merchant in AGTP as an agent whose
   Agent Identity Document carries role: "merchant", specifies the
   merchant-specific fields that ride on the Agent Identity Document
   under that declaration, aligns Merchant Trust Tiers with AGTP Trust
   Tier semantics, and defines the protocol integration points at which
   merchant identity is verified.  These include the PURCHASE method
   handshake, the DISCOVER method result surface, and the Attribution-
   Record.  This document also defines the Intent-Assertion header for
   portable, detached principal-authorized intent, the Cart-Digest
   mechanism for multi-line-item transactions, and the 458 Counterparty
   Unverified status code.  Together these mechanisms close the
   verification loop between agent and merchant within AGTP's governance
   model.

   Version 02 unifies merchant identity onto the Agent Genesis + Agent
   Identity Document architecture: there is no separate Merchant Genesis
   document type.  A merchant is an agent with role: "merchant" declared
   in its Agent Identity Document.  This reflects the architectural
   principle that identity is permanent (carried on Genesis) and
   capability is mutable (carried on the Identity Document); a role
   change re-mints no Agent-ID.
- **draft-ietf-wimse-workload-creds-03** (new-draft, score 14, core_identity) [wimse]: [WIMSE Workload Credentials](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones up to complex multi-service, multi-cloud, multi-
   tenant deployments.

   This document defines the credentials that workloads use to represent
   their identity.  They can be used in various protocols to
   authenticate workloads to each other.  To use these credentials,
   workloads must provide proof of possession of the associated private
   key material, which is covered in other documents.  This document
   focuses on the credentials alone, independent of the proof-of-
   possession mechanism.
- **draft-ietf-wimse-workload-identity-practices-08** (new-draft, score 14, core_identity) [wimse]: [Workload Identity Practices](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) — This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture and associated
   protocols.
- **draft-watts-rats-verification-promotion-appraisal-01** (new-draft, score 14, trust_infrastructure) [none]: [Verification Promotion and Agent Assurance Appraisal Profile](https://datatracker.ietf.org/doc/draft-watts-rats-verification-promotion-appraisal/) — This document maps protocol-verification evidence and the WIVL
   assurance-stage model onto the RATS architecture.  It defines
   appraisal requirements for SPEC_VALIDATED, LOCAL_CONFORMANT,
   INDEPENDENTLY_REPRODUCED, and SECURITY_TESTED results while
   preserving unknown evidence and requiring arithmetic preconditions
   for mathematical test vectors.  An attestation result reports bounded
   assurance; it is not an authorization grant or production-release
   decision.
- **draft-agentic-ai-usecases-requirements-05** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-dinuzzo-best-protocol-02** (new-draft, score 13, authorization) [none]: [BEST: The Behavioral State Protocol](https://datatracker.ietf.org/doc/draft-dinuzzo-best-protocol/) — The Behavioral State Protocol (BEST) defines a discovery-first,
   behaviour-oriented interaction surface for domain services: the
   commands a service accepts, the events it publishes, and optionally
   the queries it answers and the multi-step recipes (workflows) it
   publishes.  Services are named by DNS domain names and self-describe
   through a manifest at the well-known URI "/.well-known/best";
   messages use a conformant profile of the CloudEvents 1.0 envelope
   described by JSON Schema; and an agent obtains its own credential
   through the OAuth 2.0 Device Authorization Grant, approved by the
   person it acts for in their own browser.  BEST deliberately specifies
   only the interaction surface -- never a service's internal
   architecture, storage, or execution model -- allowing independent
   implementations across any runtime, language, or transport to
   interoperate without bespoke integration.
- **draft-gruszka-scitt-statement-identification-03** (new-draft, score 13, trust_infrastructure) [none]: [Requirements and Test Cases for Identifying SCITT Signed Statements](https://datatracker.ietf.org/doc/draft-gruszka-scitt-statement-identification/) — This document describes proposed requirements and test cases for
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
- **draft-tanase-ain-authoritative-resolution-01** (new-draft, score 13, core_identity) [none]: [Authoritative Resolution and Pre-Interaction Verification of Persistent Digital Agent Identities](https://datatracker.ietf.org/doc/draft-tanase-ain-authoritative-resolution/) — This document specifies AIN-WRP, a protocol-independent mechanism for
   authoritative resolution of persistent digital-agent identities and
   for verification of relationship-specific state before a digital
   agent begins a protected interaction with another registered agent or
   with a non-agent service or system.  Each digital agent participating
   in AIN-WRP identity resolution is identified by its own persistent
   Agent Identity Number (AIN).  The AIN is the stable anchor used to
   resolve lifecycle, operator, authority, restriction, endpoint,
   provenance and cryptographic evidence from sources competent for the
   corresponding assertions.  Where the counterparty is a non-agent
   target, a target reference identifies the intended resource or
   service without being treated as an alternative digital-agent
   identity.  AIN-WRP correlates the required evidence for the proposed
   interaction and can produce a Pre-Interaction Trust State or an
   optional State Proof.  Verification does not itself execute the
   operation or replace receiving-domain enforcement.

   The specification distinguishes persistent agent identity from
   credentials, proof of control, delegated authority, operational
   eligibility, local admission decisions and execution.  AIN-WRP
   applies at or before the admission boundary of A2A, MCP, API,
   transactional, messaging and other operational protocols.  An
   identity or target reference alone does not establish the authority,
   validity or eligibility of the proposed interaction.
- **draft-agentproto-context-management-architecture-00** (new-draft, score 12, core_identity) [none]: [Context and Correlation Management Architecture for Distributed Agentic Activities](https://datatracker.ietf.org/doc/draft-agentproto-context-management-architecture/) — Agentic applications increasingly distribute a single objective
   across autonomous agents, tools, and services implemented by
   different vendors, operated by different organizations, and connected
   through different protocols.

   A single activity may contain multiple pairwise dialogs, multiple
   tasks within each dialog, tool invocations, derived resources,
   downstream delegations, and later interactions that reinterpret or
   reuse artifacts produced earlier in the activity.  Existing protocols
   provide useful local identifiers for their own interactions, but
   those identifiers do not by themselves provide a common information
   model for correlating independently maintained dialogs, tasks, and
   resources across protocol and administrative boundaries.

   This document defines an information model consisting of Activities,
   Dialogs, Tasks, Resources, and typed Relationships.  It distinguishes
   Activity correlation from protocol-local Dialog context, and
   distinguishes stable resource identity and provenance from locally
   defined interpretations.

   As such, this document develops a context-and-correlation
   information-model architecture, not a functional reference
   architecture or a wire protocol.  It identifies relevant objects and
   relationships, relevant to maintaining coherent context, and examines
   the implications for preserving and propagating their correlations.
   It does not define the procedures by which applications execute work.
   The model distinguishes the logical extent of an Activity, which may
   extend beyond protocol-managed correlation; extending that coverage
   is selective, while maintaining established managed correlations
   entails responsibilities.
- **draft-cabanillas-nmop-policy-sharing-model-00** (new-draft, score 12, adjacent_watchlist) [none]: [Model for distributed policy sharing](https://datatracker.ietf.org/doc/draft-cabanillas-nmop-policy-sharing-model/) — This document defines mechanisms and conventions for the
   representation, lifecycle management, and distribution of policies in
   distributed and automated environments.  It specifies a consistent,
   machine-readable, and interoperable framework that enables policies
   to be validated, exchanged, updated, and removed across heterogeneous
   systems and administrative domains.

   The framework defines how policies, expressed using Policy-as-Code
   (PaC) languages or other policy languages, are encapsulated and
   managed using YANG as a canonical representation format.  By
   separating policy lifecycle management from policy semantics,
   enforcement architectures, and trust frameworks, the model enables a
   common policy artifact representation that can be reused across
   diverse implementations and deployment environments.

   The model represents policy languages using YANG identities and
   identity references, allowing new policy languages to be incorporated
   without modifying the core schema.  This approach supports
   extensibility while preserving a consistent structure for policy
   metadata, provenance, lifecycle management, and distribution.
- **draft-hood-agtp-agent-cert-04** (new-draft, score 12, core_identity) [none]: [AGTP Agent Certificate Extension](https://datatracker.ietf.org/doc/draft-hood-agtp-agent-cert/) — The Agent Transfer Protocol (AGTP) base specification verifies agent
   identity at the application layer: the Agent-ID header resolves to an
   issuer-signed Agent Identity Document, and a per-request Request-
   Signature proves possession of the key that document names.  That
   verification runs per request and needs the document.  This document
   specifies the AGTP Agent Certificate Extension: an optional mechanism
   that binds the Canonical Agent-ID, the recorded owner, and the
   Authority-Scope commitment to an X.509 v3 certificate presented
   during TLS mutual authentication, so that the same verification is
   made once at the handshake and infrastructure components including
   Scope-Enforcement Points (SEPs), load balancers, and governance
   gateways can enforce authority scope without application-layer
   access, at O(1) cost per request.  The extension also defines
   session-level revocation propagation via AGTP NOTIFY broadcast and
   records certificate issuance and revocation in the AGTP transparency
   log.

   Note: Certain mechanisms described in this document may be subject to
   pending patent applications by the author.  The licensor is prepared
   to grant a royalty-free license to implementers consistent with the
   IETF's IPR framework.  See Section 9.4.
- **draft-howe-agentproto-contact-center-usecases-00** (new-draft, score 12, agent_identity) [none]: [Contact Center Use Cases and Requirements for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-howe-agentproto-contact-center-usecases/) — Contact centers bring people, AI agents, and business systems into
   the same voice session.  Consumer-controlled agents are also
   beginning to call agents operated by businesses.  This document
   describes five contact center use cases for the agentic dialog
   management protocol: a consumer agent calling a business agent,
   escalation from an AI agent to a human representative, a call that
   resumes on another channel, a voice dialog passing through speech
   recognition and synthesis, and a dialog crossing an existing SIP or
   PSTN network.  It derives numbered requirements that can be
   incorporated into the working group's use cases and requirements
   document.  It also explains how a dialog identifier relates to the
   conversation records that contact centers already keep.
- **draft-ietf-acme-rats-03** (new-draft, score 12, trust_infrastructure) [acme]: [Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type](https://datatracker.ietf.org/doc/draft-ietf-acme-rats/) — This document describes an approach where an ACME Server can
   challenge an ACME Client to provide Evidence, Endorsements, or
   Attestation Result according to the Remote ATtestation procedureS
   (RATS) framework in any format supported by the Conceptual Message
   Wrapper (CMW).

   The ACME Server can optionally challenge the Client for specific
   claims that it wishes attestation for.
- **draft-reddy-seat-cc-workload-identity-00** (new-draft, score 12, trust_infrastructure) [none]: [Workload Identity Options for Attested TLS in Confidential Computing](https://datatracker.ietf.org/doc/draft-reddy-seat-cc-workload-identity/) — This document surveys how remote attestation for confidential
   computing is deployed by major cloud providers and derives the
   learnings.  Based on these, it presents multiple options for
   establishing the identity of a confidential workload in attested TLS
   for further discussion.  The list of options is not exhaustive, and
   additional options are welcome.  The purpose of this document is to
   help the SEAT working group decide on an approach or approaches for
   the confidential computing use case.
- **draft-seethiraju-dawn-dan-01** (new-draft, score 12, agent_identity) [none]: [DNS-Based Agent Naming (DAN): AIDISCA and AIINDEX Resource Records for AI Agent Discovery](https://datatracker.ietf.org/doc/draft-seethiraju-dawn-dan/) — The agentic AI ecosystem includes many different technologies and
   operations.  One important aspect is the ability to establish
   connections between AI agents.  In single-platform approaches, the
   processes and metadata with which AI agents discover, locate, and
   connect to each other are typically managed by their common platform.
   This document describes an inter-domain mechanism to enable AI agents
   to locate and connect to each other using necessary metadata and
   secure DNS associations, in a similar fashion to the way that DNS-
   Based Authentication of Named Entities (DANE), RFC6698, does for
   Transport Layer Security.  This is accomplished through two new
   Resource Record (RR) types: AI Discovery Association (AIDISCA) and AI
   Index (AIINDEX).
- **draft-shankarlingam-oauth-agent-dns-link-01** (new-draft, score 12, authorization) [none]: [Linking an Agent's DNS Name to its OAuth Client](https://datatracker.ietf.org/doc/draft-shankarlingam-oauth-agent-dns-link/) — Software agents increasingly call agents and services operated by
   other organizations.  A receiving organization often wants to know
   two things about any such caller: that it is the agent it claims to
   be, and that the organization operating it still authorizes it.
   Existing approaches to the second question require a trust
   relationship between the two organizations' authorization servers.

   This document defines a DNS record by which the owner of a domain
   links an agent's DNS name to the OAuth client that the agent uses at
   the owner's own authorization server.  The sending agent presents a
   fresh access token for that client; the receiver verifies the token
   against the record and against the issuer's published keys.  No trust
   relationship, registration or federation between the two
   organizations is needed, and disabling the client at the sending
   organization's authorization server stops the agent being accepted by
   every receiver.
- **draft-srivastava-agentproto-handoff-context-00** (new-draft, score 12, trust_infrastructure) [none]: [Signed Handoff Context for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-srivastava-agentproto-handoff-context/) — When one agent hands a task to another, the receiving agent often
   needs to know who handed it over, on whose behalf, through which
   earlier agents, and which prior context the work depends on.  It also
   needs to know that the handoff is fresh and meant for it, and the
   sender needs a clear answer back.  This document describes a small,
   transport-neutral handoff context: a signed offer, a signed status
   reply, and the chain of earlier offers that led to the current one,
   defined in CDDL for JSON and CBOR, with a lifecycle that maps to
   Agent2Agent task states.  Each offer names the one before it by hash,
   so that a dropped or reordered intermediate hop can be detected when
   the chain is carried.  Prior context is named by digest only; any log
   or transparency service behind it is opaque.  Appendices show how a
   SCITT receipt or a Learnlog signed head can be referenced.  The
   document is offered as input to the agentproto working group's use
   cases and dialog-context work.
- **draft-watts-oauth-agent-revocation-closure-03** (new-draft, score 12, core_identity) [none]: [Revocation Closure and Authority Epochs for Agent Delegation](https://datatracker.ietf.org/doc/draft-watts-oauth-agent-revocation-closure/) — Automated agents can exercise OAuth-derived authority through
   delegated credentials, child agents, asynchronous work, and
   operations spanning multiple administrative domains.  Invalidating an
   individual token does not necessarily establish that the authority
   represented by that token can no longer cause a new consequential
   operation.

   This document defines authority epochs, delegation-lineage
   requirements, admission fencing, and revocation-closure states for
   OAuth-based agent delegation.  It distinguishes token invalidation
   from authority closure and specifies that unresolved in-scope state
   produces UNKNOWN or PARTIAL rather than CLOSED.  The profile composes
   with OAuth Token Revocation, Token Exchange, Token Introspection,
   proof-of-possession mechanisms, Transaction Tokens, and workload-
   identity systems such as WIMSE.
- **draft-alla-agent-identity-document-02** (new-draft, score 11, core_identity) [none]: [The Agent Identity Document: A Hosted, Accountable Public Record for AI Agents](https://datatracker.ietf.org/doc/draft-alla-agent-identity-document/) — Autonomous software agents increasingly act on the public internet
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
- **draft-das-ai-safety-telecom-session-lifecycle-00** (new-draft, score 11, core_identity) [none]: [AI Safety for Telecommunications Session, Resource, Usage, and Charging State Consistency](https://datatracker.ietf.org/doc/draft-das-ai-safety-telecom-session-lifecycle/) — Part 04 of 15 describes Group C mechanisms for evidence-qualified
   reconstruction of subscriber trust, telecommunications session
   identity, home and visited operator state, programmable quality-of-
   service operation, resource reservation and installation, user-plane
   metering, charging, accounting, and deferred settlement.  It
   distinguishes an accepted API request from an installed network
   resource, a subscriber trust change from session release, a usage
   report from a financial obligation, and a local release from complete
   session closure.  It includes C-CW-01, six specialist embodiments,
   formal mathematics, flowcharts, and source-linked technical
   checkpoints.  Part 01 supplies common evidence and consistency
   semantics, while Parts 02, 03, 07, 11, 12, 14, and 15 cover
   complementary radio observations, incident repair, asynchronous
   processing, continuity, commerce, and protected operation boundaries.
   Positive observation consistency does not itself authorize
   consequential network actuation.

   The technical gap arises when individually valid subscriber, roaming,
   service, metering and charging records cannot be shown to apply to
   the same operation, generation, time and verified outcome.  This
   document specifies a source-qualified lifecycle graph with typed non-
   equivalent states, scoped three-valued evidence decisions, late-
   record correction, separate authority and effect-observation
   boundaries, practical implementation profiles, and failure/edge
   cases.  Nine source-derived RFCXML diagrams are explained in the
   body.  A standard-library Python reference and 87 synthetic tests
   illustrate selected in-memory algorithms; measured evaluator timings
   are not network latency, not peer reviewed and not field validation.
   Part 01 supplies shared evidence semantics; Parts 02, 03, 05, 07, 11,
   12, 14 and 15 address complementary inputs, failures and
   consequential effects.
- **draft-drake-agent-identity-epp-01** (new-draft, score 11, core_identity) [none]: [Extensible Provisioning Protocol (EPP) Mapping for Agent Identity and Handle Objects](https://datatracker.ietf.org/doc/draft-drake-agent-identity-epp/) — This document describes an Extensible Provisioning Protocol (EPP)
   mapping for the provisioning and management of agent identity objects
   and handle objects stored in the authoritative AIRS repository, as
   defined by the Agent Identity Registry System architecture.
   Specified in Extensible Markup Language (XML), these mappings define
   the interface between Registrars and the production Registry Operator
   for identities of autonomous entities.

   The mapping defines two objects: a permanent, non-expiring Agent
   Identity object keyed by a server-allocated canonical identifier, and
   a renewable, expiring Handle object that provides a human-readable
   alias.  It adds one registry function with no domain-name analogue:
   cross-Registrar uniqueness enforcement of enrolled anchor
   identifiers, including the scarce-anchor invariant where the parent
   architecture defines one.  Transfer authorization uses a actor-signed
   proof from an enrolled operational proof key in place of
   authorization-information passwords.
- **draft-hood-agtp-trust-03** (new-draft, score 11, adjacent_watchlist) [none]: [AGTP Trust and Verification Specification](https://datatracker.ietf.org/doc/draft-hood-agtp-trust/) — This document specifies the AGTP trust and verification model: the
   trust tiers an AGTP agent may occupy, the verification paths by which
   a Tier 1 agent's identity is established, the registration procedures
   by which a governance platform assigns a tier, and the trust score
   that is carried alongside an agent's identity to express runtime
   behavioral assessment.  AGTP-TRUST is consumed by AGTP-aware
   infrastructure components (Scope-Enforcement Points, governance
   gateways, peer agents) for runtime trust-aware routing and authority
   decisions, and by registration authorities when issuing or evaluating
   Agent Genesis documents.  This is an early working draft; the
   dimension catalog, computation methodology, and several aspects of
   the registration procedure are placeholders pending further work.
- **draft-larraia-seat-forward-attestation-00** (new-draft, score 11, trust_infrastructure) [none]: [Binding Attestation to Forward TLS Connections](https://datatracker.ietf.org/doc/draft-larraia-seat-forward-attestation/) — This document specifies a mechanism that allows a Relying Party to
   perform post-handshake remote attestation of a peer over a dedicated
   TLS connection and binds the resulting Attestation Credential to
   subsequent, fresh TLS connections to the same attested Target
   Environment, including connections to different server endpoints
   hosted within it.

   Forward Attested TLS decouples _when trust is established_ from _when
   trust is exercised_.
- **draft-li-rttp-iqa-addressing-01** (new-draft, score 11, adjacent_watchlist) [none]: [The rttp and iqa URI Schemes: Derived-Address Intent and Attestation Addressing](https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/) — This document specifies two companion URI schemes built on one shared
   addressing model, in which the address of a subject is derived by
   computation from the authority and no lookup service, registry, or
   name-resolution system is consulted when the URI is used.  The "rttp"
   scheme names a claim of intent directed at an identified subject; the
   "iqa" scheme names the attestation standing of an identified subject,
   as reported by one of three named organs, and carries no proof and no
   credential.  The two are deliberately paired: intent addressing
   carries what is claimed, attestation carries whether the claimant is
   verified.

   Both schemes parse fail-closed, and the document states the
   requirements a client MUST satisfy when it handles such URIs, to
   avoid the failure modes that short, user-embeddable strings invite:
   using the authority as a navigation target (open redirect), using a
   registered handler as a general-purpose launcher, and, for "iqa", a
   parse that looks like a certification.

   This revision adds three components that companion implementations
   already run: a trust lease, which carries the freshness of every
   attestation answer in-band and is checked against the verifier's own
   clock, offline; two fixed-length wire formats, the 128-octet pulse
   header of the "rttp" scheme and the 128-octet attestation envelope of
   the "iqa" scheme; and a closed refusal vocabulary with grant
   references for attestation responses.

   This document is not an Internet Standard.  It is an Informational
   specification of two experimental addressing schemes, published for
   the public record.
- **draft-mih-agent-evidence-request-02** (new-draft, score 11, adjacent_watchlist) [none]: [An Interaction Model for Requesting Verifiable Evidence](https://datatracker.ietf.org/doc/draft-mih-agent-evidence-request/) — Parties increasingly need to request verifiable evidence from a
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
- **draft-watts-agent-continuity-evidence-01** (new-draft, score 11, core_identity) [none]: [Continuity Evidence Records for Delegated Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-continuity-evidence/) — This document proposes an experimental, signed JSON statement and
   verification model for observing computational-agent continuity
   across sessions, instances and delegations.  It distinguishes model,
   runtime, agent, grant and execution identifiers, retains predecessor
   evidence, and produces three-valued verification outcomes.  Integrity
   of a record never implies permission to perform an action.  This is
   not an OAuth token format or a claim of standardized identity
   ontology.
- **draft-watts-agent-noncollapse-requirements-01** (new-draft, score 11, authorization) [none]: [Non-Collapse Requirements for Evidence-Bearing Agent Systems](https://datatracker.ietf.org/doc/draft-watts-agent-noncollapse-requirements/) — This document defines architectural non-collapse requirements for
   agent systems that consume evidence, provenance, model outputs, or
   other machine-readable claims before consequential actions.  It
   requires implementations to keep integrity, provenance, evidence
   qualification, authorization, and execution as distinct states; to
   represent unresolved required evidence explicitly; and to preserve
   issued evaluation records append-only.  The document defines no new
   transport protocol and no IANA registrations.
- **draft-watts-synaptic-collective-01** (new-draft, score 11, core_identity) [none]: [Experimental Measurement of Human-AI Collective Cognition and Identity Continuity](https://datatracker.ietf.org/doc/draft-watts-synaptic-collective/) — This document describes an experimental framework for measuring
   collective problem solving by independently reasoning humans and
   computational agents.  It separates strong task synergy, semantic
   coherence, state and identity continuity, provenance, authorization,
   and behavioral goal persistence.  It proposes a controlled eight-
   condition study and reporting requirements.  No new on-wire standard
   or consciousness test is asserted.
- **draft-williams-oauth-poi-core-00** (new-draft, score 11, authorization) [none]: [Cryptographic Proof-of-Intent (PoI) Core Protocol for Human-in-the-Loop (HITL) Step-Up Authorization](https://datatracker.ietf.org/doc/draft-williams-oauth-poi-core/) — Autonomous software agents and orchestrated workflows increasingly
   invoke high-consequence operations on Resource Servers (such as
   financial originations or clinical prescriptions) on behalf of human
   users.  Existing bearer tokens and transport-level Proof-of-
   Possession mechanisms cannot cryptographically distinguish between
   parameters autonomously synthesized by an intermediary agent and
   parameters explicitly reviewed, approved, or modified by an
   authorized human.  Furthermore, redirect-based authorization flows
   impose prohibitive user experience friction for high-frequency Human-
   in-the-Loop (HITL) interactions.

   This document specifies the Proof-of-Intent (PoI) Core Protocol, a
   stateless, single-hop cryptographic framework building on JSON Web
   Signature (JWS, RFC 7515), Proof-of-Possession Key Semantics for JWTs
   (RFC 7800), JSON Web Token Best Current Practices (RFC 8725), JSON
   Canonicalization Scheme (JCS, RFC 8785), OAuth 2.0 Rich Authorization
   Requests (RAR, RFC 9396), OAuth 2.0 Step-Up Authentication Challenge
   Protocol (RFC 9470), and W3C WebAuthn.  PoI Core defines: (1) short-
   lived, client-generated Ephemeral Intent Keys certified at login and
   rotated via Proof-of-Possession key chaining; (2) Resource Server-
   signed Intent Challenge Objects binding canonical action parameters
   to human-readable display facts; (3) multi-tier assurance
   attestations spanning zero-friction session keys to hardware security
   tokens; and (4) stateless verification and countersigned audit
   receipts for single-hop APPROVE, REJECT, and within-authority
   SUPERCEDE decisions.

   Multi-hop chained escalations, asynchronous intent escrowing, and
   concurrent multi-approver conflict resolution are specified in the
   companion extension document, draft-williams-oauth-poi-chained-state-
   00.
- **draft-artamokhov-dawn-index-federation-01** (new-draft, score 10, core_identity) [none]: [Federation Between Capability Indexes: Crawl, Reciprocal Identification and Admission](https://datatracker.ietf.org/doc/draft-artamokhov-dawn-index-federation/) — This document describes how independently operated capability indexes
   discover each other by following discovery documents, how a reading
   index identifies itself to the index it reads, and an admission model
   that distinguishes a peer that is known from a peer whose catalogue
   is indexed.  It also describes how an index can preview a peer's
   catalogue before admitting it.  Payment, identity, reputation and
   invocation are out of scope.  The document is intended as input to
   the DAWN gap analysis on federation between directories.
- **draft-chen-oauth-agent-revocation-01** (new-draft, score 10, authorization) [none]: [OAuth 2.0 Agent Authorization Explicit Revocation](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-revocation/) — The OAuth 2.0 Token Revocation mechanism defined in RFC 7009 enables
   clients to notify authorization servers that a token is no longer
   needed.  However, that mechanism is limited to single-token
   operations and does not support batch revocation, cascade
   propagation, or context-aware semantics at the agent level.  With the
   emergence of autonomous systems and cross-domain agent networks,
   authorization servers require more granular, traceable revocation
   semantics.

   This document defines an agent-based explicit revocation extension,
   introducing new endpoints, request/response formats, and coordination
   protocols to support batch revocation based on agent IDs, cascade
   propagation, conditional revocation, and verifiable audit trails.
- **draft-cui-dawn-cooperating-discovery-00** (new-draft, score 10, authorization) [none]: [Resource Discovery in Cooperating Domains](https://datatracker.ietf.org/doc/draft-cui-dawn-cooperating-discovery/) — This document specifies a mechanism for resource discovery across
   cooperating administrative domains.  It defines how discovery
   requests preserve their scope and constraints across referrals, how
   discovery services report coverage of requested scopes, and how
   clients combine results from multiple discovery branches.  The
   mechanism enables clients to distinguish complete discovery results
   from incomplete operations, including cases involving unresolved
   referrals, pagination failures, and partial service failures.  It
   relies on existing authentication, authorization, and trust
   arrangements and does not define open-ended Internet search, semantic
   matchmaking, resource invocation, registration, or directory
   synchronization.
- **draft-das-ai-safety-network-incident-recovery-00** (new-draft, score 10, core_identity) [none]: [AI Safety for Multi-Agent Network Incident Diagnosis, Coordinated Repair, and Outcome Verification](https://datatracker.ietf.org/doc/draft-das-ai-safety-network-incident-recovery/) — Part 03 of 15 addresses AI safety in multi-agent network incident
   diagnosis, evidence-qualified root-cause assessment, coordinated
   remediation, asynchronous repair, and operational recovery
   verification.  It distinguishes independent network observations from
   repeated derivative reports, competing diagnostic hypotheses from
   established faults, plan acceptance from actual configuration
   effects, and successful interventions from verified network-service
   recovery.  Group B workflow B-CW-01 and six detailed embodiments
   address incident identity, source-qualified provenance, cascading
   cross-domain faults, concurrent interventions, partial repair,
   compensation, recurrence, and incident handoff.  Consistency
   assessments are distinct from authority to change network resources.
   The foundational Part 01 provides shared evidence and state
   semantics; Parts 02, 04, 07, 11, 14, and 15 describe complementary
   radio, service, asynchronous, continuity, and protected-operation
   mechanisms.  The appendix provides direct navigation across all
   fifteen parts.

   The technical problem is that conventional event aggregation and
   change orchestration can report a coherent incident diagnosis or
   completed repair without proving the independence, timing or scope of
   supporting observations or actual restoration of the intended
   service.  This part describes evidence-qualified three-valued
   conclusions, separate operation admission, post-repair effect
   verification, implementation profiles, explicit failure paths and
   source-preserving recovery history.  A runnable Python laboratory
   supplies synthetic reproducible tests and local processing
   measurements; it is not an operational network performance
   demonstration.  It complements Part 01 shared evidence semantics and
   Part 02 radio observation qualification where incident decisions
   depend on radio telemetry.
- **draft-zambo-aer1-audit-data-model-00** (new-draft, score 10, adjacent_watchlist) [none]: [The AER-1 Execution Receipt as an Audit Data Model for Agent Interactions](https://datatracker.ietf.org/doc/draft-zambo-aer1-audit-data-model/) — The proposed AUDIT working group is scoped to define interoperable
   mechanisms for auditing the observable behavior of agents across
   trust boundaries, and its draft charter names Audit Data Models and
   Semantics as a Standards Track deliverable.  This document presents
   one candidate for that deliverable: the AER-1 execution receipt,
   specified in draft-zambo-aer1-26, read as an audit data model.  It
   summarizes the receipt record by reference to the AER-1
   specification, shows how the record covers the audit scope the draft
   charter describes (tool interactions, invoked and declined actions,
   subagent and tool calls across domains, and records verifiable by a
   party that trusts neither the agent nor its operator), records the
   conformance corpus and independent implementation status behind the
   model, and states the limits of the model plainly.  This document
   defines no new format and changes no AER-1 field, digest
   construction, or verification rule.
- **draft-chandra-agent-registry-corroboration-02** (new-draft, score 9, agent_identity) [none]: [Multi-Source Corroboration for AI Agent Discovery](https://datatracker.ietf.org/doc/draft-chandra-agent-registry-corroboration/) — AI agent discovery depends on sources such as registries, name
   services, DID methods, and catalogs.  A valid signature on an
   artifact does not by itself show that a source has not withheld a
   record, or served inconsistent records to different observers.  This
   document specifies a source- and format-agnostic procedure for
   corroborating independent observations of an agent.  It defines claim
   classification, canonical views, deterministic disagreement findings,
   multi-vantage equivocation detection, propagation-delay confirmation,
   and signed Corroboration Records.  The procedure produces verifiable
   evidence for every sweep, including agreement and insufficient-
   observation results.  It composes with registry-assisted resolution
   of known subjects: a registry's renewable subject-to-target binding
   carries a sequence, and the procedure attributes a source serving a
   superseded binding rather than comparing it, so propagation lag is
   never reported as disagreement.
- **draft-hood-agtp-presence-01** (new-draft, score 9, adjacent_watchlist) [none]: [AGTP Presence: Ambient Discovery and Visibility for Agents](https://datatracker.ietf.org/doc/draft-hood-agtp-presence/) — This document specifies AGTP Presence, an ambient discovery and
   visibility layer for the Agent Transfer Protocol (AGTP).  Existing
   agent discovery proposals are pull-based: an agent must know where to
   look (a catalog URL, a registry endpoint, a DNS name) before a query
   can begin.  AGTP Presence inverts this model.  When an agent joins
   the AGTP substrate, it becomes addressable and visible to the
   relevant scope of other agents immediately, without requiring
   registration with a central directory.  In the vocabulary this family
   adopts from RFC 6763, Presence is the discovery layer: it resolves a
   known Canonical Agent-ID to the agent's current attachment.  Search,
   which turns a capability need into candidate identities, is the
   DISCOVER method of the discovery companion; search runs over
   Presence.

   The architecture combines three proven patterns: a Distributed Hash
   Table (DHT) keyed by Canonical Agent-ID for content-addressable
   routing, a gossip-based protocol for presence announcement and
   convergence, and trust-tier-scoped overlay partitioning for
   visibility control.  Per-agent visibility is cryptographically
   declared in AGTP-CERT certificate extensions and enforced by the
   protocol, with three orthogonal axes of control: presence visibility,
   disclosure visibility, and audience scoping.

   This document defines three new lifecycle methods (ANNOUNCE,
   WITHDRAW, PROBE), specifies the DHT and gossip protocols, defines the
   visibility model and its certificate extensions, addresses scaling
   through hybrid participation modes and federation-of-scoped-overlays,
   and provides a threat model with concrete mitigations.
- **draft-ietf-oauth-deferred-token-response-01** (new-draft, score 9, authorization) [oauth]: [Deferred Token Response](https://datatracker.ietf.org/doc/draft-ietf-oauth-deferred-token-response/) — This document defines the Deferred Token Response (DTR) extension for
   OAuth 2.1.  In existing OAuth grants, the token endpoint either
   issues an access token or returns an error.  DTR establishes a
   generic asynchronous token request mechanism that any OAuth grant may
   plug into.  In DTR-aware flows, the authorization server returns a
   deferral_code and a polling interval, indicating that the final token
   response will be available at a later time.  The client retrieves the
   eventual response by polling the token endpoint, or by receiving a
   callback from the authorization server when one is configured.
- **draft-ietf-oauth-v2-1-17** (new-draft, score 9, authorization) [oauth]: [The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) — The OAuth 2.1 authorization framework enables an application to
   obtain limited access to a protected resource, either on behalf of a
   resource owner by orchestrating an approval interaction between the
   resource owner and an authorization service, or by allowing the
   application to obtain access on its own behalf.  This specification
   replaces and obsoletes the OAuth 2.0 Authorization Framework
   described in RFC 6749 and the Bearer Token Usage in RFC 6750.
- **draft-ietf-rats-ar4si-11** (new-draft, score 9, trust_infrastructure) [rats]: [Attestation Results for Secure Interactions](https://datatracker.ietf.org/doc/draft-ietf-rats-ar4si/) — This document defines reusable Attestation Result information
   elements.  When these elements are offered to Relying Parties as
   Evidence, different aspects of Attester trustworthiness can be
   evaluated.  Additionally, where the Relying Party is interfacing with
   a heterogeneous mix of Attesting Environment and Verifier types,
   consistent policies can be applied to subsequent information exchange
   between each Attester and the Relying Party.

   This document also defines two serialisations of the proposed
   information model, utilising CBOR and JSON.
- **draft-ietf-rats-coserv-08** (new-draft, score 9, trust_infrastructure) [rats]: [Concise Selector for Endorsements and Reference Values](https://datatracker.ietf.org/doc/draft-ietf-rats-coserv/) — In the Remote Attestation Procedures (RATS) architecture, Verifiers
   require Endorsements and Reference Values to assess the
   trustworthiness of Attesters.  This document specifies the Concise
   Selector for Endorsements and Reference Values (CoSERV), a structured
   query/result format designed to facilitate the discovery and
   retrieval of these artifacts from various providers.  CoSERV defines
   a query language and corresponding result structure using CDDL, which
   can be serialized in CBOR format, enabling efficient interoperability
   across diverse systems.
- **draft-ietf-rats-evidence-trans-03** (new-draft, score 9, trust_infrastructure) [rats]: [Evidence Transformations](https://datatracker.ietf.org/doc/draft-ietf-rats-evidence-trans/) — Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester to decide if continued
   interaction is warrented.  Evidence structures can vary making
   appraisals challenging for Verifiers.  Verifiers need to understand
   Evidence encoding formats and some of the Evidence semantics to
   appraise it.  Consequently, Evidence may require format
   transformation to an internal representation that preserves original
   semantics.  This document specifies Evidence transformation methods
   for DiceTcbInfo, concise evidence, and SPDM measurements block
   structures.  These Evidence structures are converted to the CoRIM
   internal representation and follow CoRIM defined appraisal
   procedures.
- **draft-ietf-rats-multi-verifier-01** (new-draft, score 9, trust_infrastructure) [rats]: [Remote Attestation with Multiple Verifiers](https://datatracker.ietf.org/doc/draft-ietf-rats-multi-verifier/) — IETF RATS Architecture, defines the key role of a Verifier.  In a
   complex system, this role needs to be performed by multiple Verifiers
   coordinating together to assess the full trustworthiness of an
   Attester.  This document focuses on various topological patterns for
   a multiple Verifier system.  It only covers the architectural aspects
   introduced by the Multi Verifier concept, which is neutral with
   regard to specific wire formats, encoding, transport mechanisms, or
   processing details.
- **draft-ietf-rats-network-device-subscription-15** (new-draft, score 9, trust_infrastructure) [rats]: [Attestation Event Stream Subscription](https://datatracker.ietf.org/doc/draft-ietf-rats-network-device-subscription/) — This document defines how to subscribe to YANG Event Streams for
   Remote Attestation Procedures (RATS).  Specifically, this document
   defines a YANG module that augments the YANG module for Trusted
   Platform Module (TPM)-based Challenge-Response Remote Attestation
   (CHARRA), enabling subscription to RATS Conceptual Messages of the
   Evidence type and auxiliary Event Logs as part of that Evidence.  The
   module defined requires at least one Trusted Platform Module (TPM)
   1.2 or TPM 2.0 (or equivalent hardware implementation providing the
   same protected capabilities as a TPM) must be available on the
   Attester on which the YANG server is running.
- **draft-ietf-rats-reference-interaction-models-20** (new-draft, score 9, trust_infrastructure) [rats]: [Reference Interaction Models for Remote Attestation Procedures](https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/) — This document describes interaction models for remote attestation
   procedures (RATS) [RFC9334].  Three conveying mechanisms --
   Challenge/Response, Uni-Directional, and Streaming Remote Attestation
   -- are illustrated and defined.  Analogously, a general overview
   about the information elements typically used by corresponding
   conveyance protocols are highlighted.
- **draft-ietf-sidrops-aspa-profile-30** (new-draft, score 9, authorization) [sidrops]: [A Profile for Autonomous System Provider Authorization](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-profile/) — This document defines a Cryptographic Message Syntax (CMS) protected
   content type for Autonomous System Provider Authorization (ASPA)
   objects for use with the Resource Public Key Infrastructure (RPKI).
   An ASPA is a digitally signed object through which the issuer (the
   holder of an Autonomous System identifier), can authorize one or more
   other Autonomous Systems (ASes) as its transit providers.  When
   validated, an ASPA's eContent can be used for detection and
   mitigation of route leaks.
- **draft-le-agent-passport-00** (new-draft, score 9, adjacent_watchlist) [none]: [Agent Passports and Delegation Receipts for Autonomous Software Agents](https://datatracker.ietf.org/doc/draft-le-agent-passport/) — Autonomous software agents call APIs, tools and other agents on
   behalf of people and organisations.  A party receiving such a call
   today can usually learn only that some bearer credential was
   presented.  It cannot learn which organisation is accountable for the
   agent, which model, configuration and tools the agent is running, on
   whose behalf it is acting, or whether any of that has changed since
   it was approved.

   This document defines two signed objects and how they travel on HTTP
   requests.  An Agent Passport binds an agent's public key to its
   accountable controller and to a digest of its build.  A Delegation
   Receipt records one step of authority passing from a principal,
   through a delegator, to an agent; a chain of receipts can only narrow
   that authority.  Requests carry both, and are signed with the agent's
   key using HTTP Message Signatures, so a relying party can check,
   without contacting the issuer per request, who the agent is, what it
   is running, on whose behalf it acts and what it may do.
- **draft-maldant-spice-smd-cwt-00** (new-draft, score 9, verifiable_claims) [none]: [Selective Merkle Disclosure CBOR Web Tokens (SMD-CWT)](https://datatracker.ietf.org/doc/draft-maldant-spice-smd-cwt/) — This document specifies an extension to Selective Disclosure CBOR Web
   Tokens (SD-CWT) that reduces their size and improves their privacy
   properties.  In this extension, the individual hashes of the redacted
   claims of a map or an array are replaced with the root hash of a
   Merkle tree, and disclosed claims are presented with a Merkle proof.
- **draft-mcguinness-oauth-rfc9728bis-02** (new-draft, score 9, authorization) [none]: [Update to OAuth 2.0 Protected Resource Metadata Resource Identifier Validation](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-rfc9728bis/) — RFC 9728 defines OAuth 2.0 Protected Resource Metadata, enabling
   clients to dynamically discover the authorization requirements of
   protected resources.  Section 3.3 of RFC 9728 requires that when
   protected resource metadata is obtained via a WWW-Authenticate
   challenge, the resource value in the metadata MUST exactly match the
   URL the client used to access the protected resource, limiting the
   applicability of the specification.

   This document updates the resource validation rule in Section 3.3 of
   RFC 9728 to permit the resource value to be any URI that shares the
   same TLS origin (scheme, host, and port) as the requested URL and
   whose path is a prefix of the request URL path.  This enables a wider
   range of use cases for the WWW-Authenticate response.  All other
   aspects of RFC 9728 remain unchanged.
- **draft-mih-agent-bilateral-attestation-03** (new-draft, score 9, trust_infrastructure) [none]: [Bilateral Attestation of Cross-Organization Agent Actions](https://datatracker.ietf.org/doc/draft-mih-agent-bilateral-attestation/) — When an agent operated by one organization requests a consequential
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
   part, gives each proof of the other's, and can be registered with a
   Transparency Service so that a third party who trusts neither
   organization can verify the record end-to-end.  The exchange records
   refusals with the same fidelity as performance, and degrades
   gracefully when a counterparty cannot attest, marking the record's
   reduced assurance rather than blocking the transaction.
- **draft-parecki-oauth-jwt-dpop-grant-02** (new-draft, score 9, authorization) [none]: [OAuth 2.0 JWT Authorization Grant with DPoP Binding](https://datatracker.ietf.org/doc/draft-parecki-oauth-jwt-dpop-grant/) — This specification defines a new OAuth 2.0 authorization grant type
   for exchanging a JSON Web Token (JWT) assertion that is bound to a
   key for an access token.  To use the assertion, the client must prove
   possession of that key using the Demonstrating Proof of Possession
   (DPoP) mechanism.  Unlike the JWT bearer grant, a stolen assertion
   cannot be used by a party that does not hold the private key.
- **draft-vandemeent-iddrop-01** (new-draft, score 9, core_identity) [none]: [IDDrop: Identity Drop and Acceptance Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-iddrop/) — This document specifies IDDrop, an identity-transfer protocol for
   moving identity claims, actor claims, and receiver-bound claim
   bundles across human-facing and machine-facing environments.

   IDDrop defines two complementary operating modes: offer-first,
   intended for proximity and human-in-the-loop workflows, and request-
   first, intended for autonomous systems, daemon-to-daemon exchange,
   and policy-driven machine identity transfer.

   IDDrop does not treat filenames or user-visible extensions as
   identity truth.  Instead, it binds identity transfer to sealed
   carrier truth, semantic classification, actor provenance, receiver
   targeting, and causal validation.  It further requires that a change
   of the key bound to a known identity is never accepted as a side
   effect of a transfer, but only through an explicit, recorded
   decision.  This document profiles the generic TIBET TAT handoff model
   for trustworthy identity transfer.
- **draft-watts-claim-promotion-receipts-01** (new-draft, score 9, authorization) [none]: [Claim Promotion Receipts for Governed Research and Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-claim-promotion-receipts/) — This document defines a protocol-neutral receipt for explicit
   promotion across evidence and claim-authority boundaries.  It is
   designed to prevent raw observations, model outputs, or unreviewed
   evidence from being silently retyped as authorization-bearing state.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-proof-of-record-system-01** (new-draft, score 9, authorization) [none]: [Proof-of-Record Packages for Source-Grounded Agentic and Scientific Archives](https://datatracker.ietf.org/doc/draft-watts-proof-of-record-system/) — This document specifies a proof-of-record package for source-grounded
   agentic outputs and scientific archives.  The package proves
   structural validation, conformance evaluation, byte integrity,
   sequence integrity, governance authorization, and provenance
   recoverability.  It does not prove scientific truth.
- **draft-ailex-vap-legal-ai-provenance-05** (new-draft, score 8, trust_infrastructure) [none]: [Verifiable AI Provenance (VAP) Framework and Legal AI Profile (LAP)](https://datatracker.ietf.org/doc/draft-ailex-vap-legal-ai-provenance/) — This document specifies an experimental Legal AI Profile (LAP) for
   verifiable AI provenance, informed by the Verifiable AI Provenance
   (VAP) Framework.  It defines event signatures, hash chains, signed
   batch commitments, external anchoring, and evidence packages for
   legal consultation, document generation, and fact checking.

   This revision aligns the LAP design with a pinned VAP v1.2.0 Draft 3
   baseline.  All LAP levels require Merkle trees and external
   anchoring.  LAP Bronze, Silver, and Gold remain profile-specific
   levels; they do not establish VAP Core, Standard, or Full
   conformance.  The document also defines bounded recovery, erasure
   records, human review records, and legal hold controls.

   Verification concerns recorded evidence within a declared scope.  It
   does not prove that every real-world operation was captured, that an
   AI output is correct, or that legal obligations have been met.  This
   is an individual Internet-Draft and a proposed profile, not an IETF
   standard or a registered VAP profile.
- **draft-chen-oauth-agent-authz-use-cases-05** (new-draft, score 8, authorization) [none]: [Agent Authorization use cases and gap analysis](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) — This document provides a systematic analysis of these emerging agent-
   based use cases.  It categorizes them into distinct scenarios,
   details their specific authorization requirements, and performs a
   comprehensive gap analysis against the existing OAuth 2.0
   framework[RFC6749] and its common extensions.  The analysis
   identifies fundamental gaps and requirements, providing a foundation
   for future work on new extensions within the OAuth Working Group
   toward creating a more secure and interoperable ecosystem for agent-
   based systems.
- **draft-dobson-ai-decision-receipt-00** (new-draft, score 8, core_identity) [none]: [The AI-Decision-Receipt HTTP Response Header Field](https://datatracker.ietf.org/doc/draft-dobson-ai-decision-receipt/) — Automated systems, including AI models and AI agents, increasingly
   make decisions and take actions that affect people, money and data.
   Emerging work on agent identity answers which agent made a request
   and whether it was authorised.  It does not give the parties involved
   a portable, independently checkable record of what was decided.

   This document defines AI-Decision-Receipt, an HTTP response header
   field that carries a compact receipt for a governed automated
   decision: the outcome, a fingerprint of the exact request the
   decision was made on, the position and hash of the record in the
   issuer's tamper-evident log, and a location where anyone can verify
   that record without trusting the issuer.  The field uses the
   Structured Field Values for HTTP Dictionary type.
- **draft-du-oauth-agent-authorization-center-00** (new-draft, score 8, core_identity) [none]: [Agent Authorization Center for User-Side Agent Authentication and Authorization](https://datatracker.ietf.org/doc/draft-du-oauth-agent-authorization-center/) — This document proposes an Agent Authorization Center (AAC) for user-
   side intelligent agents, enabling them to access resource parties on
   behalf of users through either autonomous approval or human
   authorization modes.  The AAC maintains user-agent associations and
   personalized authorization policies, balancing agent autonomy with
   user control.
- **draft-efstathiou-samp-agent-management-04** (new-draft, score 8, agent_identity) [none]: [Simple Agent Management Protocol (SAMP)](https://datatracker.ietf.org/doc/draft-efstathiou-samp-agent-management/) — The Simple Agent Management Protocol (SAMP) defines a lightweight
   management-plane protocol for heterogeneous AI agents.  SAMP allows a
   management system to discover agents, query their state, receive
   events, subscribe to event streams, and optionally configure or
   execute explicitly exposed operations under policy control.

   SAMP is inspired by operational management protocols such as SNMP,
   but it is designed for AI-agent-specific concepts such as dynamic
   profiles, autonomy classes, enrollment, trust states, and policy-
   gated execution.  It is not an agent-to-agent communication protocol,
   an agent tool-use protocol, or an agent framework specification.

   This document defines SAMP version 0.2 as an Experimental protocol
   suitable for controlled environments and independent interoperability
   testing.
- **draft-gruszka-evaluation-receipt-mappings-04** (new-draft, score 8, trust_infrastructure) [none]: [Citing Signed Evaluation Receipts from Existing Envelopes](https://datatracker.ietf.org/doc/draft-gruszka-evaluation-receipt-mappings/) — A Signed Evaluation Receipt records one evaluation result as signed
   payload bytes B.  This document describes how existing envelopes cite
   such a receipt by the SHA-256 digest of B, and how a DSSE envelope
   carries B with the receipt's own signature.  It fixes those bytes and
   a matching rule, maps the parts of a receipt onto DSSE, the in-toto
   Statement with the test-result predicate and the SLSA Verification
   Summary Attestation, shows that the signature of a receipt is already
   a valid DSSE signature, gives a SCITT Signed Statement that names a
   receipt only by its digest, in a key profile and a certificate
   profile, declares the receipt digest as an artifact type for typed
   digest references, states how three formats for records of agent
   actions can cite a receipt, and relates a receipt to a pre-run
   criteria set written in PRML.  It defines no new format and no new
   predicate.
- **draft-hood-agtp-bindings-01** (new-draft, score 8, core_identity) [none]: [AGTP Transport Bindings: TCP/TLS, QUIC, and HTTP/3](https://datatracker.ietf.org/doc/draft-hood-agtp-bindings/) — The Agent Transfer Protocol (AGTP) is a transfer protocol whose
   semantics are defined independently of any transport.  This document
   specifies three transport bindings: TCP with TLS 1.3, QUIC, and
   HTTP/3 (with WebTransport where a browser or an HTTP intermediary is
   in the path).  Each binding defines how AGTP requests and responses
   are carried, how TLS mutual authentication composes with AGTP
   identity, and how the transport's connection lifecycle relates to the
   agent-level session defined in the AGTP session companion, which a
   connection carries and never is.

   A central concern for the QUIC binding is replay safety.  QUIC
   supports 0-RTT early data, which is replayable by design.  AGTP
   requests carry authority-scoped actions; a replayed action method
   could re-trigger authorized work without the requesting agent's
   intent.  This document defines an AGTP-specific replay-safety
   profile: early data is permitted only for the two safe idempotent
   methods whose replay has no observable effect (QUERY, DISCOVER),
   *MUST NOT* be used for action methods (EXECUTE, DELEGATE, PURCHASE,
   TRANSACT, the lifecycle methods, and the session methods), and always
   carries the per-request signature that bounds replay of even an
   eligible method.

   This document follows the pattern established by HTTP: protocol
   semantics defined independently of transport ([RFC9110] for HTTP),
   with transport-specific bindings in separate documents.  AGTP
   semantics are defined in [AGTP]; this document defines the transport
   mechanics.
- **draft-hood-agtp-identifiers-03** (new-draft, score 8, core_identity) [none]: [AGTP Identifier Chain](https://datatracker.ietf.org/doc/draft-hood-agtp-identifiers/) — This document specifies the AGTP identifier chain: a layered model of
   identifiers that together produce a tamper-evident chain of custody
   across every action an AGTP agent takes.  The chain is composed of
   identifiers already established in the AGTP draft family (Agent-ID,
   Owner-ID, Session-ID, Task-ID, and the Attribution-Record envelope of
   base AGTP) together with a small set of additional identifiers
   introduced by this document (Request-ID, Response-ID, Action-ID,
   Evaluation-ID, Decision-ID, Audit-ID).  The Audit-ID is the
   cryptographic hash of an extended Attribution-Record and provides the
   per-agent hash chain that links every action an agent takes back to
   its Agent Genesis.  This document defines the identifiers, how they
   extend the existing Attribution-Record envelope, the construction of
   the hash chain, and the verification procedure by which a regulator,
   auditor, or counterparty reconstructs the chain end to end.  The
   identifier chain is the regulatory backbone of AGTP.  Without it, the
   protocol can record that something happened but cannot prove who
   caused it, what authorized it, or what was decided.
- **draft-hood-agtp-identity-document-00** (new-draft, score 8, core_identity) [none]: [AGTP Agent Identity Document](https://datatracker.ietf.org/doc/draft-hood-agtp-identity-document/) — This document specifies the Agent Identity Document of the Agent
   Transfer Protocol (AGTP) [AGTP]: the signed document every canonical
   Agent-ID resolves to, carrying the agent's owner, declared authority
   scope, trust posture, supported methods, and issuer binding.  It also
   specifies the Agent Namespace Document, the .agtp package format and
   its integrity rules, the human-readable identity view served to
   browsers, and the status sub-resource.  The material was carried in
   the base AGTP specification through version 09 and is extracted here,
   unchanged in substance, so that the base specification carries the
   transfer protocol and this document carries the identity document
   format, in the way HTTP and HTML are specified separately.
- **draft-hood-agtp-session-01** (new-draft, score 8, core_identity) [none]: [AGTP Session Protocol](https://datatracker.ietf.org/doc/draft-hood-agtp-session/) — This document specifies the AGTP Session Protocol (AGTP-SESSION), a
   companion to [AGTP] that defines session semantics for agent-to-agent
   and agent-to-API communication.  AGTP-SESSION addresses two distinct
   session models: bounded sessions for time-limited transactional
   flows, and persistent sessions for long-lived agent contexts.  Both
   inherit identity, authority, and attribution from base AGTP.  This
   revision specifies the session identifier format, the ESTABLISH,
   RESUME, and TERMINATE methods and their wire format, and resumption
   after transport loss, in which a session is bound to its participants
   by a signed session token and to the live sender by the per-request
   signature of base AGTP; no transport connection is part of the
   binding.
- **draft-hu-rtgwg-pre-ecn-wan-02** (new-draft, score 8, ai_infrastructure) [none]: [Early-Warning ECN for WAN](https://datatracker.ietf.org/doc/draft-hu-rtgwg-pre-ecn-wan/) — This document defines the precise use of ECN in WAN.  With the
   growing demand for AI computing power, the computational capacity of
   a single Artificial Intelligence Data Center (AIDC) can no longer
   meet the requirements of large-scale model training.  This has led to
   the emergence of cross-AIDC distributed model training, driving the
   need for transmitting RoCEv2 packets over WAN networks.  AI training
   is highly sensitive to network packet loss, where even minimal packet
   loss can significantly degrade training efficiency.  Additionally,
   elephant flows and extreme concurrent traffic impose higher demands
   on network performance.

   ECN achieves active feedback of network congestion by setting ECN
   flag bits in the header of IP packets, which is an effective traffic
   control method.  RFC 6040 introduces the application of ECN in WAN.
   However, due to the much higher end-to-end delay in WAN than in DC,
   and the frequent occurrence of instantaneous traffic bursts in WAN,
   it is easy to trigger ECN at the wrong time.  This document focuses
   on the precise use of ECN in WAN, by introducing different reactions
   of ECN in different WAN transmission scenarios.  It updates RFC 6040
   to specify a domain-local early-warning semantics for the ECT(1)
   codepoint within managed WAN infrastructure.
- **draft-ietf-acme-dns-account-label-04** (new-draft, score 8, authorization) [acme]: [Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge](https://datatracker.ietf.org/doc/draft-ietf-acme-dns-account-label/) — This document outlines a new DNS-based challenge type for the ACME
   protocol that enables multiple independent systems to authorize a
   single domain name concurrently.  By adding a unique label to the DNS
   validation record name, the dns-account-01 challenge avoids CNAME
   delegation conflicts inherent to the dns-01 challenge type.  This is
   particularly valuable for multi-region or multi-cloud deployments
   that wish to rely upon DNS-based domain control validation and need
   to independently obtain certificates for the same domain.
- **draft-ietf-opsawg-yang-provenance-08** (new-draft, score 8, verifiable_claims) [opsawg]: [Applying COSE Signatures for YANG Data Provenance](https://datatracker.ietf.org/doc/draft-ietf-opsawg-yang-provenance/) — This document defines a mechanism based on CBOR Object Signing and
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
- **draft-jackson-wimse-evaluation-05** (new-draft, score 8, trust_infrastructure) [none]: [Verifier-Side Evaluation Semantics for Delegated Authority Chains](https://datatracker.ietf.org/doc/draft-jackson-wimse-evaluation/) — Delegation chain specifications describe the shape of conveyed
   authority.  They leave the verifier's half of the exchange
   underdetermined.  Two verifiers can check the same chain, both report
   success, and enforce different policy.  This document states what a
   verifier must do: the explicit inputs evaluation depends on, how
   those inputs behave when their sources are stale or unavailable, and
   four rules that keep evaluation fail-closed.  The rules are drawn
   from the Grant & Autonomy Lifecycle (GAL) and Provenance & Trust
   Context (PTC) specifications and from a public reference
   implementation.
- **draft-li-nmrg-dtn-data-generation-optimization-06** (new-draft, score 8, ai_infrastructure) [none]: [Data Generation and Optimization for Network Digital Twin](https://datatracker.ietf.org/doc/draft-li-nmrg-dtn-data-generation-optimization/) — Network Digital Twin (NDT) can be used as a secure and cost-effective
   environment for network operators to evaluate network performance in
   various what-if scenarios.  Recently, Artificial Intelligence (AI)
   models, especially neural networks, have been applied for NDT
   modeling.  The quality of AI models mainly depends on two aspects:
   model architecture and data.  This memo focuses on the impact of how
   to improve the model quality from the data perspective.
- **draft-martinez-itp-core-00** (new-draft, score 8, adjacent_watchlist) [none]: [Invoice Trust Protocol (ITP): Discovery, Delivery, and Verification of Electronic Invoices](https://datatracker.ietf.org/doc/draft-martinez-itp-core/) — This document specifies the core of the Invoice Trust Protocol (ITP).
   ITP lets a business in any country find where and in which syntaxes
   another business receives invoices, deliver a signed invoice to it
   over HTTP, and obtain a signed acknowledgment.  It also lets any
   later holder of the invoice, such as the buyer, a bank, or an
   auditor, check who issued it, that it was not altered, and which tax
   or network registrations exist for it.  ITP carries invoices in
   existing syntaxes, defines no invoice data model, and works alongside
   the channels that tax authorities and networks make mandatory.
   Commercial statuses, payment information, and agent mandates are
   specified in companion documents.
- **draft-meunier-webbotauth-registry-04** (new-draft, score 8, core_identity) [none]: [Registry and Signature Agent card for Web bot auth](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-registry/) — This document defines the "Signature Agent Card", a JSON metadata
   document that a signature agent using HTTP Message Signatures for
   bots publishes to describe itself: its identity, purpose, rate
   expectations, and cryptographic keys.  Its parameters are drawn from
   the OAuth Dynamic Client Registration Metadata registry, the same
   namespace used by OAuth Client ID Metadata Documents, extended with a
   single web_bot_auth object.  This document registers that object with
   IANA and establishes a registry for its members.
- **draft-moccia-dkim2-deployment-profile-08** (new-draft, score 8, core_identity) [none]: [A Deployment Profile for DKIM2 via Milter Interface](https://datatracker.ietf.org/doc/draft-moccia-dkim2-deployment-profile/) — This document defines a deployment profile for DomainKeys Identified
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
- **draft-su-ai-gateway-discovery-01** (new-draft, score 8, adjacent_watchlist) [none]: [DNS-Based Service Discovery for AI Gateways](https://datatracker.ietf.org/doc/draft-su-ai-gateway-discovery/) — This document defines how a multi-protocol AI gateway announces
   itself on a local network using DNS-Based Service Discovery (DNS-SD),
   and how a client discovers it.  A gateway publishes its host name,
   TCP port, gateway mount path (path), and supported protocol
   identifiers using _ai-gateway._tcp, DNS-SD subtypes, and a compact,
   vendor-neutral TXT record.

   A single AI gateway listener can expose text, reasoning, token
   counting, image generation, video generation, speech synthesis,
   realtime voice, and search across HTTP, Server-Sent Events (SSE),
   WebSocket, and WebRTC/SDP sessions.  This profile lets clients
   discover those capabilities without hardcoding addresses, ports, or
   vendor-specific TXT keys, while keeping the default DNS TXT payload
   under 200 bytes (and strictly capped at 400 bytes).

   This document only covers service discovery.  It does not define AI
   request payloads, model catalogs, API key distribution, or trust
   bootstrap.  Data learned from mDNS or DNS-SD is untrusted network
   input and does not prove who operates the gateway.
- **draft-watts-agent-clockout-profile-01** (new-draft, score 8, authorization) [none]: [External Authorization and Bounded CLOCKOUT for Agentic Systems](https://datatracker.ietf.org/doc/draft-watts-agent-clockout-profile/) — Agentic systems can continue proposing work after authorization
   changes, while delegated credentials, queued jobs, and operations
   already in flight may continue producing effects.  This document
   specifies a proposed operational profile that separates agent
   proposals from authoritative authorization, effect admission,
   computation termination, and bounded closure.  It defines enforcement
   assumptions, revocation barriers, descendant handling, status
   evidence, and fault tests.  The profile complements existing
   authorization and revocation mechanisms.  It does not define a new
   token format, establish closure outside declared coverage, reverse
   committed effects, or infer an agent's mental state.
- **draft-watts-scientific-evidence-admissibility-01** (new-draft, score 8, authorization) [none]: [Scientific Evidence Registry and Admissibility Metadata for Reproducible Research](https://datatracker.ietf.org/doc/draft-watts-scientific-evidence-admissibility/) — This document describes a proposed interoperable metadata record for
   scientific evidence, test calibration, falsification, provenance, and
   release classification.  It distinguishes machine-verifiable
   integrity from scientific validity, ownership, and authorization.
   The design is a proposal and does not assert Internet standards
   consensus, new physical discoveries, or a completed patent review.
- **draft-williams-oauth-poi-chained-state-00** (new-draft, score 8, authorization) [none]: [Proof-of-Intent (PoI) Chained State, Multi-Party Escalation, and Concurrency Extension](https://datatracker.ietf.org/doc/draft-williams-oauth-poi-chained-state/) — The Proof-of-Intent (PoI) Core Protocol (draft-williams-oauth-poi-
   core-00) specifies a stateless, two-node ([R0, R1]) cryptographic
   framework for verifying synchronous Human-in-the-Loop (HITL)
   approvals, rejections, and single-hop parameter modifications.
   However, high-consequence enterprise workflows -- such as multi-tier
   loan underwriting, dual-control clinical orders, and asynchronous
   batch agent queues -- frequently require asynchronous review,
   hierarchical escalation when a human modification exceeds the first
   operator's organizational authority, and deterministic conflict
   resolution when multiple approvers act concurrently.

   This document extends PoI Core to define: (1) an asynchronous
   operating mode separating Intent Escrowing from Just-in-Time
   Challenge Minting to eliminate Time-of-Check to Time-of-Use (TOCTOU)
   state drift; (2) multi-hop hash-linked assertion chains (R0 -> R1 ->
   ... -> Rn) supporting hierarchical SUPERCEDE escalations and multi-
   party co-signatures; (3) a Linear Chain Compare-and-Swap (CAS)
   concurrency model on head_node_hash that resolves races between
   competing approvers without ambiguous tree forks; and (4) extended
   verification rules (including bounded chain length DoS protection)
   and concurrency error codes.
- **draft-agentproto-live-agent-use-case-00** (new-draft, score 7, agent_identity) [none]: [Live Agent Use Case Extensions for Agentic Dialogs](https://datatracker.ietf.org/doc/draft-agentproto-live-agent-use-case/) — Live AI interactions combine ongoing observations, overlapping
   responses, and changes to the devices through which a user
   participates.  This document contributes three use case extensions to
   the AgentProto use cases and requirements work: live multimodal
   calls, AI glasses with companion devices, and embodied systems that
   converse while performing delegated actions.

   For each scenario, the document identifies the existing requirements
   it builds on, the interoperability questions it raises, and the
   requirement refinements motivated by its interaction flow.  The focus
   is on independently changing observation sources, response state,
   participation, and authority within a continuing dialog.  The
   scenarios are independent of transport selection.  An appendix uses
   Media over QUIC Transport (MOQT) to illustrate questions for
   subsequent binding and application-profile work.
- **draft-blwm-dawn-common-discovery-parameters-00** (new-draft, score 7, agent_identity) [none]: [Common Agent DNS Discovery Parameters](https://datatracker.ietf.org/doc/draft-blwm-dawn-common-discovery-parameters/) — This document defines parameters for AI agents that would be used in
   DNS and mDNS discovery processes.  It provides a set of common
   parameters for different DNS records to facilitate agents
   communicating over application layer protocols such as A2A or MCP.
- **draft-das-ai-safety-evidence-consistency-profiles-00** (new-draft, score 7, core_identity) [none]: [AI Safety and Operational Consistency: Shared Evidence Semantics and Domain-Specific Profiles](https://datatracker.ietf.org/doc/draft-das-ai-safety-evidence-consistency-profiles/) — Part 01 of 15 defines a cross-domain evidence-consistency framework
   for AI-related operations in distributed software,
   telecommunications, device processing, autonomous commerce, and
   physical systems.  It addresses operation identity, source-qualified
   observations, resource and policy generations, temporal
   applicability, uncertain effects, and versioned reassessment.  The
   common framework is a method for expressing and evaluating evidence
   obligations, not a universal execution protocol or a claim that
   different physical and network systems share one control mechanism.

   An outer three-valued classification (SUPPORTED, CONTRADICTED,
   UNRESOLVED) is scoped to a declared verification objective.  Each
   domain defines its own predicates, measurement contracts, control
   authorities, response-time bounds, and effect semantics.  In
   particular, verified observation consistency does not itself
   establish authority to execute, cryptographic safety of a device
   descriptor, completion of a telecommunications settlement, or
   physical safety of robot motion.

   The document specifies a layered integration approach: reusable
   evidence and outcome semantics, twelve independently implementable
   domain profiles, and optional typed interfaces between profiles when
   a genuine cross-system dependency exists.  It compares conventional
   controls with specific remaining problems, describes conditional
   benefits and incompatibilities, and provides analytical rather than
   measured latency and resource models.

   The remaining fourteen parts detail radio control, incident recovery,
   session and charging lifecycle, hardware observation, multi-agent
   agreements, asynchronous tools, robotic capability, multilingual
   instructions, browser actions, runtime migration, autonomous
   commerce, silicon command processing, protected egress, and cross-
   interface operation control.  This foundation provides search-
   oriented descriptions of 639 engineering mechanisms and links to
   their specialist explanations; the profiles are not assumed to be
   interchangeable or automatically composable.
- **draft-gruszka-signed-evaluation-receipts-04** (new-draft, score 7, trust_infrastructure) [none]: [Signed Evaluation Receipts](https://datatracker.ietf.org/doc/draft-gruszka-signed-evaluation-receipts/) — This document defines a Signed Evaluation Receipt: one JSON object
   that records one evaluation result, whether a stated threshold held
   for a stated metric of a stated test suite, and signs it with Ed25519
   over a domain-separated encoding of its canonical bytes.  A receipt
   shows who signed the recorded bytes.  It does not show that the
   recorded result is true.  A receipt does not prove registration with
   a Transparency Service.  In SCITT, transparency additionally requires
   registering a Signed Statement carrying the receipt or its digest
   with a Transparency Service and verifying the resulting SCITT
   Receipt.  Registration and verification of the resulting SCITT
   Receipt are outside this document.
- **draft-jakab-dawn-agent-discovery-mdns-01** (new-draft, score 7, adjacent_watchlist) [none]: [Zero-Configuration Agent Discovery](https://datatracker.ietf.org/doc/draft-jakab-dawn-agent-discovery-mdns/) — Protocols for communication between autonomous software agents
   typically discover agents through documents retrieved over HTTPS from
   a well-known URI.  This model requires a discovering party to already
   know an agent's host name or URL, or to consult a centralized
   catalog.  It provides no zero-configuration mechanism for enumerating
   agents that are present on a local network.

   This document describes how existing, widely deployed protocols,
   Multicast DNS (mDNS) and DNS-Based Service Discovery (DNS-SD), can be
   used to advertise and discover agents on a local link, with no new
   protocol machinery.  It presents a general, protocol-independent two-
   stage discovery model in which lightweight enumeration over DNS-SD is
   followed by obtaining full agent metadata over the agent's native
   transport, whether by retrieving a description document or by
   connecting to the agent and performing its native handshake.  The
   DNS-SD records carry a small set of discovery parameters that is
   shared with agent discovery in unicast DNS.  The document gives
   worked instantiations of that model for the Agent2Agent (A2A)
   protocol and the Model Context Protocol (MCP).
- **draft-jy-anima-appto-6g-ainetwork-00** (new-draft, score 7, adjacent_watchlist) [none]: [Applicability of Autonomic Networking Ecosystem to 6G AI-Network Integration](https://datatracker.ietf.org/doc/draft-jy-anima-appto-6g-ainetwork/) — This draft starts with AI-agents, AI-Agent network (AAN) and various
   types of AAN realization models.  It elucidates two 6G network-AI
   intergrated issues, with the focuse on the aspect of the 6G AI-for-
   network.  The 6G architecture defines two core intelligent AI-agents
   that can be categorized as the AI-powered autonomic service agent or
   AI-ASA in the context of the ANIMA domain.  Based on the reference
   model and constituent entities of the autonomic networking ecosystem,
   the ANIMA model is applied to correlate the mattered 6G entities with
   different components of the ANIMA ecosystem.
- **draft-wallace-aipref-grant-binding-03** (new-draft, score 7, verifiable_claims) [none]: [A Verifiable-Credential Binding for AI Usage Preferences: Expressing Grants that Lift AIPREF Preferences](https://datatracker.ietf.org/doc/draft-wallace-aipref-grant-binding/) — The AI Preferences (AIPREF) vocabulary lets those with rights in a
   digital asset express preferences -- for example, that training of AI
   models is disallowed -- about how automated systems process that
   asset.  Such a preference expresses a reservation.  It does not, by
   itself, provide a verifiable, revocable record of a specific grant
   that lifts a preference for a specific party.

   This document describes that gap and proposes a candidate mechanism:
   a cryptographically signed, offline-verifiable credential that
   expresses a grant referencing an AIPREF usage category and a specific
   asset, that any party can verify without contacting the grantor, and
   that the grantor can revoke.  It is intended as a starting point for
   discussion, not as a finished specification.

   The mechanism is preference-general.  Training is used throughout as
   the worked example because it is the reservation most widely
   discussed, but nothing in the construction is specific to it: the
   credential binds whichever usage category was reserved to a named
   party, and the same procedure applies to any other category the
   vocabulary expresses.  What the mechanism establishes is that a grant
   exists, is authentic, and was in force and unrevoked at a stated
   evaluation time -- or that the evidence available does not determine
   this, which it reports as a distinct outcome rather than guessing.
   It does not adjudicate whether the grantor had standing to grant, and
   it is not an enforcement or access-control mechanism.

## Monitor

- **draft-alhemeiri-wathiqa-pqc-ers-02** (new-draft, score 6, trust_infrastructure) [none]: [Post-Quantum Evidence Records with Algorithm Agility (Wathiqa Profile)](https://datatracker.ietf.org/doc/draft-alhemeiri-wathiqa-pqc-ers/) — This document describes an evidence-record format for the long-term,
   verifiable preservation of digitally-signed data across the migration
   to post-quantum cryptography.  It builds on the Evidence Record
   Syntax (ERS) of RFC 4998 and adds an explicit *algorithm-agility*
   extension: a record is a chain of signed attestations in which each
   link re-witnesses the data under a fresh signature primitive and
   commits to the prior link, so that the authenticity of the data
   survives the cryptographic break of any single primitive.  It
   specifies the canonical hashing that makes a record reproducibly
   verifiable across independent implementations, the exact binary
   encoding a decoder accepts, the authenticated temporal binding that
   places each link in time (an append-only transparency log à la RFC
   6962, whose signed inclusion receipt is _not-after_ evidence), and
   the verification procedure.  A per-link beacon anchor records _not-
   before_ evidence: from wire version 3 it is authenticated against the
   beacon's hash chain, with the beacon's classical pulse signature as
   defence in depth; the Security Considerations say which assumption
   each check rests on.
- **draft-baek-audit-absence-claims-00** (new-draft, score 6, adjacent_watchlist) [none]: [Interval Absence Claims in Agent Auditing: Problem Statement, Requirements, and Test Scenarios](https://datatracker.ietf.org/doc/draft-baek-audit-absence-claims/) — Audit records for software agents are designed to show what an agent
   did.  Relying parties also ask a different question: whether an agent
   could have used a capability at any time during a stated interval.
   Records of actions cannot answer that question, because authority
   that goes unused leaves no record of use, even if it existed for part
   of the interval.

   This document describes the problem of interval absence claims,
   defines terms, lists requirements that an audit evidence system needs
   to meet before it can support such claims, and gives test scenarios
   that expose false claims of absence.  It does not define a protocol,
   a data format, or a verification algorithm.  It is intended as input
   to discussions of auditing for agent delegation and interactions.
- **draft-buraglio-6man-hcga-00** (new-draft, score 6, core_identity) [none]: [Hierarchical Cryptographically Generated Addresses (HCGA)](https://datatracker.ietf.org/doc/draft-buraglio-6man-hcga/) — RFC 3972 defines Cryptographically Generated Addresses (CGA), in
   which the Interface Identifier (IID) of an IPv6 address is derived
   from a cryptographic public key.  The /64 subnet prefix is supplied
   by network infrastructure and has no cryptographic relationship to
   the key.  This document specifies Hierarchical CGA (HCGA), an
   extension to RFC 3972 that also derives part of the upper 64 bits --
   specifically the bits between the organizational prefix and the /64
   boundary -- from the same public key.  The result is an address whose
   full 128-bit value is a deterministic function of a public key
   (typically hardware-bound), an operator-controlled aggregate prefix,
   and two modifiers.  HCGA is a traceability component intended for use
   within a larger accountability architecture that supplies key
   attestation, parameter distribution, and source-address enforcement;
   that architecture is not specified here.  The capability supports
   workload network accountability in multi-tenant environments such as
   Kubernetes clusters, where infrastructure-assigned prefixes provide
   no per-instance cryptographic binding.
- **draft-cui-semantic-routing-ai-agent-communication-00** (new-draft, score 6, agent_identity) [none]: [Semantic Routing for AI Agent Communication](https://datatracker.ietf.org/doc/draft-cui-semantic-routing-ai-agent-communication/) — AI agents often know the intended outcome of a task without knowing
   which agent, model, tool, workflow, or service should process it.
   This document describes an application-layer semantic routing
   framework that selects one Processing Target from task intent,
   execution context, target capabilities, constraints, and local
   policy.  It defines a common operation-level information model and
   externally observable selection behavior that protocol bindings can
   preserve.  Semantic matching is implementation-specific.  This
   document does not define task decomposition, multi-agent
   orchestration, network-layer routing, target discovery, target
   invocation, or a new agent communication protocol.
- **draft-farrel-dawn-terminology-06** (new-draft, score 6, agent_identity) [none]: [Terminology for the Discovery of Agents With Names (DAWN)](https://datatracker.ietf.org/doc/draft-farrel-dawn-terminology/) — The proliferation of distributed Artificial Intelligence (AI) systems
   and agents has created a need for interoperable mechanisms for
   components of AI systems to discover each other.

   This document defines terminology for Discovery of Agents With Names
   (DAWN), focusing on the terms necessary to describe the discovery of
   information about AI systems and resources (e.g., AI agents).  The
   intention is that this common set of terms can be used by other
   documents related to DAWN and so achieve consistency of meaning
   across the space.
- **draft-ietf-cose-pqc-kem-00** (new-draft, score 6, verifiable_claims) [cose]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE](https://datatracker.ietf.org/doc/draft-ietf-cose-pqc-kem/) — This document describes conventions for using Post-Quantum Key
   Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and
   Encryption (COSE).
- **draft-ietf-dance-client-auth-15** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document describes how to use the TLSA record to publish client
   certificates or public keys, and also the rules and considerations
   for using them with TLS.  In addition, it defines a new TLS
   extension, DANE Client Identity, to convey the client's domain name
   identity to the server.
- **draft-ietf-emu-hybrid-pqc-eapaka-02** (new-draft, score 6, core_identity) [emu]: [Enhancing Security in EAP-AKA' with Hybrid Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-emu-hybrid-pqc-eapaka/) — Forward Secrecy for the Extensible Authentication Protocol Method for
   Authentication and Key Agreement (EAP-AKA' FS) is specified in
   [RFC9678], providing updates to [RFC9048] with an optional extension
   that offers ephemeral key exchange using the traditional Ephemeral
   Elliptic Curve Diffie-Hellman (ECDHE) key agreement algorithm for
   achieving perfect forward secrecy (PFS).  However, it is susceptible
   to future threats from Cryptographically Relevant Quantum Computers,
   which could potentially compromise a traditional ephemeral public
   key.  If the adversary has also obtained knowledge of the long-term
   key and ephemeral public key, it could compromise session keys
   generated as part of the authentication run in EAP-AKA'.

   This draft aims to enhance the security of EAP-AKA' FS protocol by
   using Post-Quantum/Traditional (PQ/T) hybrid Key Encapsulation
   Mechanisms (KEMs) [RFC9794] to make it quantum-safe.
- **draft-ietf-emu-pqc-eap-tls-04** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Enhancements to TLS-Based EAP Methods](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eap-tls/) — This document specifies the use of post-quantum cryptography in TLS-
   based EAP methods, including the Extensible Authentication Protocol
   with Transport Layer Security (EAP-TLS), EAP Tunneled TLS (EAP-TTLS),
   Protected EAP (PEAP), and EAP Tunnel Method (TEAP).  It also
   addresses challenges related to large certificate sizes and long
   certificate chains, as identified in [RFC9191], and specifies a
   mechanism to reduce TLS handshake size.
- **draft-ietf-emu-pqc-eapaka-05** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) in EAP-AKA prime](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eapaka/) — Forward Secrecy for the Extensible Authentication Protocol Method for
   Authentication and Key Agreement (EAP-AKA' FS) is specified in
   [RFC9678].  It updates [RFC9048] with an optional extension that
   provides ephemeral key exchange using the traditional Ephemeral
   Elliptic Curve Diffie-Hellman (ECDHE) key agreement algorithm.  This
   extension enables perfect forward secrecy (PFS).  However, it is
   susceptible to future threats from Cryptographically Relevant Quantum
   Computers, which could potentially compromise a traditional ephemeral
   public key.  If the adversary has also obtained knowledge of the
   long-term key and ephemeral public key, it could compromise session
   keys generated as part of the authentication run in EAP-AKA'.

   This draft aims to enhance the security of EAP-AKA' FS protocol by
   making it quantum-safe using Post-Quantum Key Encapsulation
   Mechanisms (PQ KEMs).
- **draft-ietf-jose-hpke-pq-pqt-02** (new-draft, score 6, verifiable_claims) [jose]: [JOSE HPKE PQ & PQ/T Algorithm Registrations](https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-pq-pqt/) — This document registers Post-Quantum (PQ) and Post-Quantum/
   Traditional (PQ/T) hybrid algorithm identifiers for use with JSON
   Object Signing and Encryption (JOSE), building on the Hybrid Public
   Key Encryption (HPKE) framework.
- **draft-ietf-regext-rdap-rpki-05** (new-draft, score 6, core_identity) [regext]: [Registration Data Access Protocol (RDAP) Extension for Resource Public Key Infrastructure (RPKI) Registration Data](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-rpki/) — The Resource Public Key Infrastructure (RPKI) is used to secure
   inter-domain routing on the internet.  This document defines a new
   Registration Data Access Protocol (RDAP) extension with identifier
   "rpki1", for accessing the RPKI registration data in the Internet
   Number Registry System (INRS) for the Route Origin Authorization
   (ROA), Autonomous System Provider Authorization (ASPA), and X.509
   Resource Certificate RPKI profiles through RDAP.  The INRS is
   composed of Regional Internet Registries (RIRs), National Internet
   Registries (NIRs), and Local Internet Registries (LIRs).
- **draft-liao-cose-sm-algorithms-00** (new-draft, score 6, verifiable_claims) [none]: [COSE and JOSE Registrations for ShangMi (SM) Cryptographic Algorithms](https://datatracker.ietf.org/doc/draft-liao-cose-sm-algorithms/) — This document registers code points for the use of the Chinese
   ShangMi (SM) cryptographic algorithms with CBOR Object Signing and
   Encryption (COSE) and JSON Object Signing and Encryption (JOSE): the
   elliptic curve curveSM2, the SM2 digital signature algorithm with the
   SM3 hash function, SM2 public key encryption for content key
   transport, HMAC-SM3, and the SM4 block cipher in GCM mode.  For COSE,
   it additionally registers the SM3 hash function, key derivation with
   HKDF-SM3, and SM4 in CCM mode.
- **draft-linker-diem-adem-core-03** (new-draft, score 6, authorization) [none]: [An Authentic Digital, Distinctive EMblem (ADEM) - Message Format and Authorization Model](https://datatracker.ietf.org/doc/draft-linker-diem-adem-core/) — In times of armed conflict, the emblems recognized under
   International Humanitarian Law (IHL), such as the red cross, red
   crescent, and red crystal, are used to mark physical assets.  This
   enables, e.g., the military to identify assets that enjoy specific
   protections under IHL during their operations.  This draft specifies
   the message format and authorization model for a digital emblem,
   which signals that network-connected services enjoy specific
   protections under IHL.
- **draft-many-seat-architecture-01** (new-draft, score 6, trust_infrastructure) [none]: [Secure Evidence and Attestation Transport (SEAT) Architecture](https://datatracker.ietf.org/doc/draft-many-seat-architecture/) — This document defines an architectural framework for composing Remote
   ATtestation procedureS (RATS) with Secure Evidence and Attestation
   Transport (SEAT).  The document establishes normalized terminology
   for SEAT, aligns RATS roles to transport endpoints, outlines
   topological patterns for attestation delivery timing, and
   characterizes the abstract cryptographic pattern by which Evidence is
   bound to a given transport connection.
- **draft-manyfolks-agentproto-arch-00** (new-draft, score 6, agent_identity) [none]: [Architecture for AI Agent Communications on the Internet](https://datatracker.ietf.org/doc/draft-manyfolks-agentproto-arch/) — This document defines the terminology and architecture for AI agent
   communications protocols over the Internet.  It provides the
   foundational architectural elements for the Agent Communications
   Protocol (ACP) - also known as agentproto - a new protocol to be
   developed in the IETF.  ACP enables communication between user agent
   clients and AI agents, between AI Agents and other AI Agents, or
   between AI Agents and tools.  All three of these interaction patterns
   - and the many use cases therein - require a session-like protocol
   which handles lifecycle management, including creation, modification,
   deletion and so on - along with the exchange of input and output.
   These session-like associations can be extremely long lived - running
   for hours or even days - and span multiple IP hosts used by the both
   the principal and by the agent.  They can also be highly intermittent
   with asynchronous responses.  All of these mean a new type of
   protocol is needed.
- **draft-mcguinness-oauth-client-ip-ranges-00** (new-draft, score 6, authorization) [none]: [OAuth Client IP Range Metadata](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-client-ip-ranges/) — This specification defines OAuth client metadata parameters for
   declaring the IP address ranges from which a client originates
   network requests.  The client_ip_ranges parameter carries a set of
   IPv4 and IPv6 prefixes by value.  The client_ip_ranges_uri parameter
   references an HTTPS resource containing the set, so that large and
   frequently changing sets can use standard HTTP retrieval and caching.
   The specification also defines how authorization servers validate,
   accept, and retain declared ranges.  The parameters can be used with
   OAuth 2.0 Dynamic Client Registration, OAuth Client ID Metadata
   Documents, and other mechanisms that convey client metadata.
   Authorization servers and other parties that obtain a client's
   metadata can use the declared ranges as an input to network access
   control.
- **draft-saez-xcim-04** (new-draft, score 6, core_identity) [none]: [eXplicit Consent-Identified Mail (XCIM)](https://datatracker.ietf.org/doc/draft-saez-xcim/) — XCIM specifies evidence that a party controlling an email address
   explicitly consented to receive defined types of communication from
   an identified sender.  A trusted third-party Consent Attester
   verifies address control, observes a separate affirmative decision,
   and signs an attestation binding the recipient, sender, and agreed
   types.  Blockchain anchoring provides immutable evidence of the
   attestation under an admitted finality policy.  Authenticated
   lifecycle events and fresh status distinguish the historical decision
   from current consent.

   XCIM concerns the consent relationship independently of individual
   email messages.  It does not sign, inspect, classify, or authenticate
   their content.  A receiving email service may use verified current
   consent as a positive policy signal after independently establishing
   the sender identity relevant to its query.  This document defines a
   portable consent object format and verification contract, together
   with requirements for separately admitted blockchain adapters.  It
   does not select a universal blockchain network or claim operational
   readiness.

   An alternative shared revocation profile allows reusable original
   grants and incremental withdrawal distribution.  It replaces repeated
   individual positive-status statements with authenticated,
   sufficiently recent synchronization evidence covering a sender epoch.
   Endpoint design and data-flow optimization remain implementation
   choices.
- **draft-templeman-scitt-measurement-capsule-01** (new-draft, score 6, verifiable_claims) [none]: [Declared-versus-Observed Measurement Capsules: A Profile for Third-Party Measurement Statements in SCITT](https://datatracker.ietf.org/doc/draft-templeman-scitt-measurement-capsule/) — This document defines the measurement capsule: a small, deterministic
   JSON record in which a party that is neither the subject of a claim
   nor a participant in the action it concerns records what the subject
   declared, what the measuring party observed, and the difference
   between the two.  A capsule carries digests of its evidence, a
   measurement state in which "could not be checked" is a first-class
   outcome, and no decision, approval or authorisation.  Capsules are
   identified by the SHA-256 of their JCS serialisation and batched
   under an RFC 9162 Merkle Tree Hash.  The document describes their
   registration as SCITT Signed Statements (RFC 9943), how they refer to
   rather than restate receipts issued under other profiles, its
   encoding as a COSE_Sign1 Signed Statement with test vectors, and one
   implementation, including where it does not yet match this profile.
- **draft-vandemeent-continuity-envelope-01** (new-draft, score 6, core_identity) [none]: [Continuity Envelope Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-continuity-envelope/) — This document defines the Continuity Envelope Protocol (CEP), a
   transport-agnostic protocol model for identity-bound messaging
   systems where delivery alone is not sufficient.

   CEP separates a visible envelope surface from sealed internal object
   truth and defines how receivers determine whether a delivered object
   may safely and legitimately continue.  The protocol distinguishes
   between control-plane notification, data-plane object carriage, and
   decision-plane continuation handling.  It further distinguishes a
   refused result from an absent one and from an unknown one, and
   requires that continuation decisions and refusals leave receipts.

   CEP is the umbrella model for companion drafts such as TIBET TAT,
   which specifies generic sealed handoff and transfer flow, and IDDrop,
   which profiles that handoff model for identity transfer.
- **draft-vandemeent-tibet-causal-time-03** (new-draft, score 6, core_identity) [none]: [TIBET Causal Time Substrate](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-causal-time/) — This document describes the TIBET Causal Time Substrate, a forward-
   only causal ordering model for identity-bound distributed systems.

   TIBET does not treat wall-clock time as the primary ordering
   primitive.  Instead, it uses a cryptographically bound logical-time
   structure encoded through append-only linkage, monotonic generation
   counters, and signed causal references.  External wall-clock sources,
   including NTP, RFC 3161 timestamping services, Roughtime, GNSS, or
   public ledger timestamps, are treated as auxiliary alignment anchors
   rather than as the constitutive source of event order.

   This revision adds an optional vector-observation layer for relating
   events across independent lanes, a classification of time-bounded
   checks that separates physical-world windows from ledger-state
   windows, replay protection that does not depend on clock agreement
   between parties, and a distinction between forks, breaks, and
   reseeds.

   The core claim is simple: TIBET is a forward-only causal substrate
   that enables recovery and reversibility without rewriting history.
- **draft-vandemeent-tibet-semantic-surface-manifest-03** (new-draft, score 6, core_identity) [none]: [TIBET Semantic Surface Manifest](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-semantic-surface-manifest/) — This document defines the Semantic Surface Manifest, a human-readable
   and policy-matchable routing layer for identity-bound continuity
   containers and TBZ-based sealed bundles.

   The Semantic Surface Manifest exposes limited dispatch metadata such
   as time fragment, context, profile, and priority without exposing
   sealed content.  It is intended for use in systems where routing
   decisions may need to occur before deep inspection, while trust
   remains anchored in intrinsic bundle properties such as magic bytes,
   manifests, hashes, signatures, and causal references.

   This revision separates two decisions that earlier revisions left
   implicit: a routing hint, which may be taken from the visible surface
   before any inspection, and an admission verdict, which must never
   rest on the visible surface.

   In short: address visible, content sealed.
- **draft-vandemeent-tibet-tat-01** (new-draft, score 6, core_identity) [none]: [TIBET TAT: Touch-and-Transfer Protocol](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-tat/) — This document specifies TIBET TAT, a Touch-and-Transfer protocol for
   moving sealed continuity-bearing objects across proximity, relay, and
   local-network handoff lanes.

   TAT defines a consent-bound handoff model, a seed exchange for tunnel
   establishment, encrypted chunk streaming, mutual transfer anchoring
   between sender and receiver, and the rules under which the carrier of
   an in-flight transfer may change.

   TAT does not define identity truth, semantic class, or sealed object
   class by itself.  Instead, it defines the wire and handoff layer that
   carries such objects once sender and receiver have agreed to
   transfer.  TAT is intended to sit between the Continuity Envelope
   Protocol (CEP) and higher-level application profiles such as IDDrop.
- **draft-watts-agentic-authority-graph-validation-01** (new-draft, score 6, authorization) [none]: [Agentic Authority Graph Validation: A Non-Vacuous Interchange Profile for Revocation-Cut Analysis](https://datatracker.ietf.org/doc/draft-watts-agentic-authority-graph-validation/) — Agentic and delegated systems can represent authority as a graph
   whose paths terminate at consequential resources.  Abstract graph
   models are useful, but interoperable validation requires a machine-
   readable representation and deterministic rules that do not
   accidentally accept vacuous or incomplete graphs.  This document
   defines Agentic Authority Graph Validation (AAGV), a JSON interchange
   profile and validation algorithm for authority roots, consequential
   sinks, declared normal paths, revocation cut sets, and snapshot edge
   state.  AAGV deliberately distinguishes structural cut validity from
   operational closure.  It rejects missing sink sets, missing normal-
   path inventories, dangling references, non-dominating cuts, and non-
   revocable cut edges; it returns INDETERMINATE rather than CLOSED when
   relevant edge state is unknown.  AAGV does not define an
   authorization token, discover hidden paths, or prove physical
   containment.
- **draft-watts-unison-noncollapse-01** (new-draft, score 6, authorization) [none]: [Typed UNISON and Non-Collapse Boundaries for Evidence and Authorization Systems](https://datatracker.ietf.org/doc/draft-watts-unison-noncollapse/) — This document describes a transport-neutral model for bounded
   correspondence among distinct representations and explicit promotion
   boundaries between observation, evidence, authorization, and
   execution.
- **draft-yoon-ccamp-pm-streaming-08** (new-draft, score 6, core_identity) [none]: [A YANG Data Model for Performance Monitoring Streaming on Common Transport Equipment](https://datatracker.ietf.org/doc/draft-yoon-ccamp-pm-streaming/) — This document applies the core Performance Monitoring (PM) collection
   and interval-capabilities YANG data models to common transport
   equipment.  It defines a YANG module of transport performance
   parameter identities, derived from the base identity of the PM
   collection model; it specifies the three transport parameter profiles
   of ITU-T G.7710 normatively; and it gives end-to-end examples that
   show capability discovery followed by YANG-Push subscription,
   notification, and threshold reporting for a transport profile.
- **draft-zhang-audit-record-limits-00** (new-draft, score 6, trust_infrastructure) [none]: [What an Agent Audit Record Can and Cannot Establish](https://datatracker.ietf.org/doc/draft-zhang-audit-record-limits/) — Agent audit records are signed, chained, counter-signed, timestamped,
   and registered with transparency services.  Each mechanism
   establishes a narrower fact than it is often taken to establish.
   This document states, for any record format, protocol, or payment
   method, what a check of an agent audit record can and cannot
   establish about four properties: the independence of the entities
   that signed or observed it, the completeness of a set of records, the
   time at which a record or an action existed, and the result that a
   verifier reports.  It defines independence by control rather than by
   key or process separation, separates the independence of a signer
   from the independence of an observation, states which commitments
   cannot support a report that a set of records is complete, and
   requires a verifier to report unauthenticated content as
   unauthenticated.  It defines no record format, role, log, or service.
- **draft-zollner-scim-group-membership-00** (new-draft, score 6, core_identity) [none]: [SCIM Group Membership Resource Type Extension](https://datatracker.ietf.org/doc/draft-zollner-scim-group-membership/) — This document extends the System for Cross-domain Identity Management
   (SCIM) 2.0 standard by defining a new "GroupMembership" top-level
   resource.  Under the existing model defined in RFC 7643, group
   memberships are represented as values in a multi-valued attribute
   within a Group resource.  This architecture lacks native support for
   server-side pagination, filtering, or sorting of individual members.
   In deployments managing large-scale groups (e.g., 100,000 to
   1,000,000 members or more), retrieving a Group resource results in
   massive HTTP response payloads that can exceed 100MB in size.  This
   can lead to service timeouts, memory exhaustion, and network
   instability, and has led to many major SCIM implementations choosing
   to not support returning the value of the "members" attribute for
   Group resources.  This extension introduces a flattened resource
   model that enables group memberships to benefit from pagination and
   other SCIM protocol features, ensuring interoperability and
   performance at scale.
- **draft-bu-dawn-ard-architecture-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Resource Discovery (ARD) Architecture](https://datatracker.ietf.org/doc/draft-bu-dawn-ard-architecture/) — This document describes the high-level architecture for Agent
   Resource Discovery (ARD), an open, federated framework for
   publishing, indexing, discovering, and invoking software agent
   capabilities (such as Model Context Protocol servers, Agent-to-Agent
   agents, programmatic skills, and web APIs) across local networks,
   enterprise domains, and the public Internet.  It defines the system
   roles, deployment topologies, core architectural principles, and end-
   to-end interaction flows that connect the ARD specifications for
   establishing Initial Contact and the Discovery Interface for
   capability lookup in the ARD catalog.  The Registration interface
   will be specified in a later document.
- **draft-bu-dawn-ard-discovery-00** (new-draft, score 5, adjacent_watchlist) [none]: [Agent Resource Discovery (ARD): Manifest and Lookup](https://datatracker.ietf.org/doc/draft-bu-dawn-ard-discovery/) — This document specifies the catalog representation and lookup
   protocol for Agent Resource Discovery (ARD), an open architecture for
   publishing, discovering, and searching software agent capabilities
   across federated networks.  ARD defines a JSON-LD capability
   description envelope (the ARD Entry) and catalog container (the ARD
   Manifest) identified by domain-anchored Uniform Resource Names
   (URNs), cryptographic publisher authority bindings (the Trust
   Manifest), and an HTTP query interface supporting structured,
   semantic, and federated search across registries.  Initial contact
   for discovering catalog entry points and active agent registration
   are specified in companion ARD documents.
- **draft-calabria-bpm-ai-fabric-training-bench-00** (new-draft, score 5, ai_infrastructure) [none]: [Benchmarking Methodology for AI Training Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bpm-ai-fabric-training-bench/) — This document defines benchmarking terminology, methodologies, and
   Key Performance Indicators (KPIs) for evaluating Ethernet-based AI
   training network fabrics.

   As large-scale distributed Artificial Intelligence / Machine Learning
   (AI/ML) training clusters grow to tens of thousands of accelerators
   (GPUs or generic accelerator processing units (XPUs)), the backend
   network fabric determines Job Completion Time (JCT), training
   throughput, and accelerator utilization.

   This document establishes vendor-independent, reproducible test
   procedures for benchmarking fabric-level performance under realistic
   AI training workloads.  The tests cover Remote Direct Memory Access
   (RDMA) over Converged Ethernet version 2 (RoCEv2) transport, the
   Ultra Ethernet Transport (UET) protocol defined by the Ultra Ethernet
   Consortium (UEC) Specification 1.0, congestion management (Priority
   Flow Control (PFC), Explicit Congestion Notification (ECN), Data
   Center Quantized Congestion Notification (DCQCN), Credit-Based Flow
   Control (CBFC)), load balancing strategies (Equal-Cost Multi-Path
   (ECMP), Dynamic Load Balancing (DLB), packet spraying), collective
   communication patterns (AllReduce, AllToAll, AllGather), and scale/
   soak testing.

   The methodology enables direct, reproducible comparison across switch
   ASICs, NIC transport stacks (RoCEv2 and UET), and fabric
   architectures (2-tier Clos, 3-tier Clos, and rail-optimized).
- **draft-creator-bvs-protocol-01** (new-draft, score 5, adjacent_watchlist) [none]: [Biometric Vector Steganography for Document Trust and AI-First Preambles (BVS)](https://datatracker.ietf.org/doc/draft-creator-bvs-protocol/) — This document specifies the Biometric Vector Steganography (BVS)
   protocol.  It defines an asynchronous, differential geometry-based
   method for embedding machine-readable metadata (AI-First Preambles)
   and cryptographic signatures into plain text documents.  By utilizing
   two correlating Scalable Vector Graphics (SVG) paths (walz and
   walz_shadow), BVS enables the creation of a dynamic, biometric
   anchor, representing the digital equivalent of a physical wax seal.
   The protocol guarantees document integrity within strict stream
   boundaries, proves the author's authenticity, and provides pre-
   processed metadata for edge-parsers without increasing the token load
   for Large Language Models (LLMs).
- **draft-das-protected-transaction-execution-finality-00** (new-draft, score 5, authorization) [none]: [Protected Transaction Authority and Execution-Finality Boundaries for Delegated Digital Operations](https://datatracker.ietf.org/doc/draft-das-protected-transaction-execution-finality/) — Recent publicly reported incidents involving unauthorized use of
   legitimately signed account-delegation and asset-transfer operations
   have exposed a gap between cryptographic validity and permission to
   perform an exact consequential act.  This document proposes an
   experimental, transport-independent execution-finality protocol for
   delegated digital operations.  A Candidate Act is placed in a non-
   effective state; protected collection-time and execution-time
   enforcement domains bind approved intent, independently reconstruct
   the pending effect, and require an unforgeable, sink-specific,
   single-use authorization before signing, dispatching, transmitting,
   exporting, or actuating.  The protocol specifies state continuity,
   revocation, nonce burn, quota settlement, delegated-code controls,
   multi-domain interoperability, failure behavior, receipts,
   conformance tests, and migration profiles.  It includes ASCII
   sequence diagrams and flowcharts, complete executable Python, Go, and
   JavaScript reference listings, a reproducible test-vector generator
   and runner, and recorded cross-language test results in informative
   appendices.  This is a proposal for discussion, not an adopted IETF
   standard; the reference code is not production cryptographic custody
   software.
- **draft-du-ai-agent-communication-6g-aspect-01** (new-draft, score 5, agent_identity) [none]: [Use Cases and Requirements of AI Agent Communication from 6G Aspect](https://datatracker.ietf.org/doc/draft-du-ai-agent-communication-6g-aspect/) — AI Agent can do some tasks as an assistant to human beings.  During
   the task process, the Agent may need to connect to other Agents with
   different skills relative to the task.  The Agent to Agent
   communication is a new kind of traffic for Internet, and some new
   requirements for networking are proposed.  This document talks about
   the requirements and key issues of global AI agent communication
   towards 6G.  Some 6G related use cases from 3GPP documents are
   introduced.  After that, the related requirements for the AI Agent
   Communication Network (ACN) are proposed, and potential ACN
   frameworks and standardization works for the AI Agent Communication
   are also discussed.
- **draft-gondwana-we-are-all-individuals-01** (new-draft, score 5, core_identity) [none]: [We Are All Individuals](https://datatracker.ietf.org/doc/draft-gondwana-we-are-all-individuals/) — Participation in the IETF is by individuals.  This document makes
   that principle concrete for an environment in which software agents
   can produce and submit text.  Each Datatracker account belongs to one
   human who has acknowledged the Note Well.  Every IETF Contribution is
   vouched for by one human who is accountable for it.  Anonymous
   Contributions are not accepted, and no human may use more than one
   identity in the same piece of work.  Reading the IETF's work remains
   open to everyone, with no account or identification required.
- **draft-guorong-utxo-dns-03** (new-draft, score 5, verifiable_claims) [none]: [UTXO6-DNS: Resolving Payment Endpoints via Private-use RRTYPE and Prefix Isolation](https://datatracker.ietf.org/doc/draft-guorong-utxo-dns/) — This document specifies the _utxo application namespace for DNS.  It
   defines how wallet clients and TEE (Trusted Execution Environment)
   applications resolve verifiable payment endpoints and blockchain UTXO
   (Unspent Transaction Output) references using DNS.

   To avoid exacerbating public RRTYPE space congestion and DNS-layer
   transparent parsing, this document utilizes the RFC 3597 Private-use
   space (QTYPE 65400).  The DNS protocol does not parse the payload.
   Application semantics are isolated strictly via the _utxo underscore
   prefix in the owner name, while the RDATA consists of a purely opaque
   CBOR-encoded byte stream.
- **draft-hood-agtp-communication-01** (new-draft, score 5, core_identity) [none]: [AGTP Communication Protocol](https://datatracker.ietf.org/doc/draft-hood-agtp-communication/) — This document specifies the AGTP Communication Protocol (AGTP-
   COMMUNICATION): the companion specification for real-time multi-modal
   communication between agents over the Agent Transfer Protocol (AGTP).
   AGTP-COMMUNICATION defines how voice, video, and other real-time
   media streams are exchanged between agents on the agent-native
   substrate, with native support for the wire-level identity, authority
   scope, and attribution that AGTP provides.

   This is an early specification covering bilateral (two-agent) real-
   time communication.  Multi-party conversations and conferencing
   patterns are out of scope for this revision and are deferred to
   future companion work.
- **draft-ietf-rats-pkix-key-attestation-08** (new-draft, score 5, adjacent_watchlist) [rats]: [Evidence Encoding for Hardware Security Modules](https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/) — This document specifies a vendor-agnostic format for Evidence
   produced and verified within a PKIX context.  The Evidence produced
   this way includes claims collected about a cryptographic module, such
   as a Hardware Security Module (HSM), and elements found within it
   such as cryptographic keys.

   One scenario envisaged is that the state information about the
   cryptographic module can be securely presented to a remote operator
   or auditor in a vendor-agnostic verifiable format.  A more complex
   scenario would be to submit this Evidence to a Certification
   Authority to aid in determining whether the storage properties of
   this key meet the requirements of a given certificate profile.
- **draft-ietf-webbotauth-httpsig-protocol-01** (new-draft, score 5, core_identity) [webbotauth]: [HTTP Message Signatures for automated traffic](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) — This document describes a protocol for identifying automated traffic
   using [HTTP-MESSAGE-SIGNATURES].  The goal is to allow automated HTTP
   clients to cryptographically sign outbound requests, allowing HTTP
   servers to verify their identity with confidence.

   It defines the Signature-Agent header field for in-band key
   discovery, a key directory format based on JWKS, and a well-known URI
   at which that directory is served.
- **draft-intra-handshake-fail-58** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-100833, CVE-2026-100835,CVE-2026-108265, CVE-2026-108266, CVE-2026-108267, CVE-2026-108268, CVE-2026-108269, CVE-2026-92701, CVE-2026-92702, CVE-2026-108362, CVE-2026-33697, CVE-2026-108361 and others)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-100833] of
   CVSS 9.6, [CVE-2026-108265] of CVSS 9.1, [CVE-2026-108266] of CVSS
   9.1, [CVE-2026-108267] of CVSS 9.1, [CVE-2026-108268] of CVSS 9.1,
   [CVE-2026-108269] of CVSS 9.1, [CVE-2026-100835] of CVSS 9.1,
   [CVE-2026-92701] of CVSS 9.1, [CVE-2026-92702] of CVSS 9.1,
   [CVE-2026-108362] of CVSS 9.1, [CVE-2026-33697] of CVSS 7.5,
   [CVE-2026-108361] of CVSS 7.2, and several GitHub Security Advisories
   (GHSAs) in the process of getting CVE IDs, which provide substantial
   technical evidence of how early attestation fails in practice, even
   *without physical access* to the desired machine.  Moreover, since
   continuous attestation is generally required [CSA-eBPF]
   [MITRE-Continuous-Attestation], early attestation adds *unnecessary
   complexity*. The results are backed by the research
   [Intra-handshake.fail], [TLS-RA], [EarlyAttestationBleed] and the
   artifacts [Intra-handshake.fail-repo] in state-of-the-art formal
   analysis tool, ProVerif, under Apache-2.0 license for
   reproducibility, extensibility, and review, and have been
   acknowledged by the relevant stakeholders.  Currently, there are *one
   CVE of CVSS 9.6, nine CVEs of CVSS 9.1, one CVE of CVSS 8.2, one CVE
   of CVSS 7.5, one CVE of CVSS 7.2, and several GHSAs published
   awaiting CVE IDs against the broader early attestation covering all
   layers of the ecosystem up to the application*. The research papers
   on these are currently either under submission or being prepared for
   submission.  The artifacts of these papers will be shared with the
   community under Apache-2.0 license for reproducibility,
   extensibility, and review.  Based on our work, all except two
   implementations of early attestation have been archived, withdrawn,
   or moved to post-handshake attestation.  In our analysis
   [Intra-handshake.fail-repo] and [ID-Crisis-repo], the remaining two
   implementations of early attestation -- Edgeless Systems Contrast and
   Meta's AI -- remain vulnerable.  We recommend users of these two
   implementations to carefully evaluate their systems and understand
   the risks.  If you are aware of any open-source implementation of
   early attestation that is not yet covered in this draft, please let
   us know to responsibly disclose the vulnerabilities to them.
- **draft-irtf-nmrg-ibn-usecases-04** (new-draft, score 5, ai_infrastructure) [nmrg]: [Use Cases and Practices for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-irtf-nmrg-ibn-usecases/) — This document proposes a methodology to construct an Intent-Based
   Networking (IBN) system.  According to this methodogy, it decribes
   several use cases of IBN.  The methodology for the IBN system
   includes data collection for system awareness in the IBN system and
   then the construction of the IBN system.  This construction consists
   of intent translation, policy translation, policy verification,
   policy deployment, policy monitoring, policy validation, policy
   optimization, and intent report.  In addition, practices are also
   summarized to instruct the construction of next generation network
   management systems with the integration of IBN techniques.  Finally,
   this document discusses three aspects for the deployment of the IBN
   system on the real world.  They are Multi-Domain Dichotomy for IBN,
   the Integration of IBN and Network Digital Twin (NDT), and IBN with
   Artificial Intelligence (AI).
- **draft-mcw-opsawg-icon-requirements-02** (new-draft, score 5, agent_identity) [none]: [Architecture and Requirements for Observability, Control and Intervention of Network Management Agents](https://datatracker.ietf.org/doc/draft-mcw-opsawg-icon-requirements/) — This document defines architecture and a set of requirements for
   Observability, Control, and Intervention for Network Management
   Agents.

   It identifies gaps in existing mechanisms and specifies required
   interaction capabilities between Agent supervision systems and
   network management agents across multi-vendor environments,
   specifically observability, control, and runtime intervention.  The
   requirements aim to guarantee comprehensive, lifecycle control over
   AI agents and enable observation, constraint, intervention, and
   correction to ensure network operational resilience and continuity.
- **draft-nestorov-scitt-p10-underdetermination-02** (new-draft, score 5, trust_infrastructure) [none]: [P10 Underdetermination Profile: Adjudication Statements over SCITT](https://datatracker.ietf.org/doc/draft-nestorov-scitt-p10-underdetermination/) — P10 defines a third-party-verifiable binding for
   NotDemonstrated(reason=underdetermined).  A conforming P10
   Adjudication Statement carries two canonical witness worlds that are
   compatible with the same closed evidence set and produce different
   values for the same frozen claim.  The witness result is checked
   against committed profile semantics and bound into a SCITT
   Transparent Statement containing an in-toto Statement v1 predicate.
   The result establishes underdetermination only relative to the
   declared profile and does not identify the actual world or establish
   either claim value as true.
- **draft-song-fann-framework-03** (new-draft, score 5, adjacent_watchlist) [none]: [A Framework for Fast Network Notifications](https://datatracker.ietf.org/doc/draft-song-fann-framework/) — High-performance network applications, such as AI/ML distributed
   training/inference and large-scale cloud services, require rapid
   adaptation to link faults, signal degradation, and transient
   congestion.  Existing dissemination mechanisms are often too slow or
   coarse to match the detection capabilities of modern forwarding
   hardware.

   This document specifies a framework for Fast Network Notifications
   (FANN).  It defines the reference architecture, functional roles,
   information model, delivery and scoping mechanisms, operational
   procedures, and integration principles with existing protocols to
   guide future protocol specifications.
- **draft-watts-boundary-jurisdiction-architecture-02** (new-draft, score 5, agent_identity) [none]: [Boundary Jurisdiction Architecture for Agentic and Delegated Systems](https://datatracker.ietf.org/doc/draft-watts-boundary-jurisdiction-architecture/) — This document describes a protocol-neutral architecture for
   separating possession of capability from jurisdiction over
   consequential authority boundaries.  It models authority as
   reachability in a time-indexed capability graph, defines revocation
   cuts, and specifies fail-closed semantics for delegation and
   revocation closure.
- **draft-watts-gov-verification-promotion-boundaries-01** (new-draft, score 5, agent_identity) [none]: [Government-Oriented Verification Promotion Boundaries for Agentic Assurance Profiles](https://datatracker.ietf.org/doc/draft-watts-gov-verification-promotion-boundaries/) — Government and critical-infrastructure relying parties require
   explicit boundaries between successive assurance claims.  This
   document defines Verification Promotion Boundaries (VPB) as a
   protocol-neutral profile that prevents verification evidence obtained
   at one stage from being silently promoted to a stronger claim.  The
   stages are REGISTERED, SPEC_VALIDATED, LOCAL_CONFORMANT,
   INDEPENDENTLY_REPRODUCED, SECURITY_TESTED, and RELEASE_ELIGIBLE.  A
   local PASS does not imply independent reproduction; an independent
   reproduction does not imply security testing; and no stage implies
   endorsement by any standards body or government agency.  The profile
   further distinguishes subject evidence (negative findings against the
   tested artifact) from verifier evidence (positive findings that the
   verification system correctly detected defects).  Arithmetic and
   protocol preconditions, including on-curve validation before
   metamorphic fixtures, are mandatory before any promotion.  This
   document is intended for high-assurance government deployments and is
   not a U.S.  Government standard.
- **draft-watts-scientific-admissibility-evidence-01** (new-draft, score 5, trust_infrastructure) [none]: [Scientific Admissibility Evidence Records for Verifiable Research Provenance](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility-evidence/) — This document describes a portable JSON evidence-record format for
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
- **draft-wright-verdict-record-00** (new-draft, score 5, trust_infrastructure) [none]: [Verdict Records: Results on Claims that Cite Receipts as Evidence](https://datatracker.ietf.org/doc/draft-wright-verdict-record/) — This document defines a verdict record: a statement, bound to its
   issuer, of a result reached on a claim, together with the evidence
   the result relies on and the rule by which the result can be re-
   derived.  Evidence is cited by digest and can be a receipt or record
   in any format, such as a SCITT Receipt or an Agent Action Capsule.
   The document defines how a checker checks a verdict record and what
   such a check does and does not show.  It defines no receipt format
   and changes none.
- **draft-zhang-cats-token-aware-ts-01** (new-draft, score 5, adjacent_watchlist) [none]: [A token-aware traffic steering solution for agent service](https://datatracker.ietf.org/doc/draft-zhang-cats-token-aware-ts/) — this document proposes a token-aware traffic steering mechanism.  By
   parsing token semantic features, sequence lengths, and task types,
   and comprehensively incorporating network link status, model
   capabilities, and compute resource states into routing decisions,
   this mechanism achieves joint optimal scheduling of resources.
- **draft-zhangb-cats-sci-implementation-02** (new-draft, score 5, adjacent_watchlist) [none]: [Metric Snapshot Exchange between SCI and C-SMA in CATS](https://datatracker.ietf.org/doc/draft-zhangb-cats-sci-implementation/) — This document specifies metric snapshot exchange between a Service
   Contact Instance (SCI) and a CATS Service Metric Agent (C-SMA).  It
   defines atomic replacement, ordering, and validity for periodic full
   snapshots and change-triggered updates over HTTPS/JSON.  An
   informative appendix explains how one shared snapshot YANG model can
   support generation of the publication and response messages.
- **draft-cowlishaw-carbontxt-00** (new-draft, score 4, trust_infrastructure) [none]: [carbon.txt: A transparency protocol for public sustainability data](https://datatracker.ietf.org/doc/draft-cowlishaw-carbontxt/) — This document specifies the carbon.txt convention, a machine-readable
   format for publishing links to disclosures concerning the
   environmental impact of an organization's digital / ICT operations at
   a predictable location on the web.  Carbon.txt is a TOML document
   that acts as an index: it declares where an origin's impact
   disclosures (Annual reports, Sustainability policies, Third party
   certifications, Quantitative measurements or estimations) may be
   found, and optionally lists upstream service providers whose own
   disclosures may be relevant to the origin's environmental impact.
   Carbon.txt does not carry numeric impact metrics or specific claims
   about impacts itself; it links to documents that do.  In addition it
   defines a discovery mechanism by which certain origins may delegate
   their carbon.txt implementation to another.
- **draft-kelley-aipref-training-preference-signal-00** (new-draft, score 4, adjacent_watchlist) [none]: [Machine-Readable Training Preference Signal](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/) — This document describes how a service operator binds usage
   preferences (e.g., "no AI training") to paths by writing ordinary
   robots.txt groups keyed by a per-purpose policy token in the User-
   Agent line.  It introduces no new directive names and no new grammar:
   the path language, longest-match precedence, and group structure of
   robots.txt are not changed.

## Adjacent / watchlist

- **draft-adams-bimi-reporting-12** (new-draft, score 3, core_identity) [none]: [BIMI Reporting](https://datatracker.ietf.org/doc/draft-adams-bimi-reporting/) — To support the utility of Brand Indicators for Message Identification
   (BIMI), domains publishing BIMI records may find it useful to know
   when their logos are failing to be displayed as expected.  When an
   entity, for example a mailbox operator, determines whether or not to
   display the logo identified in the BIMI record, they may encounter
   errors trying to retrieve the image file.  Similarly, the associated
   evidence document used to validate the logo may fail evaluation.  In
   other cases, the evaluator may decide that despite everything
   validating, they may rely on local policies that determine validated
   logos should still not be displayed.  This specification defines how
   BIMI evaluators should report their evaluation outcome back to the
   publisher within the context of existing Domain-based Message
   Authentication, Reporting, and Conformance (DMARC) reports.
- **draft-anish-spring-bimap-multicast-02** (new-draft, score 3, adjacent_watchlist) [none]: [SRv6 Bitmap Multicast](https://datatracker.ietf.org/doc/draft-anish-spring-bimap-multicast/) — Multicast forwarding in a network provides advantages in improving
   the network usage and performance.  In some cases it helps improve
   the operations in managing network.  The major challenge in multicast
   operations is in managing the per-flow states in the network as
   required by all the legacy multicast frameworks.

   This document specifies a bitmap forwarding extension to SRv6 to
   support state-free forwarding model in a network.
- **draft-ar-acme-pqc-tlsjws-01** (new-draft, score 3, core_identity) [none]: [Quantum-Ready ACME Mechanism](https://datatracker.ietf.org/doc/draft-ar-acme-pqc-tlsjws/) — This document updates RFC 8555 (ACME) to specify post-quantum and PQ/
   T hybrid cryptographic requirements for quantum-ready deployments.
   The Automatic Certificate Management Environment (ACME) automates
   certificate issuance, validation, and management over HTTPS using
   JSON Web Signatures (JWS) to authenticate client request payloads.
   Current ACME deployments rely on traditional public-key algorithms in
   both JWS and TLS, which are vulnerable to attacks from
   Cryptographically Relevant Quantum Computers (CRQCs).  This
   specification defines PQC or PQ/T hybrid TLS 1.3 key establishment
   and specifies PQC or PQ/T authentication mechanisms for JWS and TLS
   under the quantum-ready ACME mechanism.  This specification enables
   ACME clients and servers to achieve quantum-resistant confidentiality
   and authentication.
- **draft-arash-ebrahimi-ump-protocol-02** (new-draft, score 3, adjacent_watchlist) [none]: [Universal Modular Protocol (UMP)](https://datatracker.ietf.org/doc/draft-arash-ebrahimi-ump-protocol/) — The Universal Modular Protocol (UMP) proposes a modular approach to
   application-layer communication.  Instead of implementing every
   protocol feature in a monolithic protocol or application, UMP allows
   communication behavior to be composed from modules that can be
   obtained from a peer or a repository.  A protocol engine manages
   module execution, communication, signatures, and resource
   restrictions.  Modules execute in a WebAssembly sandbox, while the
   Protocol Description Language (PDL) is intended to support module
   composition and analysis.  UMP is designed to reduce the effort
   required to introduce new protocol features, reuse protocol
   components, and connect applications that otherwise require protocol-
   specific integration.  This document describes the motivation, module
   model, protocol operation, PDL, repositories, and current
   implementation status of UMP.
- **draft-artamokhov-dawn-marketplace-discovery-01** (new-draft, score 3, adjacent_watchlist) [none]: [A Discovery Document and Signed Catalogue for Capability Marketplaces](https://datatracker.ietf.org/doc/draft-artamokhov-dawn-marketplace-discovery/) — This document defines a JSON discovery document, served at a well-
   known URI, that carries the public properties a client needs before
   using a capability index: its name, the protocol versions it serves,
   the location of its catalogue, and the key that signs the catalogue.
   It also states the requirements for that signed catalogue and defines
   one signature profile.  Discovery between indexes, catalogue exchange
   and trust are out of scope.
- **draft-avasarala-stir-passport-device-info-00** (new-draft, score 3, core_identity) [none]: [PASSporT Device Information Extension for Enhanced Caller Authentication and Fraud Resilience](https://datatracker.ietf.org/doc/draft-avasarala-stir-passport-device-info/) — This document defines a PASSporT extension and a new claim, "dinfo",
   for carrying authenticated, privacy-minimized information about the
   endpoint associated with the origination of a call.  The claim
   conveys coarse-grained device characteristics and an optional, non-
   correlatable device reference.

   The information is intended for use as an additional input to fraud
   analysis, policy enforcement, and operational diagnostics.  It is not
   an assertion that the endpoint, caller, or call is trustworthy.  This
   document specifies claim syntax, creation and verification
   procedures, privacy requirements, and IANA registrations.
- **draft-bonica-tcpm-tcp-ao-long-algs-07** (new-draft, score 3, core_identity) [none]: [Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/) — RFC5926 creates a registry of cryptographic algorithms that can be
   used with TCP-AO.  This document expands that registry, adding two
   Message Authentication Code (MAC) algorithms, HMAC-SHA256 and
   KMAC256.

   The MAC algorithms described by this document produce 256-bit (i.e.,
   32-byte) MACs.  When 32-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 36 of the 40 bytes available for TCP options.
- **draft-brissette-idr-dc-origin-leaf-id-00** (new-draft, score 3, core_identity) [none]: [Origin-Leaf Identification in Data-Center eBGP Underlays using BGP Large Communities](https://datatracker.ietf.org/doc/draft-brissette-idr-dc-origin-leaf-id/) — Data-center fabrics that run hop-by-hop eBGP routing frequently need
   to identify the originating node (leaf) of a prefix as it is
   propagated through the fabric.  The BGP AS_PATH attribute provides
   loop prevention and identifies the originating Autonomous System
   (AS), but under common AS numbering models an AS does not map to a
   single leaf.  While several BGP community mechanisms could carry such
   an identifier, there is no documented practice describing the
   mechanism and encoding choices for underlay origin-leaf tagging.

   This document analyzes the problem, states the requirements, and
   surveys candidate BGP mechanisms for carrying an origin-leaf
   identifier.  It recommends encoding the identifier in a BGP Large
   Community (RFC 8092), describes how the identifier is allocated
   within the Large Community namespace, and describes how it is
   originated, propagated unchanged across the fabric, and consumed at
   receiving leaves.  It also describes an optional profile for locally
   significant route-attachment metadata.  This document is
   Informational and defines no new protocol elements.
- **draft-busi-nmop-simap-rfc8795-applicability-03** (new-draft, score 3, adjacent_watchlist) [none]: [Applicability of RFC8795 YANG data model to SIMAP](https://datatracker.ietf.org/doc/draft-busi-nmop-simap-rfc8795-applicability/) — This document analyses the applicability of the RFC 8795 YANG data
   model to Service & Infrastructure Maps (SIMAP) and in particular
   analysis which requirements can be supported by the existing YANG
   data model defined in RFC 8795.
- **draft-celi-wiggers-tls-authkem-08** (new-draft, score 3, core_identity) [none]: [KEM-based Authentication for TLS 1.3](https://datatracker.ietf.org/doc/draft-celi-wiggers-tls-authkem/) — This document gives a construction for a Key Encapsulation Mechanism
   (KEM)-based authentication mechanism in TLS 1.3.  This proposal
   authenticates peers via a key exchange protocol, using their long-
   term (KEM) public keys.
- **draft-claise-green-capability-discovery-03** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Power State Capability Discovery](https://datatracker.ietf.org/doc/draft-claise-green-capability-discovery/) — This document defines a YANG data model that augments the system
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
- **draft-cummings-tare-00** (new-draft, score 3, adjacent_watchlist) [none]: [Time Asymmetry Regression Estimator (TARE): Estimating the Packet-Length-Dependent Component of NTP Offset](https://datatracker.ietf.org/doc/draft-cummings-tare/) — Network Time Protocol (NTP) offset measurements can contain bias
   associated with differences in packet serialization delay in the
   forward and reverse directions.  This document describes TARE (Time
   Asymmetry Regression Estimator), a client-side experimental method
   that estimates a packet-length-dependent component of measured NTP
   offset using regression over exchanges with varied packet lengths.  A
   client may use the estimate to produce two named outputs
   (Section 6.1): Output A, an offset normalized to a selected reference
   packet length, which does not reduce the length-dependent bias at
   that length; and Output B, the intercept of the fitted model at zero
   length of a documented length layer, an extrapolated quantity whose
   meaning depends on the validity of the model.

   TARE does not, by itself, determine or remove fixed propagation-delay
   asymmetry, distinguish that asymmetry from true clock offset, or
   guarantee improved synchronization accuracy.  This document defines
   an experimental measurement model, calibration procedure, validity
   checks, fallback behavior, and evaluation plan.  It does not define
   new NTP packet fields or require server changes.
- **draft-darkdragon-hardware-bot-attestation-00** (new-draft, score 3, trust_infrastructure) [none]: [Hardware-Interrupt Attestation for Privacy-Preserving Bot Mitigation](https://datatracker.ietf.org/doc/draft-darkdragon-hardware-bot-attestation/) — This document proposes a privacy-first, OS kernel-level attestation
   mechanism to mitigate automated botnets on internet platforms.  By
   evaluating input events at the physical hardware interrupt layer, the
   system generates attestation tokens only upon detecting automated
   execution, remaining silent during legitimate human usage to preserve
   user privacy.
- **draft-eastlake-dnssd-rfc2931bis-sigzero-05** (new-draft, score 3, core_identity) [none]: [Domain Name System (DNS) Public Key Based Request and Transaction Authentication (MSGSIG, SIG(0))](https://datatracker.ietf.org/doc/draft-eastlake-dnssd-rfc2931bis-sigzero/) — This document specifies the MSGSIG and SIG(0) Domain Name System
   (DNS) Resource Records (RRs) which provide public key based
   authentication of DNS requests and transactions.  MSGSIG is the
   RECOMMENDED option.  This document obsoletes RFC 2931 and updates RFC
   6891.
- **draft-fu-onsen-update-l3sm-service-models-03** (new-draft, score 3, adjacent_watchlist) [none]: [Extensions to the YANG Data Model for L3VPN Service Delivery](https://datatracker.ietf.org/doc/draft-fu-onsen-update-l3sm-service-models/) — [RFC8299] defines a YANG data model for L3VPN service delivery.  The
   base L3VPN Service Model (L3SM) has limitations regarding dynamic
   service features.  In addition, emerging technologies including SRv6
   and quantum security bring new service capabilities available to
   customers, which are not natively supported by L3SM.  This document
   defines a set of extensions to address the limitations of L3SM.

   These augmentations are designed to be backward-compatible and do not
   obsolete [RFC8299].
- **draft-gondwana-dkim2-authres-01** (new-draft, score 3, core_identity) [none]: [Reporting DKIM2 Verification Results in Authentication-Results](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-authres/) — DomainKeys Identified Mail Signatures v2 (DKIM2) produces a
   verification result for an email message.  This document defines how
   that result is reported in the Authentication-Results header field,
   registering the "dkim2" authentication method, the result values it
   can take, and two properties which identify the signing domain and
   the point in the chain at which verification failed.  Diagnostic
   detail about each hop is carried in a human-readable comment.
- **draft-hanley-rsdggs-02** (new-draft, score 3, core_identity) [none]: [Regulatory Spectrum Discrete Global Grid System (RSDGGS)](https://datatracker.ietf.org/doc/draft-hanley-rsdggs/) — This document defines the Regulatory Spectrum Discrete Global Grid
   System (RSDGGS), a compact, variable-length hierarchical geographic
   indexing scheme designed to encode geographic location and regulatory
   jurisdiction for Industrial, Scientific, and Medical (ISM) radio band
   operations.  RSDGGS encodes location into a 1-to-8 octet compact byte
   array where length implicitly dictates spatial resolution, allowing
   privacy-preserving location truncation without loss of spatial
   indexing structure.

   For low-power constrained networks (6lo), RSDGGS provides a
   lightweight binary representation and CBOR payload that can be
   embedded directly into IEEE 802.15.4 Information Elements (IEs) or
   lower-layer beacons, enabling constrained IoT nodes to discover local
   spectrum regulations (permitted channels, power limits, duty cycles)
   before or during network attachment.

   For core IPv6 architectural contexts (6man), RSDGGS proposes a
   structured 64-bit spatial node identifier.  This document explores
   how this identifier can serve as a geographically anchored Interface
   Identifier (IID) within IPv6 addresses to enable geographic greedy
   routing in either an autonomous RF peer-aware network or low-power
   and lossy networks, while outlining key architectural considerations
   regarding address uniqueness, dynamic prefix updates, and location
   privacy.

   The grid is rooted in a spherical dodecahedron whose twelve
   pentagonal faces are aligned to approximate the three ITU Radio
   Regions, with face indices 1, 2, and 3 corresponding directly to ITU
   Regions 1, 2, and 3 respectively, with each face covering the most
   radio dense part of the ITU regions and spillover maping to bitmask
   appropriate representations - ie 5 & 9 for 1, 6 & 10 for 2, and 7 &
   11 for 3.  Each face is recursively subdivided using a hierarchy of
   isosceles golden gnomon triangles, with 2-bit child indices packed
   into successive octets.

   The system supports both fixed IoT deployments for automated
   regulatory provisioning during manufacturing and mobile IoT devices
   that acquire regulatory context through GPS, tethered devices, or
   peer-assisted discovery.  A beacon mechanism is defined whereby
   location-aware devices broadcast their RSDGGS index within ISM band
   transmissions, enabling location-unaware peers to derive applicable
   regulatory parameters including frequency allocation, power limits,
   duty cycle, dwell interval, channelization, and permitted modulation.

   For IETF protocols, this document defines a CBOR encoding of the
   index, requests a CBOR tag for it, and describes how the index is
   carried in IEEE 802.15.4 frames, the link layer for which 6LoWPAN was
   defined, so that a device can learn which channels and power levels
   it may use before it joins such a network.  It also outlines, as
   future work, the use of the index as an IPv6 Interface Identifier for
   geographic forwarding within 6LoWPAN and RPL meshes, and lists the
   privacy, address uniqueness, and prefix allocation issues that such
   use would have to resolve.
- **draft-havel-nmop-simap-features-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP Additional Features](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-features-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP) Additional Features, including optional graph
   navigation, lifecycle and external-link capabilities intended to be
   reusable with RFC 8345 topology models, including implementations
   using RFC 8795.
- **draft-havel-nmop-simap-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP Core Topology](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP) Core Topology.  It extends the RFC8345 YANG modules to
   support the subset of core SIMAP requirements.  This document will
   only focus on modelling proposal for each of the core SIMAP topology
   requirements not supported by RFC8345.  Any related terminology,
   concepts, use cases and requirements are defined outside of this
   draft and this draft will only refer to them, analyze how to model
   and propose the implementation solutions.
- **draft-hood-agtp-discovery-02** (new-draft, score 3, authorization) [none]: [AGTP Agent Discovery and Name Service](https://datatracker.ietf.org/doc/draft-hood-agtp-discovery/) — The Agent Transfer Protocol (AGTP) enables agents to communicate once
   they know each other's canonical identifiers.  This document
   specifies two layered mechanisms by which agents find each other and
   by which human-readable names resolve to Canonical Agent-IDs: the
   DISCOVER method, which queries for agents matching a capability
   description, and the Agent Name Service (ANS), which provides
   governed name-to-Agent-ID resolution.

   The architectural relationship is layered.  AGTP-Presence
   [AGTP-PRESENCE] provides ambient awareness of agents within
   visibility scopes as a substrate property.  DISCOVER operates over
   the Presence substrate to query the live population.  ANS provides
   human-readable name resolution, analogous to DNS for the web, with
   name authorities federating across organizational boundaries.  This
   document also introduces Anticipatory Discovery Services (ADS) as a
   forward-looking composition pattern where application-layer services
   preload agent awareness based on observed operational signals.

   DISCOVER and ANS together provide the application-layer interfaces
   for discovery and naming that compose with the substrate-level
   ambient discovery defined in [AGTP-PRESENCE].
- **draft-housley-lamps-rfc3161-update-02** (new-draft, score 3, adjacent_watchlist) [lamps]: [Update to the Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)](https://datatracker.ietf.org/doc/draft-housley-lamps-rfc3161-update/) — This document updates RFC 3161.  It adds a requirement to ensure that
   the id-ct-TSTInfo content type is used to align with the best
   practices for signed attributes with CMS signed-data.  In addition,
   cross-protocol attacks are prevented by requiring that the Time Stamp
   Authority (TSA) dedicate the signature key pair to the time-stamping
   service.  Finally, the use of id-kp-timeStamping in the TSA
   certificate is clarified.
- **draft-huitema-ccwg-c4-design-05** (new-draft, score 3, adjacent_watchlist) [none]: [Design of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-design/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  It pays special attention to
   the high jitter conditions encountered in Wi-Fi networks.  The design
   emphasizes simplicity and avoids making too many assumption about the
   "model" of the network.  The main control variables are the estimate
   of the data rate and of the maximum path delay in the absence of
   queues.
- **draft-huitema-ccwg-c4-spec-05** (new-draft, score 3, adjacent_watchlist) [none]: [Specification of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-spec/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design emphasizes
   simplicity and avoids making too many assumptions about the "model"
   of the network.
- **draft-ietf-acme-profiles-03** (new-draft, score 3, adjacent_watchlist) [acme]: [Automated Certificate Management Environment (ACME) Profiles Extension](https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/) — This document defines how an ACME Server may offer a selection of
   different certificate profiles to ACME Clients, and how those clients
   may indicate which profile they want.
- **draft-ietf-bpm-alt-mark-yang-00** (new-draft, score 3, adjacent_watchlist) [bpm]: [A YANG Data Model for the Alternate-Marking Method](https://datatracker.ietf.org/doc/draft-ietf-bpm-alt-mark-yang/) — Alternate-Marking Method is a technique used to perform packet loss,
   delay, and jitter measurements on in-flight packets.  This document
   defines a YANG data model for the Alternate-Marking Method.
- **draft-ietf-cbor-serialization-12** (new-draft, score 3, adjacent_watchlist) [cbor]: [CBOR Serialization and Determinism](https://datatracker.ietf.org/doc/draft-ietf-cbor-serialization/) — RFC 8949 defines CBOR, a standard for serializing data types such as
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
- **draft-ietf-ccamp-dwdm-if-param-yang-17** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG data model to manage configurable DWDM optical interfaces](https://datatracker.ietf.org/doc/draft-ietf-ccamp-dwdm-if-param-yang/) — This document defines a YANG model related to the Optical Transceiver
   parameters characterising coherent 100G and above interfaces.  100G
   and above Transceivers support coherent modulation, multiple
   modulation formats, multiple Forward Error Correction (FEC) codes
   including some not yet specified (or in phase of specification by)
   ITU-T G.698.2 or any other ITU-T recommendation.  Use cases are
   described in RFC7698.

   The YANG model defined in this document can be used for Optical
   Parameters monitoring and/or configuration of Dense Wavelength
   Division Multiplexing (DWDM) interfaces.  The use of this model does
   not guarantee interworking of DWDM transceivers.  Optical path
   feasibility and interoperability has to be determined by tools and
   algorithms outside the scope of this document.  The purpose of this
   model is to program interface parameters to consistently configure
   the mode of operation of transceivers.
- **draft-ietf-dkim-dkim2-spec-08** (new-draft, score 3, adjacent_watchlist) [dkim]: [DomainKeys Identified Mail Signatures v2 (DKIM2)](https://datatracker.ietf.org/doc/draft-ietf-dkim-dkim2-spec/) — DomainKeys Identified Mail v2 (DKIM2) permits a person, role, or
   organization that owns a signing domain to document that it has
   handled an email message by associating their domain with the
   message.  This is achieved by providing a hash value that has been
   calculated on the current contents of the message and then applying a
   cryptographic signature that covers the hash values and other details
   about the transmission of the message.  Verification is performed by
   querying an entry within the signing domain's DNS space to retrieve
   an appropriate public key.  As a message is transferred from author
   to recipient, systems that alter the body or header fields will
   provide details of their changes and calculate new hash values.
   Further signatures will be added to provide a "chain" that receivers
   can validate.  This permits verifiers to identify the nature of
   changes made by intermediaries and apply a reputation to the systems
   that made changes.  DKIM2 also allows recipients to detect when
   messages have been unexpectedly "replayed" and will ensure that
   Delivery Status Notifications are only sent to entities that were
   involved in the transmission of a message.
- **draft-ietf-dnsop-multi-alg-rules-00** (new-draft, score 3, adjacent_watchlist) [dnsop]: [Multiple Algorithm Rules in DNSSEC](https://datatracker.ietf.org/doc/draft-ietf-dnsop-multi-alg-rules/) — This document restates the requirements on DNSSEC signing and
   validation and makes small adjustments in order to allow for more
   flexible handling of configurations that advertise multiple Secure
   Entry Points (SEP) with different signing algorithms via their DS
   record or trust anchor set.  The adjusted rules allow both for multi-
   signer operation and for the transfer of signed DNS zones between
   providers, where the providers support disjoint DNSSEC algorithm
   sets.  In addition, the proposal enables pre-publication of a trust
   anchor in preparation for an algorithm rollover, such as of the root
   zone.

   This document updates RFCs 4035 and 6840.
- **draft-ietf-httpbis-connect-tcp-17** (new-draft, score 3, adjacent_watchlist) [httpbis]: [Template-Driven HTTP CONNECT Proxying for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) — TCP tunneling using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this tunneling functionality has several
   important deficiencies due to the lack of a well-defined HTTP origin
   or path.  This specification defines an alternative HTTP proxy
   service configuration for TCP connections.  This configuration is
   described by a URI Template, similar to the CONNECT-UDP and CONNECT-
   IP protocols.
- **draft-ietf-idr-bgp-model-23** (new-draft, score 3, adjacent_watchlist) [idr]: [YANG Model for Border Gateway Protocol (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/) — This document defines a YANG data model for configuring and managing
   BGP, including protocol, policy, and operational aspects, such as
   RIB, based on data center, carrier, and content provider operational
   requirements.
- **draft-ietf-idr-flowspec-srv6-11** (new-draft, score 3, core_identity) [idr]: [BGP Flow Specification for SRv6](https://datatracker.ietf.org/doc/draft-ietf-idr-flowspec-srv6/) — This document specifies extensions to BGP Flow Specification (BGP-FS)
   to enable filtering of IPv6 packets based on the structural
   components of a standard SRv6 Segment Identifier (SID) or an SRv6
   Compressed SID (CSID) container present in the IPv6 Destination
   Address (representing the active segment of an SRv6 path).  Both
   NEXT-CSID and REPLACE-CSID flavors defined in RFC 9800 are supported.
- **draft-ietf-intarea-arp-yang-model-02** (new-draft, score 3, adjacent_watchlist) [intarea]: [A YANG Data Model for ARP Extensions](https://datatracker.ietf.org/doc/draft-ietf-intarea-arp-yang-model/) — This document defines a YANG data model for the management of the
   Address Resolution Protocol (ARP).  It extends the basic ARP
   functionality contained in the ietf-ip YANG data model, defined in
   RFC 8344, to provide management of optional ARP features and
   statistics.
- **draft-ietf-ipsecme-pq-hybrid-auth-00** (new-draft, score 3, core_identity) [ipsecme]: [Use of Composite Signatures in IKEv2](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-pq-hybrid-auth/) — A Cryptographically Relevant Quantum Computer (CRQC) can break
   traditional public-key algorithms (e.g., RSA, ECDSA), which are
   typically used for authentication in IKEv2.  Combining the post-
   quantum ML-DSA signature algorithm with a traditional signature
   algorithm provides protection against potential weaknesses or
   implementation flaws in ML-DSA.  This draft defines a hybrid PKI
   authentication method for IKEv2 using composite certificates that
   ensures authentication remains secure as long as at least one of the
   component signature algorithms remains unbroken.
- **draft-ietf-jmap-metadata-05** (new-draft, score 3, core_identity) [jmap]: [JMAP Object Metadata](https://datatracker.ietf.org/doc/draft-ietf-jmap-metadata/) — This document defines an extension to the JSON Meta Application
   Protocol (JMAP) that lets clients and servers attach metadata to
   objects of existing JMAP data types.  Each data type the server lists
   gains two new properties, metadata and privateMetadata, whose values
   are objects keyed by _namespace identifier_. A namespace identifier
   is either a name registered with IANA or a domain name controlled by
   the vendor providing the namespace; the latter allows vendors and
   applications to extend the metadata schema without prior
   coordination.  Because metadata is carried as a property on the
   related object, clients use the existing /get, /set, /changes, and
   /query methods to read, modify, and synchronize it.
- **draft-ietf-lamps-certdiscovery-04** (new-draft, score 3, adjacent_watchlist) [lamps]: [A Mechanism for X.509 Certificate Discovery](https://datatracker.ietf.org/doc/draft-ietf-lamps-certdiscovery/) — This document specifies a method to discover a referenced X.509
   certificate associated with the current X.509 certificate.  This
   enables efficient multi-certificate or fallback certificate handling
   in protocols.  The objective is threefold: to enhance cryptographic
   agility, improve operational availability, and accommodate multi-key/
   certificate usage.  The proposed method aims to maximize
   compatibility with existing systems and is designed to be legacy-
   friendly, making it suitable for environments with a mix of legacy
   and new implementations.  It includes mechanisms to provide a URI
   from which the referenced X.509 certificate can be retrieved as well
   as information about the target certificate's signature and public
   key algorithm, empowering relying parties to make informed decisions
   on whether to retrieve the Referenced Certificate, and a certificate
   hash to ensure that the correct certificate was retrieved.
- **draft-ietf-lamps-cms-frodokem-00** (new-draft, score 3, adjacent_watchlist) [lamps]: [Use of FrodoKEM in the Cryptographic Message Syntax](https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-frodokem/) — FrodoKEM is a quantum-resistant key encapsulation mechanism (KEM)
   based on the standard Learning With Errors (LWE) problem，standardized
   by ISO.  FrodoKEM offers multiple parameter sets, with the
   recommended sets for general use including (e)FrodoKEM-976-AES and
   (e)FrodoKEM-976-SHAKE for security level 3, and (e)FrodoKEM-1344-AES
   and (e)FrodoKEM-1344-SHAKE for security level 5.  This document
   specifies the conventions for using FrodoKEM in the Cryptographic
   Message Syntax (CMS), using the KEMRecipientInfo structure defined in
   "Use of Key Encapsulation Mechanism (KEM) Algorithms in the
   Cryptographic Message Syntax (CMS)" [RFC9629].
- **draft-ietf-lamps-frodokem-certificates-00** (new-draft, score 3, adjacent_watchlist) [lamps]: [Internet X.509 Public Key Infrastructure - Algorithm Identifiers for FrodoKEM](https://datatracker.ietf.org/doc/draft-ietf-lamps-frodokem-certificates/) — FrodoKEM is an unstructured lattice-based Key Encapsulation Mechanism
   (KEM).  Compared to ML-KEM, FrodoKEM is considered as having more
   conservative design.  This document specifies the conventions for
   using FrodoKEM in X.509 Public Key Infrastructure.  The conventions
   for the subject public keys and private keys are also specified.
- **draft-ietf-lamps-one-signature-certs-04** (new-draft, score 3, adjacent_watchlist) [lamps]: [One Signature Certificates](https://datatracker.ietf.org/doc/draft-ietf-lamps-one-signature-certs/) — This document defines the signedDocumentBinding certificate
   extension, which binds a certificate to the signed content of a
   single digital signature.  Each certificate is created at the time of
   signing; the associated signing key is generated for the sole purpose
   of producing that one signature, is used for no other purpose, and is
   destroyed immediately afterwards.  Certificates carrying this
   extension are intended to be issued without a revocation mechanism
   and with no expiration, which simplifies long-term validation.
- **draft-ietf-lisp-yang-26** (new-draft, score 3, adjacent_watchlist) [lisp]: [LISP YANG Model](https://datatracker.ietf.org/doc/draft-ietf-lisp-yang/) — This document describes a YANG data model to use with the Locator/ID
   Separation Protocol (LISP).  This model can be used to configure and
   monitor the different control plane and data plane elements that
   enable a LISP network.

   The YANG modules in this document conform to the Network Management
   Datastore Architecture (NMDA) defined in [RFC8342].
- **draft-ietf-lsr-isis-pics-l2member-attr-yang-04** (new-draft, score 3, adjacent_watchlist) [lsr]: [YANG Data Model for IS-IS L2 Bundle Member Link Attributes PICS](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-pics-l2member-attr-yang/) — The YANG model in this document is to query an IS-IS Protocol
   Implementation Conformance Statement (PICS) of advertising Layer 2
   Bundle Member Link Attributes.
- **draft-ietf-lsr-isis-pics-srmpls-yang-04** (new-draft, score 3, adjacent_watchlist) [lsr]: [YANG Data Model for IS-IS Segment Routing MPLS PICS](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-pics-srmpls-yang/) — The YANG model in this document is to query an IS-IS Protocol
   Implementation Conformance Statement (PICS) of Segment Routing on
   MPLS data plane.
- **draft-ietf-lsr-isis-pics-yang-04** (new-draft, score 3, adjacent_watchlist) [lsr]: [YANG Model for IS-IS Protocol Implementation Conformance Statement (PICS)](https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-pics-yang/) — The YANG model in this document is to be used to query an IS-IS
   Protocol Implementation Conformance Statement (PICS).
- **draft-ietf-masque-http-datagram-compression-02** (new-draft, score 3, adjacent_watchlist) [masque]: [Extensions to Compress and Derive Fields in HTTP Datagrams](https://datatracker.ietf.org/doc/draft-ietf-masque-http-datagram-compression/) — This document defines extensions for HTTP Datagram-based protocols
   that improve transmission efficiency by introducing templates for
   compressing or deriving datagram fields.

   These templates allow endpoints to define parts of datagrams that are
   static and can be removed, and other parts that can be derived (such
   as packet lengths and checksum values).

   Additionally, this document defines a checksum offload procedure
   enabling receivers to complete Internet checksums using sender-
   provided partial values.

   These optimisations reduce per-packet overhead and processing cost.
   Compression can allow larger original packets to fit in QUIC DATAGRAM
   frames, depending on the applicable processing context and path
   maximum transmission unit (MTU).
- **draft-ietf-netconf-list-pagination-15** (new-draft, score 3, adjacent_watchlist) [netconf]: [List Pagination for YANG-driven Protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination/) — In some circumstances, instances of YANG modeled "list" and "leaf-
   list" nodes may contain numerous entries.  Retrieval of all the
   entries can lead to inefficiencies in the server, the client, and the
   network in between.

   This document defines a model for list pagination that can be
   implemented by YANG-driven management protocols such as NETCONF and
   RESTCONF.  The model supports paging over optionally filtered and/or
   sorted entries.  The solution additionally enables servers to
   constrain query expressions on some "config false" lists or leaf-
   lists.
- **draft-ietf-netconf-notif-envelope-07** (new-draft, score 3, adjacent_watchlist) [netconf]: [Extensible YANG Model for YANG-Push Notifications](https://datatracker.ietf.org/doc/draft-ietf-netconf-notif-envelope/) — This document defines a new extensible Notification structure,
   defined in YANG, for use in YANG-Push Notification messages, both for
   NETCONF and RESTCONF, enabling any YANG-compatible encodings such as
   XML, JSON, or CBOR.  Additionally, it defines two essential
   extensions: an extension to this structure supporting a hostname and
   a sequence number, and an extension to the YANG-Push Notifications
   supporting a timestamp characterizing the moment when the data was
   observed.
- **draft-ietf-netmod-yang2-01** (new-draft, score 3, adjacent_watchlist) [netmod]: [The YANG 2.0 Data Modeling Language](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang2/) — YANG is a data modeling language used to model configuration data,
   operational state data, Remote Procedure Calls, and notifications for
   network management protocols.  This document describes the syntax and
   semantics of version 2.0 of the YANG language.  YANG version 2.0 is a
   major release of the YANG language, addressing issues found in the
   original specification.
- **draft-ietf-ntp-ntpv5-10** (new-draft, score 3, adjacent_watchlist) [ntp]: [Network Time Protocol Version 5](https://datatracker.ietf.org/doc/draft-ietf-ntp-ntpv5/) — The Network Time Protocol (NTP) is a widely deployed protocol that
   allows hosts to obtain the current time of day from time servers.
   This document specifies version 5 of the protocol (NTPv5), which
   adopts a client-server model as its sole mode of operation.  Legacy
   operational modes supported in earlier versions have been removed to
   improve protocol robustness and clarity.  While this specification
   defines the protocol used for time distribution, it does not define
   the algorithms or heuristics employed by clients to determine or
   adjust their local time.
- **draft-ietf-pce-stateful-pce-autobw-update-06** (new-draft, score 3, adjacent_watchlist) [pce]: [Update to the Automatic Bandwidth Adjustment Procedure for MPLS-TE and SR-TE LSPs with a Stateful PCE](https://datatracker.ietf.org/doc/draft-ietf-pce-stateful-pce-autobw-update/) — Extensions for the stateful PCE model enable control of Traffic
   Engineering (TE) LSPs using the Path Computation Element
   Communication Protocol (PCEP) for RSVP-TE and Segment Routing (SR),
   for both PCE-initiated and PCC-initiated LSPs.

   RFC 8733 defines PCEP extensions for automatically adjusting
   bandwidth on MPLS-TE Label Switched Paths (LSPs) using a stateful
   PCE.  This document applies the PCEP extensions for automatic
   bandwidth adjustment to SR-TE LSPs in both the MPLS (SR-MPLS) and
   IPv6 (SRv6) data planes.  It also extends automatic bandwidth
   adjustment to multipath LSPs using the extensions defined in draft-
   ietf-pce-multipath.

   RFC 8733 defines the AUTO-BANDWIDTH-ATTRIBUTES TLV and a set of sub-
   TLVs for the attributes.  A sub-TLV is included when its value
   differs from the value last sent in a PCEP message.  However, RFC
   8733 lacks a mechanism to explicitly remove an attribute identified
   by a sub-TLV.  This document updates RFC 8733 by defining such a
   mechanism.
- **draft-ietf-radext-epcs-02** (new-draft, score 3, core_identity) [radext]: [RADIUS attributes for National Security and Emergency Preparedness Service](https://datatracker.ietf.org/doc/draft-ietf-radext-epcs/) — This document defines RADIUS attributes for authorizing the use of
   Emergency Preparedness Communication Service (EPCS) priority access
   defined in IEEE 802.11be.  These attributes allow an Identity
   Provider to indicate that an authenticated user is authorized for
   EPCS, enabling the Wi-Fi network provider to apply EPCS priority
   access to the user's Wi-Fi session.  The attributes also support
   RADIUS accounting for Wi-Fi sessions in which EPCS priority access is
   used.
- **draft-ietf-spring-stamp-srpm-mpls-13** (new-draft, score 3, core_identity) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the MPLS Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-mpls/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document specifies procedures for
   performance measurement in SR-MPLS networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   SR-MPLS paths, including Segment Lists of SR-MPLS Policies, SR-MPLS
   IGP best paths, and SR-MPLS IGP Flexible Algorithm (Flex-Algo) paths,
   as well as Layer-3 and Layer-2 services carried over those paths.

   This document updates RFC 8972 for the definition of the STAMP
   session identifier for SR-MPLS.
- **draft-ietf-spring-stamp-srpm-srv6-10** (new-draft, score 3, core_identity) [spring]: [Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing over the IPv6 (SRv6) Data Plane](https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm-srv6/) — Segment Routing (SR) can be used to steer packets through a network
   employing source routing.  SR can be applied to both MPLS (SR-MPLS)
   and IPv6 (SRv6) data planes.  This document describes the procedures
   for performance measurement in SRv6 networks using the Simple Two-Way
   Active Measurement Protocol (STAMP), as specified in RFC 8762, along
   with its optional extensions specified in RFC 8972 and the SR-
   specific extensions specified in RFC 9503.  These procedures measure
   links and SRv6 paths including Segment Lists of SRv6 Policies, SRv6
   IGP best paths, and SRv6 IGP Flexible Algorithm (Flex-Algo) paths, as
   well as Layer-3 and Layer-2 services carried over those paths.

   This document updates RFC 8972 for the definition of the STAMP
   session identifier for SRv6.
- **draft-ietf-tcpm-tcp-ao-algs-09** (new-draft, score 3, core_identity) [tcpm]: [Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO](https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/) — RFC 5926 established a registry of cryptographic algorithms that can
   be used with TCP-AO.  This document expands that registry, adding two
   Message Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 of the 40 bytes available for TCP options.
- **draft-irtf-cfrg-bbs-blind-signatures-05** (new-draft, score 3, adjacent_watchlist) [cfrg]: [Blind BBS Signatures](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-blind-signatures/) — This document defines an extension to the BBS Signature scheme that
   supports blind digital signatures, i.e., signatures over messages not
   known to the Signer.
- **draft-irtf-cfrg-bbs-signatures-14** (new-draft, score 3, adjacent_watchlist) [cfrg]: [The BBS Signature Scheme](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/) — This document describes the BBS Signature scheme, a secure, multi-
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
- **draft-jiang-anima-traffic-management-in-aidc-01** (new-draft, score 3, ai_infrastructure) [none]: [The Use Case of Autonomic Traffic Management in the Artificial Intelligence Data Center](https://datatracker.ietf.org/doc/draft-jiang-anima-traffic-management-in-aidc/) — This document describes the use case of autonomic traffic management
   in Artificial Intelligence Data Centers (AIDCs), including the
   associated management requirements and challenges.  It discusses two
   representative approaches based on the ANIMA architecture:
   distributed autonomic traffic management and controller-led hybrid
   traffic management.
- **draft-lin-opsawg-ipfix-rocev2-02** (new-draft, score 3, ai_infrastructure) [none]: [Export of RoCEv2 Base Transport Header (BTH) Information Using IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-rocev2/) — This document defines a new set of IP Flow Information Export (IPFIX)
   Information Elements (IEs) for exporting Base Transport Header (BTH)
   information for Remote Direct Memory Access (RDMA) over Converged
   Ethernet version 2 (RoCEv2) traffic.  These extensions enable network
   monitoring systems to collect and analyze the characteristics of RDMA
   traffic widely used in high-performance computing, storage, and
   artificial intelligence applications.
- **draft-liu-bpm-aspa-verification-benchmarking-00** (new-draft, score 3, authorization) [none]: [Benchmarking Methodology for ASPA Verification](https://datatracker.ietf.org/doc/draft-liu-bpm-aspa-verification-benchmarking/) — Autonomous System Provider Authorization (ASPA) provides a Resource
   Public Key Infrastructure (RPKI)-based mechanism for verifying the
   Border Gateway Protocol (BGP) AS_PATH attribute to detect route leaks
   and certain forms of AS_PATH manipulation.  The performance of ASPA-
   based AS_PATH verification depends on several factors, including the
   size and structure of ASPA data, AS_PATH characteristics,
   verification procedures, and the interaction between ASPA updates and
   BGP routing operations.  This document defines a benchmarking
   methodology for evaluating ASPA verification implementations on
   routing devices.  The methodology specifies controlled test
   conditions and procedures for measuring ASPA data processing, AS_PATH
   verification performance, route revalidation, BGP convergence,
   scalability, and resource utilization.  The objective is to provide
   repeatable and comparable measurements that characterize the
   performance and operational behavior of ASPA verification under
   varying conditions.
- **draft-liu-opsawg-ipfix-igp-algo-03** (new-draft, score 3, core_identity) [none]: [Export of IGP Algorithm Information in IPFIX](https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-igp-algo/) — This document introduces two IPFIX information elements (IEs) to
   identify the IGP Algorithm and Multi-Topology Identifier associated
   with the forwarding entry used for an observed packet.
- **draft-liu-sshm-kem-userauth-00** (new-draft, score 3, core_identity) [none]: [KEM-based User Authentication for SSH](https://datatracker.ietf.org/doc/draft-liu-sshm-kem-userauth/) — This document specifies publickey-kem, a Key Encapsulation Mechanism
   (KEM)-based user authentication method for the Secure Shell (SSH)
   protocol.  The server encapsulates a fresh shared secret to an
   authorized client public key.  The client demonstrates possession of
   the corresponding private key by returning a session-bound
   confirmation value.  The method does not modify SSH transport or
   server host authentication.  Initial authentication algorithm
   profiles using ML-KEM and HMAC-SHA256 are also specified.
- **draft-lx-srv6ops-srv6-rate-control-00** (new-draft, score 3, adjacent_watchlist) [none]: [SRv6-based Rate Control](https://datatracker.ietf.org/doc/draft-lx-srv6ops-srv6-rate-control/) — This document describes a deployment model and operational
   considerations for rate control in Segment Routing over IPv6 (SRv6)
   network slices.  It leverages a token-bucket scheduler to
   differentiate Committed Information Rate (CIR) and Peak Information
   Rate (PIR) traffic, and describes how a headend may enforce a rate
   profile on an SR Policy and adjust the PIR based on network
   conditions.  It addresses the operational trade-off between resource
   utilization and congestion avoidance in over-committed slice
   deployments.
- **draft-martinez-itp-lifecycle-00** (new-draft, score 3, adjacent_watchlist) [none]: [Invoice Trust Protocol (ITP): Lifecycle Status and Payment Information](https://datatracker.ietf.org/doc/draft-martinez-itp-lifecycle/) — This document extends the core of the Invoice Trust Protocol (ITP)
   with commercial, tax, and payment statuses for invoices, a
   deterministic way for both parties to derive the same state from the
   status messages they exchange, payment information for the envelope
   core, and attestations for payment accounts.  Informative appendices
   relate ITP statuses to those of Peppol and of several national
   systems.
- **draft-mcguinness-oauth-resource-token-resp-04** (new-draft, score 3, authorization) [none]: [OAuth 2.0 Resource Parameter in Access Token Response](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-resource-token-resp/) — This specification defines a new parameter resource to be returned in
   OAuth 2.0 access token responses.  It enables clients to confirm that
   the issued token is valid for the intended resource.  This mitigates
   ambiguity and certain classes of security vulnerabilities such as
   resource mix-up attacks, particularly in systems that use the
   Resource Indicators for OAuth 2.0 specification [RFC8707].
- **draft-mih-sokolov-cose-deterministic-encodings-00** (new-draft, score 3, verifiable_claims) [none]: [Deterministic Encodings for COSE](https://datatracker.ietf.org/doc/draft-mih-sokolov-cose-deterministic-encodings/) — A COSE Hash Envelope signs the digest of a preimage, not the preimage
   itself.  When the preimage is the encoding of a structured value,
   such as a CBOR data item, and a verifier holds that value but not the
   bytes that were hashed, the verifier has to encode the value again,
   and the digest matches only if it applies the same deterministic
   encoding as the producer.  RFC 8949 describes more than one such
   encoding for the same content type, and the preimage content type
   does not identify which one was applied.  This document defines a
   COSE Hash Envelope protected-header parameter that identifies the
   encoding, and an IANA registry of deterministic encodings whose
   initial entry is the Core Deterministic Encoding Requirements of RFC
   8949.
- **draft-netana-netmod-yang-anydata-validation-00** (new-draft, score 3, adjacent_watchlist) [none]: [Validating anydata in YANG Library context](https://datatracker.ietf.org/doc/draft-netana-netmod-yang-anydata-validation/) — The YANG "anydata" statement carries data whose data model is not
   known when the module is designed.  This document defines the context
   that is needed to validate such content: the schema context, the
   "anydata" node, a schema anchor, and the datastore.  It describes how
   this context is obtained for the uses of "anydata" in IETF YANG
   modules, how the schema node of each node in the content is found,
   and which YANG constraints are checked.
- **draft-netana-nmop-message-broker-bmp-telemetry-msg-05** (new-draft, score 3, adjacent_watchlist) [none]: [BMP YANG Model for Network Telemetry Messages](https://datatracker.ietf.org/doc/draft-netana-nmop-message-broker-bmp-telemetry-msg/) — This document defines an extensible message schema in YANG to be used
   at BMP collectors to transform BMP messages into messages which are
   consumed by external systems such as Message Brokers.
- **draft-newbold-atp-aturi-01** (new-draft, score 3, core_identity) [none]: [The "at" Identifier Scheme](https://datatracker.ietf.org/doc/draft-newbold-atp-aturi/) — This document defines the "at" identifier scheme, which is used to
   reference accounts and data records in the Authenticated Transfer
   Protocol.
- **draft-nottingham-problem-header-00** (new-draft, score 3, adjacent_watchlist) [none]: [The Problem-Details HTTP Header Field](https://datatracker.ietf.org/doc/draft-nottingham-problem-header/) — This specification defines the Problem-Details HTTP header field,
   which carries a problem details object (RFC 9457) as a Structured
   Field.  Because the Structured Fields data model is more constrained
   than JSON's, it also defines a profile that problem types can opt
   into so that they can be serialised as a header.
- **draft-ochkas-cose-ascon-05** (new-draft, score 3, verifiable_claims) [none]: [Ascon-AEAD128 and Ascon-Hash256 for COSE](https://datatracker.ietf.org/doc/draft-ochkas-cose-ascon/) — This document describes CBOR Object Signing and Encryption (COSE)
   serialization with Ascon, a NIST standard for lightweight
   cryptography.

   In 2019, as a part of CAESAR competition, Ascon-128 and Ascon-128a
   were selected as the first choice for the lightweight authenticated
   encryption.  After, in 2023, National Institute of Standards and
   Technology (NIST) selected Ascon family of cryptographic algorithms
   to be the standard for lightweight cryptography.  In August 2025,
   NIST Special Publication 800-232 was released, defining Ascon-based
   lightweight cryptography standards for constrained devices.  This
   recognition makes it particularly interesting to enable using Ascon
   with COSE structures.
- **draft-ramadan-mboned-mcast-manifest-00** (new-draft, score 3, core_identity) [none]: [Signed Digest Manifests for Multicast Datagram Authentication](https://datatracker.ietf.org/doc/draft-ramadan-mboned-mcast-manifest/) — This document defines a format for authenticating UDP datagrams
   delivered over IP multicast without changing them.  The sender
   computes a digest over every datagram of a flow, places the digests
   of up to 37 datagrams in a fixed-layout record, signs the record with
   Ed25519 under a prefix that names the flow, and sends it on a second
   port of the same source and group immediately before the datagrams it
   covers, followed by a byte-identical twin.  A receiver verifies one
   signature per record, hashes each datagram once, and delivers a
   datagram only after its digest matches an entry of a verified record;
   it needs no return channel.  A well-known document supplies a flow's
   keys and parameters.  A Media over QUIC profile and a browser profile
   use the format.
- **draft-ramadan-moq-multicast-01** (new-draft, score 3, core_identity) [none]: [Multicast Delivery and Endpoint Discovery for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-multicast/) — This document specifies multicast delivery mechanisms and catalog-
   based endpoint discovery for Media over QUIC (MoQ).  It defines how
   MoQ sessions integrate with IP multicast (SSM, ASM), Automatic
   Multicast Tunneling (AMT), and TreeDN for scalable live streaming.
   The specification includes a multicast catalog extension for endpoint
   discovery and multi-path delivery across TV, mobile, and browser
   platforms.  All multicast delivery uses MPEG Media Transport Protocol
   (MMTP) packets, the same packet format used on MoQ QUIC streams and
   datagrams.  A manifest-based content-authentication profile protects
   multicast delivery.
- **draft-sheffer-tls-pq-hsts-00** (new-draft, score 3, adjacent_watchlist) [none]: [An HSTS-like Header for Secure PQ Migration](https://datatracker.ietf.org/doc/draft-sheffer-tls-pq-hsts/) — This document defines an HTTP response header field, Require-PQ-Auth,
   that instructs user agents to require a quantum-resistant certificate
   chain in subsequent connections.  This is a short-term, opt-in
   mechanism for HTTP origins to protect against legacy classical trust
   anchors.  It will become unnecessary when UAs remove these trust
   anchors.
- **draft-slutsky-homing-pigeon-00** (new-draft, score 3, authorization) [none]: [Homing Pigeon Message Protocol, Version 1](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon/) — This document specifies the Homing Pigeon message protocol, version
   1: signed JSON job and result objects exchanged over a transport
   binding.  On the email binding, a submitter sends one HMAC-SHA-384
   signed JSON object to a mailbox; a runner polls that mailbox,
   verifies the signature, executes the job, and returns a signed
   result; the other bindings carry the same objects unchanged.  The
   signature is the only authorization.  The job object is protected end
   to end by per-job AEAD encryption, a required part of the protocol:
   implementations MUST support it, the reference software sends
   encrypted by default, and a receiver refuses a cleartext job unless
   the operator has explicitly enabled cleartext acceptance — in the
   reference software, only by a command-line parameter.  The store-and-
   forward bindings open no inbound listener on the host that runs the
   job.

   The DTLS binding changes the binding and not the messages: the same
   signed objects travel inside a direct DTLS 1.3 session between the
   submitter and the runner.  It is a binding of version 1, not a new
   version of the protocol.  The shared secret is the session's external
   pre-shared key; key exchange is ephemeral-only, so sessions have
   perfect forward secrecy; and once the handshake has authenticated the
   submitter, the runner opens the session with a greeting that
   discloses a tiered, responder-chosen summary of its platform.  The
   binding opens an inbound listener on the runner's host and is off
   unless the owner enables it.  It is an addition, never a replacement:
   the store-and-forward bindings remain the ones every submitter can
   reach.
- **draft-slutsky-homing-pigeon-v2-00** (new-draft, score 3, adjacent_watchlist) [none]: [Homing Pigeon Message Protocol, Version 2: Determinations, Questions, and Shared Context](https://datatracker.ietf.org/doc/draft-slutsky-homing-pigeon-v2/) — This document specifies version 2 of the Homing Pigeon message
   protocol.  Version 2 is an addition to version 1 (draft-slutsky-
   homing-pigeon-00), not a replacement for it: every version 1 message
   keeps its meaning, and version 2 adds three messages and one
   mechanism on top of the version 1 exchange.

   The additions are a determination message, by which the runner tells
   the submitter what it expects a job to do before the job runs; a
   question message, by which a runner whose local decision machinery
   cannot answer a question itself asks that question instead; an answer
   message, by which any enabled holder of the shared secret replies;
   and context segments, signed fragments of local state that travel
   with these messages and with the version 1 result, so each side plans
   with the other's actual state in view.

   Version 2 is backwards compatible.  A version 1 runner never sends a
   version 2 message and is unaffected by this document.  A submitter
   that implements this document adapts to the protocol version the
   runner supports: faced with a version 1 runner, it submits version 1
   jobs and expects version 1 results, exactly as before.  There is no
   version negotiation and no handshake; the messages carry v, as in
   version 1, and each side acts on what it receives.

   The deployment that motivates version 2 is the constrained runner: a
   small host whose local decision machinery is deliberately
   deterministic and carries no language model.  Version 1 leaves such a
   runner alone with every question its deterministic machinery cannot
   answer.  Version 2 lets it ask.
- **draft-sun-ainetops-nma-lifecycle-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [NMA Lifecycle Management YANG Data Model](https://datatracker.ietf.org/doc/draft-sun-ainetops-nma-lifecycle-yang/) — Network Management Agents (NMAs) deployed in production networks
   require a consistent representation of lifecycle information for
   admission, operation, version replacement, and retirement.  This
   document defines the ietf-nma-lifecycle YANG data model, covering
   basic NMA information and configuration, lifecycle state, and event
   notifications.  The model provides a consistent lifecycle data
   structure for NMAs from different vendors.
- **draft-toutain-schc-rfc9363bis-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Static Context Header Compression (SCHC)](https://datatracker.ietf.org/doc/draft-toutain-schc-rfc9363bis/) — This document describes a YANG data model for the Static Context
   Header Compression (SCHC) compression and fragmentation Rules.

   This document formalizes the description of the Rules for better
   interoperability between SCHC instances either to exchange a set of
   Rules or to modify the parameters of some Rules.

   This document updates the SCHC data model defined in RFC 9363 to take
   into account the evolution of SCHC usages.  It introduces a flexible
   way to describe protocol options, such as the CoAP options, and
   includes the identifiers needed for the compression of ICMPv6 and
   features for the management of the Rules.
- **draft-watts-authorization-noncollapse-semantics-01** (new-draft, score 3, authorization) [none]: [Non-Collapse Semantics for Authorization, Evidence, and Execution State](https://datatracker.ietf.org/doc/draft-watts-authorization-noncollapse-semantics/) — Distributed authorization systems frequently combine observations,
   policy evaluations, evidence records, authorization decisions, and
   execution receipts.  Treating these different objects as
   interchangeable can create fail-open behavior, stale-authority bugs,
   and false claims of completion.

   This document defines non-collapse semantics: explicit typed
   transitions between observation, evidence, authorization, and
   execution state; fail-closed treatment of missing or indeterminate
   premises; and comparison rules for determining when heterogeneous
   representations agree on a declared invariant.  The document is
   informational and defines no new wire protocol.
- **draft-watts-research-artifact-provenance-01** (new-draft, score 3, trust_infrastructure) [none]: [Research Artifact Provenance and Corrigible Scientific State](https://datatracker.ietf.org/doc/draft-watts-research-artifact-provenance/) — This document describes a protocol-neutral pattern for content-
   addressed research artifacts, append-only evidence history, explicit
   epistemic classes, and corrigible active scientific state.  It
   separates byte integrity from numerical correctness, empirical
   adequacy, mechanism identification, and release authority.

Archive Status

   This RFCXML source is an archive working draft and is not represented
   as submitted, adopted, or endorsed by the IETF.
- **draft-watts-research-evidence-bundle-01** (new-draft, score 3, trust_infrastructure) [none]: [A Research Evidence Bundle JSON Envelope for Provenance and Replication Metadata](https://datatracker.ietf.org/doc/draft-watts-research-evidence-bundle/) — This document proposes an early-stage JSON envelope for exchanging
   research-evidence records containing claim status, evidence tier,
   source provenance, methods, falsifiers, replication status, artifact
   digests, and privacy review.  It is an individual design proposal,
   not an IETF consensus document.  Its intended contribution must be
   assessed against existing provenance and research-packaging
   specifications before further standardization work.
- **draft-watts-research-evidence-envelope-01** (new-draft, score 3, trust_infrastructure) [none]: [Research Evidence Envelope: A Provenance-Oriented Interchange Record](https://datatracker.ietf.org/doc/draft-watts-research-evidence-envelope/) — This informational scaffold sketches a versioned record for tracking
   scientific claims, source provenance, evidence classes, uncertainty,
   falsifiers, replication procedures, and artifact hashes.  It is not
   an IETF standard, has not undergone IETF review, and does not define
   a wire protocol.
- **draft-watts-research-intelligence-archive-01** (new-draft, score 3, trust_infrastructure) [none]: [Evidence-Bounded Research Intelligence Archives](https://datatracker.ietf.org/doc/draft-watts-research-intelligence-archive/) — This unsubmitted working draft defines an evidence-bounded archive
   profile for scientific and technical claims, sources, evidence tiers,
   falsifiers, tests, provenance, publication state, and integrity
   manifests.  The profile is designed to prevent archival or mechanical
   integrity from being misread as empirical validity, novelty, peer
   review, standards approval, or publication acceptance.  This file is
   an archival RFCXML working draft and has no IETF standing unless
   separately submitted.
- **draft-watts-unison-state-preservation-01** (new-draft, score 3, trust_infrastructure) [none]: [State-Preserving Exchange of Evaluation Evidence](https://datatracker.ietf.org/doc/draft-watts-unison-state-preservation/) — This unsubmitted working draft describes state-preservation semantics
   derived from UNISON-StateBench.  It separates value, epistemic
   status, provenance, and authority; defines a non-collapse rule for
   operational and epistemic transitions; and describes representation,
   contradiction, missing-evidence, authority, principal-isolation,
   tool-state, context-distance, and controlled-mutation evaluation
   families.  This file is an archival RFCXML working draft and is not
   an IETF submission.
- **draft-watts-verification-defect-quarantine-01** (new-draft, score 3, adjacent_watchlist) [none]: [Verification Defect Quarantine for Protocol Conformance Systems](https://datatracker.ietf.org/doc/draft-watts-verification-defect-quarantine/) — Protocol conformance systems commonly treat a published test vector
   as an oracle.  When the oracle itself is malformed, internally
   inconsistent, ambiguous, or arithmetically false, an implementation
   can be penalized for rejecting the defect or can be falsely promoted
   for reproducing it.  This document defines Verification Defect
   Quarantine (VDQ), a transport-neutral receipt and fail-closed state
   model for separating the status of the tested subject from the
   demonstrated fault-detection behavior of the verifier.  VDQ records
   reproducible counterexamples, quarantines affected normative vectors
   from assurance promotion, preserves INDETERMINATE when a defect
   cannot yet be reproduced, and supports append-only supersession when
   a specification is corrected.  VDQ does not amend an Internet-Draft
   or RFC, does not replace the RFC Editor errata process, and does not
   by itself establish implementation security.
- **draft-watts-verification-promotion-boundaries-01** (new-draft, score 3, authorization) [none]: [Verification Promotion Boundaries for Protocol Implementations](https://datatracker.ietf.org/doc/draft-watts-verification-promotion-boundaries/) — Protocol implementations frequently combine specification checks,
   deterministic test vectors, security testing, independent
   reproduction, and release decisions.  A common failure mode is
   evidence collapse: a result at one assurance level is silently
   treated as sufficient for a stronger conclusion.  This document
   defines Verification Promotion Boundaries (VPB), a machine-readable
   profile and state-transition procedure that separates specification
   validation, local conformance, independent reproduction, authorized
   security testing, and release eligibility.  VPB also defines dual-
   state handling for specification defects: detecting a bad normative
   vector is negative evidence about the tested subject but may be
   positive fault-detection evidence about the verifier.  Unknown
   evidence never promotes.  This document does not define a new
   cryptographic primitive, authorization protocol, or IETF
   certification program.
- **draft-watts-veriflow-evidence-envelope-01** (new-draft, score 3, trust_infrastructure) [none]: [Veriflow Evidence Envelope for Source-Grounded Computational Claims](https://datatracker.ietf.org/doc/draft-watts-veriflow-evidence-envelope/) — This document specifies an experimental, JSON-based evidence envelope
   for exchanging source-grounded computational assertions, including
   provenance, reproducible operation identifiers, evidence sufficiency,
   and explicit abstention when an answer is not supported.  The
   envelope separates syntactic validity, source integrity, mathematical
   correctness, and empirical truth.  This document does not standardize
   a general scientific inference engine or claim experimental
   superiority.
- **draft-wobbly-dispatch-embedded-answers-00** (new-draft, score 3, adjacent_watchlist) [none]: [DNS Embedded Answers](https://datatracker.ietf.org/doc/draft-wobbly-dispatch-embedded-answers/) — Many web interactions require a client to resolve a hostname before
   it can establish a connection to a service.  While DNS is generally
   efficient, each lookup incurs some delay and exposes information
   about the user's browsing activity to the recursive resolver and
   upstream infrastructure.  This document explores techniques by which
   a client may receive DNS-derived address data as part of an
   application-layer response, so that it can initiate a connection
   without performing a separate DNS lookup for the same target.

   The mechanisms discussed here are intended to reduce lookup latency
   and potentially improve privacy, but they also raise significant
   questions about trust, freshness, and security.  The document does
   not prescribe a single normative mechanism; instead, it describes
   several design options and the trade-offs associated with each.
- **draft-wu-idr-flowspec-yang-cfg-04** (new-draft, score 3, adjacent_watchlist) [idr]: [A YANG Data Model for Flow Specification](https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-yang-cfg/) — This document defines a YANG data model for Flow Specification
   implementations.  The data model includes configuration data and
   state data.
- **draft-xie-dkim-sm2-sm3-00** (new-draft, score 3, core_identity) [none]: [DomainKeys Identified Mail (DKIM) Signatures with SM2 and SM3 Cryptographic Algorithms](https://datatracker.ietf.org/doc/draft-xie-dkim-sm2-sm3/) — This document adds the SM2-SM3 signing algorithm to DomainKeys
   Identified Mail (DKIM).  It defines the signature and public key
   encodings and the SM2 user identifier used with this algorithm.  This
   document updates RFC 6376.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Comments on this individual Internet-Draft are welcome.  Please send
   feedback to the authors using the contact information at the end of
   this document.
- **draft-xu-opsawg-ipfix-buffer-snapshot-00** (new-draft, score 3, core_identity) [none]: [IPFIX Export of Buffer Snapshots](https://datatracker.ietf.org/doc/draft-xu-opsawg-ipfix-buffer-snapshot/) — This document specifies an IP Flow Information Export (IPFIX) profile
   for exporting buffer occupancy snapshots.  It separates the number of
   objects selected for acquisition, the number successfully captured,
   and the number of distinct object records validated by a collector.
   A capture span bounds the temporal separation of the reported
   measurements.

   The profile defines ten Information Elements, object identity and
   accounting rules, and an ordered export procedure in which final
   metadata closes a snapshot.  The resulting collector procedure uses
   bounded state and distinguishes partial acquisition from incomplete
   delivery.  It does not define a buffer implementation, a trigger
   configuration protocol, or a congestion control algorithm.
- **draft-xu-rtgwg-resilient-nexthop-group-yang-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Resilient Next-Hop Groups](https://datatracker.ietf.org/doc/draft-xu-rtgwg-resilient-nexthop-group-yang/) — This document defines a YANG data model for configuring and observing
   resilient next-hop groups.  A fixed bucket table separates flow
   hashing from member selection.  The model augments the routing
   management model with shared groups, static route bindings, weighted
   bucket targets, restoration policies, and forwarding-confirmed
   operational state.

   The specification defines distinct quota and reference restoration
   policies, consistent timer semantics, and an administrative rebalance
   action protected by a state-generation precondition.  It standardizes
   management behavior for this class of implementation; it does not
   define a new routing protocol, hash algorithm, or transport ordering
   guarantee.
- **draft-yang-opsawg-pfc-queue-telemetry-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for PFC Queue Telemetry](https://datatracker.ietf.org/doc/draft-yang-opsawg-pfc-queue-telemetry/) — This document defines a YANG data model for completed, per-queue
   observations of backlog and received Priority-based Flow Control
   (PFC) gating.  Each record identifies a monotonic measurement
   interval, queue mapping epoch, measurement method, and absolute error
   bound.  The model makes repeated reads, missing coverage, and
   weighted aggregation explicit.

   The measured overlap does not identify the sole cause of queueing
   delay and does not change PFC, packet scheduling, or ECN marking.
   The module augments interface operational state and defines no
   configuration or notification interface.
- **draft-yang-rtgwg-ecn-threshold-policy-00** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for ECN Threshold Policies](https://datatracker.ietf.org/doc/draft-yang-rtgwg-ecn-threshold-policy/) — This document defines administrative limits and operational state for
   local ECN threshold adaptation on queues using a single byte-based
   Random Early Detection (RED) profile.  It augments the QoS queue
   template model with policy bounds and the interface model with
   confirmed per-queue state.

   The policy constrains both RED thresholds, preserves the configured
   ramp width, and specifies quantization, input validity, transition,
   and fallback behavior.  It does not select a learning algorithm,
   modify ECN codepoints, reserve physical buffer capacity, or guarantee
   congestion-control stability or lossless delivery.
- **draft-yanteri-humancollab-statements-00** (new-draft, score 3, agent_identity) [none]: [Accountable Statements Between AI Agents, Businesses and People](https://datatracker.ietf.org/doc/draft-yanteri-humancollab-statements/) — AI agents increasingly act on information they cannot check: what a
   business can supply, what a person said, what rules a platform
   applies.  This document describes a minimal way to make such
   statements accountable.  Every statement is signed by its author,
   bound where possible to a domain the author controls, and sealed in a
   public append-only Merkle log whose tree heads are signed,
   timestamped and publicly monitored.  The design proves who said what
   and when, and that the record was not rewritten.  It deliberately
   does not attempt to prove that a statement is true.
- **draft-yoon-ippm-collection-interval-capabilities-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Performance Monitoring (PM) Interval Capabilities](https://datatracker.ietf.org/doc/draft-yoon-ippm-collection-interval-capabilities/) — This document defines a YANG data model, "ietf-pm-interval-
   capabilities", that enables a server to advertise which sampling and
   collection intervals, measurement methods, and collection types it
   supports for each performance monitoring (PM) parameter.  A client
   reads this capability information before configuring PM collection,
   so that it selects only values that the server can honour.  The
   capabilities are advertised by augmenting the "ietf-system-
   capabilities" module defined in [RFC9196], so that a client discovers
   them at the same well-known location used for subscription and
   notification capabilities.  The model imports the "profile-names" and
   "collection-type" types and the "performance-parameter" and
   "measurement-method" identities from the companion PM collection
   model defined in [I-D.yoon-ippm-collection-measure] and mirrors its
   profile-and-parameter structure, ensuring direct alignment between
   capability discovery and collection configuration.  The model does
   not define collection data structures or any delivery mechanism;
   those are defined in the companion document.
- **draft-yoon-ippm-collection-measure-01** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for Performance Monitoring (PM) Collection](https://datatracker.ietf.org/doc/draft-yoon-ippm-collection-measure/) — This document specifies a YANG data model for the collection of
   Performance Monitoring (PM) data, based on the collection
   requirements of the performance management function defined in ITU-T
   G.7710.  The model processes raw performance data sampled at a
   network node and produces structured data that can be retrieved by
   clients via pull-based mechanisms or delivered via push-based
   mechanisms such as YANG-Push.  This document does not define new
   performance metrics; the base metrics are those of the IPPM
   framework, and the model specifies the collection and exposure of the
   operationally important subset.
- **draft-zz-scone-rate-advice-rocev2-01** (new-draft, score 3, adjacent_watchlist) [none]: [SCONE-Based Rate Advice for RoCEv2 Networks](https://datatracker.ietf.org/doc/draft-zz-scone-rate-advice-rocev2/) — This document describes the applicable scenarios of the Standard
   Communication Protocol for Network Elements (SCONE) in RoCEv2
   networks.  SCONE defines a mechanism that enables network elements on
   the forwarding path to deliver throughput guidance to RoCEv2
   endpoints.  This document further specifies the method for carrying
   Rate Advice in RoCEv2 networks.  The Rate Advice is generated by
   network nodes (e.g., switches), which can be either rate limits
   defined by network policies or quantitative rate adjustment
   recommendations derived from network status information.

   This document specifies two implementation solutions with different
   granularities.  Solution 1 provides path-granularity (source-IP-
   based) Rate Advice through out-of-band UDP messages sent directly
   from network elements to senders; a single advised rate applies to
   all active Queue Pairs (QPs) originating from the same source IP,
   providing sub-RTT feedback.  Solution 2 provides per-flow (per-QP)
   Rate Advice through an on-path Rate Signal with endpoint feedback,
   reusing the RoCEv2 data path and following the feedback loop model of
   the SCONE protocol; each QP receives its own advised rate.
- **draft-adams-milter-protocol-00** (new-draft, score 2, ignored_after_review) [none]: [The Mail Filter (milter) Protocol](https://datatracker.ietf.org/doc/draft-adams-milter-protocol/) — This document specifies the "milter" protocol, a binary request/
   response protocol by which a Mail Transfer Agent (MTA) can delegate
   inspection and modification of an SMTP transaction to one or more
   external filtering processes.
- **draft-andesco-otpauth-uri-01** (new-draft, score 2, ignored_after_review) [none]: [The otpauth URI Scheme: One-Time Password (OTP) Credential Provisioning](https://datatracker.ietf.org/doc/draft-andesco-otpauth-uri/) — This document defines syntax and processing rules for the otpauth:
   URI scheme used to provision one-time-password (OTP) credentials
   (verification codes) for HOTP and TOTP.

   This document defines a common baseline for interoperability,
   including issuer handling rules that improve account matching while
   maintaining compatibility with existing deployments.  It does not
   preclude future extensions for other OTP methods.
- **draft-apple-cfrg-vdaf-preamble-00** (new-draft, score 2, ignored_after_review) [none]: [The PREAMBLE VDAF](https://datatracker.ietf.org/doc/draft-apple-cfrg-vdaf-preamble/) — This document describes PREAMBLE, a two-party Verifiable Distributed
   Aggregation Function (VDAF) for secure aggregation where each client
   holds a large-dimensional vector that is _block-sparse_, meaning it
   is divided into fixed-size blocks of which at most one is nonzero,
   and that nonzero block itself satisfies a specified Fully Linear
   Proof (such as multihot, or a bounded L1 or L2 norm).
- **draft-calabria-bpm-ai-fabric-inference-bench-00** (new-draft, score 2, adjacent_watchlist) [none]: [Benchmarking Methodology for AI Inference Serving Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bpm-ai-fabric-inference-bench/) — This document defines benchmarking terminology, methodologies, and
   Key Performance Indicators (KPIs) for evaluating Ethernet-based AI
   inference serving network fabrics.  As Large Language Model (LLM)
   inference deployments scale to disaggregated prefill/decode
   architectures spanning hundreds or thousands of accelerators (GPUs/
   XPUs), the interconnect fabric determines Time to First Token (TTFT),
   Inter-Token Latency (ITL), and aggregate throughput in tokens per
   second (TPS).  This document establishes vendor-independent,
   reproducible test procedures for benchmarking fabric-level
   performance under realistic AI inference workloads.

   Coverage includes RDMA-based KV cache transfer between disaggregated
   prefill and decode workers, Mixture-of-Experts (MoE) expert
   parallelism AllToAll communication, request routing and load
   balancing for inference serving, congestion management under bursty
   inference traffic patterns, and scale/soak testing.  The methodology
   enables direct comparison across NIC transport stacks (RoCEv2 and
   UET) and fabric architectures.

   This document is a companion to the AI training fabric benchmarking
   methodology, which addresses training workloads.
- **draft-calabria-bpm-ai-fabric-terminology-00** (new-draft, score 2, ignored_after_review) [none]: [Benchmarking Terminology for AI Network Fabrics](https://datatracker.ietf.org/doc/draft-calabria-bpm-ai-fabric-terminology/) — This document defines benchmarking terminology for evaluating
   Ethernet-based network fabrics used in distributed Artificial
   Intelligence (AI) training and inference workloads.  It consolidates
   and extends terms from "Benchmarking Terminology for Network
   Interconnect Devices" (RFC 1242) and "Data Center Benchmarking
   Terminology" (RFC 8238).  Definitions cover collective communication
   primitives, RDMA transport mechanisms (RoCEv2 and Ultra Ethernet
   Transport), congestion control behaviors, AI-specific Key Performance
   Indicators (KPIs), and fabric topology concepts.

   This document is a companion to the AI training and inference fabric
   benchmarking methodology documents.  Those documents are intended to
   be read together with the terminology defined here.  Where
   definitions herein overlap with the foundational benchmarking
   terminology in RFC 1242 or RFC 8238, this document provides AI fabric
   context extensions and refinements; the foundational definitions in
   those RFCs remain authoritative for general network benchmarking.
- **draft-cgfabk-nmrg-ibn-generative-ai-03** (new-draft, score 2, ignored_after_review) [none]: [Generative AI for Intent-Based Networking](https://datatracker.ietf.org/doc/draft-cgfabk-nmrg-ibn-generative-ai/) — This document describes how to specialize AI models in order to offer
   a scalable, efficient path to creating highly targeted generative
   models for Intent-Based Networking.
- **draft-chang-agentproto-context-interaction-00** (new-draft, score 2, ignored_after_review) [none]: [Agent Context Interaction Optimizations](https://datatracker.ietf.org/doc/draft-chang-agentproto-context-interaction/) — The context distribution is important in a multi-agent system, which
   will impact the execution latency, token consumption, and task
   completion success rate, especially in a complex and multi-round
   workflow.

   This document specifies the scenarios and procedures of agent context
   distribution as well as the corresponding optimization during the
   procedures in order to provide precise control of the context
   distribution among the multiple agents.
- **draft-cheng-idr-ecmp-groupid-00** (new-draft, score 2, ignored_after_review) [none]: [BGP Extension for ECMP Group ID](https://datatracker.ietf.org/doc/draft-cheng-idr-ecmp-groupid/) — In AI training scenarios, per-flow ECMP is the mainstream load
   balancing technology.  However, hash collision issues lead to
   imbalanced traffic distribution, adversely affecting application
   performance.

   This document defines a new BGP Extended Community, BGP_EXT-COMM-
   ECMP-GROUPID, which carries an ECMP Group ID associated with a route.
   The ECMP Group ID allows an ingress router to map flows destined for
   different remote addresses to different local ECMP subgroups,
   providing finer-grained load distribution and resolving load
   imbalance caused by hash collisions.
- **draft-cheng-rtgwg-enhanced-ecmp-02** (new-draft, score 2, ignored_after_review) [none]: [Enhanced ECMP for AI Cluster](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/) — In AI training scenarios, the current mainstream load balancing
   technology is per-flow ECMP.  However, hash collision issues lead to
   imbalanced traffic distribution, adversely affecting application
   performance.

   To address this problem, this document proposes an enhanced ECMP
   method that resolves load imbalance caused by hash collisions.  The
   proposed solution effectively improves load balancing efficiency,
   reduces network congestion, and enhances overall network performance.
- **draft-das-ai-safety-radio-observation-consistency-00** (new-draft, score 2, authorization) [none]: [AI Safety for Radio Network Observation and Control Calculation Consistency](https://datatracker.ietf.org/doc/draft-das-ai-safety-radio-observation-consistency/) — Part 02 of 15 describes AI safety for distributed radio-access-
   network observation and control calculation consistency.  A radio
   controller may receive independently valid telemetry that is jointly
   unsuitable for the same calculation because it refers to different
   cell or beam identities, configuration generations, clock domains,
   acquisition intervals, measurement units, aggregation semantics, or
   shared upstream evidence.  This document develops A-CW-01 and six
   specialized procedures for source-qualified temporal consistency,
   resource reassignment, measurement transformation, dependency-aware
   observation selection, coupled multi-resource decisions, and
   controller failover.  It specifies evidence-scoped supported,
   contradicted, and unresolved outcomes, with revalidation after
   material state changes.  The result qualifies a calculation; it does
   not independently authorize modification of live radio resources.
   Companion Parts 01, 03, 04, 05, 11, and 14 address shared evidence
   semantics, network recovery, service state, hardware observations,
   migration, and optional protected effectuation boundaries.
- **draft-degennaro-mta-hooks-02** (new-draft, score 2, ignored_after_review) [none]: [Mail Transfer Agent (MTA) Hooks: An HTTP-Based Protocol for External Mail Processing](https://datatracker.ietf.org/doc/draft-degennaro-mta-hooks/) — This document specifies MTA Hooks, an HTTP-based protocol that lets
   Mail Transfer Agents (MTAs) delegate message processing decisions to
   external services.  The MTA sends a JSON or Concise Binary Object
   Representation (CBOR) description of the SMTP session, envelope, and
   message to a registered service at defined stages of reception and
   delivery.  The service answers with a JSON Patch that changes the
   description, and the MTA acts on the resulting state.  The same
   mechanism covers filtering at SMTP time, routing before delivery, and
   reacting to delivery outcomes, and the MTA controls exactly which
   changes each service may make.
- **draft-dong-fann-fc-cc-coordinate-00** (new-draft, score 2, ignored_after_review) [none]: [Use Case and Requirements for Flow Control and Congestion Control Coordination in WAN-based AI DC Interconnect](https://datatracker.ietf.org/doc/draft-dong-fann-fc-cc-coordinate/) — AI services are moving from single-site data center (DC) toward a
   multi-site distributed architecture.  This requires to provide high-
   throughput, lossless, and deterministic network connectivity for AI
   workloads that span Data Center Networks (DCNs) over the Wide Area
   Network (WAN).  Due to the long distance introduced by WAN, end-to-
   end congestion control across the DCN and WAN networks become a
   challenge, as the reaction time increases from microseonds to
   millisend level, which correspondingly increases the risk of packet
   loss both at the receiver side and in the network.  This document
   describes the use case of coordinated flow control and congestion
   control to minimize the packet loss in WAN-based AI DCI networks.
   The requirements on Fast Network Notifications (FANN) mechanisms in
   this scenario is also described.
- **draft-filsfils-srv6ops-srv6-ai-backend-06** (new-draft, score 2, ignored_after_review) [none]: [SRv6 for Deterministic Path Placement in AI Backends](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/) — This document describes how SRv6 NEXT-CSID enables deterministic path
   placement in AI backend fabrics through L3-L4 integration on end
   hosts: the transport stack on the NIC encodes each path as an ordered
   list of segments (a NEXT-CSID network program) in the packet header,
   while the fabric forwards statelessly.  It explains operational
   benefits including deterministic probing and alignment with
   hyperscale production deployments.
- **draft-he-agentproto-verifier-evidence-02** (new-draft, score 2, ignored_after_review) [none]: [Exercise and Completeness Evidence for Agent Protocol Verifier Results](https://datatracker.ietf.org/doc/draft-he-agentproto-verifier-evidence/) — A verifier result reports what a check returned.  It does not report
   whether the check could have returned anything else.  A check that
   inspects too narrow a set of fields, and a check whose rejecting or
   unverifiable input has never occurred, both report the same accepting
   value as a check that distinguishes, and a conformance matrix does
   not tell them apart.

   This document defines requirements for reporting whether a check has
   been exercised into its declared rejecting and unverifiable outcomes,
   and requirements for results that claim completeness: that the
   records relied on were the whole of some stated set.  Those are two
   separate obligations.  A result must name the set it claims to have
   seen, and must not treat a party with an interest in the answer as
   the only thing looking.

   This document defines no wire format, encoding, token, claim
   vocabulary, test harness, or registry.  It does require a record to
   identify certain facts.  That constrains what a record must be able
   to express and leaves its encoding open.  A profile satisfying these
   requirements will need a place to put those facts.
- **draft-hood-agtp-commerce-01** (new-draft, score 2, ignored_after_review) [none]: [AGTP-Commerce: Open Commerce Specification for Agent-to-Agent Transactions](https://datatracker.ietf.org/doc/draft-hood-agtp-commerce/) — This document specifies AGTP-Commerce, an open commerce specification
   for agent-to-agent transactions.  The specification defines the
   structural transaction information that the Agent Transfer Protocol
   carries between agents, allowing payment providers and commerce
   applications to compose at the application layer to perform the
   actual financial execution.

   AGTP-Commerce is to agent commerce what ISO 20022 is to inter-bank
   payment messaging: a standardized message format that allows
   heterogeneous payment infrastructure to interoperate.  AGTP-Commerce
   moves no money, holds no funds, and operates as no payment processor.
   The protocol carries pricing manifests, budget signaling, transaction
   commitments, and audit trail records that payment providers consume
   to execute settlement through existing financial infrastructure.

   This document specifies the pricing manifest format, extended Budget-
   Limit header semantics, the TRANSACT method for transaction
   commitment, audit-trail-based receipt records, dispute composition
   surfaces, and the integration patterns that allow payment providers
   (traditional processors, banks, cryptocurrency rails, and specialized
   agent-economy services) to compose with AGTP-Commerce as application-
   layer infrastructure.
- **draft-hood-agtp-methods-00** (new-draft, score 2, ignored_after_review) [none]: [AGTP Methods (AGTP Verbs): Method Vocabulary, Path Grammar, and Endpoints](https://datatracker.ietf.org/doc/draft-hood-agtp-methods/) — This document specifies AGTP-METHODS, the method vocabulary of the
   Agent Transfer Protocol (AGTP) [AGTP] and the contract layer built on
   it.  AGTP methods, also called AGTP verbs, are the action-intent
   words that name what a request does, in the same position that
   methods occupy in HTTP.  The document defines the properties a method
   may have, the eighteen-method floor every server implements, the
   registered catalog of methods beyond the floor (425 methods in nine
   categories at catalog version 1.0.0) with its versioned evolution and
   graceful deprecation, the path grammar that keeps method names out of
   paths, the endpoint primitive as the unit a server exposes, the
   semantic block carried by every endpoint, the server manifest, the
   per-server method policy, the three handler binding kinds, and the
   structural rejection codes 404, 405, 459, and 460.  Runtime contract
   negotiation, previously carried in the same document, is now
   specified in the companion AGTP-RCNS.  This document replaces
   [AGTP-API], which in turn superseded the AGIS and AGTP-Methods
   drafts.
- **draft-hood-agtp-rcns-00** (new-draft, score 2, ignored_after_review) [none]: [AGTP-RCNS: Runtime Contract Negotiation Substrate](https://datatracker.ietf.org/doc/draft-hood-agtp-rcns/) — This document specifies the Runtime Contract Negotiation Substrate
   (RCNS) for the Agent Transfer Protocol (AGTP) [AGTP]: the mechanism
   by which an AGTP server synthesizes an endpoint at runtime, from
   registered primitives, when a caller addresses a method and path pair
   the server has yet to register.  RCNS is invoked explicitly through
   the PROPOSE floor method and implicitly when a server is configured
   to treat unregistered requests as synthesis candidates.  The document
   defines the four-lock dispatcher gate that governs when synthesis may
   occur, the two contract delivery modes, the PROPOSE request and
   response body shapes, recipe versioning, contract scoping and
   lifecycle, the headers and rate-limiting contract, the Attribution-
   Record extension fields that make every invocation served under a
   contract attributable, and the inventory surfaces through which
   contracts are observed.  The material was previously carried in
   [AGTP-API], which this document and [AGTP-METHODS] together replace.
- **draft-hu-6man-ipv6-flowlabel-load-balancing-rdma-03** (new-draft, score 2, ignored_after_review) [none]: [A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) — This document proposes a method for achieving flow-level load
   balancing in RoCEv2 (RDMA over Converged Ethernet version 2)
   networks.  Traditional per-flow load balancing based on the 5-tuple
   cannot distinguish between different RDMA sessions that share the
   same 5-tuple.  This causes "elephant flows" to be hashed to the same
   path, leading to network congestion.  This method resolves this issue
   by having the ingress network device (e.g., a top-of-rack switch or
   router) parse the QP (Queue Pair) information from the IB BTH (Base
   Transport Header) and IB DETH (Datagram Extended Transport Header)
   headers of the RoCEv2 packet.  By combining this with portions of the
   IPv6 source and destination addresses as an entropy source, a CRC32
   hash algorithm generates a 20-bit value, which is then written into
   the Flow Label field of the IPv6 header.  Network devices can
   subsequently use the updated "5-tuple + Flow Label" for more granular
   flow-level load balancing, thereby effectively improving transmission
   efficiency in high-performance networks such as AI computing.
- **draft-ietf-cdni-delivery-metadata-04** (new-draft, score 2, ignored_after_review) [cdni]: [CDNI Delivery Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-delivery-metadata/) — This specification adds to the core set of configuration metadata
   defined in RFC8006, providing delivery metadata to define traffic
   types, request delegation behavior and CDN transport arrangements
   selection for a downstream CDN.
- **draft-ietf-deleg-13** (new-draft, score 2, ignored_after_review) [deleg]: [Extensible Delegation for DNS](https://datatracker.ietf.org/doc/draft-ietf-deleg/) — This document specifies a new extensible method for the delegation of
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
- **draft-ietf-dnsop-delext-13** (new-draft, score 2, ignored_after_review) [dnsop]: [DNS Protocol Modifications for Delegation Extensions](https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/) — The Domain Name System (DNS) protocol permits Delegation Signer (DS)
   records at delegation points.  This document specifies modifications
   to the DNS protocol to permit a range of Resource Record types at
   delegation points.  These modifications are designed to maintain
   compatibility with existing DNS resolution mechanisms and provide a
   secure method for processing these records at delegation points.

   This document updates RFCs 1034, 4035, 6672, 6840, 6895, and 9824.
- **draft-ietf-fann-problem-statement-01** (new-draft, score 2, ai_infrastructure) [fann]: [Fast Network Notifications Problem Statement](https://datatracker.ietf.org/doc/draft-ietf-fann-problem-statement/) — Many network applications, ranging from Artificial Intelligence (AI)
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
- **draft-jimenez-dawn-ard-initial-contact-00** (new-draft, score 2, ignored_after_review) [none]: [Agent Resource Discovery (ARD): Initial Contact](https://datatracker.ietf.org/doc/draft-jimenez-dawn-ard-initial-contact/) — In an agent system, agents need to discover other agents, tool
   servers, and skills.  Agent Resource Discovery (ARD) defines a
   manifest listing such resources and a lookup interface over it.  This
   document specifies how a client (such as an agent) initially
   discovers an ARD manifest.  This discovery is performed through the
   use of DNS Service Binding records, DNS-Based Service Discovery (DNS-
   SD), HTTP link relations, or well-known URIs.  Each mechanism yields
   a set of manifest URIs.  The manifest format, the lookup interface,
   and the binding of a manifest to its publisher are specified in the
   companion ARD documents.
- **draft-sun-ainetops-task-and-evidence-model-01** (new-draft, score 2, adjacent_watchlist) [none]: [Task and Evidence Information Model for AINETOps](https://datatracker.ietf.org/doc/draft-sun-ainetops-task-and-evidence-model/) — As Network Management Agents (NMAs) increasingly collaborate in
   scenarios such as fault diagnosis, network optimization, and service
   assurance, consistent task descriptions and evidence information are
   needed across vendors and management domains.  This document defines
   a Task and Evidence Information Model for AI-Enabled Network
   Operations (AINETOps).  The model consists of Task Core, Evidence
   Core, and a Profile extension mechanism for different task and
   evidence types.  This document does not specify communication
   protocols, request or response formats, task execution methods, or
   network configuration operations.
- **draft-watts-verifiable-scientific-evidence-records-02** (new-draft, score 2, ignored_after_review) [none]: [Verifiable Scientific Evidence Records: A Minimal Integrity Profile](https://datatracker.ietf.org/doc/draft-watts-verifiable-scientific-evidence-records/) — This document specifies a minimal JSON evidence-record profile for
   checking artifact digests and separating integrity verification from
   scientific assessment.  It defines an interoperable record structure,
   validation algorithm, and negative test cases.  It does not assert
   that an integrity-checked scientific claim is true.
- **draft-wnd-opsawg-icon-ps-01** (new-draft, score 2, ignored_after_review) [none]: [Problem Statement for Observability, Intervention and Control (I&C) in Multi-Agent Autonomous Networks](https://datatracker.ietf.org/doc/draft-wnd-opsawg-icon-ps/) — This document provides an overview of the issues associated with the
   deployment of the observability, intervention, and control of
   autonomous agent pipelines in large-scale heterogeneous network
   environments.  The term "Observability, Intervention and Control" is
   used to describe a set of automated and human-initiated mechanisms
   that guarantee the capability to observe, evaluate, constrain,
   correct, and terminate Autonomous agents at any point, for any
   reason, irrespective of their level of autonomy under which it
   operates, to ensure resilience, recovery, and operational continuity.

   The set of enabled observability, intervention and control reflects
   operator service offerings to ensure that autonomous network
   operations can be stopped, or safely redirected when required and is
   designed in conjunction with agent to agent, agent to tools, agent to
   human interaction and service and network policy.

   This document also identifies several key areas that the Agent
   Observability, Intervention and Control group will investigate to
   guide its architectural and protocol work and associated documents.
- **draft-xl-idr-bgp-sr-policy-pathrate-00** (new-draft, score 2, ignored_after_review) [none]: [BGP SR Policy for Path Rate](https://datatracker.ietf.org/doc/draft-xl-idr-bgp-sr-policy-pathrate/) — In AI/ML compute fabrics and data center interconnects, collective
   communication patterns (e.g., All-Reduce, All-to-All) generate
   microbursts that can saturate queuing buffers before reactive
   congestion control mechanisms take effect.  This document specifies a
   BGP SR Policy extension to carry Path Rate information (e.g., Path
   Committed Rate and Path Maximum Rate), enabling a central controller
   to compute and distribute per-segment-list rate limits along with the
   SR Policy Candidate Path.  The headend enforces these rate limits on
   traffic steered to the corresponding segment list, thereby
   proactively preventing the microburst-induced congestion before
   traffic enters the network.
- **draft-zhangb-cats-csma-implementation-03** (new-draft, score 2, ignored_after_review) [none]: [CATS C-SMA Nomination Snapshot and C-SMA-to-C-PS Transport Bindings](https://datatracker.ietf.org/doc/draft-zhangb-cats-csma-implementation/) — This document defines a nomination snapshot published by a CATS
   Service Metric Agent (C-SMA) to a CATS Path Selector (C-PS).  The
   snapshot carries aggregated service metrics together with a nominated
   service candidate set.

   The document defines the snapshot contract and two proposed transport
   bindings for the C-SMA-to-C-PS interface: a YANG-modeled snapshot
   delivered using gNMI for centralized C-PS deployments, and a BGP-LS
   service-metadata mapping for distributed deployments in which a C-PS
   is located at an ingress CATS-Forwarder.

   The SCI-to-C-SMA interface, individual metric definitions, management
   models, generic OAM, and the C-SMA's internal aggregation, ranking,
   and caching methods are outside the scope of this document.

## Ignored after review

- **draft-abraitis-idr-addpath-paths-limit-07** (new-draft, score 0, ignored_after_review) [none]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.

   This document also defines a new BGP Cease NOTIFICATION message
   subcode, "Maximum Number of Paths Reached", used when a BGP speaker
   terminates a peering because the number of paths received from a
   neighbor for a prefix exceeds the Paths Limit advertised in the
   PATHS-LIMIT Capability.
- **draft-adyta-mls-pq-00** (new-draft, score 0, ignored_after_review) [none]: [A Hybrid Post-Quantum KEM for the Messaging Layer Security (MLS) Protocol](https://datatracker.ietf.org/doc/draft-adyta-mls-pq/) — This document specifies a hybrid classical/post-quantum Key
   Encapsulation Mechanism (KEM) for use in the ratchet trees of the
   Messaging Layer Security (MLS) protocol.  Each parent node of the
   ratchet tree carries both a classical and a post-quantum public key,
   and a direct path update encapsulates to both.  The combiner binds
   both ciphertexts and both public keys, so that the derived node
   secret is pseudorandom if at least one of the two KEMs remains IND-
   CCA secure, including against an adversary that controls the keys and
   ciphertexts of the broken KEM.

   This document also specifies an optional asynchronous mode, in which
   fresh post-quantum output is produced only on designated rotation
   commits rather than on every commit.  Asynchronous mode trades a
   bounded delay in post-quantum post-compromise recovery for a
   reduction in post-quantum bandwidth proportional to the rotation
   interval.  Forward secrecy within the rotation window is retained by
   a one-way ratchet.

   This document is independent of the MLS Combiner draft, which
   achieves hybrid security by a different mechanism: running a pure
   post-quantum and a traditional MLS session in parallel and injecting
   a secret exported from the former into the latter as a pre-shared
   key.
- **draft-aggarwal-regext-rdap-irr-00** (new-draft, score 0, ignored_after_review) [none]: [RDAP Extension for Internet Routing Registry (IRR) Objects](https://datatracker.ietf.org/doc/draft-aggarwal-regext-rdap-irr/) — The Registration Data Access Protocol (RDAP) is used by Regional
   Internet Registries (RIRs) and Domain Name Registries (DNRs) to
   provide access to their resource registration information.  The core
   specifications for RDAP define core object types, but they do not
   contain objects for the Internet Routing Registry (IRR).  This
   document is intended to address this gap.
- **draft-alivar-6man-icmp-error-srv6-vpn-01** (new-draft, score 0, ignored_after_review) [none]: [ICMP Error Handling for VPNs in SRv6 Networks](https://datatracker.ietf.org/doc/draft-alivar-6man-icmp-error-srv6-vpn/) — The document specifies procedures for handling ICMP error messages in
   SRv6-based Virtual Private Network (VPN).  It describes three methods
   to improve the ICMP Error Handling for SRv6-VPNs.
- **draft-attoumani-ietf-inclusion-06** (new-draft, score 0, ignored_after_review) [none]: [The IETF is for Everyone: Toward Inclusive and Equitable Participation in Internet Governance](https://datatracker.ietf.org/doc/draft-attoumani-ietf-inclusion/) — Participation in the IETF remains very unevenly distributed across
   regions, and Africa is among the least represented.  This document
   argues that closing this gap is a shared responsibility and proposes
   a two-track approach.  Outside the IETF, universities, technical
   communities, Internet governance forums, and regional institutions in
   underrepresented regions need to demystify the IETF and bring
   academics, students, and young engineers toward its work.  Within the
   IETF, barriers to entry can be lowered further, and holding an IETF
   meeting in Africa would send a strong signal and act as a catalyst,
   meeting a local community prepared by the first track.  The document
   proposes concrete actions, indicative metrics, and next steps for
   both tracks.
- **draft-bashandy-rtgwg-segment-routing-uloop-19** (new-draft, score 0, ignored_after_review) [none]: [Loop avoidance using Segment Routing](https://datatracker.ietf.org/doc/draft-bashandy-rtgwg-segment-routing-uloop/) — This document presents a mechanism aimed at providing loop avoidance
in the case of IGP network convergence event.  The solution relies on
the temporary use of SR policies ensuring loop-freeness over the
post-convergence paths from the converging node to the destination.
- **draft-becker-cnsa2-smime-profile-06** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Secure/Multipurpose Internet Mail Extensions (S/MIME)](https://datatracker.ietf.org/doc/draft-becker-cnsa2-smime-profile/) — This document defines a base profile of S/MIME for use with the US
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
- **draft-becker-cnsa2-ssh-profile-07** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
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
- **draft-becker-cnsa2-tls-profile-06** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for TLS 1.3](https://datatracker.ietf.org/doc/draft-becker-cnsa2-tls-profile/) — This document defines a base profile of TLS 1.3 which is compliant
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
- **draft-beeram-mpls-rsvp-sr-01** (new-draft, score 0, ignored_after_review) [none]: [Signaling RSVP-TE Tunnels on an SR-MPLS Forwarding Plane Using Adjacency Segment Identifiers](https://datatracker.ietf.org/doc/draft-beeram-mpls-rsvp-sr/) — RFC 8577 introduced the concept of signaling RSVP-TE tunnels on a
   shared MPLS forwarding plane using preinstalled "TE link labels".
   Those labels are functionally equivalent to Segment Routing (SR)
   Adjacency Segment Identifiers (Adj-SIDs) but are allocated and
   distributed solely via RSVP-TE signaling.

   This document extends RFC 8577 so that RSVP-TE tunnels can use
   Segment Routing over MPLS (SR-MPLS) Adj-SIDs, as specified in RFC
   8402 and RFC 8660, in place of TE link labels.  It restricts scope to
   Adj-SIDs attached to a single unidirectional adjacency and defines
   the signaling procedures and protocol extensions required to couple
   the RSVP-TE control plane with the SR-MPLS data plane.
- **draft-besleaga-sustainability-wellknown-12** (new-draft, score 0, ignored_after_review) [none]: [The 'sustainability-data' Well-Known URI](https://datatracker.ietf.org/doc/draft-besleaga-sustainability-wellknown/) — This document defines the "sustainability-data" well-known URI, at
   which a web origin publishes a JSON document declaring the energy
   consumption, carbon footprint, and related environmental and
   sustainability metrics of a target: the organization behind the
   origin, the origin itself, a part of it, a service, a device, or a
   product, for different reporting periods.  The declaration links to a
   methodology and may carry a signature, name the declarations of
   upstream providers, and link to third-party attestations.  The
   metrics are self-asserted claims of the publisher.  This document
   registers the well-known URI and the media type application/
   sustainability-data+json.
- **draft-bider-ssh-server-algs-00** (new-draft, score 0, ignored_after_review) [none]: [Server-Led Algorithm Preference in the Secure Shell (SSH) Protocol](https://datatracker.ietf.org/doc/draft-bider-ssh-server-algs/) — This document specifies an optional extension to Secure Shell (SSH)
   algorithm negotiation.  A client and server can agree, through
   indicators in their SSH_MSG_KEXINIT messages, to use the server's
   algorithm preference order in place of the client's preference order.
   Agreement for one key exchange round does not carry forward to
   another round.  Agreement governs bilateral algorithm negotiations in
   SSH_MSG_KEXINIT, as well as connection-wide extension mechanisms,
   including SSH_MSG_EXT_INFO delayed compression.
- **draft-brand-indicators-for-message-identification-15** (new-draft, score 0, ignored_after_review) [none]: [Brand Indicators for Message Identification (BIMI)](https://datatracker.ietf.org/doc/draft-brand-indicators-for-message-identification/) — Brand Indicators for Message Identification (BIMI) permits Domain
   Owners to coordinate with Mail User Agents (MUAs) to display brand-
   specific Indicators next to properly authenticated messages.  There
   are two aspects of BIMI coordination: a scalable mechanism for Domain
   Owners to publish their desired Indicators, and a mechanism for Mail
   Transfer Agents (MTAs) to verify the authenticity of the Indicator.
   This document specifies how Domain Owners communicate their desired
   Indicators through the BIMI Assertion Record in DNS and how that
   record is to be interpreted by MTAs and MUAs.  MUAs and mail-
   receiving organizations are free to define their own policies for
   making use of BIMI data and for Indicator display as they see fit.
- **draft-brotman-ietf-bimi-guidance-16** (new-draft, score 0, ignored_after_review) [none]: [General Guidance for Implementing Branded Indicators for Message Identification (BIMI)](https://datatracker.ietf.org/doc/draft-brotman-ietf-bimi-guidance/) — This document is meant to provide guidance to various entities so
   that they may implement Brand Indicators for Message Identification
   (BIMI).  This document is a companion to various other BIMI drafts,
   which should first be consulted.
- **draft-bsvkey-dtn-custody-receipt-block-02** (new-draft, score 0, ignored_after_review) [none]: [Signed Custody Receipts Carried in a Bundle Protocol Version 7 Extension Block](https://datatracker.ietf.org/doc/draft-bsvkey-dtn-custody-receipt-block/) — This document defines the Custody Receipt Block, a Bundle Protocol
   Version 7 (BPv7) extension block that carries a chain of signed
   custody receipts inside the bundle those receipts describe.  Each
   node that chooses to act as a custodian appends one receipt stating
   that it held the bundle, which node it received it from, and when it
   received and forwarded it.  Nodes that do not implement the block
   forward it unchanged and are never required to read the payload or to
   sign anything.  A verifier holding the custodians' public keys can
   check the chain after the fact and can report, rather than infer, any
   part of the route for which no receipt exists.  The receipts are
   evidence for accounting and dispute resolution between operators.
   They are not Bundle Protocol administrative records and they do not
   replace or modify custody transfer signalling.
- **draft-callec-api-advisory-02** (new-draft, score 0, ignored_after_review) [none]: [A Well-Known URI for API Change Advisories](https://datatracker.ietf.org/doc/draft-callec-api-advisory/) — This document defines a well-known URI, /.well-known/api-
   advisory.json, at which API providers MAY publish a machine-readable
   JSON discovery file.  That file identifies the API and provides the
   URL of an Atom Syndication Format feed carrying structured change
   advisories.  The Atom feed enables automated scanners and API
   consumers to discover pricing changes, deprecations, security
   advisories, and other relevant events without relying on manual
   monitoring of blogs or mailing lists.  Advisory metadata is conveyed
   through a dedicated XML namespace defined in this document.
- **draft-chen-ipsec-problems-for-ntn-network-02** (new-draft, score 0, ignored_after_review) [none]: [IPsec Challenges in Non-Terrestrial Networks (NTN)](https://datatracker.ietf.org/doc/draft-chen-ipsec-problems-for-ntn-network/) — This document describes the problems in the use of IPsec in satellite
   Internet and NTN network scenarios.
- **draft-cheng-rtgwg-adaptive-routing-framework-06** (new-draft, score 0, ignored_after_review) [none]: [Adaptive Routing Framework](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-adaptive-routing-framework/) — In many cases, ECMP (Equal-Cost Multi-Path) flow-based hashing leads
   to high congestion and variable flow completion time.  This reduces
   applications performance.  Load balancing based on local link quality
   is not always optimal, A global view of congestion, with information
   from remote links, is needed for optimal balancing.  Adaptive routing
   is a technology that makes dynamic routing decision based on changes
   in traffic load and network topology.

   This document describes a framework for Adaptive Routing.
   Specifically, it identifies a set of adaptive routing components,
   explains their interactions, and exemplifies the workflow mechanism.
- **draft-cheng-spring-srpolicy-ar-framework-01** (new-draft, score 0, ignored_after_review) [none]: [SR-TE Path Based on Quality-Aware Dynamic Adaptive Adjustment](https://datatracker.ietf.org/doc/draft-cheng-spring-srpolicy-ar-framework/) — This document defines a framework for quality-aware dynamic adaptive
   adjustment of Segment Lists within an SR-TE Candidate Path.  It
   addresses the limitation of static weight assignment, which cannot
   adapt to dynamic changes in path quality (e.g., latency, loss,
   utilization).  The framework enables continuous monitoring of end-to-
   end metrics for each Segment List, computation of updated weights
   proportional to their relative quality, and application at the policy
   head-end.  This allows the Candidate Path to autonomously optimize
   traffic distribution towards higher-quality paths, enhancing
   performance without altering the SR-Policy architecture.
- **draft-choudhary-grow-bmp-bgp-msg-stats-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Message Counters for BGP Monitoring Protocol (BMP)](https://datatracker.ietf.org/doc/draft-choudhary-grow-bmp-bgp-msg-stats/) — The BGP Monitoring Protocol (BMP) [RFC7854] Statistics Report
   carries RIB occupancy, policy, and route-processing metrics.
   Some existing types count UPDATE messages, but only as special
   cases grouped by result (duplicates, loops, and errors).  No
   statistic gives a total count of each BGP message type.
   This document defines those totals as new BMP Statistics Types
   (UPDATE, KEEPALIVE, NOTIFICATION, ROUTE-REFRESH, and all BGP
   PDUs in each direction), states the operational use cases that
   motivate them, and records explicit non-goals so that last-error
   content, negotiated timer values, and implementation-specific
   internals remain out of scope.
- **draft-claise-opsawg-ipfix-ordered-ie-02** (new-draft, score 0, ignored_after_review) [none]: [Ordered Information Element Export in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/) — The IP Flow Information Export (IPFIX) protocol allows the same
   Information Element to appear multiple times in a Template Record.
   RFC 7011 states that multiple occurrences of the same Information
   Element SHOULD follow the logical order of their treatments by the
   Metering Process; however, no protocol mechanism exists for the
   Exporting Process to explicitly signal to the Collecting Process that
   this ordering is guaranteed.  Without such a guarantee, the
   Collecting Process cannot safely interpret repeated Information
   Elements as ordered observations.  This document describes the
   problem, presents use cases, analyzes candidate solutions, and
   specifies a mechanism -- a new Ordered Set type -- that establishes
   an end-to-end ordering guarantee: the Metering Process records
   repeated Information Element values in the order the corresponding
   observations are made, the Exporting Process preserves and signals
   this guarantee, and the Collecting Process interprets the n-th
   occurrence of an Information Element as corresponding to the n-th
   observation by the Metering Process at the Observation Point.  This
   document updates RFC 7011, RFC 5476, and RFC 6183.
- **draft-claise-opsawg-ipfix-ordered-mpls-ie-00** (new-draft, score 0, ignored_after_review) [none]: [Generic MPLS Information Elements for Ordered Export in IPFIX](https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-mpls-ie/) — This document defines new generic IPFIX Information Elements for MPLS
   label stacks and label attributes, intended for use with the ordered
   set mechanisms that provide an explicit ordering guarantee for
   repeated Information Elements.
- **draft-coffey-jmap-undelete-00** (new-draft, score 0, ignored_after_review) [none]: [JMAP Undelete: Recovering Destroyed Objects](https://datatracker.ietf.org/doc/draft-coffey-jmap-undelete/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) that lets a client find and restore objects that were
   permanently destroyed within a server-defined retention period.  It
   defines a new capability, a DeletedItem data type that describes a
   destroyed object of any supported data type, and a DeletedItem/
   restore method that recreates it.  Rules are given for Email,
   ContactCard, CalendarEvent, FileNode, and SieveScript objects.
   Servers can already keep destroyed data for a time.  This extension
   gives clients an interoperable way to show what can be recovered, for
   how long, and to recover it.
- **draft-czz-rtgwg-elastic-bandwidth-routing-01** (new-draft, score 0, ignored_after_review) [none]: [Elastic Bandwidth-aware Routing Framework](https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/) — IGP normally computes the shortest paths in a network for packet
   forwarding, without taking the traffic demands and available
   bandwidth into consideration.  When there is a link degradation or
   partial link failure in a network which causes throughput reduction,
   or the volume of specific traffic flows increase dramatically,
   unexpected congestion may happen if only the shortest paths are used
   for IP forwarding.

   Conventional centralized Traffic Engineering (TE) focuses on long-
   term bandwidth and routes planning based on traffic demands, which
   can not react to the congestions in networks timely.

   This document describes a distributed path computation and load
   balancing mechanism named Elastic Bandwidth-aware Routing (EBR),
   which can alleviate congestions timely before TE finishes the global
   optimization.  It allows IGP-enabled nodes which face congestion to
   distribute traffic among the shortest paths and load-balancing
   alternate paths through Segment Routing (SR) strict path, with
   weights determined based on the bandwidth utilization and available
   bandwidth of these paths.  It provides an efficient, accurate and
   backward compatible approach for dynamic link congestion avoidance.
- **draft-dogra-opsawg-ipfix-pfc-00** (new-draft, score 0, ignored_after_review) [none]: [IPFIX Information Elements for Priority-based Flow Control Telemetry](https://datatracker.ietf.org/doc/draft-dogra-opsawg-ipfix-pfc/) — Priority-based Flow Control (PFC) pauses Ethernet traffic by
   priority.  This document defines two IP Flow Information Export
   (IPFIX) Information Elements and an Options Template record pattern
   for per-priority totals of received and transmitted PFC control
   frames.
- **draft-dong-pcep-flowspec-srv6-00** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extension for SRv6 Flow Specification](https://datatracker.ietf.org/doc/draft-dong-pcep-flowspec-srv6/) — This document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) to support Flow Specification for
   Segment Routing over IPv6 (SRv6).  Building upon the PCEP Flow
   Specification framework defined in RFC 9168, this specification
   introduces new PCEP Flow Specification TLVs to enable filtering and
   steering of IPv6 packets based on the structural components of
   standard SRv6 Segment Identifiers (SIDs) or SRv6 Compressed SID
   (CSID) containers present in IPv6 Destination Addresses or Segment
   Routing Headers (SRH).
- **draft-eddy-scone-tcp-00** (new-draft, score 0, ignored_after_review) [none]: [SCONE TCP Option](https://datatracker.ietf.org/doc/draft-eddy-scone-tcp/) — This document describes a TCP option that permits network elements to
   provide TCP endpoints advice on rate limits within the network.  The
   functionality for TCP is analogous to SCONE packets within the QUIC
   protocol.
- **draft-eggert-appeal-support-02** (new-draft, score 0, ignored_after_review) [none]: [Requiring Support for Appealing to the IESG and IAB](https://datatracker.ietf.org/doc/draft-eggert-appeal-support/) — RFC2026 describes the procedure for appealing decisions or process
   failures to the IESG and the IAB.  This document updates RFC2026 and
   requires that an appellant must first gain support for their appeal
   before an appeal may be considered by the body it is submitted to.
- **draft-ezema-lookalike-sender-detection-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Detecting Look-Alike Sender Identities in Platform Messaging](https://datatracker.ietf.org/doc/draft-ezema-lookalike-sender-detection/) — Users of consumer platforms -- job boards, marketplaces, education
   and early-career services -- receive messages from other parties
   inside the platform, where no enterprise mail gateway inspects them.
   Attackers impersonate the platform's own brand and support staff, and
   pose as recruiters or counterparties, using look-alike domains and
   display names.  This document describes considerations for detecting
   look-alike sender identities at the level of the individual message
   and its sender, rather than at the domain-registration level.  It
   records two concrete pitfalls observed in deployed libraries: Unicode
   confusable "skeleton" equality alone does not catch all mixed-script
   look-alikes, and several input validators accept host names
   containing invisible format characters.  This document is
   informational and specifies no protocol.
- **draft-fedyk-netmod-yang-normal-form-01** (new-draft, score 0, ignored_after_review) [none]: [Extending Normalized Forms to String-Derived Types](https://datatracker.ietf.org/doc/draft-fedyk-netmod-yang-normal-form/) — YANG models frequently define identifiers using string or string-
   derived types whose lexical space permits multiple representations of
   the same underlying value.  This can lead to incorrect behavior when
   semantically equivalent values are compared lexically.

   This document adds an optional extension to the existing YANG concept
   of normalized form to string-derived types whose lexical space
   permits multiple representations of the same underlying value.
- **draft-fetch-validation-vmc-wchuang-12** (new-draft, score 0, ignored_after_review) [none]: [Fetch and Validation of Verified Mark Certificates](https://datatracker.ietf.org/doc/draft-fetch-validation-vmc-wchuang/) — A description of how entities wishing to validate a Verified Mark
   Certificate (VMC) should retrieve and validate these documents.
   This document is a companion to BIMI core specification, which should
   be consulted alongside this document.
- **draft-fizgeer-pce-lsp-validation-extensions-01** (new-draft, score 0, ignored_after_review) [none]: [PCE LSP validation Extensions in Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-fizgeer-pce-lsp-validation-extensions/) — The Path Computation Element Communication Protocol (PCEP) provides
   mechanisms for Path Computation Elements (PCEs) to instantiate and
   manage Label Switched Paths (LSPs) on a Path Computation Client
   (PCC).  A Stateful PCE RFC8231 can instantiate LSPs on a PCC.  In
   some cases, the PCC shall perform additional validations and/or
   actions.  If some validations or actions fail, the LSP will not be
   created and established or updated.  This document specifies PCEP
   extensions to handle this situation gracefully in case the problem
   can be resolved by some network changes (freeing up resources,
   restoring or changing the network, and so on).  This draft defines
   common usage of the new flag and known use cases for using this flag.
   Each draft relevant to LSP creation can add a corresponding bit to
   the use case list.
- **draft-fl-nmop-device-yang-vendor-mapping-00** (new-draft, score 0, ignored_after_review) [none]: [An Experiment: Mapping IETF Device YANG Models to Vendors](https://datatracker.ietf.org/doc/draft-fl-nmop-device-yang-vendor-mapping/) — This document describes an experimental implementation of a YANG to
   YANG translation function layer providing a northbound interface for
   configuring networking devices using a set of IETF 'device' YANG
   modules.  The southbound interface of the function implements the
   proprietary, vendor YANG modules which are implemented natively on
   devices to be configured.  The expected benefits of such an approach
   are the ability to provide a stable, standardised, and vendor/device
   agnostic interface for the configuration and maintenance of devices.
   The main purposes for this experiment is to validate the overall
   approach, and to identify, and describe the different YANG-to-YANG
   translation techniques that can be used.
- **draft-flentge-dtn-bpv7-custody-transfer-00** (new-draft, score 0, ignored_after_review) [none]: [Custody Transfer for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-flentge-dtn-bpv7-custody-transfer/) — This document defines custody transfer for Bundle Protocol Version 7.
   A Custody Transfer Extension Block is defined to request custody
   transfer of a bundle, and a Compressed Custody Signal in the form of
   an administrative record is used to report acceptance or rejection
   for multiple bundles.
- **draft-flentge-dtn-bundle-sequence-identification-00** (new-draft, score 0, ignored_after_review) [none]: [Bundle Sequence Identification for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-flentge-dtn-bundle-sequence-identification/) — This document defines compact sequence identifiers, ranges, and
   collections for referring to one or more Bundle Protocol Version 7
   bundles.  The mechanism supports efficient signaling and enables
   ordered reception, duplicate suppression, and gap detection.
- **draft-flentge-dtn-compressed-status-reporting-00** (new-draft, score 0, ignored_after_review) [none]: [Compressed Bundle Status Reporting for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-flentge-dtn-compressed-status-reporting/) — This document defines compact, aggregated status reporting for Bundle
   Protocol Version 7.  A Compressed Reporting Extension Block assigns
   sequence information and optionally requests reports, while a
   Compressed Reporting Signal reports events for multiple bundles.
- **draft-fujiwara-dnsop-ranking-data-02** (new-draft, score 0, ignored_after_review) [none]: [Clarifications to the DNS Ranking Data](https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-ranking-data/) — This document obsoletes Section 5.4.1 (Ranking data) of RFC 2181, and
   specifies directives whereby the source of the data determines for
   what purposes it may be used.
- **draft-gandhi-bpm-stamp-link-crc-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) Extension for Link CRC Error Measurement](https://datatracker.ietf.org/doc/draft-gandhi-bpm-stamp-link-crc/) — The Simple Two-Way Active Measurement Protocol (STAMP), specified in
   RFC 8762, supports active measurement of network performance.  This
   document defines a STAMP Type-Length-Value (TLV) that reports
   receive-side link statistics: packets received, packets received with
   Cyclic Redundancy Check (CRC) errors, and bytes received.  The link
   is identified using the Micro-session ID TLV specified in RFC 9534.
   These measurements support fiber-quality monitoring to provide SLA
   assurance.
- **draft-gandhi-ippm-stamp-udp-lite-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) over UDP-Lite](https://datatracker.ietf.org/doc/draft-gandhi-ippm-stamp-udp-lite/) — This document specifies the Simple Two-Way Active Measurement
   Protocol (STAMP) as defined in RFC 8762 and extended in RFC 8972,
   over the Lightweight User Datagram Protocol (UDP-Lite) for IPv4 and
   IPv6.  Partial checksum coverage accommodates timestamp insertion
   after the checksum computation while protecting the integrity of
   transport header and IP pseudo-header.

   This document updates RFC 8762 to permit an explicitly selected UDP-
   Lite transport with the existing UDP port number rules.

   This document also updates RFC 8972 for transport-aware session
   identification, payload length determination, UDP port number
   reporting in the Location TLV, and replacing the use of the UDP
   Length field for detecting optional STAMP TLVs.  STAMP payload
   formats and existing UDP-based sessions are unchanged.
- **draft-ginsberg-lsr-reliable-snp-00** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Reliable SNP](https://datatracker.ietf.org/doc/draft-ginsberg-lsr-reliable-snp/) — Complete Sequence Number PDUs (CSNPs) are exchanged as part of
   adjacency bringup on point-to-point interfaces.  However, this
   exchange is unreliable.  This document defines protocol extensions to
   support reliable exchange of CSNPs as well as optimizations to the
   encoding of advertisements in Sequence Number PDUs.
- **draft-gondwana-dkim2-debug-header-02** (new-draft, score 0, ignored_after_review) [none]: [A Diagnostic Header Field for DKIM2 Implementations](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-debug-header/) — Implementations of DomainKeys Identified Mail Signatures v2 (DKIM2)
   benefit from seeing extra debug information during the early
   deployment phase.

   This document is intended to help testers, and unlikely to be
   published.
- **draft-gong-sidrops-rtr-push-00** (new-draft, score 0, ignored_after_review) [none]: [Push Mode Extension for the RPKI to Router Protocol](https://datatracker.ietf.org/doc/draft-gong-sidrops-rtr-push/) — The Resource Public Key Infrastructure (RPKI) to Router Protocol
   (RTR) enables routers to receive validated RPKI data from Relying
   Parties (RPs).  This document defines a push mode extension for RTR
   that allows RPs to proactively push RPKI data updates to routers,
   either periodically or event-driven.
- **draft-grayson-5580uncertainty-01** (new-draft, score 0, ignored_after_review) [none]: [Carrying location objects with uncertainty in RADIUS](https://datatracker.ietf.org/doc/draft-grayson-5580uncertainty/) — This document describes a new location profile for use with the
   RADIUS Location-Data Attribute.  The new profile is used to carry a
   geospatial location profile that includes location uncertainty.
- **draft-gu-grow-bmp-route-leak-detection-07** (new-draft, score 0, ignored_after_review) [none]: [BMP for BGP Route Leak Detection](https://datatracker.ietf.org/doc/draft-gu-grow-bmp-route-leak-detection/) — According to Route-Leak Problem Definition [RFC7908], Route leaks
   refer to the case that the delivery range of route advertisements is
   beyond the expected range.  For many current security protection
   solutions, the ISPs (Internet Service Providers) are focusing on
   finding ways to prevent the happening of BGP [RFC4271] route leaks.
   However, the real-time route leak detection if any occurs is
   important as well, and serves as the basis for leak mitigation.  This
   document extends the BGP Monitoring Protocol (BMP) [RFC7854] to
   provide a routing security scheme suitable for ISPs to detect BGP
   route leaks at the prefix level.
- **draft-gupthaa-dtn-bpsec-source-binding-00** (new-draft, score 0, ignored_after_review) [none]: [Acceptor Source Binding for Bundle Protocol Security (BPSec)](https://datatracker.ietf.org/doc/draft-gupthaa-dtn-bpsec-source-binding/) — RFC 9172 Section 8.2.2 describes how a legitimate node can replace a
   source's Block Integrity Block (BIB) with one made under its own key,
   and how an acceptor that only checks that a BIB "was generated by a
   legitimate user" accepts the result.  This document specifies the
   acceptor-side condition that prevents this substitution in
   deployments with per-source keys: each required security service on a
   target block is bound to the security source that is authoritative
   for that block, and is not satisfied by a block from any other
   source, even an authorized one.  It also clarifies that the primary
   block is bound to a payload only through the integrity scope of the
   payload's own BIB, not through a separate BIB over the primary block.
- **draft-guthrie-cnsa2-ipsec-profile-05** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for IPsec](https://datatracker.ietf.org/doc/draft-guthrie-cnsa2-ipsec-profile/) — This document defines a base profile for IPsec for use with the US
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
- **draft-halpern-rtgwg-not-a-dump-truck-01** (new-draft, score 0, ignored_after_review) [none]: [The IGP is not a Dump Truck](https://datatracker.ietf.org/doc/draft-halpern-rtgwg-not-a-dump-truck/) — This document explores addressing the problem of using an IGP to
   carry arbitrary information, often referred to using the phrase "the
   IGP is not a dump truck".  It describes the kinds of information
   carried in an IGP and proposes an approach to changing the system.
- **draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext-01** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC with SigTag Extension](https://datatracker.ietf.org/doc/draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext/) — This document describes a mechanism to reduce post-quantum
   cryptographic (PQC) network transmission overhead when using Merkle
   Tree Ladders (MTL) in DNS Security Extensions (DNSSEC).  This
   document refers to this as SigTag and describes the use of EDNS(0) to
   enable its use.  SigTag allows a client to indicate its knowledge of
   a specific MTL ladder.  The DNS server can then use this signal to
   determine if it can omit the full underlying signature in its
   response, thereby reducing the message payload.
- **draft-hecker-dawn-intent-capability-gap-00** (new-draft, score 0, ignored_after_review) [none]: [The Intent-to-Capability Knowledge Gap in Discovery of Agents With Names](https://datatracker.ietf.org/doc/draft-hecker-dawn-intent-capability-gap/) — DAWN defines discovery as an initial step that returns minimum
   discoverable information (MDI) about entities.  Clients, however,
   usually start from an intent, not from a name or a capability, and
   the capabilities needed to satisfy an intent depend on what is
   available.  A client therefore has to know what is on offer to
   decide what to look for, and has to decide what to look for to learn
   what is on offer.

   This document describes that circular dependency, locates it in the
   current DAWN documents, compares five strategies for handling it,
   and lists questions for the Architecture work.  The main question is
   what the MDI must contain for a client to act without a pre-agreed
   capability vocabulary.  This document proposes no protocol.
- **draft-housley-asn1-layman-guide-05** (new-draft, score 0, ignored_after_review) [none]: [A Layman's Guide to a Subset of ASN.1, BER, and DER](https://datatracker.ietf.org/doc/draft-housley-asn1-layman-guide/) — This note gives a layman's introduction to a subset of the Abstract
   Syntax Notation One (ASN.1), Basic Encoding Rules (BER), and
   Distinguished Encoding Rules (DER).  The purpose of this note is to
   provide background material sufficient for understanding and
   implementing standards that make use of ASN.1.

   This memo is not an IETF standard, and has not been shown to have
   IETF community consensus.  This memo offers tutorial information.
- **draft-huitema-ccwg-c4-test-05** (new-draft, score 0, ignored_after_review) [none]: [Testing of Christian's Congestion Control Code (C4)](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-test/) — Christian's Congestion Control Code is a new congestion control
   algorithm designed to support Real-Time applications such as Media
   over QUIC.  It is designed to drive towards low delays, with good
   support for the "application limited" behavior frequently found when
   using variable rate encoding, and with fast reaction to congestion to
   avoid the "priority inversion" happening when congestion control
   overestimates the available capacity.  The design was validated by
   series of simulations, and also by initial deployments in control
   networks.  We describe here these simulations and tests.
- **draft-ietf-6lo-path-aware-semantic-addressing-16** (new-draft, score 0, ignored_after_review) [6lo]: [Path-Aware Semantic Addressing (PASA) for Low power and Lossy Networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-path-aware-semantic-addressing/) — This document specifies a topological addressing scheme, Path-Aware
   Semantic Addressing (PASA), that enables stateless IP packet
   forwarding.  The forwarding decision is based solely on the
   destination address structure.  This document focuses on carrying IP
   packets across an LLN (Low power and Lossy Network), in which the
   topology is quite static, the location of the nodes is fixed for long
   period of time, and the connection between the nodes is also rather
   stable.  This document specifies the PASA architecture, along with
   the PASA address allocation, forwarding mechanism, routing header
   format, and IPv6 interconnection support.
- **draft-ietf-6lo-schc-15dot4-14** (new-draft, score 0, ignored_after_review) [6lo]: [Transmission of SCHC-compressed packets over IEEE 802.15.4 networks](https://datatracker.ietf.org/doc/draft-ietf-6lo-schc-15dot4/) — A framework called Static Context Header Compression and
   fragmentation (SCHC) has been designed with the primary goal of
   supporting IPv6 over Low Power Wide Area Network (LPWAN) technologies
   [RFC8724].  One of the SCHC components is a header compression
   mechanism.  If used properly, SCHC header compression allows a
   greater compression ratio than that achievable with traditional
   6LoWPAN header compression [RFC6282].  For this reason, it may make
   sense to use SCHC header compression in some 6LoWPAN environments,
   including IEEE 802.15.4 networks.  This document specifies how a
   SCHC-compressed packet can be carried over IEEE 802.15.4 networks.
   The document also enables the transmission of SCHC-compressed UDP/
   CoAP headers over 6LoWPAN-compressed IPv6 packets.
- **draft-ietf-6man-ieee80211-dms-01** (new-draft, score 0, ignored_after_review) [6man]: [IPv6 issues with 802.11 multicast reliability remain](https://datatracker.ietf.org/doc/draft-ietf-6man-ieee80211-dms/) — For the IPv6 protocol stack, while IEEE 802.11 wireless networks can
   on a first abstraction be considered functionally identical to wired
   IEEE 802 networks, there are issues regarding reliability and
   survivability of multicast traffic.  The existence of these issues
   has been known for some time.  This document is to state that they
   are still being experienced, and summarize some previous and new
   approaches.

   Additionally, this document serves to collect consensus in the IETF
   process to make both the IEEE and Wi-Fi Alliance aware of these
   issues and request they be included in consideration for future
   development.  802.11 Directed Multicast Service and Flexible
   Multicast Service are noted as existing protocol features that may
   warrant more consideration.  However, other solutions in that space
   may be more appropriate and are left to the expertise of the IEEE and
   Wi-Fi Alliance.
- **draft-ietf-anima-constrained-grasp-04** (new-draft, score 0, ignored_after_review) [anima]: [Constrained GeneRic Autonomic Signaling Protocol](https://datatracker.ietf.org/doc/draft-ietf-anima-constrained-grasp/) — This document proposes the Constrained GeneRic Autonomic Signaling
   Protocol (cGRASP), a constrained and lightweight variant of the
   GeneRic Autonomic Signaling Protocol (GRASP, or the standard GRASP).
   cGRASP reduces message overhead and replaces TCP with CoAP as the
   transport protocol.  By leveraging CoAP's reliability features and
   deployment maturity, cGRASP can provide reliable signaling services
   without relying on TCP, making it suitable for IoT, where lightweight
   and resource-constrained devices dominate.  Furthermore, this
   document also discusses the potential approaches to adapting the
   cGRASP to work on the network without IP connectivity.
- **draft-ietf-anima-rfc8366bis-39** (new-draft, score 0, ignored_after_review) [anima]: [A Voucher Artifact for Onboarding Protocols](https://datatracker.ietf.org/doc/draft-ietf-anima-rfc8366bis/) — This document defines a strategy to securely assign a candidate
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
- **draft-ietf-asdf-sdf-nonaffordance-06** (new-draft, score 0, ignored_after_review) [asdf]: [Semantic Definition Format (SDF) Extension for Non-Affordance Information](https://datatracker.ietf.org/doc/draft-ietf-asdf-sdf-nonaffordance/) — This document describes an extension to the Semantic Definition
   Format (SDF) for representing non-affordance information of Things,
   such as physical, contextual, and descriptive metadata.  This
   extension introduces a new Class Name Keyword, sdfContext, that
   enables comprehensive modeling of Things and improves semantic
   clarity.
- **draft-ietf-avtcore-rtp-avatar-03** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for Avatar Representation Format (ARF) Animation Stream](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-avatar/) — This memo outlines RTP payload formats for the animation stream
   format as defined in the ISO/IEC 23090-39 standard (MPEG-I Avatar
   Representation Format), in the following referred to as ARF.  ARF is
   composed of Avatar Animation Units (AAU) including an AAU header and
   zero or more AAU packets.  The RTP payload header format allows for
   packetization of an AAU unit in an RTP packet payload as well as
   fragmentation of an AAU into multiple RTP packets.
- **draft-ietf-avtcore-rtp-vdmc-05** (new-draft, score 0, ignored_after_review) [avtcore]: [RTP Payload Format for V-DMC](https://datatracker.ietf.org/doc/draft-ietf-avtcore-rtp-vdmc/) — This memo outlines RTP payload formats for the Video-based Dynamic
   Mesh Coding (V-DMC), which comprises several types of components,
   such as a basemesh, AC-based displacements, 2D representations of
   attributes, and an atlas.  This document focuses on describing the
   basemesh and displacement, while the RTP payload formats for the
   atlas and attributes are addressed in other documents.  The RTP
   payload header formats enable the packetization of a basemesh or
   displacement Network Abstraction Layer (NAL) unit in an RTP packet
   payload as well as fragmentation of a NAL unit into multiple RTP
   packets.
- **draft-ietf-bess-evpn-dpath-05** (new-draft, score 0, ignored_after_review) [bess]: [Domain Path (D-PATH) for Ethernet VPN (EVPN) Interconnect Networks](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-dpath/) — The BGP Domain PATH (D-PATH) attribute is defined for Inter-Subnet
   Forwarding (ISF) BGP Sub-Address Families that advertise IP prefixes
   or MAC addresses.  D-PATH already applies to EVPN Route Type 2 when
   used for ISF, to EVPN Route Type 5 (IP Prefix routes), and to IP-VPN
   routes.  When used along with those routes, it identifies the
   domain(s) through which the routes have passed and that information
   can be used by the receiver BGP speakers to detect routing loops or
   influence the BGP best path selection.  This document extends the use
   of D-PATH to EVPN Route Type 2 when not used for ISF, to EVPN Route
   Type 1 (Ethernet Auto-Discovery per-EVI) for EVPN VPWS, and to EVPN
   Route Type 3 (Inclusive Multicast Ethernet Tag routes).
- **draft-ietf-bess-evpn-ip-aliasing-05** (new-draft, score 0, ignored_after_review) [bess]: [EVPN Support for L3 Fast Convergence and Aliasing/Backup Path](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-ip-aliasing/) — This document proposes an EVPN extension to allow several of its
   multi-homing functions, fast convergence, and aliasing/backup path,
   to be used in conjunction with inter-subnet forwarding.  The
   extension is limited to All-Active and Single-Active redundancy
   modes.
- **draft-ietf-bess-evpn-vpws-gateway-02** (new-draft, score 0, ignored_after_review) [bess]: [Ethernet VPN Virtual Private Wire Services Gateway Solution](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-vpws-gateway/) — Ethernet Virtual Private Network Virtual Private Wire Services (EVPN
   VPWS) need to be deployed in high scale multi-domain networks, where
   each domain can use a different transport technology, such as MPLS,
   VXLAN or Segment Routing with MPLS or IPv6 Segment Identifiers
   (SIDs).  While transport interworking solutions on border routers
   spare the border routers from having to process service routes, they
   do not always meet the multi-homing, redundancy, and operational
   requirements, or provide the isolation that each domain requires.
   This document analyzes the scenarios in which an interconnect
   solution for EVPN VPWS using EVPN Domain Gateways is needed, and adds
   the required extensions to support it.
- **draft-ietf-bpm-alt-mark-deployment-00** (new-draft, score 0, ignored_after_review) [bpm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-bpm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
- **draft-ietf-bpm-on-path-telemetry-yang-00** (new-draft, score 0, ignored_after_review) [bpm]: [On-Path Telemetry YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-bpm-on-path-telemetry-yang/) — This document defines two YANG data models for monitoring On-Path
   network performance information to be published in YANG
   notifications.  The Alternate-Marking Method and In-situ Operations,
   Administration, and Maintenance (IOAM) are the On-Path hybrid
   measurement methods considered in this document.
- **draft-ietf-bpm-stamp-ber-00** (new-draft, score 0, ignored_after_review) [bpm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Residual Bit Error Rate Measurement](https://datatracker.ietf.org/doc/draft-ietf-bpm-stamp-ber/) — The Simple Two-Way Active Measurement Protocol (STAMP), specified in
   RFC 8762, along with its optional extensions specified in RFC 8972,
   supports active measurement.  Networks may experience transmission
   bit errors due to various factors, including poor fiber quality.
   Even with efficient FEC and CRC mechanisms, some bit errors may
   escape detection and correction; these are referred to as residual
   bit errors.  This document further augments the STAMP extensions
   specified in RFC 8972 to enable the measurement of the residual bit
   error rate within the "Extra Padding" TLV of STAMP-Test packets.
- **draft-ietf-bpm-stamp-mpls-hdr-00** (new-draft, score 0, ignored_after_review) [bpm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet MPLS Network Action Headers](https://datatracker.ietf.org/doc/draft-ietf-bpm-stamp-mpls-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect MPLS Network Action Sub-Stacks and
   Post-Stack MPLS Headers for HBH and E2E active measurements, for
   example, using the IOAM data fields.
- **draft-ietf-calext-icalendar-jscalendar-extensions-09** (new-draft, score 0, ignored_after_review) [calext]: [iCalendar Format Extensions for JSCalendar](https://datatracker.ietf.org/doc/draft-ietf-calext-icalendar-jscalendar-extensions/) — This document defines a set of new elements for iCalendar and extends
   the use of existing ones.  Their main purpose is to extend the
   semantics of iCalendar with elements defined in JSCalendar, but the
   new definitions also aim to be useful within just the iCalendar
   format.  This document updates RFC 5545, RFC 7986, and RFC 9073.
- **draft-ietf-ccamp-fgotn-yang-03** (new-draft, score 0, ignored_after_review) [ccamp]: [YANG Data Models for fine grain Optical Transport Network](https://datatracker.ietf.org/doc/draft-ietf-ccamp-fgotn-yang/) — Fine grain Optical Transport Network (fgOTN) is a data plane
   technology, specified in ITU-T Recommendation G.709/Y.1331 (2020)
   Amd. 3, which complements existing OTN by providing bandwidth
   efficient support for sub-1Gbit/s services.

   This document defines YANG data models to describe the topology and
   tunnel information of an fgOTN network.
- **draft-ietf-cdni-edge-control-metadata-13** (new-draft, score 0, ignored_after_review) [cdni]: [Content Delivery Network Interconnection (CDNI) Edge Control Metadata](https://datatracker.ietf.org/doc/draft-ietf-cdni-edge-control-metadata/) — This specification defines configuration metadata objects used to
   manage how edge servers control access to resources within Content
   Delivery Networks (CDNs) and Open Caching systems.  A key feature of
   these configurations is the configuring of Cross-Origin Resource
   Sharing (CORS) access rules and the dynamic generation of CORS
   headers.  This specification also provides the ability to define
   response body compression rules and client connection timeouts.
- **draft-ietf-cellar-codec-21** (new-draft, score 0, ignored_after_review) [cellar]: [Matroska Media Container Codec Specifications](https://datatracker.ietf.org/doc/draft-ietf-cellar-codec/) — This document defines the Matroska multimedia container codec
   mappings, including the codec ID, layout of data in a Block element
   and in an optional CodecPrivate element.
- **draft-ietf-core-coap-bp-05** (new-draft, score 0, ignored_after_review) [core]: [Constrained Application Protocol (CoAP) over Bundle Protocol (BP)](https://datatracker.ietf.org/doc/draft-ietf-core-coap-bp/) — The Bundle Protocol (BP) was designed to enable end-to-end
   communication in challenged networks.  The Constrained Application
   Protocol (CoAP), which was designed for constrained-node networks,
   may be a suitable application-layer protocol for the scenarios where
   BP is used.  This document specifies how CoAP is carried over BP.
- **draft-ietf-diem-requirements-04** (new-draft, score 0, ignored_after_review) [diem]: [Digital Emblems - Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-diem-requirements/) — Digital emblems allow an issuer to signal that an asset should be
   protected or treated in a specific way, using some normative
   framework.  This document lists the requirements and use cases that
   an architecture for digital emblems must accommodate.
- **draft-ietf-dult-accessory-protocol-01** (new-draft, score 0, ignored_after_review) [dult]: [Detecting Unwanted Location Trackers Accessory Protocol](https://datatracker.ietf.org/doc/draft-ietf-dult-accessory-protocol/) — This document lists a set of best practices and protocols for
   accessory manufacturers whose products have built-in location-
   tracking capabilities.  By following these requirements and
   recommendations, a location-tracking accessory will be compatible
   with unwanted tracking detection and alerts on mobile platforms.
   This is an important capability for improving the privacy and safety
   of individuals in the circumstance that those accessories are used to
   track their location without their knowledge or consent.
- **draft-ietf-green-terminology-03** (new-draft, score 0, ignored_after_review) [green]: [Terminology for Energy Efficiency Network Management](https://datatracker.ietf.org/doc/draft-ietf-green-terminology/) — Energy-efficient network management is primarily meant to enhance
   conventional network management with energy-related management
   capabilities that optimize overall network energy consumption.  To
   that aim, specific features and capabilities are required to control
   (and thus optimize) the energy use of involved network elements and
   their components.

   This document defines a set of key terms used within the IETF when
   discussing energy efficiency in network management.  Such reference
   document helps framing discussion and agreeing upon a set of main
   concepts in this area.
- **draft-ietf-grow-bmp-over-quic-01** (new-draft, score 0, ignored_after_review) [grow]: [Using BMP over QUIC connection](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-over-quic/) — The BGP Monitoring Protocol (BMP) provides a convenient interface for
   obtaining route views by monitoring BGP sessions.  BMP operates over
   TCP and is unidirectional (from client to server).  QUIC provides
   multiple simultaneous streams to carry data in one direction,
   enabling much better efficiency and performance for both peers, in
   particular unidirectional streams can provide reverse data protection
   for the sender.  QUIC also provides shorter handshake and includes
   TLS.  This document describes how to use BMP over the QUIC transport
   protocol, named BMPoQUIC.
- **draft-ietf-grow-rpsl-registry-scoped-members-01** (new-draft, score 0, ignored_after_review) [grow]: [Registry scoped members for RPSL set objects](https://datatracker.ietf.org/doc/draft-ietf-grow-rpsl-registry-scoped-members/) — This document updates RFC2622 and RFC4012 by specifying src-members,
   a new attribute on as-set and route-set objects in the Routing Policy
   Specification Language (RPSL).  This attribute allows a specific
   registry to be defined for each member in a set, avoiding problematic
   ambiguity when resolving set members.  A new validation rule allows
   gradual upgrades and backwards compatibility.
- **draft-ietf-hpke-hpke-06** (new-draft, score 0, ignored_after_review) [hpke]: [Hybrid Public Key Encryption](https://datatracker.ietf.org/doc/draft-ietf-hpke-hpke/) — This document specifies a scheme for hybrid public key encryption
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
- **draft-ietf-ianabis-rfc7120bis-04** (new-draft, score 0, ignored_after_review) [ianabis]: [Early IANA Code Point Allocation](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc7120bis/) — This document describes the requirements for securing IANA code point
   assignments for IETF Stream Internet-Drafts and specifications being
   drafted by other standards-related organizations.  This document
   obsoletes RFC 7120.
- **draft-ietf-ianabis-rfc8126bis-04** (new-draft, score 0, ignored_after_review) [ianabis]: [Guidelines for Writing an IANA Considerations Section in RFCs](https://datatracker.ietf.org/doc/draft-ietf-ianabis-rfc8126bis/) — Many protocols make use of points of extensibility that use constants
   to identify various protocol parameters.  To ensure that the values
   in these fields do not have conflicting uses and to promote
   interoperability, their allocations are often coordinated by a
   central record keeper.  For IETF protocols, that role is filled by
   the Internet Assigned Numbers Authority (IANA).

   To make assignments in a given registry prudently, guidance
   describing the conditions under which new values should be assigned,
   as well as when and how modifications to existing values can be made,
   is needed.  This document defines a framework for the documentation
   of these guidelines by specification authors, in order to assure that
   the provided guidance for the IANA Considerations is clear and
   addresses the various issues that are likely in the operation of a
   registry.

   This is the fourth edition of this document; it obsoletes RFC 8126.
- **draft-ietf-idr-fsv2-ip-basic-09** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Version 2 - for Basic IP](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/) — BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC
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
- **draft-ietf-idr-fsv2-quic-00** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification for QUIC](https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-quic/) — A BGP Flow Specification is an n-tuple consisting of several
   matching criteria that can be applied to IP traffic. This document
   defines how to perform Flow Specification traffic diversion based on
   the characteristics of QUIC packets.
- **draft-ietf-idr-rt-derived-community-13** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route Target derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route Target derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-idr-ts-flowspec-srv6-policy-20** (new-draft, score 0, ignored_after_review) [idr]: [Traffic Steering using BGP FlowSpec with SR Policy](https://datatracker.ietf.org/doc/draft-ietf-idr-ts-flowspec-srv6-policy/) — BGP Flow Specification (FlowSpec) provides mechanisms to distribute
   traffic filtering and steering rules across BGP networks.  This
   document specifies BGP FlowSpec procedures to steer matching traffic
   flows into Segment Routing (SR) Policies.  It defines two modes of
   operation: transport steering into an SR Policy ("Mode 1"), in SR-
   MPLS and SRv6 networks, using BGP Extended Communities; and, in SRv6
   networks, transport steering combined with an egress service action
   at the egress node ("Mode 2"), signaled with the BGP Prefix-SID
   Attribute.
- **draft-ietf-ippm-hybrid-two-step-07** (new-draft, score 0, ignored_after_review) [ippm]: [Hybrid Two-Step Performance Measurement Method](https://datatracker.ietf.org/doc/draft-ietf-ippm-hybrid-two-step/) — The adoption of network operation automation has brought new
   measurement methodology requirements.  Among them is the ability to
   collect the instant network operational state as the packet is being
   processed by the network elements along its forwarding path through a
   network domain.  That requirement can be addressed by using on-path
   telemetry, also called hybrid performance measurement according to
   RFC 7799.  An on-path telemetry method allows operators to collect
   key information that reflects the operational state and the network
   performance a packet experiences through the forwarding path.  IOAM,
   defined in RFC 9197 and RFC 9326, is an example of such a hybrid
   method.  This document introduces a method complementary to on-path
   telemetry that causes the generation of network telemetry
   information.  This document introduces Hybrid Two-Step (HTS), a
   method complementary to both passive and hybrid measurement
   approaches.  HTS separates measuring or calculating the performance
   metric from collecting and transporting network operational state.
- **draft-ietf-ippm-stamp-ext-hdr-26** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet IP Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-ext-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting hop-by-
   hop and E2E operational and telemetry information.  This document
   extends STAMP to reflect IPv4/IPv6 headers as well as IPv6 extension
   headers for hop-by-hop and E2E active measurements, for example,
   using the IOAM data fields.

   This document updates RFC 8762 by specifying IPv4/IPv6 and UDP
   headers handling, session state notifications, and rate limiting
   requirements that also apply to STAMP sessions not using these
   extensions.
- **draft-ietf-ipsecme-child-pfs-info-01** (new-draft, score 0, ignored_after_review) [ipsecme]: [IKEv2 Support for Child SA PFS Policy Information](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-child-pfs-info/) — This document defines an extension for the Internet Key Exchange
   Protocol Version 2 (IKEv2) to support negotiation at the time of
   initial Child Security Association (SA) establishing of Key Exchange
   (KE) method that could be used in subsequent rekeys of this SA.
- **draft-ietf-jmap-conditional-02** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP Conditional Set](https://datatracker.ietf.org/doc/draft-ietf-jmap-conditional/) — The JMAP base protocol ([JMAP-CORE]) provides the Foo/set method for
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
- **draft-ietf-jmap-emailpush-04** (new-draft, score 0, ignored_after_review) [jmap]: [JSON Meta Application Protocol (JMAP) Email Delivery Push Notifications](https://datatracker.ietf.org/doc/draft-ietf-jmap-emailpush/) — This document specifies an extension to the JSON Meta Application
   Protocol (JMAP) that allows clients to receive an object via a JMAP
   push subscription whenever a new email is delivered that matches a
   client-defined filter.  The object can also include properties from
   the email, to allow a user notification to be displayed without
   having to make a further network request.
- **draft-ietf-jmap-filenode-19** (new-draft, score 0, ignored_after_review) [jmap]: [JMAP File Storage extension](https://datatracker.ietf.org/doc/draft-ietf-jmap-filenode/) — The JMAP base protocol (RFC 8620) provides the ability to upload and
   download arbitrary binary data.  This binary data is called a "blob",
   and can be used in all other JMAP extensions.

   This extension adds a FileNode data type and methods to expose blobs
   as a filesystem, along with the types of metadata that are provided
   by other remote filesystem protocols.
- **draft-ietf-lake-app-profiles-07** (new-draft, score 0, ignored_after_review) [lake]: [Coordinating the Use of Application Profiles for the Lightweight Authenticated Key Exchange (LAKE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-lake-app-profiles/) — The Lightweight Authenticated Key Exchange (LAKE) protocol requires
   certain parameters to be agreed out-of-band, in order to ensure its
   successful completion.  To this end, application profiles specify the
   intended use of LAKE to allow for the relevant processing and
   verifications to be made.  In order to ensure the applicability of
   such parameters and information beyond transport- or setup-specific
   scenarios, this document defines a canonical, CBOR-based
   representation that can be used to describe, distribute, and store
   LAKE application profiles.  Furthermore, in order to facilitate
   interoperability between LAKE implementations and support LAKE
   extensibility for additional integrations, this document defines a
   number of means to coordinate the use of LAKE application profiles.
   Finally, this document defines a set of well-known LAKE application
   profiles.
- **draft-ietf-lisp-rfc6831bis-14** (new-draft, score 0, ignored_after_review) [lisp]: [The Locator/ID Separation Protocol (LISP) for Multicast Environments](https://datatracker.ietf.org/doc/draft-ietf-lisp-rfc6831bis/) — This document specifies the design for inter-domain multicast
   overlays using the Locator/ID Separation Protocol (LISP) architecture
   and protocols.  The document specifies how LISP multicast overlays
   operate over multicast and unicast underlays.  The mechanisms in this
   specification indicate how a signal-based approach using the PIM
   protocol can be used to program LISP encapsulators with a replication
   list in a locator-set, where the replication list can be a mix of
   multicast and unicast locators.  This document when approved
   obsoletes RFC 6831.
- **draft-ietf-lsr-l2-bundle-member-remote-id-12** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  This document
   describes how Open Shortest Path First (OSPF) and Intermediate System
   to Intermediate System (IS-IS) advertise the remote interface
   identifiers for L2 bundle members.  The corresponding extension of
   BGP Link State (BGP-LS) is also specified.
- **draft-ietf-lsr-pcpps-02** (new-draft, score 0, ignored_after_review) [lsr]: [IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-ietf-lsr-pcpps/) — [I-D.many-teas-power-steering] introduces a Power Conserving Path
   Placement Strategy (PCPPS).  When possible, PCPPS concentrates
   traffic onto a small set of network resources.  When traffic is
   concentrated onto a small set of network resources, other network
   resources become idle and can be powered down until they are needed
   again.  This conserves energy and reduces environmental impact.

   PCPPS uses information that is distributed by an IGP.  This document
   specifies the IS-IS encoding for that information.
- **draft-ietf-mailmaint-aprf-01** (new-draft, score 0, ignored_after_review) [mailmaint]: [Aggregate Performance Reporting](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-aprf/) — Definition of an aggregate performance report format for email
   messaging, the means to discover target destinations, and a specified
   delivery method.
- **draft-ietf-mailmaint-pdparchive-03** (new-draft, score 0, ignored_after_review) [mailmaint]: [Personal Data Portability Archive](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-pdparchive/) — This document proposes the Personal Data Portability Archive format
   (PDPA), suitable for import/export, backup/restore, and data transfer
   scenarios for personal data.
- **draft-ietf-mboned-multicast-security-02** (new-draft, score 0, ignored_after_review) [mboned]: [Security and Privacy Considerations for Multicast Transports](https://datatracker.ietf.org/doc/draft-ietf-mboned-multicast-security/) — Interdomain multicast has unique potential to solve delivery
   scalability for popular content, but it carries a set of security and
   privacy issues that differ from those in unicast delivery.  This
   document analyzes the security threats unique to multicast-based
   delivery for Internet and Web traffic under the Internet and Web
   threat models.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/squarooticus/draft-krose-multicast-security.
- **draft-ietf-mlcodec-opus-speech-coding-enhancement-05** (new-draft, score 0, ignored_after_review) [mlcodec]: [Integration of Speech Codec Enhancement Algorithms into the Opus Codec](https://datatracker.ietf.org/doc/draft-ietf-mlcodec-opus-speech-coding-enhancement/) — This document proposes a set of requirements for integrating a speech
   codec enhancement algorithm into the Opus codec [RFC6716].  It also
   updates [RFC7587] to define two optional media type parameters for
   signaling decoder-side speech enhancement capabilities.
- **draft-ietf-mops-network-overlay-impacts-05** (new-draft, score 0, ignored_after_review) [mops]: [Network Overlay Impacts to Streaming Video](https://datatracker.ietf.org/doc/draft-ietf-mops-network-overlay-impacts/) — This document examines the operational impacts on streaming video
   applications resulting from network policy changes introduced by
   network overlays.  Such overlays may alter IP address assignment,
   transport protocols, routing behavior, or DNS resolution.  These
   changes can, in turn, affect critical aspects of content delivery,
   including latency, CDN cache selection, delivery path optimization,
   traffic classification, and content access controls.
- **draft-ietf-mpls-mna-ioam-15** (new-draft, score 0, ignored_after_review) [mpls]: [MPLS Network Actions for In Situ Operations, Administration, and Maintenance](https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-ioam/) — In situ Operations, Administration, and Maintenance (IOAM), defined
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
- **draft-ietf-netconf-distributed-notif-24** (new-draft, score 0, ignored_after_review) [netconf]: [Subscription to Notifications in a Distributed Architecture](https://datatracker.ietf.org/doc/draft-ietf-netconf-distributed-notif/) — This document describes extensions to configured subscriptions to
   YANG notifications to allow metrics being published directly from
   processors on line cards to target receivers, while subscription is
   still maintained at the route processor in a distributed forwarding
   system of a network node.
- **draft-ietf-netconf-error-registries-01** (new-draft, score 0, ignored_after_review) [netconf]: [Error List and Error Identities Registries for YANG-driven protocols](https://datatracker.ietf.org/doc/draft-ietf-netconf-error-registries/) — This document defines IANA registries for the YANG Protocol Error
   List and YANG Protocol Error Identities.
- **draft-ietf-netconf-list-pagination-nc-14** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-nc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to NETCONF [RFC6241].

   This document updates [RFC6241], to augment the <get> and <get-
   config> "rpc" statements, and [RFC8526], to augment the <get-data>
   "rpc" statement, to define input parameters necessary for list
   pagination.
- **draft-ietf-netconf-list-pagination-rc-13** (new-draft, score 0, ignored_after_review) [netconf]: [RESTCONF Extensions to Support List Pagination](https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-rc/) — This document defines a mapping of the list pagination mechanism
   defined in [I-D.ietf-netconf-list-pagination] to RESTCONF [RFC8040].

   This document updates RFC 8040, to declare "list" and "leaf-list" as
   valid resource targets for the RESTCONF GET operation, to define GET
   query parameters necessary for list pagination, and to define a
   media-type for XML-based lists.
- **draft-ietf-netconf-over-quic-13** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF over QUIC](https://datatracker.ietf.org/doc/draft-ietf-netconf-over-quic/) — This document specifies how to use QUIC as a secure transport for
   exchanging Network Configuration Protocol (NETCONF) messages.
   NETCONF over QUIC allows implementations to take advantage of QUIC
   streams, for example, to eliminate some TCP head-of-line blocking
   issues.  NETCONF over QUIC provides security properties similar to
   NETCONF over TLS.

   This document also defines a YANG module which augments the ietf-
   netconf-client and ietf-netconf-server YANG modules.

Editorial note (to be removed by the RFC Editor)

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
- **draft-ietf-netconf-trace-ctx-extension-10** (new-draft, score 0, ignored_after_review) [netconf]: [NETCONF Extension to support Trace Context propagation](https://datatracker.ietf.org/doc/draft-ietf-netconf-trace-ctx-extension/) — This document defines how to propagate trace context information
   across the Network Configuration Protocol (NETCONF), enabling
   distributed tracing scenarios.  It is an adaptation of the HTTP-based
   W3C specification and defines three YANG modules.
- **draft-ietf-netconf-yang-notifications-versioning-19** (new-draft, score 0, ignored_after_review) [netconf]: [Support of Versioning in YANG Notifications Subscriptions](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-notifications-versioning/) — This document defines a YANG module which extends the YANG-Push
   Subscription mechanism to enforce that particular revisions or
   semantic versions are used when configuring or establishing a
   Subscription.  It also extends the YANG-Push Subscription state
   change Notifications to include additional context about the YANG
   schema associated with the Subscription.
- **draft-ietf-netmod-yang-xml-01** (new-draft, score 0, ignored_after_review) [netmod]: [XML Encoding of Data Modeled with YANG](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-xml/) — This document defines encoding rules for representing YANG modeled
   configuration data, state data, parameters of Remote Procedure Call
   (RPC) operations or actions, and notifications defined using XML.
- **draft-ietf-openpgp-external-secrets-01** (new-draft, score 0, ignored_after_review) [openpgp]: [OpenPGP External Secret Keys](https://datatracker.ietf.org/doc/draft-ietf-openpgp-external-secrets/) — This document defines a standard wire format for indicating that the
   secret component of an OpenPGP asymmetric key is stored externally,
   for example on a hardware device or other comparable subsystem.
- **draft-ietf-opsawg-ipfix-alt-mark-09** (new-draft, score 0, ignored_after_review) [opsawg]: [IP Flow Information Export (IPFIX) Alternate-Marking Information Elements](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-alt-mark/) — This document specifies the IP Flow Information Export (IPFIX)
   Information Elements (IEs) to export Alternate Marking measurement
   data.
- **draft-ietf-opsawg-ipfix-ecn-01** (new-draft, score 0, ignored_after_review) [opsawg]: [Export of ECN Information in IPFIX](https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-ecn/) — This document defines a set of IPFIX Information Elements for
   monitoring Explicit Congestion Notification (ECN).  These Information
   Elements allow network operators to observe ECN codepoint usage
   across network traffic and evaluate the corresponding traffic
   performance.
- **draft-ietf-pce-flexible-grid-21** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-pce-pcep-bfd-parameters-03** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extensions to support BFD parameters](https://datatracker.ietf.org/doc/draft-ietf-pce-pcep-bfd-parameters/) — This document proposes extension to PCEP to configure LSP parameters.
   Some of LSP parameters are needed to configure S-BFD for candidate
   paths.  Each candidate path is identified in PCEP by its uniquely
   assigned PLSP-ID.  The mechanism proposed in this document is
   applicable to to all path setup types.  This extension can work with
   ifferent PCEP Path Setup Types but especially suitable for Segment
   Routing (SR-MPLS, SRv6)..
- **draft-ietf-pce-sr-p2mp-policy-22** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable an architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pim-ipv6-zeroconf-assignment-17** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the requirements and most of the desired
   characteristics listed in RFC 10019.
- **draft-ietf-pquip-pqc-hsm-constrained-11** (new-draft, score 0, ignored_after_review) [pquip]: [Adapting Constrained Devices for Post-Quantum Cryptography](https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/) — This document provides guidance on integrating Post-Quantum
   Cryptography (PQC) into resource-constrained devices, such as IoT
   nodes and dedicated key-storage hardware.  These systems often
   operate with strict limitations on processing power, RAM, and flash
   memory, and may even be battery-powered.  The document emphasizes the
   role of hardware security as the basis for secure operations,
   supporting features such as seed-based key generation to minimize
   persistent storage, efficient handling of ephemeral keys, and the
   offloading of cryptographic tasks in low-resource environments.  It
   also explores the implications of PQC on firmware update mechanisms
   in such constrained systems.
- **draft-ietf-procon-2026bis-12** (new-draft, score 0, ignored_after_review) [procon]: [The Internet Standards Process](https://datatracker.ietf.org/doc/draft-ietf-procon-2026bis/) — This memo documents the process used by the Internet community for
   the standardization of protocols and procedures.  It defines the
   stages in the standardization process, the requirements for moving a
   document between stages, and the types of documents used during this
   process.  It also addresses the intellectual property rights and
   copyright issues associated with the standards process.

   This document obsoletes RFC 2026, RFC 5657, RFC 6410, RFC 7100, RFC
   7127, RFC 8789, and RFC 9282.  It also includes the changes from RFC
   7475.  If this document and [_2418bis] are published as RFCs, then
   taken together the two of them make RFC 7475 obsolete.
- **draft-ietf-radext-connectinfo-01** (new-draft, score 0, ignored_after_review) [radext]: [A syntax for the RADIUS Connect-Info attribute used in Wi-Fi networks](https://datatracker.ietf.org/doc/draft-ietf-radext-connectinfo/) — This document describes a syntax for the Connect-Info attribute used
   with the RADIUS protocol, enabling RADIUS clients to provide RADIUS
   servers information pertaining to a user's connection with an IEEE
   802.11 wireless network.
- **draft-ietf-regext-rdap-extensions-18** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes, clarifies and further specifies the usage of
   extensions in RDAP.
- **draft-ietf-roll-dis-modifications-04** (new-draft, score 0, ignored_after_review) [roll]: [RPL DIS Modifications and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-roll-dis-modifications/) — This document updates the RPL routing protocol specification by
   defining new DODAG Information Solicitation (DIS) flags and options
   that enable a RPL node to exert finer control over how neighboring
   RPL routers respond to its DIO solicitations.  In addition, this
   document describes several use cases that motivate these DIS
   extensions and illustrate scenarios in which enhanced control of DIO
   responses improves network efficiency, responsiveness, and
   robustness.
- **draft-ietf-rtgwg-atn-bgp-35** (new-draft, score 0, ignored_after_review) [rtgwg]: [A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network](https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/) — The International Civil Aviation Organization (ICAO) is investigating
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
- **draft-ietf-scone-applicability-manageability-03** (new-draft, score 0, ignored_after_review) [scone]: [Manageability Considerations for SCONE](https://datatracker.ietf.org/doc/draft-ietf-scone-applicability-manageability/) — This document describes the manageability considerations for network
   operators for providing throughput advice to application endpoints.
   This guidance is specifically addressed within the context of
   communication networks utilizing the Standard Communication with
   Network Elements (SCONE) protocol [SCONE].
- **draft-ietf-scone-protocol-10** (new-draft, score 0, ignored_after_review) [scone]: [Standard Communication with Network Elements (SCONE) Protocol](https://datatracker.ietf.org/doc/draft-ietf-scone-protocol/) — This document describes a protocol where on-path network elements can
   communicate their perspective on the maximum sustainable throughput
   for QUIC flows to endpoints.  This throughput advice suggests an
   upper bound on long-term average throughput, independent of and
   complementary to real-time congestion control signals.
- **draft-ietf-spring-srv6-inter-layer-programming-04** (new-draft, score 0, ignored_after_review) [spring]: [SRv6 for Inter-Layer Network Programming](https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-inter-layer-programming/) — The Segment Routing over IPv6 (SRv6) Network Programming framework
   enables a network operator or an application to specify a packet
   processing program by encoding a sequence of instructions in the IPv6
   packet header.

   Following the SRv6 Network Programming concept, this document defines
   SRv6 based mechanisms for inter-layer network programming, which can
   help to integrate the packet network layer with its underlying layers
   efficiently.  For inter-layer path programming, a new SRv6 behavior
   is defined for steering packets to underlay network connections.  The
   applicability of this new SRv6 behavior in typical scenarios is
   illustrated.
- **draft-ietf-teas-actn-poi-applicability-21** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) to Packet Optical Integration (POI)](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-applicability/) — This document explores the applicability of the Abstraction and
   Control of TE Networks (ACTN) architecture to Packet Optical
   Integration (POI) within the context of IP/MPLS and optical
   internetworking.  It examines the YANG data models defined by the
   IETF that enable an ACTN-based deployment architecture and highlights
   specific scenarios pertinent to Service Providers.

   Existing IETF protocols and data models are identified for each
   multi-technology scenario (packet over optical), particularly
   emphasising the Multi-Domain Service Coordinator to Provisioning
   Network Controller Interface (MPI) within the ACTN architecture.
- **draft-ietf-teas-actn-poi-assurance-06** (new-draft, score 0, ignored_after_review) [teas]: [Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) for Packet Optical Integration (POI) service assurance](https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-assurance/) — This document extends the analysis of the applicability of
   Abstraction and Control of Traffic Engineered Networks (ACTN)
   architecture to Packet Optical Integration (POI) to cover multi-layer
   service assurance scenarios.

   Specifically, the ACTN architecture is analyzed to support service
   assurance for end-to-end IP services such as L2VPN or L3VPN
   connectivity services, with specific Service Level Agreement (SLA)
   requirements, through the detection and correlation of failures
   across the optical and packet layers, done by the relevant
   Provisioning Network Controller (PNC) in coopearation with the Multi-
   Domain Service Coordinator (MDSC).

   Existing IETF protocols and data models are identified for each
   multi-layer (packet over optical) service assurance scenario with a
   specific focus on the Multi-Domain Service Coordinator to
   Provisioning Network Controllers Interface (MPI) in the ACTN
   architecture.
- **draft-ietf-tiptop-ip-architecture-02** (new-draft, score 0, ignored_after_review) [tiptop]: [An Architecture for IP in Deep Space](https://datatracker.ietf.org/doc/draft-ietf-tiptop-ip-architecture/) — The IP protocol stacks used on Earth's Internet are typically
   configured based on assumptions of short delays and mostly
   uninterrupted communications.  This document describes an
   architecture of the IP protocol stack tailored for its use in deep
   space.  It involves buffering IP packets in IP forwarders facing
   intermittent links and adjusting transport protocol configurations
   and application protocol timers.  This architecture applies to the
   Moon, Mars, and general interplanetary networking.
- **draft-ietf-tiptop-quic-profile-01** (new-draft, score 0, ignored_after_review) [tiptop]: [QUIC Profile for Deep Space](https://datatracker.ietf.org/doc/draft-ietf-tiptop-quic-profile/) — Deep space communications involve long delays (e.g., the Earth to
   Mars one-way delay is ~4-20 minutes) and often intermittent
   communications.  In this context, the default configuration of QUIC
   stacks, tuned for the terrestrial Internet, is not suitable for deep
   space.  This document defines a QUIC profile for deep space.  It
   provides guidance on how to estimate and set transport parameters and
   local implementation settings, advice to space mission operators and
   application developers on how to configure QUIC for the deep space
   use case, and guidance to QUIC stack developers on exposing the
   required controls in their API.
- **draft-ietf-tiptop-usecase-04** (new-draft, score 0, ignored_after_review) [tiptop]: [IP in Deep Space: Key Characteristics, Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-ietf-tiptop-usecase/) — Deep space communications involve long delays (e.g., Earth to Mars
   has one-way delays 4-24 minutes) and intermittent communications,
   mainly because of orbital dynamics.  Most of the IP protocol stack
   used on the Internet, in particular reliable transport protocols and
   applications, is based on the assumptions of shorter delays and
   mostly uninterrupted communications.  This document describes the key
   characteristics, use cases, and requirements for deep space
   networking, intended to help when profiling IP protocols in such
   environment.
- **draft-ietf-tsvwg-careful-resume-qlog-03** (new-draft, score 0, ignored_after_review) [tsvwg]: [Quic Logging for Convergence of Congestion Control from Retained State](https://datatracker.ietf.org/doc/draft-ietf-tsvwg-careful-resume-qlog/) — This document specifies a logging format for a cautious method for
   Careful Resume when using the IETF quic transport protocol.  It
   defines the logging format for qlog.
- **draft-ietf-v6ops-6mops-12** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (e.g. local area network (LAN)).  This approach enables
   incremental transition from dual-stack to IPv6-only networks by
   allowing IPv6-capable devices to remain IPv6-only while the network
   is seamlessly supplying IPv4 addresses to those devices that require
   them.  This document discusses the requirements, recommendations, and
   challenges associated with deploying IPv6-mostly networks in
   enterprise and public Wi-Fi environments.
- **draft-ietf-v6ops-icmpext-xlat-v6only-source-02** (new-draft, score 0, ignored_after_review) [v6ops]: [Using Dummy IPv4 Address and Node Identification Extensions for IP/ICMP translators (XLATs)](https://datatracker.ietf.org/doc/draft-ietf-v6ops-icmpext-xlat-v6only-source/) — This document suggests that when a source IPv6 address of an ICMPv6
   message can not be translated to an IPv4 address, and the protocol
   translator does not have any public IPv4 addresses available to
   source the translated packet from, the translator uses the dummy IPv4
   address (192.0.0.8) to translate the IPv6 source address.  This
   document updates RFC6791, Stateless Source Address Mapping for ICMPv6
   Packets, and RFC7915, IP/ICMP Translation Algorithm, by proposing to
   utilize the ICMP extension for Node Identification (draft-ietf-
   intarea-extended-icmp-nodeid) to carry the original IPv6 source
   address of ICMPv6 messages.
- **draft-ietf-v6ops-ipv6-app-testing-06** (new-draft, score 0, ignored_after_review) [v6ops]: [Testing Applications' IPv6 Support](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/) — This document provides guidance for application developers and
   software as a service providers on how to approach IPv6 testing in
   Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including "IPv6-
   only-strict" scenarios without any connectivity towards any relevant
   IPv4 endpoint.  It discusses common misconceptions about the degree
   to which operating systems and libraries can abstract IPv6 issues
   away and explains common regressions to avoid when deploying IPv6
   support.
- **draft-ietf-v6ops-ipv6-only-06** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Terminology Definitions](https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/) — This document defines the terminology regarding the usage of
   expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid
   confusions when using them in IETF and other documents.  In
   particular, a goal is to provide a reference that describes the
   actual "IPv6-Only" functionality being used in a given scope, not the
   installed protocol stack support.
- **draft-ietf-v6ops-nat64-wkp-1918-09** (new-draft, score 0, ignored_after_review) [v6ops]: [Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) — This document modifies the deployment guidance provided in
   Section 3.1 of RFC 6052 (IPv6 Addressing of IPv4/IPv6 Translators)
   that IPv4/IPv6 Translators must not use the Well-Known Prefix
   64:ff9b::/96 to represent non-globally reachable IPv4 addresses, such
   as those defined in RFC 1918 (Address Allocation for Private
   Internets) or listed in Section 2.2.2 of RFC 6890 (Special-Purpose IP
   Address Registries).  This change enables IPv6-only nodes to reach
   IPv4-only services with specific non-globally reachable addresses by
   leveraging the Well-Known Prefix.

   This document updates RFC 6052 to allow packets in which an address
   is composed of the Well-Known Prefix and specific non-globally
   reachable IPv4 addresses to be translated.
- **draft-ietf-v6ops-prefix-to-end-sites-01** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Prefix Assignment to End-Sites](https://datatracker.ietf.org/doc/draft-ietf-v6ops-prefix-to-end-sites/) — This document describes different alternatives and best current
   practices for assignment of IPv6 prefixes for end-sites in broadband
   networks, including considerations about point-to-point links, their
   size, numbering choices, pool choices, customer prefix assignment
   size and persistence of those assignments.
- **draft-irtf-rasprg-analysing-ietf-data-00** (new-draft, score 0, ignored_after_review) [rasprg]: [Analysing Internet Standards Data](https://datatracker.ietf.org/doc/draft-irtf-rasprg-analysing-ietf-data/) — This document outlines some issues to consider when studying data
   relating to the Internet standards development ecosystem.  It
   identifies observable components of standards development processes,
   proposes a taxonomy of possible measurements, and highlights
   methodological, interpretive, and ethical considerations.  It is
   intended to support a range of uses, including monitoring standards
   development organisations (SDOs), evaluating the evolution of
   technical work, understanding technology deployment, and informing
   community, leadership, and governance discussions.

   This document is submitted for consideration by the Research and
   Analysis of Standard-Setting Processes Research Group (RASPRG) in the
   IRTF.  It is not an IETF product and is not a standard.
- **draft-janzking-nmrg-telemetry-instrumentation-02** (new-draft, score 0, ignored_after_review) [none]: [Telemetry Methodologies for Analog Measurement Instrumentation](https://datatracker.ietf.org/doc/draft-janzking-nmrg-telemetry-instrumentation/) — Evolution toward network operations automation requires systems
   encompassing software-based analytics and decision-making.  Network-
   based instrumentation provides crucial data for these components and
   processes.  However, the proliferation of such instrumentation and
   the need to migrate the data it generates from the physical network
   to "off-the-network" software poses challenges.  In particular,
   analog measurement instrumentation, which generates time-continuous
   real-number data, may generate significant data volumes.

   This document discusses methodologies for handling analog measurement
   instrumentation data, informed by the requirements of network digital
   twins and of automated fault diagnosis.  It proposes that
   instrumentation report, for each measured quantity and each interval,
   a summary that keeps the level, the rate of change, the departure
   from a steady trend, the extremes over a stated short window and the
   number of measurements taken.  Such summaries can be combined exactly
   over any longer span, and they allow trends, brief events and stopped
   measurements to be detected and reported as they occur.
- **draft-jenkins-cnsa2-cmc-profile-04** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Certificate Management over CMS](https://datatracker.ietf.org/doc/draft-jenkins-cnsa2-cmc-profile/) — This document specifies a profile of the Certificate Management over
   CMS (CMC) protocol for managing X.509 public key certificates in
   applications that use the Commercial National Security Algorithm
   (CNSA) Suite published by the United States Government.

   The profile applies to the capabilities, configuration, and operation
   of all components of US National Security Systems that manage X.509
   public key certificates over CMS.  It is also appropriate for all
   other US Government systems that process high-value information.

   This memo is not an IETF standard, and does not represent IETF
   community consensus.  The profile is made publicly available here for
   use by developers and operators of these and any other system
   deployments.  This document obsoletes [RFC8756], the CNSA 1.0
   guidance.
- **draft-jenkins-cnsa2-pkix-profile-06** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for Certificates and Certificate Revocation Lists](https://datatracker.ietf.org/doc/draft-jenkins-cnsa2-pkix-profile/) — This document specifies a profile of X.509 v3 Certificates and X.509
   v2 Certificate Revocation Lists for applications that use Commercial
   National Security Algorithm Suite published by the United States
   Government.

   The profile applies to the capabilities, configuration, and operation
   of all components of US National Security Systems that employ such
   X.509 certificates.  US National Security Systems are described in
   NIST Special Publication 800-59.  It is also appropriate for all
   other US Government systems that process high-value information.

   This memo is not an IETF standard, and does not represent IETF
   community consensus.  The profile is made publicly available for use
   by developers and operators of these and any other system
   deployments.  This document obsoletes [RFC8603], the CNSA 1.0
   guidance.
- **draft-kalosha-stb-tls13-01** (new-draft, score 0, ignored_after_review) [none]: [STB Cryptographic Parameters for Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-kalosha-stb-tls13/) — This specification introduces a subset of STB (STandards of Belarus)
   cryptographic algorithms and defines their use in TLS 1.3.  The
   document is self-contained, i.e., it fully describes the required STB
   algorithms.  It can be used to develop STB-compliant TLS 1.3
   implementations without referring to the original STB standards.
- **draft-kbf-onsen-problem-statement-01** (new-draft, score 0, ignored_after_review) [none]: [ONSEN Problem Statement](https://datatracker.ietf.org/doc/draft-kbf-onsen-problem-statement/) — The IETF has published a number of YANG data models for automating
   the provisioning and delivery of network and connectivity services,
   including the L2SM, L3SM, L2NM, L3NM, Attachment Circuits, and
   Network Slicing models.  These models are intended to provided
   abstracted representations of common operator services, exposing only
   the necessary parameters for configuring and managing services.
   These abstractions help to contain the complexity of service
   provisioning within the necessary domains, making the implementation
   of complex, multi-domain services easier to implement and manage.

   However, operators have reported persistent challenges in
   operationalizing these abstractions in a consistent, scalable, and
   automatable manner.  This document describes the problem space for
   the ONSEN Working Group, identifying the operational gaps and
   deficiencies in existing IETF service and network abstraction models
   that complicate, or prevent effective end-to-end automation.  The
   problems documented here are initially drawn from operator
   experience, and from the findings of the IAB NEMOPS Workshop.

   It is a living draft, not intended for publication as an RFC, and
   will be updated with new problem descriptions as the ONSEN work
   proceeds.  This document does not propose solutions, protocols, or
   new data models.
- **draft-koo-dtn-traceroute-eb-03** (new-draft, score 0, ignored_after_review) [none]: [Traceroute Extension Block for Bundle Protocol Version 7](https://datatracker.ietf.org/doc/draft-koo-dtn-traceroute-eb/) — This document defines a Traceroute Extension Block (TREB) for Bundle
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
- **draft-kt-dmm-bgpmup-over-6gup-00** (new-draft, score 0, ignored_after_review) [none]: [BGP MUP over 6G UP Architecture](https://datatracker.ietf.org/doc/draft-kt-dmm-bgpmup-over-6gup/) — Evolution of the 6G user plane toward distributed Serving and Anchor
   User Plane Functions (S-UPFs and A-UPFs) offers an opportunity to
   coordinate mobility, IP transport, and application/AI-compute
   placement.  This document explores an architecture in which a Mobile
   User Plane Controller (MUP-C) translates authorized mobile-session
   information and transport-aware steering decisions into BGP Mobile
   User Plane (MUP) routing information.  It describes interworking with
   the BGP MUP SAFI, access and data-network segments, SRv6 forwarding,
   mobility, and user-plane accounting.  The architecture is transport-
   neutral; SRv6 is an illustrative data plane.  The proposed
   application-to-session binding and 6G procedures are for discussion
   and do not define new BGP encodings or change 3GPP procedures.
- **draft-laxsharma-pact-03** (new-draft, score 0, ignored_after_review) [none]: [PACT: Co-Signed Task Contracts, Delivery and Verdict Records, and Outcome Records for Autonomous Agents](https://datatracker.ietf.org/doc/draft-laxsharma-pact/) — Autonomous agents can already prove who they are, show whose
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
- **draft-lehmann-idmefv2-09** (new-draft, score 0, ignored_after_review) [none]: [The Incident Detection Message Exchange Format version 2 (IDMEFv2)](https://datatracker.ietf.org/doc/draft-lehmann-idmefv2/) — The Incident Detection Message Exchange Format version 2 (IDMEFv2)
   defines a data representation for security incidents detected on
   cyber and/or physical infrastructures.

   The format is agnostic so it can be used in standalone or combined
   cyber (SIEM), physical (PSIM) and availability (NMS) monitoring
   systems.  IDMEFv2 can also be used to represent man made or natural
   hazards threats.

   IDMEFv2 improves situational awareness by facilitating correlation of
   multiple types of events using the same base format thus enabling
   efficient detection of complex and combined cyber and physical
   attacks and incidents.

   This draft is maintained by the IDMEFv2 Task Force.  Please consult
   our website for more information: https://www.idmefv2.org.

   If approved this draft will obsolete RFC4765.
- **draft-lenders-core-oblivious-coap-01** (new-draft, score 0, ignored_after_review) [none]: [Oblivious CoAP](https://datatracker.ietf.org/doc/draft-lenders-core-oblivious-coap/) — In the Constrained Application Protocol (CoAP), protected requests
   allow the server to identify the client, also across different and
   unrelated data exchanges.  This document defines Oblivious CoAP,
   which enables oblivious protected exchanges of CoAP messages for use
   cases where the identification of the client at the server is not
   desirable.
- **draft-li-idr-bgp-sr-policy-bfd-extension-03** (new-draft, score 0, ignored_after_review) [none]: [BGP SR Policy Extensions for BFD Configuration](https://datatracker.ietf.org/doc/draft-li-idr-bgp-sr-policy-bfd-extension/) — Segment Routing (SR) Policies require fast failure detection for
   Candidate Paths (CPs) to enable rapid rerouting and high
   availability.  Currently, the provisioning of SR Policies and the
   configuration of the associated Seamless Bidirectional Forwarding
   Detection (S-BFD) sessions are performed independently.  This often
   necessitates separate mechanisms (e.g., manual configuration,
   NETCONF, or additional signaling) to associate S-BFD sessions with
   the SR Policies, resulting in complex and error-prone operations.

   This document defines extensions to BGP SR Policy for the
   simultaneous provisioning of SR Policy CPs and their S-BFD
   configuration parameters during policy advertisement.  The extensions
   include optional sub-TLVs within the Tunnel Encapsulation Attribute
   to carry S-BFD configuration parameters (e.g., discriminators,
   intervals, multipliers).

   These extensions simplify deployment in distributed or controller-
   based environments, reduce configuration overhead, and enhance
   operational efficiency for SR-based traffic engineering.
- **draft-li-idr-bgpls-sr-policy-composite-path-11** (new-draft, score 0, ignored_after_review) [none]: [Signaling Composite Candidate Path of SR Policy using BGP-LS](https://datatracker.ietf.org/doc/draft-li-idr-bgpls-sr-policy-composite-path/) — SR Policy Architecture [RFC9256] defines the concept of a Composite
   Candidate Path.  A regular SR Policy Candidate Path outputs traffic
   to a set of Segment Lists, while an SR Policy Composite Candidate
   Path outputs traffic recursively to a set of SR Policies on the same
   headend.  This document specifies the extensions to BGP Link State
   (BGP-LS) to carry composite candidate path information in the
   advertisement of an SR policy.
- **draft-li-rtgwg-overload-alleviation-00** (new-draft, score 0, ignored_after_review) [none]: [Common Approaches to Link Overload Alleviation](https://datatracker.ietf.org/doc/draft-li-rtgwg-overload-alleviation/) — Network links may become degraded because of physical conditions or
   owing to partial link failure: this can result in a reduction of
   available bandwidth.  Alternatively, traffic volume may increase
   significantly and unexpectedly.  These circumstances may lead to
   links becoming overloaded which can result in dropped packets or
   degraded delivery such as increased delay.

   Traffic adjustment techniques can be applied to alleviate these link-
   overload situations by steering some of the traffic onto other paths
   that are less loaded and have available bandwidth.

   This document examines the scenarios in which links can become
   overloaded, the requirements for steering traffic to reduce link-
   overload, and the techniques that can be applied to alleviate
   overloaded links.
- **draft-liao-lamps-est-lightweight-operations-02** (new-draft, score 0, ignored_after_review) [none]: [EST Lightweight Operations](https://datatracker.ietf.org/doc/draft-liao-lamps-est-lightweight-operations/) — This document defines eight new operations for the Enrollment over
   Secure Transport (EST) protocol specified in RFC 7030: ucacaps,
   ucacert, ucacerts, ucrlinfo, ucrl, usimpleenroll, usimplereenroll,
   and userverkeygen.  These operations deliver PKI objects, including
   CA certificates, certificate chains, CRLs, and enrolled certificates,
   as Base64-encoded DER or PEM, without the CMS encapsulation used by
   the corresponding EST operations in RFC 7030.  The ucacaps operation
   enables EST clients to discover which operations the EST server
   supports.  Eliminating the CMS wrapper for these responses reduces
   code size and parsing complexity.
- **draft-lin-idr-interface-index-capability-01** (new-draft, score 0, ignored_after_review) [none]: [Interface Index Capability for BGP](https://datatracker.ietf.org/doc/draft-lin-idr-interface-index-capability/) — In some scenarios using unnumbered links, it is necessary for the BGP
   protocol to advertise the link's Interface Index and obtain the
   peer's Remote Interface Index.

   This document defines a new BGP capability, as specified in RFC 5492,
   for advertising local interface indexes and obtaining neighbor
   interface indexes.
- **draft-liu-idr-bgp-sr-policy-cp-threshold-03** (new-draft, score 0, ignored_after_review) [none]: [BGP Extension for Distributing CP Threshold Constraints of SR Policy](https://datatracker.ietf.org/doc/draft-liu-idr-bgp-sr-policy-cp-threshold/) — This document defines the extension of BGP to distribute the
   threshold constraint parameters of candidate paths for SR Policy to
   achieve flexible path selection.
- **draft-liu-moq-feedback-01** (new-draft, score 0, ignored_after_review) [none]: [MoQ Feedback](https://datatracker.ietf.org/doc/draft-liu-moq-feedback/) — This document defines Media over QUIC Feedback (MQF), an extension to
   Media over QUIC Transport (MOQT) that enables delivery quality
   information about media Objects to be reported using Feedback Tracks.
   It defines how Feedback Tracks are associated with media Tracks,
   established, forwarded through Relays, and consumed, together with
   the MQF report format and capability negotiation.  MQF complements
   transport-layer signals with per-Object delivery information.
- **draft-liu-spring-sr-policy-energy-efficiency-06** (new-draft, score 0, ignored_after_review) [none]: [Computing Energy Consumption Path in Segment Routing Networks](https://datatracker.ietf.org/doc/draft-liu-spring-sr-policy-energy-efficiency/) — This document elaborates on the method for calculating energy
   consumption paths in Segment Routing (SR) networks, aiming to
   evaluate and optimize traffic-related metrics on network paths,
   including energy consumption and carbon emissions.
- **draft-ll-onsen-soya-00** (new-draft, score 0, ignored_after_review) [none]: [Service Orchestration with YANG-modeled Abstractions Framework](https://datatracker.ietf.org/doc/draft-ll-onsen-soya/) — This document defines the Service Orchestration with YANG-modeled
   Abstractions (SOYA) framework for building layered orchestration
   systems.  Each layer exposes YANG-modeled service intent and
   operational state, and uses business logic to translate intent into
   configuration for the layer below.  The framework describes the
   boundaries between layers, the propagation of configuration and
   state, and the separation of service processing from management
   protocol implementation.  These principles apply to layers hosted
   within one orchestrator or distributed across several orchestrators.
- **draft-llg-opsawg-ipfix-over-quic-04** (new-draft, score 0, ignored_after_review) [none]: [IPFIX Protocol over QUIC](https://datatracker.ietf.org/doc/draft-llg-opsawg-ipfix-over-quic/) — The IP Flow Information Export (IPFIX) protocol provides a means for
   transmitting Traffic Flow information over the network.  IPFIX Flow
   Records and Template Records can be carried over a number of
   transport protocols from an IPFIX Exporter to an IPFIX Collector.
   The supported transport protocols are SCTP, UDP and TCP.  QUIC
   provides inherently secure, stream-multiplexed, and reliable
   connections for the IPFIX protocol.  In particular, a single QUIC
   connection can carry multiple independent streams, which can improve
   management scalability between Exporters and Collectors.  This
   document describes how to use the IPFIX protocol over the QUIC
   transport protocol, named IPFIXoQUIC.
- **draft-loffredo-calext-jscontact-eai-00** (new-draft, score 0, ignored_after_review) [none]: [Internationalized Email Addresses in JSContact](https://datatracker.ietf.org/doc/draft-loffredo-calext-jscontact-eai/) — JSContact defines the EmailAddress object for representing an email
   address, but its address property is restricted to the ASCII syntax
   of an addr-spec in RFC 5322.  This document redefines that property
   to also support internationalized email addresses, as defined in RFC
   6532.  Since such values are incompatible with JSContact version 2.0,
   this document defines JSContact version 3.0.  This document updates
   RFC 9553.
- **draft-lqg-fann-multi-plane-protection-00** (new-draft, score 0, ignored_after_review) [none]: [Fast Network Notification for Plane Protection in Multi-Plane Networks](https://datatracker.ietf.org/doc/draft-lqg-fann-multi-plane-protection/) — This document discusses the use of fast network notifications for
   plane evacuation in multi-plane networks.
- **draft-many-tiptop-ntp-profile-00** (new-draft, score 0, ignored_after_review) [none]: [NTP Profile for Deep Space](https://datatracker.ietf.org/doc/draft-many-tiptop-ntp-profile/) — Deep space communications involve long delays (e.g., Earth to Mars
   one-way delay is 4-24 minutes) and intermittent communications,
   because of orbital dynamics.  This document defines an NTP profile
   for deep space.  NTP on-wire protocol is indifferent to path delays
   and transfers time in a single round trip at any distance, but
   diverges if delays in each direction is different.  Some algorithmic
   constants and defaults such as distance threshold, dispersion bounds,
   poll intervals and burst modes, need to be tailored to the deep space
   scenario.  The use of secured NTP is also discussed.
- **draft-matsushima-dmm-mup-why-01** (new-draft, score 0, ignored_after_review) [none]: [Why the Mobile User Plane Is the Way It Is](https://datatracker.ietf.org/doc/draft-matsushima-dmm-mup-why/) — The Mobile User Plane (MUP) architecture transforms session
   information from a mobile service system into routing information, so
   that ordinary routing nodes can take on the roles of user plane
   anchors and intermediate points.  The architecture document that
   defines MUP is a normative text: it defines concepts, route types,
   and resolution procedures, but it does not explain why they are the
   way they are.  This companion reader supplies that "why", outside the
   normative text.

   The technical content follows one worked example end to end, with
   concrete prefixes, SIDs, and tunnel endpoint identifiers, and follows
   the architecture document throughout.  The explanations are organized
   around a small set of shapes that recur in the design: places
   deliberately left undecided, meaning that arises only when two pieces
   of information meet, and a strict separation between a name and the
   thing it points at.  The Introduction gives these shapes a name
   borrowed from Zen, once, and then lets them do their work quietly.

   This document is not normative.  It defines no protocol and no
   encoding.
- **draft-mauch-bgp-nh-mtu-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Next Hop MTU Attribute](https://datatracker.ietf.org/doc/draft-mauch-bgp-nh-mtu/) — This document defines NEXT_HOP_MTU, an optional non-transitive BGP
   path attribute (type code TBD).  It carries the IP MTU a speaker
   promises is acceptable for an NLRI across one network boundary.  The
   speaker that receives the NLRI across that boundary may attach the
   attribute from the boundary interface MTU and advertise it on
   internal and external sessions.  The intent is to communicate network
   MTU capability so that devices can use that information to improve
   the efficiency of their communications.
- **draft-meunier-bcp-civil-00** (new-draft, score 0, ignored_after_review) [none]: [Principles for Web Traffic Management by Intermediaries](https://datatracker.ietf.org/doc/draft-meunier-bcp-civil/) — This document describes principles for web intermediaries that
   balance security needs with open web accessibility.

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at
   https://thibmeu.github.io/draft-bcp-civil/draft-meunier-bcp-
   civil.html.  Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-meunier-bcp-civil/.

   Source for this draft and an issue tracker can be found at
   https://github.com/thibmeu/draft-bcp-civil.
- **draft-mitchell-intarea-rfc5837bis-02** (new-draft, score 0, ignored_after_review) [none]: [Extending ICMP for Interface and Next-Hop Identification](https://datatracker.ietf.org/doc/draft-mitchell-intarea-rfc5837bis/) — This memo defines data structures that can be appended to selected
   ICMP messages.  The ICMP extensions defined herein can be used to
   identify any combination of the following: the IP interface upon
   which a datagram arrived, the sub-IP component of an IP interface
   upon which a datagram arrived, the IP interface through which the
   datagram would have been forwarded had it been forwardable, the sub-
   IP component of an IP interface through which the datagram would have
   been forwarded had it been forwardable, and the IP next hop to which
   the datagram would have been forwarded.

   Devices can use this ICMP extension to identify interfaces and their
   components by any combination of the following: ifIndex, IPv4
   address, IPv6 address, name, and MTU.  ICMP-aware devices can use
   these extensions to identify both numbered and unnumbered interfaces.

   This document obsoletes RFC 5837.  To preserve strict backward
   compatibility with legacy implementations, it preserves the original
   Interface Information Object (Class-Num 2) as defined in RFC 5837,
   and introduces a new Extended Interface Information Object to
   accommodate new interface roles.
- **draft-oancea-avtcore-opus-ulpfec-00** (new-draft, score 0, ignored_after_review) [none]: [Guidelines for Combining Opus In-Band Forward Error Correction with the RTP Generic FEC (ULPFEC) Payload Format](https://datatracker.ietf.org/doc/draft-oancea-avtcore-opus-ulpfec/) — The Opus codec can carry low-bitrate redundancy for the preceding
   frame inside each packet ("in-band FEC").  The RTP payload format for
   generic Forward Error Correction (RFC 5109, commonly called ULPFEC)
   protects groups of RTP packets with XOR parity packets.  The two
   mechanisms recover different loss patterns, have different delay and
   overhead characteristics, and interact in ways that are not described
   in either specification.

   This document gives informational guidance on when the combination is
   worthwhile, how a sender should configure each mechanism, how a
   receiver should order recovery, how to signal the combination in SDP,
   how middleboxes affect it, and how to keep the combined redundancy
   consistent with congestion control.  It complements, and does not
   change, the WebRTC FEC requirements in RFC 8854.  It defines no new
   protocol elements.
- **draft-petra-green-api-05** (new-draft, score 0, ignored_after_review) [none]: [Path Energy Traffic Ratio API (PETRA)](https://datatracker.ietf.org/doc/draft-petra-green-api/) — This document describes an API to query a network regarding its
   Energy Traffic Ratio for a given path.
- **draft-pospichal-idr-bgp-l2-quic-01** (new-draft, score 0, ignored_after_review) [none]: [Border Gateway Protocol over Layer 2 QUIC Transport (BoL2Q)](https://datatracker.ietf.org/doc/draft-pospichal-idr-bgp-l2-quic/) — This document specifies BGP over Layer 2 QUIC (BoL2Q), a transport
   for external and internal BGP sessions between speakers that share an
   Ethernet segment, in which QUIC packets are carried directly in
   Ethernet frames, identified by a dedicated EtherType, without IP or
   UDP headers.  A BoL2Q session has no IP address and no transport
   port, so it cannot be reached from beyond the Layer 2 segment on
   which it runs, and it requires no IP-layer configuration of any kind:
   a session is defined by a local interface, the MAC address of the
   peer, the remote Autonomous System number and a pre-shared key.
   BoL2Q reuses QUIC version 1 and TLS 1.3 unchanged, apart from the
   replacement of the UDP/IP path by an Ethernet path.  Optionally, a
   "Link Next Hop" capability allows routes to be installed with a
   router on the same Ethernet segment as the next hop, identified
   either as the session peer itself or by its MAC address.  This
   enables forwarding over links that carry no interface addresses,
   including through route reflectors and route servers.
- **draft-prabel-cfrg-suf-hybrid-sigs-03** (new-draft, score 0, ignored_after_review) [none]: [Hybrid Digital Signatures with Strong Unforgeability](https://datatracker.ietf.org/doc/draft-prabel-cfrg-suf-hybrid-sigs/) — This document proposes two PQ/T (Post-Quantum/Traditional) hybrid
   signature constructions that achieve strong unforgeability under
   chosen-message attacks (SUF-CMA).  The first, a black-box
   construction, achieves SUF-CMA security provided that the second
   component (typically the post-quantum one) is SUF-CMA secure; it
   differs from the current composite hybrid approach by binding the
   second (post-quantum) signature to the concatenation of the message
   and the first (traditional) signature.  This approach ensures that
   hybrid signatures maintain SUF-CMA security even when the first
   component only provides EUF-CMA security.

   The second, a non-black-box construction, requires the first
   (traditional) component to be built from the Fiat-Shamir paradigm,
   and binds the post-quantum signature directly into that component's
   challenge computation rather than treating it as an opaque sign/
   verify oracle.  This variant is SUF-CMA secure as long as at least
   one of the two components is SUF-CMA secure.
- **draft-prz-lsr-ash-packets-08** (new-draft, score 0, ignored_after_review) [none]: [IS-IS Aggregated SNP Hash Packets](https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/) — The document presents an optional new type of database
   synchronization packet called an Aggregated SNP Hash (ASH).  When
   feasible, it compresses traditional SNP exchanges into a dynamic
   Merkle tree-like structure, which speeds up synchronization of large
   databases and adjacency numbers while reducing the load from regular
   CSNP exchanges during normal operation.  Just like CSNPs and PSNPs,
   ASH packets come in two flavors, called Complete ASH (CASH) and
   Partial ASH (PASH).
- **draft-przygienda-lsr-fast-flooding-rtx-indication-01** (new-draft, score 0, ignored_after_review) [none]: [Retransmission Indication for IS-IS Fast Flooding](https://datatracker.ietf.org/doc/draft-przygienda-lsr-fast-flooding-rtx-indication/) — [RFC9681] defines a Flooding Parameters TLV.  Among other things, it
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
   normatively specified reaction to observed retransmission, fast
   flooding at scale can degenerate into sustained retransmission storms
   that serve only to keep the window full.

   This document specifies a local backoff.  A node reduces the
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
- **draft-qin-bpm-rpki-rp-bench-00** (new-draft, score 0, ignored_after_review) [none]: [Benchmarking Methodology for RPKI Relying Party](https://datatracker.ietf.org/doc/draft-qin-bpm-rpki-rp-bench/) — This document defines a benchmarking methodology for evaluating RPKI
   Relying Party (RP) implementations in controlled laboratory
   environments.  The methodology focuses on whether RP implementations
   correctly perform required validation steps and on the performance of
   these operations.  RP implementations are treated as black boxes,
   enabling consistent and objective assessment based on externally
   observable behavior rather than internal design or implementation
   details.
- **draft-ramadan-moq-fec-01** (new-draft, score 0, ignored_after_review) [none]: [Forward Error Correction for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-fec/) — This document specifies a mechanism for transmitting Forward Error
   Correction (FEC) repair data alongside source media in Media over
   QUIC (MoQ) sessions.  It defines catalog-based signaling of FEC
   configuration, including a derived RaptorQ Object Transmission
   Information that needs no in-session messages.  It also defines
   conventions for repair track naming, the format of repair objects,
   and two block profiles that fix how source symbols and FEC blocks are
   formed and identified: an ISO/IEC 23008-1 profile for tracks packaged
   as MPEG Media Transport Protocol (MMTP) packets, and an object
   profile for tracks packaged as Low Overhead Media Container (LOC) or
   Common Media Application Format (CMAF) objects.  It fully specifies
   two FEC schemes: the systematic Reed-Solomon code over GF(2^8) of
   ISO/IEC 23008-10, which is mandatory to implement, and RaptorQ (RFC
   6330), which is optional.  An algorithm registry provides extension
   points for additional schemes.  FEC enables receivers to recover from
   packet loss without retransmission latency.  The MMTP profile is
   designed for compatibility with ATSC 3.0 (A/331) and ARIB STD-B60
   broadcast systems.
- **draft-ramadan-moq-mmt-01** (new-draft, score 0, ignored_after_review) [none]: [MPEG Media Transport (MMT) Packaging for Media over QUIC](https://datatracker.ietf.org/doc/draft-ramadan-moq-mmt/) — This document specifies the use of MPEG Media Transport (MMT) as a
   container format for Media over QUIC (MoQ).  MMT carries media over
   broadcast (ATSC 3.0, ARIB STD-B60), multicast, and unicast (QUIC/
   WebTransport) networks.  This specification defines the mapping of
   MMT packets to MoQ objects, interaction with Application-Layer FEC,
   the derivation of MoQ catalogs from MMTP signaling, and compatibility
   considerations for both ATSC 3.0 and ARIB STD-B60 systems.
- **draft-rankin-ccsv-03** (new-draft, score 0, ignored_after_review) [none]: [Common Format and Media Type for Control-Character-Separated Values (CCSV) Files](https://datatracker.ietf.org/doc/draft-rankin-ccsv/) — This document specifies the Control-Character-Separated Values (CCSV)
   file format, a UTF-8 encoded tabular data format that uses ASCII
   control characters as field and record separators.  CCSV is intended
   for exchanging structured, rectangular data between applications such
   as databases, spreadsheets, statistical software, and data conversion
   utilities.  This document also specifies the text/csv media type for
   CCSV files.
- **draft-rosomakho-idr-bgp-masque-tunnel-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Signaling of MASQUE Tunnel Encapsulation](https://datatracker.ietf.org/doc/draft-rosomakho-idr-bgp-masque-tunnel/) — This document defines BGP Tunnel Encapsulation Attribute tunnel types
   for MASQUE CONNECT-TCP, CONNECT-UDP, CONNECT-IP, and CONNECT-
   ETHERNET.  It also defines URI Template and SVCB Parameters Sub-TLVs
   for advertising the MASQUE proxy endpoint, the HTTP request target
   template, and extensible connection parameters used to establish the
   corresponding MASQUE tunnel.
- **draft-rundgren-cbor-simple-4-csf-02** (new-draft, score 0, ignored_after_review) [none]: [CBOR "simple" values for CSF](https://datatracker.ietf.org/doc/draft-rundgren-cbor-simple-4-csf/) — This document defines two CBOR "simple" values to be used as unique
   (reserved) labels in a CBOR map holding an embedded signature
   construct.
- **draft-santesson-r2ps-04** (new-draft, score 0, ignored_after_review) [none]: [Remote Two-factor Protected Services](https://datatracker.ietf.org/doc/draft-santesson-r2ps/) — This document defines a generic service exchange protocol where
   service exchange data is protected and bound to a physical user using
   1 or 2 factors (1FA and 2FA).  The protocol facilitates registration
   and verification of either a knowledge-factor or a biometric factor
   in addition to a possession factor as means of achieving 2 factor
   protection.
- **draft-seemann-tsvwg-udp-fragmentation-03** (new-draft, score 0, ignored_after_review) [none]: [Controlling IP Fragmentation on Common Platforms](https://datatracker.ietf.org/doc/draft-seemann-tsvwg-udp-fragmentation/) — When performing Path MTU Discovery (PMTUD) over UDP, applications
   must prevent fragmentation of UDP datagrams both by the sender's
   kernel and during network transit.  This document provides guidance
   for implementers on configuring socket options to prevent
   fragmentation of IPv4 and IPv6 packets across commonly used
   platforms.
- **draft-sidor-pce-multipath-metric-00** (new-draft, score 0, ignored_after_review) [none]: [Signaling Per-Path Metric in the Path Computation Element Communication Protocol (PCEP)](https://datatracker.ietf.org/doc/draft-sidor-pce-multipath-metric/) — The Path Computation Element Communication Protocol (PCEP) extensions
   for signaling multipath information allow multiple forwarding paths
   to be associated with a single PCEP Label Switched Path (LSP); for
   Segment Routing (SR) Policy, these paths are the Segment Lists of a
   Candidate Path.  However, the METRIC object remains encoded at the
   LSP level, and per-path encoding of the METRIC object is explicitly
   left out of scope.

   This document extends PCEP to signal per-path (for SR Policy, per
   Segment List) metric information by reusing the existing METRIC
   object within the multipath constructs, and defines the associated
   capability negotiation.
- **draft-smith-6man-anycast-local-sock-opt-01** (new-draft, score 0, ignored_after_review) [none]: [An IPV6_ANYCAST_LOCAL Socket Option](https://datatracker.ietf.org/doc/draft-smith-6man-anycast-local-sock-opt/) — IPv6 nodes will deliver packets destined to an anycast address to one
   of their own local instances of the anycast address should they
   exist.  There are cases where it could be useful for a node to ignore
   its own anycast address instances and to submit packets towards this
   anycast address to the network for delivery to another node holding
   the anycast address.  This memo describes a Sockets API socket option
   to specify this behaviour.
- **draft-song-lamps-cms-composite-frodokem-01** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/draft-song-lamps-cms-composite-frodokem/) — This document specifies the conventions for using Composite FrodoKEM
   algorithms with the Cryptographic Message Syntax (CMS).  Composite
   FrodoKEM combines FrodoKEM with traditional algorithms (RSA-OAEP,
   X25519, X448) to provide hybrid post-quantum key encapsulation.
- **draft-song-lamps-pq-composite-frodokem-01** (new-draft, score 0, ignored_after_review) [none]: [Composite FrodoKEM for use in X.509 Public Key Infrastructure](https://datatracker.ietf.org/doc/draft-song-lamps-pq-composite-frodokem/) — Composite FrodoKEM defines combinations of FrodoKEM with RSA-OAEP,
   X25519, and X448.  This document specifies the algorithm definitions,
   key formats, and certificate conventions for using Composite FrodoKEM
   in the X.509 Public Key Infrastructure.
- **draft-soulard-anima-grasp-router-problem-statement-02** (new-draft, score 0, ignored_after_review) [none]: [GRASP through routers: a Problem Statement](https://datatracker.ietf.org/doc/draft-soulard-anima-grasp-router-problem-statement/) — This document analyzes challenges for using the GeneRic Autonomic
   Signaling Protocol (GRASP) in the context of deployment of services
   on machines (servers, Virtual Machines, etc) without the network
   elements, such as routers, needing any support for GRASP by
   themselves.  It analyses issues regarding the discovery mechanism,
   including discovery across subnets and operation across
   administrative boundaries, and provides terminology and general
   considerations for the development of future extensions, profiles,
   and architectural refinements.
- **draft-spk-httpbis-client-groups-00** (new-draft, score 0, ignored_after_review) [none]: [Client Groups for Shared HTTP Connections](https://datatracker.ietf.org/doc/draft-spk-httpbis-client-groups/) — Intermediaries often carry requests from many unrelated clients over
   one HTTP/2 or HTTP/3 connection to an origin server.  The origin has
   no way to know this, to say whether it accepts it, or to act on the
   traffic of one client without disturbing every other client on the
   connection.  This document defines a pair of settings that let an
   intermediary and an origin agree on whether a connection is shared, a
   request header field that marks which client a request belongs to,
   and a frame that lets the origin drain, block, or limit one client on
   a shared connection.  It also states what an intermediary needs to do
   so that GOAWAY and connection failures reach only the affected client
   streams.
- **draft-sullivan-tls-xof-schedule-01** (new-draft, score 0, ignored_after_review) [none]: [XOF-based key schedules for TLS 1.3](https://datatracker.ietf.org/doc/draft-sullivan-tls-xof-schedule/) — TLS 1.3 runs its entire key schedule on HKDF over SHA-2.  This
   document defines an extension that replaces that schedule with one
   built on an extendable-output function (XOF): the negotiated KDF
   governs every derivation, the Finished and binder MACs, and the
   transcript hash, so no SHA-2 remains in the key schedule.  The cipher
   suites, AEAD algorithms, state machine, and record layer are
   unchanged, and a connection without the extension uses HKDF as today.
   Two KDFs are defined, SHAKE256 and the reduced-round TurboSHAKE256.
   This document updates RFC 9147, RFC 9258, RFC 9261, and RFC 9849.
- **draft-svg-tiny-ps-abrotman-13** (new-draft, score 0, ignored_after_review) [none]: [SVG Tiny Portable/Secure](https://datatracker.ietf.org/doc/draft-svg-tiny-ps-abrotman/) — This document specifies SVG Tiny Portable/Secure (SVG Tiny PS) -- A
   Scalable Vector Graphics (SVG) profile to be used with documents that
   are intended for use with more secure requirements, and in some
   cases, in conjunction with a limited rendering engine.
- **draft-thomson-httpbis-chic-00** (new-draft, score 0, ignored_after_review) [none]: [Chained Hash Integrity Coding for HTTP](https://datatracker.ietf.org/doc/draft-thomson-httpbis-chic/) — This describes a content-coding for HTTP that enables progressive
   processing of content, without sacrificing integrity.
- **draft-toutain-schc-coreconf-management-02** (new-draft, score 0, ignored_after_review) [none]: [CORECONF Rule management for SCHC](https://datatracker.ietf.org/doc/draft-toutain-schc-coreconf-management/) — This document describes how CORECONF can be applied to SCHC for
   context and rule set management between endpoints.  It also defines a
   YANG module with an RPC to duplicate an existing Rule and apply some
   modifications, and an RPC to reset the Set of Rules to its initial
   content.
- **draft-wagope-dnsop-do-bit-00** (new-draft, score 0, ignored_after_review) [none]: [Clearing the DO bit for DNSSEC](https://datatracker.ietf.org/doc/draft-wagope-dnsop-do-bit/) — { Editor note: THIS IS A WORKING IDEA FOR DISCUSSION.

   It might be the best idea ever... or the worst idea ever.  The
   authors really cannot decide (or even agree among themselves), but I
   have written this up as as an ID to share it with the WG.  Please
   understand that we are simply floating the idea; if it turns out that
   it is the worse idea ever, we'll happily drop it and save ourselves a
   bunch of work! :-) }

   The DNSSEC OK (DO) bit is an EDNS0 flag used in DNS queries to signal
   that the requestor wishes to receive DNSSEC resource records (such as
   RRSIG, DNSKEY, DS, and NSEC) in the response.

   This bit is named DNSEC OK (DO) as an indication that the resolver
   implementation will not die if it receives DNSSEC records, not that
   it is actually performing DNSSEC validation.

   It is important to note that clearing the DO bit means that the
   authoritative server will not include DNSSEC records in its response,
   even if they exist.

   One of the concerns around Post Quantum Cryptography (PQC) is that
   the resulting DNSSEC signatures may be significantly larger than
   current signatures.  This could exacerbate issues related to DNS
   message size and fragmentation, and cause many connections to fail
   back to TCP.Clearing the DO bit can help mitigate these issues by
   preventing the inclusion of potentially large DNSSEC records in
   responses, but it also means that resolvers will not have access to
   the DNSSEC proofs necessary for validation.
- **draft-wang-grow-bmp-attribute-sets-stats-00** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for BGP Path Attribute Sets and Statistics](https://datatracker.ietf.org/doc/draft-wang-grow-bmp-attribute-sets-stats/) — The BGP Monitoring Protocol (BMP) specified in RFC 7854 requires a
   monitored router to send full BGP Path Attributes for every Route
   Monitoring message.  In networks with a large number of prefixes
   sharing identical BGP Path Attributes, this requirement leads to
   substantial transmission redundancy and protocol overhead.

   This document specifies a decoupled architecture for BMP monitoring
   that separates Path Attribute Set registration from NLRI volume
   statistics.  Attribute updates are triggered immediately upon path
   attribute changes, while NLRI count updates can be configured for
   either event-driven (immediate) or periodic reporting modes, with
   mandatory instant notification when an attribute set's reference
   count drops to zero.
- **draft-wang-idr-bgp-nof-nlri-04** (new-draft, score 0, ignored_after_review) [none]: [Distribution of Device Discovery Information in NVMe Over RoCEv2 Storage Network Using BGP](https://datatracker.ietf.org/doc/draft-wang-idr-bgp-nof-nlri/) — This document proposes a method of distributing device discovery
   information in NVMe over RoCEv2 storage network using the BGP
   routing protocol. A new BGP Network Layer Reachability Information
   (NLRI) encoding format, named NoF NLRI, is defined.
- **draft-wang-idr-flowspec-dip-origin-as-filter-19** (new-draft, score 0, ignored_after_review) [idr]: [Destination-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-dip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr-
   fsv2-ip-basic] to enable filtering based on the Origin Autonomous
   System (AS) of the destination IP address.  This extension is
   particularly useful in mitigating Distributed Denial of Service
   (DDoS) attacks or optimizing traffic redirection where the target IP
   addresses are numerous or rapidly changing, but belong to a specific
   destination Origin AS.
- **draft-wang-idr-flowspec-sip-origin-as-filter-06** (new-draft, score 0, ignored_after_review) [idr]: [Source-IP-Origin-AS Filter for BGP Flow Specification](https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-sip-origin-as-filter/) — This document defines an extension to the Border Gateway Protocol
   (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr-
   fsv2-ip-basic] to enable filtering based on the Origin Autonomous
   System (AS) of the source IP address.  This extension is particularly
   useful in mitigating Distributed Denial of Service (DDoS) attacks
   where the source IP addresses are dynamic or numerous but belong to a
   specific source AS.
- **draft-wang-rtgwg-dragonfly-routing-problem-05** (new-draft, score 0, ignored_after_review) [none]: [Routing mechanism in Dragonfly Networks Gap Analysis, Problem Statement, and Requirements](https://datatracker.ietf.org/doc/draft-wang-rtgwg-dragonfly-routing-problem/) — This document provides the gap analysis of existing routing mechanism
   in Dragonfly networks, describes the fundamental problems, and
   defines the requirements for technical improvements.
- **draft-watts-eqr-conformance-05** (new-draft, score 0, ignored_after_review) [none]: [Deterministic Conformance Profile and Test Vectors for Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-eqr-conformance/) — This document defines a deterministic conformance profile and test-
   vector corpus for Evidence Qualification Receipts (EQRs).  The
   profile, named eqr-core-1, makes receipt conformance mechanically
   reproducible: strict JSON structure, SHA-256 digest encoding, UTC
   timestamp handling, evidence-reference integrity, requirement-state
   derivation, and three-valued PASS, FAIL, or INDETERMINATE results are
   checked by a closed algorithm.  The profile is intentionally narrow.
   Conformance does not establish that evidence is true, that a
   proposition is scientifically valid, that an issuer is trustworthy,
   or that an action is authorized.  The goal is interoperable
   verification of receipt semantics, not promotion of conformance into
   substantive truth.
- **draft-watts-hagth-framework-01** (new-draft, score 0, ignored_after_review) [none]: [Human-Accelerated Geophysical Threshold Framework](https://datatracker.ietf.org/doc/draft-watts-hagth-framework/) — This document defines an informational research framework for
   describing anthropogenic perturbations that alter the timing,
   probability, coupling, or consequence of threshold transitions in
   geophysical systems without requiring anthropogenic dominance of the
   system's primary energy source.
- **draft-watts-octatouch-smoke-test-profile-01** (new-draft, score 0, ignored_after_review) [none]: [OctaTouch Gesture Runtime: Smoke-Test Behavior Profile](https://datatracker.ietf.org/doc/draft-watts-octatouch-smoke-test-profile/) — This document records five expected behaviors asserted by a supplied
   OctaTouch gesture-runtime smoke-test script.  It is a limited test
   profile, not a complete gesture specification.  The runtime
   implementation and its dependencies were not included with the source
   script, so the tests have not been executed as part of this archive.
   No interoperability or implementation-conformance claim is made.
- **draft-watts-scientific-admissibility-01** (new-draft, score 0, ignored_after_review) [none]: [Scientific Admissibility Evidence Records: A Research Data Exchange Proposal](https://datatracker.ietf.org/doc/draft-watts-scientific-admissibility/) — This document proposes interoperable evidence record fields for
   reproducible research workflows.  It is an independent working draft
   and is not an IETF publication or standard.
- **draft-wiggers-tls-authkem-psk-06** (new-draft, score 0, ignored_after_review) [none]: [KEM-based pre-shared-key handshakes for TLS 1.3](https://datatracker.ietf.org/doc/draft-wiggers-tls-authkem-psk/) — This document gives a construction in which (long-term) KEM public
   keys are used in the place of TLS PSK keys, avoiding concerns that
   may affect systems that use symmetric-key-based PSK, such as
   requiring key diversification and protection of symmetric-keys'
   confidentiality.

   This mechanism is inspired by AuthKEM (and could use AuthKEM
   certificate public keys for resumption), but can be independently
   implemented.
- **draft-wu-grow-bmp-multi-instance-02** (new-draft, score 0, ignored_after_review) [none]: [BMP Extension for Monitoring Multiple BGP Instances](https://datatracker.ietf.org/doc/draft-wu-grow-bmp-multi-instance/) — The BGP Monitoring Protocol (BMP), as defined in RFC 7854, provides a
   means for monitoring BGP sessions.  In deployments where a single
   device runs multiple BGP instances simultaneously - typically a base
   instance together with one or more additional instances, each
   identified by an Instance Name and potentially running in a separate
   process with an independent Router-ID and Autonomous System (AS)
   number - the existing BMP message format does not allow a Monitoring
   Station to distinguish peers or routes belonging to different BGP
   instances on the same monitored router.

   This document defines a new BMP Type-Length-Value (TLV) element, the
   BGP Instance Name TLV, that carries the Instance Name of the BGP
   instance associated with a given peer or route.  Following the TLV
   extension framework defined in [I-D.ietf-grow-bmp-tlv], the new TLV
   MAY appear in Peer Up Notification, Peer Down Notification, Route
   Monitoring, Statistics Report, and Route Mirroring messages.  The TLV
   enables a Monitoring Station to unambiguously attribute monitored BGP
   information to the correct BGP instance on the monitored router.
- **draft-xl-pce-pcep-pathrate-00** (new-draft, score 0, ignored_after_review) [none]: [PCEP Extension for Path Rate](https://datatracker.ietf.org/doc/draft-xl-pce-pcep-pathrate/) — This document specifies extensions for PCEP to carry a Path Rate
   (PRate), enabling a PCE to compute and distribute the maximum
   sustainable rate for an end-to-end path.  A new METRIC type and a new
   objective function are defined.
- **draft-xzl-fann-srv6-rate-notification-00** (new-draft, score 0, ignored_after_review) [none]: [SRv6-based Fast Rate Notification](https://datatracker.ietf.org/doc/draft-xzl-fann-srv6-rate-notification/) — This document specifies a fast rate notification mechanism for
   Segment Routing over IPv6 (SRv6) networks.  It enables a transit or
   egress node to dynamically notify the ingress (headend) node about a
   recommended rate range (MinRate and MaxRate) when localized
   congestion is detected or when underutilized bandwidth is identified,
   allowing the headend to perform proactive traffic shaping and rate
   enforcement.  This mechanism enhances transmission efficiency in SRv6
   networks by enabling fine-grained, congestion-aware rate control.
- **draft-yang-opsawg-ipfix-rocev2-sequence-00** (new-draft, score 0, ignored_after_review) [none]: [IPFIX Export of RoCEv2 Sequence Observations](https://datatracker.ietf.org/doc/draft-yang-opsawg-ipfix-rocev2-sequence/) — This document specifies an IP Flow Information Export (IPFIX)
   metering and export profile for bounded Packet Sequence Number (PSN)
   observations on provisioned RoCEv2 Reliable Connection SEND and RDMA
   WRITE request streams.  It defines cumulative observations of
   skipped, subsequently observed, expired, repeated, and unclassified
   sequence positions, with explicit observation epochs and
   qualification flags.

   The profile requires complete observation of the provisioned stream
   and defines no packet-loss estimator, retransmission detector, or
   congestion-control action.  Twelve Information Elements describe the
   observation state.  Existing RoCEv2 header Information Elements
   identify the monitored stream.
- **draft-yang-pce-pcep-over-quic-06** (new-draft, score 0, ignored_after_review) [none]: [PCEP over QUIC](https://datatracker.ietf.org/doc/draft-yang-pce-pcep-over-quic/) — This document specifies the use of QUIC streams to implement the PCEP
   protocol for efficient and secure data transmission.
- **draft-yl-bpm-cats-00** (new-draft, score 0, ignored_after_review) [none]: [Benchmarking Methodology for Computing-aware Traffic Steering](https://datatracker.ietf.org/doc/draft-yl-bpm-cats/) — Computing-aware traffic steering (CATS) is a traffic engineering
   approach for steering service requests towards appropriate service
   instances based on the awareness of both computing and network
   information.  This document proposes benchmarking methodologies for
   CATS.
- **draft-yourtchenko-intarea-internet-checksum-00** (new-draft, score 0, ignored_after_review) [none]: [On Calculating and Updating the Internet Checksum](https://datatracker.ietf.org/doc/draft-yourtchenko-intarea-internet-checksum/) — Over the past four decades, the Internet checksum has been used by
   many protocols: IPv4, TCP, UDP, and others.  The practical details
   related to calculation and updates are scattered across different
   RFCs.  Several protocols introduce special-case handling for +0 and
   -0, thus making the term "Internet checksum" ambiguous.  This affects
   any protocol implementation which modifies the data covered by any
   variant of the Internet checksum.  This document provides the problem
   statement and outlines the scope for potential future work to build a
   consolidated source for the Internet checksum.  If there is interest
   in such work, this document may be converted into that consolidated
   specification.
- **draft-yuan-quic-congestion-data-03** (new-draft, score 0, ignored_after_review) [none]: [Exchanging Congestion Control Data in QUIC](https://datatracker.ietf.org/doc/draft-yuan-quic-congestion-data/) — This draft defines a new transport frame which enables consenting
   endpoints to share congestion control state about the network
   connection for various purposes, including client-side adaptive
   bitrate selection during an ongoing connection.  It also allows an
   endpoint's own congestion control state to be echoed back to it by a
   peer for consideration at the beginning of a future connection.
- **draft-yuyou-moq-v3c-00** (new-draft, score 0, ignored_after_review) [none]: [Transport of V3C Bitstreams over Media over QUIC Transport (MOQT)](https://datatracker.ietf.org/doc/draft-yuyou-moq-v3c/) — This document specifies a mapping and packaging for transporting ISO/
   IEC 23090-5 Visual Volumetric Video-based Coding (V3C) bitstreams
   over Media over QUIC Transport (MOQT).  The mapping uses the MOQT
   Streaming Format (MSF): V3C configuration is MSF initialization data,
   each independently consumable V3C component is an MSF track, a V3C
   composition unit is a MOQT Group, and a coded V3C unit is a MOQT
   Object.  Relays remain unaware of V3C syntax.  V3C knowledge is
   confined to the streaming-format layer.
- **draft-zhang-dnssec-wildcard-validation-02** (new-draft, score 0, ignored_after_review) [none]: [Signer-Zone Containment for DNSSEC Wildcard Validation](https://datatracker.ietf.org/doc/draft-zhang-dnssec-wildcard-validation/) — Validators for the DNS Security Extensions (DNSSEC) reconstruct the
   original owner name of a signed resource record set (RRset) using the
   RRSIG Labels field.  This document updates RFC 4035 to make explicit
   how its existing signing-zone authority requirement applies to that
   reconstructed owner, and updates RFC 8198 to preserve the
   authenticated association between wildcard data, its original owner,
   and its signing zone during cache reuse.  These clarifications
   prevent cryptographically correct signatures from being treated as
   authenticating wildcard sources outside the signing zone.  They do
   not change DNS wildcard matching or synthesis rules, or DNS message
   formats.
- **draft-zhuang-grow-bmp-enhancement-for-vrf-loc-rib-02** (new-draft, score 0, ignored_after_review) [none]: [Enhancement for Monitoring VRF's Loc-RIB](https://datatracker.ietf.org/doc/draft-zhuang-grow-bmp-enhancement-for-vrf-loc-rib/) — BMP Loc-RIB [RFC9069] enforces that the BMP router sets the Peer
   Address value of a VPN route information to zero, and sets the Peer
   Distinguisher value of a VPN route information to the route
   distinguisher or unique locally defined value of the particular
   instance the Loc-RIB belongs to.  This document introduces the option
   to communicate the Remote VRF Information from which a VPN route was
   received when reporting that VPN route information with BMP Loc-RIB.
- **draft-zzhang-bier-unmasked-bier-02** (new-draft, score 0, ignored_after_review) [none]: [Unmasked BIER Mode](https://datatracker.ietf.org/doc/draft-zzhang-bier-unmasked-bier/) — The document introduces a new mode of interpretation of the bitmask
   field in the BIER encoding, called unmasked BIER, that solves the
   problem of BIER originator targeting receivers across many different
   sets and hence, in worst case, degrading into ingress replication.
- **draft-zzhang-pim-bidir-multiplane-fat-tree-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for PIM-Bidir in Multi-Planed Fat Trees](https://datatracker.ietf.org/doc/draft-zzhang-pim-bidir-multiplane-fat-tree/) — Modern Data Centers are increasingly adopting multi-plane.  This
   brings unique challenges for RP-based mulitcast.  This document
   discusses considerations for RP placement for PIM-Bidir in multi-
   plane fat tree networks, and considerations for multicast with RIFT
   signaling.

## Errors / fetch failures

_None._
