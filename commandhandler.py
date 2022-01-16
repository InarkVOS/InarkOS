from programs import *
from programs import __all__

def check(cmd):
    if cmd.startswith("dir") or cmd.startswith("ls"):
        ls.listdirectory(cmd[3:])
    elif cmd.startswith("./"):
        programmanager.run(cmd[2:])
    elif cmd.startswith("micro"):
        micro.run()
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
<<<<<<< HEAD
=======
    elif cmd.startswith("pkgm install "):
        pkgm.install(cmd)
    elif cmd.startswith("./"):
        executables.run(cmd)
>>>>>>> eab552289164e59aed0f5ab5d726e60da98ba0fc
    else:            
        print("Command not found do help for help")