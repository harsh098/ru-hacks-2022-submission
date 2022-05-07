from nextcord.ext import commands
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
        for sample in data:
            record = "----------------\n"
            for x,y in zip(sample.keys() , sample.values()):
                record += f"{x} : {y} \n"
            response +=  record
        await ctx.send(response)
    else:
        await ctx.send('Unavailable blood Type')

@bot.command()
async def organ(ctx, organ_name:str, donor_blood_group:str):
    data = await get_organ_data(organ_name , donor_blood_group)

    if data:
        response =  f"{len(data)} samples available \n"
        for sample in data:
            record = "----------------\n"
            for x,y in zip(sample.keys() , sample.values()):
                record += f"{x} : {y} \n"
            response +=  record
            
        await ctx.send(response)
    else:
        await ctx.send('Requested organ data is not Available')
    
bot.run(API_KEY)
