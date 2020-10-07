# Automatic text conversion with EmailGateBot

Quite often automatically generated email messages that are sent to Telegram via EmailGateBot,
contain redundant and service information that is not required by the user, but only clutters the chat.
Such messages need to be processed in such a way as to leave only important and necessary information.

Another common case is the publication of messages from sources that you do not control.
In this situation, the automatic moderation of incoming content is often required.

For such cases, and also similar to them, EmailGateBot provides the function of automatic text conversion.

This function is available via the 'Set text-transform' item in the menu for managing the allowlist email

- chat managing menu
- 'Allowlist'
- choose email

There you can specify the server address on the Internet, where the bot will send the text from the received email.
In the Telegram chat, the bot will publish the text from the response of this server.

You can create and deploy your own server or use the [open-source notification handler](transform_text.md) built into EmailGateBot.

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-conversion)
- Return [to TOC](guide.md)
- Next: [Editing published messages](editing_published.md)
