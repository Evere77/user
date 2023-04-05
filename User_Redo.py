class User:

    def __init__(self, first_name, last_name, email, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("====================")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Rewards Points: {self.gold_card_points}")
        print("====================")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_rewards_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points.")
        else:
            self.gold_card_points -= amount
        
my_user = User("Everett", "Martinez", "evere777@yahoo.com", 40)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.display_info(100)
my_user.display_info()