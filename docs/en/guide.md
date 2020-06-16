# Emailing to the channels and groups of Telegram Messenger.

![EmailGateBot logo](../logo.png)

@EmailGateBot allows messaging to channels and groups of Telegram by emailing to the special mailbox.

The bot can publish files of any type supported by Telegram (photo, sticker, voice, etc), buttons for navigating and polling buttons with emoji icons. The list of users participating in the poll can be viewed. It is possible to publish messages at a specified time (up to 30 days ahead), to make repeated and auto-deleted posts. Published messages can contain emoji and Markdown/HTML markup. Messages can be 'pinned' and later edited.

Compared to GmailBot and similar bots, EmailGateBot cannot send outgoing emails from Telegram and does not require access to your email accounts.

- [How to messaging](#how-to-messaging)
- ['stoplist' and 'allowlist'](#stoplist-and-allowlist)
- [Publish pictures and files](#publish-pictures-and-files)
- [Scheduled, repeatable, and auto-deleted publications](#scheduled-repeatable-and-auto-deleted-publications)
- [Pinned messages](#pinned-messages)
- [Polls](#polls)
- [View voters](#view-voters)
- [Emoji emoticons and text formatting](#emoji-emoticons-and-text-formatting)
- [Automatic text conversion](#automatic-text-conversion)
- [Editing published messages](#editing-published-messages)
- [Bulk messaging](#bulk-messaging)
- [List of bot commands](#list-of-bot-commands)
- [Help and support](#help-and-support)

Related

- [EmailGateBot FAQ](faq.md)
- [Notifications from popular resources: YouTube, Twitter, Reddit, etc.](transform_text.md)

## How to messaging

You can be messaging to Telegram channel and groups by sending emails to `SPECIAL_CODE@telegram-email.appspotmail.com`

For posting to group and supergroup just add the bot as a member. The bot will tell you the code that you need to specify in the email address so that messages reach this group.

For messages to the channel add the bot as channel administrator, then send to the bot /start command and follow instructions.

When you send the first message to the chat from the new mailbox, the bot will ask you for confirmation of receiving emails from this address. To prevent a bot from writing to the chat, delete it from the corresponding channel/group.

## 'stoplist' and 'allowlist'

When the message from the new email address first arrives at the chat email address, the bot asks you what to do with letters from this address. If you press the menu button 'Allow permanently' or 'Disable permanently', then this email address falls into the 'allowlist' or 'stoplist', respectively.

Subsequent letters from addresses from the 'allowlist' are published automatically, and letters from addresses from the 'stoplist' are ignored. If you later changed your initial decision and want to prevent a allowlist address from automatically posting, you need to do the following.

Send the /start command in private with the bot, select the group where you want to delete the email address, select the 'Allowlist' menu item (at the very end of the menu, scroll the mouse wheel), select the desired email address from the list of addresses, select from the menu item 'Remove'.

Managing a 'stoplist' is similar to managing a 'allowlist'.

You can completely disable the verification of incoming email addresses and automatically publish all incoming mail to the channel/group address, displaying the address from which it was received.
Use this mode carefully. This is a potential opportunity for an attacker to spam your channels and groups.

## Publish pictures and files

You can publish images by attaching an image file to the email you send. The first 1024 bytes of the text of the letter will be used as a caption for the picture. During the day in this way, you can post no more than 120 pictures. The limit is reset every day at 00:00 GMT. Mass mailing (see further) to several chats via post@telegram-email.appspotmail.com is counted as one picture.

Also, you can publish pictures and files of any type in another way. Send the file to the private chat with a bot. The bot will respond to you with a message that contains a special code. This code should be added as a separate line in the text of the email and your file will be published.

You can send files of the following types: audio, animation, photo, sticker, video, voice, video message, and regular file (document). Files and images sent in this way are not counted for the daily quota of sent pictures.

If you send an email containing the code and the attached image file, the attached image file will be published, but the code will be ignored.

## Scheduled, repeatable, and auto-deleted publications

EmailGateBot can send scheduled messages. To do this, put the special code in a separate line of your message. For example:

```
###start 31-12-2018 23:59
```

In this case, the message will be published in the Telegram at the specified time (UTC time zone used).

To publish a message several times at different times, add additional lines with the desired publication time.

```
###start 31-12-2018 23:00
###start 31-12-2018 23:59
###start 01-01-2019 10:00
```

To post a message at a specified time and then automatically delete it, add the `stop` tag after the `start` tag. For example, the following lines in the body of the message will plan the first publication with its removal after 1 hour and the repeated publication of the same message 1 hour after the removal of the first.

```
###start 01-01-2019 10:00 stop 01-01-2019 11:00
###start 01-01-2019 12:00
```

Lines with a code will not be included in the published message. You can schedule publications to 30 days ahead. Each channel/group queue can contain up to 10 scheduled tasks.

For each channel/group, you can view the queue of scheduled tasks and manage these tasks.

## Pinned messages

A bot can 'pin' messages sent to supergroups and channels if it has the appropriate rights there. To 'pin' a message, add a separate line to the message body.

```
###pin
```

This line will be removed from the published message, and the message itself will be 'pinned' in the target channel/supergroup.

## Polls

EmailGateBot can also be used to create polls with buttons, that have location, titles, and emotions as you need. Messages in Telegram, that were sent via an EmailGateBot, can contain any combination of inline buttons with emoji icons. If you put special string ###buttons in the email text body, the tail of the email after this sign will be interpreted as inline buttons definition.

The text inside square brackets defines the inline button as the poll option. You can put several definitions, separated by spaces, in one row.

```
###buttons
[Yes] [No]
```

The text of buttons title can contain codes, that displaying as emoji icons. A complete list of emoji codes can be [found here](http://www.unicode.org/emoji/charts/full-emoji-list.html) or use the bot command /emojicode to get the code for the desired icon.

If a closed square bracket is followed by an open round bracket (with no spaces), then this button definition is interpreted as the url-link button. Url address must be put inside round brackets.

![EmailGateBot poll](img/poll.jpeg)

And all of this can be mixed in any combination. For example, to create the poll shown in the picture above, the body of the email should be:

```
To be or not to be?
###buttons en
[{0001F44D} Yes] [Maybe] [{0001F44E}{0001F3FF} No]
[{0001F1EC}{0001F1E7} Google](https://google.com)
[{0001F1F7}{0001F1FA} Yandex](https://ya.ru)
[{0001F1E8}{0001F1F3} Baidu](http://www.baidu.com)
```

And the corresponding picture should be attached to the email.

By default, the poll will be active for 30 days from the date of creation. This is the maximum duration of the poll. You can reduce it by setting the duration of the poll in minutes. For example, for a 10-minute poll:

```
###buttons 10
```

## View voters

In polls created with the bot, the button is added: 'Who has voted?'. Follows this button you can see a list of the latest votes in the poll. Each vote is a link to the Telegram profile of the voter.

When viewing the list of voters in the poll results, you can forward a contact from the list or a message from any Telegram user to a private chat with a bot. The bot will tell you how this contact or user voted in the poll.

## Emoji emoticons and text formatting

Emoji emoticons can be included in the message text.
In the text of the email in curly brackets specify the code of the desired emoji and this emoticon will appear in the message published in Telegram. For instance:

```
{0001F44D}
```

To find out the emoticon code, send the command `/emojicode` to the bot and then the emoticon you need.

The text in the email may contain a markup of two types supported by Telegram: [Markdown](https://core.telegram.org/bots/api#markdown-style) or [HTML](https://core.telegram.org/bots/api#html-style). To enable markup, add follows code at the separate line of email body:

```
###text_mode markdown
```

or

```
###text_mode html
```

A string with this code will not be included in the published message. If you use HTML markup, then your email program should send an email with the header

```
Content-Type: text/plain
```

Otherwise, the Html tags in the message will not work.

## Automatic text conversion

Quite often automatically generated email messages that are sent to Telegram via EmailGateBot, contain redundant and service information that is not required by the user, but only clutters the chat. Such messages need to be processed in such a way as to leave only important and necessary information.

Another common case is the publication of messages from sources that you do not control. In this situation, the automatic moderation of incoming content is often required.

For such cases, and also similar to them, EmailGateBot provides the function of automatic text conversion.

This function is available via the 'Set text-transform' item in the menu for managing the allowlist email (chat managing menu, 'Allowlist', choose email). There you can specify the server address on the Internet, where the bot will send the text from the received email. In the Telegram chat, the bot will publish the text from the response of this server.

You can create and deploy your own server or use the [open-source notification handler](transform_text.md) built into EmailGateBot.

## Editing published messages

You can change Telegram messages from the bot by sending a reply to that message (with a quotation). The text in the original Telegram message will be replaced by text from your reply.

To use markup in updated message, include special code `###text_mode markdown` or `###text_mode HTML` at the separate line of your reply. This line doesnt be included in the updated message.

The bot automatically deletes your reply with a new message text if it has the permitting to delete messages in the corresponding chat. If the bot does not have such permission, you will need to delete your answer yourself (if necessary).

There are some limitations.

- editing does not work for messages published earlier than February 13, 2018 18:00 GMT
- editing does not work in private chat with the bot
- in groups and supergroups to edit bot messages, a user must add a bot to this group
- editing works in channels where the mode 'signed messages' is on

## Bulk messaging

Assume, you added EmailGateBot in 1000 chat rooms and want to publish your text in all these chat rooms. You send a message to the address of one chat and add the remaining 999 addresses in the 'CC' field. EmailGateBot will send your message to 1000 chats in a few minutes.

The situation is different if the message contains a picture. When sending a message with a picture in the usual way, this picture will need to be uploaded 1000 times into the Telegram. In this case, errors will occur. Therefore, EmailGateBot does not guarantee the delivery of messages with pictures when sending them in the usual way.

EmailGateBot offers an alternative way to send mass messages with pictures. You need to send a message with a picture to the address post@telegram-email.appspotmail.com

In the Subject field of this letter, you need to place a list of chat codes where you need to send this message. The chat code is the part before the '@' character in the email address used for posting to the chat.

For example, if you use the email address obtained from EmailGateBot `123456789@telegram-email.appspotmail.com` for posting in the chat, the chat code will be '123456789'. Chat codes in the subject field of the letter should be separated by spaces.

With this method of sending, your picture will be uploaded to Telegram once and EmailGateBot will be able to send a message with a picture to the specified chat list without errors.

## List of bot commands

`/start` - The most important command. If you are confused in the bot menu, then you will return to the bot start message with a list of your chats.

`/language` - Sets the language in which the bot communicates with you in a private chat.

`/help` - Brief information on the use of the bot.

`/chatlist` - Creates a CSV file with a list of your chats. It is useful when there are a lot of chats. The file is created in UTF-8 encoding. For each chat are displayed:

- type (channel, group, etc)
- title
- email for messaging

`/emojicode` - For an emoji icon shows the code for use in the polling buttons.

`/clearkeyboard` - If some sloppy or malicious bot has activated and left a custom keyboard in your group, you can remove it by using this command.

`/donate` - For those who wish to support the development of the project.

## Help and support

More information on using the bot and developer contacts can be obtained through the /help command.

[Try EmailGateBot](http://t.me/EmailGateBot)
