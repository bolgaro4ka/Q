import urllib

CODE = {
    'А': '%C0', 'Б': '%C1', 'В': '%C2', 'Г': '%C3', 'Д': '%C4', 'Е': '%C5', 'Ж': '%C6', 'З': '%C7', 'И': '%C8',
    'Й': '%C9', 'К': '%CA', 'Л': '%CB', 'М': '%CC', 'Н': '%CD', 'О': '%CE', 'П': '%CF', 'Р': '%D0', 'С': '%D1',
    'Т': '%D2', 'У': '%D3', 'Ф': '%D4', 'Х': '%D5', 'Ц': '%D6', 'Ч': '%D7', 'Ш': '%D8', 'Щ': '%D9', 'Ъ': '%DA',
    'Ы': '%DB', 'Ь': '%DC', 'Э': '%DD', 'Ю': '%DE', 'Я': '%DF', 'а': r'%E0', 'б': r'%E1', 'в': r'%E2', 'г': r'%E3',
    'д': r'%E4', 'е': r'%E5', 'ж': r'%E6', 'з': r'%E7', 'и': r'%E8', 'й': r'%E9', 'к': r'%EA', 'л': r'%EB', 'м': r'%EC',
    'н': r'%ED', 'о': r'%EE', 'п': r'%EF', 'р': r'%F0', 'с': r'%F1', 'т': r'%F2', 'у': r'%F3', 'ф': r'%F4', 'х': r'%F5',
    'ц': r'%F6', 'ч': r'%F7', 'ш': r'%F8', 'щ': r'%F9', 'ъ': r'%FA', 'ы': r'%FB', 'ь': r'%FC', 'э': r'%FD', 'ю': r'%FE',
    'я': r'%FF'
}

def decode_url(url):
    for key, value in CODE.items():
        url = url.replace(value, key)
    return url

def get_domain(url):
    return  url.split('://')[0]+'://'+urllib.parse.urlparse(url).netloc
