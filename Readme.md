# Документация Telegram Bot API

## Рабочая версия: `/api/v1`

## Список доступных ресурсов:
  * <b>users</b>
  * <b>contacts</b>
  * <b>chats</b>
  * <b>notifications</b>

## Общие методы доступные для ресурсов (<b>users</b>, <b>contacts</b>, <b>chats</b>):

> GET `/api/v1/[имя ресурса]/count/`

Возвращает количество элементов.<br>
Схема ответа:
```json
{
  "count": 0
}
```

> GET `/api/v1/[имя ресурса]/per-day-count/`

Возвращает распределение количества элементов по дням.<br>
Схема ответа:
```json
{
  "distribution": [
    {
      "date": "2025-03-22T14:47:48.363Z",
      "count": 0
    }
  ]
}
```

## Users:
Ресурс для работы с пользователями. Предоставляет методы только для чтения, не вносит изменения в ресурс.

> GET `/api/v1/users/`

Получает всех пользователей.<br>
Схема ответа:
```json
{
  "users": [
    {
      "user_id": 0,
      "username": "string",
      "created_at": "2025-03-13T15:20:11.267Z"
    }
  ]
}
```

> GET `/api/v1/users/{user_id}/`

Возвращает пользователя по его telegram id (int).<br>

| Name | Type |
|:--------:|:-------:|
| user_id  | int |

Схема ответа:
```json
{
  "user_id": 0,
  "username": "string",
  "created_at": "2025-03-22T14:51:08.105Z"
}
```

## Contacts
Ресурс для получения контактов пользователей (пользователи которые могут получать уведомления).

> GET `/api/v1/contacts/ `

Возвращает все контакты.<br>
Схема ответа:
```json
{
  "contacts": [
    {
      "user_id": 0,
      "phone_number": "string",
      "created_at": "2025-03-22T14:54:39.980Z"
    }
  ]
}
```

> GET `/api/v1/contacts/{user_id}/`

Метод для получения контакта по user_id пользователя.<br>

| Name | Type |
|:--------:|:-------:|
| user_id  | int |

Схема ответа:
```json
{
  "user_id": 0,
  "phone_number": "string",
  "created_at": "2025-03-22T14:56:29.006Z"
}
```

## Chats
Ресурс для работы с чатами, диалогами пользователей.

> GET `/api/v1/chats/`

Возвращает все диалоги пользователей (история чата). (Не рекомендовано использовать)<br>
Схема ответа:
```json
{
  "dialogs": [
    {
      "user_id": 0,
      "user_message": "string",
      "chatbot_message": "string",
      "created_at": "2025-03-22T14:57:23.694Z"
    }
  ]
}
```

> GET `/api/v1/chats/{user_id}/`

Метод для получения истории сообщений пользователя.

| Name |         Type          |
|:--------:|:---------------------:|
| user_id  |          int          |
| is_paginated | boolean default false |
| page |        int default 1 |
| limit | int default 10 |

<b>is_paginated</b> - true для использования пагинации.<br>
<b>page</b> - страница с диалогами.<br>
<b>limit</b> - лимит элементов на одной странице.<br>

Схема ответа:
```json
{
  "user_id": 0,
  "dialogs": [
    {
      "user_id": 0,
      "user_message": "string",
      "chatbot_message": "string",
      "created_at": "2025-03-22T15:02:54.294Z"
    }
  ]
}
```

## Notifications:

Ресурс для отправки уведомлений зарегистрированным пользователям.

> POST `/api/v1/notifications/notify-all/`

Тело запроса:
```json
{
  "text": "string"
}
```

Схема ответа:
```json
{
  "detail": "notification delivered"
}
```

> POST `/api/v1/notifications/notify-by-phone-number/`

Тело запроса:

```json
{
  "text": "string",
  "phone_number": "string"
}
```

Схема ответа:
```json
{
  "detail": "notification delivered"
}
```
