import os, subprocess
from utils import *
from lib import *

DEBUG = True
DEBUG_LOG = True

def debug_log(message):
    now = datetime.datetime.now()
    logFile.write('['+now.strftime("%H:%M:%S")+'] DEBUG: '+str(message)+'\n')
    print('['+now.strftime("%H:%M:%S")+'] DEBUG: '+str(message)+'\n')

class commands:
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
    # end of function
# end of class

def cmd():
    Dir = os.path.normpath(os.getcwd())
    usr_in = input(Dir+'>')

    Temp = usr_in.split(' ', 1)
    if DEBUG:
        print(usr_in)
        print(Temp)
        if DEBUG_LOG:
            debug_log(usr_in)
            debug_log(Temp)


    if Temp[0] == 'help':
        if 1 < len(Temp):
            if DEBUG:
                print('Uses arguements')
                if DEBUG_LOG:
                    debug_log('Uses arguements')
            commands.Help(Temp[1])
        else:
            if DEBUG:
                print('Does not use arguements')
                if DEBUG_LOG:
                    debug_log('Uses arguements')
            commands.Help()

    elif Temp[0] == 'cd':
        if 1 < len(Temp):
            if os.path.exists(os.path.normpath(Temp[1])):
                os.chdir(os.path.normpath(Temp[1]))
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            commands.Help(Temp[0])

    elif Temp[0] == 'ls' or Temp[0] == 'dir':
        if 1 < len(Temp):
            if os.path.exists(os.path.normpath(Temp[1])):
                print(os.listdir(os.path.normpath(Temp[1])))
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            print(os.listdir())

    elif Temp[0] == 'sys' or Temp[0] == 'system':
        if 1 < len(Temp):
            log(lang['ERROR']['missing_command'], 4)
        else:
            commands.Help(Temp[0])

    elif Temp[0] == 'integ' or Temp [0]== 'pkg':
        if 1 < len(Temp):
            log(lang['ERROR']['missing_command'], 4)
        else:
            commands.Help(Temp[0])

    elif Temp[0] == 'host':
        log("It appears that this may not work correctly", 2)
        if 1 < len(Temp):
            log(Temp[1], Print=False)
            subprocess.run(Temp[1])
        else:
            commands.Help(Temp[0])

    elif Temp[0] == 'read' or Temp[0] == 'dump':
        if 1 < len(Temp):
            if os.path.exists(os.path.normpath(Temp[1])):
                if os.path.isfile(os.path.normpath(Temp[1])):
                    file = open(os.path.normpath(Temp[1]), 'r')
                    print(file.read())
                    file.close()
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            commands.Help(Temp[0])
            
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

    elif usr_in == '':
        log(lang['ERROR']['no_command_inputted'], 3)

    else:
        log(lang['ERROR']['unknown_command'], 3)

    cmd()
# end of function

print('   _____ _          _ _  \n  / ____| |        | | | \n | (___ | |__   ___| | | \n  \___ \| \'_ \ / _ \ | | \n  ____) | | | |  __/ | | \n |_____/|_| |_|\___|_|_| \n')
print('Welcome to Shell! A command line shell created by Not Mark, because why not!\nNote: The command set is bit of everything.\n')
cmd()
die()