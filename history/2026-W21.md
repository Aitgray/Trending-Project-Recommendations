# Trending Project Ideas

**Week of 2026-05-17** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> Rust infrastructure has broadened significantly beyond backends into full-stack tooling (bun, dioxus) and emerging database layer (neon), while security scanning (nuclei, trufflehog) has emerged as a persistent theme with community-driven DSLs. Workflow automation consolidation continues, but now competing directly with project management tools (plane) for workspace integration. System design education and AI/ML infrastructure training have newly surfaced as durable topics, reflecting organizational focus on architectural knowledge and large-scale model training.

---

## Trending Topics


### Rust systems infrastructure and developer tooling

Rust continues dominating infrastructure, version control, and developer tools (rustdesk, ruff, helix, miri, neon, bun), reflecting production maturity and preference for memory-safe, high-performance systems. This extends beyond previous trends into frontend tooling and database infrastructure.

<details>
<summary>Supporting repos (7)</summary>


- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

- [astral-sh/ruff](https://github.com/astral-sh/ruff)

- [helix-editor/helix](https://github.com/helix-editor/helix)

- [rust-lang/miri](https://github.com/rust-lang/miri)

- [neondatabase/neon](https://github.com/neondatabase/neon)

- [oven-sh/bun](https://github.com/oven-sh/bun)

- [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus)


</details>


### Workflow automation and no-code/low-code platforms

n8n, plane, and superset represent a consolidation around visual automation, project management, and data tools that reduce custom development friction. These platforms emphasize integration-first architecture and rapid API generation without boilerplate.

<details>
<summary>Supporting repos (4)</summary>


- [n8n-io/n8n](https://github.com/n8n-io/n8n)

- [makeplane/plane](https://github.com/makeplane/plane)

- [apache/superset](https://github.com/apache/superset)

- [usememos/memos](https://github.com/usememos/memos)


</details>


### Security scanning, vulnerability detection, and credential management

nuclei, nuclei-templates, and trufflehog show sustained interest in automated security scanning, DSL-driven vulnerability detection, and secret detection across infrastructure. This reflects organizational shift toward continuous, community-driven security validation.

<details>
<summary>Supporting repos (3)</summary>


- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)

- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)


</details>


### Fullstack type-safe APIs and end-to-end frameworks

trpc, supabase, svelte, and react-three-fiber demonstrate demand for frameworks that unify frontend and backend with shared types, reducing API contract friction. These tools prioritize developer experience and compile-time safety.

<details>
<summary>Supporting repos (4)</summary>


- [trpc/trpc](https://github.com/trpc/trpc)

- [supabase/supabase](https://github.com/supabase/supabase)

- [sveltejs/svelte](https://github.com/sveltejs/svelte)

- [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber)


</details>


### System design education and AI/ML pipeline infrastructure

donnemartin/system-design-primer, huggingface/transformers, pathwaycom/pathway, and NVIDIA/Megatron-LM reflect growing demand for both architectural knowledge and production-grade AI infrastructure for training and inference at scale.

<details>
<summary>Supporting repos (4)</summary>


- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

- [huggingface/transformers](https://github.com/huggingface/transformers)

- [pathwaycom/pathway](https://github.com/pathwaycom/pathway)

- [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Rust systems infrastructure and developer tooling


##### Rust Compilation Timeline Analyzer

Build a CLI tool that hooks into cargo's compilation lifecycle to generate detailed timelines of crate compilation, linking, and codegen. Produce interactive HTML reports showing per-module bottlenecks, incremental build efficiency, and LLVM optimization time. Suggest concrete optimizations (split work, enable thin-LTO, etc.).

**Why now:** Rust's expansion into full-stack tooling (bun, dioxus, neon) makes compile-time visibility critical for teams scaling Rust adoption.

**Stack hints:** `Rust`, `cargo_metadata`, `serde`, `plotly.rs`






#### Workflow automation and no-code/low-code platforms


##### Type-Safe Workflow Builder for n8n

Develop a TypeScript code generator that reads n8n workflow JSONs and generates fully typed, refactorable workflow definitions. Support IDE autocomplete for nodes, edge conditions, and variable bindings. Compile back to native n8n format with validation.

**Why now:** As workflow automation matures, developers need programmatic, type-safe abstractions over visual builders to reduce manual errors and enable versioning.

**Stack hints:** `TypeScript`, `n8n API`, `zod`, `prettier`






#### Security scanning, vulnerability detection, and credential management


##### Security Policy DSL Validator

Create a linter and validator for nuclei templates and custom security policies. Detect malformed DSL, suggest performance optimizations, identify unreachable conditions, and auto-generate test cases. Export reports as JSON for CI/CD integration.

**Why now:** nuclei's momentum as a community-driven scanning platform creates demand for policy tooling that ensures template quality and consistency at scale.

**Stack hints:** `Rust`, `pest`, `serde_yaml`, `clap`









#### System design education and AI/ML pipeline infrastructure


##### AI Model Cost Attribution Dashboard

Build a lightweight dashboard that aggregates compute costs from Megatron-LM training runs, fine-tuning jobs, and inference endpoints. Track per-model, per-layer, and per-task costs with projected ROI. Integrate with wandb or mlflow.

**Why now:** Large-scale AI training is becoming accessible to more teams, and cost attribution remains opaque—this fills a critical observability gap.

**Stack hints:** `Python`, `FastAPI`, `Plotly`, `SQLite`





---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Rust systems infrastructure and developer tooling


##### Rust-Native Database Migration Engine for Neon

Build a migration manager for Neon (serverless Postgres) that safely handles branching, schema evolution, and automatic rollback. Include conflict detection, dry-run simulation, and time-travel recovery to any previous branch state. Expose both CLI and SDK.

**Why now:** Neon's code-like branching model creates opportunities for developer-friendly migration tooling that manages the complexity of distributed schema changes.

**Stack hints:** `Rust`, `tokio`, `sqlx`, `neon_api`






#### Workflow automation and no-code/low-code platforms


##### Distributed Workflow Orchestration for n8n

Design a distributed execution layer for n8n that enables workflow spans across multiple workers with fault tolerance, rate limiting, and job prioritization. Support dependency graphs, conditional branching across workers, and result aggregation. Include Kubernetes-native deployment.

**Why now:** As n8n scales to enterprise teams, execution bottlenecks and resource contention require enterprise-grade distributed orchestration.

**Stack hints:** `TypeScript`, `Bull`, `Redis`, `n8n Plugin API`, `Kubernetes`






#### Security scanning, vulnerability detection, and credential management


##### Vulnerability Remediation Suggestion Engine

Extend nuclei output with an AI-powered suggestion layer that proposes concrete fixes for detected vulnerabilities (code patches, configuration changes, WAF rules). Integrate with GitHub PRs to auto-create remediation branches. Include severity-based prioritization and false-positive feedback loop.

**Why now:** As teams adopt nuclei for continuous scanning, manual remediation becomes a bottleneck—intelligent suggestions bridge detection and action.

**Stack hints:** `TypeScript`, `LangChain`, `GitHub API`, `PostgreSQL`






#### Fullstack type-safe APIs and end-to-end frameworks


##### Full-Stack Type Safety Bridge for Svelte + tRPC

Create an integrated framework that seamlessly bridges Svelte stores, tRPC client, and server procedures, ensuring end-to-end type safety. Auto-generate reactive form bindings, request/response validation, and error handling. Include dev-server with hot-reload.

**Why now:** Svelte's momentum combined with tRPC's typesafe API design creates demand for a unified development experience that eliminates manual type duplication.

**Stack hints:** `TypeScript`, `Svelte`, `tRPC`, `Zod`, `Vite`






#### System design education and AI/ML pipeline infrastructure


##### Interactive System Design Learning Platform

Create an interactive web-based platform built on donnemartin/system-design-primer's content that includes hands-on simulations (capacity planning calculators, load balancing visualizers, consistency model explorers). Auto-generate interview prep modules from system designs. Support collaborative whiteboarding.

**Why now:** System design education is reaching critical mass; interactive, immersive learning tools outperform static content and create stronger retention.

**Stack hints:** `TypeScript`, `React`, `D3.js`, `FastAPI`, `PostgreSQL`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Rust systems infrastructure and developer tooling


##### Dioxus Component Visual Builder

Develop a drag-and-drop visual builder for Dioxus components that generates production-ready Rust code. Support component composition, event binding, state management (hooks), and hot-reload. Export as git-friendly Rust files with prop types enforced by compiler. Include preview and test harness.

**Why now:** Dioxus is maturing as a fullstack Rust framework; a visual builder lowers the barrier to entry while maintaining Rust's type safety and performance benefits.

**Stack hints:** `TypeScript`, `React`, `Dioxus SDK`, `tree-sitter`, `WebSocket`


##### Rust Embedded Systems Runtime

Design a batteries-included Rust runtime for embedded and edge systems that combines async I/O (like Tokio), zero-copy serialization (serde), and deterministic resource management. Support WebAssembly compilation, OTA updates, and cross-device state sync. Ship with hardware abstraction layer for common MCUs.

**Why now:** Rust's proven success in systems infrastructure (rustdesk, neon, bun) makes it a natural fit for embedded systems; a cohesive runtime eliminates fragmentation and accelerates adoption.

**Stack hints:** `Rust`, `tokio-embedded`, `embassy`, `serde`, `WebAssembly`






#### Workflow automation and no-code/low-code platforms


##### End-to-End Encrypted Workflow Execution Platform

Build a privacy-first alternative to n8n/plane that encrypts workflow data in transit and at rest, supports zero-knowledge execution traces, and audits all access. Maintain full compatibility with n8n's JSON format for portability. Ship with FHIR/PII detection and compliance reporting.

**Why now:** Enterprise adoption of workflow automation platforms creates demand for privacy-preserving alternatives that handle sensitive data without exposing execution details to platform operators.

**Stack hints:** `TypeScript`, `TweetNaCl.js`, `PostgreSQL`, `n8n SDK`, `OpenTelemetry`






#### Security scanning, vulnerability detection, and credential management


##### Automated Security Posture Continuous Improvement System

Create a comprehensive platform that orchestrates nuclei scanning, trufflehog credential detection, and policy compliance checking across multi-cloud infrastructure. Auto-correlate findings, detect exploit chains, and generate risk-scored remediation playbooks. Include feedback loop for nuclei template refinement based on organizational context.

**Why now:** Security scanning tools are fragmenting across multiple specialized projects; a unified platform with intelligent correlation and continuous improvement creates significant operational value for teams.

**Stack hints:** `Go`, `Rust`, `Kubernetes`, `OpenSearch`, `NATS`, `Terraform`









#### System design education and AI/ML pipeline infrastructure


##### AI-Native Model Training Orchestrator

Develop a distributed training framework that abstracts Megatron-LM, DeepSpeed, and FSDP under a unified API. Auto-allocate GPU resources, manage checkpointing across failures, support multi-modal training (text + vision), and generate cost/performance tradeoff recommendations. Integrate with wandb for experiment tracking.

**Why now:** Large-scale model training is becoming mainstream; a unified orchestration layer that hides infrastructure complexity while exposing cost optimization is a critical missing piece.

**Stack hints:** `Python`, `PyTorch`, `Ray`, `Kubernetes`, `FastAPI`, `wandb API`





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

*Generated 2026-05-17 13:21 UTC · commit `31c6993`*
