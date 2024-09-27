<script setup lang="ts">
    const props = defineProps(['err'])
</script>

<template>
    <div class="no-found-wrapper">
        <div class="no-found">
        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="purple"><path d="M480-280q17 0 28.5-11.5T520-320q0-17-11.5-28.5T480-360q-17 0-28.5 11.5T440-320q0 17 11.5 28.5T480-280Zm-40-160h80v-240h-80v240Zm40 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg>
        <p>По вашему запросу ничего не найдено, попробуйте переформулировать запрос</p>
        <code style="text-align: center" v-if="props.err" >Backend error: {{ props.err }}</code>
    </div>
    </div>

</template>

<style lang="scss" scoped>
.no-found-wrapper {
    width: 90vw;
    margin: 0 auto;
    height: calc(100vh - 170px);
    display: flex;
    align-items: center;
    justify-content: center;
}

@media screen and (max-width: 700px) {
    .no-found-wrapper {
        height: calc(100vh - 350px);
    }
    
    
}

.no-found {
    width: 500px;
    height: 400px;
    color: var(--color-text);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    p {
        text-align: center;
    }

    svg {
        transform: scale(10);
        margin-bottom: 100px;
        margin-top: 150px;
    }
}

code {
    background-color: #232222;
    padding: 5px;
    margin-top: 5px;
    border-radius: 10px;
}
</style>