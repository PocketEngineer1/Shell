import toml, importlib.util, os, json, mergedeep
import data, functions

def load():
  for i in os.listdir(functions.REPLACE('<APP_DIR>')+'/INTEG'):
    if os.path.isdir(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i):
      if os.path.exists(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/integ.toml'):
        integ_config = toml.decoder.load(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/integ.toml')

        spec = importlib.util.spec_from_file_location(i, functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/'+integ_config['MAIN']['script'])
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        data.INTEG_Storage[i] = {
          'config': integ_config,
          'module': module,
          'aliases': integ_config['MAIN']['aliases'],
          'dir': functions.REPLACE('<APP_DIR>')+'/INTEG/'+i,
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
# end