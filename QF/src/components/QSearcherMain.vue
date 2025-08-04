<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue';
import { useRouter } from 'vue-router';

import { replaceSpecialSymbols } from '@/common/main';
import Modal from './Base/Modal.vue';
import PopupSettings from './Modals/PopupSettings.vue';
import QFTP from './QFTP.vue';
import Loader from './Base/Loader.vue';
import AddTab from './Modals/AddTab.vue';
import { lang, LC_ADD_TAB, LC_LIST_OF_FTP_SERVERS, LC_QVPN, LC_SEARCH_IN_FIELS, LC_SEARCH_IN_INTERNET, LC_SETTINGS_Q, LC_VHTML_ABOUT } from '@/locale/dict';

const query = ref('')
const mode : Ref<string> = ref('')

onMounted(() => {
    mode.value = 'w'
})

const isSettingsPopupOpen = ref(false)
const isFTPPopupOpen = ref(false)
const isAddTabOpen = ref(false)


function handleClick(e : Event) {
    if (mode.value != 'q') location.href = `/get?st=${replaceSpecialSymbols(query.value)}&in=${mode.value}&ot=0`
    if (mode.value == 'q') location.href = `/qvpn?url=${query.value}`
    // router.push(`/get?st=${query.value}&in=w`)
}

function handleAddTab(e : Event) {
    isAddTabOpen.value = true
}

function handleDeleteTab(e : Event) {
    const Ltabs = JSON.parse(localStorage.getItem('tabs') || '[]') as Array<{title: string, url: string}>;
    Ltabs.splice(Number((e.target as HTMLButtonElement).dataset.index), 1)
    localStorage.setItem('tabs', JSON.stringify(Ltabs));

    tabs.value = Ltabs
}

window.addEventListener('keypress', (e : KeyboardEvent) => {if (e.key == 'Enter') handleClick(e);} )

onMounted(() => {
    document.body.style.backgroundImage = `url(${localStorage.getItem('url') || 'https://scientificrussia.ru/images/i/31qi-full.jpg'})`;
})


const tabs = ref(localStorage.getItem('tabs') ? JSON.parse(localStorage.getItem('tabs') as string) : []) // [{"title": "title", "url": "url"}]



</script>

<template>
    <div class="searcher__head">
        <div class="searcher__content">
            <div class="circle"></div>
            <div class="searcher">
                <input type="text" v-model="query" autofocus>
                <div  @click="handleClick" class="searcher_svg"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z"/></svg></div>
            </div>
            <div class="searcher__tabs">

                <a v-for="tab in tabs" :href="tab.url" target="_blank" class="searcher__tab" @click.right.prevent="handleDeleteTab">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M160-240h640v-320H520v-160H160v480Zm0 80q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm0-80v-480 480Z"/></svg>
                    <p>{{tab.title}}</p>
                </a>
                <div @click="handleAddTab" class="searcher__tab">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h240v80H200v560h560v-240h80v240q0 33-23.5 56.5T760-120H200Zm440-400v-120H520v-80h120v-120h80v120h120v80H720v120h-80Z"/></svg>
                    <p style="text-align: center; color: var(--color-text);">{{ LC_ADD_TAB[lang] }}</p>
                </div>
            </div>
            
        </div>
        <div class="searcher__links">
            <a :class="(mode == 'f') && 'searcher_active' " @click="mode = 'f'">{{ LC_SEARCH_IN_FIELS[lang] }}</a>
            <a :class="(mode == 'w') && 'searcher_active' " @click="mode = 'w'">{{ LC_SEARCH_IN_INTERNET[lang] }}</a>
            <a :class="(mode == 'q') && 'searcher_active' " @click="mode = 'q'">{{ LC_QVPN[lang] }}</a>
        </div>
        <div class="searcher__edit" @click="isSettingsPopupOpen = true">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M200-200h57l391-391-57-57-391 391v57Zm-80 80v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm640-584-56-56 56 56Zm-141 85-28-29 57 57-29-28Z"/></svg>
        </div>
        <div  @click="isFTPPopupOpen = true" class="searcher__ftp">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M280-600v-80h560v80H280Zm0 160v-80h560v80H280Zm0 160v-80h560v80H280ZM160-600q-17 0-28.5-11.5T120-640q0-17 11.5-28.5T160-680q17 0 28.5 11.5T200-640q0 17-11.5 28.5T160-600Zm0 160q-17 0-28.5-11.5T120-480q0-17 11.5-28.5T160-520q17 0 28.5 11.5T200-480q0 17-11.5 28.5T160-440Zm0 160q-17 0-28.5-11.5T120-320q0-17 11.5-28.5T160-360q17 0 28.5 11.5T200-320q0 17-11.5 28.5T160-280Z"/></svg>
        </div>
    </div>

    <div class="q__bottom">
        <div class="author">
            <p v-html="LC_VHTML_ABOUT[lang]"></p>
        </div>
    </div>

    <Teleport to="body">
        <Modal v-if="isSettingsPopupOpen" @close="isSettingsPopupOpen = false"  :title="LC_SETTINGS_Q[lang]">
            <PopupSettings />
        </Modal>
    </Teleport>

    <Teleport to="body">
        <Modal v-if="isFTPPopupOpen" @close="isFTPPopupOpen = false"  :title="LC_LIST_OF_FTP_SERVERS[lang]">
            <Suspense>
                <QFTP />
                <template #fallback><Loader style="height: 400px;"/></template>
            </Suspense>
        </Modal>
    </Teleport>

    <Teleport to="body">
        <Modal v-if="isAddTabOpen" @close="isAddTabOpen = false"  :title="LC_ADD_TAB[lang]">
            <Suspense>
                <AddTab />
                <template #fallback><Loader style="height: 400px;"/></template>
            </Suspense>
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
    background-color: var(--color-secondary);
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
        border: 100px solid var(--color-main);
        position: absolute;
        z-index: 1;
    }

    @media screen and (max-width: 700px) {
        .circle {
            width: calc( ( 1vh + 1vw ) * 20 );
            height: calc( ( 1vh + 1vw ) * 20 );
        }

        .searcher {
            top: calc( ( 1vh + 1vw ) * 11 ) !important;
            left: 25vw;
            width: 70vw;
            z-index: 2;
            display: flex;
            position: absolute;
        }

        
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
            background-color: var(--color-secondary);
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
        background-color: var(--color-secondary);
    }

    .searcher_svg {
        position: relative;
        cursor: pointer;
    }



    @media (max-width: 800px) {
        .circle {
            border: 50px solid var(--color-main);
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
        border-bottom: 2px solid var(--color-main);
    }

    .searcher__ftp {
        position: absolute;
        top: 10px;
        left: 10px;
    }

    .searcher__tabs {
        position: absolute;
        top: 60%;
        left: 60%;
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: center;
        max-width: 400px;
    }

    .searcher__tab {
        display: flex;
        flex-direction: column;
        align-items: center;
        cursor: pointer;

    }

    @media screen and (max-width: 700px) {
        .searcher__tabs {
            top: 40%;
            left: calc(0);
            max-width: none;
            width: 100%;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        
    }
</style>
