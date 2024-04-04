from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pickle
from sklearn.preprocessing import StandardScaler
##################
root =  Tk()

warehouse = StringVar()
shipment = StringVar()
weight = StringVar()
discount = StringVar()
prior_purchase = StringVar()
product_imp = StringVar()
gender = StringVar()  
cost = StringVar()
rating = StringVar()
customer_care = StringVar()

def validations():
    if warehouse.get() == 'nearby city:':
        messagebox.showerror("Alert", "Select city")
    elif shipment.get() == "shipment: " :
        messagebox.showerror("Alert", "Select shipment")
    elif weight.get() == "weight of product in gms: " :
        messagebox.showerror("Alert", "select weight of product")
    elif discount.get() == "discount in dollars:" :
        messagebox.showerror("Alert", "select discount")
    elif product_imp.get() == "product importance: " :
        messagebox.showerror("Alert", "Select product importance")
    elif prior_purchase.get() == "prior purchases:" :
        messagebox.showerror("Alert", "select prior purchases")
    elif cost.get() == "cost range in dollars: " :
        messagebox.showerror("Alert", "Select cost")
    elif rating.get() == "product rating: " :
        messagebox.showerror("Alert", "Select rating")
    elif gender.get() == "gender:  " :
        messagebox.showerror("Alert", "Select gender")
    elif customer_care.get() == "total calls: " :
        messagebox.showerror("Alert", "Select calls")






def reset() :
    shipment.set("shipment: ")
    weight.set("weight of product in gms: ")
    discount.set("discount in dollars: ")
    product_imp.set("product importance: ")
    prior_purchase.set("prior purchases: ")
    cost.set("cost range in dollars: ")
    rating.set("product rating: ")
    gender.set("gender: ")
    warehouse.set("nearby city: ")
    customer_care.set("total calls: ")
    messagebox.showinfo("Sucess", "Records cleared!")

