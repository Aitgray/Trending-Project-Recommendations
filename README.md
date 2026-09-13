# Trending Project Ideas

**Week of 2026-09-13** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> Self-hosted media and data management has emerged as a distinct theme, driven by privacy concerns and the maturation of platforms like Immich displacing generic cloud storage. Security scanning has solidified into a core concern with Gitleaks and Trivy showing sustained trending, reflecting heightened developer focus on credential leakage and supply-chain attacks. AI agent platforms now compete for dominance with clear self-hosting narratives (Windmill, n8n, LangChain), moving beyond last week's generic orchestration into native AI reasoning and visual composition. Performance-native Rust tooling remains persistent but has shifted focus from compiler/formatter dominance to ecosystem maturity—Ruff, Helix, and Zoxide show sustained interest, indicating architectural consolidation.

---

## Trending Topics


### Self-hosted media, photo, and data management

Privacy-first platforms for managing photos, videos, and personal data with local storage and sync capabilities. Emphasis on replacing centralized cloud services with self-controlled infrastructure.

<details>
<summary>Supporting repos (3)</summary>


- [immich-app/immich](https://github.com/immich-app/immich)

- [laurent22/joplin](https://github.com/laurent22/joplin)

- [calcom/cal.diy](https://github.com/calcom/cal.diy)


</details>


### Security scanning and credential detection

Tools for discovering, verifying, and analyzing leaked credentials and security vulnerabilities across codebases and infrastructure. Enables automated secret detection and compliance workflows.

<details>
<summary>Supporting repos (3)</summary>


- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)

- [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

- [aquasecurity/trivy](https://github.com/aquasecurity/trivy)


</details>


### AI agent and workflow orchestration platforms

Self-hosted systems combining LLM orchestration, workflow automation, and native AI capabilities without vendor lock-in. Enables multi-step automation with agent reasoning and visual/code-based composition.

<details>
<summary>Supporting repos (3)</summary>


- [windmill-labs/windmill](https://github.com/windmill-labs/windmill)

- [langchain-ai/langchain](https://github.com/langchain-ai/langchain)

- [n8n-io/n8n](https://github.com/n8n-io/n8n)


</details>


### Performance-native Rust developer tools

High-velocity CLI utilities and frameworks written in Rust for tasks like linting, editing, and navigation. Replaces slower interpreted-language alternatives with orders-of-magnitude speed improvements.

<details>
<summary>Supporting repos (3)</summary>


- [astral-sh/ruff](https://github.com/astral-sh/ruff)

- [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)

- [helix-editor/helix](https://github.com/helix-editor/helix)


</details>


### Remote access and decentralized infrastructure

Rust-native tools enabling self-hosted remote desktop, terminal access, and secure device management without reliance on centralized platforms. Focuses on control, privacy, and peer-to-peer connectivity.

<details>
<summary>Supporting repos (3)</summary>


- [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

- [zitadel/zitadel](https://github.com/zitadel/zitadel)

- [authelia/authelia](https://github.com/authelia/authelia)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Self-hosted media, photo, and data management


##### Self-Hosted Photo Library Sync Agent

Create a Python daemon that monitors local photo directories, auto-organizes by date/EXIF metadata, generates thumbnails and low-res previews, and syncs to a remote server via rsync over SSH. Include a simple CLI to configure sync rules and conflict resolution strategies.

**Why now:** Self-hosted photo management is trending; individuals need lightweight sync without subscriptions or cloud vendor lock-in.

**Stack hints:** `Python`, `Pillow`, `exifread`, `asyncio`, `paramiko`






#### Security scanning and credential detection


##### Credential Drift Detector with Automated Rotation Triggers

Build a lightweight Go CLI that periodically scans a directory tree with Gitleaks and Trufflehog, tracks credential history in a local SQLite database, and alerts via webhook when new secrets are detected or credentials age past a configurable threshold. Output JSON reports suitable for CI/CD integration.

**Why now:** Security scanning is trending; teams need automated detection that feeds into rotation workflows rather than siloed alerts.

**Stack hints:** `Go`, `gitleaks/gitleaks`, `trufflesecurity/trufflehog`, `SQLite`






#### AI agent and workflow orchestration platforms


##### Workflow Template Registry with Version Control

Build a Git-like CLI tool that manages workflow templates for n8n/Windmill, enables versioning via local YAML storage, supports branching/merging for template variants, and exports to platform-native formats. Include search and metadata tagging for discovery.

**Why now:** AI workflow platforms are trending; teams need versioning discipline and template reuse patterns analogous to code libraries.

**Stack hints:** `Rust`, `tokio`, `git2-rs`, `serde_yaml`, `clap`






#### Performance-native Rust developer tools


##### Rust CLI Latency Dashboard with Real-Time Regression Alerts

Write a Rust binary that benchmarks a suite of CLI tools (ruff, zoxide, helix) across commits, tracks latency trends in a JSON store, and emits desktop notifications when regressions exceed a threshold. Include a minimal TUI dashboard showing historical trends.

**Why now:** Performance-native Rust tools are trending; maintainers need real-time feedback to preserve sub-millisecond guarantees.

**Stack hints:** `Rust`, `criterion`, `serde_json`, `ratatui`, `notify-rust`






#### Remote access and decentralized infrastructure


##### Decentralized Device Registry with mDNS Discovery

Create a Go service that advertises RustDesk endpoints via mDNS, maintains a local device registry in JSON, and enables peer-to-peer device discovery without a central server. Support basic reputation scoring and firewall-aware connectivity hints.

**Why now:** Remote access and self-hosting are trending; teams need resilient discovery that survives centralized infrastructure failures.

**Stack hints:** `Go`, `github.com/grandcat/zeroconf`, `encoding/json`, `net`





---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Self-hosted media, photo, and data management


##### Multi-Tenant Photo Library with Semantic Search

Develop a TypeScript/Rust service combining Immich-style photo management with CLIP-based image embeddings for semantic search. Support multi-tenant isolation, role-based album sharing, and automatic tagging via local LLM. Include a React UI for browsing, searching, and collaborative albums.

**Why now:** Self-hosted media management is trending; users need AI-powered discovery without external APIs or cloud processing.

**Stack hints:** `TypeScript`, `Rust`, `PostgreSQL`, `ort (ONNX Runtime)`, `React`, `milvus`






#### Security scanning and credential detection


##### Credential Leak Response Orchestrator

Build a Go service that ingests credential scan alerts from Gitleaks, Trivy, and custom sources, correlates them by asset type (database, API key, certificate), and triggers automated remediation chains (secret rotation via HashiCorp Vault, notification to on-call engineers, incident ticket creation). Include audit logging and rollback support.

**Why now:** Security scanning is trending; teams need coordinated responses to credential leakage rather than fragmented manual workflows.

**Stack hints:** `Go`, `PostgreSQL`, `gRPC`, `HashiCorp Vault`, `github.com/octokit/go-sdk`






#### AI agent and workflow orchestration platforms


##### Workflow Performance Profiler with Cost Attribution

Create a Python/TypeScript observability layer for n8n/Windmill workflows that tracks execution time, LLM token usage, and cost per step. Generate reports comparing performance across workflow versions, identify bottlenecks via flame graphs, and support A/B testing workflow variants with statistical significance testing.

**Why now:** AI workflow platforms are trending; teams need cost and performance visibility to optimize agent-driven automation at scale.

**Stack hints:** `Python`, `FastAPI`, `PostgreSQL`, `pydantic`, `altair`






#### Performance-native Rust developer tools


##### Rust CLI Ecosystem Benchmark Suite

Develop a comprehensive benchmarking framework comparing Rust CLI tools (ruff vs Black, zoxide vs autojump, helix vs Vim) across metrics: latency, memory, CPU, startup time. Generate public HTML reports with trend visualization, integrate with GitHub Actions for continuous tracking, and support custom metric collection via WASM plugins.

**Why now:** Performance-native Rust tooling is trending; the ecosystem needs standardized benchmarking to quantify performance gains and motivate optimization.

**Stack hints:** `Rust`, `criterion`, `pprof`, `D3.js`, `rocket`, `wasmtime`






#### Remote access and decentralized infrastructure


##### Zero-Trust Remote Access VPN with Reputation Scoring

Build a Rust VPN service using Tailscale/WireGuard primitives that authenticates peers via mTLS certificates, tracks peer reputation based on access patterns and security posture, and dynamically restricts access based on risk scoring. Support multi-hop routing through trusted peers and include audit logging for compliance.

**Why now:** Remote access and self-hosting are trending; teams need granular, reputation-aware access control for decentralized networks.

**Stack hints:** `Rust`, `tokio`, `boringtun`, `x509-parser`, `serde`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Self-hosted media, photo, and data management


##### Distributed Media Sync with Peer-to-Peer Conflict Resolution

Create a full-stack platform for syncing photo/video libraries across multiple self-hosted devices using CRDT-based conflict resolution, peer-to-peer transfers with bandwidth optimization, and end-to-end encryption. Support selective sync rules, automatic deduplication via content-addressing, and web UI for management and sharing. Include migration tools from cloud photo services.

**Why now:** Self-hosted media management is trending; users need reliable cross-device sync without centralized storage or cloud vendors.

**Stack hints:** `Rust`, `TypeScript`, `yrs (CRDT)`, `PostgreSQL`, `quinn (QUIC)`, `React`






#### Security scanning and credential detection


##### Threat Intelligence Platform with Automated Response

Develop an integrated security platform that combines credential scanning (Gitleaks), vulnerability detection (Trivy), and OSINT correlation (user account enumeration across services). Automatically ingest threat feeds, correlate detections with asset inventory, and trigger playbook-driven responses (isolation, patching, notification escalation). Include forensic capabilities for post-incident analysis and compliance reporting.

**Why now:** Security scanning is trending; organizations need centralized threat orchestration connecting credential leaks, vulnerabilities, and reconnaissance activities.

**Stack hints:** `Go`, `Rust`, `PostgreSQL`, `ClickHouse`, `gRPC`, `Kubernetes`






#### AI agent and workflow orchestration platforms


##### Agentic Workflow Studio with Live Simulation

Build a comprehensive IDE for designing, testing, and deploying AI agent workflows combining visual node-based composition, inline code editing, and live simulation against mock/real data. Support versioning, A/B testing via canary deployments, and integrated observability (latency, cost, agent reasoning traces). Include templates for common patterns (document Q&A, customer support, data extraction) with pre-built integrations.

**Why now:** AI workflow platforms are trending; teams need unified authoring, testing, and deployment environments that make agent workflows accessible to non-experts.

**Stack hints:** `TypeScript`, `React`, `Rust`, `PostgreSQL`, `LangChain`, `Tauri`






#### Performance-native Rust developer tools


##### Rust Performance Observatory with Comparative Analytics

Create a public observability platform for tracking Rust CLI ecosystem performance over time. Ingest benchmarks from maintainers (ruff, zoxide, helix, k9s) via standardized API, correlate performance with code changes via git history, and generate interactive reports showing performance tiers, regressions, and optimization opportunities. Support predictive alerts when regressions exceed statistical thresholds.

**Why now:** Performance-native Rust tooling is trending; the ecosystem needs shared infrastructure to track progress and celebrate optimizations across tools.

**Stack hints:** `Rust`, `TypeScript`, `PostgreSQL`, `TimescaleDB`, `D3.js`, `git2-rs`






#### Remote access and decentralized infrastructure


##### Enterprise Remote Access Mesh with Compliance Audit Trail

Develop a production-grade, self-hosted remote access platform combining RustDesk-style device connectivity with enterprise features: role-based access control, session recording, compliance audit logging (SOC2/ISO 27001), automatic session termination policies, and integration with Zitadel/Authelia for federated identity. Include analytics dashboard for access patterns and anomaly detection.

**Why now:** Remote access and self-hosting are trending; enterprises need privacy-preserving alternatives to centralized remote desktop services with compliance guarantees.

**Stack hints:** `Rust`, `Go`, `PostgreSQL`, `Kubernetes`, `React`, `gRPC`





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

*Generated 2026-09-13 15:43 UTC · commit `9c2d9f6`*
