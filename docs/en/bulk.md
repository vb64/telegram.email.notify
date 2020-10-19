# Bulk messaging with EmailGateBot

Assume, you added EmailGateBot in 1000 chat rooms and want to publish your text in all these chat rooms.
You send a message to the address of one chat and add the remaining 999 addresses in the 'CC' field.
EmailGateBot will send your message to 1000 chats in a few minutes.

The situation is different if the message contains a picture.
EmailGateBot has a limit on the number of published pictures attached to email: 120 pictures per day.
Therefore, this method is not suitable for this case.

EmailGateBot offers an alternative way to send mass messages with pictures.
You need to send a message with a picture to the address `post@telegram-email.appspotmail.com`

In the Subject field of this letter, you need to place a list of chat codes where you need to send this message.
The chat code is the part before the '@' character in the email address used for posting to the chat.

For example, if you use the email address obtained from EmailGateBot `123456789@telegram-email.appspotmail.com` for posting in the chat, the chat code will be `123456789`.
Chat codes in the subject field of the letter should be separated by spaces.

With this method of sending, your picture will be uploaded to Telegram once and
EmailGateBot will be able to send a message with a picture to the specified chat list without errors.

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-bulk)
- Return [to TOC](guide.md)
- Next: [Referral program](referrals.md)
