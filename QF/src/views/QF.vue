<script setup lang="ts">
import QSearcherMini from '@/components/QSearcherMini.vue';
import { REQ_ENDPOINT } from '@/config/main';
import axios from 'axios';
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { onBeforeRouteUpdate } from 'vue-router';
import iconv from 'iconv-lite';
import QPages from '@/components/QPages.vue';
import { replaceSpecialSymbols} from '@/common/main';
import NoFound from '@/components/NoFound.vue';

const route = useRoute()
const props = defineProps(['st', 'in', 'ot', 'sz', 'sg'])

console.log(REQ_ENDPOINT)

console.log(props.in, props.st)

console.log(replaceSpecialSymbols(props.st))
const g_find = ref(true)
const d_find = ref(true)

const raw_res = await axios.post(REQ_ENDPOINT, {
  st: replaceSpecialSymbols(props.st),
  in: props.in,
  ot: props.ot,
  sz: props?.sz,
  sg: props?.sg
})

if (raw_res.data.obj?.length != 0) d_find.value = true
else d_find.value = false

const res_google = await axios.get(`https://www.googleapis.com/customsearch/v1?key=AIzaSyBTFt0SF5N-DPsRpxp8t2sur8rXmQ66sqg&cx=7369df37203b745bf&q=${replaceSpecialSymbols(props.st)}&start=${parseInt(props.ot)/10}&lr=ru-RU`).catch(e => g_find.value = false)

const results = raw_res.data.obj

function getHostname(url : string) {
  return new URL(url).hostname
}





</script>


<template>
  <div v-if="raw_res.data.OK">
    <QSearcherMini :st="st" :in="in" v-if="d_find || g_find"/>
    <QPages :ot="$props.ot" :st="st" :in="in" :cpages="raw_res.data.cpages" v-if="d_find || g_find" />
    <div class="finds__wrapper">
      <div class="finds__content">

      <div class="finds">

        <div class="find google" v-if="(res_google as any)?.data?.items && props.in == 'w'" v-for="result in (res_google as any).data.items" :key="result" >
          <a :href="result.link" target="_blank"><p v-html="result.htmlTitle" class="find_url"></p></a>
          <div v-html="getHostname(result.link)" class="find_link"></div>
          
          <p v-html="result.htmlSnippet"  class="find_desc"></p>

        </div>


      <div v-for="result in results" :key="result" :class="`find ${props.in}_cls ${result.class}`">
        <template v-if="result">
          <div v-html="result.link" class="find_link"></div>
          <p v-html="result.url" class="find_url"></p>
          <div class="table" v-html="result.table"></div>
          <p v-html="result.desc"  class="find_desc"></p>
          <p v-html="result.arch" class="find_arch"></p>
          <p class="rkn__block" v-if="result.class == 'rkn'">Возможно сайт заблокирован великим и не подражаемым РКН</p>
          <div v-if="props.in == 'f'"><a :href="result.simular_url+'&ot=0'">[похожие файлы]</a><a :href="result.also_url+'&ot=0'">[найти файлы такого же размера]</a><a :href="result.search_url+'&ot=0'" v-if="result.search_url">[искать только на этом сервере]</a></div>
          <div class="find__saveWrapper" v-if="props.in == 'w'"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M840-680v480q0 33-23.5 56.5T760-120H200q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h480l160 160Zm-80 34L646-760H200v560h560v-446ZM480-240q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35ZM240-560h360v-160H240v160Zm-40-86v446-560 114Z"/></svg><p v-html="result.saved" class="find_saved"></p></div>
        </template>
      </div>
      </div>
    </div>
    </div>
    <QPages :ot="$props.ot" :st="st" :in="in" :cpages="raw_res.data.cpages"  v-if="d_find || g_find" />
  </div>
  <div v-else>
    <QSearcherMini :st="st" :in="in"/>
    <NoFound :err="raw_res.data.error"/>
  </div>
  <div v-if="!d_find && !g_find">
    <QSearcherMini :st="st" :in="in"/>
    <NoFound :err="'not found or big number of pages'"/>
  </div>
</template>

<style scoped lang="scss">

.finds__wrapper {
  margin: 0 auto;
  max-width: 2000px;
}

.f_cls .find_link * {
  color: #99c3ff;
  text-decoration: none;
}

.f_cls .find_link *:hover {
  text-decoration: underline;
}

.f_cls .find_link *:visited {
  color: #c58af9;
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

.rkn__block {
  color: red;
}

.table table * {
  font-size: 7px;
}

.f_cls {
  width: 722px;
  max-width: 722px;
  min-width: 721px;
}

.table tbody * {
  color: green !important;
}

.table * {
  color: white;
}

.google {
  border-radius: 130px;
  border-image: var(--google-gradient) 30;
  border-style: solid;
  border-width: 2px;
  width: 500px;
  .find_desc {
    color: var(--color-text);
  }

  .find_link {
    color: white;;
  }
}




</style>

<style scoped>

</style>
