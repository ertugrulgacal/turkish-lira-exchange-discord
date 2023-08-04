import discord
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

options = ["dolar", "euro", "sterlin", "bitcoin", "faiz"]

def getUSD():
	result = requests.get("https://www.doviz.com/")
	soup = BeautifulSoup(result.content, 'lxml')
	dom = etree.HTML(str(soup))
	return dom.xpath('//*[@data-socket-key="USD"]')[0].text

def getEUR():
	result = requests.get("https://www.doviz.com/")
	soup = BeautifulSoup(result.content, 'lxml')
	dom = etree.HTML(str(soup))
	return dom.xpath('//*[@data-socket-key="EUR"]')[0].text

def getGBP():
	result = requests.get("https://www.doviz.com/")
	soup = BeautifulSoup(result.content, 'lxml')
	dom = etree.HTML(str(soup))
	return dom.xpath('//*[@data-socket-key="GBP"]')[0].text

def getBTC():
	result = requests.get("https://www.doviz.com/")
	soup = BeautifulSoup(result.content, 'lxml')
	dom = etree.HTML(str(soup))
	return dom.xpath('//*[@data-socket-key="bitcoin"]')[0].text

def getFAIZ():
	result = requests.get("https://www.doviz.com/")
	soup = BeautifulSoup(result.content, 'lxml')
	dom = etree.HTML(str(soup))
	return dom.xpath('//*[@data-socket-key="TAHVIL"]')[0].text

@client.event
async def on_ready():
	print("{0.user} kullanmaya hazir.".format(client))

@client.event
async def on_message(message):
	msg = message.content

	if options[0] in msg:
		await message.channel.send("$1 = ₺" + getUSD())
	if options[1] in msg:
		await message.channel.send("€1 = ₺" + getEUR())
	if options[2] in msg:
		await message.channel.send("£1 = ₺" + getGBP())
	if options[3] in msg:
		await message.channel.send("₿1 = " + getBTC())
	if options[4] in msg:
		await message.channel.send("FAIZ = %" + getFAIZ())

f = open('token.json')
data = json.load(f)

client.run(data["TOKEN"])