# -*- coding: utf-8 -*-


class Message(object):
    def __init__(self, message):
        self.message = message

    def all(self):
        return self._generate_message(["all"])

    def channel(self):
        return self._generate_message(["channel"])

    def everyone(self):
        return self._generate_message(["everyone"])

    def group(self):
        return self._generate_message(["group"])

    def here(self):
        return self._generate_message(["here"])

    def user(self, users):
        return self._generate_message(users)

    def _generate_message(self, mentions):
        return "@%s: %s" % (": @".join(mentions), self.message)
