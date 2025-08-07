<script setup lang="ts">
import { reload } from '@/common/route';
import { lang, LC_ADD, LC_MAX_TABS_ERROR, LC_NEW_TAB, LC_TITLE, LC_URL_NOT_SPECIFIED_ERROR } from '@/locale/dict';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();


const title = ref('')
const url = ref('')

const status = ref(LC_ADD[lang])


function handleAddTab(e : Event) {
    if (url.value.length == 0) return status.value = LC_URL_NOT_SPECIFIED_ERROR[lang]
    const tabs = JSON.parse(localStorage.getItem('tabs') || '[]') as Array<{title: string, url: string}>;
    if (tabs.length > 8) return status.value = LC_MAX_TABS_ERROR[lang]
    tabs.push({ title: title.value ? title.value : LC_NEW_TAB[lang], url: url.value });
    localStorage.setItem('tabs', JSON.stringify(tabs));


    reload(router);
}

</script>

<template>
    <div class="addtab">
        <p>{{ LC_TITLE[lang] }}</p>
        <input type="text" v-model="title" @click="status=LC_ADD[lang]">
        <p>URL</p>
        <input type="text" v-model="url" @click="status=LC_ADD[lang]">
        <button @click="handleAddTab($event); ">{{ status }}</button>
    </div>
</template>

<style lang="scss" scoped>
.addtab {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px;
    color: var(--color-text);

    button {
        background-color: var(--color-main);
        color: var(--color-heading);
        border: none;
        padding: 10px;
        border-radius: 10px;
    }

    input {
        background-color: var(--color-background);
        border: none;
        color: var(--color-heading);
        outline: none;
        padding: 5px 10px;
        border-radius: 10px;
    }
}
</style>