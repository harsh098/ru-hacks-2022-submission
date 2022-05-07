from nextcord.ext import commands
from nextcord import Embed, Colour
from apikey import API_KEY
from blood_bank_data import get_blood_banks
from organs_data import get_organ_data

bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')


@bot.command()
async def help(ctx):
    blood_name = ".blood [blood_group]:"
    blood_desc = "Gives information about available blood banks for the given blood group"
    organ_name = ".organ [organ_name] [donor_blood_group]:"
    organ_desc = " Gives information about available organ donation centres,  for the input donor_blood_group and organ_name"

    embed=Embed(title= ".Help",description= 'Commands for the bot.',color= 0x00FFFF,)
    embed.add_field(name=blood_name , value=blood_desc, inline=False)
    embed.add_field(name=organ_name , value=organ_desc, inline=False)


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
    
bot.run(API_KEY)
