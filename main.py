
# Library and modules
import discord
from discord.ext import commands
import cloudscraper
import random
import aiosqlite

###################COLOR VARIABLES###################
lightblue = 0x5ca3ff
red = 0xff0000
orange = 0xffa500
yellow = 0xffff00
greensuccess = 0x81fe8f
rederror = 0xfe8181
white = 0xffffff
###################COLOR VARIABLES###################

bot = discord.Bot(command_prefix=".", intents = discord.Intents.all(), debug_guilds=[1017887450007355402])
scraper = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

imsg = " | This bot will soon be permanent"

invrid = discord.Embed(title="Error", description="This round id is invalid", color=0xff0000)

#bot start and ready event

@bot.event
async def on_ready():
    async with aiosqlite.connect("main.db") as db:
        print("Establishment of the connection to the database...")
        print("Verifying data")
        async with db.cursor() as cursor:
            await cursor.execute('CREATE TABLE IF NOT EXISTS warns (id INTEGER , date STRING , reason STRING , author INTEGER)')
        await db.commit()
        print("Connection success ready to use")

    print("  ____        _      ____        _ _            ")
    print(" |  _ \      | |    / __ \      | (_)           ")
    print(" | |_| | ___ | |_  | |  | |_ __ | |_ _ __   ___ ")
    print(" |  _ < / _ \| __| | |  | | '_ \| | | '_ \ / _ \ ")
    print(" | |_| | (_) | |_  | |__| | | | | | | | | |  __/")
    print(" |____/ \___/ \__|  \____/|_| |_|_|_|_| |_|\___|")
    print("                                                ")


#event

@bot.event
async def on_member_join(member):
    gid = member.guild.id
    if gid == 1017887450007355402:
        author = member.name
        tag = member.discriminator
        id = member.id
        channel = bot.get_channel(1019261389468086385)
        await channel.send(embed = discord.Embed(title="A new Member !!", description=f"""
        <@{id}> joined the server !
        You can use commands in <#1018594656256282634>
        Make sure to check <#1018579646729691226>
        
        You can use free commands like /mines /towers and /roulette !!! for FREE IMAGINE
        Hope you'll like your visit here :slight_smile:""", color=0xff99ff))
        default_role = discord.utils.get(member.guild.roles, id=1017933270085812275)
        await member.add_roles(default_role)
@bot.event
async def on_member_remove(member):
    gid = member.guild.id
    if gid == "1017887450007355402":
        author = member.name
        tag = member.discriminator
        id = member.id
        channel = bot.get_channel(1019261389468086385)
        await channel.send(embed = discord.Embed(title="A member left", description=f"""
        <@{id}> left the server, cyaa""", color=0xff99ff))



# Crash
@bot.command(description="Reserved for paid access")
async def crash(ctx):
    gid = ctx.guild.id
    if gid == 1017887450007355402:
        author = ctx.author.name
        tag = ctx.author.discriminator
        id = ctx.author.id
        log = f"Command mines as been used by {author}#{tag} || ID : {id}"
        print(log)
        role = discord.utils.get(ctx.guild.roles, name="customers")
        games = scraper.get("https://rest-bf.blox.land/games/crash").json()
        if role in ctx.author.roles:
            if ctx.author.id != bot.user.id:
                ok = await ctx.respond(
                embed=discord.Embed(title="checking api",
                description="Connecting to the api...",
                color=0x5ca3ff))

                def lol():
                    r = scraper.get(
                    "https://rest-bf.blox.land/games/crash").json()["history"]
                    yield [
                        r[0]["crashPoint"],
                        [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]
                    ]

                for game in lol():
                    games = game[1]
                    avg = sum(games) / len(games)
                    chance = 1
                    for game in games:
                        chance = chance = 95 / game
                        prediction = (1 / (1 - (chance)) + avg) / 2
                        if float(prediction) > 2:
                           color = 0x81fe8f
                        else:
                            color = 0xfe8181
                            description = f"""
                            **Crashpoint:**
                            *{prediction:.2f}x*
                            **Chance:**
                            {chance:.2f}%
                          """
                    await ctx.send(embed=discord.Embed(description =f"""
                           **Crashpoint:**
                            *{prediction:.2f}x*
                            **Chance:**
                            {chance:.2f}%
                          """, color=color))
                    break
            else:
                error_code = discord.Embed(title="Error",
                description="You need to had bought the the full access to be able to use this command",
                color=0xfe8181)
                await ctx.respond(embed=error_code)
        else:
            error_code = discord.Embed(title="Error",
            description="You need to had bought the the full access to be able to use this command",
            color=0xfe8181)
            await ctx.respond(embed=error_code)
    else:
        await ctx.respond(embed=discord.Embed(title="Error", description="This command is reserved for customers and CANT be used in your server. Make sure to join our server https://discord.gg/ndmQqEbuZg to be able to use this command", color=0xff0000))
