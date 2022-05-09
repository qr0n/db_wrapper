from d12db import *

cache = d12.cache
d12.config.init({"pass_through" : True, "partition_db" : False})

def catch():
    a = input()
    if a.endswith("--save"):
        return cache.write(k="input", v=a, to_db=True)
    else: 
        return cache.write(k="input", v=a, to_db=False)

def ret():
    return cache.read(k="input")

def ret_db():
    print(db.on_site.index("input"))

catch()
catch()
print(ret())
print(ret_db())