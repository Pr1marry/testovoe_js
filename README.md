# Тестовое задание по платежной системе Stripe
#### https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit#

### Реализованы доп. пункты: 
#### Запуск используя Docker
#### Использование environment variables
#### Просмотр Django Моделей в Django Admin панели
#### Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте


## Запуск и тестирование проекта:
#### Клонируем репозиторий к себе на утройство командой - git clone https://github.com/Pr1marry/testovoe_js
#### Переходим в директорию проекта - cd cd testovoe_js/
#### Запускаем docker desktop, в консольке проекта поднимаем контейнеры - docker-compose up -d
#### Приложение доступно по адресу http://localhost:8000/ в DEBUG режиме 
#### В админке проекта можно настроить как отдельные товары(item) так и заказ(order) с несколькими товарами, админ аккаунт генерируется при инициализации проекта через .env файл, стандартные данные log-admin pas-admin
#### Находим в проекте папку temlates и в файле payments.html меняем js скрипт редиректа, далее по тз: http://localhost:8000/item/'id' генерируется html сраница с кнопкой, которая получает stripe.id с эндпоинта http://localhost:8000/buy/'id' 
