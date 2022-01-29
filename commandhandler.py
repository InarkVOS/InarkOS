from programs import *
from programs import __all__

def check(cmd):
    if cmd.lower().startswith("dir") or cmd.lower().startswith("ls"):
        ls.listdirectory(cmd[3:])
    elif cmd.lower().startswith("./"):
        programmanager.run(cmd[2:])
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
    elif cmd.lower().startswith("fetchinfo"):
        fetchinfo.fetchinfo()     
    elif cmd.lower().startswith("exit"):
        exit.rl()          
    elif cmd.lower().startswith("pkgm downloadrepo"):
        pkgm.downloadrepo()
    elif cmd.lower().startswith("pkgm install "):
        pkgm.install(cmd)
    elif cmd.lower().startswith("tutr "):
        tutr.tutr(cmd)
    else:            
        print("Command not found do help for help")