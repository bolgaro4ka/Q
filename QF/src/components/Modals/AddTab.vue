<script setup lang="ts">
import { ref } from 'vue';


const title = ref('')
const url = ref('')


function handleAddTab(e : Event) {
    const tabs = JSON.parse(localStorage.getItem('tabs') || '[]') as Array<{title: string, url: string}>;
    tabs.push({ title: title.value, url: url.value });
    localStorage.setItem('tabs', JSON.stringify(tabs));


    window.location.reload();
}

</script>

<template>
    <div class="addtab">
        <p>Имя</p>
        <input type="text" v-model="title">
        <p>URL</p>
        <input type="text" v-model="url">
        <button @click="handleAddTab">Добавить</button>
    </div>
</template>

<style lang="scss" scoped>
.addtab {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px;
    color: var(--color-text);
}</style>