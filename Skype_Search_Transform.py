#!/usr/bin/env python
'''
Created: 8/10/2015
Updated: 8/10/2015
This script contains the most comprehensive list of Skype Maltego transforms.
Copyright (c) 2015, SensePost.
All rights reserved.
'''
import sys
import Skype4Py
from MaltegoTransform import *

skype = Skype4Py.Skype()

if not skype.Client.IsRunning:
    skype.Client.Start()

skype.FriendlyName = 'Skype_Transform'

skype.Attach()

def new_skype_status(status):
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()
skype.OnAttachmentStatus = new_skype_status

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
SearchString = mt.getValue()
mt = MaltegoTransform()

for user in skype.SearchForUsers(SearchString):
	NewEnt = mt.addEntity('maltego.Person', user.Handle)
	NewEnt.addAdditionalFields('Full Name', 'Full Name', 'nostrict', user.FullName.encode('utf-8'))
	NewEnt.addAdditionalFields('Sex', 'Sex', 'nostrict', user.Sex.encode('utf-8'))
	NewEnt.addAdditionalFields('Online Status', 'Online Status', 'nostrict', user.OnlineStatus.encode('utf-8'))
	NewEnt.addAdditionalFields('MoodText', 'MoodText', 'nostrict', user.MoodText.encode('utf-8'))
	NewEnt.addAdditionalFields('About', 'About', 'nostrict',user.About.encode('utf-8'))
	NewEnt.addAdditionalFields('City', 'City', 'nostrict', user.City.encode('utf-8'))
	NewEnt.addAdditionalFields('Province', 'Province', 'nostrict', user.Province.encode('utf-8'))
	NewEnt.addAdditionalFields('Homepage', 'Homepage', 'nostrict', user.Homepage.encode('utf-8'))
	NewEnt.addAdditionalFields('Phone Home', 'Phone Home', 'nostrict', user.PhoneHome.encode('utf-8'))
	NewEnt.addAdditionalFields('Phone Mobile', 'Phone Mobile', 'nostrict', user.PhoneMobile.encode('utf-8'))
	NewEnt.addAdditionalFields('Phone Office', 'Phone Office', 'nostrict', user.PhoneOffice.encode('utf-8'))
	NewEnt.addAdditionalFields('Language', 'Language', 'nostrict', user.Language.encode('utf-8'))
mt.returnOutput()
