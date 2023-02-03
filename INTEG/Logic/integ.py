from main import *

def main(input: list):
  if input[0] == 'logic':
    if 1 < len(input):
      TemP = input[1].split(' ', 1)
      if 1 < len(TemP):
        if TemP[0].lower() == 'if':
          temp = TemP[1].split(' ', 2)
          if 2 < len(temp):
            debug_log(temp)
            temp[0] = REPLACE(temp[0])
            temp[1] = REPLACE(temp[1])
            temp[2] = REPLACE(temp[2])
            debug_log(temp)
            if temp[0] == temp[1]:
              cmd(temp[2])
        else:
          log(lang['ERROR']['missing_arguement'], 3)
      else:
        commands.Help([input[0], TemP[0]])
    else:
      commands.Help([input[0]])