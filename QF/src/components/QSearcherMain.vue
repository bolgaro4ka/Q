<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue';
import { useRouter } from 'vue-router';

import { replaceSpecialSymbols } from '@/common/main';
import Modal from './Modal.vue';
import PopupSettings from './PopupSettings.vue';
import QFTP from './QFTP.vue';
const router = useRouter();

const query = ref('')
const mode : Ref<string> = ref('')

onMounted(() => {
    mode.value = 'w'
})

const isSettingsPopupOpen = ref(false)
const isFTPPopupOpen = ref(false)


function handleClick(e : Event) {
    if (mode.value != 'q') location.href = `/get?st=${replaceSpecialSymbols(query.value)}&in=${mode.value}&ot=0`
    if (mode.value == 'q') location.href = `/qvpn?url=${query.value}`
    // router.push(`/get?st=${query.value}&in=w`)
}

window.addEventListener('keypress', (e : KeyboardEvent) => {if (e.key == 'Enter') handleClick(e);} )

onMounted(() => {
    const background = localStorage.getItem('url')
    if (background) {
        document.body.style.backgroundImage = `url(${background})`
    }

    if (background == undefined) {
        document.body.style.backgroundImage = `url(https://scientificrussia.ru/images/i/31qi-full.jpg)`
    }
})

</script>

<template>
    <div class="searcher__head">
        <div class="searcher__content">
            <div class="circle"></div>
            <div class="searcher">
                <input type="text" v-model="query">
                <div  @click="handleClick" class="searcher_svg"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z"/></svg></div>
            </div>
            
        </div>
        <div class="searcher__links">
            <a :class="(mode == 'f') && 'searcher_active' " @click="mode = 'f'; console.log(mode)">Поиск среди файлов</a>
            <a :class="(mode == 'w') && 'searcher_active' " @click="mode = 'w'; console.log(mode)">Поиск по интернету</a>
            <a :class="(mode == 'q') && 'searcher_active' " @click="mode = 'q'; console.log(mode)">QVPN (только URL)</a>
        </div>
        <div class="searcher__edit" @click="isSettingsPopupOpen = true">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M200-200h57l391-391-57-57-391 391v57Zm-80 80v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm640-584-56-56 56 56Zm-141 85-28-29 57 57-29-28Z"/></svg>
        </div>
        <div  @click="isFTPPopupOpen = true">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M280-600v-80h560v80H280Zm0 160v-80h560v80H280Zm0 160v-80h560v80H280ZM160-600q-17 0-28.5-11.5T120-640q0-17 11.5-28.5T160-680q17 0 28.5 11.5T200-640q0 17-11.5 28.5T160-600Zm0 160q-17 0-28.5-11.5T120-480q0-17 11.5-28.5T160-520q17 0 28.5 11.5T200-480q0 17-11.5 28.5T160-440Zm0 160q-17 0-28.5-11.5T120-320q0-17 11.5-28.5T160-360q17 0 28.5 11.5T200-320q0 17-11.5 28.5T160-280Z"/></svg>
        </div>
    </div>

    <div class="q__bottom">
        <div class="author">
            <p>Сделано <a href="https://github.com/bolgaro4ka">bolgaro4ka</a> <a href="https://t.me/papyas_07">(telegram)</a> на сервере и сети доменов <a href="https://github.com/Paia1nik">Paia1nik`а</a> <a href="https://t.me/Paia1nik">(telegram)</a> /// <a href="https://github.com/bolgaro4ka/Q">Этот проект на GitHub</a> /// <a href="https://github.com/bolgaro4ka/Q/blob/main/LICENSE">Лицензия</a></p>
        </div>
    </div>

    <Teleport to="body">
        <Modal v-if="isSettingsPopupOpen" @close="isSettingsPopupOpen = false"  title="Настройки Q">
            <PopupSettings />
        </Modal>
    </Teleport>

    <Teleport to="body">
        <Modal v-if="isFTPPopupOpen" @close="isFTPPopupOpen = false"  title="Список FTP серверов Q">
            <QFTP />
        </Modal>
    </Teleport>


    
</template>


<style lang="scss" scoped>
.searcher__edit {
    position: fixed;
    bottom: 40px;
    right: 20px;
    height: 40px;
    width: 40px;
    border-radius: 10000px;
    background-color: #232222;
    text-align: center;
    display: flex;
    z-index: 30;
    justify-content: center;
    align-items: center;
    color: var(--color-text);
}
    .q__bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: fit-content;
        text-align: center;
        display: flex;
        z-index: 30;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(10px);
        color: var(--color-text);
    }

    .logo {
        background-size: 10px;
        background-image: url('@assets/logo.png');
        height: 50px;
        width: 100%;
    }

    .circle {
        width: calc( ( 1vh + 1vw ) * 30 );
        height: calc( ( 1vh + 1vw ) * 30 );
        border-radius: 10000px;
        border: 100px solid purple;
        position: absolute;
        z-index: 1;
    }

    .searcher {
        top: calc( ( 1vh + 1vw ) * 15 );
            left: 25vw;
            width: 70vw;
            z-index: 2;
            display: flex;
            position: absolute;
    }

    .searcher__head {
        display: flex;
        width: 100%;
        
        padding-right: 10px;
        justify-content: space-between;
        align-items: center;

        input {
           
            outline: none;
            background-color: #232222;
            border: none;
            border-radius: 10px 0px 0 10px;
            width: 90%;
            font-size: 18px;
            height: 40px;
            caret-color: var(--color-text);
            color: var(--color-text);
            padding:  0 5px;
        }
    }

    .searcher svg {
        
        height: 40px;
        padding-right: 10px;
        background-color: #232222;
    }

    .searcher_svg {
        position: relative;
        cursor: pointer;
    }



    @media (max-width: 800px) {
        .circle {
            border: 50px solid purple;
        }
        
    }

    @media (max-width: 700px) {
        .searcher__links {
            position: absolute;
            top: calc( ( 1vh + 1vw ) * 35 );
            left: calc( ( 50vw - 65px ) );
        }
        
    }

    @media screen and (max-width: 820px) {
        .searcher__edit {
            bottom: 60px;
            
        }
    }

    @media screen and (max-width: 420px) {
        .searcher__edit {
            bottom: 80px;
            
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
        padding-top: 10px;
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