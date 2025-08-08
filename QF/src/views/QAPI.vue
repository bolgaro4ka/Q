<script setup lang="ts">
import HighlightedCode from '@/components/Base/HighlightedCode.vue';
import { BASE_URL } from '@/config/main';

const codeSnippet = `
async function fetchResults() {
  isLoading.value = true
  raw_res.value = await axios.post(REQ_ENDPOINT, {
    st: route.query.st ? replaceSpecialSymbols(route.query.st as string) : '',
    in: route.query.in as string,
    ot: route.query.ot as string,
    sz: route.query?.sz as string | undefined,
    sg: route.query?.sg as string | undefined
  })

  return raw_res.value
}
`.trim()

const codeQGPT = `
// Request to QGPT (mode = 1) or ChatGPT (mode = 2)
const raw_res = await axios.post(GPT_ENDPOINT, {
    content: props.content,
    chatgpt_api_key: props.mode == 2 ? localStorage.getItem('openai_key') : ''
})`.trim()

const codeAnswerSearch = `
{
    "in": "w",
    "ot": "0",
    "st": "some",
    "obj": [
        {
            "link": "<p class=\"link_p\"><a href=\"http://some-spec.livejournal.com/profile\" target=\"_blank\" title=\"http://some-spec.livejournal.com/profile\"><b>some</b>_spec - Profile</a></p>",
            "desc": "<p class=\"desc_p\"><b>some</b> spec - Profile. 1,5Kb...</p>",
            "arch": "",
            "saved": "<p class=\"cache_p\"><a href=\"https://www.mmnt.ru/cache/1b0b77fcd41f1e0128ab3918b5bbeb84.html\" target=\"_blank\">Сохранено (19 августа 2023)</a> - 18.18Kb</p>",
            "url": "<font color=\"#fff\">some-spec.livejournal.com/profile - 498.40Kb</font>",
            "class": "link"
        },
        {
            "link": "<p class=\"link_p\"><a href=\"http://www.learn-some-english.com/\" target=\"_blank\" title=\"http://www.learn-some-english.com/\">Expert Tips On How To Find Quality Help Essay Writing</a></p>",
            "desc": "<p class=\"desc_p\">Expert Tips On How To Find Quality Help Essay Writing. 10.73Kb...</p>",
            "arch": "",
            "saved": "<p class=\"cache_p\"><a href=\"https://www.mmnt.ru/cache/703064b6905bb4c1a6b9f716802c1a91.html\" target=\"_blank\">Сохранено (24 марта 2023)</a> - 5.08Kb</p>",
            "url": "<font color=\"#fff\">www.learn-some-english.com - 10.73Kb</font>",
            "class": "link"
        },
        ...
    ],
    "OK": true,
    "cpages": "812 тыс. 393"
}`.trim()

const codeAnswerQVPN = `
{
    "html": "<!DOCTYPE html>\n<html>\n <head>\n  <title>\n   Example Domain\n  </title>\n  <meta charset=\"utf-8\"/>\n  <meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-type\"/>\n  <meta content=\"width=device-width, initial-scale=1\" name=\"viewport\"/>\n  <style type=\"text/css\">...</style>\n </head>\n <body>\n  <div>\n   <h1>\n    Example Domain\n   </h1>\n   <p>\n    This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.\n   </p>\n   <p>\n    <a href=\"https://q.blgr.space/qvpn/?url=https://www.iana.org/domains/example\">\n     More information...\n    </a>\n   </p>\n  </div>\n </body>\n</html>\n",
    "url": "https://example.com",
    "res": "OK"
}
`.trim()

const codeExampleQVPN = `
const raw_page = await axios.post(VPN_ENDPOINT, {
    url: props.url
}).catch((e) => {
    error.value = true;
})

const page = raw_page?.data?.html
`.trim()
</script>

