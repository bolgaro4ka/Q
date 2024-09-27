<script setup lang="ts">
import QSearcherMain from '@/components/QSearcherMain.vue';


</script>

<template>
  <div class="home">
    <Suspense>
      <QSearcherMain />
      <template #fallback>
        <div>Loading...</div>
      </template>
    </Suspense>
  </div>
</template>
