# -*- coding: utf-8 -*-
from urlparse import parse_qs


class Event(object):
    def __init__(self, event):
        self.params = parse_qs(event['body'])

    @property
    def channel_id(self):
        return self.params['channel_id'][0]

    @property
    def channel_name(self):
        return self.params['channel_name'][0]

    @property
    def command(self):
        return self.params['command'][0]

    @property
    def text(self):
        return self.params['text'][0]

    @property
    def response_url(self):
        return self.params['response_url'][0]

    @property
    def team_domain(self):
        return self.params['team_domain'][0]

    @property
    def team_id(self):
        return self.params['team_id'][0]

    @property
    def token(self):
        return self.params['token'][0]

    @property
    def user_name(self):
        return self.params['user_name'][0]

    @property
    def user_id(self):
        return self.params['user_id'][0]
