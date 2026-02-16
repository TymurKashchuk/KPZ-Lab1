from user_module import User

class Privileges:
    def __init__(self, privileges_list=None):
        if privileges_list is None:
            privileges_list = []
        self.privileges = privileges_list

    def show_privileges(self):
        if self.privileges:
            return "Привілеї адміністратора:\n" + "\n".join(f"- {p}" for p in self.privileges)
        return "Привілеї не задані"


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter, privileges_list=None):
        super().__init__(first_name, last_name, email, nickname, newsletter)
        self.privileges = Privileges(privileges_list)