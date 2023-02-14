import os, configparser, datetime, toml
import data, functions

class Handler:
  def Config():
    if (os.path.exists("config.ini")):
      config = configparser.ConfigParser()
      config.sections()
      config.read('config.ini')
    else:
      functions.log('No config file found!', 2)
      functions.log('Writing config file...', 1)
      file = open("config.ini", "a")
      file.write("[MAIN]\n")
      file.write("cmd_txt=<CWD>>\n")
      file.write("lang=en_US\n\n")
      file.close()
      config = configparser.ConfigParser()
      config.sections()
      config.read('config.ini')
      functions.log('Wrote new config file!', 1)
    return config
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
