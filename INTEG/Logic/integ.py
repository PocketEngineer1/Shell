import data, functions

def integ(input: list):
  if input[0] == 'logic':
    if 1 < len(input):
      TemP = input[1].split(' ', 1)
      if 1 < len(TemP):
        if TemP[0].lower() == 'if':
          temp = TemP[1].split(' ', 2)
          if 2 < len(temp):
            temp[0] = functions.REPLACE(temp[0])
            temp[1] = functions.REPLACE(temp[1])
            temp[2] = functions.REPLACE(temp[2])
            if temp[0] == temp[1]:
              functions.cmd(temp[2])
        else:
          functions.log(data.lang['ERROR']['missing_arguement'], 3)
      else:
        functions.commands.Help.Main([input[0], TemP[0]])
    else:
      functions.commands.Help.Main([input[0]])