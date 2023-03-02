import toml, importlib.util, os, json, mergedeep, zipfile, shutil
import data, functions

def load():
  try:
    for i in os.listdir(functions.REPLACE('<APP_DIR>')+'/INTEG'):
      if os.path.isdir(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i):
        if os.path.exists(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/integ.toml'):
          integ_config = toml.decoder.load(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/integ.toml')

          spec = importlib.util.spec_from_file_location(i, functions.REPLACE('<APP_DIR>/INTEG/'+i+'/'+integ_config['MAIN']['script']))
          module = importlib.util.module_from_spec(spec)
          spec.loader.exec_module(module)

          data.INTEG_Storage[i] = {
            'config': integ_config,
            'module': module,
            'version': integ_config['MAIN']['version'],
            'depends': integ_config['MAIN']['depends'],
            'aliases': integ_config['MAIN']['aliases'],
            'dir': functions.REPLACE('<APP_DIR>/INTEG/'+i),
            'lang': {},
            'help': {}
          }

          if os.path.exists(data.INTEG_Storage[i]['dir']+'/help.json'):
            with open(data.INTEG_Storage[i]['dir']+'/help.json', 'r') as JsonFile:
              data.INTEG_Storage[i]['help'] = json.loads(JsonFile.read())
            
          if os.path.exists(data.INTEG_Storage[i]['dir']+'/lang'):
            for w in os.listdir(data.INTEG_Storage[i]['dir']+'/lang'):
              data.INTEG_Storage[i]['lang'][w.split('.toml')[0]] = toml.decoder.load(data.INTEG_Storage[i]['dir']+'/lang/'+w)

          if data.config['MAIN']['lang'] in data.INTEG_Storage[i]['lang']:
            mergedeep.merge(data.lang, data.INTEG_Storage[i]['lang'][data.config['MAIN']['lang']])

          module.init()
    functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['LOAD']['main'].replace('<INT>', str(len(data.INTEG_Storage))), 1)
    del i, integ_config, spec, module, w
  except:
    functions.log(data.lang['ERROR']['INTEG']['FAIL']['load'], 4)
# end

def install():
  ...
# end

def remove(Integ: str):
    if Integ in data.INTEG_Storage:
      try:
        functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['REMOVE']['removing'].replace('<INTEG>', Integ), 1)
        shutil.rmtree(data.INTEG_Storage[Integ]['dir'])
        functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['REMOVE']['removed'].replace('<INTEG>', Integ), 1)
      except:
        functions.log(data.lang['ERROR']['INTEG']['FAIL']['remove'].replace('<INTEG>', Integ), 3)
    else:
      functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ), 3)
# end

def upgrade(Integ: str):
  if Integ in data.INTEG_Storage:
    ...
  else:
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ), 3)
# end

def package(Integ: str):
  try:
    if os.path.exists('Output') == False:
      os.mkdir('Output')
  except:
    functions.log(data.lang['ERROR']['FAIL']['create_dir'])
    return
  
  if Integ in data.INTEG_Storage:
    try:
      functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['PACKAGE']['packaging'].replace('<INTEG>', Integ), 1)
      with zipfile.ZipFile('./Output/'+Integ+'.integ', 'w') as f:
        for root, dirs, files in os.walk(data.INTEG_Storage[Integ]['dir']):
          for dir in dirs:
            if dir != '__pycache__':
              f.write(os.path.join(root, dir), os.path.join(root, dir).split(data.INTEG_Storage[Integ]['dir'])[1])
          for file in files:
            if file.endswith('.pyc') == False:
              f.write(os.path.join(root, file), os.path.join(root, file).split(data.INTEG_Storage[Integ]['dir'])[1])
      functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['PACKAGE']['packaged'].replace('<INTEG>', Integ), 1)
    except:
      functions.log(data.lang['ERROR']['INTEG']['FAIL']['package'].replace('<INTEG>', Integ), 3)
  else:
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ), 3)
# end

def reload():
  functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['RELOAD']['reloading'], 1)
  data.INTEG_Storage = {}
  load()
  functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['RELOAD']['reloaded'], 1)
# end

def run(Integ: str, Input: list):
  if Integ in data.INTEG_Storage:
    data.INTEG_Storage[Integ]['module'].main(Input)
  else:
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ), 3)
