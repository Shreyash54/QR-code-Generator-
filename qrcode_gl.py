#importing essential library-----------------------------#
import qrcode
from tkinter import *


#----------------------------------Methods--------------------------#


def code_gen():

#---------------link 1 set up for qr generation-----#
    code_f =qrcode.QRCode(box_size=35, border=4)
    code_f.add_data("https://www.netflix.com/in")
    code_f.make(fit=True)


#---------------link 2 set up for qr generation -----#
    code_d = qrcode.QRCode(box_size=35, border=4)
    code_d.add_data("https://www.hotstar.com/in")
    code_f.make(fit=True)

#-------------- OUTPUT FOR LINK 1----------------------#
    qrcode_img = code_f.make_image(fill_color = "black", back_color ="white")
    qrcode_img.save("GL1.png")


#--------------OUTPUT FOR LINK 2------------------#
    qrcode_img = code_d.make_image(fill_color="black", back_color="white")
    qrcode_img.save("GL2.png")



#------------------label---------------------------------------------#


    a =Label(tk_window , text="QR CODE GENERATED", background="white",
             fg ="red", font=("Arial",30,"italic"))
    a.pack()
#-----------FRAME SET UP--------------------------------------------#
tk_window =Tk()
tk_window.config(bg="purple")
tk_window.geometry("500x500")
tk_window.title("QR CODE GENERATOR")

a1 = Label(tk_window, text ="QR CODE GENERATOR",
          background="VIOLET", fg="red", font=("Arial", 20,"bold"))
a1.pack()


#----------------------Buttons------------------------------#


b1 = Button(tk_window, text="GENERATE", background="pink",
            fg="purple", font=("calibri",30,"bold"), command=code_gen)

b1.pack()

#-----------TO CLOSE WINDOW___________#

tk_window.mainloop()