import os
import subprocess
from threading import Timer

from enthought.traits.api import HasTraits, Str, Bool, Instance, Any, File
from enthought.traits.ui.api import View, Group, HGroup, VGroup, ImageEditor, Item, spring

HOME = os.environ["HOME"]
RECORD_DIR = os.path.join(HOME, "skype")

class App(HasTraits):
    record_dir = Str(RECORD_DIR)
    ls_record_dir = Str
    recording = Bool
    ls_timer = Any

    inscight_logo_editor = ImageEditor(image=os.path.join("..", "..", "img", "icons", "InSciGHT.jpg"))

    ok_editor = ImageEditor(image=os.path.join("..", "..", "img", "app", "ok.png"))
    not_ok_editor = ImageEditor(image=os.path.join("..", "..", "img", "app", "not_ok.png"))

    traits_view = View(HGroup(Item('inscight_logo', 
                                editor=inscight_logo_editor, 
                                show_label=False,
                                ),
                              Item('recording',
                                visible_when="False",
                                ),
                              spring,
                              Item('ok', 
                                   editor=ok_editor, 
                                   visible_when="recording", 
                                   show_label=False,
                                   ),
                              Item('not_ok', 
                                   editor=not_ok_editor, 
                                   visible_when="not recording", 
                                   show_label=False,
                                   ),
                             ),
                       #resizable=True,
                       width = 400,
                       height = 150,
                       )


    #
    # Default Traits
    #

    def list_rec_dir(self):
        lsrd = subprocess.check_output('ls -l {0}'.format(os.path.join(self.record_dir, '*')), shell=True)
        return lsrd

    def ls_timer_generator(self):
        def ls_rec_dir_timer():
            # Updates the recording trait
            lsrd = self.list_rec_dir()
            self.recording = (self.ls_record_dir != lsrd)
            self.ls_record_dir = lsrd

            # Spawns subsequent timers indefinitely
            self.ls_timer = Timer(1.0, ls_rec_dir_timer)
            self.ls_timer.start()

        # Spawns the initial timer
        self.ls_timer = Timer(1.0, ls_rec_dir_timer)
        self.ls_timer.start()

    def _recording_default(self):
        """Initializes the recording trait."""
        self.ls_record_dir = self.list_rec_dir()
        self.ls_timer_generator()
        return False

    #
    # Changed Trait Events
    # 
