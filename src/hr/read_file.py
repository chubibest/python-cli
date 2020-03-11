from json import load, dumps
from hr.users import create

def read_inventory(file):
    with open(file) as users_json:
        parsed_users = load(users_json)
        for user in parsed_users:
            create(**user)
def write_inventory(file):
    pass

