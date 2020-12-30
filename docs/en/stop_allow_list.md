# 'stoplist' and 'allowlist' in EmailGateBot

When the message from the new email address first arrives at the chat email address, the bot asks you what to do with letters from this address.

If you press the menu button 'Allow permanently' or 'Disable permanently', then this email address falls into the 'allowlist' or 'stoplist', respectively.

Subsequent letters from addresses from the 'allowlist' are published automatically, and letters from addresses from the 'stoplist' are ignored.
If you later changed your initial decision and want to prevent a allowlist address from automatically posting, you need to do the following.

- send the `/start` command in private with the bot
- select the group where you want to delete the email address
- select the 'Allowlist' menu item (at the very end of the menu, scroll the mouse wheel)
- select the desired email address from the list of addresses
- select from the menu item 'Remove'

Managing a 'stoplist' is similar to managing a 'allowlist'.

You can completely disable the verification of incoming email addresses and automatically publish all incoming mail to the channel/group address,
displaying the address from which it was received.

Use this mode carefully. This is a potential opportunity for an attacker to spam your channels and groups.

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-stoplist)
- Return [to TOC](guide.md)
- Next: [Pictures, videos, stickers and other types of media](media.md)
