import os, sys, configparser, datetime, re, subprocess, toml, json, json5, yaml, xml

home_directory = os.path.expanduser( '~' )
now = datetime.datetime.now()

if (os.path.exists('log/')):
    logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
else:
    os.mkdir('log')
    logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")

def die(error = False, message = "Unknown error!"):
    logFile.close()
    if error == True:
        sys.exit(message)
    sys.exit()

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

if (os.path.exists("config.ini")):
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
else:
    file = open("config.ini", "a")
    file.write("[MAIN]\n")
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

if os.path.exists('./lang/'+config['MAIN']['lang']+'.toml'):
    lang = toml.decoder.load('./lang/'+config['MAIN']['lang']+'.toml')

elif os.path.exists('./lang/'+config['MAIN']['lang']+'.json'):
    file = open('./lang/'+config['MAIN']['lang']+'.json', 'r')
    lang = json.load(file)
    file.close()

elif os.path.exists('./lang/'+config['MAIN']['lang']+'.json5'):
    file = open('./lang/'+config['MAIN']['lang']+'.json5', 'r')
    lang = json5.load(file)
    file.close()
    
elif os.path.exists('./lang/'+config['MAIN']['lang']+'.yaml'):
    file = open('./lang/'+config['MAIN']['lang']+'.yaml', 'r')
    lang = yaml.safe_load(file)
    file.close()
    
elif os.path.exists('./lang/'+config['MAIN']['lang']+'.xml'):
    print

else:
    raise FileExistsError('Failed to locate language file')

def Help(command=''):
    if command == '':
        print(lang['HELP']['more_info']+'\n')
        print('HELP           '+lang['HELP']['HELP']['main'])
        print('CD             '+lang['HELP']['CD']['main'])
        print('LS             '+lang['HELP']['LIST_DIR']['main'])
        print('DIR            '+lang['HELP']['LIST_DIR']['main'])
        print('CLS            '+lang['HELP']['CLEAR']['main'])
        print('CLEAR          '+lang['HELP']['CLEAR']['main'])
        print('READ           '+lang['HELP']['READ']['main'])
        print('DUMP           '+lang['HELP']['READ']['main'])
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

    elif command.upper() == 'HELP':
        print(lang['HELP']['HELP']['main']+'\n')

    elif command.upper() == 'CD':
        print(lang['HELP']['CD']['main']+'\n')

    elif command.upper() == 'LS':
        print(lang['HELP']['LIST_DIR']['main']+'\n')

    elif command.upper() == 'DIR':
        print(lang['HELP']['LIST_DIR']['main']+'\n')

    elif command.upper() == 'CLS':
        print(lang['HELP']['CLEAR']['main']+'\n')

    elif command.upper() == 'CLEAR':
        print(lang['HELP']['CLEAR']['main']+'\n')

    elif command.upper() == 'READ':
        print(lang['HELP']['READ']['main']+'\n')

    elif command.upper() == 'DUMP':
        print(lang['HELP']['READ']['main']+'\n')

    elif command.upper() == 'HOST':
        print(lang['HELP']['HOST_CMD']['main']+'\n')

    elif command.upper() == 'INTEG':
        print(lang['HELP']['PACKAGE']['main']+'\n')
        print('INSTALL        '+lang['HELP']['PACKAGE']['SUB']['install'])
        print('REMOVE         '+lang['HELP']['PACKAGE']['SUB']['remove'])

    elif command.upper() == 'PKG':
        print(lang['HELP']['PACKAGE']['main']+'\n')
        print('INSTALL        '+lang['HELP']['PACKAGE']['SUB']['install'])
        print('REMOVE         '+lang['HELP']['PACKAGE']['SUB']['remove'])

    elif command.upper() == 'EXIT':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'QUIT':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'DIE':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'END':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'ABORT':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'ENDCLI':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'ABANDON':
        print(lang['HELP']['EXIT']['main']+'\n')

    elif command.upper() == 'SYS':
        print(lang['HELP']['SYSTEM']['main']+'\n')
        print('RECURSION      '+lang['HELP']['SYSTEM']['SUB']['recursion'])

    elif command.upper() == 'SYSTEM':
        print(lang['HELP']['SYSTEM']['main']+'\n')
        print('RECURSION      '+lang['HELP']['SYSTEM']['SUB']['recursion'])

