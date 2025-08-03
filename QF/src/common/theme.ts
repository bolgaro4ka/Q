export function applySettings() {
    // replace css varable --color-main
    console.log(localStorage.getItem('color1'))
    document.documentElement.style.setProperty('--color-main', localStorage.getItem('color1') as string ?? '#800080');
    document.documentElement.style.setProperty('--color-secondary', localStorage.getItem('color2') as string ?? '#232222');

}