Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> tk = Tk()
>>> btn = Button(tk, text = "click me")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    btn = Button(tk, text = "click me")
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 2208, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 2138, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
_tkinter.TclError: can't invoke "button" command: application has been destroyed
>>> btn = Button(tk, text="click me")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    btn = Button(tk, text="click me")
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 2208, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 2138, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
_tkinter.TclError: can't invoke "button" command: application has been destroyed
>>> tk = Tk():
	
SyntaxError: invalid syntax
>>> tk = Tk()
>>> btn = Button(tk, text="click me")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    btn = Button(tk, text="click me")
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 2208, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 2138, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
_tkinter.TclError: can't invoke "button" command: application has been destroyed
>>> from tkinter import *
>>> tk=Tk()
>>> 
>>> btn=Button(tk,text="click me")
>>> btn.pack()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    btn.pack()
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 1990, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't invoke "pack" command: application has been destroyed
>>> from tkinter import *
>>> tk = Tk()
>>> btn=Button(tk. text="click me")
SyntaxError: keyword can't be an expression
>>> btn = Button(tk, text= "Click me")
>>> btn.pack()
>>> btn.pack()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    btn.pack()
  File "C:\Users\22B\AppData\Local\Programs\Python\Python35\lib\tkinter\__init__.py", line 1990, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't invoke "pack" command: application has been destroyed
>>> 
