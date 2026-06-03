<template>
  <main class="orion-home">
    <header class="topbar">
      <button class="brand" @click="scrollToTop" aria-label="Go to top">
        <span class="brand-mark">O</span>
        <span>Orion</span>
      </button>
      <a class="ghost-link" href="https://github.com/666ghj/MiroFish" target="_blank" rel="noreferrer">
        Source
      </a>
    </header>

    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">AI scenario lab</p>
        <h1>Turn source material into a living prediction workspace.</h1>
        <p class="lead">
          Orion reads your documents, builds a memory graph, prepares simulated agents,
          runs the scenario, and gives you an analysis report you can keep exploring.
        </p>
        <div class="highlights">
          <span>Graph memory</span>
          <span>Agent simulation</span>
          <span>Interactive reports</span>
        </div>
      </div>

      <form class="launch-panel" @submit.prevent="startSimulation">
        <div class="panel-heading">
          <div>
            <p class="section-kicker">New run</p>
            <h2>Start a scenario</h2>
          </div>
          <span class="status-pill" :class="{ ready: canSubmit }">
            {{ canSubmit ? 'Ready' : 'Waiting' }}
          </span>
        </div>

        <label
          class="upload-zone"
          :class="{ active: isDragOver, filled: files.length > 0 }"
          @dragover.prevent="isDragOver = true"
          @dragleave.prevent="isDragOver = false"
          @drop.prevent="handleDrop"
        >
          <input
            ref="fileInput"
            type="file"
            multiple
            accept=".pdf,.md,.txt,.markdown,.html,.htm"
            @change="handleFileSelect"
          />
          <span class="upload-icon">+</span>
          <span class="upload-title">Drop reports, notes, PDFs, markdown, or HTML</span>
          <span class="upload-subtitle">PDF, TXT, MD, Markdown, and HTML files are supported.</span>
        </label>

        <div v-if="files.length" class="file-list" aria-label="Selected files">
          <div v-for="(file, index) in files" :key="`${file.name}-${index}`" class="file-row">
            <span>{{ file.name }}</span>
            <button type="button" @click="removeFile(index)" aria-label="Remove file">Remove</button>
          </div>
        </div>

        <label class="prompt-field">
          <span>Scenario question</span>
          <textarea
            v-model="formData.simulationRequirement"
            rows="7"
            placeholder="Example: If the company announces a price increase next week, how might customers, competitors, and media respond over the next 30 days?"
          ></textarea>
        </label>

        <p v-if="error" class="error-text">{{ error }}</p>

        <button class="primary-action" type="submit" :disabled="!canSubmit || loading">
          <span>{{ loading ? 'Preparing...' : 'Build Orion workspace' }}</span>
          <span aria-hidden="true">-></span>
        </button>
      </form>
    </section>

    <section class="workflow">
      <div class="section-heading">
        <p class="section-kicker">Workflow</p>
        <h2>One clear path from upload to insight</h2>
      </div>
      <div class="workflow-grid">
        <article v-for="step in steps" :key="step.number" class="workflow-card">
          <span class="step-number">{{ step.number }}</span>
          <h3>{{ step.title }}</h3>
          <p>{{ step.description }}</p>
        </article>
      </div>
    </section>

    <HistoryDatabase />
  </main>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'

const router = useRouter()

const formData = ref({ simulationRequirement: '' })
const files = ref([])
const loading = ref(false)
const error = ref('')
const isDragOver = ref(false)

const steps = [
  { number: '01', title: 'Build memory graph', description: 'Extract entities, relationships, and context from your seed material.' },
  { number: '02', title: 'Prepare agents', description: 'Generate scenario-ready personas and simulation settings from the graph.' },
  { number: '03', title: 'Run the world', description: 'Simulate social behavior across supported platforms and rounds.' },
  { number: '04', title: 'Write the report', description: 'Use the simulation output to produce a structured forecast and evidence trail.' },
  { number: '05', title: 'Keep exploring', description: 'Ask follow-up questions and inspect agents, posts, actions, and graph memory.' }
]

const canSubmit = computed(() => {
  return formData.value.simulationRequirement.trim().length > 0 && files.value.length > 0
})

const addFiles = (newFiles) => {
  error.value = ''
  const validFiles = newFiles.filter(file => {
    const ext = file.name.split('.').pop()?.toLowerCase()
    return ['pdf', 'md', 'txt', 'markdown', 'html', 'htm'].includes(ext)
  })

  if (validFiles.length !== newFiles.length) {
    error.value = 'Some files were skipped. Orion accepts PDF, TXT, MD, Markdown, and HTML files.'
  }

  files.value.push(...validFiles)
}

const handleFileSelect = (event) => {
  addFiles(Array.from(event.target.files || []))
  event.target.value = ''
}

const handleDrop = (event) => {
  isDragOver.value = false
  addFiles(Array.from(event.dataTransfer.files || []))
}

