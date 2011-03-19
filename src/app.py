import os
import subprocess
from threading import Timer

from enthought.traits.api import HasTraits, Str, Bool, Instance, Any
from enthought.traits.ui.api import View, Group, HGroup, VGroup, ImageEditor, Item

HOME = os.environ["HOME"]
RECORD_DIR = os.path.join(HOME, "skype")

class App(HasTraits):
    record_dir = Str(RECORD_DIR)
    ls_record_dir = Str
    recording = Bool
    ls_timer = Any

    inscight_logo_editor = ImageEditor(image=os.path.join("..", "img", "icons", "InSciGHT.jpg"))

    traits_view = View(Item('inscight_logo', 
                            editor=inscight_logo_editor, 
                            show_label=False,
                            ),
                       Item('recording',
                            #style="custom",
                            ),
                       )


    #
    # Default Traits
    #

    def list_rec_dir(self):
        lsrd = subprocess.check_output('ls -l {0}'.format(os.path.join(self.record_dir, '*')), shell=True)
        return lsrd

    def ls_timer_generator(self):
        def ls_rec_dir_timer():
            print "here"
            self.ls_record_dir = self.list_rec_dir()
            self.ls_timer = Timer(1.0, ls_rec_dir_timer)
            self.ls_timer.start()

        self.ls_timer = Timer(1.0, ls_rec_dir_timer)
        self.ls_timer.start()

    def _recording_default(self):
        print "Recording"
        self.ls_record_dir = self.list_rec_dir()
        print self.ls_record_dir
        self.ls_timer_generator()
        return False

    #
    # Changed Trait Events
    # 

    def _ls_record_dir_changed(self, old, new):
        print "Yo"
        recording = (old != new)
