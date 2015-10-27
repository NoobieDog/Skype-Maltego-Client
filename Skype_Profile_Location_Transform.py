#!/usr/bin/env python
import sys
import Skype4Py
from MaltegoTransform import *

# Instatinate Skype object, all further actions are done
# using this object.
skype = Skype4Py.Skype()

# Start Skype if it's not already running.
if not skype.Client.IsRunning:
    skype.Client.Start()

# Set our application name.
skype.FriendlyName = 'Skype_Transform'

# Attach to Skype. This may cause Skype to open a confirmation
# dialog.
skype.Attach()

# Set up an event handler.
def new_skype_status(status):
    # If Skype is closed and reopened, it informs us about it
    # so we can reattach.
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()
skype.OnAttachmentStatus = new_skype_status

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
SearchString = mt.getValue()
mt = MaltegoTransform()

user = skype.User(SearchString)
if not user.Country:
	mt.addEntity("maltego.Location","UNKOWN")
else:
	mt.addEntity("maltego.Location",user.Country)

mt.returnOutput()