const removeFile = (index) => {
  files.value.splice(index, 1)
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const startSimulation = async () => {
  if (!canSubmit.value || loading.value) return
  loading.value = true
  error.value = ''

  try {
    const { setPendingUpload } = await import('../store/pendingUpload.js')
    setPendingUpload(files.value, formData.value.simulationRequirement)
    router.push({ name: 'Process', params: { projectId: 'new' } })
  } catch (err) {
    error.value = err.message || 'Unable to start the workspace.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.orion-home {
  min-height: 100vh;
  background: #f7f4ee;
  color: #17201a;
}

.topbar {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  border-bottom: 1px solid rgba(23, 32, 26, 0.12);
  background: rgba(247, 244, 238, 0.92);
  position: sticky;
  top: 0;
  z-index: 10;
  backdrop-filter: blur(14px);
}

.brand,
.ghost-link {
  color: inherit;
  text-decoration: none;
  font: inherit;
}

.brand {
  border: 0;
  background: transparent;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  font-size: 18px;
  cursor: pointer;
}

.brand-mark {
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #17201a;
  color: #f7f4ee;
}

.ghost-link {
  border: 1px solid rgba(23, 32, 26, 0.18);
  border-radius: 999px;
  padding: 9px 14px;
  font-weight: 700;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(360px, 520px);
  gap: 48px;
  align-items: start;
  padding: 76px 32px 48px;
  max-width: 1240px;
  margin: 0 auto;
}

.eyebrow,
.section-kicker {
  margin: 0 0 12px;
  color: #8f5b2f;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 12px;
}

.hero h1 {
  margin: 0;
  max-width: 780px;
  font-size: clamp(44px, 7vw, 84px);
  line-height: 0.96;
  letter-spacing: 0;
}

.lead {
  margin: 28px 0 0;
  max-width: 660px;
  font-size: 19px;
  line-height: 1.65;
  color: #4d5b50;
}

.highlights {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 28px;
}

.highlights span {
  border: 1px solid rgba(23, 32, 26, 0.16);
  border-radius: 999px;
  padding: 9px 12px;
  background: rgba(255, 255, 255, 0.45);
  font-weight: 700;
}

.launch-panel {
  background: #fffdf8;
  border: 1px solid rgba(23, 32, 26, 0.14);
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 24px 60px rgba(23, 32, 26, 0.1);
}

.panel-heading,
.file-row,
.primary-action {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.panel-heading h2,
.section-heading h2,
.workflow-card h3 {
  margin: 0;
}

.status-pill {
  border-radius: 999px;
  padding: 7px 10px;
  background: #ece7dc;
  color: #6b6559;
  font-weight: 800;
  font-size: 12px;
}

.status-pill.ready {
  background: #d7eadb;
  color: #246333;
}

.upload-zone {
  margin-top: 22px;
  min-height: 150px;
  border: 1.5px dashed rgba(23, 32, 26, 0.24);
  border-radius: 8px;
  display: grid;
  place-items: center;
  text-align: center;
  padding: 26px;
  cursor: pointer;
  background: #faf7ef;
}

.upload-zone.active,
.upload-zone:hover {
  border-color: #8f5b2f;
  background: #f5ebdc;
}

.upload-zone input {
  display: none;
}

.upload-icon {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #17201a;
  color: white;
  font-weight: 800;
  margin-bottom: 12px;
}

.upload-title,
.prompt-field span {
  font-weight: 800;
}

.upload-subtitle {
  color: #667168;
  font-size: 13px;
  margin-top: 6px;
}

.file-list {
  display: grid;
  gap: 8px;
  margin-top: 14px;
}

.file-row {
  gap: 16px;
  border: 1px solid rgba(23, 32, 26, 0.12);
  border-radius: 6px;
  padding: 10px 12px;
  background: white;
}

.file-row span {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-row button {
  border: 0;
  background: transparent;
  color: #9b3d2e;
  font-weight: 800;
  cursor: pointer;
}

.prompt-field {
  display: grid;
  gap: 10px;
  margin-top: 20px;
}

.prompt-field textarea {
  width: 100%;
  resize: vertical;
  border: 1px solid rgba(23, 32, 26, 0.16);
  border-radius: 8px;
  padding: 14px;
  font: inherit;
  line-height: 1.55;
  background: white;
  color: #17201a;
}

.error-text {
  color: #9b3d2e;
  font-weight: 700;
}

.primary-action {
  width: 100%;
  margin-top: 20px;
  border: 0;
  border-radius: 8px;
  padding: 16px 18px;
  background: #17201a;
  color: white;
  font-weight: 900;
  cursor: pointer;
}

.primary-action:disabled {
  cursor: not-allowed;
  background: #d9d3c7;
  color: #777064;
}

.workflow {
  max-width: 1240px;
  margin: 0 auto;
  padding: 28px 32px 64px;
}

.workflow-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 14px;
  margin-top: 22px;
}

.workflow-card {
  background: rgba(255, 253, 248, 0.78);
  border: 1px solid rgba(23, 32, 26, 0.12);
  border-radius: 8px;
  padding: 18px;
}

.step-number {
  display: block;
  color: #8f5b2f;
  font-weight: 900;
  margin-bottom: 20px;
}

.workflow-card p {
  color: #5c685e;
  line-height: 1.55;
  margin-bottom: 0;
}

@media (max-width: 980px) {
  .hero {
    grid-template-columns: 1fr;
    padding-top: 44px;
  }

  .workflow-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 620px) {
  .topbar {
    padding: 0 18px;
  }

  .hero,
  .workflow {
    padding-left: 18px;
    padding-right: 18px;
  }

  .workflow-grid {
    grid-template-columns: 1fr;
  }
}
</style>
