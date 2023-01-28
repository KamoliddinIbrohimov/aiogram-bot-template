from utils.db_api.sqlite import Database


db = Database()


def test():
    db.create_table_user()
    users = db.select_all_users()
    print(f"Existing users in the database: {users=}")
    db.add_user(1, "One", "email")
    db.add_user(2, "Two", "user@gmail.com")
    db.add_user(3, "Three", "user@gmail.com")
    db.add_user(4, "Four", "user@gmail.")

    users = db.select_all_users()
    print(f"Existing users in the database: {users=}")

    user = db.select_user(Name="Four", id=4)
    print(f"User: {user}")

    count = db.count_user()
    print(f"Count: {count}")

test()