import nextcord
from nextcord.ext import commands
import random
import os

class commands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.responses = ["Yes", "No", "Hohoho", "Ughh", "Nanana", "*Hangs Up*"]
    self.weights = [10,10,5,7,5,2]
    self.indexes = list(range(len(self.responses)))

    self.emotes = [954512669967253554, 
               954513681448841306, 
               954513940535201883, 
               954513272462278686, 
               954514529851670608, 
               954513050575204353]
  
  @commands.Cog.listener()
  async def on_message(self, message):

    if message.author == self.bot.user:
      return

    txt = message.content
      
    if len(message.mentions) > 0:
      for member in message.mentions:
        if member.id == 954450131535659089:

          if 'lean' in txt.lower() and random.randint(1,10) == 1:
            lean = self.bot.get_emoji(954528048777138226)
            await message.channel.send(f'{lean} LEANN TORNADOO!')
          
          else:
            index = random.choices(self.indexes,weights=self.weights)[0]
            await message.channel.send(f'{str(self.bot.get_emoji(self.emotes[index]))} {self.responses[index]}')


def setup(client):
  client.add_cog(commands(client))
  print(f"Module '{os.path.basename(__file__)}' initialised")