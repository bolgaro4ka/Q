<script setup lang="ts">
import { ref } from 'vue';


const url = ref('')

function saveSettings(e : MouseEvent) {
    localStorage.setItem('url', url.value)
    document.body.style.backgroundImage = `url(${url.value})`
    
}
</script>

<template>
    <div class="settings_popup">
        <div>
            <p>Обои (URL)</p>
            <input type="text" placeholder="https://example.com/1.jpg" v-model="url">
        </div>
        <button @click.prevent="saveSettings">Сохранить и применить</button>
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
</style>