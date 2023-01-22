import os, sys, configparser, datetime, toml
from utils import *

DEBUG = False

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

# System Config File Handler
if (os.path.exists("system.ini")):
    system_conf = configparser.ConfigParser()
    system_conf.sections()
    system_conf.read('system.ini')
else:
    file = open("system.ini", "a")
    file.write("[MAIN]\n")
    file.write("recursion=1000\n\n")
    file.close()
    system_conf = configparser.ConfigParser()
    system_conf.sections()
    system_conf.read('system.ini')
# System Config File Handler

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
