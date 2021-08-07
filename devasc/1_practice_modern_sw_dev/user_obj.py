import yaml

pwd = '/Users/james/PycharmProjects/cisco_devnet/1_practice_modern_sw_dev/'

with open(pwd + 'user.yaml', 'r') as file:
    data = yaml.safe_load(file)

user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)

user['location']['city'] = 'Dallas'

# the next section serializes the data back into YAML format
with open(pwd + './user_edited.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
