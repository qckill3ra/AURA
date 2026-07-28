class Permissions:

    RULES = {
        "read_personal_files": False,
        "read_passwords": False,
        "delete_files": False,
        "internet_access": False,
        "execute_scripts": "confirmation"
    }


    def check(self, action):

        if action not in self.RULES:
            return False

        return self.RULES[action]