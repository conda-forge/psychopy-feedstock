import sys

import psychopy
import psychopy.app
import psychopy.data
import psychopy.experiment
import psychopy.gui
import psychopy.hardware
import psychopy.monitors
import psychopy.preferences
import psychopy.sound
assert psychopy.sound.audioLib == 'sounddevice'

# Disable problematic tests on Linux.
# See https://github.com/conda-forge/staged-recipes/pull/8645
if sys.platform != 'linux':
    import psychopy.event
    import psychopy.visual
