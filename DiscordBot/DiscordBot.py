# ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━━╮╱╱╱╭╮
# ╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭╮┃╱╱╭╯╰╮
# ╱┃┃┃┣┳━━┳━━┳━━┳━┳━╯┃┃╰╯╰┳━┻╮╭╯
# ╱┃┃┃┣┫━━┫╭━┫╭╮┃╭┫╭╮┃┃╭━╮┃╭╮┃┃
# ╭╯╰╯┃┣━━┃╰━┫╰╯┃┃┃╰╯┃┃╰━╯┃╰╯┃╰╮
# ╰━━━┻┻━━┻━━┻━━┻╯╰━━╯╰━━━┻━━┻━╯

#Usage

#In order to create a discord bot, 
#You first need to go to this link,
#https://discord.com/developers/applications

#Create an application, and give it a name.

#Once you are done, click on bot in settings.
#Click add bot and finally put in the information.

#Then click on OAuth2.
#Inside the table, click on bot.

#When a new table pops up, click on the permissions.
#Make sure your bot has the right to send messages.
#If you don't want to check off all permissions,
#Just click on administator.

#Click on the link below the first table,
#Copy it into your website address.
#It should bring you to an invite bot page.
#Invite the bot to your server and done.

#The bot should be offline, and that is where we will code it.

#Now we are ready to program out bot.
#First, you need the discord module

import discord
from discord.ext import commands
import nest_asyncio

ApplyingNest_Asyncio = nest_asyncio.apply()

#You can change the prefix in order to activate the bot.
client = commands.Bot(command_prefix='!')

#If you want a command, first write this line of code. 
@client.command()

#The function name is the function that is used in discord.
#Ctx has to go inside the function because that is the channel.
#In this case, the function is Say_Hello!
#The ctx.send(), which will send the message, needs an await.
#Inside the ctx.send, we can have our message.
async def Say_Hello(ctx):
    await ctx.send("Hello There!")
    
#If you want an event, like when a player joins, 
#You would do something similar.

#In this case, we are doing the command when the bot becomes ready.
@client.event

#In this case, the name of the function is important. 
async def on_ready():
    print("Hello")
    
#If you want to have the user input something you can do something like this.
@client.command()
async def Add_10(ctx, Number):
    #I will have error handling in case the user inputs a string.
    #Since all discord values are strings, I will need to try to convert it.
    
    try:
        UserNumber = int(Number)
        await ctx.send(UserNumber + 10)
    except:
        await ctx.send("Input is not a number!")
    
#This is a more complex command, however still is very basic in code.
@client.command()
async def Reply(ctx, Message):
    if Message == "Hello":
        await ctx.send("Hello")
    elif Message == "Bye":
        await ctx.send("Bye!")

#Notice! Below your bot, there is a token.
#Copy your token and paste it inside.
#This is IMPORTANT because your bot will not run!

client.run('YourToken')

#When you run your code, you should notice that your discord bot goes online.
#This means that is works!

#Of course, if you want to learn more, go to the official documentation.
#https://discordpy.readthedocs.io/en/stable/

#Otherwise, I hope you enjoyed!

#Coded by Nicholas Smirnov
