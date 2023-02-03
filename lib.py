import os, sys, configparser, datetime, toml, platform, re, importlib

DEBUG = False
INTEG_Storage = {}

now = datetime.datetime.now()
if os.path.exists('log/'):
  logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
else:
  os.mkdir('log')
  logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
# end

def die(error = False, message = "Unknown error!"):
  logFile.close()
  if error == True:
    sys.exit(message)
  sys.exit()
# end

def log(message, level = 0, Print = True):
  now = datetime.datetime.now()
  if (level == 0):
    logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['0']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['0']+': '+str(message))
  elif (level == 1):
    logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['1']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['1']+': '+str(message))
  elif (level == 2):
    logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['2']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['2']+': '+str(message))
  elif (level == 3):
    logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['3']+': '+str(message)+'\n')
    if Print == True:
      print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['3']+': '+str(message))
  elif (level == 4):
    logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['4']+': '+str(message))
    if Print == True:
      die(True, '['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['4']+': '+str(message))
  else:
    die(True, 'Invalid logging level!')
# end

def debug_log(message, level = 0, Print = True):
  if DEBUG:
    now = datetime.datetime.now()
    if (level == 0):
      logFile.write('['+now.strftime("%H:%M:%S")+'] DEBUG: '+str(message)+'\n')
      if Print == True:
        print('['+now.strftime("%H:%M:%S")+'] DEBUG: '+str(message))
    else:
      die(True, 'Invalid logging level!')
# end

# Config File Handler
if (os.path.exists("config.ini")):
  config = configparser.ConfigParser()
  config.sections()
  config.read('config.ini')
else:
  file = open("config.ini", "a")
  file.write("[MAIN]\n")
  file.write("cmd_txt=<CWD>>\n")
  file.write("lang=en_US\n\n")
  file.write("[LOGGING]\n")
  file.write("0=LOG\n")
  file.write("1=INFO\n")
  file.write("2=WARN\n")
  file.write("3=ERROR\n")
  file.write("4=FATAL ERROR")
  file.close()
  config = configparser.ConfigParser()
  config.sections()
  config.read('config.ini')
  log('No config file found!', 2)
# Config File Handler

# Language File Handler
if os.path.exists('./lang/'+config['MAIN']['lang']+'.toml'):
  lang = toml.decoder.load('./lang/'+config['MAIN']['lang']+'.toml')
else:
  raise FileExistsError('Failed to locate language file')
# Language File Handler

def debug_die():
  if DEBUG != True:
    die()
# end

UserStorage = {
  "APP_DIR": str(os.path.dirname(os.path.realpath(__file__))),
  "HOME_DIR": str(os.path.normpath(os.path.expanduser('~'))),
  "USER": str(os.getlogin()),
  "HOSTNAME": str(platform.node())
}

def REPLACE(Input: str):
  y = str(Input)
  for x in UserStorage:
    y = y.replace("<"+x+">", UserStorage[x])
  y = re.sub('\n$', '', y)
  debug_log(y)
  return y
# end

class INTEG:
  def load():
    for i in os.listdir(REPLACE('<APP_DIR>')+'/INTEG'):
      if os.path.isdir(REPLACE('<APP_DIR>')+'/INTEG/'+i):
        if os.path.exists(REPLACE('<APP_DIR>')+'/INTEG/'+i+'/integ.toml'):
          integ_config = toml.decoder.load(REPLACE('<APP_DIR>')+'/INTEG/'+i+'/integ.toml')

          spec = importlib.util.spec_from_file_location(i, REPLACE('<APP_DIR>')+'/INTEG/'+i+'/'+integ_config['MAIN']['script'])
          module = importlib.util.module_from_spec(spec)
          spec.loader.exec_module(module)

          INTEG_Storage[i] = {
            'config': integ_config,
            'module': module,
            'aliases': integ_config['MAIN']['aliases'],
            'dir': REPLACE('<APP_DIR>')+'/INTEG',
            'lang': {}
          }

          if os.path.exists(REPLACE('<APP_DIR>')+'/INTEG/'+i+'/lang'):
            for w in os.listdir(REPLACE('<APP_DIR>')+'/INTEG/'+i+'/lang'):
              INTEG_Storage[i]['lang'][os.path.splitext(w)[0]] = toml.decoder.load(REPLACE('<APP_DIR>')+'/INTEG/'+i+'/lang/'+w)
    if config['MAIN']['lang'] in INTEG_Storage[i]['lang']:
      lang.update(INTEG_Storage[i]['lang'][config['MAIN']['lang']])
  # end
# end
