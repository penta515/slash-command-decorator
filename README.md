# slash-command-decorator
slash-command-decorator is a simple decorator for the use of AWS Lambda as the [Slack Slash Command](https://api.slack.com/slash-commands) backend.

[![CircleCI](https://circleci.com/gh/penta515/slash-command-decorator.svg?style=svg)](https://circleci.com/gh/penta515/slash-command-decorator) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE) 

## Installation
The latest release of slash-command-decorator can be installed via pip

```
$ pip install slash-command-decorator
```

An alternative install method would be manually installing it leveraging `setup.py`

```
$ git clone https://github.com/penta515/slash-command-decorator
$ cd slash-command-decorator
$ python setup.py install
```

## Set the Query String in the event

In handler function `event.body` parameter, it is necessary to set up URL query string that was tranmitted by Slack 


###Example event.body

```python
"token=aCec9XZPS6klbnAAAAAAAAAA&team_id=T0AAAAAAA&team_domain=test-domain&channel_id=C0AAAAAAA&channel_name=general&user_id=U0AAAAAAA&user_name=hoge&command=%2Fcommand&text=hoge&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT0JQU92NA%2F1234567890%2Faaaaaaaaaaaaaaaaaaa"
```

## Basic usage
Usage examples are included in the [samples directory](https://google.co.jp)


```python
# -*- coding: utf-8 -*-
from __future__ import print_function
from slash_command_decorator.slash_command import SlashCommand
from slash_command_decorator import (
    lambda_manager,
    respond_to_option
)

SLACK_API_TOKEN = "xoxp-12345678901-12345678901-12345678901-hogefugapiyo"
CONFIG = {
    "username": "Slash Command",
    "icon_emoji": ":penguin:"
}


@lambda_manager
def lambda_handler(event, context):
    @respond_to_option("^help$")
    def help_option(reaction):
        reaction.ephemeral("HELP!")

    @respond_to_option("^hoge$")
    def hoge_option(reaction):
        reaction.in_channel("HOGE!")

    @respond_to_option("^fuga$")
    def fuga_option(reaction):
        reaction.send("FUGA!")

    @respond_to_option("^piyo$")
    def piyo_option(reaction):
        reaction.reply("PIYO!")

    SlashCommand(
        token=SLACK_API_TOKEN,
        config=CONFIG
    ).start(
        help_option,
        hoge_option,
        fuga_option,
        piyo_option
    )

```

###Response Messages
####ephemeral 
 
```
@respond_to_option("^help$")
def help_option(reaction):
    reaction.ephemeral("HELP!")
```

####in_channel

```
@respond_to_option("^help$")
def help_option(reaction):
    reaction.in_channel("HELP!")
```

####send

```
@respond_to_option("^help$")
def help_option(reaction):
    reaction.send("HELP!")
```

####reply

```
@respond_to_option("^help$")
def help_option(reaction):
    reaction.reply("HELP!")
```

## Running tests

```
$ py.test tests
```
