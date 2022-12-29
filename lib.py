import os, sys, configparser, datetime, toml
from utils import *

home_directory = os.path.expanduser( '~' )
now = datetime.datetime.now()

if (os.path.exists('log/')):
    logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
else:
    os.mkdir('log')
    logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
# end of if else satement

def die(error = False, message = "Unknown error!"):
    logFile.close()
    if error == True:
        sys.exit(message)
    sys.exit()
# end of function

def log(message, level = 0, Print = True):
    now = datetime.datetime.now()
    if (level == 0):
        logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['0']+': '+message+'\n')
        if Print == True:
            print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['0']+': '+message)
    elif (level == 1):
        logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['1']+': '+message+'\n')
        if Print == True:
            print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['1']+': '+message)
    elif (level == 2):
        logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['2']+': '+message+'\n')
        if Print == True:
            print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['2']+': '+message)
    elif (level == 3):
        logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['3']+': '+message+'\n')
        if Print == True:
            print('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['3']+': '+message)
    elif (level == 4):
        logFile.write('['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['4']+': '+message)
        if Print == True:
            die(True, '['+now.strftime("%H:%M:%S")+'] '+config['LOGGING']['4']+': '+message)
    else:
        die(True, 'Invalid logging level!')
# end of function

# Config File Handler
if (os.path.exists("config.ini")):
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
else:
    file = open("config.ini", "a")
    file.write("[MAIN]\n")
    file.write("lang=en_US\n")
    file.write("fallback_lang=fallback\n\n")
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
if os.path.exists('./lang/'+config['MAIN']['fallback_lang']+'.toml'):
    lang = toml.decoder.load('./lang/'+config['MAIN']['fallback_lang']+'.toml')
else:
    raise FileExistsError('Failed to locate fallback language file')

if os.path.exists('./lang/'+config['MAIN']['lang']+'.toml'):
    Merge(toml.decoder.load('./lang/'+config['MAIN']['lang']+'.toml'), lang)
else:
    raise FileExistsError('Failed to locate language file')
# Language File Handler