import os, re, subprocess
from utils import *
from lib import *

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

    Temp = re.split(' ', usr_in, 1)[0]
    Temp = Temp.lower()

    if Temp == 'help':
        if Temp.startswith(Temp+' '):
            commands.Help(re.split(' ', usr_in, 1)[1])
        else:
            commands.Help(Temp)

    elif Temp == 'cd':
        if Temp.startswith(Temp+' '):
            if os.path.exists(os.path.normpath(re.split(' ', usr_in, 1)[1])):
                os.chdir(os.path.normpath(re.split(' ', usr_in, 1)[1]))
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            commands.Help(Temp)

    elif Temp == 'ls' or Temp == 'dir':
        if Temp.startswith(Temp+' '):
            if os.path.exists(os.path.normpath(re.split(' ', usr_in, 1)[1])):
                print(os.listdir(os.path.normpath(re.split('ls ', usr_in, 1, flags=re.IGNORECASE)[1])))
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            print(os.listdir())

    elif Temp == 'sys' or Temp == 'system':
        if Temp.startswith(Temp+' '):
            log(lang['ERROR']['missing_command'], 4)
        else:
            commands.Help(Temp)

    elif Temp == 'integ' or Temp == 'pkg':
        if usr_in.lower().startswith(Temp+' '):
            log(lang['ERROR']['missing_command'], 4)
        else:
            commands.Help(Temp)

    elif Temp == 'host':
        log("It appears that this may not work correctly", 2)
        if usr_in.lower().startswith(Temp+' '):
            log(re.split(Temp+' ', usr_in, 1, flags=re.IGNORECASE)[1], Print=False)
            subprocess.run(re.split(Temp+' ', usr_in, 1, flags=re.IGNORECASE)[1].split(" "))
        else:
            commands.Help(Temp)

    elif Temp == 'read' or Temp == 'dump':
        if usr_in.lower().startswith(Temp+' '):
            if os.path.exists(os.path.normpath(re.split(Temp+' ', usr_in, 1, flags=re.IGNORECASE)[1])):
                if os.path.isfile(os.path.normpath(re.split(Temp+' ', usr_in, 1, flags=re.IGNORECASE)[1])):
                    file = open(os.path.normpath(re.split(Temp+' ', usr_in, 1, flags=re.IGNORECASE)[1]), 'r')
                    print(file.read())
                    file.close()
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            commands.Help(Temp)
            
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

    Temp = None
    usr_in = None

    cmd()
# end of function

print('   _____ _          _ _  \n  / ____| |        | | | \n | (___ | |__   ___| | | \n  \___ \| \'_ \ / _ \ | | \n  ____) | | | |  __/ | | \n |_____/|_| |_|\___|_|_| \n')
print('Welcome to Shell! A command line shell created by Not Mark, because why not!\nNote: The command set is bit of everything.\n')
cmd()
die()