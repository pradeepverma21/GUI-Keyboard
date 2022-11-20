import tkinter as tk 
from tkinter import ttk


#functioning code

exp = " "
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)

def clear():
    global exp
    exp = " "
    equation.set(exp)

def action():
    global exp
    exp = " Next Line "
    equation.set(exp)

#function finished


key = tk.Tk()
key.title("Keyboard by Pradeep")  
key.geometry("1270x250")
key.maxsize(width=1270,height=250)
key.minsize(width=1270,height=250)

equation = tk.StringVar()
dis_entry = ttk.Entry(key,state='readonly',textvariable=equation)
dis_entry.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20)
key.config(bg='orange')

#first line 
q= ttk.Button(key,text='Q',command=lambda:press('Q'))
q.grid(row=1,column=0,ipadx=6,ipady=10)

w = ttk.Button(key,text='W',command=lambda:press('W'))
w.grid(row=1,column=1,ipadx=6,ipady=10)

e = ttk.Button(key,text='E',command=lambda:press('E'))
e.grid(row=1,column=2,ipadx=6,ipady=10)

r = ttk.Button(key,text='R',command=lambda:press('R'))
r.grid(row=1,column=3,ipadx=6,ipady=10)

t = ttk.Button(key,text='T',command=lambda:press('T'))
t.grid(row=1,column=4,ipadx=6,ipady=10)

y = ttk.Button(key,text='Y',command=lambda:press('Y'))
y.grid(row=1,column=5,ipadx=6,ipady=10)

u = ttk.Button(key,text='U',command=lambda:press('U'))
u.grid(row=1,column=6,ipadx=6,ipady=10)

i = ttk.Button(key,text='I',command=lambda:press('I'))
i.grid(row=1,column=7,ipadx=6,ipady=10)

o = ttk.Button(key,text='O',command=lambda:press('O'))
o.grid(row=1,column=8,ipadx=6,ipady=10)

p = ttk.Button(key,text='P',command=lambda:press('P'))
p.grid(row=1,column=9,ipadx=6,ipady=10)

curly= ttk.Button(key,text='{',command=lambda:press('{'))
curly.grid(row=1,column=10,ipadx=6,ipady=10)

curly1 = ttk.Button(key,text='}',command=lambda:press('}'))
curly1.grid(row=1,column=11,ipadx=6,ipady=10)


clean = ttk.Button(key,text='Clear',command=clear)
clean.grid(row=1,column=12,ipadx=6,ipady=10)

# second line 

a= ttk.Button(key,text='A',command=lambda:press('A'))
a.grid(row=2,column=0,ipadx=6,ipady=10)

s = ttk.Button(key,text='S',command=lambda:press('S'))
s.grid(row=2,column=1,ipadx=6,ipady=10)

d = ttk.Button(key,text='D',command=lambda:press('D'))
d.grid(row=2,column=2,ipadx=6,ipady=10)

f = ttk.Button(key,text='F',command=lambda:press('F'))
f.grid(row=2,column=3,ipadx=6,ipady=10)

g = ttk.Button(key,text='G',command=lambda:press('G'))
g.grid(row=2,column=4,ipadx=6,ipady=10)

h = ttk.Button(key,text='H',command=lambda:press('H'))
h.grid(row=2,column=5,ipadx=6,ipady=10)

j = ttk.Button(key,text='J',command=lambda:press('J'))
j.grid(row=2,column=6,ipadx=6,ipady=10)

k = ttk.Button(key,text='K',command=lambda:press('K'))
k.grid(row=2,column=7,ipadx=6,ipady=10)

l = ttk.Button(key,text='L',command=lambda:press('L'))
l.grid(row=2,column=8,ipadx=6,ipady=10)

colon = ttk.Button(key,text=':',command=lambda:press(':'))
colon.grid(row=2,column=9,ipadx=6,ipady=10)

div = ttk.Button(key,text='\\',command=lambda:press('\\'))
div.grid(row=2,column=10,ipadx=6,ipady=10)


apos = ttk.Button(key,text='"',command=lambda:press('"'))
apos.grid(row=2,column=11,ipadx=6,ipady=10)

enter = ttk.Button(key,text='Enter',command=action)
enter.grid(row=2,column=12,ipadx=6,ipady=10)


# third line 

shift = ttk.Button(key,text='Shift',command=lambda:press('Shift'))
shift.grid(row=3,column=0,ipadx=6,ipady=10)

z= ttk.Button(key,text='Z',command=lambda:press('Z'))
z.grid(row=3,column=1,ipadx=6,ipady=10)

x = ttk.Button(key,text='X',command=lambda:press('X'))
x.grid(row=3,column=2,ipadx=6,ipady=10)

c = ttk.Button(key,text='C',command=lambda:press('C'))
c.grid(row=3,column=3,ipadx=6,ipady=10)

v = ttk.Button(key,text='V',command=lambda:press('V'))
v.grid(row=3,column=4,ipadx=6,ipady=10)

b = ttk.Button(key,text='B',command=lambda:press('B'))
b.grid(row=3,column=5,ipadx=6,ipady=10)

n = ttk.Button(key,text='N',command=lambda:press('N'))
n.grid(row=3,column=6,ipadx=6,ipady=10)

m = ttk.Button(key,text='M',command=lambda:press('M'))
m.grid(row=3,column=7,ipadx=6,ipady=10)

comma = ttk.Button(key,text=',',command=lambda:press(','))
comma.grid(row=3,column=8,ipadx=6,ipady=10)

dot = ttk.Button(key,text='.',command=lambda:press('.'))
dot.grid(row=3,column=9,ipadx=6,ipady=10)

question = ttk.Button(key,text='?',command=lambda:press('?'))
question.grid(row=3,column=10,ipadx=6,ipady=10)

div = ttk.Button(key,text='\\',command=lambda:press('\\'))
div.grid(row=3,column=11,ipadx=6,ipady=10)

shift = ttk.Button(key,text='Shift',command=lambda:press('Shift'))
shift.grid(row=3,column=12,ipadx=6,ipady=10)

#fourth line 

control = ttk.Button(key,text='Ctrl',command=lambda:press('Ctrl'))
control.grid(row=4,column=0,ipadx=6,ipady=10)

fn = ttk.Button(key,text='Fn',command=lambda:press('Fn'))
fn.grid(row=4,column=1,ipadx=6,ipady=10)

window = ttk.Button(key,text='window',command=lambda:press('window'))
window.grid(row=4,column=2,ipadx=6,ipady=10)

alt = ttk.Button(key,text='Alt',command=lambda:press('Alt'))
alt.grid(row=4,column=3,ipadx=6,ipady=10)

space = ttk.Button(key,text='Space',command=lambda:press(' '))
space.grid(row=4,columnspan=14,ipadx=160,ipady=10)

alt_gr = ttk.Button(key,text='Alt Gr',command=lambda:press('Alt Gr'))
alt_gr.grid(row=4,column=9,ipadx=6,ipady=10)

paren = ttk.Button(key,text='(',command=lambda:press('('))
paren.grid(row=4,column=10,ipadx=6,ipady=10)

paren1 = ttk.Button(key,text=')',command=lambda:press(')'))
paren1.grid(row=4,column=11,ipadx=6,ipady=10)

tab = ttk.Button(key,text='Tab',command=lambda:press('Tab'))
tab.grid(row=4,column=12,ipadx=6,ipady=10)







key.mainloop()
