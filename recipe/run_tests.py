import sys

import psychopy
import psychopy.app
# import psychopy.app.builder
# import psychopy.data
# import psychopy.experiment
import psychopy.gui
import psychopy.gui.qtgui
import psychopy.gui.wxgui
import psychopy.hardware
import psychopy.monitors
import psychopy.preferences
# import psychopy.visual
# import psychopy.sound

# Disable problematic tests on Linux.
# See https://github.com/conda-forge/staged-recipes/pull/8645
if sys.platform != 'linux':
    import psychopy.event

# Skip on Linux and Windows
if sys.platform == 'darwin':
    import psychopy.app.coder
