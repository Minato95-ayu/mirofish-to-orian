<template>
  <section class="workbench-panel">
    <div class="panel-title">
      <p>Step 01</p>
      <h2>Build memory graph</h2>
      <span :class="['status', statusTone]">{{ statusText }}</span>
    </div>

    <div class="summary-grid">
      <article>
        <span>Project</span>
        <strong>{{ projectData?.project_id || 'Creating...' }}</strong>
      </article>
      <article>
        <span>Graph</span>
        <strong>{{ projectData?.graph_id || 'Not ready yet' }}</strong>
      </article>
      <article>
        <span>Nodes</span>
        <strong>{{ nodeCount }}</strong>
      </article>
      <article>
        <span>Edges</span>
        <strong>{{ edgeCount }}</strong>
      </article>
    </div>

    <div class="progress-card">
      <h3>{{ headline }}</h3>
      <p>{{ detailMessage }}</p>
      <div class="progress-track">
        <span :style="{ width: `${progressValue}%` }"></span>
      </div>
    </div>

    <div v-if="projectData?.ontology" class="ontology-card">
      <h3>Generated schema</h3>
      <div class="tag-list">
        <span v-for="entity in entityTypes" :key="entity.name || entity">
          {{ entity.name || entity }}
        </span>
      </div>
    </div>

    <div class="log-card">
      <h3>Activity</h3>
      <div class="log-list">
        <p v-if="!systemLogs?.length">Orion is waiting for the first backend update.</p>
        <p v-for="(log, index) in systemLogs?.slice(-8)" :key="index">
          <span>{{ log.time }}</span>
          {{ log.msg }}
        </p>
      </div>
    </div>

    <button class="primary-action" :disabled="currentPhase < 2" @click="$emit('next-step')">
      Continue to environment setup
    </button>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentPhase: Number,
  projectData: Object,
  ontologyProgress: Object,
  buildProgress: Object,
  graphData: Object,
  systemLogs: Array
})

defineEmits(['next-step'])

const nodeCount = computed(() => props.graphData?.node_count || props.graphData?.nodes?.length || 0)
const edgeCount = computed(() => props.graphData?.edge_count || props.graphData?.edges?.length || 0)

const entityTypes = computed(() => {
  const ontology = props.projectData?.ontology || {}
  return ontology.entity_types || ontology.entities || []
})

const progressValue = computed(() => {
  if (props.currentPhase >= 2) return 100
  if (props.currentPhase === 1) return props.buildProgress?.progress || 50
  if (props.currentPhase === 0) return 25
  return 5
})

const headline = computed(() => {
  if (props.currentPhase >= 2) return 'Graph is ready'
  if (props.currentPhase === 1) return 'Building graph memory'
  if (props.currentPhase === 0) return 'Extracting ontology'
  return 'Starting workspace'
})

const detailMessage = computed(() => {
  return props.buildProgress?.message || props.ontologyProgress?.message || 'Upload accepted. Orion is preparing the knowledge layer.'
})

const statusText = computed(() => props.currentPhase >= 2 ? 'Ready' : 'Processing')
const statusTone = computed(() => props.currentPhase >= 2 ? 'ready' : 'processing')
</script>

<style scoped>
.workbench-panel {
  height: 100%;
  overflow-y: auto;
  padding: 28px;
  background: #fffdf8;
}

.panel-title {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px 16px;
  align-items: start;
  margin-bottom: 22px;
}

.panel-title p {
  grid-column: 1 / -1;
  color: #8f5b2f;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.panel-title h2 {
  margin: 0;
  font-size: 30px;
}

.status {
  border-radius: 999px;
  padding: 8px 10px;
  font-weight: 900;
  font-size: 12px;
  background: #ece7dc;
}

.status.ready {
  background: #d7eadb;
  color: #246333;
}

.status.processing {
  background: #fff0cb;
  color: #85620c;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.summary-grid article,
.progress-card,
.ontology-card,
.log-card {
  border: 1px solid rgba(23, 32, 26, 0.12);
  border-radius: 8px;
  background: white;
  padding: 16px;
}

.summary-grid span {
  display: block;
  color: #69756b;
  font-size: 12px;
  font-weight: 800;
  margin-bottom: 8px;
}

.summary-grid strong {
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.progress-card,
.ontology-card,
.log-card {
  margin-top: 14px;
}

.progress-card h3,
.ontology-card h3,
.log-card h3 {
  margin: 0 0 8px;
}

.progress-card p {
  color: #5c685e;
  line-height: 1.5;
}

.progress-track {
  height: 10px;
  border-radius: 999px;
  background: #eee8dd;
  overflow: hidden;
  margin-top: 16px;
}

.progress-track span {
  display: block;
  height: 100%;
  border-radius: inherit;
  background: #8f5b2f;
  transition: width 0.3s ease;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-list span {
  border-radius: 999px;
  background: #ece7dc;
  padding: 7px 10px;
  font-weight: 800;
  font-size: 12px;
}

.log-list {
  display: grid;
  gap: 8px;
  color: #5c685e;
}

.log-list p {
  margin: 0;
  line-height: 1.45;
}

.log-list span {
  color: #8f5b2f;
  font-family: 'JetBrains Mono', monospace;
  margin-right: 8px;
}

.primary-action {
  width: 100%;
  margin-top: 16px;
  border: 0;
  border-radius: 8px;
  padding: 15px;
  background: #17201a;
  color: white;
  font-weight: 900;
  cursor: pointer;
}

.primary-action:disabled {
  background: #d9d3c7;
  color: #777064;
  cursor: not-allowed;
}
</style>
