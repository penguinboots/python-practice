def save_user(**user):
    print(user)


# dictionary - pass keyword arguments
save_user(id=1, name="admin")  # -> prints {'id': 1, 'name': 'admin'}


def save_user_again(**user):
    print(user["name"])


save_user_again(id=1, name="admin")  # -> prints "admin"
