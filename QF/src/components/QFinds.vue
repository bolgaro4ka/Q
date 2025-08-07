<script setup lang="ts">
import QSearcherMini from '@/components/QSearcherMini.vue';
import { REQ_ENDPOINT } from '@/config/main';
import axios from 'axios';
import { ref, type Ref } from 'vue';
import QPages from '@/components/QPages.vue';
import { getHostname, replaceAll, replaceSpecialSymbols} from '@/common/main';
import NoFound from '@/components/Base/NoFound.vue';
import QGPT from './QGPT.vue';
import Loader from './Base/Loader.vue';
import { useRoute, useRouter } from 'vue-router';
import { lang, LC_ARCHIVE_LINK, LC_SAVED, LC_SEARCH_FIELS_SAME_SIZE, LC_SEARCH_ONLY_ON_THIS_SERVER, LC_SIMULAR_FIELS, LC_SITE_MAYBE_BLOCK_RKN } from '@/locale/dict';
import { LC_JANUARY, LC_FEBRUARY, LC_MARCH, LC_APRIL, LC_MAY, LC_JUNE, LC_JULY, LC_AUGUST, LC_SEPTEMBER, LC_OCTOBER, LC_NOVEMBER, LC_DECEMBER } from '@/locale/dict';
import { watch, onMounted } from 'vue'


const route = useRoute();
const query = ref(route.query.st ? replaceSpecialSymbols(route.query.st as string) : '')

const props = defineProps(['st', 'in', 'ot', 'sz', 'sg'])

// FIRST LOAD
const g_find = ref(true)
const d_find = ref(true)

const isLoading = ref(true);

const results = ref<any[]>([])
const res_google = ref<any>(null)

/**
 * Localizes a given saved string by replacing Russian month names with their corresponding translations.
 *
 * @param {string} saved - The saved string to be localized.
 * @return {string} The localized saved string.
 */
function localizeSaved(saved: string): string {
  let s = saved
    .replace('Сохранено', LC_SAVED[lang].slice(0, LC_SAVED[lang].length-1))
    s = replaceAll(s, 'января', LC_JANUARY[lang])
    s = replaceAll(s, 'февраля', LC_FEBRUARY[lang])
    s = replaceAll(s, 'марта', LC_MARCH[lang])
    s = replaceAll(s, 'апреля', LC_APRIL[lang])
    s = replaceAll(s, 'мая', LC_MAY[lang])
    s = replaceAll(s, 'июня', LC_JUNE[lang])
    s = replaceAll(s, 'июля', LC_JULY[lang])
    s = replaceAll(s, 'августа', LC_AUGUST[lang])
    s = replaceAll(s, 'сентября', LC_SEPTEMBER[lang])
    s = replaceAll(s, 'октября', LC_OCTOBER[lang])
    s = replaceAll(s, 'ноября', LC_NOVEMBER[lang])
    s = replaceAll(s, 'декабря', LC_DECEMBER[lang])
    
  return s;
}

const raw_res = ref<any>()




// SECOND LOAD
async function fetchResults() {
  isLoading.value = true
  d_find.value = true
  g_find.value = true
  raw_res.value = await axios.post(REQ_ENDPOINT, {
    st: route.query.st ? replaceSpecialSymbols(route.query.st as string) : '',
    in: route.query.in as string,
    ot: route.query.ot as string,
    sz: route.query?.sz as string | undefined,
    sg: route.query?.sg as string | undefined
  })

  query.value = route.query.st ? replaceSpecialSymbols(route.query.st as string) : '',
  
  results.value = raw_res.value.data.obj
  raw_res.value.data.obj?.length != 0 ? d_find.value = true : d_find.value = false

  if (props.in == 'w') res_google.value = await axios.get(`https://www.googleapis.com/customsearch/v1?key=AIzaSyBTFt0SF5N-DPsRpxp8t2sur8rXmQ66sqg&cx=7369df37203b745bf&q=${replaceSpecialSymbols(route.query.st as string)}&start=${parseInt(route.query.ot as string)/10}&lr=ru-RU`).then(r => { g_find.value = true; return r}).catch(e => { g_find.value = false; return null })
  isLoading.value = false
}


onMounted(fetchResults)
watch(
  () => [route.query.st, route.query.in, route.query.ot, route.query.sz, route.query.sg],
  fetchResults,
  { deep: false }
)

