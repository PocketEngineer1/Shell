import toml, importlib.util, os, json
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
          'dir': functions.REPLACE('<APP_DIR>')+'/INTEG',
          'lang': {}
        }

        if os.path.exists(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/lang'):
          for w in os.listdir(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/lang'):
            data.INTEG_Storage[i]['lang'][os.path.splitext(w)[0]] = toml.decoder.load(functions.REPLACE('<APP_DIR>')+'/INTEG/'+i+'/lang/'+w)

        if os.path.exists(functions.REPLACE('<APP_DIR>')+'/INTEG/help.json'):
          data.INTEG_Storage[i]['help'] = json.loads(functions.REPLACE('<APP_DIR>')+'/INTEG/help.json')

  if data.config['MAIN']['lang'] in data.INTEG_Storage[i]['lang']:
    data.lang.update(data.INTEG_Storage[i]['lang'][data.config['MAIN']['lang']])
# end
