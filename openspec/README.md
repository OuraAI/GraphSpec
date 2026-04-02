# OpenSpec Directory

This directory contains specifications and change proposals managed by [OpenSpec](https://github.com/Fission-AI/OpenSpec).

## Structure

```
openspec/
├── config.yaml      # Project configuration
├── specs/           # Source of truth (system behavior specs)
├── changes/         # Active change proposals
└── explorations/    # Exploratory specs (not yet committed)
```

## Workflow

```text
/opsx:propose <name>  →  Create change proposal
/opsx:apply           →  Implement tasks
/opsx:archive         →  Archive completed change
```

## Getting Started

1. Install OpenSpec: `npm install -g @fission-ai/openspec@latest`
2. Run `openspec update` to sync agent instructions
3. Use `/opsx:propose <feature-name>` to start a new change

## Configuration

See `config.yaml` for project-specific rules and context.
