def echo(cmd):
        argonly = cmd.split('echo ', 1)[-1]
        print(argonly)