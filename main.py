import os, subprocess, platform, re
from utils import *
from lib import *

debug_log(config)
debug_log(lang)

def REPLACE(Input: str):
  y = str(Input)
  for x in UserStorage:
    y = y.replace("<"+x+">", UserStorage[x])
  y = re.sub('\n$', '', y)
  debug_log(y)
  return y

class commands:
  def Reference(ScriptPath: str):
    if os.path.exists(ScriptPath):
      with open(ScriptPath) as script:
        for line in script:
          debug_log(line)
          cmd(line)
  # end

  def Help(Input: list):
    if 0 < len(Input):
      Input[0] = Input[0].upper()

      if Input[0] == 'HELP':
        print(lang['HELP']['HELP']['main']+'\n')

      elif Input[0] == 'CD':
        print(lang['HELP']['CD']['main']+'\n')

      elif Input[0] == 'LS' or Input[0] == 'DIR':
        print(lang['HELP']['LIST_DIR']['main']+'\n')

      elif Input[0] == 'RMDIR':
        print(lang['HELP']['REMOVE_DIRECTORY']['main']+'\n')

      elif Input[0] == 'MKDIR':
        print(lang['HELP']['MAKE_DIRECTORY']['main']+'\n')

      elif Input[0] == 'RM':
        print(lang['HELP']['REMOVE_FILE']['main']+'\n')

      elif Input[0] == 'CLS' or Input[0] == 'CLEAR':
        print(lang['HELP']['CLEAR']['main']+'\n')

      elif Input[0] == 'PRINT' or Input[0] == 'ECHO':
        print(lang['HELP']['PRINT']['main']+'\n')

      elif Input[0] == 'REFERENCE' or Input[0] == 'INCLUDE':
        print(lang['HELP']['REFERENCE_SCRIPT']['main']+'\n')

      elif Input[0] == 'WAIT' or Input[0] == 'INPUT':
        print(lang['HELP']['USER_INPUT']['main']+'\n')

      elif Input[0] == 'READ' or Input[0] == 'DUMP':
        print(lang['HELP']['READ']['main']+'\n')

      elif Input[0] == 'LOGIC':
        if 1 < len(Input):
          Input[1] = Input[1].upper()

          if Input[1] == 'IF':
            print(lang['HELP']['LOGIC']['if']+'\n')

        else:
          print(lang['HELP']['LOGIC']['main']+'\n')

      elif Input[0] == 'HOST':
        print(lang['HELP']['HOST_CMD']['main']+'\n')

      elif Input[0] == 'INTEG' or Input[0] == 'PKG':
        if 1 < len(Input):
          Input[1] = Input[1].upper()

          if Input[1] == 'INSTALL':
            print(lang['HELP']['PACKAGE']['install']+'\n')

          elif Input[1] == 'REMOVE':
            print(lang['HELP']['PACKAGE']['remove']+'\n')

        else:
          print(lang['HELP']['PACKAGE']['main']+'\n')

      elif Input[0] == 'EXIT' or Input[0] == 'QUIT' or Input[0] == 'DIE' or Input[0] == 'END' or Input[0] == 'ABORT' or Input[0] == 'ENDCLI' or Input[0] == 'ABANDON':
        print(lang['HELP']['EXIT']['main']+'\n')

      elif Input[0] == 'SYS' or Input[0] == 'SYSTEM':
        if 1 < len(Input):
          Input[1] = Input[1].upper()

          if Input[1] == 'RECURSION':
            print(lang['HELP']['SYSTEM']['recursion']+'\n')
        else:
          print(lang['HELP']['SYSTEM']['main']+'\n')

    else:
      print(lang['HELP']['more_info']+'\n')
      print('HELP           '+lang['HELP']['HELP']['main'])
      print('CD             '+lang['HELP']['CD']['main'])
      print('LS             '+lang['HELP']['LIST_DIR']['main'])
      print('DIR            '+lang['HELP']['LIST_DIR']['main'])
      print('RMDIR          '+lang['HELP']['REMOVE_DIRECTORY']['main'])
      print('MKDIR          '+lang['HELP']['MAKE_DIRECTORY']['main'])
      print('RM             '+lang['HELP']['REMOVE_FILE']['main'])
      print('CLS            '+lang['HELP']['CLEAR']['main'])
      print('CLEAR          '+lang['HELP']['CLEAR']['main'])
      print('ECHO           '+lang['HELP']['PRINT']['main'])
      print('PRINT          '+lang['HELP']['PRINT']['main'])
      print('REFERENCE      '+lang['HELP']['REFERENCE_SCRIPT']['main'])
      print('INCLUDE        '+lang['HELP']['REFERENCE_SCRIPT']['main'])
      print('WAIT           '+lang['HELP']['USER_INPUT']['main'])
      print('INPUT          '+lang['HELP']['USER_INPUT']['main'])
      print('READ           '+lang['HELP']['READ']['main'])
      print('DUMP           '+lang['HELP']['READ']['main'])
      print('LOGIC          '+lang['HELP']['LOGIC']['main'])
      print('HOST           '+lang['HELP']['HOST_CMD']['main'])
      print('INTEG          '+lang['HELP']['PACKAGE']['main'])
      print('PKG            '+lang['HELP']['PACKAGE']['main'])
      print('EXIT           '+lang['HELP']['EXIT']['main'])
      print('QUIT           '+lang['HELP']['EXIT']['main'])
      print('DIE            '+lang['HELP']['EXIT']['main'])
      print('END            '+lang['HELP']['EXIT']['main'])
      print('ABORT          '+lang['HELP']['EXIT']['main'])
      print('ENDCLI         '+lang['HELP']['EXIT']['main'])
      print('ABANDON        '+lang['HELP']['EXIT']['main'])
      print('SYS            '+lang['HELP']['SYSTEM']['main'])
      print('SYSTEM         '+lang['HELP']['SYSTEM']['main'])
  # end

  class system:
    def recursion(limit: int):
      sys.setrecursionlimit(limit)
      system_conf['MAIN']['recursion'] = str(limit)
      with open('system.ini', 'w') as conf:
        system_conf.write(conf)
    # end
  # end
