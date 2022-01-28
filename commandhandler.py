from programs import *
from programs import __all__

def check(cmd):
    if cmd.startswith("dir") or cmd.startswith("ls"):
        ls.listdirectory(cmd[3:])
    elif cmd.startswith("./"):
        programmanager.run(cmd[2:])
    elif cmd.startswith("echo "):
        echo.echo(cmd)
    elif cmd.startswith("help"):
        help.help()
    elif cmd.startswith("version"):
        version.version()
    elif cmd.startswith("clear") or cmd.startswith("cls"):
        clear.clearConsole()
    elif cmd.startswith("animate "):
        animate.animate(cmd)
    elif cmd.startswith("fetchinfo"):
        fetchinfo.fetchinfo()     
    elif cmd.startswith("exit"):
        exit.rl()          
    elif cmd.startswith("pkgm downloadrepo"):
        pkgm.downloadrepo()
    elif cmd.startswith("pkgm install "):
        pkgm.install(cmd)
    elif cmd.startswith("tutr "):
        tutr.tutr(cmd)
    else:            
        print("Command not found do help for help")