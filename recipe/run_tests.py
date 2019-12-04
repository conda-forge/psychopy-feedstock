import sys
import os
os.environ['LC_ALL'] = 'en_US.UTF-8'

import psychopy
import psychopy.app
import psychopy.app.builder
import psychopy.app.coder
import psychopy.data
import psychopy.experiment
import psychopy.gui
import psychopy.gui.qtgui
import psychopy.gui.wxgui
import psychopy.hardware
import psychopy.monitors
import psychopy.preferences
import psychopy.event
import psychopy.visual

# Disable sounddevice test on Windows, as currently we don't have a
# soundfile package, without which this device won't work.
if sys.platform != 'win32':
    import psychopy.sound
    assert psychopy.sound.audioLib == 'sounddevice'

