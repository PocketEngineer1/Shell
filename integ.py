import toml, importlib.util, os, json, mergedeep, zipfile, shutil, tempfile
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
            'name': integ_config['MAIN']['pkgname'],
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
    functions.log(data.lang['INTEG']['LOAD']['main'].replace('<INT>', str(len(data.INTEG_Storage))), 1)
    del i, integ_config, spec, module, w
  except:
    functions.log(data.lang['INTEG']['LOAD']['fail'], 4)
# end

def install(Integ: str):
  functions.log(data.lang['INTEG']['INSTALL']['installing'], 1)
  for c in data.config['MAIN']['integ_sources']:
    for x in os.listdir(c):
      if zipfile.is_zipfile(c+'/'+x):
        if x.lower().endswith('.integ'):
          with zipfile.ZipFile(c+'/'+x) as f:
            dir = data.Storage['TEMP_DIR']+'/'+x
            f.extractall(dir)
            f.close()
            if os.path.exists(dir+'/integ.toml'):
              temp_conf = toml.decoder.load(dir+'/integ.toml')
              if Integ == temp_conf['MAIN']['pkgname']:
                shutil.copytree(dir, functions.REPLACE('<APP_DIR>/INTEG/'+Integ))
                reload()
  functions.log(data.lang['INTEG']['INSTALL']['installed'], 1)
# end

def remove(Integ: str):
    if Integ in data.INTEG_Storage:
      try:
        functions.log(data.lang['INTEG']['REMOVE']['removing'].replace('<INTEG>', Integ), 1)
        shutil.rmtree(data.INTEG_Storage[Integ]['dir'])
        reload()
        functions.log(data.lang['INTEG']['REMOVE']['removed'].replace('<INTEG>', Integ), 1)
      except:
        functions.log(data.lang['INTEG']['REMOVE']['fail'].replace('<INTEG>', Integ), 3)
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
      functions.log(data.lang['INTEG']['PACKAGE']['packaging'].replace('<INTEG>', Integ), 1)
      with zipfile.ZipFile('./Output/'+Integ+'.integ', 'w') as f:
        for root, dirs, files in os.walk(data.INTEG_Storage[Integ]['dir']):
          for dir in dirs:
            if dir not in data.INTEG_ign['folder']['name'] and dir.startswith(tuple(data.INTEG_ign['folder']['startswith'])) == False and dir.endswith(tuple(data.INTEG_ign['folder']['endswith'])) == False and any([x in dir for x in data.INTEG_ign['folder']['contains']]) == False:
              f.write(os.path.join(root, dir), os.path.join(root, dir).split(data.INTEG_Storage[Integ]['dir'])[1])
          for file in files:
            if file not in data.INTEG_ign['file']['name'] and file.startswith(tuple(data.INTEG_ign['file']['startswith'])) == False and file.endswith(tuple(data.INTEG_ign['file']['endswith'])) == False and any([x in file for x in data.INTEG_ign['file']['contains']]) == False:
              f.write(os.path.join(root, file), os.path.join(root, file).split(data.INTEG_Storage[Integ]['dir'])[1])
        f.close()
      functions.log(data.lang['INTEG']['PACKAGE']['packaged'].replace('<INTEG>', Integ), 1)
    except:
      functions.log(data.lang['INTEG']['PACKAGE']['fail'].replace('<INTEG>', Integ), 3)
  else:
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ), 3)
# end

def reload():
  functions.log(data.lang['INTEG']['RELOAD']['reloading'], 1)
  data.INTEG_Storage = {}
  load()
  functions.log(data.lang['INTEG']['RELOAD']['reloaded'], 1)
# end

def run(Integ: str, Input: list):
  if Integ in data.INTEG_Storage:
    data.INTEG_Storage[Integ]['module'].main(Input)
  else:
    functions.log(data.lang['ERROR']['INTEG']['notfound'].replace('<INTEG>', Integ), 3)
