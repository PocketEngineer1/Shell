import os
import data, functions

def Help(Input: list):
  if 0 < len(Input):
    Input[0] = Input[0].upper()

    for i in data.INTEG_Storage:
      for g in data.INTEG_Storage[i]['help']:
        if Input[0] == g:
          Temp = data.INTEG_Storage[i]['help'][g][0].split('.')
          Tmp = 'data.lang'
          for k in Temp:
            Tmp += '[\''+k+'\']'
          exec('print('+Tmp+')')
          del Temp, Tmp

  #   if Input[0] == 'HELP':
  #     print(data.lang['HELP']['HELP']['main']+'\n')

  #   elif Input[0] == 'CD':
  #     print(data.lang['HELP']['CD']['main']+'\n')

  #   elif Input[0] == 'LS' or Input[0] == 'DIR':
  #     print(data.lang['HELP']['LIST_DIR']['main']+'\n')

  #   elif Input[0] == 'RMDIR':
  #     print(data.lang['HELP']['REMOVE_DIRECTORY']['main']+'\n')

  #   elif Input[0] == 'MKDIR':
  #     print(data.lang['HELP']['MAKE_DIRECTORY']['main']+'\n')

  #   elif Input[0] == 'RM':
  #     print(data.lang['HELP']['REMOVE_FILE']['main']+'\n')

  #   elif Input[0] == 'CLS' or Input[0] == 'CLEAR':
  #     print(data.lang['HELP']['CLEAR']['main']+'\n')

  #   elif Input[0] == 'PRINT' or Input[0] == 'ECHO':
  #     print(data.lang['HELP']['PRINT']['main']+'\n')

  #   elif Input[0] == 'REFERENCE' or Input[0] == 'INCLUDE':
  #     print(data.lang['HELP']['REFERENCE_SCRIPT']['main']+'\n')

  #   elif Input[0] == 'WAIT' or Input[0] == 'INPUT':
  #     print(data.lang['HELP']['USER_INPUT']['main']+'\n')

  #   elif Input[0] == 'READ' or Input[0] == 'DUMP':
  #     print(data.lang['HELP']['READ']['main']+'\n')

  #   elif Input[0] == 'LOGIC':
  #     if 1 < len(Input):
  #       Input[1] = Input[1].upper()
  #       if Input[1] == 'IF':
  #         print(data.lang['HELP']['LOGIC']['if']+'\n')
  #     else:
  #       print(data.lang['HELP']['LOGIC']['main']+'\n')

  #   elif Input[0] == 'HOST':
  #     print(data.lang['HELP']['HOST_CMD']['main']+'\n')

  #   elif Input[0] == 'INTEG' or Input[0] == 'PKG':
  #     if 1 < len(Input):
  #       Input[1] = Input[1].upper()
  #       if Input[1] == 'INSTALL':
  #         print(data.lang['HELP']['PACKAGE']['install']+'\n')
  #       elif Input[1] == 'REMOVE':
  #         print(data.lang['HELP']['PACKAGE']['remove']+'\n')
  #     else:
  #       print(data.lang['HELP']['PACKAGE']['main']+'\n')
  
  #   elif Input[0] == 'EXIT' or Input[0] == 'QUIT' or Input[0] == 'DIE' or Input[0] == 'END' or Input[0] == 'ABORT' or Input[0] == 'ENDCLI' or Input[0] == 'ABANDON':
  #     print(data.lang['HELP']['EXIT']['main']+'\n')

  #   elif Input[0] == 'SYS' or Input[0] == 'SYSTEM':
  #     if 1 < len(Input):
  #       Input[1] = Input[1].upper()
  #       if Input[1] == 'RECURSION':
  #         print(data.lang['HELP']['SYSTEM']['recursion']+'\n')
  #     else:
  #       print(data.lang['HELP']['SYSTEM']['main']+'\n')

  # else:
  #   print(data.lang['HELP']['more_info']+'\n')
  #   print('HELP           '+data.lang['HELP']['HELP']['main'])
  #   print('CD             '+data.lang['HELP']['CD']['main'])
  #   print('LS             '+data.lang['HELP']['LIST_DIR']['main'])
  #   print('DIR            '+data.lang['HELP']['LIST_DIR']['main'])
  #   print('RMDIR          '+data.lang['HELP']['REMOVE_DIRECTORY']['main'])
  #   print('MKDIR          '+data.lang['HELP']['MAKE_DIRECTORY']['main'])
  #   print('RM             '+data.lang['HELP']['REMOVE_FILE']['main'])
  #   print('CLS            '+data.lang['HELP']['CLEAR']['main'])
  #   print('CLEAR          '+data.lang['HELP']['CLEAR']['main'])
  #   print('ECHO           '+data.lang['HELP']['PRINT']['main'])
  #   print('PRINT          '+data.lang['HELP']['PRINT']['main'])
  #   print('REFERENCE      '+data.lang['HELP']['REFERENCE_SCRIPT']['main'])
  #   print('INCLUDE        '+data.lang['HELP']['REFERENCE_SCRIPT']['main'])
  #   print('WAIT           '+data.lang['HELP']['USER_INPUT']['main'])
  #   print('INPUT          '+data.lang['HELP']['USER_INPUT']['main'])
  #   print('READ           '+data.lang['HELP']['READ']['main'])
  #   print('DUMP           '+data.lang['HELP']['READ']['main'])
  #   print('LOGIC          '+data.lang['HELP']['LOGIC']['main'])
  #   print('HOST           '+data.lang['HELP']['HOST_CMD']['main'])
  #   print('INTEG          '+data.lang['HELP']['PACKAGE']['main'])
  #   print('PKG            '+data.lang['HELP']['PACKAGE']['main'])
  #   print('EXIT           '+data.lang['HELP']['EXIT']['main'])
  #   print('QUIT           '+data.lang['HELP']['EXIT']['main'])
  #   print('DIE            '+data.lang['HELP']['EXIT']['main'])
  #   print('END            '+data.lang['HELP']['EXIT']['main'])
  #   print('ABORT          '+data.lang['HELP']['EXIT']['main'])
  #   print('ENDCLI         '+data.lang['HELP']['EXIT']['main'])
  #   print('ABANDON        '+data.lang['HELP']['EXIT']['main'])
  #   print('SYS            '+data.lang['HELP']['SYSTEM']['main'])
  #   print('SYSTEM         '+data.lang['HELP']['SYSTEM']['main'])

def Reference(ScriptPath: str):
  if os.path.exists(ScriptPath):
    with open(ScriptPath) as script:
      for line in script:
        functions.cmd(line)
