import os, sys, configparser, datetime, re, subprocess

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

def Help(command=''):
    if command == '':
        print('For more information on a specific command, type HELP command-name\n')
        print('HELP           Shows a list of commands, and a basic explanation of what they do')
        print('CD             Change working directory')
        print('LS             List current directory')
        print('DIR            List current directory')
        print('CLS            Clear the terminal screen')
        print('CLEAR          Clear the terminal screen')
        print('READ           Dump text file contents to terminal screen')
        print('DUMP           Dump text file contents to terminal screen')
        print('EXIT           Shuts down the program')
        print('QUIT           Shuts down the program')
        print('DIE            Shuts down the program')
        print('END            Shuts down the program')
        print('ABORT          Shuts down the program')
        print('ENDCLI         Shuts down the program')
        print('ABANDON        Shuts down the program')
        print('SYS            Use to configure some system things, be careful!')
        print('SYSTEM         Use to configure some system things, be careful!')

    elif command.upper() == 'HELP':
        print('Shows a list of commands, and a basic explanation of what they do\n')

    elif command.upper() == 'CD':
        print('Change working directory\n')

    elif command.upper() == 'LS':
        print('List current directory\n')

    elif command.upper() == 'DIR':
        print('List current directory\n')

    elif command.upper() == 'CLS':
        print('Clear the terminal screen\n')

    elif command.upper() == 'CLEAR':
        print('Clear the terminal screen\n')

    elif command.upper() == 'READ':
        print('Dump text file contents to terminal screen\n')

    elif command.upper() == 'DUMP':
        print('Dump text file contents to terminal screen\n')

    elif command.upper() == 'EXIT':
        print('Shuts down the program\n')

    elif command.upper() == 'QUIT':
        print('Shuts down the program\n')

    elif command.upper() == 'DIE':
        print('Shuts down the program\n')

    elif command.upper() == 'END':
        print('Shuts down the program\n')

    elif command.upper() == 'ABORT':
        print('Shuts down the program\n')

    elif command.upper() == 'ENDCLI':
        print('Shuts down the program\n')

    elif command.upper() == 'ABANDON':
        print('Shuts down the program\n')

    elif command.upper() == 'SYS':
        print('Use to configure some system things, be careful!\n')
        print('RECURSION      Set the recursion limit, you probaly don\'t need to touch this')

    elif command.upper() == 'SYSTEM':
        print('Use to configure some system things, be careful!\n')
        print('RECURSION      Set the recursion limit, you probaly don\'t need to touch this')

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
                log('No such file or directory!', 3)
        else:
            Help('CD')

    elif usr_in.lower().startswith('ls'):
        if usr_in.lower().startswith('ls '):
            if os.path.exists(os.path.normpath(re.split('ls ', usr_in, 1, flags=re.IGNORECASE)[1])):
                print(os.listdir(os.path.normpath(re.split('ls ', usr_in, 1, flags=re.IGNORECASE)[1])))
            else:
                log('No such file or directory!', 3)
        else:
            print(os.listdir(os.path.normpath(re.split('ls', usr_in, 1, flags=re.IGNORECASE)[1])))

    elif usr_in.lower().startswith('dir'):
        if usr_in.lower().startswith('dir '):
            if os.path.exists(os.path.normpath(re.split('dir ', usr_in, 1, flags=re.IGNORECASE)[1])):
                print(os.listdir(os.path.normpath(re.split('dir ', usr_in, 1, flags=re.IGNORECASE)[1])))
            else:
                log('No file or directory!', 3)
        else:
            print(os.listdir(os.path.normpath(re.split('dir', usr_in, 1, flags=re.IGNORECASE)[1])))

    elif usr_in.lower().startswith('sys'):
        if usr_in.lower().startswith('sys '):
            log('Missing Command!', 4)
        else:
            Help('SYS')
    
    elif usr_in.lower().startswith('system'):
        if usr_in.lower().startswith('system '):
            log('Missing Command!', 4)
        else:
            Help('SYSTEM')

    elif usr_in.lower().startswith('read'):
        if usr_in.lower().startswith('read '):
            if os.path.exists(os.path.normpath(re.split('read ', usr_in, 1, flags=re.IGNORECASE)[1])):
                if os.path.isfile(os.path.normpath(re.split('read ', usr_in, 1, flags=re.IGNORECASE)[1])):
                    file = open(os.path.normpath(re.split('read ', usr_in, 1, flags=re.IGNORECASE)[1]), 'r')
                    print(file.read())
                    file.close()
            else:
                log('No such file or directory!', 3)
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
                log('No such file or directory!', 3)
        else:
            Help('DUMP')
            
    elif usr_in.lower().startswith('clear') or usr_in.lower().startswith('cls'):
        if os.name == 'nt':
            log('Cleared the screen', 1, False)
            subprocess.run("cls")
        else:
            log('Cleared the screen', 1, False)
            subprocess.run("clear")

    elif usr_in.lower().startswith('exit') or usr_in.lower().startswith('quit') or usr_in.lower().startswith('die') or usr_in.lower().startswith('endcli') or usr_in.lower().startswith('end') or usr_in.lower().startswith('abort') or usr_in.lower().startswith('abandon'):
        log('Program exited normally', 1)
        die()

    elif usr_in == '':
        log('User failed to input command!', 3)

    else:
        log('Invalid command!', 3)

    cmd()

print('   _____ _          _ _  \n  / ____| |        | | | \n | (___ | |__   ___| | | \n  \___ \| \'_ \ / _ \ | | \n  ____) | | | |  __/ | | \n |_____/|_| |_|\___|_|_| \n')
print('Welcome to Shell! A command line shell created by Not Mark, because why not!\nNote: The command set is bit of everything.\n')
cmd()
die()