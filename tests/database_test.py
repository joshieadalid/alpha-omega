from database import create_tables
from user_operations import insert_user, get_users
from minute_operations import insert_minute, get_minutes

# Create tables at the start of the program (run only once)
create_tables()

# Example of insertions and queries
insert_user("John Doe", "john@example.com", "admin")
insert_minute("First meeting: discussed important topics.")

# Retrieve and display data
users = get_users()
minutes = get_minutes()
print("Users:", users)
print("Minutes:", minutes)
