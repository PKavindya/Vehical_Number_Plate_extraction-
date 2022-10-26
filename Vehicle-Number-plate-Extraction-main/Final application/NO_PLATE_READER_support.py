
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def OK():
    print('NO_PLATE_READER_support.OK')
    sys.stdout.flush()

def READ():
    print('NO_PLATE_READER_support.READ')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import NO_PLATE_READER
    NO_PLATE_READER.vp_start_gui()




