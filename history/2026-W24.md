# Trending Project Ideas

**Week of 2026-06-07** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> Workflow automation platforms (n8n, Plane, Airflow) have surged in persistence this week, consolidating around code-first, self-hostable orchestration—a shift from last week's focus on glue code integration toward full workflow ownership. Speech AI infrastructure remains production-grade and persistent, now competing directly with enterprise platforms for transcription and compliance use cases. Rust-native infrastructure has significantly expanded beyond the five repos of last week, now spanning editors, vector databases, and version control—indicating ecosystem maturation and broader adoption pressure. Educational platforms have stabilized as durable, with new emphasis on algorithmic thinking and system design alongside project-based learning. Security and compliance tooling has emerged as a sustained theme absent from last week, reflecting heightened enterprise focus on vulnerability management and secrets detection.

---

## Trending Topics


### Workflow automation platforms

Declarative, code-first workflow orchestration tools (n8n, Plane) that combine visual building with custom logic, emphasizing self-hosting, extensibility, and AI-native integration patterns.

<details>
<summary>Supporting repos (3)</summary>


- [n8n-io/n8n](https://github.com/n8n-io/n8n)

- [makeplane/plane](https://github.com/makeplane/plane)

- [apache/airflow](https://github.com/apache/airflow)


</details>


### Speech and audio AI infrastructure

Production-grade speech recognition, transcription, and diarization systems (FunASR, Whisper) that prioritize industrial reliability, multilingual support, and real-time performance at scale.

<details>
<summary>Supporting repos (3)</summary>


- [modelscope/FunASR](https://github.com/modelscope/FunASR)

- [openai/whisper](https://github.com/openai/whisper)

- [huggingface/transformers](https://github.com/huggingface/transformers)


</details>


### Rust-native infrastructure and developer tools

High-performance systems written in Rust spanning databases (Qdrant, Chroma), editors (Helix), version control (jj), and observability, driven by safety guarantees and performance requirements.

<details>
<summary>Supporting repos (5)</summary>


- [helix-editor/helix](https://github.com/helix-editor/helix)

- [qdrant/qdrant](https://github.com/qdrant/qdrant)

- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

- [jj-vcs/jj](https://github.com/jj-vcs/jj)

- [slint-ui/slint](https://github.com/slint-ui/slint)


</details>


### Educational learning systems and content scaffolding

Structured, project-based learning platforms (freeCodeCamp, Build Your Own X, system-design-primer) that emphasize hands-on skill building, reproducible progression, and community-driven curriculum.

<details>
<summary>Supporting repos (4)</summary>


- [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)

- [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)

- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

- [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)


</details>


### Security, vulnerability, and compliance scanning

Specialized tools for finding secrets, vulnerabilities, and misconfigurations (Trivy, TruffleHog, Nuclei) that integrate into CI/CD pipelines and emphasize comprehensive, automated compliance.

<details>
<summary>Supporting repos (3)</summary>


- [aquasecurity/trivy](https://github.com/aquasecurity/trivy)

- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)

- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Workflow automation platforms


##### Workflow Template Marketplace with AI-Assisted Configuration

Build a CLI tool that discovers n8n and Airflow workflow templates from GitHub, extracts configuration requirements via LLM analysis, and generates interactive prompts that auto-fill credentials and service bindings. Output ready-to-deploy workflow manifests.

**Why now:** Workflow automation adoption is accelerating; reducing template friction and configuration complexity lowers barrier to adopting platforms like n8n and Plane.

**Stack hints:** `Python`, `Click`, `Claude API`, `GitHub API`, `YAML`






#### Speech and audio AI infrastructure


##### Multi-Language Speech Labeling and Annotation Tool

Create a web UI that streams audio, uses FunASR for live transcription with confidence scores, and enables click-to-correct annotation for training data. Export labeled datasets with audio segments, timestamps, and corrections for fine-tuning speech models.

**Why now:** Speech AI quality is production-ready; teams need efficient tools to generate labeled training data and validate transcription accuracy for domain-specific models.

**Stack hints:** `Python`, `FastAPI`, `FunASR`, `Vue.js`, `librosa`, `SQLite`






#### Rust-native infrastructure and developer tools


##### Helix Plugin Registry and Package Manager

Design a Rust-native plugin registry and CLI installer for Helix editor, enabling one-command plugin discovery, installation, and updates. Include plugin templates for language servers, themes, and custom keybindings.

**Why now:** Helix adoption is growing; a centralized plugin ecosystem bridges the minimalism-extensibility gap and accelerates community contributions.

**Stack hints:** `Rust`, `tokio`, `serde_json`, `clap`, `reqwest`






#### Educational learning systems and content scaffolding


##### Interactive Algorithm Visualizer with Step-Through Debugger

Build a web tool that visualizes algorithm execution (sorting, graph traversal, dynamic programming) with step-through debugging, variable inspection, and time-complexity annotations. Support importing algorithms from JavaScript or Python, with sharable benchmark comparisons.

**Why now:** Algorithm learning platforms are durable; visual debugging significantly improves comprehension and retention for complex data structure concepts.

**Stack hints:** `TypeScript`, `React`, `D3.js`, `Pyodide`, `Esprima`






#### Security, vulnerability, and compliance scanning


##### SBOM-Driven Dependency Risk Dashboard

Create a dashboard that ingests SBOM files generated by Trivy, visualizes dependency graphs with vulnerability risk scoring, and recommends patch priorities based on exploit prevalence and transitive exposure.

**Why now:** Security scanning is now mainstream; teams need visual SBOM analysis and risk prioritization to make informed patching decisions at scale.

**Stack hints:** `TypeScript`, `React`, `D3.js`, `Express`, `SQLite`





---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Workflow automation platforms


##### Declarative Workflow Testing Framework

Design a testing framework for n8n and Airflow workflows that supports declarative test definitions (input fixtures, assertions, mocked service responses), generates test reports with coverage metrics, and integrates with CI/CD pipelines for continuous validation.

**Why now:** Workflow platforms are proliferating; robust testing infrastructure is critical to ensure reliability and prevent production data pipeline failures.

**Stack hints:** `TypeScript`, `Jest`, `Express`, `PostgreSQL`, `Docker`






#### Speech and audio AI infrastructure


##### Real-Time Speech Intelligence for Contact Centers

Build an end-to-end contact center analytics platform using FunASR for transcription, speaker diarization for multi-party detection, and NLP for sentiment and topic extraction. Expose REST API with real-time dashboards, compliance redaction, and searchable transcript indices.

**Why now:** Speech AI has reached production maturity; enterprises urgently need real-time insights from call recordings with built-in PII protection and compliance reporting.

**Stack hints:** `Python`, `FastAPI`, `FunASR`, `spaCy`, `Qdrant`, `PostgreSQL`, `Celery`, `React`






#### Rust-native infrastructure and developer tools


##### Rust-Native Edge Vector Database with Embedded ML

Develop a lightweight, embeddable Rust library for vector search optimized for edge deployment (mobile, wasm, embedded), supporting dynamic indexing, offline-first operation, and automatic sync when connectivity resumes.

**Why now:** Rust's performance and safety are ideal for edge infrastructure; Qdrant and Chroma are server-centric; edge-optimized alternatives unlock on-device ML inference and privacy-preserving search.

**Stack hints:** `Rust`, `tokio`, `Arrow`, `RocksDB`, `wasm-bindgen`






#### Educational learning systems and content scaffolding


##### Adaptive Skill Graph Learning Engine

Create a learning platform that models programming skills as a directed graph, adapts exercise difficulty and sequencing based on learner performance, integrates spaced repetition scheduling, and recommends personalized learning paths. Support importing external tutorials and peer skill validation.

**Why now:** Educational platforms are maturing; a unified skill graph that personalizes learning across multiple content sources creates scalable, adaptive education experiences.

**Stack hints:** `Python`, `FastAPI`, `PostgreSQL`, `React`, `D3.js`, `Redis`






#### Security, vulnerability, and compliance scanning


##### Container Supply Chain Security Attestation System

Build a system that generates cryptographic attestations for container builds using Trivy scans, tracks provenance across CI/CD pipelines, and validates artifact signatures at deployment time. Include policy enforcement and audit logging for compliance frameworks (SLSA, Supply Chain Levels for Software Artifacts).

**Why now:** Container security is critical; teams need verifiable provenance and signed attestations to satisfy compliance requirements and prevent supply chain attacks.

**Stack hints:** `Go`, `TypeScript`, `Sigstore`, `Docker`, `Kubernetes`, `PostgreSQL`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Workflow automation platforms


##### AI-Optimized Workflow Composition Engine

Design an intelligent workflow platform that translates natural language descriptions into executable workflows, auto-generates error handling and retry logic, and optimizes task parallelization using cost and latency models. Include visual workflow authoring, multi-cloud support, and compliance templating for HIPAA and GDPR.

**Why now:** Workflow automation is consolidating; a platform combining natural language composition, intelligent optimization, and compliance automation captures both developer and enterprise personas simultaneously.

**Stack hints:** `TypeScript`, `Python`, `FastAPI`, `PostgreSQL`, `Claude API`, `OpenAPI Parser`, `React`, `Kubernetes`






#### Speech and audio AI infrastructure


##### Distributed Multi-Modal Speech Intelligence Platform

Build a production-grade platform that processes speech, video, and text streams in parallel, performs cross-modal analysis (lip-sync verification, visual emotion correlation), detects deepfakes and synthetic speech, and generates compliance-ready transcripts with speaker profiling. Include Kubernetes operators for auto-scaling.

**Why now:** Speech AI is enterprise-ready; integrating multi-modal analysis, fraud detection, and compliance in a single distributed system addresses emerging security and authentication needs.

**Stack hints:** `Python`, `FastAPI`, `FunASR`, `OpenCV`, `ONNX`, `Kubernetes`, `PostgreSQL`, `Redis`, `Kafka`






#### Rust-native infrastructure and developer tools


##### Rust Systems Programming University with Job Placement

Create a comprehensive Rust systems programming curriculum with hands-on projects (build a kernel module, filesystem, database, network protocol). Include automated code review, mentorship matching, portfolio generation, and direct connections with Rust-native companies for hiring.

**Why now:** Rust adoption is accelerating in systems roles; a structured bootcamp with career outcomes addresses both the skill gap and hiring bottleneck for infrastructure roles.

**Stack hints:** `Rust`, `TypeScript`, `React`, `PostgreSQL`, `GitHub API`, `Docker`






#### Educational learning systems and content scaffolding


##### Personalized Learning Dashboard with Peer Collaboration

Develop a comprehensive learning platform that combines adaptive skill graphs, real-time collaborative coding environments, peer code review workflows, and mentor matching. Support multiple programming languages and domains, integrate with external tutorials and job boards, and track employment outcomes.

**Why now:** Educational platforms have proven durable and scalable; adding peer collaboration, mentorship, and career integration transforms learning into a community-driven, outcome-focused experience.

**Stack hints:** `TypeScript`, `Python`, `FastAPI`, `PostgreSQL`, `React`, `WebSocket`, `Docker`, `Redis`






#### Security, vulnerability, and compliance scanning


##### Enterprise Supply Chain Risk Intelligence Platform

Build a comprehensive platform that aggregates vulnerability data across Trivy, TruffleHog, and Nuclei scans, correlates risks across dependencies and transitive chains, predicts exploit probability using threat intelligence feeds, and generates automated remediation workflows. Include compliance reporting for SOC 2, HIPAA, and PCI-DSS.

**Why now:** Security scanning is now standard practice; enterprises need unified risk intelligence, predictive models, and automated remediation to manage complexity at scale.

**Stack hints:** `Python`, `FastAPI`, `PostgreSQL`, `React`, `Kafka`, `Elasticsearch`, `Kubernetes`





---

## Methodology

This README is automatically regenerated each Sunday using a 7-day rolling aggregate
of [GitHub's trending page](https://github.com/trending?spoken_language_code=en).
Repos are scored by *persistence* — how many days they appeared in the window,
weighted by cumulative stars — to filter out one-day viral spikes. The top 40 repos
are passed to an LLM, which identifies 3–5 durable themes and proposes 9–15 original
project ideas across short, medium, and long scope tiers.
See [ABOUT.md](ABOUT.md) for full methodology details.

---

*Generated 2026-06-07 13:53 UTC · commit `e08d601`*
