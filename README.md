# Trending Project Ideas

**Week of 2026-10-11** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> Reverse engineering and security analysis tools have emerged as a distinct, high-velocity theme with Ghidra, Nuclei, and Trivy showing sustained engagement—a shift from last week's broader security focus toward specialized binary analysis. Rust systems tooling remains dominant and has expanded beyond traditional infra to include high-performance data engines (Polars) and language runtimes (Bun), reflecting accelerating adoption in data and DevOps workflows. UI frameworks (Svelte, Vue, egui) have consolidated as a persistent theme reflecting modern web component evolution. Self-hosted infrastructure (Immich, RustDesk, Tailscale) continues trending, now paired with workflow automation (n8n) as enterprises seek end-to-end SaaS-independent tooling.

---

## Trending Topics


### Reverse engineering and security analysis

Low-level tools for binary analysis, vulnerability scanning, and software forensics using fast, language-native implementations. Emphasis on automated detection, customizable rulesets, and actionable threat intelligence.

<details>
<summary>Supporting repos (3)</summary>


- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

- [aquasecurity/trivy](https://github.com/aquasecurity/trivy)


</details>


### Rust systems tooling and high-performance libraries

Performance-critical infrastructure written in Rust targeting speed, memory efficiency, and ergonomic developer APIs. Includes linkers, query engines, CLI tools, and async runtimes.

<details>
<summary>Supporting repos (5)</summary>


- [pola-rs/polars](https://github.com/pola-rs/polars)

- [rui314/mold](https://github.com/rui314/mold)

- [tokio-rs/tokio](https://github.com/tokio-rs/tokio)

- [astral-sh/ruff](https://github.com/astral-sh/ruff)

- [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine)


</details>


### UI and visualization frameworks for web and native

Immediate-mode and declarative UI systems enabling cross-platform interactive applications with modern rendering and state management. Focus on developer ergonomics and performance.

<details>
<summary>Supporting repos (3)</summary>


- [emilk/egui](https://github.com/emilk/egui)

- [sveltejs/svelte](https://github.com/sveltejs/svelte)

- [vuejs/core](https://github.com/vuejs/core)


</details>


### Self-hosted infrastructure and remote access

Privacy-respecting alternatives to SaaS platforms for media management, terminal access, and networking. Emphasize decentralization, data sovereignty, and self-deployment.

<details>
<summary>Supporting repos (3)</summary>


- [immich-app/immich](https://github.com/immich-app/immich)

- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

- [tailscale/tailscale](https://github.com/tailscale/tailscale)


</details>


### Workflow automation and orchestration

Low-code and visual platforms for building scalable, automated processes with native integrations and self-hosting support. Target business and technical users alike.

<details>
<summary>Supporting repos (2)</summary>


- [n8n-io/n8n](https://github.com/n8n-io/n8n)

- [oven-sh/bun](https://github.com/oven-sh/bun)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Reverse engineering and security analysis


##### Binary Diff Analyzer with MLIR-Based Patch Synthesis

Build a Rust CLI that takes two binaries, diffs their disassembly using Ghidra's headless API, highlights semantic changes, and generates a natural-language summary of functional delta. Use tree-sitter for syntax-aware comparison and export patches as annotated JSON.

**Why now:** Reverse engineering tools are trending; developers need fast, automated diffing to track malware mutations and supply-chain integrity without manual analysis.

**Stack hints:** `Rust`, `Ghidra Java bindings`, `tree-sitter`, `serde_json`, `clap`


##### Real-Time Vulnerability Risk Scorer

Write a Go service that consumes Nuclei scan results and Trivy SBOM data, correlates findings with CVSS scores and exploit availability, assigns composite risk scores by asset, and streams high-risk alerts via webhooks. Support policy-driven filtering and false-positive suppression.

**Why now:** Security scanning is trending; fragmented tool outputs create alert fatigue—unified risk scoring enables prioritized remediation.

**Stack hints:** `Go`, `gRPC`, `SQLite`, `NVD API client`, `websocket`






#### Rust systems tooling and high-performance libraries


##### Rust Systems Performance Benchmarking Suite

Create a Rust CLI that benchmarks system utilities (ls, find, grep alternatives) against their GNU counterparts using Hyperfine, captures memory profiles with pprof, and generates comparative reports with statistical significance testing. Output as HTML dashboards.

**Why now:** Rust tooling is trending; teams need quantitative data to justify migration from C utilities to Rust rewrites in production environments.

**Stack hints:** `Rust`, `hyperfine`, `pprof`, `statrs`, `tera`






#### UI and visualization frameworks for web and native


##### Interactive Web UI for Egui Components

Build a browser-based component gallery and live editor for Egui where developers can inspect, customize, and generate Rust code for common UI patterns (tables, forms, charts). Include hot-reload via WebSocket and export as boilerplate.

**Why now:** UI frameworks are trending; immediate-mode systems like Egui lack visual design tooling that web frameworks take for granted.

**Stack hints:** `Rust`, `egui`, `eframe`, `TypeScript`, `React`






#### Self-hosted infrastructure and remote access


##### Self-Hosted Terminal Session Recorder with AI Transcript

Build a lightweight Go agent that records terminal sessions (asciinema format), transcribes commands and output locally using Whisper.cpp, indexes them searchable by command or intent, and exposes a web UI for playback and search. Deploy as a single binary.

**Why now:** Self-hosted infrastructure is trending; teams need privacy-respecting audit trails for terminal access without cloud upload.

**Stack hints:** `Go`, `asciinema library`, `whisper.cpp`, `SQLite`, `htmx`








---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Reverse engineering and security analysis


##### Automated Vulnerability Remediation Orchestrator

Develop a Go/Rust service that ingests Trivy and Nuclei findings, orchestrates automated remediation via supply-chain APIs (bumping dependencies, patching configs, rotating secrets), validates fixes with re-scanning, and generates compliance audit trails. Include dry-run and approval workflows.

**Why now:** Security scanning is trending; manual remediation of findings does not scale—automated orchestration with audit trails is enterprise table-stakes.

**Stack hints:** `Go`, `Rust`, `PostgreSQL`, `GitHub API`, `Kubernetes client`, `temporal (workflow orchestration)`






#### Rust systems tooling and high-performance libraries


##### Polars-Native Analytics DSL Compiler

Build a Rust compiler that translates a high-level SQL-like DSL to optimized Polars query plans, includes cost-based optimization hints, and outputs execution flamegraphs. Support Python bindings and Jupyter integration for data science workflows.

**Why now:** Rust data tools like Polars are trending; data teams need a readable query language that compiles to efficient execution without writing DataFrame method chains.

**Stack hints:** `Rust`, `polars`, `pest (parser)`, `pyo3`, `pprof`






#### UI and visualization frameworks for web and native


##### Reactive Component State Machine for Svelte/Vue

Create a TypeScript library that defines UI component state machines via declarative YAML, automatically generates Svelte/Vue components with state validation, error handling, and async transitions. Include visual state diagram generation and time-travel debugging.

**Why now:** UI frameworks are trending; developers struggle with managing complex component state—visual, machine-based state management reduces bugs.

**Stack hints:** `TypeScript`, `Svelte`, `Vue`, `xstate`, `yaml`, `d3`









#### Workflow automation and orchestration


##### Decentralized Workflow Execution Engine

Build a TypeScript service that executes n8n-style workflows across distributed, edge-hosted nodes using P2P gossip and CRDTs for state sync. Support offline-first execution, automatic retry, and cost modeling for resource allocation.

**Why now:** Workflow automation is trending; enterprises need decentralized execution to avoid centralized bottlenecks and cloud provider dependencies.

**Stack hints:** `TypeScript`, `Node.js`, `iroh (P2P)`, `Yrs (CRDT)`, `SQLite`, `Express`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Reverse engineering and security analysis


##### Unified Binary Vulnerability Explorer

Develop a full-stack platform (Rust backend, React frontend) that indexes binaries from supply chains, runs Ghidra-based semantic analysis to extract function signatures and data flows, correlates findings with known CVEs, and visualizes attack surfaces. Include collaborative annotation and threat modeling.

**Why now:** Reverse engineering and security analysis are trending; enterprises need centralized visibility into binary composition and vulnerability propagation across dependencies.

**Stack hints:** `Rust`, `TypeScript`, `Ghidra headless API`, `PostgreSQL`, `React`, `WebSocket`, `NVD/CVE API`






#### Rust systems tooling and high-performance libraries


##### High-Performance DataFrame Vectorization Framework

Create a Rust framework that compiles high-level analytical queries to SIMD-vectorized CPU code using Polars, Arrow, and LLVM. Support spill-to-disk for out-of-core workloads, GPU acceleration via wgpu, and Python/R bindings. Benchmark against Spark for feature parity.

**Why now:** Rust systems tooling is trending; data teams need SIMD vectorization without rewriting to C++, and the gap between Python and specialized systems is closing.

**Stack hints:** `Rust`, `polars`, `arrow`, `llvm-sys`, `wgpu`, `pyo3`, `tokio`






#### UI and visualization frameworks for web and native


##### Cross-Platform Terminal UI Component Library

Create a Rust library (inspired by Egui) for building composable terminal user interfaces with immediate-mode rendering, rich animations, and keyboard/mouse input. Include React-like component composition, state hooks, and multi-theme support. Provide bindings for Python and Node.js.

**Why now:** UI frameworks are trending; terminal applications need modern, reactive UI paradigms currently dominated by web and native frameworks.

**Stack hints:** `Rust`, `crossterm`, `ratatui`, `pyo3`, `napi-rs`, `tokio`






#### Self-hosted infrastructure and remote access


##### Self-Hosted Media Recommendation Engine

Build a full-stack platform (Rust backend, React frontend) that indexes local media libraries (Immich-compatible), trains recommendation models locally using collaborative filtering, and generates personalized playlists and curations without cloud APIs. Support multi-user households with privacy isolation.

**Why now:** Self-hosted infrastructure is trending; users want recommendations for personal media without uploading viewing histories to commercial platforms.

**Stack hints:** `Rust`, `TypeScript`, `PostgreSQL`, `polars`, `React`, `ndarray (linear algebra)`, `websocket`






#### Workflow automation and orchestration


##### Enterprise Workflow Governance Platform

Develop a full-stack platform (Go/TypeScript) that manages n8n-style workflows with enterprise governance: approval gates, cost tracking, audit trails, SLA enforcement, and role-based access control. Support multi-tenant isolation, custom integrations, and deployment to Kubernetes or Docker Compose.

**Why now:** Workflow automation is trending; enterprises need visibility and control over workflow execution without surrendering operational flexibility.

**Stack hints:** `Go`, `TypeScript`, `PostgreSQL`, `React`, `GraphQL`, `Kubernetes`, `OIDC libraries`





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

*Generated 2026-10-11 17:25 UTC · commit `ad19c6b`*
