import tensorflow as tf
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

print("Model loading...")
model = tf.keras.models.load_model("model")
PLANTS_NAME = ['Tomato Healthy', 'Tomato Septoria Leaf Spot', 'Tomato Bacterial Spot', 'Tomato Blight', 'Cabbage Healthy', 'Tomato Spider Mite', 'Tomato Leaf Mold', 'Tomato_Yellow Leaf Curl Virus', 'Soy_Frogeye_Leaf_Spot', 'Soy_Downy_Mildew', 'Maize_Ravi_Corn_Rust', 'Maize_Healthy', 'Maize_Grey_Leaf_Spot', 'Maize_Lethal_Necrosis', 'Soy_Healthy', 'Cabbage Black Rot']

root = Tk()
root.geometry("800x500+300+100")
root.title("Plant Disease Classification ")
root.config(bg="black")

imag_arr = []
def openfile(img_label):
    imag_arr.clear()
    img_path = filedialog.askopenfile(title='Please select an image',
                           filetypes=[('Image Files', ['.jpeg', '.jpg', 
                                                        '.png'
                                                       ])])
    
    imag_arr.append(np.asarray(Image.open(img_path.name).resize((300, 300)))[np.newaxis, ...] / 255.0)
    
    img = ImageTk.PhotoImage(Image.open(img_path.name).resize((300,300)))
    img_label.configure(image=img)
    img_label.image=img

def predict(pred_label):
    predictions = model(imag_arr[0]).numpy()[0]
    name = PLANTS_NAME[np.argmax(predictions)]
    pred_label.config(text=name)
    



def model_page():
    win = Tk()
    win.geometry("800x500+300+100")
    win.title("Plant Disease Classification ")
    win.config(bg="black")
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\Khadim Hussain\Pictures\data visualization.png").resize((300,240)))
    img_label = Label(win, image=img)
    img_label.place(x=300,y=30)
    pred_button = Button(win, text="Classify Disease", fg = "black", bg = "green", relief = "raised", font = ("arial", 16, "bold"), command= lambda:predict(pred_label))
    select_image_button = Button(win, text="  Select  Image  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command=lambda :openfile(img_label))
    select_image_button.place(x=360,y=370)
    pred_button.place(x=360,y=420)
    pred_label = Label(win, text="None", font = ("arial", 16, "bold"),fg="white", bg="black")
    pred_label.place(x=380, y=320)
    win.mainloop()


def login():
    users = {'a': 'a'}
    username = userName.get()
    Pass = password.get()
    if username in users :
        if (users[username] == Pass):
            label4 = Label(root, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
            root.destroy()
            model_page()
        else:
            label4 = Label(root, text = ("Incorrect Password for " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

    else:
        label4 = Label(root, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)

#----------------------------------------------------------------------------------------------------------------
#first lable
label1 = Label(root, text = " Crops Disease Classification", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 20, y = 15)

label2 = Label(root, text = "User Name :", font = ("arial", 16, "bold"), bg="black", fg="white")
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(root, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(root, text = "Password :", font = ("arial", 16, "bold"),fg="white", bg="black")
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(root, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(root, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 335, y = 340)

root.mainloop()