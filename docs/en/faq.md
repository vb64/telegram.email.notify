# EmailGateBot FAQ

- [How reliable is the bot hosting?](#how-reliable-is-the-bot-hosting-how-big-is-the-chance-that-the-bot-will-stop-working-at-the-most-crucial-moment)
- [What does the message "processed earlier" mean?](#i-forget-to-click-allow-for-an-incoming-email-at-night-today-morning-i-click-on-allow-and-it-shows-processed-early-what-happened)

## How reliable is the bot hosting? How big is the chance that the bot will stop working at the most crucial moment?

The bot is implemented on the Google App Engine Standard Environment platform and uses as a hosting the
[Google data center in Council Bluffs](https://www.google.com/about/datacenters/inside/locations/council-bluffs/), Iowa, USA.
The equipment of this data center also provides the work of regular Google services (Search, Mail, Maps, etc.)

So the chance of the bot stop work by hosting reason is equal to the chance of the termination of Google services in the relevant region of the United States.

## I forget to click 'allow' for an incoming email at night. Today morning i click on 'allow' and it shows 'processed early'. What happened?

The request to process inbound email is active in one hour.
If you did not respond to this request within an hour, the incoming email is automatically rejected.

- Go to [@EmailGateBot](http://t.me/EmailGateBot?start=utm_KDaxQG000_github-en-faq)
