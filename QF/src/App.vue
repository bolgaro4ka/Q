<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <main>
    <Suspense>
    <RouterView v-slot="{ Component }">
      <Transition name="fade" mode="out-in">
        <component :is="Component" />
      </Transition>
    </RouterView>
    <template #fallback>
      <div style="color: #8c8879;">Loading...</div>
    </template>
  </Suspense>
  </main>
</template>

<style scoped>

</style>