def predict():
    validations()
    warehouse1 = warehouse.get()
    if warehouse1 == "mumbai":
        warehouse1= "1"
    elif warehouse1 == "bangalore":
        warehouse1="2"
    elif warehouse1 == "delhi":
        warehouse1="3"
    elif warehouse1 == "pune":
        warehouse1="4"
    elif warehouse1 == "surat":
        warehouse1="5"
    ####################################
    shipment1 = shipment.get()
    if shipment1 =="Road":
        shipment1 = "1"
    elif shipment1 =="Flight":
        shipment1 = "2"
    elif shipment1 =="Ship":
        shipment1 = "3"
    ##############################
    customer_care1 = customer_care.get() 
    ###########################
    rating1 = rating.get()
    ##########################
    cost1 = cost.get()
    if cost1 == "0-25":
        cost1= '1'
    if cost1 == "25-50":
        cost1= '2'
    if cost1 == "50-75":
        cost1= '3'
    if cost1 == "75-100":
        cost1= '4'
    if cost1 == "100-125":
        cost1= "5"
    if cost1 == "125-150":
        cost1 = "6"
    if cost1 == "150-175":
        cost1= "7"
    if cost1 == "175-200":
        cost1= "8"
    if cost1 == "200-225":
        cost1= "9"
    if cost1 == "225-250":
        cost1= "10"
    if cost1 == "250-275":
        cost1= "11"
    if cost1 == "275-300":
        cost1= "12"
    if cost1 == "300-325":
        cost1= "13"
    if cost1 == "325-350":
        cost1= "14"
    if cost1 == "350-375":
        cost1= "15"
    #####################
    weight1 = weight.get()
    if weight1== "0-500":
        weight1 = "1"
    if weight1== "500-1000":
        weight1 = "2"
    if weight1== "1000-1500":
        weight1 = "3"
    if weight1== "1500-2000":
        weight1 = "4"
    if weight1== "2000-2500":
        weight1 = "5"
    if weight1== "2500-3000":
        weight1 = "6"
    if weight1== "3000-3500":
        weight1 = "7"
    if weight1== "3500-4000":
        weight1 = "8"
    if weight1== "4000-4500":
        weight1 = "9"
    if weight1== "4500-5000":
        weight1 = "10"
    if weight1== "5000-5500":
        weight1 = "11"
    if weight1== "5500-6000":
        weight1 = "12"
    if weight1== "6000-6500":
        weight1 = "13"
    if weight1== "6500-7000":
        weight1 = "14"
    if weight1== "7000-7500":
        weight1 = "15"
    if weight1== "7500-8000":
        weight1 = "16"
    ###################################
    discount1 = discount.get()
    if discount1 == "0-10":
        discount1 ="1"
    if discount1 == "10-20":
        discount1 ="2"
    if discount1 == "20-30":
        discount1 ="3"
    if discount1 == "30-40":
        discount1 ="4"
    if discount1 == "40-50":
        discount1 ="5"
    if discount1 == "50-60":
        discount1 ="6"
    if discount1 == "60-70":
        discount1 ="7"
    if discount1 == "70-80":
        discount1 ="8"
    if discount1 == "80-90":
        discount1 ="9"
        ####################
    prior_purchase1 = prior_purchase.get()
    product_imp1 = product_imp.get()
    if product_imp1 == "low":
        product_imp1 = "1"
    if product_imp1 == "medium":
        product_imp1 = "2"
    if product_imp1 == "high":
        product_imp1 = "3"

    gender1 = gender.get() 
    if gender1 == "Male":
        gender1 = "1"
    if gender1 =="Female":
        gender1 ="2" 
    
    ##########################
    file = open("database.txt","a")
    file.write("warehouse "+warehouse1+"\n")
    file.write("shipment: "+shipment1+"\n")
    file.write("cc  "+customer_care1+"\n")
    file.write("rating "+rating1+"\n")
    file.write("prior_purchase: "+prior_purchase1+"\n")
    file.write("importance: "+product_imp1+"\n")
    file.write("gender: "+gender1+" ")
    file.write("weight: "+weight1+"\n")
    file.write("cost: "+cost1+"\n ")
    file.write("discount: "+discount1+"\n ")
    ##############################
    pickled_model = pickle.load(open('smote_model.pkl', 'rb'))
    scaler_model = pickle.load(open('scaler_model.pkl', 'rb'))
    prediction=scaler_model.transform([[int(warehouse1),int(shipment1),int(customer_care1),int(rating1),int(prior_purchase1),int(product_imp1),int(gender1),int(weight1),int(cost1),int(discount1)]])
    pred=pickled_model.predict(prediction)
    if (pred[0]== 1):
        messagebox.showinfo("Sucess", "Oops!your Delivery can't be on time.\n sorry for the inconvenience")
    if (pred [0] == 0):
        messagebox.showinfo("Sucess", "Hurrey!your Delivery will be in time.")
    file.close()
    #######################
    messagebox.showinfo("Sucess", "Records saved!")
    print("Printing Data: ")
    print(warehouse1,shipment1,customer_care1,rating1,prior_purchase1,product_imp1,gender1,weight1,cost1,discount1)
#



root.geometry("1000x800")
root.configure(background="#9A7B4F")
root.title("Prediction")

img =PhotoImage(file="black.png")
Label(root,image=img).pack()

title = Label(root, text="Find out your Delivery will be in time or not ??", relief=SUNKEN,bg="#671414", width="300", height="2", fg="white", font = ("Calibri 20 bold italic underline")).pack()
############################
warehouse1 = Label(root, text="Where do you stay?: ", bg="cyan",width=26, relief="raised",borderwidth=3, font=("Verdana 12")).place(x=12, y=321)
warehouse = StringVar(root)
warehouse.set("nearby city: ")
entry_warehouse = OptionMenu(root, warehouse, "mumbai", "bangalore", "delhi","pune","surat")
entry_warehouse.config(width=15,font = ("Verdana 12"))
entry_warehouse.place(x=300,y=320)
######################################

