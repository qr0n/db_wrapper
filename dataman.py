import sys
from d12db import db
temp_cache = {}

def uses():
        print("<!----------------------------Initializing Help----------------------------!>")
        print("Classes")
        print("class db = { class help }, { class core }, { class off_site }, { class on_site }\nclass d12 = { class core }, { class config }, { class cache }")
        help_with = input("What class would you like help on?\n>")
        if help_with == "db.help":
          print("[dataman.help] : This class relays information to the end user of this package allowing them to have ready access to the functions, definitions and classes.")
        elif help_with == "db.core":
          print("[dataman.help] : This class deals with internal functions such as `init` and `cdict`")
        elif help_with == "db.off_site":
          print("[dataman.help] : This class deals with the online database by reading, writing and both.")
        elif help_with == "db.on_site":
          print("[dataman.help] : This class deals with the local database by reading, writing and uploading databases to the odb")
        elif help_with == "d12.vars": #implement d12 cache help
          print("[dataman.help] : This class contains vars for the d12 caching protocal, these vars are the session cache which gets initialized before reads and writes take place to the cache and the cache itself which can be used for hands on cache reads and writes.")
        elif help_with == "d12.config":
          print("[dataman.help] : This class deals with the session configuration.")
        elif help_with == "d12.cache":
          print("[dataman.help] : This class deals with the cache itself with functions such as `read(k)` and `write(k, v, to_db)`")
          print("[dataman.help] : where k is key, v is value and to_db determines weather or not the data should be mirrored on the cache and database.")
        
def command_line():
    print("If at any point you get stuck, please press CTRL + C to exit the program")
    for i in sys.argv:
        if i == "--help":
            uses()
        elif i == "--local":
            temp_cache["host"] = "local";
        elif i == "--online":
            temp_cache["host"] = "online";
        elif i == "--name":
            a = input("What name would you like your database to be?\n>")
            temp_cache["name"] = a
            db.core.init(True, {"host" : temp_cache['host'], "name" : temp_cache['name']})
            print(f"database '{temp_cache['name']}' fully configured as {temp_cache['host']}")

while True:
    command_line()
