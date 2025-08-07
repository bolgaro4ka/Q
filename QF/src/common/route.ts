import type { Router } from "vue-router";


export function reload(router: Router) {
    router.go(0);
}

export function redirect(router: Router, path: string) {
    router.push(path);
}