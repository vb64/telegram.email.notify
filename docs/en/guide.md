# Emailing to the channels and groups of Telegram Messenger.

![EmailGateBot logo](img/logo.png)

@EmailGateBot allows messaging to channels and groups of Telegram by emailing to the special mailbox.

The bot can publish files of any type supported by Telegram (photo, sticker, voice, etc), buttons for navigating and polling buttons with emoji icons. It is possible to post deferred messages at the specified time (up to 30 days in advance), automatically change the published text according to your rules, view the list of users who participated in the poll. Published messages can contain Markdown or HTML markup. Messages can be 'pinned' and later edited in Telegram.

## How to messaging

You can be messaging to Telegram channel and groups by sending emails to `SPECIAL_CODE@telegram-email.appspotmail.com`

For posting to group and supergroup just add the bot as a member. The bot will tell you the code that you need to specify in the email address so that messages reach this group.

For messages to the channel add the bot as channel administrator, then send to the bot /start command and follow instructions.

When you send the first message to the chat from the new mailbox, the bot will ask you for confirmation of receiving emails from this address. To prevent a bot from writing to the chat, delete it from the corresponding channel/group.

## 'black' and 'white' mail lists

When the message from the new email address first arrives at the chat email address, the bot asks you what to do with letters from this address. If you press the menu button 'Whitelisted' or 'Blacklisted', then this email address falls into the 'white' or 'black' address list, respectively.

Subsequent letters from addresses from the 'white' list are published automatically, and letters from addresses from the 'black' list are ignored. If you later changed your initial decision and want to prevent a white-list address from automatically posting, you need to do the following.

Send the /start command in private with the bot, select the group where you want to delete the email address, select the 'Manage white list' menu item (at the very end of the menu, scroll the mouse wheel), select the desired email address from the list of addresses, select from the menu item 'Remove'.

Managing a 'black' list is similar to managing a 'white' list.