customer_care1 = Label(root, text="customer care calls? : ",bd=20,width=26,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12"))
customer_care1.place(x=12, y=362)
customer_care = StringVar(root)
customer_care.set("total calls: ")
entry_customer = OptionMenu(root, customer_care, "1", "2","3", "4","5", "6","7")
entry_customer.config(width=15,font = ("Verdana 12"))
entry_customer.place(x=300,y=360)
##########################################

gender1 = Label(root, text="Gender : ",bd=20,  bg="cyan",width=26, relief="raised",borderwidth=3,font=("Verdana 12")).place(x=12, y=402)
gender = StringVar(root)
gender.set("gender: ")
entry_gender = OptionMenu(root, gender, "Male", "Female")
entry_gender.config(width=15,font = ("Verdana 12"))
entry_gender.place(x=300,y=400)
################################
rating1 = Label(root, text="Customer rating product had? : ",bd=20,width=26,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=12, y=442)
rating = StringVar(root)
rating.set("product rating: ")
entry_rating = OptionMenu(root, rating,"1", "2","3", "4","5")
entry_rating.config(width=15,font = ("Verdana 12"))
entry_rating.place(x=300,y=440)
#############################
cost1 = Label(root, text="cost of the product? : ",bd=20,width=28,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=500, y=321)
cost = StringVar(root)
cost.set("cost range in dollars: ")
entry_cost = OptionMenu(root, cost, "0-25","25-50","50-75","75-100","100-125","125-150","150-175","175-200","200-225","200-250","250-275","275-300","300-325","325-350","350-375")
entry_cost.config(width=15,font = ("Verdana 12"))
entry_cost.place(x=800,y=321)

#############################
prior_purchase1 = Label(root, text="number of prior purchases? : ",bd=20,width=28,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=500, y=362)
prior_purchase = StringVar(root)
prior_purchase.set("prior purchases: ")
entry_pp = OptionMenu(root,prior_purchase, "1", "2","3", "4","5", "6","7","8","9","10")
entry_pp.config(width=15,font = ("Verdana 12"))
entry_pp.place(x=800,y=360)

#############################
product_imp1 = Label(root, text="what is the product importance? : ",bd=20,width=28,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=500, y=402)
product_imp = StringVar(root)
product_imp.set("product importance: ")
entry_pi = OptionMenu(root, product_imp, "low","medium","high")
entry_pi.config(width=15,font = ("Verdana 12"))
entry_pi.place(x=800,y=400)

#############################
discount1 = Label(root, text="how much discount you got? : ",bd=20,width=28,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=500, y=442)
discount = StringVar(root)
discount.set("discount in dollars: ")
entry_discount = OptionMenu(root, discount,"0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90")
entry_discount.config(width=15,font = ("Verdana 12"))
entry_discount.place(x=800,y=440)
#############################
weight1 = Label(root, text="weight of the product? : ",bd=20,width=26,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=12, y=482)
weight= StringVar(root)
weight.set("weight of product in gms: ")
entry_weight = OptionMenu(root, weight, "0-500","500-1000","1000-1500","1500-2000","2000-2500","2500-3000","3000-3500","3500-4000","4000-4500","4500-5000","5000-5500","5500-6000","6000-6500","6500-7000","7000-7500","7500-8000")
entry_weight.config(width=15,font = ("Verdana 12"))
entry_weight.place(x=300,y=480)
#################
shipment1 = Label(root, text="shipment? : ",bd=20,width=28,  bg="cyan", relief="raised",borderwidth=3,font=("Verdana 12")).place(x=500, y=482)
shipment = StringVar(root)
shipment.set("shipment: ")
entry_shipment = OptionMenu(root,shipment, "Road", "Flight","Ship")
entry_shipment.config(width=15,font = ("Verdana 12"))
entry_shipment.place(x=800,y=480)



#######
#
#adding button
reset = Button(root, text="Reset",command=reset, width=10, background='#671414', activebackground='cornsilk4', foreground='white', bd=8, padx=24, pady=1,font = ("Calibri 12 ")).place(x=300, y=650)
submit = Button(root,text="Predict",command=predict, background='#671414',width=10, activebackground='cornsilk4', foreground='white', bd=8, padx=24, pady=1, font = ("Calibri 12 ")).place(x=500, y=650)





root.mainloop()