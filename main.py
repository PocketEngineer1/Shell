import os, subprocess, platform
from utils import *
from lib import *

debug_log(config)
debug_log(lang)

def REPLACE(Input):
    y = str(Input)
    for x in UserStorage:
        y = y.replace("<"+x+">", UserStorage[x])
    debug_log(y)
    return y

class commands:
    def Help(command=''):
        Temp = command.upper()

        if Temp == '':
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
            print('WAIT           '+lang['HELP']['USER_INPUT']['main'])
            print('INPUT          '+lang['HELP']['USER_INPUT']['main'])
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

        elif Temp == 'HELP':
            print(lang['HELP']['HELP']['main']+'\n')

        elif Temp == 'CD':
            print(lang['HELP']['CD']['main']+'\n')

        elif Temp == 'LS' or Temp == 'DIR':
            print(lang['HELP']['LIST_DIR']['main']+'\n')

        elif Temp == 'MKDIR':
            print(lang['HELP']['MAKE_DIRECTORY']['main']+'\n')

        elif Temp == 'RMDIR':
            print(lang['HELP']['REMOVE_DIRECTORY']['main']+'\n')

        elif Temp == 'RM':
            print(lang['HELP']['REMOVE_FILE']['main']+'\n')

        elif Temp == 'CLS' or Temp == 'CLEAR':
            print(lang['HELP']['CLEAR']['main']+'\n')

        elif Temp == 'ECHO' or Temp == 'PRINT':
            print(lang['HELP']['PRINT']['main']+'\n')

        elif Temp == 'WAIT' or Temp == 'INPUT':
            print(lang['HELP']['USER_INPUT']['main']+'\n')

        elif Temp == 'READ' or Temp == 'DUMP':
            print(lang['HELP']['READ']['main']+'\n')

        elif Temp == 'HOST':
            print(lang['HELP']['HOST_CMD']['main']+'\n')

        elif Temp == 'INTEG' or Temp == 'PKG':
            print(lang['HELP']['PACKAGE']['main']+'\n')
            print('INSTALL        '+lang['HELP']['PACKAGE']['SUB']['install'])
            print('REMOVE         '+lang['HELP']['PACKAGE']['SUB']['remove'])

        elif Temp == 'EXIT' or Temp == 'QUIT' or Temp == 'DIE' or Temp == 'END' or Temp == 'ABORT' or Temp == 'ENDCLI' or Temp == 'ABANDON':
            print(lang['HELP']['EXIT']['main']+'\n')

        elif Temp == 'SYS' or Temp == 'SYSTEM':
            print(lang['HELP']['SYSTEM']['main']+'\n')
            print('RECURSION      '+lang['HELP']['SYSTEM']['SUB']['recursion'])
    # end of function
# end of class

UserStorage = {
    "APP_DIR": str(os.path.normpath(os.getcwd())),
    "HOME_DIR": str(os.path.normpath(os.path.expanduser('~'))),
    "USER": str(os.getlogin()),
    "HOSTNAME": str(platform.node())
}

def cmd():
    Dir = os.path.normpath(os.getcwd())
    UserStorage['CWD'] = Dir

    usr_in = input(REPLACE(str(config['MAIN']['cmd_txt'])))

    Temp = usr_in.split(' ', 1)
    Temp[0] = Temp[0].lower()
    debug_log(usr_in)
    debug_log(Temp)

    if Temp[0] == 'help':
        if 1 < len(Temp):
            commands.Help(Temp[1])
        else:
            commands.Help()
    
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
            commands.Help(Temp[0])

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
        if EXPERIMENTAL:
            if 1 < len(Temp):
                log(lang['ERROR']['missing_command'], 4)
            else:
                commands.Help(Temp[0])

    elif Temp[0] == 'wait' or Temp[0] == 'input':
        if 1 < len(Temp):
            UserStorage['usr_in'] = input(REPLACE(Temp[1]))
        else:
            UserStorage['usr_in'] = input()

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
            commands.Help(Temp[0])

    elif Temp[0] == 'integ' or Temp[0] == 'pkg':
        if EXPERIMENTAL:
            if 1 < len(Temp):
                log(lang['ERROR']['missing_command'], 4)
            else:
                commands.Help(Temp[0])

    elif Temp[0] == 'echo' or Temp[0] == 'print':
        if 1 < len(Temp):
            print(REPLACE(Temp[1]))
        else:
            print()

    elif Temp[0] == 'host':
        y = REPLACE(Temp[1])
        if EXPERIMENTAL:
            log("It appears that this may not work correctly", 2)
            if 1 < len(Temp):
                log(Temp[1], Print=False)
                subprocess.run(Temp[1])
            else:
                commands.Help(Temp[0])

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
            commands.Help(Temp[0])

    elif Temp[0] == 'rm':
        if 1 < len(Temp):
            y = REPLACE(Temp[1])
            if os.path.exists(os.path.normpath(y)):
                os.remove(os.path.normpath(y))
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            commands.Help(Temp[0])

    elif Temp[0] == 'rmdir':
        if 1 < len(Temp):
            y = REPLACE(Temp[1])
            if os.path.exists(os.path.normpath(y)):
                os.rmdir(os.path.normpath(y))
            else:
                log(lang['ERROR']['invalid_path'], 3)
        else:
            commands.Help(Temp[0])

    elif Temp[0] == 'mkdir':
        if 1 < len(Temp):
            y = REPLACE(Temp[1])
            if os.path.exists(os.path.normpath(y)) == False:
                os.mkdir(os.path.normpath(y))
            else:
                log(lang['ERROR']['existing_path'], 3)
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

print('  _   _       _     __  __            _    _        _____ _          _ _  \n | \ | |     | |   |  \/  |          | |  ( )      / ____| |        | | | \n |  \| | ___ | |_  | \  / | __ _ _ __| | _|/ ___  | (___ | |__   ___| | | \n | . ` |/ _ \| __| | |\/| |/ _` | \'__| |/ / / __|  \___ \| \'_ \ / _ \ | | \n | |\  | (_) | |_  | |  | | (_| | |  |   <  \__ \  ____) | | | |  __/ | | \n |_| \_|\___/ \__| |_|  |_|\__,_|_|  |_|\_\ |___/ |_____/|_| |_|\___|_|_| \n')
print('Welcome to Not Mark\'s Shell! A command line shell created by Not Mark, because why not!\nNote: The command set is bit of everything.\n')
cmd()
die()