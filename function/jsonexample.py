import json
# JSON string version of your data
json_data = '''
[
    {
        "id": 1,
        "first_name": "Betta",
        "last_name": "Dandie",
        "email": "bdandie0@tmall.com",
        "gender": "Female",
        "ip_address": "55.34.7.138"
    },
    {
        "id": 2,
        "first_name": "Nikolai",
        "last_name": "Beadel",
        "email": "nbeadel1@scribd.com",
        "gender": "Male",
        "ip_address": "184.32.217.157"
    }
]
'''

# Parse the JSON string
y = json.loads(json_data)

# Access first name of first user
#print(y[0]["first_name"])  # Output: Betta
print(y)