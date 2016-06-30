# -*- coding: utf-8 -*-
import re
import urllib2
import json
from copy import deepcopy
from message import Message


class Reaction(object):
    def __init__(self, pattern, event, context, client, config):
        self._pattern = pattern
        self._event = event
        self._context = context
        self._client = client
        self._config = config
        self._match_pattern = re.search(self._pattern, event.text)

    def in_channel(self, message, args={}):
        config = dict(deepcopy(self._config), **args)
        headers = {"content-type": "application/json"}
        config["text"] = message
        config["response_type"] = "in_channel"
        req = urllib2.Request(
                self.event.response_url,
                json.dumps(config),
                headers)
        urllib2.urlopen(req)

    def ephemeral(self, message, args={}):
        config = dict(deepcopy(self._config), **args)
        headers = {"content-type": "application/json"}
        config["text"] = message
        config["response_type"] = "ephemeral"
        req = urllib2.Request(
                self.event.response_url,
                json.dumps(config),
                headers)
        urllib2.urlopen(req)

    def send(self, message, args={}):
        config = dict(deepcopy(self._config), **args)
        config["link_names"] = 1
        self._client.chat.post_message(
            self.event.channel_id,
            message,
            **config
        )

    def reply(self, message, args={}):
        config = dict(deepcopy(self._config), **args)
        reply_message = Message(message).user([self.event.user_name])
        config["link_names"] = 1
        self._client.chat.post_message(
            self.event.channel_id,
            reply_message,
            **config
        )

    def match(self, index):
        if self._match_pattern:
            return self._match_pattern.group(index)
        else:
            return None

    @property
    def event(self):
        return self._event

    @property
    def context(self):
        return self._context
