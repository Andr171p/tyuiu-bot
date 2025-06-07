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
    ### Запрос</br>
    - <b>user_id</b> - uuid</br>
    Уникальный ID пользователя получаемый при регистрации
    ### Ответ</br>
    - <font style="color: green;">200 OK</font></br>
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
   ### Запрос (Query params)</br>
   - <b>phone_number</b> - string</br>
   Номер телефона пользователя в формате +7(XXX)XXX-XX-XX
   - <b>user_id</b> - uuid</br>
   Уникальный ID пользователя получаемый при регистрации (обновляемый параметр)
  ### Ответ
  - <span style="color: green;">
  