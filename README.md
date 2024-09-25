# Q (Quadrillion)
Q - поисковик по всему интернету
![favicon](https://github.com/user-attachments/assets/6e17156d-fd27-4e3b-a4d3-214d530dea91)

## Что это
Поисковик с глубоким поиском по интернету и FTP-серверам, с google и встроенным VPN (QVPN) в одном флаконе

## Как это работает
Глубокий поиск берёт страницы из [этого источника](https://mmnt.ru)
В поисковой выдаче также присутствуют результаты из Google (они выделены градиентноц рамкой)

## Как работает QVPN
Тут всё довольно просто:
- С Клиента отправляется POST-запрос на Backend-сервер содержащий URL
- Backend-сервер загружает HTML-страницу по этому URL
- Результат отдаётся Клиенту

## Установка

### Backend:

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
