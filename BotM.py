from hikkatl.types import Message
from .. import loader
from .. import utils
import requests

@loader.tds
class botm(loader.Module):
	"""BotM"""
	strings = {"name": "BotM"}

	@loader.command()
	async def reqb(self, message: Message):
		""".reqb <bot token> <chatid> <message> Recomended to send command in local messages""" 
		await utils.answer(message, "Sended!")
		args = utils.get_args(message)
		token = str(args[0].strip())
		chatid = str(args[1].strip())
		message = str(args[2].strip())
		r = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chatid + "&text=" + message)
		print("Sended! Status code:", r.status_code)
		print("Text:", r.text)
    
