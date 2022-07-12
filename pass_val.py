def pass_val(pw: str):
        """
        A program that validates a password's strength
        :param pw: The password to be validated
        :return: exit code 0/1
        """
        if len(pw)>=10:
                for char in pw:
                        if char.islower():
                                pass