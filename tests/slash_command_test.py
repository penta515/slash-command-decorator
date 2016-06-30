# -*- coding: utf-8 -*-
from slash_command_decorator.slash_command import SlashCommand


class TestSlashCommand(object):
    def setup_method(self, method):
        event = {
            "body": "token=hogehoge&team_id=T0AAAAAAA&team_domain=test-domain&channel_id=C0AAAAAAA&channel_name=general&user_id=U0AAAAAAA&user_name=penta515&command=%2Ftest&text=option&response_url=https%3A%2F%2Fhooks%2Eslack%2Ecom%2Fcommands%2FT0AAAAAAA%2F11111111111%2F111111111111111111"
        }
        self.event = Event(event)
        self.context = "context"

    def set_lambda_object(self):
        SlashCommand.set_lambda_object(self.event, self.context)
        assert SlashCommand.EVENT == self.event
        assert SlashCommand.CONTEXT == "context"
