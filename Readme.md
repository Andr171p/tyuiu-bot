# Telegram bot абитуриента ТИУ

## REST API

## Users

### User shema:

```json
{
  "telegram_id": 0,
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "first_name": "string",
  "last_name": "string",
  "username": "string",
  "phone_number": "string",
  "status": "READY",
  "created_at": "",
  "updated_at": ""
}
```

 * <b>telegram_id</b> - Telegram ID пользователя
 * <b>user_id</b> - ID пользователя в формате UUID получаемый при регистрации
 * <b>first_name</b> - Имя пользователя (опционально)
 * <b>last_name</b> - Фамилия пользователя (опционально)
 * <b>username</b> - Telegram nickname пользователя (опционально)
 * <b>phone_number</b> - Номер телефона в формате +7(XXX)XXX-XX-XX
 * <b>status</b> - Статус пользователя:
   * READY - готов получать уведомления (поделился контактом в Telegram боте и зарегистрировался на сайте)
   * REGISTRATION_REQUIRE - нужно пройти регистрацию на сайте (поделился контактом, но не зарегистрировался на сайте)
 * <b>created_at</b> - Дата создания ресурса
 * <b>updated_at</b> - Дата обновления ресурса

### Базовый ендпоинт `/api/v1/users`

* ### <b>GET</b> `/{user_id}`</br>
    Метод для получения пользователя по его user_id.

    ### Запрос</br>
    - <b>user_id</b> - uuid</br>
    Уникальный ID пользователя получаемый при регистрации
    ### Ответ</br>
    - <font style="color: #22863a;">200 OK</font></br>
     Возвращает user schema</br>
     ```json
     {
       "telegram_id": 0,
       "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
       "first_name": "string",
       "last_name": "string",
       "username": "string",
       "phone_number": "string",
       "status": "READY",
       "created_at": "",
       "updated_at": ""
    }
     ```
     - <span style="color: red;">404 Not found</span></br>
    ```json
    {"detail": "User not found"}
    ```

* ### <b>PATCH</b> `/`
   Метод для обновления поля user_id пользователя (если пользователь не зарегистрирован на сайте, но поделился контактом).

   ### Запрос (Query params)</br>
   - <b>phone_number</b> - string</br>
   Номер телефона пользователя в формате +7(XXX)XXX-XX-XX
   - <b>user_id</b> - uuid</br>
   Уникальный ID пользователя получаемый при регистрации (обновляемый параметр)
  ### Ответ
  - <span style="color: green;">200 OK</span></br>
  Возвращает обновлённую user schema
  - <span style="color: red;">404 Not found</span></br>
  ```json
  {"detail": "User has not yet shared contact"}
  ```
  Когда пользователь ещё не поделился контактом.

* ### <b>GET</b> `/{user_id}/notifications`
Метод для просмотра уведомлений отправленных пользователю.

### Запрос</br>
- <b>user_id</b> - uuid</br>
Уникальный ID пользователя полученный при регистрации.</br>
### Ответ</br>
 - <span style="color: green;">200 OK</span></br>
 Возвращает список отправленных уведомлений.
 ```json
 [
  {
    "level": "INFO",
    "user_id": "string",
    "photo": "string",
    "text": "string",
    "notification_id": "string",
    "status": "DELIVERED",
    "created_at": ""
  }
 ]
 ```
 - <span style="color: red;">404 Not found</span></br>
 ```json
 {"detail": "Notification not found"}
 ```

## Notifications

### Notification schema

```json
{
  "level": "INFO",
  "user_id": "string",
  "photo": "string",
  "text": "string",
  "notification_id": "string",
  "status": "DELIVERED",
  "created_at": ""
}
```
 * <b>level</b> - Уровень уведомления абитуриента.</br>
   - <b>INFO</b> - Информационный уведомления (например появилось новое мероприятие).
    - <b>CHANGE_PASSWORD</b> - Смена пароля пользователя (создаёт клавиатуру для продолжени или отмены от смены пароля).
     - <b>POSITIVE</b> - Уведомление положительного характера (например абитуриент проходит на бюджет).
     - <b>WARNING</b> - Предупреждение 
     - <b>CRITICAL</b> - Критический уровень (например когда абитуриент не проходит на бюдже).
  * <b>user_id</b> - Уникальный ID полученный при регистрации.
  * <b>photo</b> - Фото прикреплённое к сообщению в формате base64 (опцианально).
  * <b>text</b> - Текст сообщения.
  * <b>notification_id</b> - Уникальный ID уведомления в формате uuid. ID присвается после попытки отправки уведомления.
  * <b>status</b> - Статус отправки уведомления:
    - <b>DELIVERED</b> - Уведомление успешно доставлено.
    - <b>NOT_DELIVERED</b> - Уведомлние не доставлено (возможные причины: пользователь не поделился контактом; номер телефона на сайте не совпадает с номером в боте)
    - <b>ERROR</b> - Уведомление не отправилось из за ошибки.
* <b>created_at</b> - Дата отправки уведомления.


### Базовый ендпоинт `/api/v1/notifications`

* <b>POST</b> `/`</br>
Метод для отправки уведомлений. Гарантирует отправку и сохранения уведомления в рамках одной сессии.
  ### Запрос (Request body)
  ```json
  {
    "level": "INFO",
    "user_id": "string",
    "photo": "string",
    "text": "string"
  }
   ```
  ### Ответ
  - <span style="color: green;">201 Created</span></br>
  ```json
  {"notification_id": "string", "sent_at": ""}
  ```
  - <span style="color: red;">500 Internal server error</span></br>
  ```json
  {"detail": "Error while sending notification"}
  ```
  