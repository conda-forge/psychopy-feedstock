import sys

import psychopy
import psychopy.app
import psychopy.data
import psychopy.experiment
import psychopy.gui
import psychopy.gui.qtgui
import psychopy.gui.wxgui
import psychopy.hardware
import psychopy.monitors
import psychopy.preferences

# Disable sounddevice test on Windows, as currently we don't have a
# soundfile package, without which this device won't work.
if sys.platform != 'win32':
    import psychopy.sound
    assert psychopy.sound.audioLib == 'sounddevice'

    # Builder will also look for a working audio backend, so disable this
    # test for Windows too.
    import psychopy.app.builder

# Disable problematic tests on Linux.
# See https://github.com/conda-forge/staged-recipes/pull/8645
if sys.platform != 'linux':
    import psychopy.event
    import psychopy.visual
    import psychopy.app.coder
