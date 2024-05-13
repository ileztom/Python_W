from user import User, SuperUser

def main():
    user1 = User('Paul McCartney', 'paul', '1234', 3)
    user2 = User('George Harrison', 'george', '5678', 2)
    user3 = User('Richard Starkey', 'ringo', '8523', 3)
    admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

    user1.display_info()
    admin.display_info()

    print()

    total_users = User.get_total_users()
    total_admins = SuperUser.get_total_admins()

    print(f'Всего обычных пользователей: {total_users}')
    print(f'Всего супер-пользователей: {total_admins}')

    print()

    print(user1.grade < user2.grade)
    print(admin.grade > user3.grade)
    print(user1.grade == user3.grade)

    print()

    user3.name = 'Ringo Star'
    user1.set_password('Pa$$w0rd')

    print(user3.name)
    print(user2.password)
    print(user2.login)

    user2.login = 'geo'

    print(user1.grade)
    admin.grade = 10


if __name__ == "__main__":
    main()
