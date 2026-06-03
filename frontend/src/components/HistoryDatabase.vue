<template>
  <section class="history">
    <div class="section-heading">
      <p class="section-kicker">History</p>
      <h2>Recent workspaces</h2>
    </div>

    <div v-if="loading" class="state">Loading recent scenarios...</div>
    <div v-else-if="projects.length === 0" class="state">
      No previous workspaces yet. Start one above and Orion will keep it here.
    </div>

    <div v-else class="history-grid">
      <article v-for="project in projects" :key="project.simulation_id" class="history-card">
        <div class="card-topline">
          <span>{{ formatSimulationId(project.simulation_id) }}</span>
          <span :class="['run-status', getProgressClass(project)]">{{ formatRounds(project) }}</span>
        </div>
        <h3>{{ getSimulationTitle(project.simulation_requirement) }}</h3>
        <p>{{ truncateText(project.simulation_requirement, 130) }}</p>
        <div class="file-strip" v-if="project.files?.length">
          <span v-for="file in project.files.slice(0, 3)" :key="file.filename">
            {{ getFileTypeLabel(file.filename) }}
          </span>
          <span v-if="project.files.length > 3">+{{ project.files.length - 3 }}</span>
        </div>
        <div class="card-actions">
          <button :disabled="!project.project_id" @click="goToProject(project)">Graph</button>
          <button @click="goToSimulation(project)">Simulation</button>
          <button :disabled="!project.report_id" @click="goToReport(project)">Report</button>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getSimulationHistory } from '../api/simulation'

const router = useRouter()
const projects = ref([])
const loading = ref(true)

const truncateText = (text, maxLength) => {
  if (!text) return ''
  return text.length > maxLength ? `${text.slice(0, maxLength)}...` : text
}

const getSimulationTitle = (requirement) => {
  if (!requirement) return 'Untitled scenario'
  return truncateText(requirement, 58)
}

const formatSimulationId = (simulationId) => {
  if (!simulationId) return 'SIM_UNKNOWN'
  const prefix = simulationId.replace('sim_', '').slice(0, 6)
  return `SIM_${prefix.toUpperCase()}`
}

const formatRounds = (simulation) => {
  const current = simulation.current_round || 0
  const total = simulation.total_rounds || 0
  if (total === 0) return 'Not started'
  return `${current}/${total} rounds`
}

const getProgressClass = (simulation) => {
  const current = simulation.current_round || 0
  const total = simulation.total_rounds || 0
  if (total === 0 || current === 0) return 'idle'
  return current >= total ? 'done' : 'running'
}

const getFileTypeLabel = (filename) => {
  if (!filename) return 'FILE'
  return filename.split('.').pop()?.toUpperCase() || 'FILE'
}

const goToProject = (project) => {
  if (project.project_id) {
    router.push({ name: 'Process', params: { projectId: project.project_id } })
  }
}

const goToSimulation = (project) => {
  if (project.simulation_id) {
    router.push({ name: 'Simulation', params: { simulationId: project.simulation_id } })
  }
}

const goToReport = (project) => {
  if (project.report_id) {
    router.push({ name: 'Report', params: { reportId: project.report_id } })
  }
}

const loadHistory = async () => {
  try {
    loading.value = true
    const response = await getSimulationHistory(20)
    projects.value = response.success ? (response.data || []) : []
  } catch (error) {
    console.error('Failed to load workspace history:', error)
    projects.value = []
  } finally {
    loading.value = false
  }
}

onMounted(loadHistory)
</script>

<style scoped>
.history {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 32px 80px;
}

.section-kicker {
  margin: 0 0 10px;
  color: #8f5b2f;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 12px;
}

.section-heading h2 {
  margin: 0;
}

.state {
  margin-top: 18px;
  border: 1px solid rgba(23, 32, 26, 0.12);
  border-radius: 8px;
  padding: 24px;
  background: rgba(255, 253, 248, 0.72);
  color: #5c685e;
}

.history-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  margin-top: 22px;
}

.history-card {
  background: #fffdf8;
  border: 1px solid rgba(23, 32, 26, 0.12);
  border-radius: 8px;
  padding: 18px;
  min-height: 260px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.card-topline,
.card-actions,
.file-strip {
  display: flex;
  align-items: center;
}

.card-topline {
  justify-content: space-between;
  color: #69756b;
  font-size: 12px;
  font-weight: 800;
}

.run-status {
  border-radius: 999px;
  padding: 5px 8px;
  background: #ece7dc;
}

.run-status.running {
  background: #fff0cb;
  color: #85620c;
}

.run-status.done {
  background: #d7eadb;
  color: #246333;
}

.history-card h3 {
  margin: 0;
  font-size: 18px;
  line-height: 1.3;
}

.history-card p {
  margin: 0;
  color: #5c685e;
  line-height: 1.55;
}

.file-strip {
  flex-wrap: wrap;
  gap: 6px;
  margin-top: auto;
}

.file-strip span {
  border-radius: 999px;
  background: #ece7dc;
  padding: 5px 8px;
  font-size: 11px;
  font-weight: 900;
}

.card-actions {
  gap: 8px;
}

.card-actions button {
  flex: 1;
  border: 1px solid rgba(23, 32, 26, 0.16);
  border-radius: 6px;
  background: white;
  color: #17201a;
  padding: 9px 10px;
  font-weight: 800;
  cursor: pointer;
}

.card-actions button:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

@media (max-width: 980px) {
  .history-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 620px) {
  .history {
    padding-left: 18px;
    padding-right: 18px;
  }

  .history-grid {
    grid-template-columns: 1fr;
  }
}
</style>
