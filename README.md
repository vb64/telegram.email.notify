# Message text transformation for @EmailGateBot in Telegram Messenger
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/vb64/telegram.email.notify/telegram.email.notify%20tests?label=Python%202.7&style=plastic)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/2ace560fa61c481488dec980d2e3d6f4)](https://www.codacy.com/manual/vb64/telegram.email.notify?utm_source=github.com&utm_medium=referral&utm_content=vb64/telegram.email.notify&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2f7d4597eef143d99014e59379b4b6a4)](https://app.codacy.com/manual/vb64/telegram.email.notify?utm_source=github.com&utm_medium=referral&utm_content=vb64/telegram.email.notify&utm_campaign=Badge_Grade_Dashboard)

@EmailGateBot allows messaging to channels and groups of Telegram by emailing to the special mailbox.

You can automatically transform text of messages for emails from the whitelist of the chat. To do this, you need to deploy a web server on the Internet that accepts POST requests at a permanent address. A request to this address should not require authorization.

@EmailGateBot sends POST requests with data in the request body (the data is transmitted exactly in the request body, and not as the value of some form field). The data is UTF-8 encoded text and has the following format.

The first line contains the subject field of the email received by the bot and a line feed. The following lines contain the body of the email, including HTML markup.

Your program should return a response with code 200 and the header 'Content-Type=text/plain'. The text for publication in the Telegram chat should be contained in the response body.

If your program returns a response code other than 200, then @EmailGateBot will ignore your reply and apply its standard rules for converting the contents of the received email for publication on Telegram.

This project is an implementation of such a conversion for mailing lists of some popular resources. The project is written in python/flask and is intended to be deployed to the Google Cloud Platform AppEngine Standard Environment.

The live version is [located here](https://text-transform-198104.appspot.com).
