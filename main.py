import PySimpleGUI as ps
ps.change_look_and_feel('DarkAmber')
layout =[
    [ps.Text('MINI CALCULATOR V.1.0.0')],
    [ps.Text('First Number'),ps.Input()],
    [ps.Text('Second Number'),ps.Input()],
    [ps.Button('Mul'), ps.Button('SUM'),ps.Text('Result:'),ps.Tes]]

window = ps.Window('Izvor_Calculator,V.1.0.0', layout)
def add(x1,x2):
    return x1+x2
def divide(x1,x2):
    return x1/x2
def substract(x1,x2):
    return x1-x2
def multiply(x1,x2):
    return x1*x2
def switch(chose):
    if(chose=='1'):
        return add(nr1,nr2)
    elif (chose == '2'):
        return substract(nr1,nr2)
    elif (chose == '3'):
        return divide(nr1,nr2)
    elif (chose == '4'):
        return multiply(nr1,nr2)

def switch_operation(chose):
    if(chose=='1'):
        return '+'
    elif (chose == '2'):
        return '-'
    elif (chose == '3'):
        return '/'
    elif (chose == '4'):
        return '*'

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
    
