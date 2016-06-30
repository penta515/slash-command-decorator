# -*- coding: utf-8 -*-
from slash_command_decorator.event import Event


class TestEvent(object):
    def setup_method(self, method):
        event = {
            "body": "token=hogehoge&team_id=T0AAAAAAA&team_domain=test-domain&channel_id=C0AAAAAAA&channel_name=general&user_id=U0AAAAAAA&user_name=penta515&command=%2Ftest&text=option&response_url=https%3A%2F%2Fhooks%2Eslack%2Ecom%2Fcommands%2FT0AAAAAAA%2F11111111111%2F111111111111111111"
        }
        self.event = Event(event)

    def test_properties(self):
        assert self.event.channel_id == "C0AAAAAAA"
        assert self.event.channel_name == "general"
        assert self.event.command == "/test"
        assert self.event.text == "option"
        assert self.event.response_url == "https://hooks.slack.com/commands/T0AAAAAAA/11111111111/111111111111111111"
        assert self.event.team_domain == "test-domain"
        assert self.event.team_id == "T0AAAAAAA"
        assert self.event.token == "hogehoge"
        assert self.event.user_name == "penta515"
        assert self.event.user_id == "U0AAAAAAA"
