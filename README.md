<div align="center">
  <h1>🌌 Orion (Evolved from MiroFish)</h1>
  <p><strong>A Next-Generation, Open-Source Multi-Agent AI Simulation Workspace</strong></p>
  <p><em>Transformed & Enhanced by <a href="https://github.com/Minato95-ayu">Minato95-ayu</a></em></p>
</div>

## 📖 The Evolution: From MiroFish to Orion

**Orion** is not just a fork; it's a complete evolution. Originally based on the powerful **MiroFish** engine (powered by CAMEL-AI and OASIS), this project has been heavily adapted, refactored, and transformed into the **Orion AI Scenario Simulation Workspace** by Minato95-ayu.

### 🚀 What's New in Orion?
Here is what makes **Orion** unique and highlights the new implementations:
- **Rebranded & Restructured Core**: The entire project structure, configuration files (`package.json`, `pyproject.toml`), and application entry points have been fundamentally renamed and tailored from MiroFish to the Orion ecosystem.
- **Enhanced Workspace Environment**: Orion focuses on creating a seamless "prediction workspace" where users can upload complex documents (PDFs, TXT, MD) and immediately spawn an interactive digital twin of that data.
- **Custom Integrations**: Built with extensibility in mind, Orion makes it easier to plug in custom LLM APIs (like Gemini 2.5 Flash) out-of-the-box and connect deeply with Zep Cloud for robust graph-backed memories.
- **Optimized Deployment Pipeline**: Streamlined Docker configurations and local execution scripts (`npm run setup:all`, `npm run dev`) for instant, concurrent full-stack development.

## ✨ Core Engine Features

- **🧠 GraphRAG Knowledge Construction**: Parses seed material to extract key entities and complex relationships into a dynamic memory graph.
- **🤖 Autonomous Agent Generation**: Automatically prepares thousands of unique simulation agents, each with independent personalities and behavioral logic.
- **🌍 Multi-Agent Social Simulation**: Agents interact, persuade, and evolve within a simulated digital twin.
- **📊 Prediction Reports**: Observes emergent social patterns to produce comprehensive future trajectory reports.

## 🏗️ Architecture Stack

### Frontend
- **Framework**: Vue 3 & Vite
- **Data Visualization**: D3.js (for memory graph and agent interaction rendering)
- **API Communication**: Axios
- **Routing**: Vue Router

### Backend
- **Framework**: Python 3.11+ / Flask
- **Simulation Engine**: `camel-oasis` & `camel-ai` for multi-agent role-playing
- **Graph & Memory**: `zep-cloud` for graph-backed memory management
- **LLM Integration**: `openai` compatible APIs (configured out-of-the-box for Gemini models)
- **Document Parsing**: `PyMuPDF` for fast document ingestion

## 🚀 Future Scope & Roadmap (The Orion Vision)

As **Orion** continues to grow, the following features are on the immediate roadmap:
- **Real-Time Web Search Grounding**: Allowing agents to fetch live internet data during simulations.
- **Enhanced 3D Visualizations**: Upgrading the D3 graph to an immersive 3D simulation explorer.
- **Custom Agent Prompt Injections**: Permitting users to manually tweak agent personalities, hidden agendas, and biases before a simulation run.
- **Exportable Simulations**: Saving complete simulation states for later playback.
- **Broader Local LLM Support**: Native adapters for local models (e.g., via Ollama) for completely private, offline simulations.

## 🛠️ Local Setup

Create a `.env` file based on `.env.example` and fill in your actual keys:

```env
LLM_API_KEY=your_key
LLM_BASE_URL=http://127.0.0.1:8000/v1
LLM_MODEL_NAME=gemini/gemini-2.5-flash
ZEP_API_KEY=your_zep_key
SECRET_KEY=replace_with_a_long_random_secret
FLASK_DEBUG=False
```

### Quick Start (Node & Python)

Install all dependencies (frontend and backend via `uv`) and run both servers simultaneously:

```bash
npm run setup:all
npm run dev
```

**Useful URLs**:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5001`
- Health Check: `http://localhost:5001/health`

### Docker Deployment

For a seamless, containerized setup, ensure your `.env` is ready and run:

```bash
docker compose up -d
```
The compose file automatically mounts your local `.env` and maps ports `3000` and `5001`.

---
<div align="center">
  <sub>Transformed with ❤️ by Minato95-ayu | Core Engine powered by MiroFish, CAMEL-AI, and OASIS teams.</sub>
</div>
