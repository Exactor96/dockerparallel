import _xxsubinterpreters as interpreters
import threading
import textwrap as tw
import pickle

# Create a sub-interpreter
interpid = interpreters.create()

print(interpid)

inter_chanel = interpreters.channel_create()


