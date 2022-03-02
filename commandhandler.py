from bin import *
from bin import __all__

def check(cmd):
    if cmd.lower() == "":
        pass
    elif cmd.lower() == "clock":
        clock.run()
    elif cmd.lower() == "dir" or cmd.lower() == "ls":
        ls.listdirectory(cmd[3:])
    elif cmd.lower().startswith("echo "):
        echo.echo(cmd)
    elif cmd.lower() == "help":
        help.help()
    elif cmd.lower() == "version":
        version.version()
    elif cmd.lower() == "clear" or cmd.lower() == "cls":
        clear.clearConsole()
    elif cmd.lower().startswith("animate "):
        animate.animate(cmd)
    elif cmd.lower() == "exit" or cmd.lower() == "shutdown":
        exit.rl()
    elif cmd.lower().startswith("pkgm install "):
        pkgm.install(cmd)
    elif cmd.lower().startswith("tutr "):
        tutr.tutr(cmd)
    elif cmd.lower().startswith("exec "):
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
        print('WORK IN PROGRESS!!!')
    elif cmd.lower() == "pkgm-gui run":
        command = 'pkgm install ' + guipkgm.run()
        pkgm.install(command)
    else:
        print("Command not found run help for list of commands")
