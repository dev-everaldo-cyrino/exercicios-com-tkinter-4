from tkinter import *

root = Tk()
root.geometry('700x500+0+0')
root.title('cadastro com checkbutton')

def imprimir(pesar,precao,vista,audicao):
    print(pesar,precao,vista,audicao)
    if pesar == 1:
        pesar = 'exame feito'
    else:
        pesar = 'não feito !'
    if precao == 1:
        precao = 'exame feito'
    else:
        precao = 'não feito !'
    if vista == 1:
        vista = 'exame feito'
    else:
        vista = 'não feito !'
    if audicao == 1:
        audicao = 'exame feito'
    else:
        audicao = 'não feito !'
    
    print('''
          -----exames feitos-----
          pesagem: {}
          preção: {}
          vista: {}
          audição: {}'''.format(pesar,precao,vista,audicao))
    
    
Label(root,text='cadastro de ficha medica',font=('Arial',30)).place(x=80,y=10)

pesar = IntVar()
precao = IntVar()
vista = IntVar()
audicao = IntVar()

pesare = Checkbutton(root,text='pesagem',font=('Arial',18),variable=pesar,onvalue=1,offvalue=0)
pesare.place(x=10,y=60)
precaoe = Checkbutton(root,text='preção',font=('Arial',18),variable=precao,onvalue=1,offvalue=0)
precaoe.place(x=10,y=100)
vistae = Checkbutton(root,text='vista',font=('Arial',18),variable=vista,onvalue=1,offvalue=0)
vistae.place(x=10,y=140)
audicaoe = Checkbutton(root,text='audição',font=('Arial',18),variable=audicao,onvalue=1,offvalue=0)
audicaoe.place(x=10,y=180)

btn = Button(root,text='imprimir',font=('Arial',20),bd=5,command=lambda:imprimir(pesar.get(),precao.get(),vista.get(),audicao.get()))
btn.place(x=10,y=220)

root.mainloop()