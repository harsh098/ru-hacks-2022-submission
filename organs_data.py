from dbdriver import getMultiSetRecords
from json import loads
import asyncio

'''
Org_Name VARCHAR(255),
Organ_type VARCHAR(50),
donor_blood_group VARCHAR(4),
geotag_of_org VARCHAR(255),
specs VARCHAR(255)

'''


async def get_organ_data(organ_name, donor_blood_group):
    data = await getMultiSetRecords('organ_data', {'Organ_type': organ_name, 'donor_blood_group': donor_blood_group})
    return_object = []
    if data:
        # if not empty_set
        for sample in data:
            return_object.append(
                {
                    "ORG Name": sample[0],
                    "Organ Name":  sample[1],
                    "Blood Group of Owner":  sample[2],
                    "Location": sample[3],
                    "Specifications of Organs and Donor": extract_specs(sample[4])
                }
            )
        return return_object
    else:
        return ()


def extract_specs(json_string):
    specs = loads(json_string)
    return_string = "\n"
    for x, y in zip(specs.keys(),  specs.values()):
        return_string += f"\t{x} : {y} \n"
    return return_string

# async def test():
#     data = await get_organ_data('skin' , 'A')
#     if data:
#         for sample in data:
#             print(sample)
#     else:
#         print("No compatible samples")

# if __name__ == '__main__':
#     asyncio.run(test())
