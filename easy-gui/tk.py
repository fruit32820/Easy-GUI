from tkinter import *

def restrict_values(values,index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args and args[index] not in values:
                raise ValueError('Invalid value')
            return func(*args, **kwargs) 
        return wrapper 
    return decorator

def restrict_values_type(types,index):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not args and not isinstance(args[index],types):
                raise TypeError('Invalid value type')
            return func(*args, **kwargs) 
        return wrapper 
    return decorator

class tkapp:
    def __init__(self,title:str|None=None):
        self.tk=Tk()
        if title!=None:
            self.tk.title(title)
    @restrict_values(['title','geometry','var'],1)
    @restrict_values_type([str,list],2)
    def set(self,key:str,value:str):
        if key=="title":
            self.tk.title(value)
        elif key=="geometry":
            self.tk.geometry(value)
        elif key=="var":
            l=value.split('=')
            self.tk.setvar(l[0],l[1])
    def go(self):
        self.tk.mainloop()
    def stop(self):
        self.tk.quit()


a=tkapp("123")
a.set('geometry','1920x1080+1+0')
a.set('geomeetry',{"s":'1920x1080+1+0'})
a.go()
