import os


def tutr(command):
    arg = command.split('tutr ', 1)[-1]
    if arg.lower().startswith("readdocs "):
        filename = arg.split('readdocs ', 1)[-1]
        if os.path.exists("docs/" + filename + ".txt"):
            with open('docs/' + filename + ".txt", 'r') as f:
                print(f.read())
        else:
            print("No documentation found for: " + filename)
