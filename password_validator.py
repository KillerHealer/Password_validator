import sys

from colorama import Fore


def pass_val(pw: str):
    """
        A program that validates a password's strength
        :param pw: The password to be validated
        :return: exit code 0/1
        """
    lo, upp, num, length = False, False, False, False
    if len(pw) >= 10:
        length = True
        for char in pw:
            if char.islower():
                lo = True
            if char.isupper():
                upp = True
            if char.isnumeric():
                num = True
    if lo and upp and num and length:
        print(Fore.GREEN + "This password is Valid!")
    else:
        if not length:
            print(Fore.RED + "This password is invalid because there are not enough characters!")
            exit(1)
        if not lo:
            print(Fore.RED + "This password is invalid because there are no lowercase letters!")
            exit(1)
        if not upp:
            print(Fore.RED + "This password is invalid because there are no uppercase letters!")
            exit(1)
        if not num:
            print(Fore.RED + "This password is invalid because there are no numbers!")
            exit(1)


if sys.argv[1] != '-f':
    pass_val(str(sys.argv[1]))
else:
    f = open(sys.argv[2])
    pass_val(f.read())
