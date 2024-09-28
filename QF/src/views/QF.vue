<script setup lang="ts">
import QFinds from '@/components/QFinds.vue';
import Loader from '@/components/Loader.vue';

const props = defineProps(['st', 'in', 'ot', 'sz', 'sg'])
</script>

<template>
  <Suspense>
  <QFinds :st="props.st" :in="props.in" :ot="props.ot" :sz="props.sz" :sg="props.sg"/>
  <template #fallback><Loader style="width: 100%; height: 100dvh;"/></template>
</Suspense>
</template>