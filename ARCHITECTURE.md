# Orion: Architecture & Logic Workflow

This document outlines the core architecture, the step-by-step logic workflow of the Orion simulation engine, and the future development roadmap.

## 🏗️ 1. System Architecture Overview

Orion follows a modern, decoupled Client-Server architecture designed for heavy AI processing and dynamic data visualization.

### Frontend (Client Layer)
- **Framework**: Vue 3 powered by Vite for rapid development and optimized builds.
- **Visualization**: D3.js is used to render complex memory graphs and live agent interaction networks.
- **State Management & Routing**: Vue Router for navigation, interacting with backend endpoints via Axios.

### Backend (Server Layer)
- **Framework**: Python 3.11+ with Flask, providing robust API endpoints.
- **Simulation Engine**: Leverages `camel-oasis` and `camel-ai` for managing multi-agent role-playing and autonomous behaviors.
- **Memory Management**: Integrates **Zep Cloud** for robust, graph-backed memory storage, allowing agents to query past context and relationships.
- **LLM Gateway**: Uses OpenAI-compatible API structures, configured by default to utilize high-speed models like Gemini 2.5 Flash.
- **Document Processing**: Utilizes `PyMuPDF` for fast, reliable ingestion of PDFs and other document formats.

---

## 🔄 2. Logic Workflow (End-to-End Execution)

The core lifecycle of an Orion simulation runs through the following distinct phases:

### Phase 1: Data Ingestion & Parsing
1. **Upload**: The user uploads source material (PDF, TXT, MD) and defines a simulation goal via the Vue frontend.
2. **Parsing**: The Flask backend receives the document and uses `PyMuPDF` to extract raw text, chunking it for optimal LLM processing.

### Phase 2: Knowledge Graph Construction (GraphRAG)
1. **Extraction**: The LLM processes the text chunks to identify key entities, concepts, and relationships.
2. **Graph Building**: This structured data is fed into **Zep Cloud**, constructing a dynamic memory graph. This graph serves as the "world knowledge base" for the simulation.

### Phase 3: Autonomous Agent Generation
1. **Persona Creation**: Based on the context of the knowledge graph and the user's prompt, the system automatically spawns a diverse set of simulation agents.
2. **Initialization**: Each agent is injected with unique traits, behavioral logic, hidden agendas, and memory access permissions using the `camel-ai` framework.

### Phase 4: Multi-Agent Simulation
1. **Execution**: The environment goes live. Agents interact with one another, query the Zep memory graph, and make decisions.
2. **Evolution**: Agents debate, persuade, and adapt. The `camel-oasis` engine orchestrates these interactions to ensure logical progression and prevent looping.

### Phase 5: Visualization & Synthesis
1. **Live Rendering**: Simulation data is sent to the frontend, where **D3.js** renders the evolving network of agents and their interactions in real-time.
2. **Reporting**: Once the simulation concludes (or hits a milestone), the system observes the emergent social patterns and synthesizes a comprehensive **Prediction Report** for the user.

---

## 🚀 3. Future Plan & Roadmap

As the Orion engine evolves, the following features and architectural improvements are planned:

### Near-Term Goals
- **Real-Time Web Search Grounding**: Equip agents with tools to fetch live internet data during simulations, allowing for highly relevant, real-world predictions.
- **Custom Agent Prompt Injections**: Develop a UI module that allows users to manually tweak an agent's hidden agenda, biases, or starting knowledge before launching a run.
- **Broader Local LLM Support**: Implement native adapters for local models (e.g., via Ollama or LM Studio) to enable completely private, offline simulations without API costs.

### Mid-Term Goals
- **Immersive 3D Visualizations**: Upgrade the current D3.js 2D graph to an interactive 3D simulation explorer (using Three.js/WebGL) for better spatial understanding of massive agent networks.
- **Simulation State Export/Import**: Allow users to pause, save, export, and share complete simulation states, enabling "playback" or branching simulations from a specific point in time.

### Long-Term Vision
- **Massive Scalability & Container Orchestration**: Transition the backend simulation engine to support Kubernetes (K8s) deployments, enabling simulations with tens of thousands of concurrent agents distributed across multiple nodes.
- **Cross-Simulation Agent Memory**: Allow veteran agents to retain memories and experiences across completely different simulation runs.