const qgpt : Ref<number | null> = ref(Number(localStorage.getItem('qgpt')) != undefined ? Number(localStorage.getItem('qgpt') ) : 1)
</script>


<template>
  <div v-if="raw_res?.data?.OK">
    <QSearcherMini :st="st" :in="in" v-if="d_find || g_find"/>
    <template v-if="d_find || g_find"><QPages :ot="$props.ot" :st="st" :in="in" :cpages="raw_res.data.cpages"  /></template>
    <Suspense><QGPT :content="query" v-if="route.query.in == 'w' && qgpt != 0 && d_find && g_find" :mode="qgpt"/><template #fallback><Loader style="width: 100%; height: 100%;"/></template></Suspense>
    
    <div class="finds__wrapper">
      <div class="finds__content">
      <div class="finds">
        <div class="find google" v-if="(res_google as any)?.data?.items && props.in == 'w'" v-for="result in (res_google as any).data.items" :key="result" >
          <a :href="result.link" target="_blank"><p v-html="result.htmlTitle" class="find_url"></p></a>
          <div v-html="getHostname(result.link)" class="find_link"></div>
          <p v-html="result.htmlSnippet"  class="find_desc"></p>
        </div>
      <div v-for="result in results" :key="result" :class="`find ${props.in}_cls ${result.class}`" v-if="results">
        <template v-if="result">
          <div v-html="result.link" class="find_link"></div>
          <p v-html="result.url" class="find_url"></p>
          <div class="table" v-html="result.table"></div>
          <p v-html="result.desc"  class="find_desc"></p>
          <p v-html="result.arch?.replace('Архивная ссылка (web.archive.org)', LC_ARCHIVE_LINK[lang])" class="find_arch"></p>
          <p class="rkn__block" v-if="result.class == 'rkn'">{{ LC_SITE_MAYBE_BLOCK_RKN[lang] }}</p>
          <div v-if="props.in == 'f'" class="find__links">
            <RouterLink :to="result.simular_url+'&ot=0'">{{ LC_SIMULAR_FIELS[lang] }}</RouterLink>
            <RouterLink :to="result.also_url+'&ot=0'">{{ LC_SEARCH_FIELS_SAME_SIZE[lang] }}</RouterLink>
            <RouterLink :to="result.search_url+'&ot=0'" v-if="result.search_url">{{ LC_SEARCH_ONLY_ON_THIS_SERVER[lang] }}</RouterLink>
          </div>
          <div class="find__saveWrapper" v-if="props.in == 'w'">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M840-680v480q0 33-23.5 56.5T760-120H200q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h480l160 160Zm-80 34L646-760H200v560h560v-446ZM480-240q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35ZM240-560h360v-160H240v160Zm-40-86v446-560 114Z"/></svg>
            <p v-html="localizeSaved(result.saved)" class="find_saved"></p>
          </div>
        </template>
      </div>
      </div>
    </div>
    </div>
    <QPages :ot="$props.ot" :st="st" :in="in" :cpages="raw_res.data.cpages"  v-if="d_find || g_find" :bottom="true" style="margin-top: 20px;"/>
  </div>
  <div v-else-if="isLoading" style="width: 100vw; height: 100dvh;">
    <Loader/>
  </div>
  <div v-else>
    <QSearcherMini :st="st" :in="in"/>
    <Suspense><QGPT :content="props.st" v-if="props.in == 'w'"/><template #fallback><Loader style="width: 100%; height: 100%;"/></template></Suspense>
    <NoFound :err="raw_res?.data?.error"/>
  </div>
  <div v-if="!d_find && !g_find">
    <QSearcherMini :st="st" :in="in"/>
    <Suspense><QGPT :content="props.st" v-if="props.in == 'w'"/><template #fallback><Loader style="width: 100%; height: 100%;"/></template></Suspense>
    <NoFound :err="'not found or big number of pages'"/>
  </div>
</template>

<style scoped lang="scss">
.find__links {
  display: flex;
  gap: 10px;
}
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

table {
  background-color: #99c3ff;
}

@media screen and (max-width: 739px) {
  .f_cls .table  {
    display: flex;
    font-size: calc( ( 1vh) * .86 );

    
  }

  .f_cls * {
    word-wrap: break-word;
  }
  
}

@media screen and (min-width: 739px) {
  .f_cls {
    width: 722px;
    max-width: 722px;
    min-width: 721px;
  }
  
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

@media screen and (max-width: 600px) {
  .find {
    max-width: 90dvw;
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
