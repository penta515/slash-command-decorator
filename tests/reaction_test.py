# -*- coding: utf-8 -*-
from slash_command_decorator.reaction import Reaction
from slash_command_decorator.event import Event
from mock import MagicMock


class TestReaction(object):
    def setup_method(self, method):
        event = {
            "body": "token=hogehoge&team_id=T0AAAAAAA&team_domain=test-domain&channel_id=C0AAAAAAA&channel_name=general&user_id=U0AAAAAAA&user_name=penta515&command=%2Ftest&text=option%20hoge&response_url=https%3A%2F%2Fhooks%2Eslack%2Ecom%2Fcommands%2FT0AAAAAAA%2F11111111111%2F111111111111111111"
        }
        self.pattern = "option\s(.*)"
        self.event = Event(event)
        self.context = MagicMock()
        self.client = MagicMock()
        self.config = {
            "username": "SlashCommand",
            "icon_emoji": ":bow:"
        }
        self.reaction = Reaction(self.pattern,
                                 self.event,
                                 self.context,
                                 self.client,
                                 self.config)

    def test_match(self):
        assert self.reaction.match(0) == "option hoge"
        assert self.reaction.match(1) == "hoge"

