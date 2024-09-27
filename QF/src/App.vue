<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Loader from '@/components/Loader.vue';
</script>

<template>
  <main>
    <Suspense>
    <RouterView></RouterView>
    <template #fallback>
      <Loader/>
    </template>
  </Suspense>
  </main>
</template>

<style scoped>

</style>
