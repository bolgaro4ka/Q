<script setup lang="ts">
import { ref, type Ref } from 'vue';


const url : Ref<string | null> = ref(localStorage.getItem('url') == undefined ? 'https://scientificrussia.ru/images/i/31qi-full.jpg' : localStorage.getItem('url'))
const qgpt : Ref<boolean | null> = ref(localStorage.getItem('qgpt') == 'true' ? true : false)

const button : Ref<HTMLButtonElement | null> = ref(null)
const Rbutton : Ref<HTMLButtonElement | null> = ref(null)

const emits = defineEmits(['close'])

function saveSettings(e : MouseEvent) {
    localStorage.setItem('url', url.value as string)

    document.body.style.backgroundImage = `url(${url.value})`

    localStorage.setItem('qgpt', qgpt.value ? 'true' : 'false');
    (button.value as HTMLButtonElement).innerText = 'Сохранено!'
    emits('close');

    
    
}


function resetSettings(e : MouseEvent) {
    localStorage.removeItem('url');
    localStorage.removeItem('qgpt');

    document.body.style.backgroundImage = `url(https://scientificrussia.ru/images/i/31qi-full.jpg)`;

    (Rbutton.value as HTMLButtonElement).innerText = 'Сброшено!';
    location.reload();
    emits('close');
}


</script>

<template>
    <div class="settings_popup">
        <div>
            <p>Обои (URL)</p>
            <input type="text" placeholder="https://example.com/1.jpg" v-model="url">
        </div>
        <div>
            <p>QGPT</p>
            
            <input type="checkbox" id="qgpt" v-model="qgpt"><label for="qgpt">Включить QGPT</label>
        </div>
        <button @click.prevent="resetSettings" ref="Rbutton">Сбросить настройки</button>
        <button @click.prevent="saveSettings" ref="button">Сохранить и применить</button>
    </div>
</template>


<style lang="scss" scoped>
.settings_popup {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 10px;
    background-color: #232222;
    p {
        color: var(--color-text);
    }
}

button {
    background-color: purple;
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