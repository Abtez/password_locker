#! /usr/bin/env python3
from user_class import User

def create_user(name, password):
    new_user = User(name, password)
    return new_user