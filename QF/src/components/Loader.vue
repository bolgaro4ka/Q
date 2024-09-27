<script setup lang="ts">


</script>

<template>
    <div class="loader">
        <div class="loader__container">
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
            <div class="loader__block"></div>
          </div>
    </div>
</template>

<style scoped lang="scss">
  
  .loader__container {
    width: 80px;
    height: 100px;
  }
  
  .loader__block {
    position: relative;
    box-sizing: border-box;
    float: left;
    margin: 0 10px 10px 0;
    width: 12px;
    height: 12px;
    border-radius: 3px;
    background: purple;
  }

  .loader {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    min-height: 200px;
    min-width: 200px;
  }
  
  .loader__block:nth-child(4n+1) { animation: wave 2s ease .0s infinite; }
  .loader__block:nth-child(4n+2) { animation: wave 2s ease .2s infinite; }
  .loader__block:nth-child(4n+3) { animation: wave 2s ease .4s infinite; }
  .loader__block:nth-child(4n+4) { animation: wave 2s ease .6s infinite; margin-right: 0; }
  
  @keyframes wave {
    0%   { top: 0;     opacity: 1; }
    50%  { top: 30px;  opacity: .2; }
    100% { top: 0;     opacity: 1; }
  }
</style>