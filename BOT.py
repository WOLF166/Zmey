import discord
from discord.ext import commands
import json
import requests
import random
import sqlite3
import asyncio

TOKEN = ""
vseya_owner = "WOLF#9649"


# client = discord.Client()


class Zmey(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.con = sqlite3.connect('Users.db')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    # функция $ping
    @commands.command(name='ping')
    async def ping(self, ctx):
        author = ctx.message.author
        await ctx.send(f"pong, {author.mention}")

    # функция $send-pic
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

        # если не нашло изображение
        except:
            author = ctx.message.author
            await ctx.send(f"{author.mention}, Error:404")

    # фунция $roll
    @commands.command(name='roll')
    async def roll(self, ctx):
        try:
            if "$roll" in ctx.message.content.lower():

                if "данет" in ctx.message.content.lower():
                    await ctx.send(random.choice(["ДА", "НЕТ"]))

                else:
                    vseinmess = str(ctx.message.content.lower())
                    vseinmess = vseinmess.split(' ')
                    spis = []
                    spis.append(vseinmess[-1])
                    vseinmess.remove(str(vseinmess[-1]))
                    spis.append(vseinmess[-1])
                    print(spis)
                    await ctx.send(random.randint(int(spis[-1]), int(spis[0])))

        # если чтото не сработало
        except:
            author = ctx.message.author
            await ctx.send(
                f"{author.mention}, произошла ошибка(использование команды $roll число число, или $roll данет)")

    # функия $send_amd-mes
    @commands.command(name='send_adm-mes')
    async def send_adm_mes(self, ctx):
        person = str(ctx.message.author)

        if person == 'WOLF#9649':
            await ctx.send(ctx.message.content[13:])

        else:

            author = ctx.message.author
            await ctx.send(f'{author.mention} ты не Админ обратись к WOLF#9649')

    # фунция Жалоб
    @commands.command(name='ЖАЛОБА')
    async def complaint(self, ctx):
        comp_ch = bot.get_channel(963846872915664916)

        if 'жалоба' in ctx.message.content.lower():
            text_compl = ctx.message.content.lower()
            text_compl = str(text_compl).split(" ")
            text_compl.remove(text_compl[0])
            to_send = " ".join(text_compl)
            author = ctx.message.author
            await comp_ch.send(f'{author.mention} отправил жалобу: {to_send}')

    # фунция Заявка
    @commands.command(name="ЗАЯВКА")
    async def zayavka(self, ctx):
        comp_ch = bot.get_channel(963846872915664916)

        if 'заявка' in ctx.message.content.lower():
            text_compl1 = ctx.message.content.lower()
            text_compl1 = str(text_compl1).split(" ")
            text_compl1.remove(text_compl1[0])
            to_send = " ".join(text_compl1)
            author = ctx.message.author
            await comp_ch.send(f'{author.mention} отправил заявку: {to_send}')

    #функция $bd_add
    @commands.command(name="bd_add")
    async def db_add(self, ctx):

        try:
            author = str(ctx.message.author)
            mes = ctx.message.content
            mes = str(mes).split(" ")
            mes.remove(mes[0])
            print(mes)
            print(author)
            cur = self.con.cursor()
            cur.execute('insert into allusers (name_user, isadmin, whoadd) values (?, ?, ?)',
                        (mes[0], mes[1], author))
            self.con.commit()
            await ctx.send("OK")

        # если чтото всётаки сломалось
        except:
            await ctx.send("Дядь, чёт не так")

    # фунция $showbdusers
    @commands.command(name="showbdusers")
    async def showbdusers(self, ctx):
        cur = self.con.cursor()
        result = cur.execute('select * from allusers').fetchall()
        for i in result:
            i = list(i)
            embed = discord.Embed(color=0xff9900, title=(f"Имя: {i[0]}, АDMIN: {i[1]}, id: {i[2]}, Добавил: {i[3]}"))
            await ctx.send(embed=embed)

    # фунция $delbduser
    @commands.command(name='delbduser')
    async def delbduser(self, ctx):
        try:
            chis = str(ctx.message.content).split(" ")
            chis = int(str(chis[1]))
            print(chis)
            cur = self.con.cursor()
            cur.execute(f'delete from allusers where id == ({chis})')
            self.con.commit()
            await ctx.send("ok")
        except:
            await ctx.send("дядь такого id нет")

    # фунция $set_timer
    @commands.command(name='set_timer')
    async def set_timer(self, ctx):
        msg = str(ctx.message.content)
        if '$set_timer' in msg:
            vrem = msg.split(' ')
            minut = int(vrem[3])
            hour = int(vrem[1])
            mesg = str(msg)[28:]
            await ctx.send("ok")
            alltime = int(minut) * 60 + (int(hour) * 60) * 60
            # Бот уходит спать ниже
            await asyncio.sleep(alltime)
            # Бот скидывает напоминалку
            await ctx.send(mesg)


bot = commands.Bot(command_prefix='$')


# при включении бота
@bot.event
async def on_ready():
    adm_aud = bot.get_channel(706420232507490304)
    embed = discord.Embed(color=0xff9900, title=("Бот Включён"))
    await adm_aud.send(embed=embed)
    print("бот онлайн")


# @bot.event
# async def on_message(message):
#     con = sqlite3.connect('Users.db')
#     cur = con.cursor()
#     cur.execute('insert into allusers (name_user, isadmin, whoadd) values (?, ?, ?)',
#                 (message.content.lower(), 0, "ы"))
#     con.commit()


bot.add_cog(Zmey(bot))
bot.run(TOKEN)
