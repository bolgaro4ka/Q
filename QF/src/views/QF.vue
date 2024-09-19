<script setup lang="ts">
import QSearcherMini from '@/components/QSearcherMini.vue';
import { REQ_ENDPOINT } from '@/config/main';
import axios from 'axios';
import { watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { onBeforeRouteUpdate } from 'vue-router';

const route = useRoute()
const props = defineProps(['st', 'in'])

console.log(REQ_ENDPOINT)
const raw_res = await axios.post(REQ_ENDPOINT, {
  st: props.st,
  in: props.in
})


const results = raw_res.data.obj

</script>


<template>
  <QSearcherMini :st="st" :in="in"/>
  <div class="finds__wrapper">
    <div class="finds__content">
    <div class="finds">
    <div v-for="result in results" :key="result" class="find" :class="result.class">
      <div v-html="result.link" class="find_link"></div>
      <p v-html="result.url" class="find_url"></p>
      <p v-html="result.desc"  class="find_desc"></p>
      <p v-html="result.arch" class="find_arch"></p>
      <div class="find__saveWrapper"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M840-680v480q0 33-23.5 56.5T760-120H200q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h480l160 160Zm-80 34L646-760H200v560h560v-446ZM480-240q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35ZM240-560h360v-160H240v160Zm-40-86v446-560 114Z"/></svg><p v-html="result.saved" class="find_saved"></p></div>
      
    </div>
    </div>
  </div>
  </div>
</template>

<style scoped lang="scss">

.finds__wrapper {
  margin: 0 auto;
  max-width: 2000px;
}

.finds {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: center;
}

.find {
  max-width: 500px;
  word-wrap: break-word;
  padding: 10px;
  border-radius: 10px;
  .desc_p {
    text-wrap:wrap;
    word-wrap: break-word;
    display: block;
  }

  
}

.rkn {
  border: 2px solid red;
}

.arch {
  border: 2px solid brown;
}

.link {
  border: 2px solid gray;
}

b {
  font-weight: 900;
}



.find_desc *:not(a) {
  color: var(--color-text);
}

.find__saveWrapper {
  display: flex;
  gap: 10px;
}

.cache_p font {
  color: var(--color-text) !important;
}



</style>
