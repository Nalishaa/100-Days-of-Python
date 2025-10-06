class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0    # we can also set default values

user_1 = User("001","nalisha")

print(user_1.username)

