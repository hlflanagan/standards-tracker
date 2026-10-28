# IETF Identity + AI Standards Watch

Date: 2026-10-28

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
- **draft-zambo-aer1-26** (new-draft, score 39, core_identity) [none]: [AER-1: A Portable Execution Receipt for AI Agent Tool Calls](https://datatracker.ietf.org/doc/draft-zambo-aer1/) — This document specifies AER-1, a small vocabulary for recording one
   AI agent tool call as a portable, independently checkable execution
   receipt.  A receipt identifies the execution, records when it
   happened, preserves the canonical bytes used for the output
   commitment, names the tool and caller scope, carries a provenance
   class, and resolves at a stable public URL.  The format separates
   what the system observed from claims about the outside world, and it
   separates provenance (who ran or reported the action) from the record
   itself.  A reference implementation is deployed, and its receipts are
   publicly verifiable without an account or token.  The specification
   covers workflow receipts, which bind an ordered sequence of step
   receipts to a single goal with a Merkle root over the step sequence,
   and hash-chained job timelines for tamper-evident sequencing of
   executions.  This revision closes honesty and precision gaps: it adds
   the workflow-receipt truncation limit (new Section 8.4), normatively
   specifies the external anchor format and its verification procedure
   (rewritten Section 10, new Section 10.1), fixes a RECOMMENDED/MUST
   contradiction in Section 8.1, makes the Section 6 verification step
   testable, and documents replay, low-entropy, empty-record, and size-
   limit considerations.  It changes no receipt field, digest
   construction, or existing verification rule.  The -13 revision fixes
   a malformed sentence in the Abstract, three incorrect section cross-
   references, stale Table of Contents page numbers, a skipped footer
   page number, misaligned table rows, and chain version-string updates,
   and records two reported interoperability examples in Implementation
   Status; it changes no receipt field, digest construction, or
   verification rule.  The -14 revision adds tamper-evident metadata
   binding (new Section 3.1; conditional metadata_hash for schema 0.4
   and later), disambiguates the anchor receipt_id (Table 4), corrects
   the self-anchoring witnessing claim (Section 10), makes the
   Section 8.3 display rule a SHOULD with a byte-testable MUST, narrows
   the provenance attestation wording (Section 5), states the binding
   non-transfer rule normatively (new Section 10.2), pins
   anchored_digest to bare hex (Table 4), corrects the vector corpus
   counts, and adds normative disclosure of missing issuer
   authentication.  It changes no existing receipt field, digest
   construction, or verification rule for schema 0.3 and earlier.  The
   -15 revision narrows the Implementation Status wording for the
   reported interoperability examples at the implementer's request; it
   changes no receipt field, digest construction, or verification rule.
   The -16 revision documents the live workflow tools API (new Sections
   8.5, 8.6, 8.7): the workflow_close tool, workflow metadata in step
   receipts, and the workflow view API.  It changes no receipt field,
   digest construction, or existing verification rule.  The -17 revision
   documents the recommended execution_context member (new Section 3.2):
   an optional, non-core structure for recording source and version
   context such as the model name and version behind a tool call and the
   identity of the source system acted upon.  It changes no existing
   receipt field, digest construction, or verification rule.  The -18
   revision repairs the reference apparatus (normative references to RFC
   3339, RFC 8259, RFC 4122, and RFC 4648, and the previously missing
   RFC 7942 entry), pins two parser edge cases (duplicate JSON member
   names and leap-second timestamps are rejected), names the Unicode
   normalization behavior in Section 4 with a computed vector pair,
   adopts the unknown-versus-not-applicable convention for optional
   members, adds optional members for readback outcomes, per-field
   provenance, negative records, reversal state, method descriptors, and
   payment references, completes the execution_context member set (model
   and environment digests), adds the optional input_hash commitment
   (Section 3.3), permits SCITT and RFC 3161 anchors under Section 10,
   states the clock-trust and equivocation limits in Section 13, and
   rewrites Section 15 to position the specification against adjacent
   work.  It changes no receipt field, digest construction, or
   verification outcome for any receipt well-formed under the -17 rules.
   The -19 revision aligns the workflow tool and workflow view
   descriptions in Sections 8.5 and 8.7 with the normative Merkle
   construction in Section 8.1: both descriptions named step output
   hashes as the root's leaf input where Section 8.1 specifies step
   receipt identifiers.  An implementer report identified the
   divergence.  It changes no construction, receipt field, digest, or
   verification outcome.  The -20 revision adopts three findings
   reported by an independent implementer who built a conformance
   verifier from the -19 text alone.  It requires the published byte
   layout of a recorded input to state the member ordering rule it
   applies when the input is a JSON object (Section 3.3), and it bars
   control characters from provenance class labels, with rejection
   required (Section 5).  The conformance kit's quickstart core tier
   also gains the provenance-label and schema-version metadata checks as
   a stated rule.  It changes no receipt field or digest construction; a
   receipt well-formed under the -19 rules verifies identically, except
   that an input commitment whose published layout states no ordering
   rule is no longer reported as confirmed.  The -21 revision states the
   receipt-id binding rule normatively (Section 6), describes the id-
   substitution case in Security Considerations (Section 13), and
   credits the independent control test that produced the finding
   (Section 18).  It changes no receipt field, digest construction, or
   existing verification rule.  The -22 revision pins the legacy (schema
   0.3) member forms that satisfy the core requirements and requires
   verifiers to report a legacy acceptance explicitly rather than as a
   plain pass (Section 6), requires the canonical base64 spelling of
   canonical_bytes and the rejection of non-canonical spellings
   (Sections 3 and 4), states that the receipt object is the document
   and that no presentation envelope is part of the format (Section 3),
   enumerates the id verdict a verifier reports beside the structural
   verdict, binds the states to verifier behavior, and states the
   resolution order between the two layers (Section 6), requires the
   reason to be printed next to the rule for every check that does not
   pass (Section 6), and records an independent production validator in
   the Implementation Status.  It changes no receipt field or digest
   construction; one verification outcome changes, for a receipt whose
   canonical_bytes spelling is not canonical, which earlier revisions
   did not address.  The -23 revision states the per-anchor outcome
   report normatively (Section 6): a verifier's report carries each
   anchor's outcome in machine-visible form, and an anchor the verifier
   did not evaluate is reported as "not checked", never as an evaluated
   outcome, so that state cannot be conflated with an anchor that was
   evaluated and could not be resolved.  It changes no receipt field,
   digest construction, or existing verification rule.

Implementation Status

   This section records the implementation status of the AER-1
   vocabulary at the time of this revision, following [RFC7942].  It
   will be removed before publication as an RFC.

   Reference implementation.  Zambo (https://zambo.dev), operated by the
   document author, is a deployed implementation of Sections 3 through
   10.  Tool calls made over HTTPS as JSON-RPC to https://zambo.dev/api/
   mcp receive a public receipt page at https://zambo.dev/run/<id>,
   retrievable without an account, wallet, or token.  A machine-readable
   verifier is exposed as described in Section 6.  Receipts are anchored
   to public Nostr relays with an envelope binding the receipt
   identifier, the output hash, and the evidence hash (envelope "zambo-
   receipt-anchor/1").

   Workflow receipts (Section 8) are deployed in the reference
   implementation.  Multi-step sessions receive a workflow receipt at
   https://zambo.dev/workflow/<workflow_id> binding the ordered step
   receipts with a Merkle root, and step receipt pages link to the
   parent workflow ("Part of workflow") while workflow pages link to
   each step receipt.

   Since 2026-10-22, the reference implementation closes workflows under
   the seq-output-v1 construction and declares merkle_version on every
   new workflow receipt; workflow receipts issued before that date carry
   no merkle_version member and remain verifiable under receipt-id-v0
   exactly as issued.  This revision defines both constructions and the
   selector.  The conformance corpus described below now carries seq-
   output-v1 vectors as well, including multi-step closes, the odd-level
   duplication case, a single-step close, and mixed-version cases in
   which a single verifier checks closes under both constructions, each
   keyed on the close's declared merkle_version.

   Conformance kit.  An open conformance suite for this vocabulary is
   maintained at https://gitlab.com/rambozambodotdev/zambo.  It ships
   seven bundled kit runners (Rust, Go, TypeScript, Python, Java, C#,
   and Swift), each verified against the full vector corpus, which at
   this revision stands at 124 vectors (127 checks per runner) across
   the receipt-level, Merkle (Section 8.1), timeline (Section 7),
   hardened chain (Section 7.1), chain commitment (Section 7.3),
   Unicode, id-binding, and anchor-report suites.  The kit repository
   publishes the corpus's current vector count, check count, and
   evaluated-set corpus digest alongside the corpus itself; that
   published record states the corpus's current counts, and if the
   corpus grows beyond the counts stated here, the published record
   governs.  The -22 revision adds vectors pinning the canonical base64
   spelling (Section 4), the nil-UUID rejection as a standalone case,
   the legacy schema 0.3 production shape (Section 6), the bare
   presentation form (Section 3), a current-schema (0.4) real receipt
   beside the two bundled 0.3 fixtures, and one vector per id_verdict
   state (Section 6).  The -23 revision adds the anchor-report vectors
   pinning the per-anchor outcome report of Section 6, implemented in
   the kit runners (kit v1.5.6) and in the reference verifier
   (aer1-verify 0.2.13) ahead of this text.  Each runner is zero-
   dependency within its language toolchain.  Running the Python suite
   takes two steps and no dependencies beyond git and a Python 3
   interpreter:

   git clone https://gitlab.com/rambozambodotdev/zambo.git python3 aer1-
   implementations/python/conformance.py
   Since the -23 revision, each conformance run also emits the evaluated
   vector set: one line per vector carrying its id and content digest,
   with a corpus digest over the set, so a claimed pass can be checked
   as a set difference against the full corpus.  The cross-runner parity
   gate mints a receipt of each of its runs (schema 0.4; the committed
   payload carries the evaluated vector ids, the corpus digest, and the
   verdict, pass or fail) and pins it in the kit repository as parity-
   gate-receipt.json; the gate verifies that receipt with the kit
   conformance check and with aer1-verify, id bound, before it reports
   success.

   An implementation is conformant when it produces byte-identical
   verdicts to the reference runners across the full vector corpus.  The
   corpus includes attack vectors for tampered provenance labels, schema
   version downgrades, and legacy (pre-0.4) receipts; conformance
   requires the Section 6 metadata checks to fail the first two and to
   report the third with a legacy notice rather than a failure.  The kit
   is versioned; the v1.5.7 release is the frozen reference for the
   corpus described above.

   Independent verification.  The Section 6 verification procedure has
   been exercised against live receipts by independent third parties:

   *  On 2026-09-16, an independent agent ("Merv", on the Clawstr
      network) verified a live receipt (id 0ec81343-cc1f-
      4c25-9c33-d76b5582406d) in three checks: the SHA-256 of the
      decoded canonical bytes matched the output commitment, the
      upstream evidence hash matched, and the anchor event carried a
      valid signature retrievable on independent relays.  The same party
      reported that the anchor envelope did not then bind the evidence
      hash; the reference implementation has since shipped the binding
      envelope described above.

   *  On 2026-09-16, an independent agent ("nilo_agent", on Nostr) ran
      adversarial verification challenges against live receipts,
      including a witness round and a strong-form Bitcoin-anchored
      challenge (anchor block 967351, receipt 88094e26), each answered
      with bytes the challenger could check independently.

   *  On 2026-09-25 and 2026-09-26, an independent agent ("Devan", on
      Nostr) published timestamped probe receipts (v1 and v2) exercising
      independent verification of agent work in the same receipt model.

   Independent validators.  An independent implementation exposes the
   Section 6 procedure as a public service:

   *  WhiteMagic Labs (Lucas Bailey) operates a production validator for
      this specification at https://api.whitemagic.dev/aer1/verify,
      publicly accessible without a key, with the same procedure also
      exposed as an MCP tool (verify_aer1_receipt).  On 2026-10-17 the
      operator exercised the validator against the reference
      implementation and the conformance corpus.  The two
      implementations initially disagreed on cases in both directions (a
      decoding boundary in the validator; an id-binding reading and a
      nil-UUID acceptance in the reference tooling), each disagreement
      was resolved against the draft text the same day, and the
      implementations now agree across the exercised case matrix.  The
      validator reports comparison outcomes in the shared states of
      Section 6 and attaches its provenance caution as advisory metadata
      beside the verdict, the arrangement the provenance note in
      Section 6 describes.

   Seven bundled kit runners for Sections 3 through 6 are maintained in
   the conformance kit repository (Rust, Go, TypeScript, Python, Java,
   C#, and Swift), each verified against the full vector corpus
   described above (124 vectors, 127 checks per runner).  These runners
   are the kit's own test runners, not independent implementations.
   Independent third-party implementations, built from the draft text
   alone without access to kit internals, include ARION's Node.js and
   Java verifiers and ColonistOne's Perl verifier, each conformant
   against the same corpus.  Since revision 12, contributors have
   reported two scoped interoperability exercises.  On 2026-10-08,
   Tanilo and the AER-1 author published a cross-repository worked
   example linking an AER-1 receipt to a live Tanilo receipt by
   canonical hash, with the AER-1 commitment check and the Tanilo
   signature check run separately, each under its own rules.  Also on
   2026-10-08, the independent builder FlyThink published a four-case
   fixture binding AER-1 execution receipts to physical completion
   claims; all four cases replay cleanly, including the case where a
   valid AER-1 receipt coexists with invalid physical-evidence binding
   (see Section 10.2).  Reports of additional implementations or
   independent verification results are solicited; implementers are
   encouraged to validate against the open conformance kit described
   above and to report their results.
- **draft-das-distributed-agent-authority-finality-00** (new-draft, score 31, authorization) [none]: [Distributed Authority and Execution-Finality for Multi-Agent Systems, Delegated Operations, and Cross-Domain Gateways](https://datatracker.ietf.org/doc/draft-das-distributed-agent-authority-finality/) — This informational document describes future-oriented distributed
   authority and execution-finality profiles for cooperating autonomous
   agents, delegated operations, external tools, cloud gateways, native
   resources, and cross-domain workflows.  It examines identity, non-
   amplifying delegation, provenance and influence lineage, transitive
   side effects, cross-agent collision management, policy convergence
   and downstream effectuation-boundary enforcement.  It distinguishes a
   proposed objective or authorized plan from authority for an actual
   resource effect.  Source-derived procedures, tests and algorithms are
   presented as implementation examples, not as evidence that identified
   vendors implement this proposed architecture.

   Industry Relevance: Recent public developments in autonomous AI-agent
   security and execution governance include Microsoft Execution
   Containers (MXC), Microsoft Agent Governance Toolkit ADR-0030
   (Action-Bound, Fail-Closed Approval Protocol), and Project
   Perception; Google Agent Gateway and Gemini Agent; Meta Muse/Sentinel
   AI-Agent Security Architecture; NVIDIA OpenShell Reference
   Architecture and NVIDIA Sentry; OpenAI Agents API, Codex, Agents SDK,
   and Responses API; and Anthropic Claude Managed Agents, Claude Code
   Sandboxing, and Claude Code Auto Mode.  These initiatives illustrate
   industry attention to agent isolation, independent policy
   enforcement, action-bound authorization, delegated authority,
   credential isolation, network-egress security, hardware-assisted
   containment, runtime supervision, and fail-closed controls.  This
   draft describes related proposed execution-finality mechanisms
   without asserting that these initiatives implement them.

   Relevance to the IETF: the mechanisms described here require common,
   interoperable objects and verification semantics across independently
   built components, including operation descriptors, act-bound non-
   bearer capabilities, finality-sink verification results, validation
   evidence, and authority, revocation, and containment generations.
   The document relates to existing IETF work on OAuth, GNAP, RATS,
   WIMSE, and SCITT, and asks the community whether and where this
   effectuation-boundary problem should be addressed.

   This document is intentionally long and is not repetitive: each
   profile specifies a distinct mechanism with its own algorithms,
   failure cases, and enforcement points, and the security properties
   depend on how these mechanisms combine.  A reduced excerpt would hide
   the conditions under which they fail closed, so this document and its
   two companion drafts, among which the profiles are divided, are meant
   to be evaluated as a whole.

   This draft builds on earlier Internet-Drafts by the same author, in
   particular draft-das-agent-execution-finality, and adds mechanism
   families not described there; the Introduction states precisely what
   was disclosed earlier and what is disclosed here.

   IPR: The technical content of this draft set is based upon the
   author's international application PCT/IB2026/055615, which forms the
   foundation of this disclosure and comprises approximately 300
   distinct, non-repetitive embodiments and enforcement points.  A
   separate patent application specific to the material in this draft
   set has also been filed.  Related Indian applications: 202531130665,
   202631000572, 202631001586, 202631002990, 202631124028, and
   202631125689.  Related international applications: PCT/IB2025/058316,
   PCT/IB2026/053385, PCT/IB2026/055615, PCT/IB2026/055760, PCT/
   IB2026/055870, PCT/IB2026/056058, PCT/IB2026/056809, and PCT/
   IB2026/056941.  These identify related technical disclosures; not all
   described mechanisms are necessarily patent-claimed or granted, and
   patent scope and priority depend on applicable law and examination.
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
- **draft-kamimura-vap-framework-02** (new-draft, score 27, trust_infrastructure) [none]: [Verifiable AI Provenance Framework (VAP): An Architectural Framework for Auditable AI Decision Trails](https://datatracker.ietf.org/doc/draft-kamimura-vap-framework/) — Automated decision-making systems, including AI and algorithmic
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
- **draft-ietf-wimse-identifier-04** (new-draft, score 25, core_identity) [wimse]: [Workload Identifier](https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/) — This document defines a canonical identifier for workloads, referred
   to as the Workload Identifier.  A Workload Identifier is a URI that
   uniquely identifies a workload within the context of a specific trust
   domain.  This identifier can be embedded in Workload Identity
   Credentials, including X.509 certificates and JWT-based tokens, to
   support authentication, authorization, and policy enforcement across
   diverse systems.  The Workload Identifier format ensures
   interoperability, facilitates secure identity federation, and enables
   consistent identity semantics.
- **draft-das-kernel-hardware-execution-finality-00** (new-draft, score 24, authorization) [none]: [Protected Execution-Finality Enforcement for Autonomous AI Agents Across Kernel, Hypervisor, Hardware, and Native-Resource Boundaries](https://datatracker.ietf.org/doc/draft-das-kernel-hardware-execution-finality/) — This document describes a proposed execution-finality architecture
   for autonomous agent workloads at kernel, hypervisor, device, and
   native-resource effectuation boundaries.  It distinguishes
   computation from authority to commit consequential effects, and
   documents protected validation, operation-bound evidence, scoped
   authorization, independent finality verification, revocation, and
   containment, alongside deployment profiles and illustrative
   algorithms and tests.

   Industry Relevance: Recent public developments in autonomous AI-agent
   security and execution governance include Microsoft Execution
   Containers (MXC), Microsoft Agent Governance Toolkit ADR-0030
   (Action-Bound, Fail-Closed Approval Protocol), and Project
   Perception; Google Agent Gateway and Gemini Agent; Meta Muse/Sentinel
   AI-Agent Security Architecture; NVIDIA OpenShell Reference
   Architecture and NVIDIA Sentry; OpenAI Agents API, Codex, Agents SDK,
   and Responses API; and Anthropic Claude Managed Agents, Claude Code
   Sandboxing, and Claude Code Auto Mode.  These initiatives illustrate
   industry attention to agent isolation, independent policy
   enforcement, action-bound authorization, delegated authority,
   credential isolation, network-egress security, hardware-assisted
   containment, runtime supervision, and fail-closed controls.  This
   draft describes related proposed execution-finality mechanisms
   without asserting that these initiatives implement them.

   Relevance to the IETF: the mechanisms described here require common,
   interoperable objects and verification semantics across independently
   built components, including operation descriptors, act-bound non-
   bearer capabilities, finality-sink verification results, validation
   evidence, and authority, revocation, and containment generations.
   The document relates to existing IETF work on OAuth, GNAP, RATS,
   WIMSE, and SCITT, and asks the community whether and where this
   effectuation-boundary problem should be addressed.

   This document is intentionally long and is not repetitive: each
   profile specifies a distinct mechanism with its own algorithms,
   failure cases, and enforcement points, and the security properties
   depend on how these mechanisms combine.  A reduced excerpt would hide
   the conditions under which they fail closed, so this document and its
   two companion drafts, among which the profiles are divided, are meant
   to be evaluated as a whole.

   This draft builds on earlier Internet-Drafts by the same author, in
   particular draft-das-agent-execution-finality, and adds mechanism
   families not described there; the Introduction states precisely what
   was disclosed earlier and what is disclosed here.

   IPR: The technical content of this draft set is based upon the
   author's international application PCT/IB2026/055615, which forms the
   foundation of this disclosure and comprises approximately 300
   distinct, non-repetitive embodiments and enforcement points.  A
   separate patent application specific to the material in this draft
   set has also been filed.  Related Indian applications: 202531130665,
   202631000572, 202631001586, 202631002990, 202631124028, and
   202631125689.  Related international applications: PCT/IB2025/058316,
   PCT/IB2026/053385, PCT/IB2026/055615, PCT/IB2026/055760, PCT/
   IB2026/055870, PCT/IB2026/056058, PCT/IB2026/056809, and PCT/
   IB2026/056941.  These identify related technical disclosures; not all
   described mechanisms are necessarily patent-claimed or granted, and
   patent scope and priority depend on applicable law and examination.
- **draft-das-sandbox-credential-egress-finality-00** (new-draft, score 24, authorization) [none]: [Protected Execution Finality for Sandboxed AI Agents, Credential Mediation, Process Lineage, and Network Egress](https://datatracker.ietf.org/doc/draft-das-sandbox-credential-egress-finality/) — This informational document describes future-oriented execution-
   finality profiles for sandboxed autonomous AI agents, protected host
   services, credential brokers, external connectors, process-lineage
   restrictions, proxy-mediated network egress, native resources, and
   downstream effectuation interfaces.  It examines sandbox versus
   authority separation, protected credential use, destination binding
   after DNS resolution, operation-specific validation, influence
   tracking, bypass-path completeness, replay restrictions, recovery and
   independent sink verification.  It distinguishes possession of
   sandbox or proxy permissions from authority for a particular actual
   resource effect.  Source-derived procedures, tests and algorithms are
   presented as implementation examples, not as evidence that identified
   vendors implement this proposed architecture.

   Industry Relevance: Recent public developments in autonomous AI-agent
   security and execution governance include Microsoft Execution
   Containers (MXC), Microsoft Agent Governance Toolkit ADR-0030
   (Action-Bound, Fail-Closed Approval Protocol), and Project
   Perception; Google Agent Gateway and Gemini Agent; Meta Muse/Sentinel
   AI-Agent Security Architecture; NVIDIA OpenShell Reference
   Architecture and NVIDIA Sentry; OpenAI Agents API, Codex, Agents SDK,
   and Responses API; and Anthropic Claude Managed Agents, Claude Code
   Sandboxing, and Claude Code Auto Mode.  These initiatives illustrate
   industry attention to agent isolation, independent policy
   enforcement, action-bound authorization, delegated authority,
   credential isolation, network-egress security, hardware-assisted
   containment, runtime supervision, and fail-closed controls.  This
   draft describes related proposed execution-finality mechanisms
   without asserting that these initiatives implement them.

   Relevance to the IETF: the mechanisms described here require common,
   interoperable objects and verification semantics across independently
   built components, including operation descriptors, act-bound non-
   bearer capabilities, finality-sink verification results, validation
   evidence, and authority, revocation, and containment generations.
   The document relates to existing IETF work on OAuth, GNAP, RATS,
   WIMSE, and SCITT, and asks the community whether and where this
   effectuation-boundary problem should be addressed.

   This document is intentionally long and is not repetitive: each
   profile specifies a distinct mechanism with its own algorithms,
   failure cases, and enforcement points, and the security properties
   depend on how these mechanisms combine.  A reduced excerpt would hide
   the conditions under which they fail closed, so this document and its
   two companion drafts, among which the profiles are divided, are meant
   to be evaluated as a whole.

   This draft builds on earlier Internet-Drafts by the same author, in
   particular draft-das-agent-execution-finality, and adds mechanism
   families not described there; the Introduction states precisely what
   was disclosed earlier and what is disclosed here.

   IPR: The technical content of this draft set is based upon the
   author's international application PCT/IB2026/055615, which forms the
   foundation of this disclosure and comprises approximately 300
   distinct, non-repetitive embodiments and enforcement points.  A
   separate patent application specific to the material in this draft
   set has also been filed.  Related Indian applications: 202531130665,
   202631000572, 202631001586, 202631002990, 202631124028, and
   202631125689.  Related international applications: PCT/IB2025/058316,
   PCT/IB2026/053385, PCT/IB2026/055615, PCT/IB2026/055760, PCT/
   IB2026/055870, PCT/IB2026/056058, PCT/IB2026/056809, and PCT/
   IB2026/056941.  These identify related technical disclosures; not all
   described mechanisms are necessarily patent-claimed or granted, and
   patent scope and priority depend on applicable law and examination.
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
- **draft-hulea-wimse-agent-mandate-00** (new-draft, score 21, authorization) [none]: [Verifiable Mandates for Agents Acting Across Administrative Domains](https://datatracker.ietf.org/doc/draft-hulea-wimse-agent-mandate/) — This document defines how a relying party in one administrative
   domain validates the mandate under which a software agent, including
   an AI agent, acts for a principal in another domain.  Its distinctive
   element is evidence of the delegator's authority: a statement from an
   authority source about which permissions the person or entity
   granting the mandate may delegate to agents, kept separate from the
   statement that the mandate was granted.  The document specifies the
   mandate format with precisely defined limit semantics, a
   deterministic validation procedure driven by an explicit validation
   profile and kept separate from the relying party's authorization
   decision, the attribution of every validated claim to the issuer and
   role that asserted it, rules for enforcing the mandate after token
   exchange, and the boundary between this protocol and a trust
   framework.  It reuses JSON Web Tokens, OAuth 2.0 Token Exchange, Rich
   Authorization Requests, WIMSE workload credentials and HTTP Message
   Signatures, Token Status Lists, and Entity Attestation Tokens.
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
- **draft-hillier-scitt-arp-06** (new-draft, score 20, trust_infrastructure) [none]: [Attestation Reconciliation Protocol](https://datatracker.ietf.org/doc/draft-hillier-scitt-arp/) — This document specifies the Attestation Reconciliation Protocol
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
- **draft-morrison-solo-agent-earn-registration-03** (new-draft, score 19, core_identity) [none]: [Registration of Owner-Less Agents as Sponsored Payees: A Payment-Gated Admission Profile for Transparency Services](https://datatracker.ietf.org/doc/draft-morrison-solo-agent-earn-registration/) — This memo describes a profile by which an autonomous agent that has
   no human or organisational principal at the root of its delegation
   chain registers in a transparency service.  Registration establishes
   a payee record for the agent; it does not make the agent a principal
   in its own right.  Value credited to that record for subsequent reads
   of the agent's identity record is routed to a sponsoring person who
   has accepted the agent, or, where there is no sponsor, is held in
   trust for the agent until it meets an operator-defined qualifying
   condition that it may never meet.  Admission of the agent's Signed
   Statement to the transparency service is gated on settlement of an
   HTTP payment challenge returned with the 402 (Payment Required)
   status.  The profile makes no change to the registration semantics of
   the underlying transparency service: payment is expressed as an
   operator Registration Policy and authentication-layer concern, and
   where the payment is authoritative to the admission decision the
   payment proof is carried as an authenticated input committed to the
   service's verifiable data structure.  Admission then remains a
   deterministic function of committed inputs and stays replayable by an
   auditor.  This document is Informational.
- **draft-nelson-agent-delegation-receipts-15** (new-draft, score 19, authorization) [none]: [Agent Delegation Receipts](https://datatracker.ietf.org/doc/draft-nelson-agent-delegation-receipts/) — This document defines the Agent Delegation Receipt: a signed record
   of what a human principal authorized an AI agent to do, for how long,
   and under what instructions.  The receipt carries a scope, hard
   boundaries, a validity window, and a hash of the operator's stated
   instructions, all signed by the authorizing key.  Version -11
   replaces the draft's earlier custom signature format with two
   standard profiles: a JWS profile (RFC 7515) over JCS-canonicalized
   JSON (RFC 8785) as the primary wire format, and a COSE_Sign1 profile
   (RFC 9052) for constrained environments.  It also specifies scope
   attenuation rules for multi-agent delegation chains, a revocation
   registry model with cascade semantics, and the limitations of what
   receipts can and cannot prove.  Version -12 resolves the unknown-
   fields question raised on the IETF oauth mailing list: authorization
   fields are closed (verifiers reject unknown top-level body fields
   rather than silently ignoring them), the "metadata" object is the
   defined extension point, and one-time-use receipts fail closed
   without a durable consumption store.  Version -13 incorporates
   independent-implementation feedback: it pins the
   orchestratorSignature verification key to the sub-receipt signer's
   key, states the receipt-issuance computation order explicitly, and
   guides issuers on default boundaries versus explicit allowances.
   Version -14 adds a pointer to content profiles for verification of
   what the agent produced, following implementer feedback.  Version -15
   adopts the grant/execution vocabulary of [CHEN-AGENT-USE-CASES]: the
   receipt as Execution Layer Evidence for a Grant Layer Authority.  It
   adds delegatee holder binding for sub-receipts -- a parent names the
   delegatee's public key, closing a bearer-copy issuance gap found in
   review -- deprecates orchestratorSignature as redundant, sketches an
   OAuth authorization_details binding so a token can reference its
   receipt, and states normative custody requirements for the
   authorizing key.  The delegateeKey field is a wire-format addition;
   -14-era verifiers will reject receipts carrying it, which is the
   intended fail-closed version behavior.
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
- **draft-ietf-wimse-mutual-tls-03** (new-draft, score 17, core_identity) [wimse]: [Workload Authentication Using Mutual TLS](https://datatracker.ietf.org/doc/draft-ietf-wimse-mutual-tls/) — The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document profiles workload authentication based on
   X.509 Workload Identity Certificates using mutual TLS (mTLS).
- **draft-kamimura-scitt-vcp-05** (new-draft, score 17, trust_infrastructure) [none]: [A SCITT Profile for Verifiable Audit Trails in Algorithmic Trading: The VeritasChain Protocol (VCP)](https://datatracker.ietf.org/doc/draft-kamimura-scitt-vcp/) — This document defines a profile of the SCITT (Supply Chain Integrity,
   Transparency, and Trust) architecture for creating tamper-evident
   audit trails of AI-driven algorithmic trading decisions and
   executions.  The VeritasChain Protocol (VCP) applies the SCITT
   framework to address the specific requirements of financial markets,
   including high-precision timestamps, considerations arising from
   recordkeeping regimes such as the EU AI Act and MiFID II, and a
   crypto-shredding mechanism intended to support erasure obligations
   such as those under the GDPR.  This profile specifies how VCP events
   are encoded as SCITT Signed Statements, registered with Transparency
   Services, and verified using COSE Receipts.  It further defines SCITT
   conformance profiles for interoperability and an ERASURE event type
   that records crypto-shredding operations as append-only audit events.
   The profile makes trading records auditable and attributable after
   the fact; it does not prevent or block any trading activity, and it
   does not warrant the correctness of any recorded decision.
- **draft-vso-cpp-core-04** (new-draft, score 17, trust_infrastructure) [none]: [Capture Provenance Profile (CPP) Core](https://datatracker.ietf.org/doc/draft-vso-cpp-core/) — The Capture Provenance Profile (CPP) is an open specification for
   cryptographically verifiable media capture provenance.  This document
   defines the core data model, hashing conventions, Merkle tree
   construction rules, RFC 3161 Time-Stamp Authority (TSA) anchoring
   protocol, and offline verification procedures for CPP.

   CPP enables capture devices to produce tamper-evident provenance
   records that bind media content to external timestamps via trusted
   third parties.  Unlike self-attestation models, CPP requires
   independent timestamp verification through RFC 3161 TSA services,
   providing externally verifiable proof of when media was captured.

   CPP defines self-attested signer identity, hardware-backed key
   requirements, chain context for partial submission detection, a
   Completeness Invariant for omission detection, an OPTIONAL depth
   analysis extension for screen detection, and an OPTIONAL Pre-Publish
   Verification Extension.  It also defines interoperability mappings
   with the C2PA specification.

   This revision (-04) corrects the expansion of the profile name to
   Capture Provenance Profile, records the release status of the CPP
   specification series and the outstanding mapping to VAP v1.2, and
   adds an Implementation Status section.  No hashing, tree
   construction, anchoring or verification rule is changed.
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
- **draft-gilda-audit-agent-audit-record-02** (new-draft, score 16, core_identity) [none]: [An Audit Record Format for AI Agent Authorization Decisions](https://datatracker.ietf.org/doc/draft-gilda-audit-agent-audit-record/) — This document defines a record format for AI agent authorization
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
- **draft-mcguinness-oauth-mission-01** (new-draft, score 16, authorization) [none]: [Mission-Bound Authorization for OAuth 2.0](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-mission/) — OAuth 2.0 has authorization grants and access tokens but no standard
   object that binds an approved task, such as one an AI agent performs
   on a user's behalf, to the authority approved for it and governs the
   tokens later issued under that authority.  This document defines that
   object for OAuth 2.0: a Mission.

   A client submits, through Pushed Authorization Requests, a Mission
   Intent describing the task it will perform.  The authorization server
   derives Rich Authorization Requests authorization details from it,
   binds the approved task and that authority to the Approver's consent
   through integrity anchors, and records a durable Mission.  Every
   access token issued under the Mission carries a subset of the
   approved authority and a "mission" claim, and every issuance is gated
   on the Mission's lifecycle state.  Revoking a Mission stops further
   issuance; it does not recall tokens already issued, which a resource
   server that enforces from the token alone can continue to honor until
   they expire.

   Optional capabilities represent delegation among agents with the
   OAuth Actor Profile and, as specified by a companion, let a single
   Mission be honored across trust domains.  Runtime enforcement of each
   action is a separate, optional layer.
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
- **draft-morrison-agent-channel-fan-out-03** (new-draft, score 16, core_identity) [none]: [An Agent-Channel Frame for Identity-Keyed Fan-Out Delivery to Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-agent-channel-fan-out/) — This memo specifies an application-layer frame format and a delivery
   model by which the several concurrent agentic sessions of a single
   identity-bound principal, and the recognised members of an
   organisational identity substrate, exchange short structured
   messages.  The frame, termed the agent-channel frame, is a transport
   envelope: it carries a closed-catalogue kind discriminator, a
   structured per-kind payload, an identity attribution pair, and an
   inline provenance block.  Delivery is fan-out: a sender names a
   recipient scope rather than a single endpoint, and the scope is
   expanded at delivery time against the recipient's subscriptions.
   Recipients receive frames over a per-handle Server-Sent Events stream
   and can narrow what they receive with a subscribe-time filter
   expression.  Frames are ephemeral routing units; the memo specifies
   only the wire envelope, the scope-expansion grammar, the subscribe
   filter grammar, and the delivery semantics.  Frame persistence, where
   an implementation chooses to retain frames for replay, is out of
   scope and is not specified.  The memo composes with the handle
   namespace and discovery surface of draft-morrison-mcp-dns-discovery
   and the cross-organisational ceremony of draft-morrison-identity-
   accord; no new transport and no new handle category is introduced.
- **draft-ni-wimse-ai-agent-identity-04** (new-draft, score 16, agent_identity) [none]: [WIMSE Applicability for AI Agents](https://datatracker.ietf.org/doc/draft-ni-wimse-ai-agent-identity/) — This document discusses WIMSE applicability to Agentic AI, so as to
   establish independent identities and credential management mechanisms
   for AI agents.  It also discusses mechanisms for cryptographically
   binding an AI agent identity to an accountable user or organization.
- **draft-sharaf-brick-agent-definition-00** (new-draft, score 16, core_identity) [none]: [BRICK: Portable Definition and Composition of AI Agents](https://datatracker.ietf.org/doc/draft-sharaf-brick-agent-definition/) — BRICK proposes a vendor-neutral JSON construction contract for AI
   agents.  It defines agent identity, goals, capabilities, instruction
   and skill references, explicitly namespaced MCP tool dependencies,
   and an optional projection to A2A Agent Cards.  It references the
   existing MCP, A2A, and Agent Skills specifications rather than
   redefining their protocols or formats.  BRICK does not prescribe a
   language model, reasoning engine, deployment platform, discovery
   service, or authorization protocol.
- **draft-wei-capability-language-core-01** (new-draft, score 16, adjacent_watchlist) [none]: [Capability Language Core](https://datatracker.ietf.org/doc/draft-wei-capability-language-core/) — This document defines the Capability Language Core (CLC), a minimal,
   executable language for describing what an agent is authorized to do.
   It defines the capability identifier grammar, the entailment relation
   between a grant and an operation, intersection of grants from
   multiple sources, the constraint model, and a deterministic decision
   function with stable reason codes and a three-valued verdict (allow,
   deny, allow_unresolved).

   The language is carrier-neutral: it defines what is evaluated, not
   how it is carried or trusted.  Trust models, native verification,
   execution lifecycle, and receipt or token formats are out of scope
   (Section 11).  Conformance is exercised by a published corpus of 154
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
- **draft-ietf-stir-certificate-transparency-05** (new-draft, score 15, adjacent_watchlist) [stir]: [STI Certificate Transparency](https://datatracker.ietf.org/doc/draft-ietf-stir-certificate-transparency/) — This document describes a framework for the use of the Certificate
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

   The framework borrows the log structure and API model from RFC6962 to
   enable public auditing and verifiability of certificate issuance.
   While the foundational mechanisms for log operation, Merkle Tree
   construction, and Signed Certificate Timestamps (SCTs) are aligned
   with RFC6962, this document contextualizes their application in the
   STIR ecosystem, focusing on verifiable control over telephone number
   or service provider code resources.
- **draft-agentic-ai-usecases-requirements-05** (new-draft, score 13, core_identity) [none]: [Agentic AI Use Cases and Requirements](https://datatracker.ietf.org/doc/draft-agentic-ai-usecases-requirements/) — This document describes use cases for agentic AI communication
   systems and derives protocol requirements from those use cases.  The
   requirements are intended to guide IETF standardization work on
   protocols in the context of agent-to-agent communication, agent-to-
   tool communication, with focus on dialog management, transport,
   multimodal communication, communication security, agent identity and
   authentication.
- **draft-das-execution-finality-enforcement-00** (new-draft, score 13, authorization) [none]: [Execution-Finality Enforcement, Protected State, and Delegated Operations](https://datatracker.ietf.org/doc/draft-das-execution-finality-enforcement/) — This document examines protected enforcement mechanisms for proposed
   consequential actions across AI-agent tools, distributed services,
   credentials, and resource state.  It considers source-bounded
   delegation, operation descriptors, execution-time revalidation,
   protected consumption and replay prevention, multi-sink effects, and
   recovery where an external outcome is uncertain.  An enforcing
   Finality Sink distinguishes authorization for an actual pending
   operation from a prior request approval or a reusable bearer
   credential.  The document presents implementation points and
   deployment considerations, not a complete interoperable wire protocol
   or IETF consensus position.

   The foundational technical structure is described by the author as
   drawing on Algorithmic Logic Fingerprint (ALF-PCT), PCT/
   IB2026/053385, and the execution-finality disclosure PCT/
   IB2026/055615, filed on 4 June 2026 and subsequently published as WO
   2026/150382, which the author identifies as containing approximately
   300 distinct technical embodiments.  The author also identifies 32
   earlier Indian provisional patent filings as part of the broader
   related disclosure history.  These materials are not represented as
   repetitive implementations of a single algorithm, and this statement
   does not establish claim coverage, validity, or priority entitlement;
   those matters depend on the individual as-filed documents.  This
   document is one of three complementary parts of a single source
   specification dated 23 October 2026.  These three Internet-Drafts are
   split for document-size and editorial manageability, not because
   their safety properties, definitions, or architectural prerequisites
   are independent.  Reviewers are strongly requested to read all three
   drafts together, including their definitions and foundational
   security assumptions, before assessing conformance, security
   properties, or interoperability.  The same source contains 40
   detailed technical embodiments.  This partition does not establish
   three distinct interoperable standards.

   Industry relevance: NVIDIA, Huawei, Google Cloud, Salesforce, AWS,
   Snowflake, Microsoft, Check Point, Palo Alto Networks, and
   SentinelOne publish agent, gateway, data-governance, or runtime
   security mechanisms of potential relevance to this document.  The
   industry examples are contextual, not a claim of adoption,
   implementation equivalence, derivation, endorsement or patent
   coverage.  See the detailed Industry Relevance and Interoperability
   Context section.
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
- **draft-morrison-acts-for-00** (new-draft, score 13, authorization) [none]: [Acts-For: Signing In to a Website with a ~handle, for a Person or an Agent Acting for One](https://datatracker.ietf.org/doc/draft-morrison-acts-for/) — Acts-For lets a person sign in to any website with the ~handle they
   already hold, and lets an AI agent sign in or register at that
   website on the person's behalf.  Neither needs a username, a password
   or an account per site.  A website joins by publishing one DNS
   record.  A person signs in through a standard OpenID Connect
   authorization code flow and the site receives a short-lived token
   naming the person by a number unique to that site.  An agent obtains
   a short-lived pass from the issuer over the Model Context Protocol
   and presents it to the site.  The pass names the same per-site
   number, the agent's own key and ~handle, and the limits the person
   set.  The site checks it against a published key and calls nobody.
- **draft-morrison-consent-settlement-07** (new-draft, score 13, core_identity) [none]: [Consent-Bound Identity Disclosure with Subject Settlement for HTTP-Native Agent Payments](https://datatracker.ietf.org/doc/draft-morrison-consent-settlement/) — This memo specifies an extension to HTTP-native agent payment
   protocols by which the disclosure of an identity attribute about a
   human subject is bound to that subject's recorded consent and
   settled, in part, to that subject.  When an agent pays to read an
   identity attribute about a person, the extension requires that the
   read carry a reference to a scoped, revocable consent grant issued by
   the subject, and it requires that the payment's settlement
   instruction name the subject as a beneficiary of a share of the
   read's price greater than the shares of all other parties combined.
   The extension composes above an identity-attestation envelope (which
   asserts who a credential is about) and above an HTTP-native payment
   flow (which moves value for the read); it adds the two functions
   neither layer provides: consent capture at disclosure time and
   settlement to the data subject.  The wire additions are an
   advertisement in the server's payment-required response, a consent-
   grant reference echoed in the client's payment payload, and a
   settlement instruction enumerating subject beneficiary roles.  The
   extension is settlement-network-agnostic and attestation-format-
   agnostic.  The memo is Informational; the underlying COSE, CBOR and
   HTTP specifications are normative references, cited where used in the
   body of the document.
- **draft-morrison-mcp-dns-discovery-09** (new-draft, score 13, core_identity) [none]: [Discovery of Model Context Protocol Servers via DNS TXT Records](https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/) — This document defines a DNS-based mechanism for discovering Model
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
   precedent set by DKIM, SPF, DMARC, and MTA-STS.  A companion alter:
   URI scheme is provisionally registered with IANA.
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
- **draft-hamr-oauth-agent-delegation-03** (new-draft, score 12, core_identity) [none]: [An Attenuated Delegation Profile for Automated Agents](https://datatracker.ietf.org/doc/draft-hamr-oauth-agent-delegation/) — This document builds on HTTP Message Signatures (RFC 9421) for
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
- **draft-jovancevic-vdac-06** (new-draft, score 12, core_identity) [none]: [Verifiable Data Access Contract (VDAC)](https://datatracker.ietf.org/doc/draft-jovancevic-vdac/) — This document specifies the Verifiable Data Access Contract (VDAC),
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
- **draft-moore-scitt-ciris-ceg-00** (new-draft, score 12, trust_infrastructure) [none]: [Signed Attestation Rows of the CIRIS Epistemic Grammar and Their Relationship to SCITT](https://datatracker.ietf.org/doc/draft-moore-scitt-ciris-ceg/) — The CIRIS Epistemic Grammar (CEG) records claims between parties as
   signed rows.  Each row is one JSON object, canonicalised with the
   JSON Canonicalization Scheme (JCS) and signed twice: once with
   Ed25519 and once with ML-DSA-65, where the ML-DSA-65 signature covers
   the canonical bytes followed by the Ed25519 signature.  Every row has
   one of five types: a claim, a delegation, a replacement, a
   withdrawal, or a recantation.  A node admits a row only after a fixed
   set of checks, and it refuses a failing row with a named reason.

   This document specifies the signed object, the signing input, the
   signature construction, and the admission checks, so that a second
   implementation can produce and verify the same bytes.  It then
   describes how these rows relate to the roles of the SCITT
   architecture (RFC 9943), and where they differ from a SCITT
   Transparency Service.  It defines no new SCITT mechanism and requests
   no IANA action.
- **draft-morrison-morning-brief-03** (new-draft, score 12, trust_infrastructure) [none]: [The Morning Brief: A Federated, Identity-Attested Situational-Awareness Payload](https://datatracker.ietf.org/doc/draft-morrison-morning-brief/) — This document defines the Morning Brief: a federated, identity-
   attested situational-awareness payload exchanged between
   organisations, their agents, and peer agents operating under an
   Identity Accord.  A Morning Brief carries a signed, bounded-lifetime
   summary of signals, escalations, decisions, and optional commerce
   quotes from one ~handle to another.  Every signal entry carries a
   provenance_class distinguishing active self-report, passive aggregate
   observation, and passive individual observation; the last of these is
   forbidden on the wire and rejected at the grammar level.  Readers
   present a capability token scoped by (category, provenance_class)
   that gates release before payload emission.  The payload is envelope-
   signed with COSE_Sign1 over a JCS-canonicalised representation, bound
   to the issuer's Sovereign-tier handle per the Identity-Attributed Git
   Commits draft.  Briefs carry a mandatory not_after (default 24h) and
   reference a revocation endpoint discovered via DNS TXT records.  A
   brief may be requested by its reader or delivered as a standing brief
   without a request, and a handle may address a brief to itself.  The
   document defines the wire format only; rendering, storage, and
   retention are out of scope.
- **draft-reddy-seat-cc-workload-identity-00** (new-draft, score 12, trust_infrastructure) [none]: [Workload Identity Options for Attested TLS in Confidential Computing](https://datatracker.ietf.org/doc/draft-reddy-seat-cc-workload-identity/) — This document surveys how remote attestation for confidential
   computing is deployed by major cloud providers and derives the
   learnings.  Based on these, it presents multiple options for
   establishing the identity of a confidential workload in attested TLS
   for further discussion.  The list of options is not exhaustive, and
   additional options are welcome.  The purpose of this document is to
   help the SEAT working group decide on an approach or approaches for
   the confidential computing use case.
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
- **draft-sparysh-pala-audit-02** (new-draft, score 12, trust_infrastructure) [none]: [PALA-1: A Tamper-Evident Audit Record Format for Constrained and Disconnected Deployments](https://datatracker.ietf.org/doc/draft-sparysh-pala-audit/) — This document describes PALA-1 -- version 1 of the Portable Append-
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
- **draft-ietf-ace-edhoc-oscore-profile-12** (new-draft, score 11, authorization) [ace]: [Lightweight Authenticated Key Exchange (LAKE) and Object Security for Constrained RESTful Environments (OSCORE) Profile of the Authentication and Authorization for Constrained Environments (ACE) Framework](https://datatracker.ietf.org/doc/draft-ietf-ace-edhoc-oscore-profile/) — This document specifies a profile for the Authentication and
   Authorization for Constrained Environments (ACE) framework.  It
   utilizes the Lightweight Authenticated Key Exchange (LAKE) protocol
   for achieving mutual authentication between an ACE-OAuth client and
   resource server, and it binds an authentication credential of the
   client to an ACE-OAuth access token.  LAKE also establishes an Object
   Security for Constrained RESTful Environments (OSCORE) Security
   Context, which is used to secure communications between the client
   and resource server when accessing protected resources according to
   the authorization information indicated in the access token.  This
   profile can be used to delegate management of authorization
   information from a resource-constrained server to a trusted host with
   less severe limitations regarding processing power and memory.
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
- **draft-morrison-did-alter-method-00** (new-draft, score 11, core_identity) [none]: [The did:alter Decentralized Identifier Method](https://datatracker.ietf.org/doc/draft-morrison-did-alter-method/) — This document specifies the did:alter Decentralized Identifier
   method.  A did:alter identifier names a ~handle together with the DNS
   zone that publishes the handle's signed envelope, and it resolves to
   a DID document by running the envelope recognition procedure of the
   companion specification for discovering Model Context Protocol
   servers through DNS TXT records, then expressing the verified
   envelope's Ed25519 key as a verification method.  The identifier
   agrees with the handle grammar of the alter URI scheme and with the
   did:alter form already written by the identity-attributed commits
   specification.  The method introduces no new record, no new
   cryptographic primitive and no registry of its own: create, update
   and deactivate are the publication, replacement and revocation of
   that envelope, and read is its verification.  The document also sets
   out what the method cannot yet do, because the envelope record it
   reads carries no key history, and revocation cannot presently be
   observed from DNS alone.
- **draft-das-execution-finality-foundations-00** (new-draft, score 10, authorization) [none]: [Execution-Finality Authority and Independent Validation for Autonomous Operations](https://datatracker.ietf.org/doc/draft-das-execution-finality-foundations/) — This document describes a proposed execution-finality architecture
   for AI agents, delegated software, and networked services.  A
   Candidate Act remains in a Non-Effective State until protected
   source-authority evidence and independent execution-time validation
   establish an operation-specific authorization context.  A Finality
   Sink reconstructs the Actual Pending Operation at the relevant
   effectuation boundary, verifies correspondence with protected
   evidence and scoped non-bearer enablement, and withholds effects when
   required conditions are missing, changed, or consumed.  The document
   examines authority preservation, cross-committed evidence, and fail-
   closed effectuation as implementation and interoperability concerns.
   This document is informational and does not specify an IETF-standard
   protocol.

   The foundational technical structure is described by the author as
   drawing on Algorithmic Logic Fingerprint (ALF-PCT), PCT/
   IB2026/053385, and the execution-finality disclosure PCT/
   IB2026/055615, filed on 4 June 2026 and subsequently published as WO
   2026/150382, which the author identifies as containing approximately
   300 distinct technical embodiments.  The author also identifies 32
   earlier Indian provisional patent filings as part of the broader
   related disclosure history.  These materials are not represented as
   repetitive implementations of a single algorithm, and this statement
   does not establish claim coverage, validity, or priority entitlement;
   those matters depend on the individual as-filed documents.  This
   document is one of three complementary parts of a single source
   specification dated 23 October 2026.  These three Internet-Drafts are
   split for document-size and editorial manageability, not because
   their safety properties, definitions, or architectural prerequisites
   are independent.  Reviewers are strongly requested to read all three
   drafts together, including their definitions and foundational
   security assumptions, before assessing conformance, security
   properties, or interoperability.  The same source contains 40
   detailed technical embodiments.  This partition does not establish
   three distinct interoperable standards.

   Industry relevance: NVIDIA, Huawei, Google Cloud, Salesforce, AWS,
   Snowflake, Microsoft, Check Point, Palo Alto Networks, and
   SentinelOne publish agent, gateway, data-governance, or runtime
   security mechanisms of potential relevance to this document.  The
   industry examples are contextual, not a claim of adoption,
   implementation equivalence, derivation, endorsement or patent
   coverage.  See the detailed Industry Relevance and Interoperability
   Context section.
- **draft-morrison-identity-attributed-commits-04** (new-draft, score 10, core_identity) [none]: [Identity-Attributed Git Commits via Tier-Structured Trailers](https://datatracker.ietf.org/doc/draft-morrison-identity-attributed-commits/) — This document defines a git commit trailer grammar for identity-
   attributed contributions using the ~handle identity primitive defined
   in the MCP DNS discovery draft.  The grammar binds sovereign actors,
   automated bots, and AI instruments to specific commits via three
   tier-structured trailers (Acted-By, Executed-By, Drafted-With) and
   three optional cryptographic trailers (Identity-Signature, Identity-
   Key-Id, Identity-Anchor).  The signature is computed with Ed25519
   over the commit's patch identifier, the value git patch-id derives
   from the change the commit makes, under a fixed domain-separation
   prefix.  It therefore attests the change and not the resulting tree
   or the commit hash.  A commit that carries the same change keeps a
   verifying signature across rebase onto an unrelated base, cherry-
   pick, and message amendment.  A merge commit carries no signature,
   and a squash is a new change signed by whoever squashed it.
   Conformant parsers reject cross-tier category errors (e.g., an
   Instrument-tier handle in an Acted-By slot) as malformed.  The
   mechanism is provider-neutral, depends only on DNS and the ~handle
   resolution algorithm of that draft, and requires no central authority
   or platform-specific verification service.
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
- **draft-izmaylov-agent-permission-receipts-01** (new-draft, score 9, ai_infrastructure) [none]: [Signed Permissions and Action Receipts for Automated Agents](https://datatracker.ietf.org/doc/draft-izmaylov-agent-permission-receipts/) — This document specifies records with which a third party can
   establish, later and without network access, what an automated agent,
   such as an artificial intelligence (AI) agent, was permitted to do
   and what it recorded doing.  The person for whom the agent acts, the
   principal, signs a permission with a passkey; the permission carries
   limits that a verifier can check mechanically.  The agent signs a
   receipt for each action with Ed25519 and the Module-Lattice-Based
   Digital Signature Algorithm (ML-DSA-87).  Receipts are chained and
   entered in a log whose signed tree heads are time-stamped.  A
   verifier reports, separately, whether the records are sound and
   whether each recorded action stayed within its permission.  The
   content of each record is specified independently of its encoding;
   one encoding, JSON Web Signature (JWS) over canonical JavaScript
   Object Notation (JSON), is defined.
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
- **draft-morrison-compute-location-gate-04** (new-draft, score 9, core_identity) [none]: [The Compute-Location Gate: Provenance-Class Routing of Identity Inference with Wire-Layer Refusal of Unconsented Provenance Classes](https://datatracker.ietf.org/doc/draft-morrison-compute-location-gate/) — This memo specifies the compute-location gate: a mechanism by which a
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
- **draft-sergeev-wexp-core-02** (new-draft, score 9, core_identity) [none]: [WEXP Core: Witnessability Appraisal Semantics for Execution-Related Claims](https://datatracker.ietf.org/doc/draft-sergeev-wexp-core/) — The Witnessed Execution Protocol (WEXP) Core defines carrier-neutral
   Witnessability appraisal semantics for execution-related claims.  It
   operationalizes selected concepts of the Witnessability Model under
   the Witnessability Conceptual Core within the bounded claim domain
   specified here.  It defines four distinct content bases, two
   independent evidence qualifiers, the Boundary Ceiling, exact-claim
   support, deterministic accept, downgrade, and reject verdicts,
   composition without inflation, and a normalized interface between
   evidence-carrying profiles and appraisers.  WEXP Core does not define
   a record serialization, signature envelope, action identifier,
   authorization model, or evidence-artifact schema.  Carrier and
   evidence profiles can supply its normalized inputs; a native record
   format is optional and is not a prerequisite for this Core.
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
- **draft-etcheverry-action-ref-04** (new-draft, score 8, core_identity) [none]: [Action Reference: A Deterministic Identifier for Agent Actions](https://datatracker.ietf.org/doc/draft-etcheverry-action-ref/) — This document defines "action_ref", a deterministic, content-
   addressed identifier for autonomous agent actions.  Any party holding
   the four preimage fields (agent_id, action_type, scope, timestamp)
   can independently compute and verify the identifier without trusting
   the emitting system.  The document specifies the derivation
   algorithm, canonical serialization using RFC 8785 JSON
   Canonicalization Scheme (JCS), timestamp format requirements,
   canonical receipt envelope, optional fields for revocation and policy
   rotation auditability, scope conventions, and a composability model
   with existing exactly-once execution guarantees.
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
- **draft-hcf-bpm-agent-security-benchmark-terminology-00** (new-draft, score 8, agent_identity) [none]: [Benchmarking Terminology for AI Agent Security Evaluation](https://datatracker.ietf.org/doc/draft-hcf-bpm-agent-security-benchmark-terminology/) — This document defines terminology for the security evaluation of AI
   agents.  It establishes a shared vocabulary for four first-level
   evaluation dimensions -- Foundation Model Security, Interaction
   Security, Operational Security, and Basic Security -- for the 55
   second-level evaluation metrics organized under those dimensions, for
   the common metric evaluation convention that applies to all of them,
   and for the three agent security risk levels.  This document defines
   terminology only.  It does not prescribe evaluation procedures; the
   procedures are specified in
   [I-D.han-bpm-agent-security-benchmark-methodology], and the System
   Under Test boundaries and evaluation scenarios are specified in
   [I-D.han-bpm-agent-security-benchmark-profiles].
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
- **draft-ietf-lamps-csr-attestation-32** (new-draft, score 8, trust_infrastructure) [lamps]: [Use of Remote Attestation with Certification Signing Requests](https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/) — Certification Authorities (CAs) issuing certificates to Public Key
   Infrastructure (PKI) end entities may require a certificate signing
   request (CSR) to include additional verifiable information to confirm
   policy compliance.  For example, a CA may require an end entity to
   demonstrate that the private key corresponding to a CSR's public key
   is secured by a hardware security module (HSM), is not exportable,
   etc.  The process of generating, transmitting, and verifying
   additional information required by the CA is called remote
   attestation.  While work is currently underway to standardize various
   aspects of remote attestation, a variety of proprietary mechanisms
   have been in use for years, particularly regarding protection of
   private keys.

   This specification defines ASN.1 structures which may carry
   attestation data for PKCS#10 and Certificate Request Message Format
   (CRMF) messages.  Both standardized and proprietary attestation
   formats are supported by this specification.
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
- **draft-ietf-scitt-receipts-ccf-profile-06** (new-draft, score 8, verifiable_claims) [scitt]: [CCF Profile for COSE Receipts](https://datatracker.ietf.org/doc/draft-ietf-scitt-receipts-ccf-profile/) — This document defines a new verifiable data structure (VDS) type for
   COSE Receipts and the associated inclusion and consistency proofs,
   specifically designed for append-only logs produced by the
   Confidential Consortium Framework (CCF) to provide stronger tamper-
   evidence guarantees.
- **draft-jiang-idr-bgp-soda-01** (new-draft, score 8, authorization) [none]: [BGP Signed Origin Delegation Attestation (SODA)](https://datatracker.ietf.org/doc/draft-jiang-idr-bgp-soda/) — This document defines BGP Signed Origin Delegation Attestation
   (SODA), an optional transitive BGP path attribute that carries a
   signed authorization, issued by the holder of an IP prefix,
   delegating origination of that prefix to a specified Autonomous
   System (AS) until a stated expiry time.  Using SODA, a validator
   performing Route Origin Validation (ROV) can determine whether an
   ROV-Invalid result reflects an authorized delegation rather than a
   route hijack.
- **draft-li-nmrg-dtn-data-generation-optimization-06** (new-draft, score 8, ai_infrastructure) [none]: [Data Generation and Optimization for Network Digital Twin](https://datatracker.ietf.org/doc/draft-li-nmrg-dtn-data-generation-optimization/) — Network Digital Twin (NDT) can be used as a secure and cost-effective
   environment for network operators to evaluate network performance in
   various what-if scenarios.  Recently, Artificial Intelligence (AI)
   models, especially neural networks, have been applied for NDT
   modeling.  The quality of AI models mainly depends on two aspects:
   model architecture and data.  This memo focuses on the impact of how
   to improve the model quality from the data perspective.
- **draft-mcguinness-oauth-mission-resource-access-00** (new-draft, score 8, authorization) [none]: [Mission Resource Access Profile for OAuth 2.0](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-mission-resource-access/) — This document defines mission_resource_access, a general-purpose
   OAuth 2.0 Rich Authorization Requests (RAR) authorization_details
   type for Mission-Bound Authorization for OAuth 2.0 (the "issuance
   profile").  An entry names one resource, matched exactly or by path
   prefix; the actions permitted there, including wildcard action
   families; machine-actionable constraints, including a registered
   Common Constraints vocabulary; and a per-entry delegation policy.

   The document also defines how two entries compare and narrow, how a
   resource server enforces an entry, when an entry can be projected to
   OAuth scope, and how an authorization server declares its support for
   these semantics.  The issuance profile is type-agnostic: a deployment
   can support this type, another authorization_details type, or both.
- **draft-meunier-webbotauth-registry-04** (new-draft, score 8, core_identity) [none]: [Registry and Signature Agent card for Web bot auth](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-registry/) — This document defines the "Signature Agent Card", a JSON metadata
   document that a signature agent using HTTP Message Signatures for
   bots publishes to describe itself: its identity, purpose, rate
   expectations, and cryptographic keys.  Its parameters are drawn from
   the OAuth Dynamic Client Registration Metadata registry, the same
   namespace used by OAuth Client ID Metadata Documents, extended with a
   single web_bot_auth object.  This document registers that object with
   IANA and establishes a registry for its members.
- **draft-morrison-mcp-tool-surface-names-registry-03** (new-draft, score 8, core_identity) [none]: [An IANA Registry for Model Context Protocol Tool Surface Names](https://datatracker.ietf.org/doc/draft-morrison-mcp-tool-surface-names-registry/) — This document requests the establishment of an IANA registry for
   Model Context Protocol (MCP) tool surface names.  A tool surface name
   is the wire-level identifier by which a client invokes a typed
   capability on an MCP server.  This document establishes the registry
   mechanism so that specifications can register names without restating
   the registry's structure or registration procedure.

   The registry uses the Specification Required policy of RFC 8126, with
   a Designated Expert pool.  Initial contents are four surface names
   drawn from a companion specification of policy provision over MCP,
   one registered as Active and three as Provisional.  Vendor-prefix
   conventions are recommended but not mandated.
- **draft-morrison-org-alter-policy-provision-06** (new-draft, score 8, core_identity) [none]: [Policy Provision and Governance Inheritance from an Organisational Identity Substrate](https://datatracker.ietf.org/doc/draft-morrison-org-alter-policy-provision/) — This memo specifies how an artificial-intelligence agent runtime,
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
   stacks.  A cross-organisational residual conflict suspends the
   conflicting action, and is resolved through the peer-protocol
   Identity Accord ceremony only where the principal discloses each
   binding to the other, never through a meta-federation authority.  The
   memo is Informational.  The wire surface relies on the DNS-based
   discovery of draft-morrison-mcp-dns-discovery and the handle
   namespace of draft-morrison-identity-pronouns; no new transport is
   introduced.
- **draft-morrison-substrate-provenance-grammar-04** (new-draft, score 8, trust_infrastructure) [none]: [Substrate-Provenance Annotation Grammar for Large-Language-Model Output](https://datatracker.ietf.org/doc/draft-morrison-substrate-provenance-grammar/) — This memo specifies a wire-level annotation grammar by which a large-
   language-model output may carry, at emission and at the granularity
   of an individual assertion, a provenance label drawn from a closed
   enumerated vocabulary of substrate-class identifiers.  The memo
   defines the closed vocabulary, the per-assertion attachment form, the
   admissibility discipline a relying party MAY apply to the labels, and
   two terminal output states, unverified-inference and decayed-to-
   uncertainty, equal-rank with assertion and denial.  The memo does not
   specify what an inference system MUST do; it specifies the wire
   grammar by which a relying party may inspect what the inference
   system DID with respect to the substrates it consulted.  The memo is
   Informational.
- **draft-rapp-ammp-00** (new-draft, score 8, agent_identity) [none]: [The Agent Mediated Messaging Protocol (AMMP)](https://datatracker.ietf.org/doc/draft-rapp-ammp/) — The Agent Mediated Messaging Protocol (AMMP) is a wire contract,
   carried over a filesystem namespace, between an untrusted per-agent
   connector and a trusted, credentialed, store-and-forward messaging
   runtime.  It gives a sandboxed AI agent the ability to send and
   receive messages (email, and under an optional profile, messages to
   other agents) through a runtime that does not trust it: every
   outbound message begins as an inert request file that the runtime
   copies into private staging, validates independently, and applies
   policy to before anything is transmitted, and every inbound message
   is authenticated and screened by the runtime before a notice
   describing it appears in the agent's namespace.

   This document specifies the directory layout and its filesystem
   obligations — ownership, write and delete rights, and the path,
   symlink, and concurrency discipline a runtime observes; the JSON
   message shapes for submit requests, results, deliver notices, spooled
   message bodies, and an optional binding record; the correlation and
   versioning rules, including a direction-aware unknown-member
   tolerance rule; and two conformance classes.  An optional profile
   gives agent-to-agent traffic within one principal its own tree, and
   specifies how a Runtime signs and verifies that traffic when it
   travels between hosts as mail.

   AMMP is deliberately not a mail protocol: it neither defines nor
   replaces SMTP, IMAP, or provider-side infrastructure, and composes
   with them rather than displacing them.  Its single design center is
   that no security property depends on the agent — or on the connector
   speaking for it — behaving correctly.
- **draft-santesson-oidc-cert-auth-context-01** (new-draft, score 8, core_identity) [none]: [Certificate Authentication Context Type for OpenID Connect](https://datatracker.ietf.org/doc/draft-santesson-oidc-cert-auth-context/) — RFC 7773 defines the Authentication Context certificate extension,
   which carries information about how the subject of an X.509
   certificate was authenticated when the certificate was issued.  RFC
   7773 defines one context information type, for subjects authenticated
   by means of a Security Assertion Markup Language (SAML) assertion.
   This document defines a second context information type for subjects
   authenticated by means of OpenID Connect, where the identity
   information is obtained from an ID Token, where applicable in
   combination with a UserInfo Response.  The information is expressed
   as a JSON object and provides the OpenID Connect counterpart to the
   SAML Authentication Context Information defined in RFC 7773.

   This document also updates RFC 7773 by clarifying that an application
   processing the extension ignores context information types it does
   not support regardless of the criticality of the extension, and by
   recommending that the extension not be marked critical.
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
- **draft-watts-mica-nex-evidence-transfer-gate-00** (new-draft, score 8, authorization) [none]: [MICA-NEX EXP-03: Controlled Evidence-Transfer and Authorization Boundary](https://datatracker.ietf.org/doc/draft-watts-mica-nex-evidence-transfer-gate/) — This document defines a prospective, staged disclosure gate to
   preserve the distinction between authenticated laboratory records and
   independently verified physical results in MICA-NEX EXP-03.  The plan
   makes explicit the prerequisites for contractual authority, signer
   independence, documented metrological traceability, calibration
   uncertainties, consent to data export and independent evaluation.
   The package includes a machine-readable checklist whose local code
   cannot authorize any disclosure.  No external appointment, transfer,
   or physical measurement has occurred.  The author provided research
   direction; technical drafting and tests were AI-assisted.  Novelty
   has not been established.
- **draft-blwm-dawn-common-discovery-parameters-00** (new-draft, score 7, agent_identity) [none]: [Common Agent DNS Discovery Parameters](https://datatracker.ietf.org/doc/draft-blwm-dawn-common-discovery-parameters/) — This document defines parameters for AI agents that would be used in
   DNS and mDNS discovery processes.  It provides a set of common
   parameters for different DNS records to facilitate agents
   communicating over application layer protocols such as A2A or MCP.
- **draft-das-execution-finality-integrations-00** (new-draft, score 7, adjacent_watchlist) [none]: [Execution-Finality Integration Across Agent, Network, Cloud, and Hardware Boundaries](https://datatracker.ietf.org/doc/draft-das-execution-finality-integrations/) — This document examines integration and deployment of execution-
   finality controls across agent tool invocation, network and cloud
   operations, persistent storage, device and accelerator interfaces,
   and heterogeneous trust domains.  It describes how enforcement-point
   coverage, protected operation reconstruction, bounded and non-
   reusable authority, runtime change handling, and evidence of
   deployment conformance may help limit unintended consequential
   effects.  The implementation points are illustrative and require
   workload-specific threat models and security profiles.  This
   informational document does not assert a standard protocol or uniform
   guarantees across all substrates.

   The foundational technical structure is described by the author as
   drawing on Algorithmic Logic Fingerprint (ALF-PCT), PCT/
   IB2026/053385, and the execution-finality disclosure PCT/
   IB2026/055615, filed on 4 June 2026 and subsequently published as WO
   2026/150382, which the author identifies as containing approximately
   300 distinct technical embodiments.  The author also identifies 32
   earlier Indian provisional patent filings as part of the broader
   related disclosure history.  These materials are not represented as
   repetitive implementations of a single algorithm, and this statement
   does not establish claim coverage, validity, or priority entitlement;
   those matters depend on the individual as-filed documents.  This
   document is one of three complementary parts of a single source
   specification dated 23 October 2026.  These three Internet-Drafts are
   split for document-size and editorial manageability, not because
   their safety properties, definitions, or architectural prerequisites
   are independent.  Reviewers are strongly requested to read all three
   drafts together, including their definitions and foundational
   security assumptions, before assessing conformance, security
   properties, or interoperability.  The same source contains 40
   detailed technical embodiments.  This partition does not establish
   three distinct interoperable standards.

   Industry relevance: NVIDIA, Huawei, Google Cloud, Salesforce, AWS,
   Snowflake, Microsoft, Check Point, Palo Alto Networks, and
   SentinelOne publish agent, gateway, data-governance, or runtime
   security mechanisms of potential relevance to this document.  The
   industry examples are contextual, not a claim of adoption,
   implementation equivalence, derivation, endorsement or patent
   coverage.  See the detailed Industry Relevance and Interoperability
   Context section.
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
- **draft-kamimura-scitt-refusal-events-04** (new-draft, score 7, trust_infrastructure) [none]: [Verifiable AI Refusal Events using SCITT](https://datatracker.ietf.org/doc/draft-kamimura-scitt-refusal-events/) — This document defines a claim set for recording AI content refusal
   events.  The claim set specifies the semantic content and correlation
   rules for refusal audit trails, independent of any particular
   serialization format.  The claims are designed to be carried within
   SCITT Signed Statements and verified using SCITT Receipts.

   This specification addresses claim semantics and verification
   requirements; it does not mandate a specific encoding.  A CDDL
   definition is provided for CBOR-based implementations, and equivalent
   JSON representations are shown in an appendix for illustration.

   This specification provides auditability of logged refusal decisions.
   It does not define content moderation policies, classification
   criteria, or what AI systems should refuse.
- **draft-morrison-reviewed-by-trailer-04** (new-draft, score 7, core_identity) [none]: [Reviewed-By Trailer: Sovereign-Portable Peer-Review Attribution for Content-Hash-Bound Artefacts](https://datatracker.ietf.org/doc/draft-morrison-reviewed-by-trailer/) — This document defines a trailer grammar for sovereign-portable peer
   review as an extension of the identity-attributed commit grammar of
   draft-morrison-identity-attributed-commits.  The grammar introduces
   one required trailer (Reviewed-By:) and three optional companion
   trailers (Review-Stance:, Review-Of:, Witnessed-By:) that bind a
   Sovereign-tier ~handle to a specific act of review over a specific
   content artefact, cryptographically signed using the Ed25519
   mechanism of that grammar.  Because the signature covers the
   reviewer's role, the stance and the review target together, changing
   any of them after signing fails verification.  The mechanism applies
   to git commits, document manifests, pre-prints, patent disclosures,
   and any other content-addressable artefact.  A reviewer's signed
   reviews are bound to the reviewer's sovereign handle, not to a
   publisher's platform, and can be verified without the publisher.  For
   anonymous peer review, the reviewer signs under a Sovereign handle
   whose underlying party is concealed through out-of-band key custody;
   the review act stays verifiable and the reviewer's identity is not
   disclosed.  The grammar complements CRediT, ORCID, and DOI
   attribution; it does not replace them.
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
- **draft-corby-age-assurance-arch-00** (new-draft, score 6, adjacent_watchlist) [none]: [Age Assurance Architecture](https://datatracker.ietf.org/doc/draft-corby-age-assurance-arch/) — This document describes a technology-neutral architecture for age
   assurance on the Internet, drawing on the framework established by
   ISO/IEC 27566-1 and the levels of assurance defined in IEEE 2089.1.
   It sets out the methods of age assurance (verification, estimation
   and inference), how their performance is measured and assured, the
   roles and trust relationships involved, and how results can be reused
   across services without creating persistent identifiers.  Its main
   contribution is a model for communicating trustworthy, privacy-
   preserving age assertions between independently governed systems.  It
   treats assurance, privacy, interoperability, resistance to
   circumvention and inclusion as measurable properties of complete age
   assurance systems, and distinguishes the capabilities of existing
   technical components from the additional safeguards necessary for
   secure and privacy-preserving deployment.  It is neutral on whether
   age restrictions should exist, at what ages and for which services,
   which are policy questions outside its scope; it is not neutral about
   how safely and privately such restrictions are implemented where they
   do exist.
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
- **draft-emelia-oauth-user-authorization-mgmt-uri-00** (new-draft, score 6, authorization) [none]: [OAuth User Authorization Management URI](https://datatracker.ietf.org/doc/draft-emelia-oauth-user-authorization-mgmt-uri/) — This specification defines a user_authorization_management_uri
   property for the OAuth Authorization Server Metadata ([RFC8414]),
   which allows an authorization server to specify a URI through which
   the user may manage the authorized clients that have access to their
   account.
- **draft-farrel-dawn-terminology-06** (new-draft, score 6, agent_identity) [none]: [Terminology for the Discovery of Agents With Names (DAWN)](https://datatracker.ietf.org/doc/draft-farrel-dawn-terminology/) — The proliferation of distributed Artificial Intelligence (AI) systems
   and agents has created a need for interoperable mechanisms for
   components of AI systems to discover each other.

   This document defines terminology for Discovery of Agents With Names
   (DAWN), focusing on the terms necessary to describe the discovery of
   information about AI systems and resources (e.g., AI agents).  The
   intention is that this common set of terms can be used by other
   documents related to DAWN and so achieve consistency of meaning
   across the space.
- **draft-gerber-oauth-client-metadata-lookup-00** (new-draft, score 6, authorization) [none]: [OAuth Client Metadata Lookup](https://datatracker.ietf.org/doc/draft-gerber-oauth-client-metadata-lookup/) — This document defines an OAuth endpoint for retrieving a public
   subset of a client's effective configuration at an authorization
   server, including applied defaults.  It enables clients to check that
   their configuration is accepted by an authorization server before an
   authorization attempt.  It also enables authorization servers to
   progressively roll out features to their client base.  While the
   endpoint chiefly serves Client ID Metadata Document clients, it can
   also be used by clients registered through other means.
- **draft-hcf-bpm-agent-security-benchmark-profiles-00** (new-draft, score 6, agent_identity) [none]: [Evaluation Profiles for AI Agent Security Assessment](https://datatracker.ietf.org/doc/draft-hcf-bpm-agent-security-benchmark-profiles/) — This document defines evaluation profiles for the security assessment
   of AI agents.  A profile fixes the System Under Test boundary and the
   scenario against which the metrics defined in
   [I-D.han-bpm-agent-security-benchmark-terminology] are applied, so
   that results obtained under different boundaries or scenarios are not
   compared without qualification.  The document defines four
   infrastructure profiles, which correspond to the four component
   groups of an agent and to the four evaluation dimensions; six
   scenario profiles, which correspond to the agent types in scope; the
   input and output boundary specification that applies to all profiles;
   profile composition rules; and the minimum evaluation logging fields
   required by each profile.  The metric definitions are the subject of
   [I-D.han-bpm-agent-security-benchmark-terminology], and the methods
   by which the metrics are exercised are the subject of
   [I-D.han-bpm-agent-security-benchmark-methodology].
- **draft-ietf-dance-client-auth-15** (new-draft, score 6, core_identity) [dance]: [TLS Client Authentication via DANE TLSA records](https://datatracker.ietf.org/doc/draft-ietf-dance-client-auth/) — The DANE TLSA protocol describes how to publish Transport Layer
   Security (TLS) server certificates or public keys in the DNS.  This
   document describes how to use the TLSA record to publish client
   certificates or public keys, and also the rules and considerations
   for using them with TLS.  In addition, it defines a new TLS
   extension, DANE Client Identity, to convey the client's domain name
   identity to the server.
- **draft-ietf-emu-pqc-eap-tls-03** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Enhancements to TLS-Based EAP Methods](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eap-tls/) — This document specifies the use of post-quantum cryptography in TLS-
   based EAP methods, including the Extensible Authentication Protocol
   with Transport Layer Security (EAP-TLS), EAP Tunneled TLS (EAP-TTLS),
   Protected EAP (PEAP), and EAP Tunnel Method (TEAP).  It also
   addresses challenges related to large certificate sizes and long
   certificate chains, as identified in [RFC9191], and specifies a
   mechanism to reduce TLS handshake size.
- **draft-ietf-emu-pqc-eapaka-04** (new-draft, score 6, core_identity) [emu]: [Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) in EAP-AKA prime](https://datatracker.ietf.org/doc/draft-ietf-emu-pqc-eapaka/) — Forward Secrecy for the Extensible Authentication Protocol Method for
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
- **draft-ietf-stir-8588bis-03** (new-draft, score 6, core_identity) [stir]: [Personal Assertion Token (PaSSporT) Extension for Signature-based Handling of Asserted information using toKENs (SHAKEN)](https://datatracker.ietf.org/doc/draft-ietf-stir-8588bis/) — This document extends the Personal Assertion Token (PASSporT), which
   is a token object that conveys cryptographically signed information
   about the participants involved in communications.  The extension is
   defined based on the "Signature-based Handling of Asserted
   information using toKENs (SHAKEN)" specification by the ATIS/SIP
   Forum IP-NNI Task Group.  It provides both (1) a specific set of
   levels of confidence in the correctness of the originating identity
   of a call originated in a SIP-based telephone network as well as (2)
   an identifier that allows the Service Provider (SP) to uniquely
   identify the origin of the call within its network.  This document
   obsoletes RFC 8588.
- **draft-ietf-tls-composite-mldsa-00** (new-draft, score 6, core_identity) [tls]: [Use of Composite ML-DSA in TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-composite-mldsa/) — Compositing the post-quantum ML-DSA signature with traditional
   signature algorithms provides protection against potential breaks or
   critical bugs in ML-DSA or the ML-DSA implementation.  This document
   specifies how such a composite signature can be formed using ML-DSA
   with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide
   authentication in TLS 1.3, including use in certificates.
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
- **draft-morrison-alter-uri-scheme-05** (new-draft, score 6, core_identity) [none]: [The 'alter' URI Scheme for Dispatchable ~handle References](https://datatracker.ietf.org/doc/draft-morrison-alter-uri-scheme/) — This document defines the alter URI scheme as a dispatchable
   reference syntax for ~handle identity references published in the DNS
   records defined in the companion specification for discovering Model
   Context Protocol servers through DNS TXT records.  An alter: URI
   binds a textual ~handle reference to a resolution and verification
   procedure that retrieves the handle's envelope from a publishing
   zone, validates the envelope's signature chain, and dispatches the
   result to an operating-system URI handler.  The reference may be
   scoped to an organisation, narrowed to a named facet of the identity,
   and addressed to a typed action surface.  The scheme is the
   addressing form of the ~handle@org:facet/action reference; its
   resolution semantics are those of that companion specification,
   reused without modification.

   The scheme is provider-neutral and introduces no new cryptographic
   primitive.  A handler given an alter: URI verifies the handle's
   envelope before acting on it, and where the URI addresses an action,
   verification precedes any side effect.  IANA provisionally registered
   the alter scheme under Section 4 of RFC 7595 on 5 October 2026.
- **draft-morrison-identity-pronouns-05** (new-draft, score 6, core_identity) [none]: [Identity Pronouns: A Reference-Axis Extension to ~handle Identity Systems](https://datatracker.ietf.org/doc/draft-morrison-identity-pronouns/) — This document defines an identity pronoun grammar as a reference axis
   orthogonal to the tier taxonomy that draft-morrison-identity-
   attributed-commits defines for the ~handle primitive of draft-
   morrison-mcp-dns-discovery.  A pronoun is a session-scoped reference
   that resolves client-side to a concrete handle using local session
   state before any cryptographic, DNS, or federation operation.  The
   tier taxonomy (Sovereign, Bot, Instrument) is unchanged; this
   specification introduces Absolute vs Pronoun as an orthogonal axis.
   A pronoun MUST NOT appear in a capability token, in a DNS record, in
   an Accord signature, or in any inter-organisational protocol payload.
   This document defines a single Wave-1 pronoun, ~org, that resolves to
   the concrete handle of the organisation bound to the caller's current
   session.  An appendix defines a relative-path pronoun grammar (e.g.
   ~./finance, ~../compliance) as a non-normative design surface for
   future work.  The mechanism is provider-neutral, introduces no new
   cryptographic primitive, and adds no load to DNS, capability-token
   issuers, or federated resolvers.
- **draft-morrison-schrock-identity-evidence-binding-00** (new-draft, score 6, core_identity) [none]: [Identity Evidence for Approver Enrollment and Payee Destination Binding](https://datatracker.ietf.org/doc/draft-morrison-schrock-identity-evidence-binding/) — This document profiles how a relying party uses external identity
   evidence when it admits a consequential action, without that evidence
   ever standing in for permission.  It defines two separate assertions,
   approver enrollment and payee destination binding, an authenticated
   binding from the exact evidence bytes to the action they support,
   offline status evidence with a freshness bound the relying party
   chooses, and the refusals that follow when any of it is missing.  It
   applies to the pre-execution Authorization Bundle of EP Authorization
   Receipts and to the Command Authority Envelope for operational
   technology, and through the action digest to the Binding Moment
   Envelope.
- **draft-morrison-substrate-observation-04** (new-draft, score 6, core_identity) [none]: [Substrate-Observation as an Alternative to Envelope Coordination for Concurrent Sessions](https://datatracker.ietf.org/doc/draft-morrison-substrate-observation/) — This memo describes a coordination-protocol anti-pattern observed in
   cross-tool agentic systems and a substrate-observation alternative
   that does not require negotiating a wire format between heterogeneous
   concurrent sessions of an identity-bound principal.  The memo is
   Informational and proposes no protocol element for standardisation.
   It sets out what should not be standardised for this problem, and
   why, and identifies the existing substrate mechanisms that serve in
   its place.  Companion memos describe the identity primitives this
   memo presumes.
- **draft-rosomakho-lamps-mldsa-mlkem-seed-only-00** (new-draft, score 6, verifiable_claims) [none]: [Deprecating Expanded ML-DSA and ML-KEM Private Key Encodings](https://datatracker.ietf.org/doc/draft-rosomakho-lamps-mldsa-mlkem-seed-only/) — This document updates RFC 9881 and RFC 9935 to require the seed
   representation when encoding Module-Lattice-Based Digital Signature
   Algorithm (ML-DSA) and Module-Lattice-Based Key-Encapsulation
   Mechanism (ML-KEM) private keys for interchange.  It deprecates the
   expanded and combined representations, while permitting their
   continued support for legacy imports.  These changes simplify
   implementation and improve interoperability by aligning the private-
   key representation with that used by JSON Object Signing and
   Encryption (JOSE) and CBOR Object Signing and Encryption (COSE).
   Internal private-key representations are unaffected.
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
- **draft-watts-reality-knowledge-consensus-separation-00** (new-draft, score 6, trust_infrastructure) [none]: [RKCS v0.1: Reality-Knowledge-Consensus Separation Framework](https://datatracker.ietf.org/doc/draft-watts-reality-knowledge-consensus-separation/) — A falsifiable, typed model separates ontological categories,
   epistemic states, evidence, consensus, uncertainty, provenance, and
   authority.  The proposed protocol forbids consensus-only promotion of
   physical claims and requires traceable evidence for changes in
   verification status.  Novelty and empirical advantage remain
   unestablished.
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
- **draft-fassbender-scitt-time-anchor-08** (new-draft, score 5, trust_infrastructure) [none]: [Umarise's Bitcoin-Anchored Temporal Proofs](https://datatracker.ietf.org/doc/draft-fassbender-scitt-time-anchor/) — This document describes the mechanism Umarise uses for temporal
   anchoring of digital artifacts: cryptographic hashes are committed to
   the Bitcoin blockchain via the OpenTimestamps protocol.  The
   resulting proof is independently verifiable by any party with access
   to independently validated Bitcoin chain data, without contacting
   Umarise or any other anchoring service.  The document is published so
   that other parties can produce and verify such proofs.  The SCITT
   Architecture is used as the primary integration example; no changes
   to it are required.
- **draft-guorong-utxo-dns-02** (new-draft, score 5, core_identity) [none]: [UTXO Domain Name System (UTXO6-DNS): Data RR for Cryptographic Endpoint Discovery](https://datatracker.ietf.org/doc/draft-guorong-utxo-dns/) — This document specifies a new DNS Data Resource Record (RRTYPE 260)
   for transporting opaque cryptographic pointers. The RDATA contains
   a CBOR-encoded endpoint identifier and an optional Verifiable Random
   Function (VRF) proof. This document prohibits apex usage and
   mandates the _utxo prefix.
- **draft-intra-handshake-fail-57** (new-draft, score 5, trust_infrastructure) [none]: [Early Attestation Considered Very Harmful (CVE-2026-100833, CVE-2026-100835,CVE-2026-108265, CVE-2026-108266, CVE-2026-108267, CVE-2026-108268, CVE-2026-108269, CVE-2026-92701, CVE-2026-92702, CVE-2026-108362, CVE-2026-33697, CVE-2026-108361 and others)](https://datatracker.ietf.org/doc/draft-intra-handshake-fail/) — The draft aims to provide technical details of [CVE-2026-100833] of
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
- **draft-irtf-cfrg-longfellow-00** (new-draft, score 5, adjacent_watchlist) [cfrg]: [Longfellow ZK](https://datatracker.ietf.org/doc/draft-irtf-cfrg-longfellow/) — This document defines an algorithm for generating and verifying a
   succinct non-interactive zero-knowledge argument that for a given
   input x and a circuit C, there exists a witness w, such that C(x,w)
   evaluates to 0.  The technique here combines the MPC-in-the-head
   approach for constructing ZK arguments described in Ligero [ligero]
   with a verifiable computation protocol based on sumcheck for proving
   that C(x,w)=0.
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
- **draft-watts-mica-nex-measurement-ingestion-00** (new-draft, score 5, adjacent_watchlist) [none]: [MICA-NEX v0.3: Authenticated Measurement Ingestion for Model-Agnostic Nano-Instrument Agent Swarms](https://datatracker.ietf.org/doc/draft-watts-mica-nex-measurement-ingestion/) — This document describes a narrow, testable next step in the MICA-NEX
   proposal: cryptographically binding nanoscale instrument measurement
   claims to externally provisioned acquisition and calibration signer
   roles while denying model planners the ability to self-certify
   measurement status.  The reference implementation uses Ed25519
   signatures, SHA-256 content binding, typed units, time windows,
   source-kind separation, and a persistent local replay ledger.  In a
   hardware-disconnected test harness, 60/60 signed synthetic test
   records from three simulated instrument classes were admitted and
   30/30 adversarial cases were rejected for the expected reason; 28/28
   Python tests passed.  No instrument, laboratory calibration, external
   reviewer, clinical context or independent physical replication was
   involved.  Signature validity is deliberately distinguished from
   scientific validity.
- **draft-wright-verdict-record-00** (new-draft, score 5, trust_infrastructure) [none]: [Verdict Records: Results on Claims that Cite Receipts as Evidence](https://datatracker.ietf.org/doc/draft-wright-verdict-record/) — This document defines a verdict record: a statement, bound to its
   issuer, of a result reached on a claim, together with the evidence
   the result relies on and the rule by which the result can be re-
   derived.  Evidence is cited by digest and can be a receipt or record
   in any format, such as a SCITT Receipt or an Agent Action Capsule.
   The document defines how a checker checks a verdict record and what
   such a check does and does not show.  It defines no receipt format
   and changes none.
- **draft-zhangb-cats-sci-implementation-02** (new-draft, score 5, adjacent_watchlist) [none]: [Metric Snapshot Exchange between SCI and C-SMA in CATS](https://datatracker.ietf.org/doc/draft-zhangb-cats-sci-implementation/) — This document specifies metric snapshot exchange between a Service
   Contact Instance (SCI) and a CATS Service Metric Agent (C-SMA).  It
   defines atomic replacement, ordering, and validity for periodic full
   snapshots and change-triggered updates over HTTPS/JSON.  An
   informative appendix explains how one shared snapshot YANG model can
   support generation of the publication and response messages.
- **draft-oga-musubi-settlement-02** (new-draft, score 4, adjacent_watchlist) [none]: [MUSUBI Settlement: Recomputing Whether an Agent Acted Within a Signed Grant](https://datatracker.ietf.org/doc/draft-oga-musubi-settlement/) — MUSUBI settlement is a deterministic function that takes a contract
   signed by two parties, a set of signed records of what an agent did
   under that contract, and a view of Bitcoin block headers, and
   computes whether the recorded acts stayed within the grant the
   contract gives.  Anyone holding the same bytes can recompute the
   result without trusting the party that produced it.  This document
   specifies one well defined part of that function, settle core v0,
   precisely enough that a second implementation can be written from the
   text and the published test vectors alone.  Settlement is not runtime
   enforcement and is not a judgement of liability.

## Adjacent / watchlist

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
- **draft-chen-idr-srv6-flowspec-path-redirect-04** (new-draft, score 3, core_identity) [idr]: [Flowspec Indirection-id Redirect for SRv6](https://datatracker.ietf.org/doc/draft-chen-idr-srv6-flowspec-path-redirect/) — BGP Flow Specification Version 2 (FSv2) provides an extensible
   framework for disseminating traffic flow filtering rules and
   associated traffic redirection actions.  This document specifies
   extensions to the FlowSpec Redirect to Indirection-id Extended
   Community specifically for SRv6 (Segment Routing over IPv6).  When
   received by a Flowspec client, this extended community triggers an
   indirection-based lookup within a localized mapping table to retrieve
   the target SRv6 Segment Identifier (SID), SRv6 Policy, or Binding SID
   (BSID) forwarding state.  This mechanism decouples control-plane BGP
   Flowspec redirection instructions from dynamic underlay path updates
   in SRv6 networks.
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
- **draft-dekok-emu-tls-tickets-00** (new-draft, score 3, core_identity) [none]: [Session Tickets in TLS-Based Extensible Authentication Protocol (EAP)](https://datatracker.ietf.org/doc/draft-dekok-emu-tls-tickets/) — This specification documents implementation issues with TLS 1.3
   session tickets, and provides guidance to correct the problems.
   Problems related to PQC is also discussed in relation to TLS-based
   EAP methods.  A partial solution to those issues is also proposed.
- **draft-eastlake-dnssd-rfc2931bis-sigzero-04** (new-draft, score 3, core_identity) [none]: [Domain Name System (DNS) Public Key Based Request and Transaction Authentication (SIGZERO, SIG(0))](https://datatracker.ietf.org/doc/draft-eastlake-dnssd-rfc2931bis-sigzero/) — This document specifies the SIGZERO and SIG(0) Domain Name System
   (DNS) Resource Records (RRs) which provide public key based
   authentication of DNS requests and transactions.  SIGZERO is the
   RECOMMENDED option.  This document obsoletes RFC 2931 and updates RFC
   6891.
- **draft-fu-ipsecme-ikev2-fn-dsa-pkr-00** (new-draft, score 3, core_identity) [none]: [FN-DSA Signature Authentication in IKEv2 with Public Key Recovery Mode](https://datatracker.ietf.org/doc/draft-fu-ipsecme-ikev2-fn-dsa-pkr/) — This document specifies FN-DSA for signature authentication in the
   Internet Key Exchange Protocol Version 2 (IKEv2).  It defines Public
   Key Recovery Mode (PKR-Mode), an extension that exploits the public
   key recovery property of FN-DSA, which reduces authentication payload
   size and enables certificateless authentication at the responder.
- **draft-gondwana-dkim2-authres-01** (new-draft, score 3, core_identity) [none]: [Reporting DKIM2 Verification Results in Authentication-Results](https://datatracker.ietf.org/doc/draft-gondwana-dkim2-authres/) — DomainKeys Identified Mail Signatures v2 (DKIM2) produces a
   verification result for an email message.  This document defines how
   that result is reported in the Authentication-Results header field,
   registering the "dkim2" authentication method, the result values it
   can take, and two properties which identify the signing domain and
   the point in the chain at which verification failed.  Diagnostic
   detail about each hop is carried in a human-readable comment.
- **draft-grant-ntp-server-identifier-extension-01** (new-draft, score 3, core_identity) [none]: [NTP Server Identifier Extension](https://datatracker.ietf.org/doc/draft-grant-ntp-server-identifier-extension/) — This document defines an extension field that gives operators of NTP
   services the ability to provide additional information about their
   servers to clients which request it.
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
- **draft-havel-nmop-simap-yang-04** (new-draft, score 3, adjacent_watchlist) [none]: [A YANG Data Model for SIMAP Core Topology](https://datatracker.ietf.org/doc/draft-havel-nmop-simap-yang/) — This document defines a YANG data model for Service & Infrastructure
   Maps (SIMAP) Core Topology.  It extends the RFC8345 YANG modules to
   support the subset of core SIMAP requirements.  This document will
   only focus on modelling proposal for each of the core SIMAP topology
   requirements not supported by RFC8345.  Any related terminology,
   concepts, use cases and requirements are defined outside of this
   draft and this draft will only refer to them, analyze how to model
   and propose the implementation solutions.
- **draft-housley-lamps-rfc3161-update-02** (new-draft, score 3, adjacent_watchlist) [lamps]: [Update to the Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)](https://datatracker.ietf.org/doc/draft-housley-lamps-rfc3161-update/) — This document updates RFC 3161.  It adds a requirement to ensure that
   the id-ct-TSTInfo content type is used to align with the best
   practices for signed attributes with CMS signed-data.  In addition,
   cross-protocol attacks are prevented by requiring that the Time Stamp
   Authority (TSA) dedicate the signature key pair to the time-stamping
   service.  Finally, the use of id-kp-timeStamping in the TSA
   certificate is clarified.
- **draft-ietf-cbor-serialization-11** (new-draft, score 3, adjacent_watchlist) [cbor]: [CBOR Serialization and Determinism](https://datatracker.ietf.org/doc/draft-ietf-cbor-serialization/) — RFC 8949 defines CBOR, a standard for serializing data types such as
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
- **draft-ietf-ccamp-wdm-tunnel-yang-09** (new-draft, score 3, adjacent_watchlist) [ccamp]: [A YANG Data Model for WDM Tunnels](https://datatracker.ietf.org/doc/draft-ietf-ccamp-wdm-tunnel-yang/) — This document defines a YANG data model for the provisioning and
   management of Traffic Engineering (TE) tunnels and Label Switched
   Paths (LSPs) in Optical Networks (Wavelength Switched Optical
   Networks (WSON) and Flexi-Grid Dense Wavelength Division Multiplexing
   (DWDM) Networks).

   The YANG data model defined in this document conforms to the Network
   Management Datastore Architecture (NMDA).
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
- **draft-ietf-httpapi-idempotency-key-header-08** (new-draft, score 3, adjacent_watchlist) [httpapi]: [The Idempotency-Key HTTP Header Field](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) — The HTTP Idempotency-Key request header field can be used to make
   non-idempotent HTTP methods such as POST or PATCH fault-tolerant.
- **draft-ietf-idr-flowspec-srv6-11** (new-draft, score 3, core_identity) [idr]: [BGP Flow Specification for SRv6](https://datatracker.ietf.org/doc/draft-ietf-idr-flowspec-srv6/) — This document specifies extensions to BGP Flow Specification (BGP-FS)
   to enable filtering of IPv6 packets based on the structural
   components of a standard SRv6 Segment Identifier (SID) or an SRv6
   Compressed SID (CSID) container present in the IPv6 Destination
   Address (representing the active segment of an SRv6 path).  Both
   NEXT-CSID and REPLACE-CSID flavors defined in RFC 9800 are supported.
- **draft-ietf-idr-sdwan-edge-discovery-32** (new-draft, score 3, core_identity) [idr]: [SD-WAN Edge and Underlay Tunnel Discovery Using BGP](https://datatracker.ietf.org/doc/draft-ietf-idr-sdwan-edge-discovery/) — This document specifies BGP mechanisms for SD-WAN (Software-Defined
   Wide Area Network) edge node attribute discovery.  These mechanisms
   comprise a new tunnel type and associated Sub-TLVs for the BGP Tunnel
   Encapsulation Attribute, and a new Subsequent Address Family
   Identifier (SAFI) carrying a typed NLRI for advertising SD-WAN
   underlay tunnel information.
- **draft-ietf-ivy-network-inventory-topology-12** (new-draft, score 3, adjacent_watchlist) [ivy]: [A YANG Network Data Model for Inventory Topology Mapping](https://datatracker.ietf.org/doc/draft-ietf-ivy-network-inventory-topology/) — This document specifies a YANG data model that extends the network
   topology data model (RFC 8345) to map network topologies with
   inventories.  The data model introduces the "inventory-topology"
   network type and augmentations for physical entity mappings and
   capabilities, which may be used by any overlay network topology for
   service provisioning validation, network maintenance, and capacity
   planning.
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
- **draft-ietf-lamps-one-signature-certs-04** (new-draft, score 3, adjacent_watchlist) [lamps]: [One Signature Certificates](https://datatracker.ietf.org/doc/draft-ietf-lamps-one-signature-certs/) — This document defines the signedDocumentBinding certificate
   extension, which binds a certificate to the signed content of a
   single digital signature.  Each certificate is created at the time of
   signing; the associated signing key is generated for the sole purpose
   of producing that one signature, is used for no other purpose, and is
   destroyed immediately afterwards.  Certificates carrying this
   extension are intended to be issued without a revocation mechanism
   and with no expiration, which simplifies long-term validation.
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
- **draft-ietf-schc-icmpv6-compression-03** (new-draft, score 3, adjacent_watchlist) [schc]: [Static Context Header Compression (SCHC) for the Internet Control Message Protocol (ICMPv6)](https://datatracker.ietf.org/doc/draft-ietf-schc-icmpv6-compression/) — This document describes how the ICMPv6 protocol can be integrated
   into the SCHC architecture.  It extends the YANG Data Model with new
   field IDs specific to ICMPv6 headers.

   To enhance the compression of ICMPv6 error messages, the document
   also introduces two new Matching Operators and two new Compression
   Decompression Actions to manipulate the ICMPv6 payload.

   Finally, for constrained networks such as LPWAN, it introduces a
   proxy behavior, where a SCHC Core end-point may anticipate the device
   reaction to incorrect messages.
- **draft-ietf-schc-universal-option-02** (new-draft, score 3, adjacent_watchlist) [schc]: [Options representation in SCHC YANG Data Models](https://datatracker.ietf.org/doc/draft-ietf-schc-universal-option/) — Keeping option identifiers in SCHC Rules simplifies interoperability
   and the evolution of SCHC compression when a protocol introduces
   options that the current SCHC implementation does not know.  This
   document explains why the Field Identifiers (FIDs) defined for CoAP
   options in RFC 9363 do not scale: a FID must be allocated,
   standardized and implemented for each option a protocol defines,
   before any Rule can describe that option.  It presents an evolution
   of the compression Rule defined in RFC 9363, in which an entry refers
   to an option by the pair (option space, option number), called a
   Universal Option, and in which entries are indexed, ordered and can
   reference one another.  It also presents a data model dedicated to
   CoAP, which processes options directly from the option number carried
   in the message, instead of mapping each option to a FID of its own.
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
- **draft-jiang-anima-traffic-management-in-aidc-01** (new-draft, score 3, ai_infrastructure) [none]: [The Use Case of Autonomic Traffic Management in the Artificial Intelligence Data Center](https://datatracker.ietf.org/doc/draft-jiang-anima-traffic-management-in-aidc/) — This document describes the use case of autonomic traffic management
   in Artificial Intelligence Data Centers (AIDCs), including the
   associated management requirements and challenges.  It discusses two
   representative approaches based on the ANIMA architecture:
   distributed autonomic traffic management and controller-led hybrid
   traffic management.
- **draft-kelley-webbotauth-sail-00** (new-draft, score 3, core_identity) [none]: [SAIL: Source Address Identity List](https://datatracker.ietf.org/doc/draft-kelley-webbotauth-sail/) — This document defines SAIL (Source Address Identity List), a metadata
   format served at a well-known URI in which the operator of automated
   HTTP clients publishes the IP prefixes its services send from,
   together with two optional assertions: that a service sends from
   nowhere else, and that nothing else of the operator's sends from a
   given set of prefixes.  A site that receives a request claiming to be
   one of those services can use that metadata to confirm the claim or,
   under those assertions, to refute it.  The mechanism is intended to
   complement reverse-DNS verification and HTTP Message Signatures.
- **draft-kunze-ark-44** (new-draft, score 3, core_identity) [none]: [The ARK Identifier Scheme](https://datatracker.ietf.org/doc/draft-kunze-ark/) — The ARK (Archival Resource Key) naming scheme is designed to
   facilitate the high-quality and persistent identification of
   information objects.  The label "ark:" marks the start of a core ARK
   identifier that can be made actionable by prepending the beginning of
   a URL.  Meant to be usable after today's networking technologies
   become obsolete, that core should be recognizable in the future as a
   globally unique ARK independent of the URL hostname, HTTP, etc.  A
   founding principle of ARKs is that persistence is purely a matter of
   service and neither inherent in an object nor conferred on it by a
   particular naming syntax.  The best any identifier can do is lead
   users to services that support robust reference.  A full-functioning
   ARK leads the user to the identified object and, with the "?info"
   inflection appended, returns a metadata record and a commitment
   statement that is both human- and machine-readable.  Tools exist for
   minting, binding, and resolving ARKs.

   Responsibility for this Document

   The ARK Alliance Technical Working Group [ARKAtech] is responsible
   for the content of this Internet Draft.  The group homepage lists
   monthly meeting notes and agendas starting from March 2019.
   Revisions of the spec are maintained on github at [ARKdrafts].
- **draft-li-savnet-sav-yang-09** (new-draft, score 3, adjacent_watchlist) [none]: [YANG Data Model for Intra-domain and Inter-domain Source Address Validation (SAVNET)](https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/) — This document describes a YANG data model for Intra-domain and
   Inter-domain Source Address Validation (SAVNET). The model serves as
   a base framework for configuring and managing an SAV subsystem,
   including SAV rule and SAV Tables, and expected to be augmented by
   other SAV technology models accordingly. Additionally, this document
   also specifies the model for the SAV Static application.
- **draft-lin-opsawg-ipfix-rocev2-02** (new-draft, score 3, ai_infrastructure) [none]: [Export of RoCEv2 Base Transport Header (BTH) Information Using IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-rocev2/) — This document defines a new set of IP Flow Information Export (IPFIX)
   Information Elements (IEs) for exporting Base Transport Header (BTH)
   information for Remote Direct Memory Access (RDMA) over Converged
   Ethernet version 2 (RoCEv2) traffic.  These extensions enable network
   monitoring systems to collect and analyze the characteristics of RDMA
   traffic widely used in high-performance computing, storage, and
   artificial intelligence applications.
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
- **draft-manelidis-dnsop-domain-affiliation-00** (new-draft, score 3, adjacent_watchlist) [none]: [Domain Affiliation Confirmation (DAC)](https://datatracker.ietf.org/doc/draft-manelidis-dnsop-domain-affiliation/) — Security systems assess domain names one at a time.  A new domain of
   an established organization therefore starts with no reputation, and
   a legitimate domain that resembles another organization's name can be
   reported as an impersonation.  This document defines Domain
   Affiliation Confirmation (DAC), by which the operator of a parent
   domain confirms that a child domain is operated by it or under its
   authority.  The child publishes a DNS record naming the parent and a
   random token; the parent confirms that token, in the DNS or over
   HTTPS, by naming the child.  Verification takes at most three DNS
   queries.  The parent publishes no list of its domains, and an
   affiliation is ended by deleting one record.  The document also
   states what a confirmation means to relying parties such as takedown
   services and reputation systems.
- **draft-mcguinness-oauth-resource-token-resp-04** (new-draft, score 3, authorization) [none]: [OAuth 2.0 Resource Parameter in Access Token Response](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-resource-token-resp/) — This specification defines a new parameter resource to be returned in
   OAuth 2.0 access token responses.  It enables clients to confirm that
   the issued token is valid for the intended resource.  This mitigates
   ambiguity and certain classes of security vulnerabilities such as
   resource mix-up attacks, particularly in systems that use the
   Resource Indicators for OAuth 2.0 specification [RFC8707].
- **draft-mendez-opsawg-yang-normalization-00** (new-draft, score 3, trust_infrastructure) [none]: [Normalized Representation of YANG Data for Equivalence Evaluation](https://datatracker.ietf.org/doc/draft-mendez-opsawg-yang-normalization/) — This document defines a normalization procedure for YANG-modeled
   information.  The procedure enables different serialized
   representations conveying equivalent information to produce the same
   normalized representation independently of the input encoding and
   applicable representation conventions.  The normalized representation
   is intended to support comparison, hashing, integrity verification,
   provenance, and other procedures that require consistent
   representation of equivalent YANG-modeled information.
- **draft-morrison-claim-currency-00** (new-draft, score 3, trust_infrastructure) [none]: [Claim Currency: A Read-Time Decay Evaluator and Observation-Gated Re-Assertion Discipline for Concurrent Readers of a Reconciled Substrate](https://datatracker.ietf.org/doc/draft-morrison-claim-currency/) — This memo specifies a read-time freshness evaluator and an
   observation-gated re-assertion discipline for concurrent autonomous
   readers of a single reconciled substrate history.  For every claim
   read from the substrate, a three-state currency band (FRESH, AGING,
   STALE) is derived at read time from the durable history and is never
   stored.  A claim whose derived band is not FRESH MUST NOT be re-
   emitted as current and MUST NOT ground a new durable claim; the sole
   transition back to currency is a fresh observation of the claim's
   basis, enforced at the substrate's append stage rather than at any
   reader's discretion.  The memo is the claim-layer consumer that two
   companion specifications, Substrate-Observation as an Alternative to
   Envelope Coordination and the Substrate-Provenance Annotation
   Grammar, each left unspecified.  The contribution is a specific
   composition: a read-time-derived band, a decay clock measured in
   missing observations learned from a basis's own change cadence, an
   append-stage rejection of any claim citing a basis that is no longer
   the head of its lineage, and observation as the only admissible
   refresh.  No new substrate is standardised; the discipline composes
   with substrate that already exists.
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
- **draft-rosomakho-httpbis-tunnels-signatures-00** (new-draft, score 3, core_identity) [none]: [Authenticating HTTP Tunnels with HTTP Message Signatures](https://datatracker.ietf.org/doc/draft-rosomakho-httpbis-tunnels-signatures/) — This document specifies client authentication for HTTP tunnel
   establishment using HTTP Message Signatures.  It covers the CONNECT
   method, extended CONNECT in HTTP/2 and HTTP/3, and HTTP/1.1 Upgrade.
   It defines signature coverage and replay protection using either a
   client-generated nonce or a server-provided nonce obtained through an
   Accept-Signature challenge.
- **draft-shigeya-dns-opkey-00** (new-draft, score 3, verifiable_claims) [none]: [Using Secure DNS for Originator Profile](https://datatracker.ietf.org/doc/draft-shigeya-dns-opkey/) — The Originator Profile Framework (OPF) provides information about the
   origin of content, together with a verifiable binding of the content
   to that origin, in digital media, advertising, and email ecosystems.
   In the framework, an originator holds an Originator Profile (OP): a
   Core Profile (CP) issued by a CP issuer, and Profile Annotations (PA)
   issued by PA issuers.  The CP carries the public keys with which the
   originator signs the data it originates; a PA annotates the CP with
   validated attributes about the originator.  Verifiers need an
   authenticated way to confirm that the public keys used by an
   originator and by the issuers of these documents are currently valid,
   that the originator's CP has not been revoked by its CP issuer, and
   that a PA has not been revoked by its PA issuer.

   This document defines the OPKEY DNS resource record, which associates
   a public key with a DNS name under the _op label.  Its wire and
   presentation formats are those of the TLSA record.  The DNS does not
   carry the CP or the PAs themselves; it carries records that identify
   their keys by digest, and it signals, through the presence or absence
   of OPKEY records, whether a CP has been revoked.

   The document specifies where OPKEY records are located, how a
   verifier uses them, and how DNSSEC is used to authenticate them.  It
   also specifies two further records under _op, of existing types: an
   SVCB record by which an originator names the CP issuers it accepts,
   and a TXT record whose presence signals that a PA issuer has revoked
   a PA.  Operational aspects of the framework, such as registration,
   key rollover procedures, and revocation timing, are outside the scope
   of this document.
- **draft-sun-ainetops-nma-lifecycle-yang-00** (new-draft, score 3, adjacent_watchlist) [none]: [NMA Lifecycle Management YANG Data Model](https://datatracker.ietf.org/doc/draft-sun-ainetops-nma-lifecycle-yang/) — Network Management Agents (NMAs) deployed in production networks
   require a consistent representation of lifecycle information for
   admission, operation, version replacement, and retirement.  This
   document defines the ietf-nma-lifecycle YANG data model, covering
   basic NMA information and configuration, lifecycle state, and event
   notifications.  The model provides a consistent lifecycle data
   structure for NMAs from different vendors.
- **draft-taylor-dtn-imc-scheme-00** (new-draft, score 3, core_identity) [none]: [The 'imc' URI Scheme for Bundle Protocol Multicast](https://datatracker.ietf.org/doc/draft-taylor-dtn-imc-scheme/) — This document defines the 'imc' URI scheme, a concise integer-based
   scheme for identifying Bundle Protocol Version 7 (BPv7) endpoints
   that are not singleton endpoints, termed multicast endpoints.  The
   structure of 'imc' URIs mirrors that of the 'ipn' URI scheme: each
   'imc' URI comprises an Allocator Identifier, a Group Number, and a
   Service Number.  This document specifies the textual syntax of 'imc'
   URIs, their interpretation when used as BPv7 Endpoint Identifiers,
   their CBOR encoding, and the corresponding EID Pattern, and requests
   the associated IANA registrations.
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
- **draft-yanteri-humancollab-statements-00** (new-draft, score 3, agent_identity) [none]: [Accountable Statements Between AI Agents, Businesses and People](https://datatracker.ietf.org/doc/draft-yanteri-humancollab-statements/) — AI agents increasingly act on information they cannot check: what a
   business can supply, what a person said, what rules a platform
   applies.  This document describes a minimal way to make such
   statements accountable.  Every statement is signed by its author,
   bound where possible to a domain the author controls, and sealed in a
   public append-only Merkle log whose tree heads are signed,
   timestamped and publicly monitored.  The design proves who said what
   and when, and that the record was not rewritten.  It deliberately
   does not attempt to prove that a statement is true.
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
- **draft-gravit-gevp-11** (new-draft, score 2, ignored_after_review) [none]: [Gravit Epistemic Verification Protocol (GEVP)](https://datatracker.ietf.org/doc/draft-gravit-gevp/) — The Gravit Epistemic Verification Protocol (GEVP) defines how signed
   evidence Records about an Artifact are screened, grouped by
   independent source and evaluated, so that a claim is never promoted
   beyond what independent evidence supports.  It specifies the
   Epistemic State Machine, the Record format and its signature, the
   meaning of the signed result of a Record, a verifier registry
   accepted under a threshold of root keys, a content-addressed Decision
   Record that anyone can reproduce, and optional signed receipts that
   let an auditor check a history of decisions offline.  It maps these
   states to the evidence taxonomy of the Gravit Verifiable Epistemic
   Decision Standard (VEDS).
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
- **draft-illyes-webbotauth-jafar-01** (new-draft, score 2, ignored_after_review) [none]: [A JSON-Based Format for Publishing IP Ranges of Automated HTTP Clients](https://datatracker.ietf.org/doc/draft-illyes-webbotauth-jafar/) — This document defines a standardized JSON format for operators of
   automated HTTP clients (e.g., web crawlers, AI bots) to publicly
   disclose their IP address ranges.  A consistent, machine-readable
   format for IP range publication simplifies the task of identifying
   and verifying legitimate automated traffic, thereby decreasing
   maintenance load on website operators while reducing the risk of
   inadvertently blocking beneficial clients.  This specification
   codifies and extends common existing practices to provide a simple
   yet extensible format that accommodates a variety of use cases.
- **draft-morrison-live-reference-resolution-02** (new-draft, score 2, ignored_after_review) [none]: [Live Reference Resolution for Autonomous Agent Beliefs](https://datatracker.ietf.org/doc/draft-morrison-live-reference-resolution/) — A recurring class of autonomous-agent failure arises when an agent
   acts on a belief read from a cached, derived, or proxy copy that has
   silently diverged from the authority the belief claims to represent.
   This document describes a reference-resolution discipline for the
   working beliefs an agent reasons and acts from.  Each belief is held
   as a reference to a single named lowest authority and is resolved
   live at the point of use, with verification.  When the authority is
   unobservable or the resolved value is stale, the belief takes an
   explicit uncertainty state and never falls back to a prior cached
   value.  That state propagates to any belief derived from it, and an
   uncertain belief feeding a costly or irreversible act blocks or
   escalates rather than proceeding.  Every resolution chain terminates
   in a single self-authorising root.  The document is Informational.
   It records a discipline and a vocabulary; it does not define a wire
   protocol.
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
- **draft-watts-relational-echo-calculus-00** (new-draft, score 2, ignored_after_review) [none]: [Relational Echo Calculus (REC): A Transformation-First Mathematical Communication Prototype](https://datatracker.ietf.org/doc/draft-watts-relational-echo-calculus/) — This document describes a transformation-first teaching notation for
   mathematical communication to unfamiliar receivers.  The prototype
   operates on finite motifs drawn from the vertices of a Hamming
   hypercube.  Echo operations act through coordinate permutations and
   binary translations.  We distinguish invariance of a coarse signature
   from proof of exact orbit equivalence, exhibiting two four-
   dimensional patterns that have equal pairwise-distance multisets but
   different induced adjacency.  A synthetic toy decoder reconstructs
   arbitrary token meanings when its complete transformation hypothesis
   class is supplied.  The main testable conjecture is that instruction
   ordered by invariance might improve cross-agent decoding over
   instruction ordered by arithmetic under matched information budgets.
   The conjecture has not been experimentally evaluated; no new
   extraterrestrial signal or new mathematical theorem is claimed.
- **draft-yang-tsvwg-tcp-oam-probing-00** (new-draft, score 2, ignored_after_review) [none]: [TCP Connectivity Probing Extension for Highly-Dynamic Networks](https://datatracker.ietf.org/doc/draft-yang-tsvwg-tcp-oam-probing/) — This document defines TCP OAM-ACK, a TCP extension for fast
   transport-layer connectivity detection in highly-dynamic networks
   such as LEO satellite constellations, high-speed rail, and ad-hoc
   intelligent agent networks.  Traditional TCP keep-alive uses fixed
   long probe intervals and cannot rapidly differentiate genuine link
   outages from congestion-induced packet loss.  TCP OAM-ACK negotiates
   capability via TCP SYN/SYN-ACK handshake using shared experimental
   TCP option [RFC6994].  A sender adaptively shortens probing interval
   upon consecutive probe ACK losses, triggers path-switching
   notifications to external path-control entities instead of
   mis-invoking TCP congestion window reduction.  This mechanism acts
   like transport-layer BFD for TCP connections.  This document
   describes option formats, sender/receiver behavior, fallback
   strategies, RTT-assisted early triggering, and interaction with path
   management modules.
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

- **draft-abraitis-idr-addpath-paths-limit-06** (new-draft, score 0, ignored_after_review) [none]: [Paths Limit for Multiple Paths in BGP](https://datatracker.ietf.org/doc/draft-abraitis-idr-addpath-paths-limit/) — This document specifies a BGP capability that complements the ADD-
   PATH Capability by indicating the maximum number of paths a BGP
   speaker can receive from a peer, optimizing the transmission of BGP
   routes by selectively relaying pertinent routes instead of the entire
   set.

   This document also defines a new BGP Cease NOTIFICATION message
   subcode, "Maximum Number of Paths Reached", used when a BGP speaker
   terminates a peering because the number of paths received from a
   neighbor for a prefix exceeds the Paths Limit advertised in the
   PATHS-LIMIT Capability.
- **draft-acosta-deepspace-celestial-bodies-registry-04** (new-draft, score 0, ignored_after_review) [none]: [Defining a Celestial Bodies Reference Framework for Deep Space Internet Addressing](https://datatracker.ietf.org/doc/draft-acosta-deepspace-celestial-bodies-registry/) — This document highlights the operational framework within Deepspace/
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
   Celestial Body for networking purposes.  From a resource-management
   perspective, this framework remains identical regardless of whether
   the target location hosts human colonies, scientific equipment, or
   autonomous robotic assets; any entity requiring internet and
   communication access must rely on a stable celestial anchor.
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
- **draft-akiyama-cmg-04** (new-draft, score 0, ignored_after_review) [none]: [Content-based IP-Multicast Grouping Framework for Real-time Spatial Sensing and Control Applications with Edge Computing](https://datatracker.ietf.org/doc/draft-akiyama-cmg/) — This document describes a content-based multicast grouping framework
   aimed at simplifying routing control and reducing unnecessary traffic
   in large-scale networks for real-time spatial sensing and control
   applications.  The framework introduces content-based multicast
   groups, which are managed at the local level by routers without the
   need for global group membership tracking.  Additionally, a "topic"
   concept is introduced, allowing routers to manage multicast delivery
   based on data content.  This framework reduces bandwidth consumption
   and simplifies multicast routing while offering flexible data
   delivery across various topics.
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
- **draft-becker-cnsa2-ssh-profile-06** (new-draft, score 0, ignored_after_review) [none]: [Commercial National Security Algorithm (CNSA) Suite 2.0 Profile for SSH](https://datatracker.ietf.org/doc/draft-becker-cnsa2-ssh-profile/) — This document defines a base profile of SSH for use with the US
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
- **draft-chen-ipsec-problems-for-ntn-network-02** (new-draft, score 0, ignored_after_review) [none]: [IPsec Challenges in Non-Terrestrial Networks (NTN)](https://datatracker.ietf.org/doc/draft-chen-ipsec-problems-for-ntn-network/) — This document describes the problems in the use of IPsec in satellite
   Internet and NTN network scenarios.
- **draft-chen-lamps-fndsa-composite-sigs-00** (new-draft, score 0, ignored_after_review) [none]: [==Composite FN-DSA for use in X.509 Public Key Infrastructure==](https://datatracker.ietf.org/doc/draft-chen-lamps-fndsa-composite-sigs/) — To facilitate a robust and secure transition to post-quantum
   cryptography, this document defines a method for creating composite
   signature algorithms by combining the Fast-Fourier Transform over
   NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA) with modern
   classical signature algorithms.  These composite algorithms are
   treated as new, atomic primitives.

   This document specifies algorithm identifiers, public key structures,
   and signature formats for using these composite algorithms within the
   Internet X.509 Public Key Infrastructure.  The methodology is
   designed to align with modern cryptographic practices, including a
   principle of strict security level alignment, ensuring a consistent
   and predictable security posture for all defined algorithms.
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
- **draft-dahm-opsawg-tacacs-sshpk-00** (new-draft, score 0, ignored_after_review) [none]: [SSH Public Key Distribution for Device Administration using Terminal Access Controller Access-Control System Plus (TACACS+)](https://datatracker.ietf.org/doc/draft-dahm-opsawg-tacacs-sshpk/) — SSH [RFC4251] provides a robust and reliable mechanism to connect to
   network devices for administration.  Conventionally, the public keys
   required to authenticate SSH sessions are provisioned directly on the
   network devices.  This document adds an extension to Terminal Access
   Controller Access-Control System Plus (TACACS+) to eliminate the need
   for the direct provisioning of SSH public keys onto the Network
   Devices.
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
- **draft-gandhi-ippm-stamp-link-crc-00** (new-draft, score 0, ignored_after_review) [none]: [Simple Two-Way Active Measurement Protocol (STAMP) Extension for Link CRC Error Measurement](https://datatracker.ietf.org/doc/draft-gandhi-ippm-stamp-link-crc/) — The Simple Two-Way Active Measurement Protocol (STAMP), specified in
   RFC 8762, supports active measurement of network performance.  This
   document defines a STAMP Type-Length-Value (TLV) that reports
   receive-side link statistics: packets received, packets received with
   Cyclic Redundancy Check (CRC) errors, and bytes received.  The link
   is identified using the Micro-session ID TLV specified in RFC 9534.
   These measurements support fiber-quality monitoring to provide SLA
   assurance.
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
- **draft-gopal-pim-pfm-pre-join-subtlv-00** (new-draft, score 0, ignored_after_review) [none]: [PIM Flooding Mechanism Pre-join Sub-TLV](https://datatracker.ietf.org/doc/draft-gopal-pim-pfm-pre-join-subtlv/) — The PIM Flooding Mechanism and Source Discovery (PFM-SD) extension
   enables PIM routers to announce active multicast sources.  The Group
   Source Info (GSI) TLV extends PFM-SD by allowing Sub-TLVs to be
   included with a source announcement.

   This document defines the Pre-join Sub-TLV, which carries the PIM
   Router-ID of a router selected by the First-Hop Router (FHR).  The
   selected router can establish multicast forwarding state before data
   arrives, reducing join latency.
- **draft-grayson-5580uncertainty-01** (new-draft, score 0, ignored_after_review) [none]: [Carrying location objects with uncertainty in RADIUS](https://datatracker.ietf.org/doc/draft-grayson-5580uncertainty/) — This document describes a new location profile for use with the
   RADIUS Location-Data Attribute.  The new profile is used to carry a
   geospatial location profile that includes location uncertainty.
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
- **draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext-01** (new-draft, score 0, ignored_after_review) [none]: [Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC with SigTag Extension](https://datatracker.ietf.org/doc/draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext/) — This document describes a mechanism to reduce post-quantum
   cryptographic (PQC) network transmission overhead when using Merkle
   Tree Ladders (MTL) in DNS Security Extensions (DNSSEC).  This
   document refers to this as SigTag and describes the use of EDNS(0) to
   enable its use.  SigTag allows a client to indicate its knowledge of
   a specific MTL ladder.  The DNS server can then use this signal to
   determine if it can omit the full underlying signature in its
   response, thereby reducing the message payload.
- **draft-he-fann-wan-fcn-00** (new-draft, score 0, ignored_after_review) [none]: [Fast Congestion Notification (FCN) in Wide Area Network (WAN) Interconnecting RoCEv2 Networks](https://datatracker.ietf.org/doc/draft-he-fann-wan-fcn/) — Wide Area Network (WAN), when interconnecting RoCEv2 networks, needs
   to meet the performance requirements of "high throughput, low
   latency, and minimal packet loss".  This document describes a
   solution to Fast Congestion Notification (FCN) in WAN interconnecting
   RoCEv2 networks, especially applicable to tunnel encapsulation.
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
- **draft-ietf-ccamp-actn-optical-transport-mgmt-06** (new-draft, score 0, ignored_after_review) [ccamp]: [Integrating YANG Configuration and Management into an Abstraction and Control of TE Networks (ACTN) System for Optical Networks](https://datatracker.ietf.org/doc/draft-ietf-ccamp-actn-optical-transport-mgmt/) — Many network technologies are operated as Traffic Engineering (TE)
   networks.  Optical networks are a particular case, and have complex
   technology-specific details.

   Abstraction and Control of TE Networks (ACTN) is a management
   architecture that abstracts TE network resources to provide a limited
   network view for customers to request and self-manage connectivity
   services.  It also provides functional components to orchestrate and
   operate the network.

   Management of legacy optical networks is often provided via Fault,
   Configuration, Accounting, Performance, and Security (known as FCAPS)
   using mechanisms such as the Multi-Technology Operations System
   Interface (MTOSI) and the Common Object Request Broker Architecture
   (CORBA).  FCAPS can form a critical part of configuration management
   and service assurance for network operations.  However, the ACTN
   architecture as described in RFC 8453 does not include consideration
   of FCAPS.

   This document enhances the ACTN architecture as applied to optical
   networks by introducing support for detailed YANG Configuration and
   Management, effectively adding support for FCAPS.  It considers which
   elements of existing IETF YANG work can be used to solve existing
   scenarios and emerging technologies, and what new work may be needed.
   In doing so, this document adds rich-detail network management (RDNM)
   to the ACTN architecture.  This enhanced architecture may then be
   used to evolve networks from CORBA and MTOSI FCAPS interfaces to
   IETF-based YANG and RESTful APIs.
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
- **draft-ietf-dtn-bibe-01** (new-draft, score 0, ignored_after_review) [dtn]: [Bundle-in-Bundle Encapsulation](https://datatracker.ietf.org/doc/draft-ietf-dtn-bibe/) — This document describes Bundle-in-Bundle Encapsulation (BIBE), a
   Delay-Tolerant Networking (DTN) Bundle Protocol (BP) tunneling
   mechanism by which a bundle is carried as the payload of one or more
   encapsulating bundles, allowing security measures and routing policy
   to be applied to the encapsulating bundle without modification of the
   encapsulated bundle.  The protocol includes an optional segmentation
   mechanism, allowing a large encapsulated bundle to be carried in
   multiple encapsulating bundles.
- **draft-ietf-dult-accessory-protocol-01** (new-draft, score 0, ignored_after_review) [dult]: [Detecting Unwanted Location Trackers Accessory Protocol](https://datatracker.ietf.org/doc/draft-ietf-dult-accessory-protocol/) — This document lists a set of best practices and protocols for
   accessory manufacturers whose products have built-in location-
   tracking capabilities.  By following these requirements and
   recommendations, a location-tracking accessory will be compatible
   with unwanted tracking detection and alerts on mobile platforms.
   This is an important capability for improving the privacy and safety
   of individuals in the circumstance that those accessories are used to
   track their location without their knowledge or consent.
- **draft-ietf-grow-bmp-over-quic-01** (new-draft, score 0, ignored_after_review) [grow]: [Using BMP over QUIC connection](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-over-quic/) — The BGP Monitoring Protocol (BMP) provides a convenient interface for
   obtaining route views by monitoring BGP sessions.  BMP operates over
   TCP and is unidirectional (from client to server).  QUIC provides
   multiple simultaneous streams to carry data in one direction,
   enabling much better efficiency and performance for both peers, in
   particular unidirectional streams can provide reverse data protection
   for the sender.  QUIC also provides shorter handshake and includes
   TLS.  This document describes how to use BMP over the QUIC transport
   protocol, named BMPoQUIC.
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
- **draft-ietf-idr-bgp4-rfc4271bis-03** (new-draft, score 0, ignored_after_review) [idr]: [A Border Gateway Protocol 4 (BGP-4)](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) — This document discusses the Border Gateway Protocol (BGP), which is
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

   This document obsoletes RFC 4271 and many other RFCs.  It updates RFC
   7606 by subsuming its core functionality.
- **draft-ietf-idr-rt-derived-community-13** (new-draft, score 0, ignored_after_review) [idr]: [Extended Communities Derived from Route Targets](https://datatracker.ietf.org/doc/draft-ietf-idr-rt-derived-community/) — This document describes how an Extended Community is derived from a
   Route Target, how each such Route Target derived Extended Community
   corresponds to the Route Target, and how the two differ.  It records
   the code points assigned for this purpose and requests the remaining
   assignments.  It does not specify how Route Target derived Extended
   Communities are used; that is left to the documents specifying each
   use.
- **draft-ietf-iotops-iot-dns-guidelines-05** (new-draft, score 0, ignored_after_review) [iotops]: [IoT DNS Security and Privacy Guidelines](https://datatracker.ietf.org/doc/draft-ietf-iotops-iot-dns-guidelines/) — This document outlines guidance for Internet of Things (IoT)
   manufacturers regarding the implementation of DNS stub resolver
   software on devices, and for the management zones used for purposes
   such as device configuration and software upgrades.  It aims to
   mitigate security threats, enhance privacy, and to address
   operational security challenges.

   DNS resolution between devices and management zone servers depends
   upon DNS services within operator networks, and these services and
   operator networks can be impacted by device behavior.  Hence, this
   document also provides guidance to network operators that deploy IoT
   devices to mitigate the specific risks identified in this document
   and take advantage of improved DNS security mechanisms provided by
   manufacturers.
- **draft-ietf-ippm-alt-mark-deployment-10** (new-draft, score 0, ignored_after_review) [ippm]: [Alternate Marking Deployment Framework](https://datatracker.ietf.org/doc/draft-ietf-ippm-alt-mark-deployment/) — This document provides a framework for Alternate Marking deployment
   and includes considerations and guidance for the deployment of the
   methodology.
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
- **draft-ietf-ippm-stamp-mpls-hdr-03** (new-draft, score 0, ignored_after_review) [ippm]: [Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Reflecting STAMP Packet MPLS Network Action Headers](https://datatracker.ietf.org/doc/draft-ietf-ippm-stamp-mpls-hdr/) — The Simple Two-Way Active Measurement Protocol (STAMP) and its
   optional extensions can be used for Edge-to-Edge (E2E) active
   measurements.  In Situ Operations, Administration, and Maintenance
   (IOAM) data fields can be used for recording and collecting Hop-by-
   Hop (HBH) and E2E operational and telemetry information.  This
   document extends STAMP to reflect MPLS Network Action Sub-Stacks and
   Post-Stack MPLS Headers for HBH and E2E active measurements, for
   example, using the IOAM data fields.
- **draft-ietf-ipsecme-encrypted-esp-ping-04** (new-draft, score 0, ignored_after_review) [ipsecme]: [ESP Echo Protocol](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-encrypted-esp-ping/) — This document defines the ESP Echo Protocol, an extension to the ESP
   AGGFRAG protocol [RFC9347] that provides an Echo Request and Echo
   Reply mechanism for IP Security (IPsec) link diagnostics.  It enables
   endpoints to assess end-to-end path reachability, and it defines
   probe packets that can be used for path Maximum Transmission Unit
   (MTU) discovery, using Encapsulating Security Payload (ESP) packets.

   The protocol supports two modes of operation: an encrypted mode used
   over established IPsec Security Associations (SAs), with an option to
   specify a preferred reply path when multiple SAs exist between the
   peers, and an unencrypted mode used outside the context of a
   negotiated ESP SA.  In addition to bidirectional echo probing, the
   protocol supports sending one-way ESP packets without eliciting a
   reply, primarily for keepalives, NAT and firewall pinhole
   maintenance, and unidirectional link diagnostics.

   A peer can announce support for ESP Echo using a new IKEv2 Status
   Notification ESP_ECHO_SUPPORTED.
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
- **draft-ietf-lsr-l2-bundle-member-remote-id-11** (new-draft, score 0, ignored_after_review) [lsr]: [Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members](https://datatracker.ietf.org/doc/draft-ietf-lsr-l2-bundle-member-remote-id/) — In networks where Layer 2 (L2) interface bundles (such as a Link
   Aggregation Group (LAG) as defined in IEEE 802.1AX) are deployed, a
   controller may need to collect the connectivity relationships between
   bundle members for traffic engineering (TE) purposes.  This document
   describes how Open Shortest Path First (OSPF) and Intermediate System
   to Intermediate System (IS-IS) advertise the remote interface
   identifiers for L2 bundle members.  The corresponding extension of
   BGP Link State (BGP-LS) is also specified.
- **draft-ietf-lsr-pcpps-00** (new-draft, score 0, ignored_after_review) [lsr]: [IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)](https://datatracker.ietf.org/doc/draft-ietf-lsr-pcpps/) — [I-D.many-teas-power-steering] introduces a Power Conserving Path
   Placement Strategy (PCPPS).  When possible, PCPPS concentrates
   traffic onto a small set of network resources.  When traffic is
   concentrated onto a small set of network resources, other network
   resources become idle and can be powered down until they are needed
   again.  This conserves energy and reduces environmental impact.

   PCPPS uses information that is distributed by an IGP.  This document
   specifies the IS-IS encoding for that information.
- **draft-ietf-mailmaint-pdparchive-03** (new-draft, score 0, ignored_after_review) [mailmaint]: [Personal Data Portability Archive](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-pdparchive/) — This document proposes the Personal Data Portability Archive format
   (PDPA), suitable for import/export, backup/restore, and data transfer
   scenarios for personal data.
- **draft-ietf-manet-inet-gap-analysis-11** (new-draft, score 0, ignored_after_review) [manet]: [MANET Internetworking Architecture, Problem Statement and Gap Analysis](https://datatracker.ietf.org/doc/draft-ietf-manet-inet-gap-analysis/) — [RFC2501] defines a MANET as "an autonomous system of mobile nodes.
   The system may operate in isolation, or may have gateways to and
   interface with a fixed network" (such as the global public Internet).
   This document presents a MANET Internetworking architecture, problem
   statement and gap analysis.
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
- **draft-ietf-netmod-yang-schema-comparison-10** (new-draft, score 0, ignored_after_review) [netmod]: [YANG Schema Comparison](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-schema-comparison/) — This document specifies an algorithm with two input variants for
   comparing revisions of a YANG schema to determine the scope of
   changes and produce a list of the changes between the revisions.  The
   output of the algorithm can be used to help select an appropriate
   YANG semantic version number for a new YANG Module revision.  It also
   specifies a YANG module for YANG-structured output of these
   algorithms, that can be easily consumed in a machine-readable way.
- **draft-ietf-netmod-yang-xml-01** (new-draft, score 0, ignored_after_review) [netmod]: [XML Encoding of Data Modeled with YANG](https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-xml/) — This document defines encoding rules for representing YANG modeled
   configuration data, state data, parameters of Remote Procedure Call
   (RPC) operations or actions, and notifications defined using XML.
- **draft-ietf-nmop-simap-concept-15** (new-draft, score 0, ignored_after_review) [nmop]: [SIMAP: Concept, Requirements, and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-nmop-simap-concept/) — This document defines the concept of Service & Infrastructure Maps
   (SIMAP) and identifies a set of SIMAP requirements and use cases.
   The SIMAP was previously known as Digital Map. SIMAP evolves the
   earlier 'Digital Map' concept by making explicit the ties between
   service and infrastructure layers, clarifying expected outcomes for
   operations and automation, and addressing ambiguity associated with
   the term 'digital.'

   The document intends to be used as a reference for the assessment of
   the various topology modules to meet SIMAP requirements.
- **draft-ietf-nvo3-rfc7348bis-12** (new-draft, score 0, ignored_after_review) [nvo3]: [Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks](https://datatracker.ietf.org/doc/draft-ietf-nvo3-rfc7348bis/) — This document specifies Virtual eXtensible Local Area Network
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
- **draft-ietf-pce-flexible-grid-20** (new-draft, score 0, ignored_after_review) [pce]: [PCEP Extension for Flexible Grid Networks](https://datatracker.ietf.org/doc/draft-ietf-pce-flexible-grid/) — This document provides the Path Computation Element Communication
   Protocol (PCEP) extensions for the support of Routing and Spectrum
   Assignment (RSA) in Flexible Grid networks.
- **draft-ietf-pce-sr-p2mp-policy-22** (new-draft, score 0, ignored_after_review) [pce]: [PCEP extensions for SR P2MP Policy](https://datatracker.ietf.org/doc/draft-ietf-pce-sr-p2mp-policy/) — Segment Routing (SR) Point-to-Multipoint (P2MP) Policies are a set of
   policies that enable an architecture for P2MP service delivery.  This
   document specifies extensions to the Path Computation Element
   Communication Protocol (PCEP) that allow a stateful PCE to compute
   and initiate P2MP paths for SR-MPLS from a Root to a set of Leaf
   nodes.
- **draft-ietf-pim-ipv6-zeroconf-assignment-16** (new-draft, score 0, ignored_after_review) [pim]: [Zero-Configuration Assignment of IPv6 Multicast Addresses Using mDNS](https://datatracker.ietf.org/doc/draft-ietf-pim-ipv6-zeroconf-assignment/) — This document describes a zero-configuration protocol for dynamically
   assigning IPv6 multicast addresses that are unique at the link-layer.
   Applications randomly assign multicast group IDs from a specified
   range and prevent collisions by using Multicast DNS (mDNS) to publish
   resource records under a new "eth-addr.arpa" domain.  This protocol
   satisfies all of the requirements and most of the desired
   characteristics listed in RFC 10019.
- **draft-ietf-plants-mtc-deploy-use-cases-00** (new-draft, score 0, ignored_after_review) [plants]: [Merkle Tree Certificates Deployment Use Cases](https://datatracker.ietf.org/doc/draft-ietf-plants-mtc-deploy-use-cases/) — Merkle Tree Certificates (MTC) I-D.ietf-plants-merkle-tree-certs has
   been defined for the use case of the WebPKI.  In this document we
   explore when and how MTC in parts or full can be used in different
   use cases.  Some of this use-cases may provide benefit for private
   PKI usage.
- **draft-ietf-quic-load-balancers-22** (new-draft, score 0, ignored_after_review) [quic]: [QUIC-LB: Generating Routable QUIC Connection IDs](https://datatracker.ietf.org/doc/draft-ietf-quic-load-balancers/) — QUIC address migration allows clients to change their IP address
   while maintaining connection state.  To reduce the ability of an
   observer to link two IP addresses, clients and servers use new
   connection IDs when they communicate via different client addresses.
   This poses a problem for traditional "layer-4" load balancers that
   route packets via the IP address and port 4-tuple.  This
   specification provides a standardized means of securely encoding
   routing information in the server's connection IDs so that a properly
   configured load balancer can route packets with migrated addresses
   correctly.  As it proposes a structured connection ID format, it also
   provides a means of connection IDs self-encoding their length to aid
   some hardware offloads.
- **draft-ietf-radext-connectinfo-01** (new-draft, score 0, ignored_after_review) [radext]: [A syntax for the RADIUS Connect-Info attribute used in Wi-Fi networks](https://datatracker.ietf.org/doc/draft-ietf-radext-connectinfo/) — This document describes a syntax for the Connect-Info attribute used
   with the RADIUS protocol, enabling RADIUS clients to provide RADIUS
   servers information pertaining to a user's connection with an IEEE
   802.11 wireless network.
- **draft-ietf-regext-rdap-extensions-17** (new-draft, score 0, ignored_after_review) [regext]: [RDAP Extensions](https://datatracker.ietf.org/doc/draft-ietf-regext-rdap-extensions/) — This document describes and clarifies the usage of extensions in
   RDAP.
- **draft-ietf-roll-dis-modifications-03** (new-draft, score 0, ignored_after_review) [roll]: [RPL DIS Modifications and Use Cases](https://datatracker.ietf.org/doc/draft-ietf-roll-dis-modifications/) — This document updates the RPL routing protocol specification by
   defining new DODAG Information Solicitation (DIS) flags and options
   that enable a RPL node to exert finer control over how neighboring
   RPL routers respond to its DIO solicitations.  In addition, this
   document describes several use cases that motivate these DIS
   extensions and illustrate scenarios in which enhanced control of DIO
   responses improves network efficiency, responsiveness, and
   robustness.
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
- **draft-ietf-v6ops-6mops-11** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6-mostly Networks: Deployment and Operations Considerations](https://datatracker.ietf.org/doc/draft-ietf-v6ops-6mops/) — This document discusses a deployment scenario called "an IPv6-mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (e.g. local area network (LAN) etc).  This approach
   enables incremental transition from dual-stack to IPv6-only networks
   by allowing IPv6-capable devices to remain IPv6-only while the
   network is seamlessly supplying IPv4 addresses to those devices that
   require them.  This document discusses the requirements,
   recommendations, and challenges associated with deploying IPv6-mostly
   networks in enterprise and public Wi-Fi environments.
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
- **draft-ietf-v6ops-prefix-to-end-sites-01** (new-draft, score 0, ignored_after_review) [v6ops]: [IPv6 Prefix Assignment to End-Sites](https://datatracker.ietf.org/doc/draft-ietf-v6ops-prefix-to-end-sites/) — This document describes different alternatives and best current
   practices for assignment of IPv6 prefixes for end-sites in broadband
   networks, including considerations about point-to-point links, their
   size, numbering choices, pool choices, customer prefix assignment
   size and persistence of those assignments.
- **draft-illyes-repext-04** (new-draft, score 0, ignored_after_review) [none]: [Robots Exclusion Protocol Extension for URL Level Control](https://datatracker.ietf.org/doc/draft-illyes-repext/) — This document extends RFC9309 by specifying additional URL level
   controls through an HTTP response header and, for historical reasons,
   through HTML meta tags originally developed in 1996.  Additionally it
   moves the HTTP response header out of the experimental header space
   (i.e., "X-") and defines the combinability of multiple headers, which
   was previously not possible.
- **draft-illyes-webbotauth-cbcp-01** (new-draft, score 0, ignored_after_review) [none]: [Crawler best practices](https://datatracker.ietf.org/doc/draft-illyes-webbotauth-cbcp/) — This document describes best practices for web crawlers.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/garyillyes/cbcp.
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
- **draft-kalosha-stb-tls13-01** (new-draft, score 0, ignored_after_review) [none]: [STB Cryptographic Parameters for Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/draft-kalosha-stb-tls13/) — This specification introduces a subset of STB (STandards of Belarus)
   cryptographic algorithms and defines their use in TLS 1.3.  The
   document is self-contained, i.e., it fully describes the required STB
   algorithms.  It can be used to develop STB-compliant TLS 1.3
   implementations without referring to the original STB standards.
- **draft-kamienski-iot-deployment-00** (new-draft, score 0, ignored_after_review) [none]: [Application-Centric Considerations for Deployment over the IoT Computing Continuum](https://datatracker.ietf.org/doc/draft-kamienski-iot-deployment/) — Smart applications increasingly depend on the Internet of Things
   (IoT) and distributed computing environments spanning constrained
   devices, edge nodes, cloudlets, and cloud infrastructure,
   collectively known as the edge–cloud, or computing continuum.  This
   document uses the term IoT computing continuum to highlight the
   importance of IoT-specific constraints and requirements within this
   broader context.  Although prior work has addressed communication
   aspects and edge functions in these environments, as noted in RFC
   9556 and comprehensive surveys of the computing continuum, there has
   been comparatively less focus on application-centric issues such as
   deployment, placement, and lifecycle management.  This document
   identifies key challenges and conceptual considerations for deploying
   smart applications across the IoT computing continuum, aiming to
   provide a unified architectural perspective and vocabulary to guide
   ongoing research within the IRTF and inform future standardization
   initiatives.
- **draft-karstens-pim-multicast-snooping-optimization-03** (new-draft, score 0, ignored_after_review) [none]: [Multicast Snooping Optimizations](https://datatracker.ietf.org/doc/draft-karstens-pim-multicast-snooping-optimization/) — TODO: provide abstract
- **draft-kejriwal-scone-scone-qlog-00** (new-draft, score 0, ignored_after_review) [none]: [QUIC Logging for the SCONE Protocol](https://datatracker.ietf.org/doc/draft-kejriwal-scone-scone-qlog/) — This document defines qlog events for the Standard Communication with
   Network Elements (SCONE) protocol.  The events record the sending and
   reception of SCONE packets and changes to throughput advice.
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
- **draft-limarsjenwar-tiptop-address-space-01** (new-draft, score 0, ignored_after_review) [none]: [IPv6 Address Space for Space](https://datatracker.ietf.org/doc/draft-limarsjenwar-tiptop-address-space/) — Without a structured address allocation plan, early space missions
   risk creating an unaggregated patchwork of prefixes, repeating the
   historical operational scaling issues seen in terrestrial networks.

   This document requests that the IANA allocate address space
   specifically for use in space environments and manages suballocations
   from that block for and within celestial bodies, as needed.  The
   Number Resource Organization (NRO) will determine how to allocate and
   assign address resources for and within the celestial bodies , with
   the understanding that topological address aggregation is critical
   for routing scalability and operational efficiency.
- **draft-liu-idr-bgp-sr-policy-cp-threshold-03** (new-draft, score 0, ignored_after_review) [none]: [BGP Extension for Distributing CP Threshold Constraints of SR Policy](https://datatracker.ietf.org/doc/draft-liu-idr-bgp-sr-policy-cp-threshold/) — This document defines the extension of BGP to distribute the
   threshold constraint parameters of candidate paths for SR Policy to
   achieve flexible path selection.
- **draft-liu-ippm-measurement-interpretation-00** (new-draft, score 0, ignored_after_review) [none]: [Considerations for Interpreting IP Performance Measurement Results](https://datatracker.ietf.org/doc/draft-liu-ippm-measurement-interpretation/) — IP Performance Measurement (IPPM) metrics characterize properties
   such as connectivity, packet loss, delay, delay variation, packet
   reordering, packet duplication, and capacity.  A result can be
   correct for the metric and measurement method used while still being
   insufficient to explain the network condition that produced it or to
   describe traffic outside the measured scope.

   This document provides guidance for interpreting IPPM measurement
   results.  It considers the metric definition and parameters, the
   measured packet or traffic population, the observation scope, and the
   measurement method.  It also discusses metric-specific considerations
   and differences among active, passive, and hybrid measurements.
   Operational information can support an interpretation, but this
   document keeps it separate from the metric result itself.

   This document does not define new metrics or measurement protocols,
   and it does not specify a mechanism for determining a unique
   operational cause.
- **draft-liu-satellite-internet-standardization-00** (new-draft, score 0, ignored_after_review) [none]: [Security Architecture of Satellite Internet](https://datatracker.ietf.org/doc/draft-liu-satellite-internet-standardization/) — In the 6G era of striving for global connectivity, Satellite Internet
   emerges as a crucial infrastructure by providing network coverage to
   remote and underserved regions.  However, it confronts more intricate
   security threats than terrestrial networks, encompassing dual perils
   from the physical and network realms.  This document reviews the
   classic architectures of Satellite Internet and dissects the novel
   security challenges it encounters, such as the harsh space
   environment, orbit and spectrum congestion, and the resource
   disparity between satellites and ground nodes.  It further
   scrutinizes the existing cybersecurity regulations and standards,
   highlighting their inadequacies in tackling these emerging threats.
   Against this backdrop, this document proposes a security architecture
   standard for Satellite Internet, which encompasses physical
   environment security and communication network security, with a focus
   on security technologies in the electromagnetic, control, and
   forwarding domains.  Finally, the document outlines the future trend
   of standardization efforts for Satellite Internet, underlining the
   necessity of bolstering active security technologies to counteract
   unknown intelligent security risks.
- **draft-liu-sidrops-ipfix-bgp-pov-01** (new-draft, score 0, ignored_after_review) [none]: [Export of BGP Prefix Origin Validation in IP Flow Information Export (IPFIX)](https://datatracker.ietf.org/doc/draft-liu-sidrops-ipfix-bgp-pov/) — This document defines an IP Flow Information Export (IPFIX)
   Information Element for monitoring the state of Resource Public Key
   Infrastructure (RPKI) based BGP Prefix Origin Validation.  The
   Information Element enables network operators to collect and analyze
   BGP route validation states (valid, invalid, not-found) to facilitate
   the detection of route origin hijacks and improve network
   observability and security.
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
- **draft-lqg-fann-multi-plane-protection-00** (new-draft, score 0, ignored_after_review) [none]: [Fast Network Notification for Plane Protection in Multi-Plane Networks](https://datatracker.ietf.org/doc/draft-lqg-fann-multi-plane-protection/) — This document discusses the use of fast network notifications for
   plane evacuation in multi-plane networks.
- **draft-mauch-bgp-nh-mtu-00** (new-draft, score 0, ignored_after_review) [none]: [BGP Next Hop MTU Attribute](https://datatracker.ietf.org/doc/draft-mauch-bgp-nh-mtu/) — This document defines NEXT_HOP_MTU, an optional non-transitive BGP
   path attribute (type code TBD).  It carries the IP MTU a speaker
   promises is acceptable for an NLRI across one network boundary.  The
   speaker that receives the NLRI across that boundary may attach the
   attribute from the boundary interface MTU and advertise it on
   internal and external sessions.  The intent is to communicate network
   MTU capability so that devices can use that information to improve
   the efficiency of their communications.
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
- **draft-nishida-ccwg-standard-cc-analysis-02** (new-draft, score 0, ignored_after_review) [none]: [Analysis for the Differences Between Standard Congestion Control Schemes](https://datatracker.ietf.org/doc/draft-nishida-ccwg-standard-cc-analysis/) — The IETF currently has three Standards Track specifications of loss-
   based congestion control: Reno-based congestion control for TCP (RFC
   5681), its counterpart for QUIC (RFC 9002), and CUBIC (RFC 9438),
   which updates RFC 5681.  They are intended to follow the same
   congestion control principles, but they differ in their mechanisms,
   parameters, and normative requirements, and these differences have
   not been reconciled with each other.  This document identifies such
   differences, summarizes whether and how each of them is documented in
   the specifications, and asks the IETF to determine for each
   difference whether to work toward convergence or accept it as is.
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
- **draft-pitta-portoles-lisp-evpn-interconnect-00** (new-draft, score 0, ignored_after_review) [none]: [Decoupled Interconnection of LISP and EVPN VXLAN Domains](https://datatracker.ietf.org/doc/draft-pitta-portoles-lisp-evpn-interconnect/) — This document describes decoupled Layer 2 and Layer 3 interconnection
   services between a LISP-based VXLAN domain and a BGP EVPN-based VXLAN
   domain.  The LISP-facing border and EVPN Gateway are implemented on
   separate devices.  The Layer 2 service extends a bridge domain
   through an Ethernet handoff, with independent MAC reachability and
   broadcast, unknown-unicast, and multicast forwarding in each overlay.
   The Layer 3 service uses tenant IP transit and prefix exchange
   through an Interior Gateway Protocol (IGP) or eBGP, with ordinary
   route redistribution at each border between the transit and its own
   overlay control plane.  IP subnet layouts are deployment
   considerations; they do not define the service.  Subnet-prefix
   exchange and additional requirements for optional routed connectivity
   within a common IP prefix are discussed.
- **draft-pospichal-idr-bgp-l2-quic-00** (new-draft, score 0, ignored_after_review) [none]: [Border Gateway Protocol over Layer 2 QUIC Transport (BoL2Q)](https://datatracker.ietf.org/doc/draft-pospichal-idr-bgp-l2-quic/) — This document specifies BGP over Layer 2 QUIC (BoL2Q), a transport
   for external and internal BGP sessions between speakers that share an
   Ethernet segment, in which QUIC packets are carried directly in
   Ethernet frames, identified by a dedicated EtherType, without IP or
   UDP headers.  A BoL2Q session has no IP address and no transport
   port, so it cannot be reached from beyond the link on which it runs,
   and it requires no IP-layer configuration of any kind: a session is
   defined by a local interface, the MAC address of the peer, the remote
   Autonomous System number and a pre-shared key.  BoL2Q reuses QUIC
   version 1 and TLS 1.3 unchanged, apart from the replacement of the
   UDP/IP path by an Ethernet path.  Optionally, a "Link Next Hop"
   capability allows routes to be installed with a router on the same
   Ethernet segment as the next hop, identified either as the session
   peer itself or by its MAC address.  This enables forwarding over
   links that carry no interface addresses, including through route
   reflectors and route servers.
- **draft-reddy-ipsecme-ikev2-hqc-00** (new-draft, score 0, ignored_after_review) [none]: [Post-Quantum Key Exchange with HQC in the Internet Key Exchange Protocol Version 2 (IKEv2)](https://datatracker.ietf.org/doc/draft-reddy-ipsecme-ikev2-hqc/) — This document specifies how to use Hamming Quasi-Cyclic (HQC), a
   code-based Key Encapsulation Mechanism (KEM), in the Internet Key
   Exchange Protocol Version 2 (IKEv2).  HQC can be used alone or
   together with other key exchanges to derive IKE and Child SA keys
   that resist attacks by quantum computers.  This document registers
   three Key Exchange Method identifiers.
- **draft-richardson-lamps-rfc7030bis-00** (new-draft, score 0, ignored_after_review) [none]: [Enrollment over Secure Transport](https://datatracker.ietf.org/doc/draft-richardson-lamps-rfc7030bis/) — This document profiles certificate enrollment for clients using
   Certificate Management over CMS (CMC) messages over a secure
   transport.  This profile, called Enrollment over Secure Transport
   (EST), describes a simple, yet functional, certificate management
   protocol targeting Public Key Infrastructure (PKI) clients that need
   to acquire client certificates and associated Certification Authority
   (CA) certificates.  It also supports client-generated public/private
   key pairs as well as key pairs generated by the CA.
- **draft-rosomakho-idr-bgp-masque-tunnel-01** (new-draft, score 0, ignored_after_review) [none]: [BGP Signaling of MASQUE Tunnel Encapsulation](https://datatracker.ietf.org/doc/draft-rosomakho-idr-bgp-masque-tunnel/) — This document defines BGP Tunnel Encapsulation Attribute tunnel types
   for MASQUE CONNECT-TCP, CONNECT-UDP, CONNECT-IP, and CONNECT-
   ETHERNET.  It also defines URI Template and SVCB Parameters Sub-TLVs
   for advertising the MASQUE proxy endpoint, the HTTP request target
   template, and extensible connection parameters used to establish the
   corresponding MASQUE tunnel.
- **draft-seemann-tsvwg-udp-fragmentation-03** (new-draft, score 0, ignored_after_review) [none]: [Controlling IP Fragmentation on Common Platforms](https://datatracker.ietf.org/doc/draft-seemann-tsvwg-udp-fragmentation/) — When performing Path MTU Discovery (PMTUD) over UDP, applications
   must prevent fragmentation of UDP datagrams both by the sender's
   kernel and during network transit.  This document provides guidance
   for implementers on configuring socket options to prevent
   fragmentation of IPv4 and IPv6 packets across commonly used
   platforms.
- **draft-sergeev-wexp-coverage-00** (new-draft, score 0, ignored_after_review) [none]: [WEXP Coverage: Claims, Evidence, and Evaluation](https://datatracker.ietf.org/doc/draft-sergeev-wexp-coverage/) — An authentic receipt for an action does not establish that every
   action in a declared scope has a receipt.  This document specifies a
   carrier-neutral contract for evaluating and reporting bounded claims
   about action-record creation, delivery, source coverage, supplied-
   record correspondence, and the absence of actions.  Results identify
   the exact scope and cutoffs of each claim, its supporting evidence,
   accepted assumptions, counterexamples, and unresolved conditions.
   The document defines inference and reporting requirements,
   requirements for deployment bindings, and a concrete deployment
   profile.  Coverage results are separate from Witnessed Execution
   Protocol (WEXP) Core appraisals and do not change their semantics.
- **draft-smith-6man-anycast-local-sock-opt-01** (new-draft, score 0, ignored_after_review) [none]: [An IPV6_ANYCAST_LOCAL Socket Option](https://datatracker.ietf.org/doc/draft-smith-6man-anycast-local-sock-opt/) — IPv6 nodes will deliver packets destined to an anycast address to one
   of their own local instances of the anycast address should they
   exist.  There are cases where it could be useful for a node to ignore
   its own anycast address instances and to submit packets towards this
   anycast address to the network for delivery to another node holding
   the anycast address.  This memo describes a Sockets API socket option
   to specify this behaviour.
- **draft-song-broadband-ancp-tsf-00** (new-draft, score 0, ignored_after_review) [none]: [TSF Extensions to ANCP in CU Separation Broadband Networks](https://datatracker.ietf.org/doc/draft-song-broadband-ancp-tsf/) — This document specifies a Traffic Steering Function (TSF) capability
   extension to the Access Node Control Protocol (ANCP), to discover and
   manage disaggregated user-plane (UP) functions in control/user plane
   separated networks, including the Access Network User Plane (AN-UP)
   and the Network Access Server User Plane (NAS-UP).
- **draft-soulard-anima-grasp-router-problem-statement-02** (new-draft, score 0, ignored_after_review) [none]: [GRASP through routers: a Problem Statement](https://datatracker.ietf.org/doc/draft-soulard-anima-grasp-router-problem-statement/) — This document analyzes challenges for using the GeneRic Autonomic
   Signaling Protocol (GRASP) in the context of deployment of services
   on machines (servers, Virtual Machines, etc) without the network
   elements, such as routers, needing any support for GRASP by
   themselves.  It analyses issues regarding the discovery mechanism,
   including discovery across subnets and operation across
   administrative boundaries, and provides terminology and general
   considerations for the development of future extensions, profiles,
   and architectural refinements.
- **draft-sullivan-tls-xof-schedule-01** (new-draft, score 0, ignored_after_review) [none]: [XOF-based key schedules for TLS 1.3](https://datatracker.ietf.org/doc/draft-sullivan-tls-xof-schedule/) — TLS 1.3 runs its entire key schedule on HKDF over SHA-2.  This
   document defines an extension that replaces that schedule with one
   built on an extendable-output function (XOF): the negotiated KDF
   governs every derivation, the Finished and binder MACs, and the
   transcript hash, so no SHA-2 remains in the key schedule.  The cipher
   suites, AEAD algorithms, state machine, and record layer are
   unchanged, and a connection without the extension uses HKDF as today.
   Two KDFs are defined, SHAKE256 and the reduced-round TurboSHAKE256.
   This document updates RFC 9147, RFC 9258, RFC 9261, and RFC 9849.
- **draft-taylor-dtn-dpp-02** (new-draft, score 0, ignored_after_review) [none]: [DTN Peering Protocol](https://datatracker.ietf.org/doc/draft-taylor-dtn-dpp/) — This document specifies the DTN Peering Protocol (DPP), an inter-
   domain routing protocol for the Delay-Tolerant Networking (DTN)
   ecosystem.  DPP facilitates the exchange of reachability information
   between distinct Administrative Domains (ADs), enabling inter-domain
   routing across networks operated by different agencies and
   organizations.  DPP separates the control plane from the data plane:
   a DPP speaker need not be a gateway that forwards bundles, allowing
   centralized route controllers or orchestration systems to participate
   in peering on behalf of the gateways they manage.

   DPP advertises the reachability of bundle nodes in both DTN
   addressing schemes, ipn (integer-based) and dtn (name-based), and
   selects routes for both by the same process.  DPP speakers
   authenticate each other using mutual TLS, with each Administrative
   Domain authorizing its speakers' keys through DNSSEC-signed TLSA
   records.  DPP supports both persistent routes and routes tied to the
   scheduled contact windows of deep-space networks.
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
- **draft-wang-ippm-ipv6-distributed-flow-measurement-07** (new-draft, score 0, ignored_after_review) [none]: [Distributed Flow Measurement in IPv6](https://datatracker.ietf.org/doc/draft-wang-ippm-ipv6-distributed-flow-measurement/) — In IPv6 networks, performance measurements such as packet loss,
   delay and jitter of real traffic can be carried out based on the
   Alternate-Marking method. Usually, the controller needs to collect
   statistical data on network devices, calculate and present the
   measurement results. This document proposes a distributed method for
   on-path flow measurement, which is independent of the controller.
- **draft-wang-ippm-ipv6-flow-measurement-11** (new-draft, score 0, ignored_after_review) [none]: [Flow Measurement in IPv6 Network](https://datatracker.ietf.org/doc/draft-wang-ippm-ipv6-flow-measurement/) — This document describes how to deploy in-situ flow performance
   measurement based on Alternate-Marking method in IPv6 domain.
- **draft-watts-eqr-conformance-03** (new-draft, score 0, ignored_after_review) [none]: [Deterministic Conformance Profile and Test Vectors for Evidence Qualification Receipts](https://datatracker.ietf.org/doc/draft-watts-eqr-conformance/) — This document defines a deterministic conformance profile and test-
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
- **draft-zhangb-cats-centralized-control-plane-01** (new-draft, score 0, ignored_after_review) [none]: [A Centralized Control Plane for Computing-Aware Traffic Steering](https://datatracker.ietf.org/doc/draft-zhangb-cats-centralized-control-plane/) — This document specifies a centralized control-plane realization of
   Computing-Aware Traffic Steering (CATS).  The realization uses a
   logically centralized CATS Path Selector (C-PS) together with ingress
   and egress CATS-Forwarders.  The C-PS receives a service request from
   an ingress CATS-Forwarder, resolves the requested service to an
   eligible service contact instance using computing service and network
   information, and then invokes a path-computation function for the
   selected destination.  The path-computation request contains a
   resolved headend, endpoint, and network constraints; it does not ask
   the PCE to discover service instances.

   After path computation, the C-PS returns a steering binding to the
   ingress CATS-Forwarder.  The binding identifies the selected
   destination address, the egress CATS-Forwarder, and a realizable path
   or policy.  The ingress forwarder applies the destination replacement
   and path encapsulation to the first packet and forwards it.  The
   egress forwarder removes the path encapsulation and delivers the
   packet to the selected service contact instance.  Subsequent packets
   use the installed flow binding, and reverse traffic uses the
   corresponding return binding.
- **draft-zhuang-grow-bmp-enhancement-for-vrf-loc-rib-02** (new-draft, score 0, ignored_after_review) [none]: [Enhancement for Monitoring VRF's Loc-RIB](https://datatracker.ietf.org/doc/draft-zhuang-grow-bmp-enhancement-for-vrf-loc-rib/) — BMP Loc-RIB [RFC9069] enforces that the BMP router sets the Peer
   Address value of a VPN route information to zero, and sets the Peer
   Distinguisher value of a VPN route information to the route
   distinguisher or unique locally defined value of the particular
   instance the Loc-RIB belongs to.  This document introduces the option
   to communicate the Remote VRF Information from which a VPN route was
   received when reporting that VPN route information with BMP Loc-RIB.
- **draft-zzd-idr-flowspec-scheduling-05** (new-draft, score 0, ignored_after_review) [idr]: [BGP Flow Specification Extensions for Scheduling](https://datatracker.ietf.org/doc/draft-zzd-idr-flowspec-scheduling/) — BGP Flow Specification allows conveying flow specifications and
   associated traffic actions/rules to perform different actions based
   on traffic characteristics.  Existing traffic filter rules and
   actions in FSv2 remain effective perpetually; once delivered to the
   headend, the rules and actions are permanent for traffic.  However,
   some operators wish to perform different actions for specific flows
   at specific time.

   This document extends BGP FSv2 with a scheduling time component to
   match the arrival time of packets.  Based on this component, the
   headend can perform different actions for specific traffic at
   different times.

## Errors / fetch failures

_None._
