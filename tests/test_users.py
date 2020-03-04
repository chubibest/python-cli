import pytest
from hr import users
from crypt import crypt, mksalt, METHOD_SHA512
import subprocess

password = crypt('password', mksalt(METHOD_SHA512))

user = {
        "name": "bruce",
        "groups": ['wheeel'],
        "password": 'password'
        }
def test_create(mocker):
    """
    given a user dictionary user.create
    shouldadd a new user
    """
    mocker.patch('subprocess.run')
    users.create(**user)
    subprocess.run.assert_called()

def test_remove(mocker):
    """
    given a user dictionary user.remove
    should remove a user
    """
    mocker.patch('subprocess.run')
    users.remove('bruce')
    subprocess.run.assert_called()
