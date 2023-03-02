import toml, importlib.util, os, json, mergedeep, zipfile
import data, functions

def load():
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
  functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['LOAD']['main'].replace('<INT>', str(len(data.INTEG_Storage))))
  del i, integ_config, spec, module, w
# end

def install():
  ...
# end

def remove():
  ...
# end

def upgrade():
  ...
# end

def package(Integ: str):
  if os.path.exists('Output') == False:
    os.mkdir('Output')
  if Integ in data.INTEG_Storage:
    functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['PACKAGE']['packaging'].replace('<INTEG>', Integ))
    with zipfile.ZipFile('./Output/'+Integ+'.integ', 'w') as f:
      for root, dirs, files in os.walk(data.INTEG_Storage[Integ]['dir']):
        for dir in dirs:
          if dir != '__pycache__':
            f.write(os.path.join(root, dir), os.path.join(root, dir).split(data.INTEG_Storage[Integ]['dir'])[1])
        for file in files:
          if file.endswith('.pyc') == False:
            f.write(os.path.join(root, file), os.path.join(root, file).split(data.INTEG_Storage[Integ]['dir'])[1])
    functions.log(data.lang['COMMAND_OUTPUT']['INTEG']['PACKAGE']['packaged'].replace('<INTEG>', Integ))
  else:
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ))
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
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ))
