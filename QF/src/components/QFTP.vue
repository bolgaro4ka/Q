<script setup lang="ts">

import { BASE_URL, FTP_ENDPOINT } from '@/config/main';
import axios from 'axios';

const raw_res = await axios.get(FTP_ENDPOINT)

const res = raw_res.data.slice(8,-1)

console.log(res)


</script>

<template>
    <div class="qftp">
        <div v-for="item in res">
            <div v-html="item[0]"></div>
            <div>{{item[1]}}</div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.qftp {
    overflow-y: scroll;
    overflow-x: hidden;
    height: 600px;
}
</style>