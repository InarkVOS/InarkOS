from bin import *
from bin import __all__

ops = ['+', '-', '/', '*', '^', '**']

def check(cmd, usr):
    math = 0
    if './' not in cmd and 'tree' not in cmd and 'dir' not in cmd and 'add-package' not in cmd and 'ls' not in cmd and 'texteditor' not in cmd and 'text-editor' not in cmd:
        for op in ops:
            if op in cmd:
                math = 1
                exec(f'print(str({cmd}).split(\'.\')[0])')
                break
    if cmd.lower() == "":
        pass
    elif cmd.lower() == "texteditor" or cmd.lower() == "text-editor":
        texteditor.run(usr)
    elif cmd.lower().startswith('tree'):
        filesys.tree(cmd)
    elif cmd.lower() == "clock":
        clock.run()
    elif cmd.lower().startswith("dir") or cmd.lower().startswith("ls"):
        ls.listdirectory(cmd[3:], usr)
    elif cmd.lower().startswith("echo"):
        echo.echo(cmd)
    elif cmd.lower() == "help":
        help.help()
    elif cmd.lower() == "version":
        version.version()
    elif cmd.lower() == "clear" or cmd.lower() == "cls":
        clear.clearConsole()
    elif cmd.lower().startswith("animate"):
        animate.animate(cmd)
    elif cmd.lower() == "exit" or cmd.lower() == "shutdown":
        exit.rl()
    elif cmd.lower().startswith("pkgm install"):
        pkgm.install(cmd)
    elif cmd.lower().startswith("tutr read"):
        tutr.tutr_read(cmd.lower().split(' ')[2])
    elif cmd.lower().startswith("exec"):
        execute.exec(cmd)
    elif cmd.lower() == "pkgm list":
        pkgm.list()
    elif cmd.lower().startswith("pkgm run") or cmd.lower().startswith("./"):
        pkgm.run(cmd)
    elif cmd.lower().startswith("pkgm uninstall"):
        pkgm.uninstall(cmd)
    elif cmd.lower() == "mkusr" or cmd.lower() == "makeuser":
        usr.mkusr()
    elif cmd.lower() == "hostname":
        sys.hostname(usr)
    elif cmd.lower() == "pkgm-gui":
        command = 'pkgm install ' + guipkgm.run()
        pkgm.install(command)
    elif cmd.lower() == "matrix":
        matrix.run()
    elif cmd.lower().startswith("add-package"):
        pkgm.add_package(cmd.lower().split(' ')[1], cmd.lower().split(' ')[2])
    else:
        if math == 0:print("Command not found run help for list of commands")
        math = 1