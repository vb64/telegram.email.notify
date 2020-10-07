# Editing published messages with EmailGateBot

You can change Telegram messages from the bot by sending a reply to that message (with a quotation).
The text in the original Telegram message will be replaced by text from your reply.

To use markup in updated message, include special code `###text_mode markdown` or `###text_mode HTML` at the separate line of your reply.
This line doesnt be included in the updated message.

There are some limitations.

- in groups and supergroups to edit bot messages, a user must add a bot to this group
- editing works in channels where the mode 'signed messages' is on
- editing does not work in private chat with the bot
- editing does not work for messages published earlier than February 13, 2018 18:00 GMT

The bot automatically deletes your reply with a new message text if it has the permitting to delete messages in the corresponding chat.
If the bot does not have such permission, you will need to delete your answer yourself (if necessary).

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-editing)
- Return [to TOC](guide.md)
- Next: [Bulk messaging](bulk.md)
