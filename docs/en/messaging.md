# How to messaging with EmailGateBot

You can be messaging to Telegram channel and groups by sending emails to `SPECIAL_CODE@telegram-email.appspotmail.com`

For posting to group and supergroup just add the bot as a member.
The bot must have the rights to publish messages and media content in this group.

The bot will inform you in private the email address for posting messages to this group.

To post messages to the channel, send the command `/helpchannel` to the private chat with the bot.
The bot will tell you a special code like
```
/start xxxxxxx
```
Add EmailGateBot to the desired channel as an administrator, and then send the received code to the channel.

The bot will inform you in private the email address for posting messages to this channel.

When you send the first message to the chat from the new mailbox, the bot will ask you for confirmation of receiving emails from this address.
To prevent a bot from writing to the chat, delete it from the corresponding channel/group.

The size of the text of the letter published via EmailGateBot should not exceed 100 Kb. The total size of the letter, including files attached to the letter, should not exceed 30 Mb.
Messages exceeding these limits are ignored by the bot.

From the text of your email, the bot publishes the first 4 Kb, this is a limit on the size of messages in the Telegram messenger.

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-messaging)
- Return [to TOC](guide.md)
- Next: ['stoplist' and 'allowlist'](stop_allow_list.md)
