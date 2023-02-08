import os, configparser, toml, platform
import commands, data, integ, functions, lib

data.Storage = {
  "APP_DIR": str(os.path.dirname(os.path.realpath(__file__))),
  "HOME_DIR": str(os.path.normpath(os.path.expanduser('~'))),
  "USER": str(os.getlogin()),
  "HOSTNAME": str(platform.node())
}

data.config = lib.Handler.Config()
data.lang = lib.Handler.Lang()
# data.logFile = lib.Handler.Log()

def main():
  if os.path.exists('INTEG') == False:
    os.mkdir('INTEG')
  print('  _   _       _     __  __            _    _        _____ _          _ _  \n | \ | |     | |   |  \/  |          | |  ( )      / ____| |        | | | \n |  \| | ___ | |_  | \  / | __ _ _ __| | _|/ ___  | (___ | |__   ___| | | \n | . ` |/ _ \| __| | |\/| |/ _` | \'__| |/ / / __|  \___ \| \'_ \ / _ \ | | \n | |\  | (_) | |_  | |  | | (_| | |  |   <  \__ \  ____) | | | |  __/ | | \n |_| \_|\___/ \__| |_|  |_|\__,_|_|  |_|\_\ |___/ |_____/|_| |_|\___|_|_| \n')
  print('Welcome to Not Mark\'s Shell! A command line shell created by Not Mark, because why not!\n')
  integ.load() 
  commands.Reference('./autorun.mshell')
  while True:
    functions.cmd()
# end

if __name__ == '__main__' or __name__ == 'main':
  main()

functions.die()