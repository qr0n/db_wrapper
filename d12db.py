import httpx
import json

#Imports#

#Starting odb - VARS

url = "https://db.infinityiron.xyz/api/ron@2000"
pull_pack = "https://db.infinityiron.xyz/"

#odb : class

class odb:
  @staticmethod
  def store(k, v, f):
    """Takes argument(s) k, v, f and applies them in the url"""
    r = httpx.get(f"{url}/store?key={k}&value={v}&file={f}")
    return r.text

  @staticmethod
  def delete(k, f):
    """Takes argument(s) k, f and applies them in the url"""
    r = httpx.get(f"{url}/del?key={k}&file={f}")
    return r.text

  @staticmethod
  def delete_db(f):
    """Takes argument(s) f and applies them in the url"""
    r = httpx.get(f"{url}/delete_db?file={f}")
    return r.text
  
  @staticmethod
  def create_db(f):
    """Takes argument(s) f and applies them in the url"""
    r = httpx.get(f"{url}/create_db?file={f}")
    return r.text
  
  @staticmethod
  def render(f):
    """Takes argument(s) f and applies them in the url"""
    r = httpx.get(f"{url}/list?file={f}")
    return r.text

  @staticmethod
  def key_focus(k, f):
    """Takes argument(s) k, f and applies them in the url"""
    r = httpx.get(f"{url}/get?key={k}&file={f}")
    return r.text
  
  @staticmethod
  def pull(package):
    r = httpx.get(f"{pull_pack}/packages?p={package}").text
    with open(f"packages/{package}.py", "w") as E:
      E.write(r.text)
      return print(f"{package} has been added successfully!")

class ldb:
    @staticmethod
    def read(f):
        """Takes argument(s) f and returns read file"""
        with open(f"{f}.json", "r") as E:
            return E.read()

    @staticmethod
    def save(k, v, f):
        "Takes argument(s) k, v, f to save a key(k) to a value(v) in a file(f)"
        with open(f, "r") as E:
            lE = json.load(E)
        lE[k] = v
        with open(f, "w") as E:
            json.dump(lE, E)

    @staticmethod
    def key_focus(k, f):
        """Takes argument(s) k, f and indexes the dict to those values, returns 'Item Not Found' if the value isnt present"""
        try:
            return ldb.read(f)[k]
        except KeyError:
            return "Item not found"

    @staticmethod
    def upload(f):
        """:::Unstable:::\nUploads a file(f) with > or  = 100 entries"""
        with open(f, "r") as E:
            lE = json.load(E)
            if len(lE) > 100:
                print("Database too large, exiting")
                exit()
            else:
                print("*DISCLAIMER* : uploading a database may result in dataloss. and heavy modification to restore it to a workable copy.")
                odb.create_db(f="UpLoadedDB")
                for i in lE:
                    odb.store(k=i, v=lE[i], f="UpLoadedDB")
                print("This may take a while.")
                return
    
    @staticmethod
    def delete(k, f):
        """Takes argument(s) k, f to index and delete a key"""
        with open(f"{f}.json", "r") as E:
            lE = E.load()
            del lE[k]
        with open(f"{f}.json", "w") as E:
            json.dump(lE, E)

class vars:
    copy_cfg = {}

def config():
  with open("hrdcfg.json", "r") as E:
    lE = json.load(E)
    return lE

cfg = config()

