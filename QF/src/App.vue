<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <main>
    <Suspense>
    <RouterView></RouterView>
    <template #fallback>
      <div>Loading...</div>
    </template>
  </Suspense>
  </main>
</template>

<style scoped>

</style>
