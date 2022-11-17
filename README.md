# Telegram Feedback Bot

## Конфигурирование

- Скопируйте файл `config.json.dist` и назовите его `config.json`

```shell
cp ./config.json.dist ./config.json
```

- Впишите токен бота в поле `token`
- Впишите ваш telegram ID в поле `admin_ids`. Можно указать несколько через запятую
- Впишите приветствующее пользователей сообщение в поле `start_message`

Идею взял у [MasterGroosha](https://github.com/MasterGroosha/telegram-feedback-bot).
Принцип работы бота такой же, только без излишеств и работает стабильной версии aiogram'а на поллинге.