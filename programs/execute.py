import os
def exec(cmd):
        print("This code runs a command on your system do you wanna continue? (y/n)")
        t = input("Answer: ")
        if t.lower() != "y":
            print("Returning to home")
        else:
            arg = cmd.split('exec ', 1)[-1]
            print(str(os.system(f"{arg}")))