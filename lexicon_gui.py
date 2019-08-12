import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import config_handler
import mongo_handler
import mongo_handler_2



class LexGUI:



    def __init__(self, win):
    	self.master = win
    	



    def createTabs(self):
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [40, 10],
                                        "font" : ('URW Gothic L', '11', 'bold')},}})
        s.theme_use("MyStyle")
        s.configure('TButton', relief='raised', padding= 6)
        

        self.tabControl = ttk.Notebook(self.master)
        
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        #self.tab3 = ttk.Frame(self.tabControl)
        #self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Write Google To Mongo')
        self.tabControl.add(self.tab2, text = 'Write Lexico To Mongo')      
        #self.tabControl.add(self.tab3, text = 'Extract')
        #self.tabControl.add(self.tab4, text = 'Upload')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/CLEANMAP", 
            title = "Select a clean map", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename):
            self.filepath.set(self.filename) #set the textbox to the file path
            #self.button2.config(state = "normal")
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE,self.filename)

    def dirDialog(self):
        self.filename = filedialog.askdirectory()
        if (self.filename):
            self.filepath.set(self.filename) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_DIR,self.filename)
    
    def processText(self):
        if(self.filepath.get()):
            mongo_handler.prepareMongoWrite(self.filepath.get())
        else:
            messagebox.showwarning("Error", "Missing input file")
   
    def createTab1(self):
        #frame

        self.labelFrame = ttk.LabelFrame(self.tab1, text= 'Select a clean map file:')
        self.labelFrame.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox
        self.filepath = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_DIR)
        self.filepath.set(value)
        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)


        self.path = ttk.Entry(self.labelFrame, width=90, textvariable = self.filepath)
        self.path.grid(column = 0, row = 1, sticky = "w")

        #button 1
        self.button1 = ttk.Button(self.labelFrame, text = "Browse A File", command=self.dirDialog)
        self.button1.grid(column = 1, row = 1, sticky = "w")

        #label 2
        self.label2 = ttk.Label(self.labelFrame, text="Click button to start writing to MongoDB:")
        self.label2.grid(column = 0, row = 2, sticky = "w")
      
        
 
   
        
        #button no 5
        self.button5 = ttk.Button(self.labelFrame, text = "START PROCESS", command=self.processText)
        self.button5.grid(column = 0, row = 5)

    def dirDialog2(self):
        self.filename2 = filedialog.askdirectory()
        if (self.filename2):
            self.filepath2.set(self.filename2) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_DIR2,self.filename2)
    
    def processText2(self):
        if(self.filepath2.get()):
            mongo_handler_2.prepareMongoWrite(self.filepath2.get())
        else:
            messagebox.showwarning("Error", "Missing input file")
   


    def createTab2(self):
        #frame

        self.labelFrame2 = ttk.LabelFrame(self.tab2, text= 'Select JSON folder:')
        self.labelFrame2.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox
        self.filepath2 = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_DIR2)
        self.filepath2.set(value)
        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)


        self.path2 = ttk.Entry(self.labelFrame2, width=90, textvariable = self.filepath2)
        self.path2.grid(column = 0, row = 1, sticky = "w")

        #button 1
        self.button21 = ttk.Button(self.labelFrame2, text = "Browse A File", command=self.dirDialog2)
        self.button21.grid(column = 1, row = 1, sticky = "w")

        #label 2
        self.label2 = ttk.Label(self.labelFrame2, text="Click button to start writing to MongoDB:")
        self.label2.grid(column = 0, row = 2, sticky = "w")
      
        
 
   
        
        #button no 5
        self.button25 = ttk.Button(self.labelFrame2, text = "START PROCESS", command=self.processText2)
        self.button25.grid(column = 0, row = 5)



    def createGUI(self):
        self.createTabs()    
        self.createTab1()
        self.createTab2()
   