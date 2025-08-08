<template>
  <pre><code ref="code" class="hljs language-javascript" v-html="highlightedCode"></code></pre>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import hljs from 'highlight.js/lib/core'
import javascript from 'highlight.js/lib/languages/javascript'

hljs.registerLanguage('javascript', javascript)

const props = defineProps<{ code: string }>()

const highlightedCode = computed(() =>
  hljs.highlight(props.code, { language: 'javascript' }).value
)
</script>

<!-- ⚠️ scoped УБИРАЕМ, иначе стили не применяются -->
<style>
@import 'highlight.js/styles/github-dark.css';
</style>
