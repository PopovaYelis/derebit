# Derebit


## Описание

**Derebit** — Программа для мониторинга курса USD на бирже DEREBIT

## Установка

### С помощью Docker

Для запуска приложения с помощью Docker выполните следующие шаги:

1. Убедитесь, что у вас установлен Docker. Если нет, скачайте и установите его с [официального сайта Docker](https://www.docker.com/get-started).

2. Клонируйте репозиторий:
   git clone https://github.com/PopovaYelis/derebit.git
3. Запуск:
   sudo docker compose up

#### Взаимодествие с API:
1. Для открытия swagger перейдите по ссылке http://localhost:5050/docs
   - отсюда можно взаимодействовать с route посмотреть какие есть query params.
2. http://localhost:5050/currency?ticker={название валюты (bct\eth)}
   - GET запрос на получение всех данных из БД по выбранной валюте (ticker)
3. http://localhost:5050/currency?ticker={название валюты (bct\eth)}&latest=true
   - GET запрос на получение последней записи из БД по выбранной валюте (ticker). По умолчанию latest=false.
4. http://localhost:5050/currency?ticker={название валюты (bct\eth)}&date_filter={Данные в формате YYYY-MM-DDTHH:MM:SS} (пример 2024-10-28T13:36:09)
   - GET запрос на получние записи из БД по выбранной валюте (ticker) и определенному времени/дате. По умолчанию date_filter=none.
   - Можно использовать либо latest, либо date_filter т.к. если уже будеь latest, то data_filter будет проигнорирован.
   
  
