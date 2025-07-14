class User :
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def print_information(self):
        print(f"{self.username}'s user id : {self.user_id}")
        print(f"{self.username}'s user name : {self.username}")
        print(f"{self.username}'s followers : {self.followers}")
        print(f"{self.username}'s following : {self.following}\n")


user_1 = User("001", "abc")
user_2 = User("002", "xyz")

user_1.print_information()
user_2.print_information()

# user_1 follow user_2
user_1.follow(user_2)

user_1.print_information()
user_2.print_information()

