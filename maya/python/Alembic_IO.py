"""source: https://github.com/4degrees/segue/blob/master/source/segue/backend/host/maya.py"""
import pymel.core as pm
import os
import errno

#load plugin
if not pm.pluginInfo('AbcExport',query=True,loaded=True):
   pm.loadPlugin( 'AbcExport' )

#selection
selection = pm.ls(sl=True)
if not selection:
   raise ValueError('Cannot save empty selection.')
previouse_selection = selection

#get frame range
fstart = pm.playbackOptions(query=True, minTime=True)
fend = pm.playbackOptions(query=True, maxTime=True)
fcurrent = pm.currentTime()
step =1

# Ensure target folder exists
target = (u'F:\local_WIP\pythonAbcExport')
try:
   os.makedirs(target)
except OSError as error:
   if error.errno != errno.EEXIST:
       raise

#build filepath
cache_path = os.path.join(target, 'cache.abc')

#main
try:
   pm.select(selection,hierarchy=True,replace=True)
   options = []
   for entry in selection:
       options.append('-root {0}'.format(entry))
   options.append('-frameRange {0} {1}'.format(fstart, fend))
   options.append('-step {0}'.format(step))
   options.append('-uvWrite')
   options.append('-writeColorSets -writeFaceSets -writeUVSets -dataFormat ogawa')
   options.append('-file {0}'.format(cache_path))
   
   pm.AbcExport(verbose=True, jobArg=' '.join(options))

finally:
   pm.select(clear=True)
   pm.select(previouse_selection,replace=True)
   pm.currentTime(fcurrent)
