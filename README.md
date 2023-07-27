# Message text transformation for @EmailGateBot in Telegram Messenger

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/telegram.email.notify/pep257.yml?label=Pep257&style=plastic&branch=master)](https://github.com/vb64/telegram.email.notify/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/telegram.email.notify/py3.yml?label=Python%203.7-3.11&style=plastic&branch=master)](https://github.com/vb64/telegram.email.notify/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2ace560fa61c481488dec980d2e3d6f4)](https://app.codacy.com/gh/vb64/telegram.email.notify/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/2ace560fa61c481488dec980d2e3d6f4)](https://app.codacy.com/gh/vb64/telegram.email.notify/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

[In Russian](README-ru.md)

@EmailGateBot allows messaging to channels and groups of Telegram by emailing to the special mailbox.

You can automatically transform text of messages for emails from the whitelist of the chat. To do this, you need to deploy a web server on the Internet that accepts POST requests at a permanent address. A request to this address should not require authorization.

@EmailGateBot sends POST requests with data in the request body (the data is transmitted exactly in the request body, and not as the value of some form field). The data is UTF-8 encoded text and has the following format.

The first line contains the subject field of the email received by the bot and a line feed. The following lines contain the body of the email, including HTML markup.

Your program should return a response with code 200 and the header 'Content-Type=text/plain'. The text for publication in the Telegram chat should be contained in the response body.

If your program returns a response code other than 200, then @EmailGateBot will ignore your reply and apply its standard rules for converting the contents of the received email for publication on Telegram.

This project is an implementation of such a conversion for mailing lists of some popular resources. The project is written in python/flask and is intended to be deployed to the Google Cloud Platform AppEngine Standard Environment.

The live version is [located here](https://text-transform-198104.appspot.com).
