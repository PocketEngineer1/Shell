import os, platform, tempfile
import commands, data, integ, functions

data.Storage = {
  "APP_DIR": str(os.path.dirname(os.path.realpath(__file__))),
  'HOME_DIR': str(os.path.expanduser('~')),
  'USER': os.getlogin(),
  'HOSTNAME': platform.node(),
  'TEMP_DIR': tempfile.mkdtemp()
}

def Main():
  if os.path.exists('INTEG') == False:
    os.mkdir('INTEG')
  integ.load()
  print('  _   _       _     __  __            _    _        _____ _          _ _  \n | \ | |     | |   |  \/  |          | |  ( )      / ____| |        | | | \n |  \| | ___ | |_  | \  / | __ _ _ __| | _|/ ___  | (___ | |__   ___| | | \n | . ` |/ _ \| __| | |\/| |/ _` | \'__| |/ / / __|  \___ \| \'_ \ / _ \ | | \n | |\  | (_) | |_  | |  | | (_| | |  |   <  \__ \  ____) | | | |  __/ | | \n |_| \_|\___/ \__| |_|  |_|\__,_|_|  |_|\_\ |___/ |_____/|_| |_|\___|_|_| \n')
  print('Welcome to Not Mark\'s Shell! A command line shell created by Not Mark, because why not!\n')
  commands.Reference('./autorun.mshell')
  while True:
    functions.cmd()
# end

if __name__ == '__main__' or __name__ == 'main':
  Main()

functions.die()