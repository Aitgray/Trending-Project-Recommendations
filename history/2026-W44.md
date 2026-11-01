# Trending Project Ideas

**Week of 2026-10-25** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> Self-hosted media and data systems emerge as a cohesive new theme, driven by Immich's sustained trending and complemented by privacy-focused alternatives like RustDesk and Joplin. Rust-native performance tools have expanded significantly beyond async runtimes to encompass entire ecosystems (Bun, Ruff, Lance), reflecting growing adoption of Rust for end-user tooling rather than infrastructure alone. Security scanning persists but shifts focus toward supply-chain visibility (SBOM, credential verification) over point-in-time vulnerability detection. AI/ML infrastructure consolidates around foundation model training and symbolic reasoning rather than application-level inference frameworks, signaling enterprise maturation.

---

## Trending Topics


### Self-hosted media and data systems

Open-source alternatives for photo/video management, note-taking, and remote access that prioritize privacy and local-first architectures. Emphasis on high-performance storage, sync strategies, and decentralized protocols.

<details>
<summary>Supporting repos (3)</summary>


- [immich-app/immich](https://github.com/immich-app/immich)

- [laurent22/joplin](https://github.com/laurent22/joplin)

- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)


</details>


### Rust-native performance tools

High-performance systems software prioritizing speed, correctness, and ergonomic APIs. Covers binary-level instrumentation, search engines, data formats, and runtime observability without sacrificing safety.

<details>
<summary>Supporting repos (7)</summary>


- [oven-sh/bun](https://github.com/oven-sh/bun)

- [sharkdp/fd](https://github.com/sharkdp/fd)

- [tokio-rs/tokio](https://github.com/tokio-rs/tokio)

- [lance-format/lance](https://github.com/lance-format/lance)

- [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

- [astral-sh/ruff](https://github.com/astral-sh/ruff)

- [helix-editor/helix](https://github.com/helix-editor/helix)


</details>


### Security and vulnerability intelligence

Tools for scanning containers, code, and binaries for vulnerabilities, misconfigurations, and secrets with emphasis on supply-chain visibility and automated remediation. Includes SBOM generation and credential verification.

<details>
<summary>Supporting repos (5)</summary>


- [aquasecurity/trivy](https://github.com/aquasecurity/trivy)

- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)

- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)

- [anchore/syft](https://github.com/anchore/syft)

- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)


</details>


### AI and ML infrastructure

Foundational frameworks and tools for training, deploying, and reasoning with large language and multimodal models. Focus on scalability, symbolic reasoning, and production-grade distributed systems.

<details>
<summary>Supporting repos (3)</summary>


- [huggingface/transformers](https://github.com/huggingface/transformers)

- [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)

- [astroautomata/PySR](https://github.com/astroautomata/PySR)


</details>


### Developer tooling and platforms

Modern build systems, deployment platforms, and infrastructure-as-code solutions enabling rapid iteration and multi-cloud orchestration. Includes package managers, HTTP servers, and headless CMS backends.

<details>
<summary>Supporting repos (5)</summary>


- [vitejs/vite](https://github.com/vitejs/vite)

- [coollabsio/coolify](https://github.com/coollabsio/coolify)

- [caddyserver/caddy](https://github.com/caddyserver/caddy)

- [directus/directus](https://github.com/directus/directus)

- [encoredev/encore](https://github.com/encoredev/encore)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Self-hosted media and data systems


##### Immich Plugin Marketplace and Performance Registry

Build a TypeScript service that indexes, catalogs, and benchmarks Immich plugins (storage backends, sync protocols, thumbnail generators). Create a searchable registry with performance metrics (thumbnail generation time, memory footprint, sync latency), community ratings, and compatibility matrices across Immich versions. Expose via REST API and static HTML marketplace.

**Why now:** Self-hosted media systems are trending; users need transparent performance data to choose plugins without trial-and-error or vendor lock-in.

**Stack hints:** `TypeScript`, `Express`, `SQLite`, `GitHub API`, `Chart.js`






#### Rust-native performance tools


##### Rust CLI Tool Benchmarking Dashboard

Create a Bash + Rust harness that benchmarks Rust CLI tools (fd, ruff, ripgrep) against their predecessors and alternatives on standard workloads, capturing runtime, memory, and latency percentiles. Generate a simple HTML dashboard with comparison tables, export results as JSON for CI/CD integration.

**Why now:** Rust-native tools are trending; developers making tool-chain migrations need objective performance data to justify adoption.

**Stack hints:** `Rust`, `bash`, `hyperfine`, `serde`, `handlebars`






#### Security and vulnerability intelligence


##### Supply Chain CVE Impact Simulator

Write a Python CLI that ingests Syft SBOM output, correlates with Trivy CVE results, and simulates the impact of each CVE on your deployment (e.g., 'if this service is exposed to the internet, this CVE is exploitable'). Generate a risk matrix with severity vs. exploitability and export recommendations.

**Why now:** Security scanning is trending; teams drown in vulnerability alerts and need contextual prioritization to focus on exploitable issues.

**Stack hints:** `Python`, `click`, `requests`, `SQLite`, `semver`






#### AI and ML infrastructure


##### LLM Fine-Tuning Cost and Performance Trade-Off Calculator

Build a TypeScript tool that accepts model size, dataset size, and target accuracy metrics, then predicts fine-tuning cost (compute hours, GPU rental), training time, and inference latency. Compare strategies (LoRA vs. full fine-tune vs. in-context learning) and generate a Pareto frontier visualization.

**Why now:** AI/ML infrastructure is trending; practitioners need decision support to choose between expensive full training and cheaper in-context alternatives.

**Stack hints:** `TypeScript`, `Node.js`, `plotly.js`, `axios`






#### Developer tooling and platforms


##### Developer Platform Deployment Manifest Generator

Create a Go CLI that scaffolds deployment manifests (Docker Compose, Kubernetes YAML, Terraform) from declarative YAML describing services, databases, environment variables, and networking. Support Coolify, Directus, and other self-hosted platforms as opinionated templates.

**Why now:** Developer tooling platforms are trending; teams need faster onboarding without manual YAML authoring for multi-service deployments.

**Stack hints:** `Go`, `Cobra`, `yaml`, `text/template`





---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Self-hosted media and data systems


##### Self-Hosted Media Library Deduplication and Organization Engine

Build a TypeScript service (Node.js backend) that connects to Immich, analyzes photo/video metadata and perceptual hashes, detects duplicates and near-duplicates, suggests organized directory hierarchies based on EXIF and ML-extracted tags, and generates batch organization commands. Support dry-run previews and rollback.

**Why now:** Self-hosted media systems are trending; users accumulate chaotic photo libraries and need intelligent bulk organization tools.

**Stack hints:** `TypeScript`, `Node.js`, `sharp`, `phash`, `Express`, `SQLite`, `WebSocket`






#### Rust-native performance tools


##### Rust Async Runtime Profiler with Timeline Visualization

Build a Rust library that instruments Tokio tasks with proc-macros to capture task spawning, wake times, and executor queue depth. Generate interactive timeline visualizations (similar to Chrome DevTools traces) showing scheduler behavior, lock contention, and task scheduling anomalies. Export flamegraphs and JSON traces.

**Why now:** Rust-native tools are trending; developers tuning async workloads need visualization of scheduler behavior beyond wall-clock timing.

**Stack hints:** `Rust`, `tokio`, `proc-macro`, `tracing`, `pprof`, `serde`, `React`






#### Security and vulnerability intelligence


##### Automated Security Remediation Workflow Orchestrator

Build a TypeScript service that watches CI/CD for Trivy and TruffleHog findings, automatically creates remediation branches (dependency updates via Dependabot, secret rotations via Vault), re-scans to validate fixes, and opens PRs with audit trail annotations. Include dry-run mode and approval workflows for sensitive operations.

**Why now:** Security scanning is trending; manual remediation does not scale—automated orchestration with audit trails enables compliance without overhead.

**Stack hints:** `TypeScript`, `Node.js`, `GitHub API`, `Vault SDK`, `PostgreSQL`, `Express`, `Bull`






#### AI and ML infrastructure


##### Foundation Model Training Pipeline Coordinator

Build a Python/Rust service that orchestrates multi-GPU training workflows (using Megatron-LM patterns) across cloud providers, manages checkpointing and resumption, tracks training metrics and logs to observability backends, and exposes a dashboard for monitoring distributed training jobs. Support failure recovery and resource auto-scaling.

**Why now:** AI/ML infrastructure is trending; teams training foundation models need robust orchestration and observability without building from scratch.

**Stack hints:** `Python`, `Rust`, `PyTorch`, `Megatron-LM`, `Ray`, `PostgreSQL`, `OpenTelemetry`, `React`






#### Developer tooling and platforms


##### Multi-Cloud Infrastructure Deployment Validation Engine

Create a Go tool that accepts declarative infrastructure code (Terraform, Helm, Coolify manifests), simulates deployments across AWS, GCP, and Azure, detects misconfigurations, cost overruns, and compliance violations before applying changes. Generate before/after reports and automated fixes.

**Why now:** Developer platforms are trending; teams need pre-deployment validation to prevent costly mistakes and compliance breaches.

**Stack hints:** `Go`, `Terraform SDK`, `policy-as-code`, `PostgreSQL`, `React`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Self-hosted media and data systems


##### Privacy-Preserving Photo Sync Service with P2P and Self-Hosted Options

Develop a full-stack photo management service (Rust backend, TypeScript frontend) that integrates with Immich, enables P2P sync between user devices using Iroh, supports selective sharing without central cloud upload, runs face recognition and clustering locally via ONNX, and provides web access with end-to-end encryption. Support offline-first mobile clients with CRDT-based conflict resolution.

**Why now:** Self-hosted media systems are trending; photographers need privacy-respecting sync across devices and secure sharing without cloud intermediaries.

**Stack hints:** `Rust`, `TypeScript`, `Iroh`, `Tokio`, `ONNX`, `SQLite`, `React`, `Yrs`






#### Rust-native performance tools


##### Comprehensive Rust Ecosystem Performance Benchmarking Platform

Build a full-stack benchmarking platform (Rust backend, React frontend) that measures Rust libraries and tools against competitors across CPU, memory, latency, and power consumption. Support continuous benchmarking on each GitHub commit, trend analysis, regression detection, and export standard benchmark formats. Include integration with CI/CD pipelines.

**Why now:** Rust-native tools are trending; the ecosystem needs centralized, authoritative performance data to guide adoption and optimization.

**Stack hints:** `Rust`, `TypeScript`, `Criterion`, `tokio`, `PostgreSQL`, `React`, `GitHub API`, `D3.js`






#### Security and vulnerability intelligence


##### Supply Chain Integrity Verification and Attestation Platform

Develop a full-stack platform (Go backend, React frontend) that ingests SBOMs from Syft and Trivy results, correlates with binary provenance data, verifies cryptographic signatures and attestations, tracks dependency lineage over time, and generates compliance reports for audits. Support integration with signed artifact registries (Sigstore, cosign).

**Why now:** Security scanning is trending; enterprises need end-to-end supply chain visibility with cryptographic proof of integrity and provenance.

**Stack hints:** `Go`, `TypeScript`, `Sigstore`, `cosign`, `PostgreSQL`, `React`, `gRPC`, `D3.js`






#### AI and ML infrastructure


##### Distributed ML Training Orchestration and Cost Attribution System

Develop a production-grade system (Python/Rust backend, React frontend) that orchestrates distributed training jobs for foundation models using Megatron-LM, tracks resource utilization per job, attributes costs to teams/projects, predicts training time and cost before execution, and optimizes hyperparameters for cost efficiency. Support multi-cloud deployment and preemption-aware scheduling.

**Why now:** AI/ML infrastructure is trending; enterprises training foundation models need visibility into training costs and automated optimization to prevent runaway expenses.

**Stack hints:** `Python`, `Rust`, `PyTorch`, `Ray`, `Kubernetes`, `PostgreSQL`, `Prometheus`, `React`






#### Developer tooling and platforms


##### Universal Infrastructure-as-Code Testing and Validation Framework

Build a comprehensive framework (Go backend, TypeScript CLI and React dashboard) that validates infrastructure code (Terraform, Helm, Coolify manifests, Docker Compose) for security, performance, cost, and compliance. Support policy-as-code templates, pre-deployment simulation, cost estimation, and post-deployment assertion testing. Generate audit trails for compliance.

**Why now:** Developer platforms are trending; teams managing multi-cloud infrastructure need unified validation and compliance checking across different IaC tools.

**Stack hints:** `Go`, `TypeScript`, `Terraform SDK`, `policy-as-code`, `Kubernetes`, `PostgreSQL`, `React`, `OpenCost`





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

*Generated 2026-10-25 15:39 UTC · commit `9342900`*
