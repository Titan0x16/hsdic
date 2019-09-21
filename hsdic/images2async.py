import requests
import math
import json
import asyncio
import aiohttp
import datetime
from time import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
from hearthstone.deckstrings import Deck
import os

BASE_DIR2 = os.path.dirname(os.path.dirname(__file__))
test_json = os.path.join(BASE_DIR2, "hsdic"+os.sep+"static"+os.sep+"hsdic"+os.sep+"test.json")
mildrttf = os.path.join(BASE_DIR2, "hsdic"+os.sep+"static"+os.sep+"hsdic"+os.sep+"mild-r.ttf")
x2png = os.path.join(BASE_DIR2, "hsdic"+os.sep+"static"+os.sep+"hsdic"+os.sep+"x2-42.png")

url_en = 'https://art.hearthstonejson.com/v1/render/latest/{lang}/256x/{img}.png'

###################################ASYNC MAGIC STARTS####################################

images_deck_unsorted = []
# images_deck = sorted(images_deck_unsorted, key=lambda value: value[0])
images_deck = {}

async def fetch_content(url, session, i):
	# Все запросы лучше делать через созданную сессию
	# С сессией мы обычно работаем через контестный менеджер. Асинхронный контекстный менеджер with
	async with session.get(url, allow_redirects=True) as response:
		# для вызова асинхронного метода импользуем ключевое cлово await
		data = await response.read() # мотод .read() возвращает бинарные данные (картинку)
		# images_deck_unsorted.append([i, data])
		images_deck.update({i: data})
		# write_image(data)
		# img.paste(data, (320, 240))

async def main2(new_sorted, lang):
	url = 'https://loremflickr.com/320/240'
	tasks = []

	# здесь нужно открыть сессию следовательно нужен контекстный менеджер
	async with aiohttp.ClientSession() as session:
		for i in range(len(new_sorted)):
			task = asyncio.create_task(fetch_content(url_en.format(img = new_sorted[i][-1], lang = lang), session, i))
			tasks.append(task)

		await asyncio.gather(*tasks)



####################################ASYNC MAGIC ENDS#####################################
def main(code, lang):
	start_time = datetime.datetime.now()

	deck = Deck.from_deckstring(code)
	new=[]
	with open(test_json, 'rb') as f:
		data = json.load(f) #list of dicts
		for i in range(len(deck.cards)):
			ext = data[str(deck.cards[i][0])]
			start = [deck.cards[i][0], deck.cards[i][1]]
			start.extend(ext)
			new.append(start)
	# print(new)

	new_sorted = sorted(new, key=lambda student: student[2]) 
	# print(new_sorted) #[[138, 2, 2, 'NEUTRAL', 'NEW1_021'], [47982, 1, 3, 'MAGE', 'BOT_103'],...] #id, quntity, cost, class, id


	lang = lang
	asyncio.run(main2(new_sorted, lang))
	# print(images_deck[0][0])
	print(images_deck.keys())


	l = len(deck.cards)
	image_y = math.ceil(l/7)

	card_width = 256
	card_height = 387
	card_down = 340
	position_x = card_width
	position_y = card_height

	img = Image.new('RGB', (card_width*7, card_height*image_y))

	x2 = Image.open(x2png) #x2-42.png 56,44
	for i in range(l):
		# print(deck.cards[i][0])
		if i <= 6:
			position = (position_x*i, position_y*0)
		elif i <=13:
			position = (position_x*(i-7), position_y)
		elif i <=20:
			position = (position_x*(i-7*2), position_y*2)
		elif i <=27:
			position = (position_x*(i-7*3), position_y*3)
		else:
			position = (position_x*(i-7*4), position_y*4)

		# print(position)
		# img.paste(get_image(deck.cards[i][0]), (position))
		# img.paste(images_deck, (position))

		img_part = Image.open(BytesIO(images_deck[i]))
		img.paste(img_part, (position))
		# img.paste(img_part, (320*i, 0))

		print(new_sorted[i])
		if new_sorted[i][1] == 2:
			img.paste(x2, (position[0] + int(card_width/2-28), position[1] + card_down))

	today = datetime.datetime.today()
	file_name = "{}.jpg".format(today.strftime("%Y-%m-%d-%H.%M.%S"))

	# draw some text
	class_ = ''
	for i in range(l):
		if new_sorted[i][3] != 'NEUTRAL':
			class_ = new_sorted[i][3]
			break
		print(new_sorted[i][3])
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(mildrttf, 24)
	draw.text((23, 7),class_ ,(100,100,100), font=font)

	file_name_for_save = os.path.join(BASE_DIR2, "hsdic"+os.sep+"static"+os.sep+"hsdic"+os.sep+file_name)
	img.save(file_name_for_save)


	finish_time = datetime.datetime.now()
	print(finish_time - start_time)
	return file_name
	# img.open()

if __name__ == '__main__':
	lang = 'enUS'
	code_string = 'AAECAaoIAt6CA5ybAw7FA9sD/gPjBdAHpwiTCeKJA4yUA7WYA8aZA/SZA6+nA8qrAwA='
	main(code_string, lang)