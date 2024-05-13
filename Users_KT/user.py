class User:
    count = 0

    def __init__(self, name, login, password, grade=0):
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
        
        if type(self) == User:
            User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return '********'

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    def get_info(self):
        return {
            'Name': self._name,
            'Login': self._login,
            'Grade': self._grade
        }

    def display_info(self):
        info = self.get_info()
        for key, value in info.items():
            print(f"{key}: {value}")

    @classmethod
    def get_total_users(cls):
        return cls.count
        
    def __lt__(self, other):
        return self._grade < other._grade
        
    def set_password(self, new_password):
        self._password = new_password
        
    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")
        
    @property
    def grade(self):
        return "Неизвестное свойство grade"

    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")



class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade=0):
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def get_info(self):
        info = super().get_info()
        info['Role'] = self._role
        return info

    def display_info(self):
        info = self.get_info()
        for key, value in info.items():
            print(f"{key}: {value}")

    @classmethod
    def get_total_admins(cls):
        return cls.count
