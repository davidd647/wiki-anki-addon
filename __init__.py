# Developed by d2dev_
# 2019-03-27
# License: Iunno - use this stuff however you want, if you'd like!

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki.hooks import addHook

from .wikipedia import *
from .exceptions import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()
    # show a message box
    showInfo("Card count: %d" % cardCount)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)


#####

def onFocusLost(flag, note, fidx):
  # flag: flag, n: note, fidx: current field
  src = None
  dst = None
  # showInfo("n: %s" % n)         # <anki.notes.Note object at 0x11a686eb8>
  # showInfo("fidx: %s" % fidx)   # 1
  # showInfo("flag: %s" % flag)   # false
  # has src and dst fields?

  # enumerate assigns an index to c, and a value to name
  for index, name in enumerate(mw.col.models.fieldNames(note.model())):
    # showInfo("c: %s" % c)       # 0, 1, 2... maybe it's the index
    # showInfo("name: %s" % name) # Front, Back Wiki
    if "Back" == name:
      src = "Back"
      srcIndex = index
    if "Wiki" == name:
      dst = "Wiki"
  if not src or not dst:
    return flag
  # event coming from src field?
  if fidx != srcIndex:
    return flag
  # grab source text
  srcTxt = mw.col.media.strip(note[src])
  if not srcTxt:
    return flag
  # update field
  # try:
    # put the same text into the distribution field...

  wikipedia.set_lang("en") # can also be fr, en, jp
  
  
  query = wikipedia.summary(srcTxt, sentences=2)
  # responseType = type(query)
  # if (responseType != "str"):
    # query = "Search resulted in non-string value: " + responseType

  note[dst] = query
  
  # Need to return True, otherwise it doesn't work!
  return True

addHook('editFocusLost', onFocusLost)
