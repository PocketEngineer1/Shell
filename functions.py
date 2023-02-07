import re, os, datetime, sys, subprocess, importlib
import commands, data, integ as INTEG

def die(error = False, message = "Unknown error!"):
  data.logFile.close()
  if error == True:
    sys.exit(message)
  sys.exit()
# end

def log(message, level = 0, Print = True):
  now = datetime.datetime.now()
  if (level == 0):
    data.logFile.write('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['0']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['0']+': '+str(message))
  elif (level == 1):
    data.logFile.write('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['1']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['1']+': '+str(message))
  elif (level == 2):
    data.logFile.write('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['2']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['2']+': '+str(message))
  elif (level == 3):
    data.logFile.write('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['3']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['3']+': '+str(message))
  elif (level == 4):
    data.logFile.write('['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['4']+': '+str(message))
    if Print == True:
      die(True, '['+now.strftime("%H:%M:%S")+'] '+data.config['LOGGING']['4']+': '+str(message))
  else:
    die(True, 'Invalid logging level!')
# end

def REPLACE(Input: str):
  y = str(Input)
  for x in data.Storage:
    y = y.replace("<"+x+">", data.Storage[x])
  y = re.sub('\n$', '', y)
  return y
# end

def cmd(Input = ''):
  Dir = os.path.normpath(os.getcwd())
  data.Storage['CWD'] = Dir

  if Input == '':
    Input = input(REPLACE(str(data.config['MAIN']['cmd_txt'])))

  Temp = Input.split(' ', 1)
  TMp = str(Temp[0])
  TMp = TMp.lower()
  Temp[0] = TMp

  if Temp[0] == 'help':
    if 1 < len(Temp):
      commands.Help(Temp[1].split(' '))
    else:
      commands.Help([])

  elif Temp[0] == 'debug':
    ...

  elif Temp[0] == 'cd':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        if os.access(os.path.normpath(y), os.R_OK):
          if os.path.isdir(os.path.normpath(y)):
            os.chdir(os.path.normpath(y))
          else:
            log(data.lang['ERROR']['PATH']['not_dir'], 3)
        else:
          log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
      else:
        log(data.lang['ERROR']['PATH']['invalid'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'reference' or Temp[0] == 'include':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        if os.access(os.path.normpath(y), os.R_OK):
          commands.Reference(os.path.normpath(y))
        else:
          log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
      else:
        log(data.lang['ERROR']['PATH']['invalid'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'ls' or Temp[0] == 'dir':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        if os.access(os.path.normpath(y), os.W_OK) == True:
          os.listdir(os.path.normpath(y))
        elif os.access(os.path.normpath(y), os.R_OK) == True:
          log(data.lang['ERROR']['PRIVILEGE']['read_only'], 3)
        else:
          log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
      else:
        log(data.lang['ERROR']['PATH']['invalid'], 3)
    else:
      print(os.listdir())

  elif Temp[0] == 'wait' or Temp[0] == 'input':
    if 1 < len(Temp):
      data.Storage['usr_in'] = input(REPLACE(Temp[1]))
    else:
      data.Storage['usr_in'] = input()

  elif Temp[0] == 'set':
    if 1 < len(Temp):
      TemP = Temp[1].split(' ', 1)
      if 1 < len(TemP):
        y = REPLACE(TemP[1])

        data.Storage[TemP[0]] = y
      else:
        log(data.lang['ERROR']['missing_arguement'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'integ' or Temp[0] == 'pkg':
    if 1 < len(Temp):
      log(data.lang['ERROR']['missing_command'], 4)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'echo' or Temp[0] == 'print':
    if 1 < len(Temp):
      print(REPLACE(Temp[1]))
    else:
      print()

  elif Temp[0] == 'host':
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
        if os.access(os.path.normpath(y), os.R_OK) == True:
          if os.path.isfile(os.path.normpath(y)):
            file = open(os.path.normpath(y), 'r')
            print(file.read())
            file.close()
          else:
            log(data.lang['ERROR']['PATH']['not_file'], 3)
        else:
          log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
      else:
        log(data.lang['ERROR']['PATH']['invalid'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'rm':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        if os.access(os.path.normpath(y), os.W_OK) == True:
          if os.path.isfile(os.path.normpath(y)):
            os.remove(os.path.normpath(y))
          else:
            log(data.lang['ERROR']['PATH']['not_file'], 3)
        elif os.access(os.path.normpath(y), os.R_OK) == True:
          log(data.lang['ERROR']['PRIVILEGE']['read_only'], 3)
        else:
          log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
      else:
        log(data.lang['ERROR']['PATH']['invalid'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'rmdir':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.path.exists(os.path.normpath(y)):
        if os.access(os.path.normpath(y), os.W_OK) == True:
          os.rmdir(os.path.normpath(y))
        elif os.access(os.path.normpath(y), os.R_OK) == True:
          log(data.lang['ERROR']['PRIVILEGE']['read_only'], 3)
        else:
          log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
      else:
        log(data.lang['ERROR']['PATH']['invalid'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'mkdir':
    if 1 < len(Temp):
      y = REPLACE(Temp[1])
      if os.access(Dir, os.W_OK) == True:
        if os.path.exists(os.path.normpath(y)) == False:
          os.mkdir(os.path.normpath(y))
        else:
          log(data.lang['ERROR']['PATH']['invalid'], 3)
      elif os.access(y, os.R_OK) == True:
        log(data.lang['ERROR']['PRIVILEGE']['read_only'], 3)
      else:
        log(data.lang['ERROR']['PRIVILEGE']['forbidden'], 3)
    else:
      commands.Help([Temp[0]])

  elif Temp[0] == 'test':
    if 1 < len(Temp):
      if Temp[1] == 'ls':
        for i in os.listdir(REPLACE('<APP_DIR>')+'/INTEG'):
          if os.path.isdir(os.path.normpath(REPLACE('<APP_DIR>')+'/INTEG/'+i)):
            print(i)
      elif Temp[1] == 'integ':
        INTEG.load()
      else:
        file_path = os.path.normpath(REPLACE('<APP_DIR>')+'/INTEG/'+i)
        module_name = i

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Verify contents of the module:
        print(dir(module))

  elif Temp[0] == 'clear' or Temp[0] == 'cls':
    if os.name == 'nt':
      log(lang['COMMAND_OUTPUT']['CLEAR']['main'], 1, False)
      subprocess.run("cls")
    else:
      log(data.lang['COMMAND_OUTPUT']['CLEAR']['main'], 1, False)
      subprocess.run("clear")

  for k in data.INTEG_Storage:
    for t in data.INTEG_Storage[k]['aliases']:
      if Temp[0] == t.lower():
        # print(data.INTEG_Storage[k]['module'])
        data.INTEG_Storage[k]['module'].integ(Temp)
        return

    if Temp[0] == 'exit' or Temp[0] == 'quit' or Temp[0] == 'die' or Temp[0] == 'end' or Temp[0] == 'abort' or Temp[0] == 'abandon':
      log(data.lang['GENERAL']['normal_exit'], 1)
      die()

    elif Temp[0] == '':
      log(data.lang['ERROR']['no_command_inputted'], 3)
      return

    else:
      log(data.lang['ERROR']['unknown_command'], 3)
      return
# end