<template>
    
    <div class="wrapper">
        <div class="content">
            <h1>Документация по API поисковика Q</h1>
            <div class="logo"><img src="/favicon.ico" alt="QF"></div>
            
            <h2 id="content">🌏 Содержание</h2>
            <ul>
                <li><RouterLink to="/api#content">🌏 Содержание</RouterLink></li>
                <li><RouterLink to="/api#main">📋 Основная информация</RouterLink></li>
                <li><RouterLink to="/api#endpoints">🎟️ Эндпоинты</RouterLink></li>
                <li><RouterLink to="/api#search">🔍🧩 Поиск (интернет и FTP)</RouterLink></li>
                <li><RouterLink to="/api#qgpt">🤖 QGPT</RouterLink></li>
                <li><RouterLink to="/api#qvpn">🔓 QVPN</RouterLink></li>
            </ul>
            <h2 id="main">📋 Основная информация</h2>
            <p>Поисковик Q - уникальный поисковик сочитающий в себе скорость и удобство.</p>
            <p>Это Open Source проект. Его исходный код доступен на <a href="https://github.com/bolgaro4ka/Q">GitHub</a>.</p>
            <h2 id="endpoints">🎟️ Эндпоинты</h2>
            <p>Далее по документации будут представлены ссылки на эндпоинты</p>
            <p>Примеры будут написанны на TypeScript с использованием библиотеки axios</p>
            <h2 id="search">🔍🧩 Поиск (интернет)</h2>
            <h3>{{ BASE_URL + '/post/' }}</h3>
            <p>Эндпоинт для поиска в интернете</p>
            <div class="reqAndRes">
                <div>
                    <div>
                        <p>Параметры запроса:</p>
                        <ul>
                            <li>st - строка поискового запроса</li>
                            <li>in - место поиска (w - интернет, f - FTP)</li>
                            <li>ot - страница (первая страница - 10, вторая - 20 и т.д.)</li>
                            <li>sz - размер файла в байтах (только для FTP)</li>
                            <li>sg - поиск по определенному серверу (только для FTP)</li>
                        </ul>
                    </div>
                    <div>
                        <p>Пример запроса:</p>
                        <HighlightedCode :code='`{\n"in": "w",\n"ot": "0",\n"st": "some"\n}`' class="code"/>
                    </div>
                    <div>
                        <p>Параметры ответа:</p>
                        <HighlightedCode :code='`{\n"in": string,\n"ot": string,\n"st": string,\n"obj": [\n{\n"link": HTMLstring,\n"desc": HTMLstring,\n"arch": HTMLstring,\n"saved": HTMLstring,\n"url": HTMLstring,\n"class": string[link | rkn | arch]\n},\n ...\n],\n"OK": boolean,\n"cpages": string\n}`' class="code"/>
                    </div>
                    
                    
                </div>
                <div>
                    <p>Пример ответа:</p>
                    <HighlightedCode :code="codeAnswerSearch" class="code"/>
                </div>
            </div>
            <p>Пример из кода:</p>
            <HighlightedCode :code="codeSnippet" class="code"/>

            <h2 id="qgpt">🤖 QGPT</h2>
            <h3>{{ BASE_URL + '/gpt/' }}</h3>
            <p>Эндпоинт для работы с ChatGPT и QGPT</p>
            <h3>Как это работает?</h3>
            <p>Есть два варианта:</p>
            <ul>
                <li>
                    <code>chatgpt_api_key</code> не пустой
                </li>
                <li>
                    <code>chatgpt_api_key</code> пустой
                </li>
            </ul>
            <p>В первом случае используется оригинальная библиотека OpenAI, которая гарантированно даст хороший ответ</p>
            <p>Во втором случае используется QGPT - это библиотека <code><a href="https://github.com/xtekky/gpt4free">g4f</a></code> (gpt4free) она не всегда может дать адекватный ответ (так как является бесплатной). Но если у пользователя всё-таки нету api-ключа ChatGPT, то это единственно возможное решение.</p>
            <div class="reqAndRes">
                <div>
                    <div>
                        <p>Параметры запроса:</p>
                        <ul>
                            <li>content - текст для обработки</li>
                            <li>chatgpt_api_key - ключ API ChatGPT (необязательно)</li>
                        </ul>
                    </div>
                    <div>
                        <p>Пример запроса:</p>
                        <HighlightedCode :code='`{\n"content": "Как дела?",\n"chatgpt_api_key": ""\n}`' class="code"/>
                    </div>
                    <div>
                        <p>Параметры ответа:</p>
                        <HighlightedCode :code='`{\n"res": string\n}`' class="code"/>
                    </div>
                </div>
                <div>
                    <p>Пример ответа:</p>
                    <HighlightedCode code='{"res": "Ну, как у меня дела — отлично! А у тебя как настроение? Что новенького или что сейчас занимает мысли?"}' class="code"/>
                </div>
            </div>
            <p>Пример из кода:</p>
            <HighlightedCode :code="codeQGPT" class="code"/>

            <h2 id="qvpn">🔓 QVPN</h2>
            <h3>{{ BASE_URL + '/qvpn/' }}</h3>
            <p>Отдаёт страницу по URL</p>
            <h3>Как это работает?</h3>
            <p>Сервер загружает HTML-страницу по указанному URL, меняет ссылки на внутренние (проксирует ссылки), отдаёт полученную страницу клиенту.</p>
            <div class="reqAndRes">
                <div>
                    <div>
                        <p>Параметры запроса:</p>
                        <ul>
                            <li>url - URL для перенаправления</li>
                        </ul>
                    </div>
                    <div>
                        <p>Пример запроса:</p>
                        <HighlightedCode :code='`{\n"url": "https://exapmle.com"\n}`' class="code"/>
                    </div>
                    <div>
                        <p>Параметры ответа:</p>
                        <HighlightedCode :code='`{\n"html": HTMLstring,\n"url": string,\n"res": string[OK | ERROR]\n}`' class="code"/>
                    </div>
                </div>
                <div>
                    <p>Пример ответа:</p>
                    <HighlightedCode :code="codeAnswerQVPN" class="code"/>
                </div>

            </div>
            <p>Пример из кода:</p>
            <HighlightedCode :code="codeExampleQVPN" class="code"/>
        </div>
    </div>
</template>

<style lang="scss" scoped>
* {
    color: white;
}

.logo {
    display: flex;
    justify-content: center;
    align-items: center;
}

.wrapper {
    margin: 0 auto;
    max-width: 900px;
}

h1 {
    text-align: center;
}

h2 {
    margin: 10px 0;
}

.reqAndRes {
    display: flex;
    gap: 10px;
    justify-content: space-between;
}

.code {
    margin: 10px auto;
    max-width: 700px;
    text-wrap: wrap;
    white-space: pre-wrap;
    word-wrap: break-word;
}
</style>