@bot.command(description="Reserved for paid access")
async def c(ctx):
    gid = ctx.guild.id
    if gid == 1017887450007355402:
        author = ctx.author.name
        tag = ctx.author.discriminator
        id = ctx.author.id
        log = f"Command mines as been used by {author}#{tag} || ID : {id}"
        print(log)
        role = discord.utils.get(ctx.guild.roles, name="customers")
        games = scraper.get("https://rest-bf.blox.land/games/crash").json()
        if role in ctx.author.roles:
            if ctx.author.id != bot.user.id:
                ok = await ctx.respond(
                embed=discord.Embed(title="checking api",
                description="Connecting to the api...",
                color=0x5ca3ff))

                def lol():
                    r = scraper.get(
                    "https://rest-bf.blox.land/games/crash").json()["history"]
                    yield [
                        r[0]["crashPoint"],
                        [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]
                    ]

                for game in lol():
                    games = game[1]
                    avg = sum(games) / len(games)
                    chance = 1
                    for game in games:
                        chance = chance = 95 / game
                        prediction = (1 / (1 - (chance)) + avg) / 2
                        if float(prediction) > 2:
                           color = 0x81fe8f
                        else:
                            color = 0xfe8181
                            description = f"""
                            **Crashpoint:**
                            *{prediction:.2f}x*
                            **Chance:**
                            {chance:.2f}%
                          """
                    await ctx.send(embed=discord.Embed(description =f"""
                           **Crashpoint:**
                            *{prediction:.2f}x*
                            **Chance:**
                            {chance:.2f}%
                          """, color=color))
                    break
            else:
                error_code = discord.Embed(title="Error",
                description="You need to had bought the the full access to be able to use this command",
                color=0xfe8181)
                await ctx.respond(embed=error_code)
        else:
            error_code = discord.Embed(title="Error",
            description="You need to had bought the the full access to be able to use this command",
            color=0xfe8181)
            await ctx.respond(embed=error_code)
    else:
        await ctx.respond(embed=discord.Embed(title="Error", description="This command is reserved for customers and CANT be used in your server. Make sure to join our server https://discord.gg/ndmQqEbuZg to be able to use this command", color=0xff0000))

