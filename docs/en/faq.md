# EmailGateBot FAQ

## How reliable is the bot hosting? How big is the chance that the bot will stop working at the most crucial moment?

The bot is implemented on the Google App Engine Standard Environment platform and uses as a hosting the [Google data center in Council Bluffs](https://www.google.com/about/datacenters/inside/locations/council-bluffs/), Iowa, USA. The equipment of this data center also provides the work of regular Google services (Search, Mail, Maps, etc.)

So the chance of the bot stop work by hosting reason is equal to the chance of the termination of Google services in the relevant region of the United States.

## I forget to click 'allow' for an incoming email at night. Today morning i click on 'allow' and it shows 'processed early'. What happened?

The request to process inbound email is active in one hour. If you did not respond to this request within an hour, the incoming email is automatically rejected.

## How to change the email addresses from that are allowed to post to the chat? I want to delete the address.

When the message from the new email address first arrives at the chat email address, the bot asks you what to do with letters from this address. If you press the menu button "Whitelisted" or "Blacklisted", then this email address falls into the "white" or "black" address list, respectively.

Subsequent letters from addresses from the "white" list are published automatically, and letters from addresses from the "black" list are ignored. If you later changed your initial decision and want to prevent a white-list address from automatically posting, you need to do the following.

Send the `/start` command in private with the bot, select the group where you want to delete the email address, select the "Manage white list" menu item (at the very end of the menu, scroll the mouse wheel), select the desired email address from the list of addresses, select from the menu item "Remove".

Managing a "black" list is similar to managing a "white" list.
