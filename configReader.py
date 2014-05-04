# -*- coding: utf-8 -*-

import errors 

class Config:
    """Internal, reads configuration from a file. Use the config object instead."""

    config = {}
    def __init__(self, uri, text=False):
        """read config file from python script ( text=False or from own text file text=True ."""
        self.configFile = uri
        if not text:
          try:
            execfile(self.configFile, {}, self.config)
          except IOError:
            pass
        else :
          self._read() 
        

    def __getitem__(self, name):
        return self.config.get(name, None)

    def __setitem__(self, name, value):
        self.config[name] = value
        self._save()

    def _save(self):
        configStr = ""
        for i in self.config:
            configStr += i+" = "+repr(self.config[i])+"\n"
        with open(self.configFile, 'w') as f:
            f.write(configStr)

    def _read(self):
       """read config file and call parse."""        
       file = self.configFile
       source = open(file, "r")
       lines = source.readlines()
       source.close()
       self.config = self._parse(lines)

    def _parse(self, lines):
       """parse config file."""
       acceptedVars = { "api", "username", "password", "botflag"  }
       statements = {}
       for line in lines:
           code = line.strip()
           if len(code) == 0 : pass #empty line
           elif code[0:1] == '\x23':pass #comment
           else :
              if ( code.find("\x23") > 0 ) : # comment found at end of line
                 code = code[:code.find("\x23")]
              
              equalIndex = code.find("=")
              if equalIndex > 0 : pass
              else : raise errors.ConfigurationError("syntax error in config file in line  : " + line)
              var = code[0:equalIndex].strip()
              value = code[equalIndex+1:].strip()
              if var in acceptedVars: pass
              else : raise errors.ConfigurationError("syntax error in config file : unknown variable " + var + " in line : " + line)
              pythonValue = None
              if value == "None":pythonValue = None
              elif value == "False":pythonValue = False
              elif value == "True": pythonValue = True 
              else : # other case is a string ( we check syntax ) only removing quotes
                  if value[0:1] == '"' : 
                     if value[-1] != '"' :
                        raise errors.ConfigurationError("syntax error in config file : missig quote in line : " + line)
                  else : raise errors.ConfigurationError("syntax error in config file : missig quote in line : " + line)
                  pythonValue = value[1:-1]
              statements[var] = pythonValue

       return statements

if __name__ == "__main__":
    
    config = Config('config.py', True)    
    for var in config.config:
        print var + "=" +  str(config[var])