# Mines:red_square:
@bot.command(description="Mines")
async def mines(ctx, mines_amount, round_id):
    author = ctx.author.name
    tag = ctx.author.discriminator
    id = ctx.author.id
    log = f"Command mines as been used by {author}#{tag} || ID : {id}"
    print(log)
    round_id = str(round_id)
    round_length = len(round_id)
    mines_amount = int(mines_amount)
    if round_length == 36:
        if mines_amount <= 5:
            mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:'
            a = random.randint(1, 8)
            b = random.randint(9, 13)
            c = random.randint(14, 17)
            d = random.randint(18, 25)
            if a == 1:
                mine1 = ":green_square:"
            elif a == 2:
                mine2 = ":green_square:"
            elif a == 3:
                mine3 = ":green_square:"
            elif a == 4:
                mine4 = ":green_square:"
            elif a == 5:
                mine5 = ":green_square:"
            elif a == 6:
                mine6 = ":green_square:"
            elif a == 7:
                mine7 = ":green_square:"
            elif a == 8:
                mine8 = ":green_square:"
            if b == 9:
                mine9 = ":green_square:"
            elif b == 10:
                mine10 = ":green_square:"
            elif b == 11:
               mine11 = ":green_square:"
            elif b == 12:
                mine12 = ":green_square:"
            elif b == 13:
                mine13 = ":green_square:"
            if c == 14:
                mine14 = ":green_square:"
            elif c == 15:
                mine15 = ":green_square:"
            elif c == 16:
                mine16 = ":green_square:"
            elif c == 17:
                mine17 = ":green_square:"
            if d == 18:
                mine18 = ":green_square:"
            elif d == 19:
                mine19 = ":green_square:"
            elif d == 20:
                mine20 = ":green_square:"
            elif d == 21:
                mine21 = ":green_square:"
            elif d == 22:
                mine22 = ":green_square:"
            elif d == 23:
                mine23 = ":green_square:"
            elif d == 24:
                mine24 = ":green_square:"
            elif d == 25:
                mine25 = ":green_square:"
            row1 = mine1 + mine2 + mine3 + mine4 + mine5
            row2 = mine6 + mine7 + mine8 + mine9 + mine10
            row3 = mine11 + mine12 + mine13 + mine14 + mine15
            row4 = mine16 + mine17 + mine18 + mine19 + mine20
            row5 = mine21 + mine22 + mine23 + mine24 + mine25
            info = str(random.randint(45, 90))
            em = discord.Embed(color=0x11F1D3)
            em.set_footer(text="Hope you won bud")
            em.add_field(name="Mines predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy**" + "\n" + info +"%")
            await ctx.respond(embed=em)
        else:
            await ctx.respond(embed=discord.Embed(title="Woops out brainning error", description="Im very sorry but my brain is limited at 5 mines max :/ you should start a game of 3 mines for more accuracy", color=0xff8595))
    else:
        await ctx.respond(embed=discord.Embed(title="Error", description="This round id is invalid", color=0xff8595))

#towers

