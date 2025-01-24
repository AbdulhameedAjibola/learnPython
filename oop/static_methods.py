class User:
    all = []
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

        assert len(password) >=8, "Password not long enough, try again"
        User.all.append(self)

    # to declare a static method, we use a decorator just as we used for the class method
    @staticmethod
    def is_integer(self):
# so this method is used to check if a number is an integer or not
        