class db:
    class help:
      def uses():
        print("<!----------------------------Initializing Help----------------------------!>")
        print("Classes")
        print("class db = { class help }, { class core }, { class off_site }, { class on_site }\n class d12 ={ class core }, { class config }, { class cache }")
        help_with = input("What class would you like help on?\n")
        if help_with == "db.help":
          print("This class relays information to the end user of this package allowing them to have ready access to the functions, definitions and classes.")
        elif help_with == "db.core":
          print("This class deals with internal functions such as `init` and `cdict`")
        elif help_with == "db.off_site":
          print("This class deals with the online database by reading, writing and both.")
        elif help_with == "db.on_site":
          print("This class deals with the local database by reading, writing and uploading databases to the odb")
        elif help_with == "d12.vars": #implement d12 cache help
          print("This class contains vars for the d12 caching protocal, these vars are the session cache which gets initialized before reads and writes take place to the cache and the cache itself which can be used for hands on cache reads and writes.")
        elif help_with == "d12.config":
          print("This class deals with the session configuration.")
        elif help_with == "d12.cache":
          print("This class deals with the cache itself with functions such as `read(k)` and `write(k, v, to_db)`")
          print("where k is key, v is value and to_db determines weather or not the data should be mirrored on the cache and database.")
    
    class core:
      def cdict(copy_from: dict, copy_to, store : bool):
        if store == False:
          copy_from['<!__Cache__!>'] = "<!__RanChar__!>"

          for i in copy_from:
            copy_to[i] = copy_from[i]

          del copy_from["<!__Cache__!>"]
          del copy_to["<!__Cache__!>"]

          return copy_to

        elif store == True:
          copy_from["<!__Cache__!>"] = "<!__RanChar__!>"

          with open(f"{copy_to}.json", "w") as E:
              E.write("{\n\n}")

          with open(f"{copy_to}.json", "r") as E:
            lE = json.load(E)
            #del lE["<!__Cache__!>"]

            for i in copy_from:
              lE[i] = copy_from[i]
              copy_to[i] = copy_from[i]
          
            del copy_from["<!__Cache__!>"]
            #del copy_to["<!__Cache__!>"]

          with open(f"hrdcfg.json", "w") as E:
            json.dump(lE, E)

          return copy_to

      @staticmethod
      def init(custom_congfig : bool, config : dict, name=None):
        if custom_congfig == True:
          db.core.cdict(config, vars.copy_cfg, store=True)
          if config['host'] == "local":
              with open(f"{config['name']}.json", "w") as E:
                  E.write("{}")
                  E.close()

                  print(config['name'], "has been configured to run locally.")
          elif config['host'] == "online":
              print("Your database files are now hosted online.")
              odb.create_db(f=config["name"])
        else:
          db.core.cdict({"host" : "local", "name" : name}, vars.copy_cfg)
          with open(name, "w") as E:
            E.write("{}")
            E.close()
            print(f"No config was provided, one was generated\n")
            

    class off_site:
      
      def check():
        try:
          with open("hrdcfg.json", "r") as E:
            lE = json.load(E)
            if lE['host'] == "online":
              return "IsOffSite"
            else:
              print("**ERROR** onsite config is being treated as offsite. **ERROR**")
              exit()
        except KeyError:
          return "NotOffSite"

      @staticmethod
      def download():
        if db.off_site.check() == "IsOffSite":
          with open(f"{cfg['name']}.json", "w") as E:
            E.write(odb.render(f=cfg['name']))
            print("Local backup created.")
        else:
          print("*ERROR* local config as online. Exiting")
          exit()

      @staticmethod
      def index(key):
        if db.off_site.check() == "IsOffSite":
          return odb.key_focus(k=key, f=cfg['name'])
        else:
          print("*ERROR*, local config as online. Exiting")
          exit()

      @staticmethod
      def save(key, val):
        if db.off_site.check() == "IsOffSite":
          return odb.store(k=key, v=val, f=cfg['name'])
        else:
          print("*ERROR*, local config as online. Exiting")
          exit()
      
      @staticmethod
      def delete(key):
        if db.off_site.check() == "IsOffSite":
          return odb.delete(k=key, file=cfg['name'])
        else:
          print("*ERROR*, local config as online. Exiting")
          exit()

    class on_site:
      def check():
        try:
          with open("hrdcfg.json", "r") as E:
            lE = json.load(E)
            if lE['host'] == "local":
              return "IsLocal"
            else:
              print("**ERROR** offsite config is being treated as onsite. **ERROR**")
              exit()
        except KeyError:
          return "NotLocal"

      @staticmethod
      def upload():
        if db.on_site.check() == "IsLocal":
          ldb.upload(f=f"{cfg['name']}.json")
        else:
          exit()

      @staticmethod
      def index(key):
        if db.on_site.check() == "IsLocal":
          with open(f"{cfg['name']}.json", "r") as E:
            lE = json.load(E)
            try:
              return lE[key]
            except KeyError:
              return 404
        else:
          exit()

      @staticmethod
      def save(key, val):
          if db.on_site.check() == "IsLocal":
              return ldb.save(k=key, v=val, f=f"{cfg['name']}.json")
          else:
              exit()

      @staticmethod
      def delete(key):
          if db.on_site.check() == "IsLocal":
            return ldb.delete(k=key, f=cfg["name"])

      @staticmethod
      def load():
          if db.on_site.check() == "IsLocal":
              return ldb.read(f=cfg['name'])
          else:
              exit()             

#mapping {"renew_keys" : bool, "env" : online/local, "name" : str}

class d12:
  class vars:
    cache = {}
    X_config = {}
  
  class config:
    @staticmethod
    def init(config):
      """example config : {'pass_through' : bool, 'partition_db' : bool}"""
      db.core.cdict(config, d12.vars.X_config, store=False)
      print('[Config] Configuation saved')

  class cache:
    @staticmethod
    def read(k):
      if d12.vars.X_config['partition_db'] == True:
        try:
          return d12.vars.cache[k]
        except KeyError:
          if d12.vars.X_config['pass_through'] == True and config()["host"] == "online":
            return db.off_site.index(k)
          elif d12.vars.X_config['pass_through'] == True and config()["host"] == "local":
            return db.on_site.index(k)
          elif d12.vars.X_config['pass_through'] == False:
            print(f"[d12.cache.read] [{k}]: Key not found, pass_through not enabled")
            return 404

    @staticmethod
    def write(k, v, to_db : bool):
      d12.vars.cache[k] = v
      if to_db == False:
        return
      elif to_db == True:
        if d12.vars.X_config['pass_through'] == True and config()["host"] == "online":
          db.off_site.save(k, v)
        elif d12.vars.X_config['pass_through'] == True and config()["host"] == "local":
          db.on_site.save(k, v)
        return