<script setup lang="ts">
import { ref, type Ref } from 'vue';
import { useRouter } from 'vue-router';

import { replaceSpecialSymbols } from '@/common/main';
const router = useRouter();

const query = ref('')
const ein : Ref<string> = ref('')

function handleClick(e : Event, mode?: string) {
    if (mode) ein.value = mode
    location.href = `/get?st=${replaceSpecialSymbols(query.value)}&in=${ein.value}&ot=0`
    // router.push(`/get?st=${query.value}&in=w`)
}

const props = defineProps(['st', 'in'])

if (props.st) query.value = props.st; ein.value = props.in
window.addEventListener('keypress', (e : KeyboardEvent) => {if (e.key == 'Enter') handleClick(e);} )


</script>

<template>
    <div class="searcher__head">
        <div class="searcher__content">
            <RouterLink to="/"><div class="circle"></div></RouterLink>
            <div class="searcher">
                <input type="text" v-model="query">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z" @click="handleClick"/></svg>
            </div>
            
        </div>
        <div class="searcher__links">
            <a :class="(ein == 'f') && 'searcher_active' " @click="(e) =>handleClick(e, 'f')">Поиск среди файлов</a>
            <a :class="(ein == 'w') && 'searcher_active' " @click="(e) =>handleClick(e, 'w')">Поиск по интернету</a>
        </div>
    </div>
</template>


<style lang="scss" scoped>
    .logo {
        background-size: 10px;
        background-image: url('@assets/logo.png');
        height: 50px;
        width: 100%;
    }

    .circle {
        width: 125px;
        height: 125px;
        border-radius: 10000px;
        border: 10px solid purple;
        position: absolute;
        z-index: 1;
    }

    .searcher__head {
        display: flex;
        justify-content: space-between;
        align-items: center;

        input {
            margin-left: 50px;
            margin-top: 50px;
            z-index: 2;
            position: relative;
            outline: none;
            background-color: #232222;
            border: none;
            border-radius: 10px 0px 0 10px;
            width: 70%;
            height: 30px;
            caret-color: var(--color-text);
            color: var(--color-text);
            padding:  0 5px;
        }
    }

    .searcher svg {
        position: relative;
        top: 10px;
        height: 30px;
        padding-right: 10px;
        background-color: #232222;
    }

    @media (min-width: 700px) {
        .searcher__head input {
            min-width: 500px;
            max-width: 500px;
        }

        
    }

    @media (max-width: 777px) {
        .searcher__head {
            display: flex;
            flex-direction: column;
            width: 100%;
            align-items: center;
            padding-bottom: 20px;
        }

        .searcher__content {
            width: 100%;
            
        }
        
    }

    .searcher__content {
        padding-top: 30px;
        padding-bottom: 60px;
        padding-left: 20px;

    }

    .searcher__links {
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding-right: 20px;
        a {
            color: var(--color-text);
        }

        a:hover {
            text-decoration: none;
            cursor: pointer;
        }
    }

    .searcher_active {
        border-bottom: 2px solid purple;
    }
</style>