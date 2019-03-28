from .wikipedia import *
from .exceptions import *

print(type({}))
print(type([]))
wikipedia.set_lang("en") # can also be fr, en, jp
# query = 
wikipedia.summary("Test", sentences=3)
# print(query)
# print(type(query))