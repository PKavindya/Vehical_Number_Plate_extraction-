

import sys
from tkinter import filedialog
from PIL import ImageTk,Image 
import cv2
import numpy as np
import pytesseract

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

import NO_PLATE_READER_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    NO_PLATE_READER_support.init(root, top)
    root.mainloop()

w = None


def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    NO_PLATE_READER_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    
path=""

class Toplevel1:
    

         
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        
        self.image = tk.StringVar()

        top.geometry("726x586+597+164")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.017, relwidth=1.011)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#00008b")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1,font= ("Times New Roman",30,"bold"))
        self.Label1.place(relx=0.03, rely=0.0, height=40, width=689)
        self.Label1.configure(activebackground="#00008b")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#c0c0c0")
        self.Label1.configure(background="#00008b")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''NUMBER PLATE READER''')

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.029, rely=0.07, relheight=0.121, relwidth=0.936)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000000")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        
        self.panel = tk.Label(root) 

        self.Label2 = tk.Label(self.Frame2, font= ("Times New Roman",14,"bold"))
        self.Label2.place(relx=0.017, rely=0.208, height=21, width=127)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="#013220")
        self.Label2.configure(background="#000000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#013220")
        self.Label2.configure(text='''IMAGE''')

        self.TEntry1 = ttk.Entry(self.Frame2,textvariable = self.image)
        self.TEntry1.place(relx=0.18, rely=0.208, relheight=0.361, relwidth=0.591)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TButton1 = ttk.Button(self.Frame2, command=self.browse )
        self.TButton1.place(relx=0.793, rely=0.208, height=30, width=78)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''BROWSE''')

        self.TFrame1 = ttk.Frame(self.Frame1)
        self.TFrame1.place(relx=0.027, rely=0.2, relheight=0.654, relwidth=0.94)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1,font= ("Times New Roman",30,"bold"))
        self.TLabel1.place(relx=0.42, rely=0.028, height=27, width=121)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''ORIGINAL IMAGE''')

        self.TFrame2 = ttk.Frame(self.TFrame1)
        self.TFrame2.place(relx=0.014, rely=0.1, relheight=0.877, relwidth=0.974)

        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")
        

        self.Canvas1 = tk.Canvas(self.TFrame2)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.016)
        self.Canvas1.configure(background="#000000")

        self.TFrame3 = ttk.Frame(self.Frame1)
        self.TFrame3.place(relx=0.027, rely=0.872, relheight=0.092
                , relwidth=0.933)
        self.TFrame3.configure(relief='groove')
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief="groove")

        self.TButton2 = ttk.Button(self.TFrame3)
        self.TButton2.place(relx=0.042, rely=0.182, height=30, width=98)
        self.TButton2.configure(command=self.Read)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''EXTRACT''')

        self.TEntry2 = ttk.Label(self.TFrame3, font= ("Times New Roman",28,"bold"))
        self.TEntry2.place(relx=0.216, rely=0.182, relheight=1, relwidth=0.753)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")
        
        
    def Read(self) :
        
        #Load image
        path=self.image.get()

        I1 = cv2.imread(path)
        
        b,g,r = cv2.split(I1)           # get b,g,r
        rgb_img = cv2.merge([r,g,b])     # switch it to rgb

        # Denoising
        dst = cv2.fastNlMeansDenoisingColored(I1,None,10,10,7,21)

        b,g,r = cv2.split(dst)           # get b,g,r
        I2 = cv2.merge([r,g,b])     # switch it to rgb
        
        gray = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        # Further noise removal
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

        # sure background area
        bg = cv2.dilate(opening, kernel, iterations=3)

        # Finding sure foreground area
        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        ret, fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

        # Finding unknown region
        fg = np.uint8(fg)
        un = cv2.subtract(bg, fg)
        
        # Marker labelling
        ret, markers = cv2.connectedComponents(fg)

        # Add one to all labels so that sure background is not 0, but 1
        markers = markers + 1

        # Now, mark the region of unknown with zero
        markers[un == 255] = 0

        markers = cv2.watershed(I1, markers)
        I1[markers == -1] = [255, 0, 0]

        I4= markers
        img = Image.fromarray(I4)
        
        img = np.array(img) 
        binarr = np.where(img>1, 255, 0)
        img1 = Image.fromarray(binarr)
        rgb_im = img1.convert('RGB')
        rgb_im.save('my.jpg')

        img2 = cv2.imread('my.jpg')
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        text = pytesseract.image_to_string(img2, config='--psm 11')
        #print
        self.TEntry2.config(text=text)
        
     
    def browse (self):

        self.image.set(filedialog.askopenfilename(title = "SELECT IMAGE", filetype = (("JPG File","*.jpg"),("PNG File","*.png"))))

        path=self.image.get()
        im=Image.open(path) 
        photo=ImageTk.PhotoImage(im) 
        
        self.Canvas1.create_image(10, 10, image=photo, anchor='nw')   
        self.panel.configure(image=im)
        
        


if __name__ == '__main__':
    vp_start_gui()
    





