# Emoji emoticons and text formatting with EmailGateBot

Emoji emoticons can be included in the message text.
In the text of the email in curly brackets specify the code of the desired emoji and this emoticon will appear in the message published in Telegram.
For instance:

```
{0001F44D}
```

To find out the emoticon code, send the command `/emojicode` to the bot and then the emoticon you need.

The text in the email may contain a markup of two types supported by Telegram:

- [Markdown](https://core.telegram.org/bots/api#markdown-style)
- [HTML](https://core.telegram.org/bots/api#html-style)

To enable markup, add follows code at the separate line of email body:

```
###text_mode markdown
```

or

```
###text_mode html
```

A string with this code will not be included in the published message.

If you use HTML markup, then your email program should send an email with the header

```
Content-Type: text/plain
```

Otherwise, the Html tags in the message will not work.

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-formatting)
- Return [to TOC](guide.md)
- Next: [Automatic text conversion](text_conversion.md)
