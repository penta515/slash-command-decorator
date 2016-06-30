# -*- coding: utf-8 -*-
import logging
from functools import wraps
from reaction import Reaction
from slash_command import SlashCommand

logger = logging.getLogger()

__title__ = 'slash-command-decorator'
__version__ = '0.0.1'


def lambda_manager(function):
    def wrap(*args, **kwargs):
        try:
            SlashCommand.set_lambda_object(args[0], args[1])
            function(*args, **kwargs)
        except Exception as exception:
            logger.error(exception)
            raise
    return wrap


def respond_to_option(matchstr="^$"):
    def _decoration(function):
        @wraps(function)
        def wrap(*args, **kwargs):
            reaction = Reaction(*[matchstr, args[0], args[1], args[2], args[3]])
            if reaction.match(0):
                return function(reaction)
        return wrap
    return _decoration
