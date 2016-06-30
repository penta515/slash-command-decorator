# -*- coding: utf-8 -*-
from slash_command_decorator.message import Message


class TestMessage(object):
    def setup_method(self, method):
        self.text = "Test Message."
        self.user = ["hoge", "fuga"]
        self.message = Message(self.text)

    def test_all(self):
        assert self.message.all() == "@all: Test Message."

    def test_channel(self):
        assert self.message.channel() == "@channel: Test Message."

    def test_everyone(self):
        assert self.message.everyone() == "@everyone: Test Message."

    def test_group(self):
        assert self.message.group() == "@group: Test Message."

    def test_here(self):
        assert self.message.here() == "@here: Test Message."

    def test_user(self):
        assert self.message.user(self.user) == "@hoge: @fuga: Test Message."
