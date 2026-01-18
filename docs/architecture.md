# Architecture

TODO

## Request Flow
```mermaid
sequenceDiagram
    participant B as Browser :3000
    participant F as Frontend (Node)
    participant A as Flask API :5000
    participant L as llama-server :8081
    participant O as owasp-llm-tool

    B->>F: 1. Type prompt
    F->>A: 2. POST /api/test
    A->>L: 3. POST /completion
    L-->>A: LLM response
    A->>O: 4. Run detection
    O-->>A: Category (LLM01/02/06/unknown)
    A-->>F: 5. JSON result
    F-->>B: Render page
```

## Components

| Component | Port | Purpose |
|-----------|------|---------|
| Frontend (Node) | 3000 | Web UI |
| Flask API | 5000 | Orchestration |
| llama-server | 8081 | LLM inference |
| owasp-llm-tool | - | OWASP category detection |


