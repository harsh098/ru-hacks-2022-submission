import aiosqlite
import asyncio

DB_NAME = "db.sqlite3"
async def getRecords(table_name,column_name,value,select_columns= "*",modifier = "="):
    
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.cursor() as cursor:
            await cursor.execute(f'SELECT {select_columns} FROM {table_name} WHERE {column_name}  {modifier} "{value}" ')
            data = await cursor.fetchall()
            if data:
                return data
            else:
                return ()

                

async def getMultiSetRecords(table_name,column_value_pairs : dict,  select_columns = "*" ):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.cursor() as cursor:
            conditions = ""
            idx = 0
            for x,y in zip(column_value_pairs.keys(),column_value_pairs.values()):
                if idx != (len(column_value_pairs) -1):
                    conditions += f'({x} = "{y}") AND'
                else:
                    conditions += f'({x} = "{y}")'
                idx+=1
            query = f'SELECT {select_columns} FROM {table_name} WHERE {conditions} '
            await cursor.execute(query)
            data = await cursor.fetchall()
            if data:
                return data
            else:
                return ()

# async def test():
#     #Replace the code within this function with your own testing code
#     data = await getMultiSetRecords('blood_samples',{'blood_type_available' : 'A+' , 'blood_bank_name' :'XYZ Blood Bank'})
    
#     for i in data:
#         print(i)
    
# if __name__ == '__main__':
#     asyncio.run(test())