from tkinter import*
import socket
import threading

def runserver():
    #####################
    serverip = '192.168.1.3'
    port = 9000
    #####################

    buffsize = 4096

    while True:
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            server.bind((serverip,port))
            server.listen(1)
            print('waiting micropython...')

            client, addr = server.accept()
            print('connected from:', addr)

            data = client.recv(buffsize).decode('utf-8')
            print('Data from MicroPython: ',data)
            
            data_split = data.split(':')
            
            if float(data_split[1]) > 30:
                img = PhotoImage(file='G/L3.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {}C°'.format(data_split[0],data_split[1]))
           
            elif float(data_split[1]) > 29:
                img = PhotoImage(file='G/L2.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {}C°'.format(data_split[0],data_split[1]))
                
            elif float(data_split[1]) > 28:
                img = PhotoImage(file='G/L1.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {}C°'.format(data_split[0],data_split[1]))
            
            else :
                img = PhotoImage(file='level/level1.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('อุณหภมิเย็นเกินไป!!')            
            '''
            if data_split[1] == 'ON':
                v_status.set('{} สถานะ {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='green')
            else:
                v_status.set('{} สถานะ {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='red')
            ''' 
            client.send('received your messages.'.encode('utf-8'))
            client.close()
            
            
            
GUI = Tk()
GUI.geometry('550x550')
GUI.title('โปรแกรมติดตามสถานะ IOT By วิบูลย์')

FONT = ('Angsana New',20)
FONT2 = ('Angsana New',30)
L1= Label(GUI, text='สถานะ LED จาก MicroPython',font=FONT)
L1.pack()

v_status = StringVar()
v_status.set('<<<< No Status >>>>')
L2 = Label(GUI, textvariable= v_status, font=FONT2)
L2.configure(fg='red')
L2.pack(ipady=30)


img = PhotoImage(file='G/L1.png')
ICON = Label(GUI,image=img)
ICON.pack(ipady= 5)


############# RUNSERVER ###############
task = threading.Thread(target=runserver)
task.start()
#######################################
GUI.mainloop()
