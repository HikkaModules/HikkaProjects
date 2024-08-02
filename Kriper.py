from hikkatl.types import Message
from .. import loader
from .. import utils
import time


@loader.tds
class Kriper(loader.Module):
	"""Мем из ТикТока"""
	strings = {"name": "SigmaKriper"}

	@loader.command()
	async def kriper(self, message: Message):
		"""Запуск"""
		await utils.answer(message, "Сигма крипер вместе с сигма свинкой шли по полю")
		time.sleep(3)
		await utils.answer(message, "Прилепили на себя алмазы по приколу")
		time.sleep(3)
		await utils.answer(message, "А навстречу им влачился слишком грустный школьник")
		time.sleep(3)
		await utils.answer(message, "Мальчик, что с тобой случилось?")
		time.sleep(2)
		await utils.answer(message, "Я получил двойку!")
		time.sleep(3)
		await utils.answer(message, "Да ты не плачь, школьник")
		time.sleep(2)
		await utils.answer(message, "Ведь у нас есть штрих сочный")
		time.sleep(2)
		await utils.answer(message, "Мы замажем тебе двойку")
		time.sleep(3)
		await utils.answer(message, "Красной ручкой нарисуем")
		time.sleep(3)
		await utils.answer(message, "Новую пятерку")
