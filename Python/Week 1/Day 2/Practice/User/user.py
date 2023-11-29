class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Insufficient points.")
        else:
            self.gold_card_points -= amount


# Testing the User class
user1 = User("John", "Doe", "john@example.com", 30)
user1.display_info()
print("Enrolling user1...")
user1.enroll()

user2 = User("Alice", "Smith", "alice@example.com", 25)
user3 = User("Bob", "Johnson", "bob@example.com", 35)

user1.spend_points(50)
user2.enroll()
user2.spend_points(80)

print("\nDisplaying user information:")
user1.display_info()
user2.display_info()
user3.display_info()

# Bonus
print("\nAttempting to re-enroll user1:")
user1.enroll()

print("\nAttempting to spend 40 points by user3:")
user3.spend_points(40)
user3.display_info()
