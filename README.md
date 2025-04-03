# wallet-service-backend

Это тестовое задание, суть задания и его описание находится в test.txt

Запуск через docker-compose
## Настройка Конфигурационного файла
```
cp .env.example .env
# Отредактируйте .env файл согласно вашей конфигурации
```

## Запуск контейнера

``` 
docker-compose up --build
```

🚀 Запуск локально

### 1. Клонирование репозитория

```
https://github.com/Eugen9719/wallet-service-backend.git
```

## 2. Установка зависимостей pip

```
pip install -r requirements.txt
  ```

## 3. Настройка Конфигурационного файла

```
cp .env.example .env
# Отредактируйте .env файл согласно вашей конфигурации
```

## 4. Запуск  сервера

```
uvicorn backend.main:app --reload
```

## 5. Документация

```
127.0.0.1:8010/docs
```

## Данные для входа:
Администратор : admin@example.com : admin 

Тестовый пользователь: testuser@example.com: test

