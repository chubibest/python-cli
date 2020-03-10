from subprocess import run, PIPE, Popen
import subprocess
import sys
from crypt import crypt, mksalt, METHOD_SHA512

def create(name, groups, password):
    print(password)
    password = crypt(password, mksalt(METHOD_SHA512))
    print(password)
    user = subprocess.run([ 'useradd', '-p', password, '-G', _str(groups),  name], stdout=PIPE, stderr=PIPE)
    status = int(user.returncode)
    if status == 6:
        print('Group does not exist')
    elif status == 9:
        print('Username already in use')
    elif status == 0:
        print('User created')
    else:
        print('Something went wrong')
        print(status)
def update(name, groups, password):
    pass
def remove(name):
    user = subprocess.run(['userdel', '-r', name], stdout=PIPE, stderr=PIPE)
    print(type(user.returncode))
    status =int(user.returncode)
    print(status)
    if status == 0:
        print('User removed')
    elif status == 6:
        print('User doesn\'t exist')
    else:
        print('Something went wrong')
def _str(groups):
        return ','.join(groups or [])