@bot.command(description="Predict what is safe in tower")
async def towers(ctx, level, round_id):
    author = ctx.author.name
    tag = ctx.author.discriminator
    id = ctx.author.id
    log = f"Command towers as been used by {author}#{tag} || ID : {id}"
    print(log)
    rid = str(round_id)
    rlen = len(rid)
    lvl = str(level)
    if lvl == "easy":
        if rlen == 36:
            tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = ":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:"
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            c = random.randint(1, 3)
            d = random.randint(1, 3)
            e = random.randint(1, 3)
            f = random.randint(1, 3)
            g = random.randint(1, 3)
            h = random.randint(1, 3)
    
            if a == 1:
                tower1 = ":star:"
            elif a == 2:
                tower2 = ":star:"
            elif a ==3:
                tower3 = ":star:"
            if b == 1:
                tower4 = ":star:"
            elif b == 2:
                tower5 = ":star:"
            elif b ==3:  
                tower6 = ":star:"
            if c == 1:
                tower7 = ":star:"
            elif c == 2:
                tower8 = ":star:"
            elif c ==3:
                tower9 = ":star:"
            if d == 1:
                tower10 = ":star:"
            elif d == 2:
                tower11 = ":star:"
            elif d ==3:
                tower12 = ":star:"
            if e == 1:
                tower13 = ":star:"
            elif e == 2:
                tower14 = ":star:"
            elif e ==3:
                tower15 = ":star:"
            if f == 1:
                tower16 = ":star:"
            elif f == 2:
                tower17 = ":star:"
            elif f ==3:
                tower18 = ":star:"
            if g == 1:
                tower19 = ":star:"
            elif g == 2:
                tower20 = ":star:"
            elif g ==3:
                tower21 = ":star:"
            if h == 1:
                tower22 = ":star:"
            elif h == 2:
                tower23 = ":star:"
            elif h ==3:
                tower24 = ":star:"

            row1 = tower1 + tower2 + tower3
            row2 = tower4 + tower5 + tower6
            row3 = tower7 + tower8 + tower9
            row4 = tower10 + tower11 + tower12
            row5 = tower13 + tower14 + tower15
            row6 = tower16 + tower17 + tower18
            row7 = tower19 + tower20 + tower21
            row8 = tower22 + tower23 + tower24
            #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
            info = str(random.randint(45, 95))
            list = [0xFF0000, 0x00FF2E, 0x000FFF, 0xF700FF]
            color = random.choice(list)
            em = discord.Embed(color=color)
            em.set_footer(text="Hope you won bud")
            em.add_field(name="Towers Predictor", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "**Accuracy**" + "\n" + info + "%")   
            await ctx.respond(embed=em)
        else:
            ctx.respond(embed=invrid)
    elif lvl == "normal":
        if rlen == 36:
            tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16 = ":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:",":x:"
            a = random.randint(1, 2)
            b = random.randint(1, 2)
            c = random.randint(1, 2)
            d = random.randint(1, 2)
            e = random.randint(1, 2)
            f = random.randint(1, 2)
            g = random.randint(1, 2)
            h = random.randint(1, 2)
            if a == 1:
                tower1 = ":star:"
            elif a ==2:
                tower2 = ":star:"
            if b == 1:
                tower3 = ":star:"
            elif b ==2:
                tower4 = ":star:"
            if c == 1:
                tower5 = ":star:"
            elif c ==2:
                tower6 = ":star:"
            if d == 1:
                tower7 = ":star:"
            elif d ==2:
                tower8 = ":star:"
            if e == 1:
                tower9 = ":star:"
            elif e ==2:
                tower10 = ":star:"
            if f == 1:
                tower11 = ":star:"
            elif f ==2:
                tower12 = ":star:"
            if g == 1:
                tower13 = ":star:"
            elif g ==2:
                tower14 = ":star:"
            if h == 1:
                tower15 = ":star:"
            elif h ==2:
                tower16 = ":star:"
            row1 = tower1 + tower2
            row2 = tower3 + tower4
            row3 = tower5 + tower6
            row4 = tower7 + tower8
            row5 = tower9 + tower10
            row6 = tower11 + tower12
            row7 = tower13 + tower14
            row8 = tower15 + tower16
            info = str(random.randint(30, 75))
            list = [0xFF0000, 0x00FF2E, 0x000FFF, 0xF700FF]
            color = random.choice(list)
            em = discord.Embed(color=color)
            em.set_footer(text="Hope you won bud")
            em.add_field(name="Towers Predictor", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "**Accuracy**" + "\n" + info + "%")   
            await ctx.respond(embed=em)
        else:
            ctx.respond(embed=invrid)
    else:
        err = discord.Embed(title="Error", description="This level isnt available, only \"easy\" and \"normal\" are working levels", color=0xff0000)
        await ctx.respond(embed=err)
    

#roulette
@bot.command(description="Predict what color will win in the roulette")
async def roulette(ctx, round_id):
    author = ctx.author.name
    tag = ctx.author.discriminator
    id = ctx.author.id
    log = f"Command roulette as been used by {author}#{tag} || ID : {id}"
    print(log)
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        predictions = ['red','red','red','purple','purple','purple','gold']
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0xFF0036
            color_text = '**Result :**'
            prediction = ":red_square:"
        elif prediction == 'purple':
            embed_color = 0xAE00FF
            color_text = '**Result :**'
            prediction = ":purple_square:"
        elif prediction == 'purple':
            embed_color = 0xFFFB00
            color_text = '**Result :**'
            prediction = ":yellow_square:"
        em = discord.Embed(color=embed_color)
        em.add_field(name="Roulette Predictor", value=color_text + "\n" + prediction)
        await ctx.respond(embed=em)
    else:
        await ctx.respond(embed=invrid) #invalid round id

#cups
@bot.command(description="Predict what color will win in a battle of 2 cups")
async def cups(ctx, round_id):
    author = ctx.author.name
    tag = ctx.author.discriminator
    id = ctx.author.id
    log = f"Command cups as been used by {author}#{tag} || ID : {id}"
    print(log)
    role = discord.utils.get(ctx.guild.roles, name="customers")
    if role in ctx.author.roles:
        round_id = str(round_id)
        rlen = len(round_id)
        if rlen == 36:
            pred = ['red', 'blue']
            rpred = random.choice(pred)
            if rpred == 'red':
                em= discord.Embed(title="Predictions For Cups",
                description="**Result :** :red_square:",
                color=0xFF0000)
                await ctx.respond(embed=em)
            else:
                em= discord.Embed(title="Predictions For Cups",
                description="**Result :** :blue_square:",
                color=0x5874ff)
                await ctx.respond(embed=em)
        else:
            em = discord.Embed(title="Error",
            description="""This round id is invalid""",
            color=0xff0000)
            await ctx.respond(embed=invrid)
    else:
        error_code = discord.Embed(title="Error",
        description="You need to had bought the the full access to be able to use this command",
        color=0xfe8181)
        await ctx.respond(embed=error_code)


