import asyncio
import discord
from discord.ext import commands
import openai
import re

intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.playing, name="with ShuppoBot <3")
bot = commands.Bot(command_prefix="e!",activity=activity, status=discord.Status.online, intents=intents)

openai_key = "[Removed]"
openai.api_key = openai_key

import re
@bot.event
async def on_message(message):

        if message.author == bot.user:
            return

        if int(message.author.id) != 851132992289898508:
            print("Author unknown")
            return

        if int(message.channel.id) != 956639433178894397:
            print("Channel unknown")
            return

        await message.channel.trigger_typing()

        message.content = message.content.replace('<@!851132992289898508>', 'ShuppoBot')
        message.content = message.content.replace('<@851132992289898508>', 'ShuppoBot')

        print(message.content)

        response = response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=f"Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou: {message.content}\nMarv:",
                    temperature=0.5,
                    max_tokens=30,
                    top_p=0.3,
                    frequency_penalty=0.5,
                    presence_penalty=0.0
                    )
        print(response)
        generated_text = response['choices'][0]['text']
        if generated_text == '' or generated_text == ' ':
            await message.channel.send("Hmm, i am not sure how to respond to that. " + "<@851132992289898508>")
            return
        print("Raw text:\n", repr(generated_text))
        #response = openai.Edit.create(
        #                    engine="text-davinci-edit-001",
        #                    input=generated_text,
        #                    instruction="Remove the prefix at the start and remove any duplicate or outstanding sentences",
        #                    temperature=0,
        #                    top_p=1
        #                    )
        formatted_text = generated_text#response['choices'][0]['text']

        print("Autocorrected text:\n")

        print(formatted_text)

        if formatted_text.startswith('"') and formatted_text.endswith('"'):
            formatted_text = formatted_text[1:]
            formatted_text = formatted_text[:-1]
        elif formatted_text.startswith("'") and formatted_text.endswith("'"):
            formatted_text = formatted_text[1:]
            formatted_text = formatted_text[:-1]

        print("Removed quotation marks:\n", formatted_text)

        print("Final message to be sent:\n----\n", formatted_text, "\n----\nRaw text:\n", repr(formatted_text), "\n----")

        asyncio.sleep(2)

        if len(formatted_text) > 1900:
            await message.channel.send("<@851132992289898508> The response i generated was too long for discord to handle! Try rephrasing the prompt.")
        else:
            await message.channel.send(formatted_text + "<@851132992289898508>")


bot.run("Other Chat bot")