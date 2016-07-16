########################################################################################################################################
'''
	Script by Rocky5
	Used to enable/disable edit mode for the skin settings.
'''
########################################################################################################################################

import os
import xbmc

Enabler = xbmc.translatePath( "special://xbmc/system/keymaps/Enabled" )


########################################################################################################################################
# Start markings for the log file.
########################################################################################################################################
print "================================================================================"
print "| CheckEditMode.py loaded."
print "| ------------------------------------------------------------------------------"

if os.path.isfile(Enabler):
	xbmc.executebuiltin('Skin.SetBool(editmode)')
	print "| Edit mode is enabled."
	print "================================================================================"
else:
	xbmc.executebuiltin('Skin.reset(editmode)')
	print "| User mode is enabled."
	print "================================================================================"