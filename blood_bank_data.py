import dbdriver
import asyncio
async def get_blood_banks(blood_type):
    data  = await dbdriver.getRecords('blood_samples', 'blood_type_available' , f'%{blood_type}%', modifier='LIKE' )
    return_object = []
    if data:
        #if not empty_set
        for sample in data:
            return_object.append(
                {
                    "ORG Name" : sample[0],
                    "Blood Group Available" : sample[1],
                    "Location" : sample[2] 
                }
            )
        return return_object
    else:
        return ()



# async def test():
#     data = await get_blood_banks('A+')
#     if data:
#         for sample in data:
#             print(sample)
#     else:
#         print("No compatible samples")


    
# if __name__ == '__main__':
#     asyncio.run(test())



