<script setup lang="ts">
import { GPT_ENDPOINT } from '@/config/main';
import axios from 'axios';
import { marked } from 'marked';

const props = defineProps(['content'])

const raw_res = await axios.post(GPT_ENDPOINT, {
    content: props.content
})

const res = marked(raw_res.data.res)
</script>


<template>
 <div class="qgpt-container">
    
    <div class="qgpt">
        <h3>Ответ <span style="color: #f6d614;">Q</span><span style="color: #53a7c8;">G</span><span style="color: #f07d02;">P</span><span style="color: #ffb6e6;">T</span>:</h3>
        <p v-html="res" v-if="res"></p>
        <p v-else>QGPT не отвечает. Попробуйте перезагрузить страницу</p>
    </div>
</div>
</template>

<style lang="scss" scoped>
.qgpt {
    border: none;
    border-radius: 10px;
    background-color: #232222;
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

