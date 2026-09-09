# genpark-cpg-island-viterbi-hmm-detector-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/alphaparkinc/genpark-cpg-island-viterbi-hmm-detector-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Hidden Markov Model (HMM) Viterbi decoder identifying CpG nucleotide islands and genomic methylation regions with dynamic state transitions.

## Architecture Overview

```mermaid
flowchart TD
    A[Agentic AI / Bioinformatics Orchestrator] -->|FASTA / DNA / Tree Matrix| B[MCP Server / Client]
    B --> C[genpark-cpg-island-viterbi-hmm-detector-skill Bio-Kernel]
    C --> D[Dynamic Programming / Hierarchical Tree / BWT Index]
    D --> E[Exact Alignment & Evolutionary Output]
    E -->|Structured Payload| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Comprehensive biochemical test cases, ultra-fast DP matrices.

## Quick Start
```bash
python example_usage.py
```
