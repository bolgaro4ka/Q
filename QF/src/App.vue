<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <main>
    <Suspense>
    <RouterView />
  </Suspense>
  </main>
</template>

<style scoped>

</style>
