# Trending Project Ideas

**Week of 2026-10-18** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> Workflow automation and orchestration has solidified as the dominant theme with n8n maintaining peak engagement, reflecting enterprise adoption of decentralized execution patterns. Reverse engineering and security scanning remain high-velocity but now emphasize supply-chain and CVE remediation rather than forensic analysis alone. Rust systems tooling persists with new emphasis on data lakehouse formats (Lance) and distributed search, moving beyond traditional infrastructure. Self-hosted privacy-first platforms show renewed momentum alongside emerging interest in knowledge workspaces (Siyuan) and governance platforms (Bytebase).

---

## Trending Topics


### Workflow automation and orchestration

Low-code platforms and distributed execution engines enabling scalable, self-hosted automation with native integrations. Focus on decentralization, cost control, and enterprise governance.

<details>
<summary>Supporting repos (3)</summary>


- [n8n-io/n8n](https://github.com/n8n-io/n8n)

- [makeplane/plane](https://github.com/makeplane/plane)

- [Infisical/infisical](https://github.com/Infisical/infisical)


</details>


### Reverse engineering and security scanning

Binary analysis, vulnerability detection, and secret scanning tools using fast native implementations. Emphasis on supply-chain security, CVE correlation, and automated remediation.

<details>
<summary>Supporting repos (3)</summary>


- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

- [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

- [aquasecurity/trivy](https://github.com/aquasecurity/trivy)


</details>


### Rust systems and data tools

Production-grade systems software and data processing engines prioritizing performance, safety, and ergonomic APIs. Includes async runtimes, search engines, and specialized infrastructure.

<details>
<summary>Supporting repos (3)</summary>


- [tokio-rs/tokio](https://github.com/tokio-rs/tokio)

- [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

- [lance-format/lance](https://github.com/lance-format/lance)


</details>


### Self-hosted and privacy-first platforms

Open-source alternatives to SaaS with focus on data sovereignty, local-first processing, and decentralized access. Targeting document management, networking, and personal data.

<details>
<summary>Supporting repos (3)</summary>


- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

- [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

- [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan)


</details>


### Web and fullstack frameworks

Modern UI and development frameworks emphasizing developer ergonomics, fast builds, and cross-platform deployment. Includes reactive component systems and rapid prototyping.

<details>
<summary>Supporting repos (3)</summary>


- [sveltejs/svelte](https://github.com/sveltejs/svelte)

- [vitejs/vite](https://github.com/vitejs/vite)

- [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Workflow automation and orchestration


##### Workflow Cost Attribution Engine

Build a TypeScript service that hooks into n8n webhook events, tracks CPU, memory, and third-party API costs per workflow execution, and exposes a simple dashboard showing cost breakdowns by team or department. Include budget alerts and cost forecasting.

**Why now:** Workflow automation platforms are trending; teams need cost visibility to prevent runaway infrastructure expenses without manual log analysis.

**Stack hints:** `TypeScript`, `Express`, `SQLite`, `Chart.js`, `node-cron`






#### Reverse engineering and security scanning


##### Supply Chain CVE Correlation and Patch Suggester

Write a Python CLI that ingests Trivy SBOM output, correlates detected CVEs with available patches across package registries, ranks patches by adoption rate and breaking-change risk, and generates prioritized remediation recommendations with estimated effort.

**Why now:** Security scanning is trending; teams face alert fatigue from fragmented vulnerability data—unified patch suggestions reduce triage overhead.

**Stack hints:** `Python`, `Trivy API`, `requests`, `SQLite`, `semver`, `click`






#### Rust systems and data tools


##### Rust Async Runtime Performance Profiler

Create a Rust proc-macro and instrumentation library that wraps async functions to capture task wake times, context switches, and lock contention. Generate flamegraphs and timeline visualizations showing Tokio scheduler behavior. Export metrics as JSON for CI integration.

**Why now:** Rust systems tooling is trending; developers tuning async workloads need visibility into scheduler behavior beyond wall-clock timing.

**Stack hints:** `Rust`, `tokio`, `proc-macro`, `pprof`, `serde_json`, `inferno`






#### Self-hosted and privacy-first platforms


##### Self-Hosted Document OCR and Knowledge Extraction Service

Write a Go service that watches a local directory for PDFs/images, runs OCR via Tesseract, extracts structured data (tables, key-value pairs) using local LLM inference, and indexes results into a searchable SQLite database exposed via REST. Deploy as single Docker container.

**Why now:** Self-hosted platforms are trending; organizations need privacy-respecting document processing without cloud upload or subscription.

**Stack hints:** `Go`, `Tesseract`, `Ollama`, `SQLite`, `fsnotify`, `Echo`






#### Web and fullstack frameworks


##### Svelte Component Snapshot Testing and Regression Detection

Create a TypeScript test utility that captures visual diffs of Svelte components across versions, generates baseline snapshots, and flags pixel-level regressions. Integrate with CI/CD pipelines and generate HTML reports with side-by-side comparisons.

**Why now:** Web frameworks are trending; component-driven development needs automated visual regression testing without heavy dependencies.

**Stack hints:** `TypeScript`, `Svelte`, `Vitest`, `Playwright`, `jimp`





---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Workflow automation and orchestration


##### GitOps-Powered Workflow Deployment CLI

Create a Go CLI that exports n8n workflows to version-controlled JSON, detects schema changes, applies Git-based workflows (PRs, approvals), and deploys changes to target environments with automatic rollback on validation failure. Support templating for multi-environment promotion.

**Why now:** Workflow automation is trending; teams need GitOps discipline and audit trails for workflow changes without manual YAML authoring.

**Stack hints:** `Go`, `GitHub API`, `JSON Schema`, `Cobra`, `Temporal`, `PostgreSQL`






#### Reverse engineering and security scanning


##### Automated Dependency Vulnerability Remediation Orchestrator

Build a TypeScript service that watches for Trivy/Gitleaks findings in CI/CD pipelines, automatically creates dependency update branches or rotates secrets via HashiCorp Vault, validates fixes with re-scanning, and opens PRs with audit trail annotations. Include dry-run mode and approval workflows.

**Why now:** Security scanning is trending; manual remediation does not scale—orchestrated fixes with audit trails enable compliance automation.

**Stack hints:** `TypeScript`, `Node.js`, `GitHub API`, `Vault SDK`, `PostgreSQL`, `Express`, `Jest`






#### Rust systems and data tools


##### Rust + Lance Vector Search Index Builder with Python Bindings

Build a Rust library that compiles high-dimensional vector indexing strategies (IVF, HNSW) to optimized CPU code using Lance, supports incremental index updates with versioning, and exposes Python bindings for seamless integration with ML workflows. Include cost modeling and index reconstruction hints.

**Why now:** Rust systems and data tools are trending; data scientists need fast, version-tracked vector indexes without manual algorithm selection.

**Stack hints:** `Rust`, `lance`, `arrow`, `pyo3`, `ndarray`, `rayon`






#### Self-hosted and privacy-first platforms


##### Self-Hosted Task Management with AI-Powered Scheduling

Build a TypeScript application (SvelteKit frontend, Node.js backend) that indexes personal tasks and calendar, runs local LLM inference to suggest optimal scheduling based on energy patterns and deadlines, and generates weekly plans with offline-first sync. Include collaborative features for households.

**Why now:** Self-hosted platforms are trending; users want productivity tools that learn personal patterns without sharing data with cloud services.

**Stack hints:** `TypeScript`, `SvelteKit`, `Node.js`, `Ollama`, `SQLite`, `CRDTs`, `WebSocket`






#### Web and fullstack frameworks


##### Vite Plugin Marketplace and Performance Analyzer

Build a TypeScript service that discovers, catalogs, and benchmarks Vite plugins against build time and bundle size metrics. Create a web interface to search plugins by use case, compare performance, and generate optimal plugin configurations for project types.

**Why now:** Web frameworks are trending; developers struggle to choose among hundreds of Vite plugins without performance data.

**Stack hints:** `TypeScript`, `Node.js`, `Vite`, `esbuild`, `React`, `SQLite`, `GitHub API`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Workflow automation and orchestration


##### Enterprise Workflow Catalog and Governance Platform

Develop a full-stack platform (Go backend, React frontend) that indexes n8n workflows, creates a searchable catalog with usage metrics and cost attribution, enforces approval gates and SLA policies, and tracks lineage and dependencies across workflow ecosystems. Support multi-tenant isolation and custom integrations.

**Why now:** Workflow automation is trending; enterprises need centralized governance and discovery to prevent duplicate workflows and enforce compliance.

**Stack hints:** `Go`, `TypeScript`, `PostgreSQL`, `React`, `GraphQL`, `Kubernetes`, `OpenCost`






#### Reverse engineering and security scanning


##### Binary Provenance Verification and Supply Chain Explorer

Develop a Rust backend with React frontend that ingests Ghidra analyses of production binaries, extracts function signatures and data flow graphs, correlates with known CVEs and malware signatures, visualizes supply chain dependencies, and tracks provenance changes over releases. Include collaborative threat modeling and export for audits.

**Why now:** Reverse engineering and security scanning are trending; enterprises need centralized binary visibility to prevent supply-chain attacks.

**Stack hints:** `Rust`, `TypeScript`, `Ghidra API`, `PostgreSQL`, `React`, `D3.js`, `WebSocket`






#### Rust systems and data tools


##### Distributed Systems Observability Platform with Rust and Lance

Develop a full-stack observability system (Rust collector, React frontend) that ingests distributed trace data into Lance for fast columnar storage and vector search, enables semantic span search via embeddings, and visualizes system topology with anomaly detection. Support cloud-agnostic deployment and cost attribution.

**Why now:** Rust systems and data tools are trending; teams need fast trace storage and semantic search without Elasticsearch/DataDog overhead.

**Stack hints:** `Rust`, `TypeScript`, `lance`, `arrow`, `tokio`, `React`, `Kubernetes`, `OpenTelemetry`






#### Self-hosted and privacy-first platforms


##### Decentralized Personal Knowledge Graph with P2P Sync

Develop a Rust backend with React frontend that stores personal knowledge as a graph database with P2P sync using Iroh, supports offline-first editing with CRDTs, runs local semantic search and entity linking via embeddings, and enables selective sharing with family/colleagues without centralized servers.

**Why now:** Self-hosted platforms are trending; users want knowledge tools that remain private yet enable selective collaboration across devices and people.

**Stack hints:** `Rust`, `TypeScript`, `Iroh`, `Yrs`, `Sled`, `React`, `WebAssembly`






#### Web and fullstack frameworks


##### Fullstack Reactive Data Binding Framework with Dioxus

Create a Rust framework that extends Dioxus with server-driven reactive data binding—components declare data dependencies, the framework automatically manages client-server sync with incremental updates, and generates type-safe TypeScript clients. Support offline-first with local cache invalidation.

**Why now:** Web and fullstack frameworks are trending; developers need seamless reactive data flow between Rust backends and UIs without manual API coordination.

**Stack hints:** `Rust`, `Dioxus`, `tokio`, `SQLx`, `TypeScript`, `CRDTs`, `WebSocket`





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

*Generated 2026-10-18 15:28 UTC · commit `87fd0c8`*
