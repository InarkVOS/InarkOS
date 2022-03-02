from bin import *
from bin import __all__

def check(cmd):
    if cmd.lower().startswith("dir") or cmd.lower().startswith("ls"):
        ls.listdirectory(cmd[3:])
    elif cmd.lower().startswith("echo "):
        echo.echo(cmd)
    elif cmd.lower().startswith("help"):
        help.help()
    elif cmd.lower().startswith("version"):
        version.version()
    elif cmd.lower().startswith("clear") or cmd.lower().startswith("cls"):
        clear.clearConsole()
    elif cmd.lower().startswith("animate "):
        animate.animate(cmd)
    elif cmd.lower().startswith("exit") or cmd.lower().startswith("shutdown"):
        exit.rl()
    elif cmd.lower().startswith("pkgm install "):
        pkgm.install(cmd)
    elif cmd.lower().startswith("tutr "):
        tutr.tutr(cmd)
    elif cmd.lower().startswith("exec "):
        execute.exec(cmd)
    elif cmd.lower().startswith("pkgm list"):
        pkgm.list()
    elif cmd.lower().startswith("pkgm run") or cmd.lower().startswith("./"):
        pkgm.run(cmd)
    elif cmd.lower().startswith("pkgm uninstall"):
        pkgm.uninstall(cmd)
    elif cmd.lower().startswith("mkusr") or cmd.lower().startswith("makeuser"):
        usr.mkusr()
    elif cmd.lower().startswith("hostname"):
        print('WORK IN PROGRESS!!!')
    elif cmd.lower().startswith("pkgm-gui run"):
        command = 'pkgm install ' + guipkgm.run()
        pkgm.install(command)
    else:
        print("Command not found run help for list of commands")