@bot.command(description="Send Rules Mesage")
async def rules(ctx):
    ar = ctx.author.roles
    role = discord.utils.get(ctx.guild.roles, name="*")
    if role in ar:
        em1 = discord.Embed(color=white)
        em1.title="General Informations"
        em1.description ="Our server is a community, that said, respect is required and for all, moderators towards members and members towards moderators. The moderators reserve the right to act accordingly in the event of non-compliance with the rules.These rules may be subject to change. For any change, you will be notified."
        await ctx.send(embed=em1)
        em = discord.Embed(color=orange)
        em.title = "Discord Rules"
        em.description = "These rules are meant to be seen as a very brief and surface-level guidelines in how our moderation decisions take place. We may deem any person of not being able to access this server at any time, or set restriction in which you cannot utilize it for a certain time."
        em.add_field(name="1. Harassment and/or Threats", value="Direct harassment to an user is tiring to deal with - and we don't accept it in our public channels. Keep it out of our server otherwise face consequences of only using this server to view it, and not speak in it.", inline=False)
        em.add_field(name="2. Sexual / Violent Content", value="No content that can be seen as sexual or NSFW will be removed instantly for the safety of our server. Users involved indirectly and directly will face punishment. Content that can be seen as potentially disgusting in nature or terrorizing will be removed instantly for the safety of our server. Users involved indirectly and directly will face punishment.", inline=True)
        em.add_field(name="3. Illegal Activities", value="Due to the safety concerns of our server and to maintain a healthy relation with Discord standards, we prohibit the act of discussing and glorifying illegal activities. [ i.e. Speaking of real-currency gambling ]", inline=True)
        em.add_field(name="4. Discussing Peripheral Topics", value="We prohibit the act of discussing, glorifying and/or talking highly of any topic that may carry pettiness and may inflict drama in chatrooms.", inline=True)
        em.add_field(name="5. Spamming and flooding", value="Spamming or sending repeated messages for the purpose of invading a channel is strictly prohibited. Spam is considered as the sending of several messages being the same one after the other with the aim of invading a channel of this message. Flooding is also forbidden. Flood is identified as sending a message with a lot of same character following the previous one ex : ffffffffffffff", inline=True)
        em.add_field(name="6. Respect", value="Respect from members towards moderators and from moderators towards members is VERY important. The same goes for moderators towards you. They respect you, respect them", inline=True)
        em.add_field(name="7. Self Advertising", value="Highlighting your server, your website, or anything else that is in the advertising category is prohibited. Failure to respect this rule will result in a warn, followed by a mute if repeated", inline=True)
        em.add_field(name="8. Begging", value="Do not ask for robux or tips. do not ask people to buy your gamepass. Also, be cool and just dont talk about tip.", inline=True)
        em.add_field(name="9. Ping", value="First of all, the ping is recognized as mentioning someone example <@683765180462792794>. It is forbidden to ping willyrire, koyp in tickets or in normal channel. Keep in mind, do **NOT** ping or you will get banned.", inline=True)
        em.add_field(name="10. For the well-being of my compute", value="For the well-being of my compute, do not spam commands. Spamming commands will result in a instant ban", inline=True)
        em.add_field(name="Official Discord Guidelines", value="Our server recommends each and every user utilizing our chatrooms to follow Discord's guidelines, while this rule list may include/exclude some of its rules, the entirety of our rules apparatus surrounds itself of Discord's guidelines. View them [here](https://discord.com/guidelines)", inline=False)
        em.set_footer(text="We consider you read those rules and accepted them")
        await ctx.send(embed=em)
        await ctx.respond("wip", delete_after=1)
#bot token
bot.run("TOKEN HERE")