# end

UserStorage = {
  "APP_DIR": str(os.path.normpath(os.getcwd())),
  "HOME_DIR": str(os.path.normpath(os.path.expanduser('~'))),
  "USER": str(os.getlogin()),
  "HOSTNAME": str(platform.node())
}

def cmd(Input = ''):
  Dir = os.path.normpath(os.getcwd())
  UserStorage['CWD'] = Dir

  if Input == '':
    loop = True
    Input = input(REPLACE(str(config['MAIN']['cmd_txt'])))
  else:
    loop = False

  Temp = Input.split(' ', 1)
  TMp = str(Temp[0])
  TMp = TMp.lower()
  Temp[0] = TMp
  debug_log(Input)
  debug_log(Temp)

  if Temp[0] == 'help':
    if 1 < len(Temp):
      commands.Help(Temp[1].split(' '))
    else:
      commands.Help([])

  elif Temp[0] == 'debug':
    debug_log(UserStorage)

  elif Temp[0] == 'cd':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        os.chdir(os.path.normpath(y))
      else:
        log(lang['ERROR']['invalid_path'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'reference' or Temp[0] == 'include':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        commands.Reference(y)
      else:
        log(lang['ERROR']['invalid_path'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'ls' or Temp[0] == 'dir':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        print(os.listdir(os.path.normpath(y)))
      else:
        log(lang['ERROR']['invalid_path'], 3)
    else:
      print(os.listdir())

  elif Temp[0] == 'sys' or Temp[0] == 'system':
    debug_die()
    if 1 < len(Temp):
      TEmp = Input.split(' ', 1)
      if 1 < len(TEmp):
        if TEmp[0] == 'recursion':
          commands.system.recursion(TEmp[1])
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'wait' or Temp[0] == 'input':
    if 1 < len(Temp):
      UserStorage['usr_in'] = input(REPLACE(Temp[1]))
    else:
      UserStorage['usr_in'] = input()

  elif Temp[0] == 'logic':
    if 1 < len(Temp):
      TemP = Temp[1].split(' ', 1)
      if 1 < len(TemP):
        if TemP[0].lower() == 'if':
          temp = TemP[1].split(' ', 2)
          if 2 < len(temp):
            debug_log(temp)
            temp[0] = REPLACE(temp[0])
            temp[1] = REPLACE(temp[1])
            temp[2] = REPLACE(temp[2])
            debug_log(temp)
            if temp[0] == temp[1]:
              cmd(temp[2])
        else:
          log(lang['ERROR']['missing_arguement'], 3)
      else:
        commands.Help([Temp[0]])
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'set':
    if 1 < len(Temp):
      TemP = Temp[1].split(' ', 1)
      if 1 < len(TemP):
        debug_log(TemP)
        y = REPLACE(TemP[1])

        UserStorage[TemP[0]] = y
      else:
        log(lang['ERROR']['missing_arguement'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'integ' or Temp[0] == 'pkg':
    debug_die()
    if 1 < len(Temp):
      log(lang['ERROR']['missing_command'], 4)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'echo' or Temp[0] == 'print':
    if 1 < len(Temp):
      print(REPLACE(Temp[1]))
    else:
      print()

  elif Temp[0] == 'host':
    debug_die()
    y = REPLACE(Temp[1])
    log("It appears that this may not work correctly", 2)
    if 1 < len(Temp):
      log(Temp[1], Print=False)
      subprocess.run(Temp[1])
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'read' or Temp[0] == 'dump':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        if os.path.isfile(os.path.normpath(y)):
          file = open(os.path.normpath(y), 'r')
          print(file.read())
          file.close()
        else:
          log(lang['ERROR']['invalid_path'], 3)
      else:
        commands.Help([Temp[0]])

  elif Temp[0] == 'rm':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        os.remove(os.path.normpath(y))
      else:
        log(lang['ERROR']['invalid_path'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'rmdir':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        os.rmdir(os.path.normpath(y))
      else:
        log(lang['ERROR']['invalid_path'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'mkdir':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)) == False:
        os.mkdir(os.path.normpath(y))
      else:
        log(lang['ERROR']['existing_path'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'clear' or Temp[0] == 'cls':
    if os.name == 'nt':
      log(lang['COMMAND_OUTPUT']['CLEAR']['main'], 1, False)
      subprocess.run("cls")
    else:
      log(lang['COMMAND_OUTPUT']['CLEAR']['main'], 1, False)
      subprocess.run("clear")

  elif Temp[0] == 'exit' or Temp[0] == 'quit' or Temp[0] == 'die' or Temp[0] == 'end' or Temp[0] == 'abort' or Temp[0] == 'abandon':
    log(lang['GENERAL']['normal_exit'], 1)
    die()

  elif Temp[0] == '':
    log(lang['ERROR']['no_command_inputted'], 3)

  else:
    log(lang['ERROR']['unknown_command'], 3)

  if loop == True:
    cmd()
# end of function

commands.Reference('./autorun.mshell')

print('  _   _       _     __  __            _    _        _____ _          _ _  \n | \ | |     | |   |  \/  |          | |  ( )      / ____| |        | | | \n |  \| | ___ | |_  | \  / | __ _ _ __| | _|/ ___  | (___ | |__   ___| | | \n | . ` |/ _ \| __| | |\/| |/ _` | \'__| |/ / / __|  \___ \| \'_ \ / _ \ | | \n | |\  | (_) | |_  | |  | | (_| | |  |   <  \__ \  ____) | | | |  __/ | | \n |_| \_|\___/ \__| |_|  |_|\__,_|_|  |_|\_\ |___/ |_____/|_| |_|\___|_|_| \n')
print('Welcome to Not Mark\'s Shell! A command line shell created by Not Mark, because why not!\n')
cmd()
die()