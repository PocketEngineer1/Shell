import os, datetime, toml
import data, functions

class Handler:
  def Config():
    try:
      if (os.path.exists("config.toml")):
        config = toml.decoder.load('./config.toml')
      else:
        functions.log('No config file found!', 2)
        functions.log('Writing config file...', 1)
        file = open("config.toml", "a")
        file.write("[MAIN]\n")
        file.write("cmd_txt='<CWD>>'\n")
        file.write("lang=\"en_US\"\n")
        file.write("integ_sources=[\""+os.path.expanduser('~')+"/Downloads\"]\n")
        file.close()
        config = toml.decoder.load('./config.toml')
        functions.log('Wrote new config file!', 1)
      return config
    except:
      functions.log('An issue ocurred while handling the config file!', 4)
  # end

  def Lang():
    if os.path.exists('./lang/'+data.config['MAIN']['lang']+'.toml'):
      lang = toml.decoder.load('./lang/'+data.config['MAIN']['lang']+'.toml')
    else:
      raise FileExistsError('Failed to locate language file')
    return lang
  # end

  def Log():
    now = datetime.datetime.now()
    if os.path.exists('log/'):
      logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
    else:
      os.mkdir('log')
      logFile = open("log/"+now.strftime("%Y %m %d %H %M %S")+".log", "a")
    return logFile
  # end
