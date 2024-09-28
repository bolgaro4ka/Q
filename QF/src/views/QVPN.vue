<script lang="ts" setup>
import { BASE_URL, VPN_ENDPOINT } from '@/config/main';
import axios from 'axios';
import { ref } from 'vue';
import { decodeUTF8 } from '@/common/main';
import NoFound from '@/components/NoFound.vue';


const props = defineProps(['url'])
const error= ref(false)
const raw_page = await axios.post(VPN_ENDPOINT, {
    url: props.url
}).catch((e) => {
    error.value = true;
})

const page = raw_page?.data?.html

const url = ref(props.url)


function changePath() {
    location.href = `/qvpn?url=${url.value}`
}
</script>

<template>
    <div >
        <div class="qvpn">
            <RouterLink to="/" style="display: flex;"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="purple"><path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z"/></svg></RouterLink>
            <p>QVPN</p>
            <input type="text" class="qvpn-input" v-model="url" @keypress.enter="changePath()">
        </div>
        <div v-html="page" style="background-color: white; height: 100vh;" v-if="!error"></div>
        <NoFound v-if="error" err="страница не найдена! Проверьте привально ли вы указали URL" />
    </div>
</template>

<style lang="scss" scoped>
.qvpn {
    position: fixed !important;
    top: 10px !important;
    left: 10px !important;
    z-index: 2147483647 !important;
    opacity: 0.5 !important;
    width: 50% !important;
    display: flex !important;
    gap: 10px !important;
    padding: 10px !important;
    border-radius: 10px !important;
    align-items: center !important;

    p {
        background-color: purple !important;
        padding: 5px !important;
        border-radius: 5px !important;
        color: white !important;
    }

}

.qvpn-input {
    color: black !important;
    border: 1px solid purple !important;
    width: 100%;
    outline: none !important;
}

.qvpn:hover, .qvpn-input:hover {
    opacity: 1 !important;
    outline: none !important;
    backdrop-filter: blur(10px) !important;
}

.qvpn:focus-within {
    outline: none !important;
    opacity: 1 !important;
    backdrop-filter: blur(10px) !important;
}

</style>