<script setup lang="ts">
import { FTP_ENDPOINT } from '@/config/main';
import axios from 'axios';

// Get list of FTP Servers
const res = await axios.get(FTP_ENDPOINT).then(raw_res => raw_res.data.slice(7,-1)).catch(e => [])
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
    width: 400px;
    padding: 10px;
}
</style>