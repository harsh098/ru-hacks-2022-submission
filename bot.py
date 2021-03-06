from nextcord.ext import commands
from nextcord import Embed, Colour, Activity, ActivityType
from os import environ
from blood_bank_data import get_blood_banks
from organs_data import get_organ_data

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    await bot.change_presence(activity=Activity(type=ActivityType.watching , name = 'people in distress'))
@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')

bot.remove_command('help')
@bot.command()
async def help(ctx , focus_command:str = ''):
    blood_name = ".blood <blood_group> :"
    blood_desc = "Gives information about available blood banks for the given blood group"
    organ_name = ".organ <organ_name> <donor_blood_group> :"
    organ_desc = " Gives information about available organ donation centres,  for the input donor_blood_group and organ_name.\n If organ name contains spaces add an '\\_' (underscore)"
    ping_name = ".ping"
    ping_desc = "Checks if the bot is online"
    embed=Embed(title= "Help",description= 'Commands for the bot.',color= 0x00FFFF,)
    if focus_command == '' :
        embed.add_field(name=blood_name , value=blood_desc, inline=False)
        embed.add_field(name=organ_name , value=organ_desc, inline=False)
        embed.add_field(name = ping_name, value=ping_desc, inline=False)
    elif focus_command == 'blood':
        embed.add_field(name=blood_name , value=blood_desc, inline=False)
    elif focus_command == 'organ' :
        embed.add_field(name=organ_name , value=organ_desc, inline=False)
    elif focus_command == 'ping' :
        embed.add_field(name = ping_name, value=ping_desc, inline=False)
    else:
        embed.add_field(name=focus_command , value="Requested command does not exist", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def blood(ctx, blood_type: str):
    data = await get_blood_banks(blood_type)

    if data:
        
        response =  f"{len(data)} samples available \n"
        await ctx.send(response)
        for sample in data:
            embed= Embed(title = sample['ORG Name'],
                description= 'Click the Card to Open Google Maps location',
                colour= Colour.blue(),
                url=sample['Location']           
                )
            for field_name,field_value in zip(sample.keys(),sample.values()):
                if field_name not in ["Location", "ORG Name"] :
                    embed.add_field(name=field_name , value=field_value, inline=False)
            await ctx.send(embed=embed)
        
    else:
        await ctx.send('Unavailable blood Type')

@bot.command()
async def organ(ctx, organ_name:str, donor_blood_group:str):
    organ_name = organ_name.replace("_"," ")
    data = await get_organ_data(organ_name , donor_blood_group)

    if data:
        response =  f"{len(data)} samples available \n"
        await ctx.send(response)
        for sample in data:
            embed= Embed(title = sample['ORG Name'],
                description= 'Click the Card to Open Google Maps location',
                colour= Colour.blue(),
                url=sample['Location']           
                )
            for field_name,field_value in zip(sample.keys(),sample.values()):
                if field_name not in ["Location", "ORG Name"] :
                    embed.add_field(name=field_name , value=field_value, inline=False)
                    
            await ctx.send(embed=embed)
            
            
    else:
        await ctx.send('Requested organ data is not Available')
    
bot.run(environ["DISCORD_API_KEY"])
