import os
import data, functions

class Help:
  TeMp = 0

  def Main(Input: list):
    if 0 < len(Input):
      Input[0] = Input[0].upper()
      for i in data.INTEG_Storage:
        for g in data.INTEG_Storage[i]['help']:
          if Input[0] == g:
            if 1 < len(Input):
              Input[1] = Input[1].upper()
              for y in data.INTEG_Storage[i]['help'][g][1]:
                if Input[1] == y:
                  Temp = data.INTEG_Storage[i]['help'][g][1][y][0].split('.')
                  Tmp = 'data.lang'
                  for k in Temp:
                    Tmp += '[\''+k+'\']'
                  exec('print('+Tmp+')')
                  del Temp, Tmp    
            else:
              Temp = data.INTEG_Storage[i]['help'][g][0].split('.')
              Tmp = 'data.lang'
              for k in Temp:
                Tmp += '[\''+k+'\']'
              exec('print('+Tmp+')')
              del Temp, Tmp
    
    else:
      for i in data.INTEG_Storage:
        for g in data.INTEG_Storage[i]['help']:
          Temp = data.INTEG_Storage[i]['help'][g][0].split('.')
          Tmp = 'data.lang'
          for k in Temp:
            Tmp += '[\''+k+'\']'
          exec('print('+Tmp+')')
          del Temp, Tmp

def Reference(ScriptPath: str):
  if os.path.exists(ScriptPath):
    with open(ScriptPath) as script:
      for line in script:
        functions.cmd(line)
