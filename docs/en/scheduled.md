# Scheduled, repeatable, and auto-deleted publications EmailGateBot

EmailGateBot can send scheduled messages.
To do this, put the special code in a separate line of your message.
For example:

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

To post a message at a specified time and then automatically delete it, add the `stop` tag after the `start` tag.
For example, the following lines in the body of the message will plan the first publication with its removal after 1 hour
and the repeated publication of the same message 1 hour after the removal of the first.

```
###start 01-01-2019 10:00 stop 01-01-2019 11:00
###start 01-01-2019 12:00
```

Lines with a code will not be included in the published message.
You can schedule publications to 30 days ahead.
Each channel/group queue can contain up to 10 scheduled tasks for free and up to 200 tasks for [paid mode](paid_and_free.md).

To cancel a scheduled task, send the `/start` command in private chat with the bot, and select from the list the chat where the publication is scheduled.
Next, select the "Scheduled:" menu item, then from the list of tasks, select the desired one, in the next menu, select "Revoke task".

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-scheduled)
- Return [to TOC](guide.md)
- Next: [Pinned messages](pinned.md)
