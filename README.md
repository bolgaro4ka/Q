# Q (Quadrillion)
Q - поисковик по всему интернету
<div align="center"> 
 <img src="https://github.com/user-attachments/assets/6e17156d-fd27-4e3b-a4d3-214d530dea91" alt="logo" />
</div>

### [🧩 Подробная документация](https://q.blgr.space/api)

## Содержание
 - [❓ Что это](#что-это)
 - [🌍 Где это](#где-это)
 - [👷 Как это работает](#как-это-работает)
    - [🛜 Как работает QVPN](#как-работает-qvpn)
    - [🤖 Как работает QGPT](#как-работает-qgpt)
 - [⚙️ Установка](#установка)
    - [🪪 Backend](#backend)
    - [✅ Frontend](#frontend)
 - [🎴 Картиночки](#картиночки)

## Где это
- Frontend: https://q.paia1nik.ru/
- Backend: https://qb.paia1nik.ru/

## Что это
Поисковик с глубоким поиском по интернету и FTP-серверам, с google и встроенным VPN (QVPN) в одном флаконе





## Как это работает
Глубокий поиск берёт страницы из [этого источника](https://mmnt.ru)

В поисковой выдаче также присутствуют результаты из Google (они выделены градиентноц рамкой)

### Как работает QVPN
Тут всё довольно просто:
- С Клиента отправляется POST-запрос на Backend-сервер содержащий URL
- Backend-сервер загружает HTML-страницу по этому URL
- Результат отдаётся Клиенту

### Как работает QGPT
С недавнего времени добавлен ответ ChatGPT в поисковой выдаче. Работает без VPN, бесплатно без СМС и регистрации.
Работает также довольно просто:
- Ответ получается с Backend-сервера Python на котором установлена библиотека [g4f](https://pypi.org/project/g4f/)
- Markdown парсится в HTML с помощью библиотеки [Marked](https://www.npmjs.com/package/marked) на Frondend-сервере
![{E3AE3F6A-EE40-424A-A502-1385BE49792A}](https://github.com/user-attachments/assets/b90c2e0a-9777-4764-8163-3a1fcbe2a330)


## Установка

### Backend

 - Разверните виртуальное окружение Python - ```python -m venv venv```
 - Запустите  виртуальное окружение Python:

     ```venv/Scripts/activate``` - windows

     ```source venv/bin/activate``` - linux
 
 - Установите зависимости - ```pip install -r req.txt```
 - Запустите сервер - ```python manage.py runserver localhost:8003```

### Frontend
 - Установите зависимости - ```npm i```
 - Замените в файле `src/common/main.ts` константу `BASE_URL` на адрес вашего Backend-сервера
 - Запустите сервер - ```npm run dev```

## Картиночки
![{918D7993-B5C2-4F9E-A3B7-9EDC01656208}](https://github.com/user-attachments/assets/89cbaf8c-7d19-4543-8616-68d7839ffcab)
Главная страница
![{9E3635AD-2D18-425E-B222-9C565179B1A8}](https://github.com/user-attachments/assets/7076fd44-aa95-4514-b791-c34bc7efad54)
Поиск по интернету
![{4C449E68-69BB-4DF3-B0AB-2A266F6BECA5}](https://github.com/user-attachments/assets/929335ff-cecd-4746-97ef-59a194d74826)
Поиск по FTP-серверам
![{4627811B-39F8-4C52-A270-67AC81365A54}](https://github.com/user-attachments/assets/9fdbb6aa-7041-42df-9349-eddd6ca196a9)
VPN (QVPN)

## Проект [Q](https://github.com/bolgaro4ka/Q) создан [Bolgaro4ka](https://github.com/bolgaro4ka) с 💜
