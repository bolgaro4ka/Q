<script setup lang="ts">
import { exportConfig, importConfig } from '@/common/configs';
import { reload } from '@/common/route';
import { applySettings } from '@/common/theme';
import { lang, LC_API_KEY_OPENAI, LC_APPLY, LC_BASE_COLOR, LC_CUSTOMIZATION, LC_DONT_USE_AI, LC_EXPORT, LC_IMPORT, LC_IMPORT_EXPORT, LC_IMPORT_EXPORT_RECOMENDATION, LC_LANGUAGE, LC_QGPT_SETTINGS, LC_RESET_SETTINGS, LC_RESETED, LC_SAVE_AND_APPLY, LC_SAVED, LC_SECONDARY_COLOR, LC_USE_CHATGPT, LC_USE_QGPT, LC_WALLAPER } from '@/locale/dict';
import { ref, type Ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Elements
// Save btn
const button : Ref<HTMLButtonElement | null> = ref(null)
// Recovery btn
const Rbutton : Ref<HTMLButtonElement | null> = ref(null)


// Base Settings
const url : Ref<string | null> = ref(localStorage.getItem('url') == undefined ? 'https://scientificrussia.ru/images/i/31qi-full.jpg' : localStorage.getItem('url'))
const qgpt : Ref<number | null> = ref(Number(localStorage.getItem('qgpt')) != undefined ? Number(localStorage.getItem('qgpt')) : 1)
const openai_key : Ref<string | null> = ref(localStorage.getItem('openai_key') ? localStorage.getItem('openai_key') : '')
const color1 : Ref<string | null> = ref(localStorage.getItem('color1') ? localStorage.getItem('color1') : '#800080')
const color2 : Ref<string | null> = ref(localStorage.getItem('color2') ? localStorage.getItem('color2') : '#232222')

// Language settings
const Llang : Ref<string | null> = ref(lang)

// Raw Config
const config : Ref<string | null> = ref('')

// Windows activators
const isShowImportActions : Ref<boolean> = ref(false)

// Events
const emits = defineEmits(['close'])

applySettings();

function saveSettings(e : MouseEvent) {
    localStorage.setItem('url', url.value as string)
    localStorage.setItem('color1', color1.value as string)
    localStorage.setItem('color2', color2.value as string)
    localStorage.setItem('openai_key', openai_key.value as string)
    localStorage.setItem('lang', Llang.value as string)
    localStorage.setItem('qgpt', String(qgpt.value));

    applySettings();
    (button.value as HTMLButtonElement).innerText = LC_SAVED[lang]
    reload(router);
}

function handleExport(e : MouseEvent) {
    config.value = exportConfig();
}

function handleImport(e : MouseEvent) {
    importConfig(config.value as string);
}

function resetSettings(e : MouseEvent) {
    // remove all items from localStorage
    localStorage.clear();

    // standart wallaper
    localStorage.setItem('url', 'https://scientificrussia.ru/images/i/31qi-full.jpg');

    (Rbutton.value as HTMLButtonElement).innerText = LC_RESETED[lang];
    reload(router);
}


</script>
<template>
    <div class="settings__popup">
        
        <details>
            <summary class="settings__title">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="m320-160-56-57 103-103H80v-80h287L264-503l56-57 200 200-200 200Zm320-240L440-600l200-200 56 57-103 103h287v80H593l103 103-56 57Z"/></svg>
                <p>{{ LC_IMPORT_EXPORT[lang] }}</p>
                
            </summary>
            <div class="settings__param">
                <div class="settings__btns">
                    <button @click="isShowImportActions = !isShowImportActions; config = ''">{{ LC_IMPORT[lang] }}</button>
                    <button @click="handleExport">{{ LC_EXPORT[lang] }}</button>
                </div>
                <textarea v-model="config" v-if="config || isShowImportActions"></textarea>
                <p style="font-size: 12px; text-wrap: balance;">{{ LC_IMPORT_EXPORT_RECOMENDATION[lang] }}</p>
                <button @click="handleImport" v-if="isShowImportActions">{{ LC_APPLY[lang]}}</button>
            </div>
            </details>
         <details>
            <summary class="settings__title">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M240-120q-45 0-89-22t-71-58q26 0 53-20.5t27-59.5q0-50 35-85t85-35q50 0 85 35t35 85q0 66-47 113t-113 47Zm0-80q33 0 56.5-23.5T320-280q0-17-11.5-28.5T280-320q-17 0-28.5 11.5T240-280q0 23-5.5 42T220-202q5 2 10 2h10Zm230-160L360-470l358-358q11-11 27.5-11.5T774-828l54 54q12 12 12 28t-12 28L470-360Zm-190 80Z"/></svg>
                <p>{{  LC_CUSTOMIZATION[lang] }}</p>
            </summary>
            <div class="settings__param">
                <div>
                    <p>{{ LC_WALLAPER[lang] }}</p>
                    <input type="text" placeholder="https://example.com/1.jpg" v-model="url">
                </div>
                <div>
                    <p>{{ LC_BASE_COLOR[lang] }}</p>
                    <input type="color" v-model="color1">
                </div>
                <div>
                    <p>{{ LC_SECONDARY_COLOR[lang] }}</p>
                    <input type="color" v-model="color2">
                </div>
            </div>
            </details>
            <details>
            <summary class="settings__title">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M323-160q-11 0-20.5-5.5T288-181l-78-139h58l40 80h92v-40h-68l-40-80H188l-57-100q-2-5-3.5-10t-1.5-10q0-4 5-20l57-100h104l40-80h68v-40h-92l-40 80h-58l78-139q5-10 14.5-15.5T323-800h97q17 0 28.5 11.5T460-760v160h-60l-40 40h100v120h-88l-40-80h-92l-40 40h108l40 80h112v200q0 17-11.5 28.5T420-160h-97Zm237 0q-33 0-56.5-23.5T480-240q0-23 11-40.5t29-28.5v-342q-18-11-29-28.5T480-720q0-33 23.5-56.5T560-800q33 0 56.5 23.5T640-720q0 23-11 40.5T600-651v101l80-48q0-34 23.5-58t56.5-24q33 0 56.5 23.5T840-600q0 33-23.5 56.5T760-520q-11 0-20.5-2.5T721-530l-91 55 101 80q7-3 14-4t15-1q33 0 56.5 23.5T840-320q0 33-23.5 56.5T760-240q-37 0-60.5-28T681-332l-81-65v89q18 11 28.5 28.5T639-240q0 33-23 56.5T560-160Z"/></svg>
                <p>{{ LC_QGPT_SETTINGS[lang] }}</p>
            </summary>
            <div class="settings__param">
                <div class="settings__gpt">
                    <div class="settings__gptp"><input type="radio" id="qgpt" v-model="qgpt" :value="0"><label for="qgpt">{{ LC_DONT_USE_AI[lang] }}</label></div>
                    <div class="settings__gptp"><input type="radio" id="qgpt" v-model="qgpt" :value="1"><label for="qgpt">{{ LC_USE_QGPT[lang] }}</label></div>
                    <div class="settings__gptp"><input type="radio" id="qgpt" v-model="qgpt" :value="2"><label for="qgpt">{{ LC_USE_CHATGPT[lang] }}</label></div>
                </div>
                <div v-if="qgpt == 2">
                    <p>{{ LC_API_KEY_OPENAI[lang] }}</p>
                    <input type="text" id="qgpt" v-model="openai_key">
                </div>
            </div>
            </details>
            <details>
            <summary class="settings__title">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M480-80q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-155.5t86-127Q252-817 325-848.5T480-880q83 0 155.5 31.5t127 86q54.5 54.5 86 127T880-480q0 82-31.5 155t-86 127.5q-54.5 54.5-127 86T480-80Zm0-82q26-36 45-75t31-83H404q12 44 31 83t45 75Zm-104-16q-18-33-31.5-68.5T322-320H204q29 50 72.5 87t99.5 55Zm208 0q56-18 99.5-55t72.5-87H638q-9 38-22.5 73.5T584-178ZM170-400h136q-3-20-4.5-39.5T300-480q0-21 1.5-40.5T306-560H170q-5 20-7.5 39.5T160-480q0 21 2.5 40.5T170-400Zm216 0h188q3-20 4.5-39.5T580-480q0-21-1.5-40.5T574-560H386q-3 20-4.5 39.5T380-480q0 21 1.5 40.5T386-400Zm268 0h136q5-20 7.5-39.5T800-480q0-21-2.5-40.5T790-560H654q3 20 4.5 39.5T660-480q0 21-1.5 40.5T654-400Zm-16-240h118q-29-50-72.5-87T584-782q18 33 31.5 68.5T638-640Zm-234 0h152q-12-44-31-83t-45-75q-26 36-45 75t-31 83Zm-200 0h118q9-38 22.5-73.5T376-782q-56 18-99.5 55T204-640Z"/></svg>
                <p>{{ LC_LANGUAGE[lang] }}</p>
            </summary>
            <div class="settings__param">
                <div>
                    <p>{{ LC_LANGUAGE[lang] }}</p>
                    <select v-model="Llang">
                        <option value="en">English</option>
                        <option value="ru">Русский</option>
                        <option value="ch">中文</option>
                        <option value="ja">日本語</option>
                        <option value="pt">Português</option>
                        <option value="ar">العربية</option>
                        <option value="az">Azərbaycan</option>
                        <option value="be">Беларуская</option>
                        <option value="el">Ελληνικά</option>
                        <option value="ko">한국어</option>
                        <option value="ro">Romani</option>
                        <option value="es">Español</option>
                        <option value="fr">Français</option>
                        <option value="de">Deutsch</option>
                        <option value="it">Italiano</option>
                        <option value="tr">Türkçe</option>
                        <option value="hi">हिन्दी</option>
                    </select>
                </div>
            </div>
            </details>
        
        
        <button @click.prevent="resetSettings" ref="Rbutton" class="reset__btn">{{ LC_RESET_SETTINGS[lang] }}</button>
        <button @click.prevent="saveSettings" ref="button">{{ LC_SAVE_AND_APPLY[lang] }}</button>
    </div>
</template>


<style lang="scss" scoped>
.settings__popup {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 10px;
    max-width: 300px;
    background-color: var(--color-secondary);
    p {
        color: var(--color-text);
    }

}

.settings__btns {
    display: flex;
    gap: 10px;
    width: 100%;

    button {
        width: 100%;
    }

}

.reset__btn {
    background-color: var(--color-text);
    opacity: 0.5;
}

.settings__title {
    display: flex;
    gap: 10px;
    align-items: center;

}

.settings__param {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    justify-content: center;
    

    input:not(input[type="checkbox"]) {
        width: 100%;
    }

    
}

.settings__gpt {
    display: flex;
    flex-direction: column;
    gap: 5px;
    input[type="radio"] {
        width: fit-content !important;
    }

    .settings__gptp {
        display: flex;
    }
}

textarea {
    height: 100px;
    background-color: var(--color-secondary);
    color: var(--color-text);
}



button {
    background-color: var(--color-main);
    border: none;
    border-radius: 10px;
    color: white;
    padding: 5px 10px;
}



label {
    color: var(--color-text);
    margin-left: 5px;
}
</style>