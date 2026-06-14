# Trending Project Ideas

**Week of 2026-06-15** | [About this project](ABOUT.md)

---

> **What's new this week**
>
> AI agent orchestration has emerged as a distinct new theme with multiple competing platforms (Manifest, ActivePieces) focused on connecting agents to MCPs and LLM providers—a shift from generic workflow automation toward specialized agent tooling. Rust-native infrastructure has substantially expanded, now spanning 7+ repos across monitoring, blockchain, and runtimes, indicating ecosystem maturation beyond databases and editors. Developer experience tools have consolidated as a durable theme around reducing friction in git, API generation, and environment management. Educational platforms remain persistent, though now emphasizing system design interview prep alongside hands-on construction.

---

## Trending Topics


### Workflow automation platforms

Declarative, code-first workflow orchestration tools (n8n, Windmill, Airflow) emphasizing self-hosting, extensibility, AI integration, and performance optimization for enterprise automation.

<details>
<summary>Supporting repos (4)</summary>


- [n8n-io/n8n](https://github.com/n8n-io/n8n)

- [windmill-labs/windmill](https://github.com/windmill-labs/windmill)

- [apache/airflow](https://github.com/apache/airflow)

- [activepieces/activepieces](https://github.com/activepieces/activepieces)


</details>


### Rust-native infrastructure and developer tools

High-performance systems written in Rust spanning vector databases (Qdrant, Chroma), editors (Helix), system monitoring (bottom, sniffnet), and blockchain (reth), driven by memory safety and blazing-fast execution.

<details>
<summary>Supporting repos (7)</summary>


- [helix-editor/helix](https://github.com/helix-editor/helix)

- [qdrant/qdrant](https://github.com/qdrant/qdrant)

- [chroma-core/chroma](https://github.com/chroma-core/chroma)

- [ClementTsang/bottom](https://github.com/ClementTsang/bottom)

- [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet)

- [paradigmxyz/reth](https://github.com/paradigmxyz/reth)

- [oven-sh/bun](https://github.com/oven-sh/bun)


</details>


### Educational learning platforms and system design

Structured, hands-on learning systems (system-design-primer, build-your-own-x) that emphasize reproducible project-based progression, algorithm visualization, and interview preparation.

<details>
<summary>Supporting repos (3)</summary>


- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

- [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)

- [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)


</details>


### AI agent orchestration and tool integration

Platforms that connect AI agents to external tools, MCPs (Model Context Protocol), and multiple LLM providers (Manifest, ActivePieces), enabling composable agentic workflows and multi-provider interoperability.

<details>
<summary>Supporting repos (4)</summary>


- [activepieces/activepieces](https://github.com/activepieces/activepieces)

- [mnfst/manifest](https://github.com/mnfst/manifest)

- [langchain-ai/langchain](https://github.com/langchain-ai/langchain)

- [calcom/cal.diy](https://github.com/calcom/cal.diy)


</details>


### Developer experience and infrastructure tools

CLI tools and platforms that reduce friction in common workflows: git operations (lazygit), dependency management (OpenAPITools), dev environment management (coder), and observability (SigNoz).

<details>
<summary>Supporting repos (5)</summary>


- [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

- [coder/coder](https://github.com/coder/coder)

- [SigNoz/signoz](https://github.com/SigNoz/signoz)

- [OpenAPITools/openapi-generator](https://github.com/OpenAPITools/openapi-generator)

- [goauthentik/authentik](https://github.com/goauthentik/authentik)


</details>


---

## Project Ideas

### Short — Weekend Build (4–12 hours, one developer)




#### Workflow automation platforms


##### Workflow Template Analyzer and Generator

Build a CLI tool that analyzes n8n and Airflow workflows from GitHub, extracts common patterns (error handling, retries, notifications), and generates boilerplate code with configurable parameters. Output as reusable workflow blocks or JSON schemas that can be imported into either platform.

**Why now:** Workflow automation adoption is accelerating; reducing boilerplate and pattern discovery lowers friction for teams migrating between platforms or standardizing on org-wide workflows.

**Stack hints:** `Python`, `Click`, `GitHub API`, `YAML`, `jinja2`






#### Rust-native infrastructure and developer tools


##### Rust CLI Metrics Exporter for System Monitoring

Build a lightweight Rust CLI that captures system metrics (CPU, memory, I/O, process stats) in real-time, formats as Prometheus or OpenMetrics, and ships to SigNoz or Grafana Cloud. Include flamegraph profiling integration for Rust binaries.

**Why now:** Rust adoption in infrastructure is accelerating; native observability tooling that integrates with established stacks bridges the monitoring gap for Rust-written services.

**Stack hints:** `Rust`, `tokio`, `prometheus`, `sysinfo`, `clap`






#### Educational learning platforms and system design


##### Algorithm Step-Through Debugger with Complexity Analyzer

Create an interactive web tool that visualizes algorithm execution (sorting, graph traversal, dynamic programming) with step-through controls, variable state inspection, and automatic time/space complexity annotation. Support importing algorithms from JavaScript or Python.

**Why now:** Algorithm learning platforms are durable; interactive debugging significantly improves comprehension by bridging the gap between theoretical complexity analysis and observable execution.

**Stack hints:** `TypeScript`, `React`, `D3.js`, `Pyodide`, `Monaco Editor`






#### AI agent orchestration and tool integration


##### Agentic Workflow Debugger with LLM Inspector

Create a browser-based debugger that visualizes agent execution traces, inspects LLM prompts and completions, logs tool calls with arguments and results, and provides one-click playback of agent failures. Export execution logs for post-mortem analysis.

**Why now:** AI agents are rapidly proliferating; debugging opaque agent behavior requires visibility into LLM reasoning and tool interactions, enabling faster iteration and production reliability.

**Stack hints:** `TypeScript`, `React`, `Express`, `SQLite`, `D3.js`






#### Developer experience and infrastructure tools


##### Developer Environment Provisioning from Declarative Templates

Build a CLI that provisions development environments (via Coder or Docker) from declarative YAML templates specifying tools, language versions, IDE extensions, git repos, and secrets. Generate reproducible onboarding scripts for new team members.

**Why now:** Developer experience is a sustained focus; automating environment setup reduces onboarding friction and ensures consistency across teams.

**Stack hints:** `Go`, `YAML`, `Docker`, `Coder API`, `Cobra CLI`





---

### Medium — 1–2 Week Project (20–50 hours, portfolio-worthy)




#### Workflow automation platforms


##### Workflow Reliability Testing Framework with Mocking

Design a testing framework for n8n, Windmill, and Airflow workflows that supports declarative test definitions, mocks external service responses, captures execution metrics, generates test reports with coverage, and integrates with CI/CD for regression detection.

**Why now:** Workflow platforms are consolidating; robust testing infrastructure prevents production data pipeline failures and enables safe refactoring of automation logic.

**Stack hints:** `TypeScript`, `Jest`, `Express`, `PostgreSQL`, `Docker`, `Testcontainers`






#### Rust-native infrastructure and developer tools


##### Rust Systems Programming Bootcamp with Peer Code Review

Create a structured 8-week curriculum that teaches Rust systems programming through hands-on projects (kernel modules, filesystems, databases, network stacks). Include peer code review workflows, automated testing for submissions, and mentorship matching with experienced Rust developers.

**Why now:** Rust infrastructure adoption is accelerating; a focused bootcamp with peer mentorship and career outcomes addresses both the skill gap and hiring bottleneck for systems roles.

**Stack hints:** `Rust`, `TypeScript`, `React`, `PostgreSQL`, `Docker`, `GitHub Actions`






#### Educational learning platforms and system design


##### Interactive System Design Interview Prep Platform

Build a collaborative learning platform that combines system design interview prep (tradeoff visualizations, design patterns, failure mode simulations) with peer whiteboarding, expert code review, and timed practice interviews with feedback.

**Why now:** System design learning is durable; adding collaborative tools, expert feedback, and timed practice transforms passive learning into realistic interview simulation.

**Stack hints:** `TypeScript`, `React`, `FastAPI`, `PostgreSQL`, `WebSocket`, `Redis`






#### AI agent orchestration and tool integration


##### Agent MCP Server Marketplace with Discovery and Registration

Build a centralized registry for Model Context Protocol (MCP) servers, enabling agents to discover tools by capability tags, version constraints, and cost/latency characteristics. Include CLI for publishing, a dashboard for browsing, and auto-generated client stubs.

**Why now:** AI agents are multiplying rapidly; a centralized, versioned MCP marketplace reduces duplication and enables agents to dynamically discover and bind tools at runtime.

**Stack hints:** `TypeScript`, `Express`, `PostgreSQL`, `React`, `Docker`, `OpenAPI`






#### Developer experience and infrastructure tools


##### Developer Experience Metrics and Adoption Tracker

Build an observability tool that integrates with lazygit, Coder, authentication systems, and API generators to track developer productivity metrics (commit frequency, environment setup time, API-first adoption rates). Generate insights and bottleneck recommendations.

**Why now:** Developer experience is a sustained focus; quantifying productivity and identifying friction points enables data-driven infrastructure investments.

**Stack hints:** `Python`, `FastAPI`, `Prometheus`, `React`, `PostgreSQL`, `Grafana`





---

### Long — 1–3 Month Project (100+ hours, shippable)




#### Workflow automation platforms


##### Multi-Cloud Workflow Orchestration and Cost Optimizer

Design a production-grade workflow platform that translates natural language descriptions into optimized execution plans, automatically distributes tasks across AWS, Azure, and GCP based on cost and latency models, implements intelligent retries and failure handling, and includes visual authoring with compliance templating (HIPAA, GDPR, SOC 2).

**Why now:** Workflow automation is consolidating as a critical platform; a system combining natural language composition, multi-cloud optimization, and compliance automation captures enterprise and developer personas simultaneously.

**Stack hints:** `TypeScript`, `Python`, `FastAPI`, `PostgreSQL`, `Kubernetes`, `Terraform`, `Claude API`






#### Rust-native infrastructure and developer tools


##### Rust-Native Embedded Vector Database with Offline Sync

Develop a lightweight, embeddable Rust library for vector search optimized for edge deployment (mobile, wasm, IoT), supporting dynamic indexing, offline-first operation, automatic sync when connectivity resumes, and transparent encryption. Include SDKs for mobile platforms.

**Why now:** Rust's safety and performance are ideal for edge infrastructure; Qdrant and Chroma are server-centric; a privacy-first, edge-optimized alternative enables on-device ML inference and offline-capable applications.

**Stack hints:** `Rust`, `tokio`, `Arrow`, `RocksDB`, `wasm-bindgen`, `tonic`, `SQLite`






#### Educational learning platforms and system design


##### Comprehensive Programming Curriculum with Skill Graphs and Career Outcomes

Create a full-stack learning platform that models programming skills as an adaptive directed graph, personalizes learning paths based on goals and performance, integrates project-based assignments with peer code review, tracks employment outcomes, and connects learners with job placements. Support multiple languages, domains, and external tutorial imports.

**Why now:** Educational platforms have proven durable and scalable; a unified, outcome-focused system combining adaptive learning, community collaboration, and career integration transforms online education from content delivery into career acceleration.

**Stack hints:** `Python`, `FastAPI`, `PostgreSQL`, `TypeScript`, `React`, `D3.js`, `Redis`, `Kubernetes`






#### AI agent orchestration and tool integration


##### Agent Intelligence Platform with Tool Performance Analytics

Build a production-grade agent platform that provisions AI agents with dynamic tool binding, tracks tool invocation performance (success rates, latency, cost), learns from failures to optimize tool selection, and provides agents with context-aware decision-making based on aggregated telemetry. Include a visual orchestration canvas and multi-provider LLM support.

**Why now:** AI agents are production-critical; understanding tool performance and enabling agents to learn from execution history transforms manual orchestration into self-optimizing systems.

**Stack hints:** `Python`, `FastAPI`, `PostgreSQL`, `React`, `Redis`, `Kafka`, `Kubernetes`, `Claude API`






#### Developer experience and infrastructure tools


##### Enterprise Developer Productivity and Velocity Platform

Build a comprehensive developer platform that integrates git workflows (lazygit-like), environment provisioning (Coder-like), authentication (Authentik), observability (SigNoz), and API governance (OpenAPI). Provide unified dashboards for team velocity, infrastructure health, and automated recommendations for reducing bottlenecks.

**Why now:** Developer experience is a sustained theme across multiple tools; unifying these previously fragmented tools into a single coherent platform enables teams to measure and systematically improve overall productivity.

**Stack hints:** `TypeScript`, `Python`, `FastAPI`, `PostgreSQL`, `React`, `Kubernetes`, `Prometheus`, `Grafana`





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

*Generated 2026-06-14 14:03 UTC · commit `7e5dcb0`*