def cmd():
    Dir = os.path.normpath(os.getcwd())
    usr_in = input(Dir+'>')

    if usr_in.lower().startswith('help'):
        if usr_in.lower().startswith('help '):
            Help(re.split('help ', usr_in, 1, flags=re.IGNORECASE)[1])
        else:
            Help()

    elif usr_in.lower().startswith('cd'):
        if usr_in.lower().startswith('cd '):
            if os.path.exists(os.path.normpath(re.split('cd ', usr_in, 1, flags=re.IGNORECASE)[1])):
                os.chdir(os.path.normpath(re.split('cd ', usr_in, 1, flags=re.IGNORECASE)[1]))
            else:
                log(lang['ERROR']['no_file_directory'], 3)
        else:
            Help('CD')

    elif usr_in.lower().startswith('ls'):
        if usr_in.lower().startswith('ls '):
            if os.path.exists(os.path.normpath(re.split('ls ', usr_in, 1, flags=re.IGNORECASE)[1])):
                print(os.listdir(os.path.normpath(re.split('ls ', usr_in, 1, flags=re.IGNORECASE)[1])))
            else:
                log(lang['ERROR']['no_file_directory'], 3)
        else:
            print(os.listdir(os.path.normpath(re.split('ls', usr_in, 1, flags=re.IGNORECASE)[1])))

    elif usr_in.lower().startswith('dir'):
        if usr_in.lower().startswith('dir '):
            if os.path.exists(os.path.normpath(re.split('dir ', usr_in, 1, flags=re.IGNORECASE)[1])):
                print(os.listdir(os.path.normpath(re.split('dir ', usr_in, 1, flags=re.IGNORECASE)[1])))
            else:
                log(lang['ERROR']['no_file_directory'], 3)
        else:
            print(os.listdir(os.path.normpath(re.split('dir', usr_in, 1, flags=re.IGNORECASE)[1])))

    elif usr_in.lower().startswith('sys'):
        if usr_in.lower().startswith('sys '):
            log(lang['ERROR']['missing_command'], 4)
        else:
            Help('SYS')
    
    elif usr_in.lower().startswith('system'):
        if usr_in.lower().startswith('system '):
            log(lang['ERROR']['missing_command'], 4)
        else:
            Help('SYSTEM')

    elif usr_in.lower().startswith('integ'):
        if usr_in.lower().startswith('integ '):
            log(lang['ERROR']['missing_command'], 4)
        else:
            Help('INTEG')

    elif usr_in.lower().startswith('pkg'):
        if usr_in.lower().startswith('pkg '):
            log(lang['ERROR']['missing_command'], 4)
        else:
            Help('PKG')

    elif usr_in.lower().startswith('host'):
        log("It appears that this may not work correctly", 2)
        if usr_in.lower().startswith('host '):
            log(re.split('host ', usr_in, 1, flags=re.IGNORECASE)[1], Print=False)
            subprocess.run(re.split('host ', usr_in, 1, flags=re.IGNORECASE)[1].split(" "))
        else:
            Help('HOST')

    elif usr_in.lower().startswith('read'):
        if usr_in.lower().startswith('read '):
            if os.path.exists(os.path.normpath(re.split('read ', usr_in, 1, flags=re.IGNORECASE)[1])):
                if os.path.isfile(os.path.normpath(re.split('read ', usr_in, 1, flags=re.IGNORECASE)[1])):
                    file = open(os.path.normpath(re.split('read ', usr_in, 1, flags=re.IGNORECASE)[1]), 'r')
                    print(file.read())
                    file.close()
            else:
                log(lang['ERROR']['no_file_directory'], 3)
        else:
            Help('READ')

    elif usr_in.lower().startswith('dump'):
        if usr_in.lower().startswith('dump '):
            if os.path.exists(os.path.normpath(re.split('dump ', usr_in, 1, flags=re.IGNORECASE)[1])):
                if os.path.isfile(os.path.normpath(re.split('dump ', usr_in, 1, flags=re.IGNORECASE)[1])):
                    file = open(os.path.normpath(re.split('dump ', usr_in, 1, flags=re.IGNORECASE)[1]), 'r')
                    print(file.read())
                    file.close()
            else:
                log(lang['ERROR']['no_file_directory'], 3)
        else:
            Help('DUMP')
            
    elif usr_in.lower().startswith('clear') or usr_in.lower().startswith('cls'):
        if os.name == 'nt':
            log(lang['COMMAND_OUTPUT']['CLEAR']['main'], 1, False)
            subprocess.run("cls")
        else:
            log(lang['COMMAND_OUTPUT']['CLEAR']['main'], 1, False)
            subprocess.run("clear")

    elif usr_in.lower().startswith('exit') or usr_in.lower().startswith('quit') or usr_in.lower().startswith('die') or usr_in.lower().startswith('endcli') or usr_in.lower().startswith('end') or usr_in.lower().startswith('abort') or usr_in.lower().startswith('abandon'):
        log(lang['GENERAL']['normal_exit'], 1)
        die()

    elif usr_in == '':
        log(lang['ERROR']['no_command_inputted'], 3)

    else:
        log(lang['ERROR']['unknown_command'], 3)

    cmd()

print('   _____ _          _ _  \n  / ____| |        | | | \n | (___ | |__   ___| | | \n  \___ \| \'_ \ / _ \ | | \n  ____) | | | |  __/ | | \n |_____/|_| |_|\___|_|_| \n')
print('Welcome to Shell! A command line shell created by Not Mark, because why not!\nNote: The command set is bit of everything.\n')
cmd()
die()