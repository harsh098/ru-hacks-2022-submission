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
