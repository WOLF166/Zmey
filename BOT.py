import discord
from discord.ext import commands
import json
import requests

TOKEN = "OTU2MTk4MTA0Njg2NzkyNzI2.Yjsu4Q.mO1AmMo_xldF9H34OpokEm9-5_E"


# client = discord.Client()


class Zmey(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    @commands.command(name='ping')
    async def ping(self, ctx):
        author = ctx.message.author
        await ctx.send(f"pong, {author.mention}")
        # if message.author == self.user:
        #     return
        # else:
        #     if "ping" in message.content.lower():
        #         pol = message.author

    @commands.command(name='send-pic')
    async def sendpic(self, ctx, message):
        try:
            if "$send-pic" in ctx.message.content.lower():
                namepic = str(ctx.message.content.lower())
                namepic = namepic.split(' ')
                namepic = namepic[-1]
                print(namepic)

                response = (f'https://some-random-api.ml/' + namepic)  # Get-запрос
                print(response)
                response = requests.get(response)  # Get-запрос
                print(response)
                json_data = json.loads(response.text)  # Извлекаем JSON

                embed = discord.Embed(color=0xff9900, title=namepic)  # Создание Embed'a
                embed.set_image(url=json_data['image'])  # Устанавливаем картинку Embed'a
                await ctx.send(embed=embed)  # Отправляем Embed


        except:
            author = ctx.message.author
            await ctx.send(f"{author.mention}, Error:404")


bot = commands.Bot(command_prefix='$')
bot.add_cog(Zmey(bot))
bot.run(TOKEN)
