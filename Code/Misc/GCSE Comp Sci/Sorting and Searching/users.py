users = ["Jeff", "Bob", "John", "Bob#"]

new_username = "Bob"

for user in users:
    if user == new_username:
        new_username += "#"
        
users.append(new_username)

print(users)

import random
random.randint()