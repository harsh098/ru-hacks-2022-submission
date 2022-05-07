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

                



# async def test():
#     #Replace the code within this function with your own testing code
#     data = await getRecords('blood_samples','blood_type_available','%A%' ,  modifier="LIKE")
    
#     for i in data:
#         print(i)
    
# if __name__ == '__main__':
#     asyncio.run(test())