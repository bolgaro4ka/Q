<script setup lang="ts">
import { GPT_ENDPOINT } from '@/config/main';
import { lang, LC_QGPT_NOT_ANSWER, LC_VHTML_ANSWER_OF_QGPT } from '@/locale/dict';
import axios from 'axios';

import { marked } from 'marked';
import { ref, watch } from 'vue';

const props = defineProps(['content', 'mode'])

const raw_res = await axios.post(GPT_ENDPOINT, {
    content: props.content,
    chatgpt_api_key: props.mode == 2 ? localStorage.getItem('openai_key') : ''
})

const res = ref(marked(raw_res.data.res))

watch(
    () => props.content,
    async () => {
        const raw_res = await axios.post(GPT_ENDPOINT, {
            content: props.content,
            chatgpt_api_key: props.mode == 2 ? localStorage.getItem('openai_key') : ''
        })
        res.value = marked(raw_res.data.res)
    }
)
</script>


<template>
 <div class="qgpt-container">
    
    <div class="qgpt">
        <h3 v-html="LC_VHTML_ANSWER_OF_QGPT[lang]"></h3>
        <p v-html="res" v-if="res"></p>
        <p v-else>{{ LC_QGPT_NOT_ANSWER[lang] }}</p>
    </div>
</div>
</template>

<style lang="scss" scoped>
.qgpt {
    border: none;
    border-radius: 10px;
    background-color: var(--color-secondary);
    background-blend-mode: screen;
	background:
		linear-gradient(limegreen, transparent),
		linear-gradient(90deg, skyblue, transparent),
		linear-gradient(-90deg, coral, transparent);
    background-size: 400% 400%;
    animation: gradient-animation 20s ease infinite;
    
    color: white;
    padding: 10px;
    margin: 15px 20px;
}

.qgpt-container {
    margin: 0 auto;
    max-width: 1570px;
}

@keyframes gradient-animation {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}


</style>

