import os
import subprocess

from enthought.traits.api import HasTraits, Str
from enthought.traits.ui.api import View, Group, HGroup, VGroup, ImageEditor, Item

HOME = os.environ["HOME"]
RECORD_DIR = os.path.join([HOME, "skype"])


class App(HasTraits):
    record_dir = Str(RECORD_DIR)
    ls_record_dir = Str

    inscight_logo_editor = ImageEditor(image=os.path.join("..", "img", "icons", "InSciGHT.jpg"))

    traits_view = View(Item('inscight_logo', 
                        editor=inscight_logo_editor, 
                        show_label=False,
                        ),
                  )


    #
    # Default Traits
    #

    def _ls_record_dir_default(self):
        lrd = subprocess.check_output(['ls', '-l', os.path.join])
        return lrd
