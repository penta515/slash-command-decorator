# -*- coding: utf-8 -*-
from slacker import Slacker
from event import Event


class SlashCommand(object):

    EVENT = None
    CONTEXT = None

    def __init__(self, token, config):
        self.config = config
        self.client = Slacker(token)

    def start(self, *functions):
        for function in functions:
            function(SlashCommand.EVENT,
                     SlashCommand.CONTEXT,
                     self.client,
                     self.config)

    @classmethod
    def set_lambda_object(cls, event, context):
        cls.EVENT = Event(event)
        cls.CONTEXT = context
