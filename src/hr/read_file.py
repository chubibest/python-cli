from json import load, dumps
from users import create

def read_inventory(file):
    with open(file) as users_json:
        parsed_users = load(users_json)
        print(parsed_users)
        for user in parsed_users:
            print(type(user))
            create(**user)
def write_inventory(file):
    pass

