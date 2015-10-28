Skype Maltego Transforms
=======
@author: Stuart Kennedy
@company: Sensepost  

1. Scope
-
This document describes each Maltego transform designed to use the Skype4py API. Also included are instructions to set up Python 2.7.x and the required librarys, which are prerequisites to using the Maltego transforms. The Maltego transforms are able to run on any platform that runs Maltego and Python. 
<br>
2. Prerequisites: Python + Skype4py Library
-
In order to use the Skype Maltego transforms, you must first install Python 2.7.x. If not already installed, please visit the following page for downloads and installation documentation:<br>

[https://www.python.org/downloads/](https://www.python.org/downloads/)  
Python 2.7.x License: [https://docs.python.org/2/license.html](https://docs.python.org/2/license.html)<br>

Once Python is installed, install the Skype4Py library. These transforms have been created and tested successfully with the latest version. Please visit the following page for installation instructions:

[https://github.com/awahlig/skype4py](https://github.com/awahlig/skype4py)

<b>pip install skype4py</b>
-
<b>Note: You will need to have Skype running and logged into for the transforms to work. </b>

Tested on Ubuntu with Skype 4.3.0.37 ([Latest available version](http://www.skype.com/en/download-skype/skype-for-linux/))
-
3. Transforms
-
You will need to add the transforms as "Local" Transforms for now until we add them to the Sensepost TDS

To use the transforms, use a "Phrase to search for users", any Skype accounts found will be "People" entities.

The following transforms have been created for the Skype transform set: 
 
1. **Skype Phrase Search**  - A transform that will return Skype users with the phrase used.  
	
	Required Maltego entity input: Phrase  
	Maltego entity output: Person

2. **Skype GetIP from Username** - A transform that will return a IPv4 addresses (If ONLINE) to a known/valid Skype username. 

	Required Maltego entity input: Person  
	Maltego entity output: IPv4 Address

3. **Skype Profile Location** - A transform that will return the location entitiy of a selected skype profile.  

	Required Maltego entity input: Person  
	Maltego entity output: Location
	
4. **Skype Email Search** - A transform that will return persons assosiated with that email address (may be multiple).  

	Required Maltego entity input: Email address 
	Maltego entity output: Person
	
5. **Skype Phone Search** - A transform that will return persons assosiated with that phone number (may be multiple).  

	Required Maltego entity input: Phone Number
	Maltego entity output: Person

5. **Skype Person Search** - A transform that will return persons assosiated with a name used (may be multiple).  

	Required Maltego entity input: Person
	Maltego entity output: Person
	
## NOTE: Only a max of 100 entities will be returned by the Skype Search API (currently working on a fix for this)