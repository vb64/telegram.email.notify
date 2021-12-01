# EmailGateBot FAQ

- [How reliable is the bot hosting?](#how-reliable-is-the-bot-hosting-how-big-is-the-chance-that-the-bot-will-stop-working-at-the-most-crucial-moment)
- [What does the message "processed earlier" mean?](#i-forget-to-click-allow-for-an-incoming-email-at-night-today-morning-i-click-on-allow-and-it-shows-processed-early-what-happened)
- [I turned the group into a supergroup and EmailGateBot stopped sending messages there. What to do?](#i-turned-the-group-into-a-supergroup-and-emailgatebot-stopped-sending-messages-there-what-to-do)
- [I created a public group with a bot. But this group does not appear in the list of groups in the bot. What to do?]

## How reliable is the bot hosting? How big is the chance that the bot will stop working at the most crucial moment?

The bot is implemented on the Google App Engine Standard Environment platform and uses as a hosting the
[Google data center in Council Bluffs](https://www.google.com/about/datacenters/inside/locations/council-bluffs/), Iowa, USA.
The equipment of this data center also provides the work of regular Google services (Search, Mail, Maps, etc.)

So the chance of the bot stop work by hosting reason is equal to the chance of the termination of Google services in the relevant region of the United States.

## I forget to click 'allow' for an incoming email at night. Today morning i click on 'allow' and it shows 'processed early'. What happened?

The request to process inbound email is active in one hour.
If you did not respond to this request within an hour, the incoming email is automatically rejected.

## I turned the group into a supergroup and EmailGateBot stopped sending messages there. What to do?

With this transformation, the group's Telegram ID has changed and for the bot, it is actually a new group.

Remove the bot from this group, it will say something like "lost access".
If the group remains in the list, select it and then the "Remove from list" menu item.
Add the bot to the group again, it will appear in the list and its email address will change.

If the group had the premium mode enabled, it will stop working, because the mode is tied to the Telegram group ID.
In this case, write to the [support group](https://t.me/joinchat/CJ4MSEfmFlaDevQOeMVoLg) to restore premium mode for the paid period.

## I created a public group with a bot. But this group does not appear in the list of groups in the bot. What to do?

Try to remove the bot from the group and then add it there again. If the group after that does not appear in the list, report the problem in the [support group](https://t.me/joinchat/CJ4MSEfmFlaDevQOeMVoLg).

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-faq)
