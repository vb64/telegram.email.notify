# Преобразование текста сообщения для @EmailGateBot в Telegram Messenger

[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/2ace560fa61c481488dec980d2e3d6f4)](https://www.codacy.com/manual/vb64/telegram.email.notify?utm_source=github.com&utm_medium=referral&utm_content=vb64/telegram.email.notify&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2f7d4597eef143d99014e59379b4b6a4)](https://app.codacy.com/manual/vb64/telegram.email.notify?utm_source=github.com&utm_medium=referral&utm_content=vb64/telegram.email.notify&utm_campaign=Badge_Grade_Dashboard)

@EmailGateBot публикует содержание отправленного ему email в каналах и группах Telegram.

Вы можете автоматически преобразовывать текст сообщения для email из белого списка чата. Для этого вам нужно развернуть в сети Internet веб-сервер, принимающий POST запросы по постоянному адресу. Запрос по этому адресу не должен требовать авторизации.

@EmailGateBot посылает POST-запросы с данными в теле запроса (данные передаются именно в теле запроса, а не как значение какого-то поля формы).
Данные представлют собой текст в кодировке UTF-8 и имеют следующий формат.

Первая строка содержит поле "Тема" (subject) полученного ботом email и перевод строки. Последующие строки содержат тело email, включая html-разметку.

Ваша программа должен вернуть ответ с кодом 200 и заголовком 'Content-Type=text/plain'. Текст для публикации в чате Telegram должен содержаться в теле ответа.

Если ваша программа вернет код ответа, отличающийся от 200, то @EmailGateBot проигнорирует ваш ответ и применит свои стандартные правила преобразования содержимого полученного email для публикации в Telegram.

Этот проект представляет собой реализацию такого преобразования для почтовых рассылок некоторых популярных ресурсов. Проект написан на python/flask и предназначен для разертывания на Google Cloud Platform AppEngine Standard Environment.

Действующая версия [находится здесь](https://text-transform-198104.appspot.com).