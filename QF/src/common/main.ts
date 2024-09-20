export const CODE : { [key: string]: string } = {
    'А': '%C0', 'Б': '%C1', 'В': '%C2', 'Г': '%C3', 'Д': '%C4', 'Е': '%C5', 'Ж': '%C6', 'З': '%C7', 'И': '%C8',
    'Й': '%C9', 'К': '%CA', 'Л': '%CB', 'М': '%CC', 'Н': '%CD', 'О': '%CE', 'П': '%CF', 'Р': '%D0', 'С': '%D1',
    'Т': '%D2', 'У': '%D3', 'Ф': '%D4', 'Х': '%D5', 'Ц': '%D6', 'Ч': '%D7', 'Ш': '%D8', 'Щ': '%D9', 'Ъ': '%DA',
    'Ы': '%DB', 'Ь': '%DC', 'Э': '%DD', 'Ю': '%DE', 'Я': '%DF', 'а': '%E0', 'б': '%E1', 'в': '%E2', 'г': '%E3',
    'д': '%E4', 'е': '%E5', 'ж': '%E6', 'з': '%E7', 'и': '%E8', 'й': '%E9', 'к': '%EA', 'л': '%EB', 'м': '%EC',
    'н': '%ED', 'о': '%EE', 'п': '%EF', 'р': '%F0', 'с': '%F1', 'т': '%F2', 'у': '%F3', 'ф': '%F4', 'х': '%F5',
    'ц': '%F6', 'ч': '%F7', 'ш': '%F8', 'щ': '%F9', 'ъ': '%FA', 'ы': '%FB', 'ь': '%FC', 'э': '%FD', 'ю': '%FE',
    'я': '%FF'
}

export const NORMALIZE_NUMBERS : { [key: string]: number } = {
    'тыс.': 1000,
    'млн.': 1000000,
    'млрд.': 1000000000

}



export function urlEncode(s: string) {
    let res=''
    for (let leter of s) {
        if (leter in CODE) res += CODE[leter]
        else res += leter
    }
    return res
}

export function toNormalNumber (s: string) {
    //  10 млн. 647 тыс. 430
    for (let key in NORMALIZE_NUMBERS) {
        s = s.replace(key, NORMALIZE_NUMBERS[key].toString())
        //  10 1000000 647 1000 430

    }
    var ss = s.split(' ')
    var res=0
        for (let i = 0; i < ss.length; i++) {
            if (!ss[i+1]) {res+=parseInt(ss[i]); break}
            if (i%2!=0) continue
            res += parseInt(ss[i])*parseInt(ss[i+1])
            console.log(ss[i],ss[i+1],res, i)
        }
    return res

}

export function roundIfNumberHaveDotWithNumberAfterItMoreThanZero(s: number) {if (parseInt(s.toString().split('.')[1]) > 0) {return parseInt(s.toString().split('.')[0])+1} else return s}

