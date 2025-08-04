export function importConfig(raw: string) {
    let data = JSON.parse(raw)
    localStorage.setItem('color1', data['color1'])
    localStorage.setItem('color2', data['color2'])
    localStorage.setItem('openai_key', data['openai_key'])
    localStorage.setItem('qgpt', data['qgpt'].toString())
    localStorage.setItem('tabs', JSON.stringify(data['tabs']))
    localStorage.setItem('url', data['url'])
    localStorage.setItem('lang', data['lang'])

    location.reload();
}

export function exportConfig() {
    let data = {
        'color1': localStorage.getItem('color1'),
        'color2': localStorage.getItem('color2'),
        'openai_key': localStorage.getItem('openai_key'),
        'qgpt': Number(localStorage.getItem('qgpt')),
        'tabs': JSON.parse(localStorage.getItem('tabs') as string),
        'url': localStorage.getItem('url'),
        'lang': localStorage.getItem('lang')
    }

    // return with convert to string
    return JSON.stringify(data)

}