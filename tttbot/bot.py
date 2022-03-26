import discord
from pathlib import Path
import logging
logger = logging.getLogger(__name__)

# PROJECT IMPORTS
from tttbot import Config 

# TYPE CHECKING
from typing import *

class Client(discord.Client):

    def __init__(self, config_path: Union[str, Path]):
        super().__init__()
        self.config = Config("config.yml")

    def run(self):
        super().run(self.config["token"])

    # @client.event
    async def on_ready(self):
        logger.info('We have logged in as {0.user}'.format(self))

    # @client.event
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            logger.debug("hello")
            await message.channel.send('Hello!')
    