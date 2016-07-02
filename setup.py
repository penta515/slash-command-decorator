import codecs
import os
from setuptools import setup

dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, 'README.md'), encoding='utf-8').read()
)

setup(
    name='slash-command-decorator',
    version='0.0.3',
    description='Useful Slack Slash Command decorators for AWS Lambda.',
    long_description=long_description,
    author='penta515',
    author_email='penta0515@gmail.com',
    url='https://github.com/penta515/slash-command-decorator',
    packages=['slash_command_decorator'],
    install_requires=['slacker']
)
