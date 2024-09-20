<script setup lang="ts">
import { toNormalNumber, urlEncode, roundIfNumberHaveDotWithNumberAfterItMoreThanZero } from '@/common/main';

const props = defineProps(['ot', 'st', 'in', 'cpages'])
</script>

<template>
<div class="pages">
    <p class="pages__total">Всего результатов: <b>{{$props?.cpages}}</b></p>
    <div class="pages__nav">
        <div class="pages__prevs">
            <a 
            v-for="count of ['-01', '-02', '-03', '-04', '-05', '-06', '-07', '-08', '-09', '-10', '-11', '-12', '-13', '-14', '-15']" 
            :key="count" 
            :href="`/get?in=${$props.in}&st=${$props.st}&ot=${(parseInt($props.ot) + parseInt(count)*10)}`">
        {{ count }}
        </a>
        <p v-if="$props.in == 'w'" class="pages__count">Количество страниц: {{roundIfNumberHaveDotWithNumberAfterItMoreThanZero(toNormalNumber($props.cpages)/10)}}</p>
        <p v-if="$props.in == 'f'" class="pages__count">Количество страниц: {{roundIfNumberHaveDotWithNumberAfterItMoreThanZero(toNormalNumber($props.cpages)/20)}}</p>    
    </div>
        <div class="pages__nexts">
            <a 
            v-for="count of ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']" 
            :key="count" 
            :href="`/get?in=${$props.in}&st=${$props.st}&ot=${(parseInt($props.ot) + parseInt(count)*10)}`">
        {{ count }}
        </a>
        <a :href="`/get?in=${$props.in}&st=${$props.st}&ot=${(parseInt($props.ot) + -1*10)}`"><- Предыдущие</a>
        <a :href="`/get?in=${$props.in}&st=${$props.st}&ot=${(parseInt($props.ot) + 1*10)}`">Следующие -></a>
        </div>
    </div>
</div>
</template>

<style lang="scss" scoped>

.pages {
    margin-left: 30px;
    margin-bottom: 20px;
}

.pages__total {
    color: #8c8879;

    b {
        font-size: 22px;
    }
}

.pages__count {
    color: #8c8879;
    font-size: 15px;
}

.pages__prevs, .pages__nexts {
    display: flex;
    gap: 5px;
    a {
        cursor: pointer;
    }
}
</style>