from tkinter import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

# import ws
# from ws import webscraper



def outp():




 def getlink():
  global url3
  url3 = url_entry.get()
  print(url3)
  webscraper(url3)



 window=tk.Tk()
 window.title("Output Panel")
 window.configure(bg='light blue')
#window.eval('tk::PlaceWindow . center')
 window.geometry('900x500')





 url_label=ttk.Label(window,text='Enter the URL:', font='lato 13 bold', relief='ridge')
 url_label.grid(row=1, column= 2, padx=5, pady= 10)
 url_entry=ttk.Entry(window, width= 70)



 url_entry.grid(row=1, column= 3, pady=10, padx=0)


 inf_label=ttk.Label(window,width=45, text='Pls enter the link of page presenting all products', font='lato 12 bold', relief='sunken')
 inf_label.grid(row=2, column=3, pady=5, padx= 5)

 option1 = tk.Radiobutton(window, width=7, text="Amazon", value=1)
 option1.grid(row=4, column=2, pady= 10, padx=0 )
 option2 = tk.Radiobutton(window, width=7,text="Flipkart", value=2)
 option2.grid(row=5, column=2, pady=10, padx=0)
 option3 = tk.Radiobutton(window,width=7, text="other", value=3)
 option3.grid(row=6, column=2, pady=10, padx=0)

 output_panel1= tk.Text(window, width=30)
 output_panel1.config(state='disabled')
 output_panel1.grid(row=9, column=1, columnspan=2, pady= 5,padx= 0)



 output_panel2 = tk.Text(window, width=10)
 output_panel2.grid(row=9, column=2, columnspan=2, pady=5, padx=0)

 output_panel3 = tk.Text(window, width=10)
 output_panel3.grid(row=9, column=3, columnspan=2, pady=5, padx=0)




 login_button = ttk.Button(window, style='', text="Proceed", command=getlink)
 style = ttk.Style()

 style.configure("Custom.TButton", font=("arial", 14, "bold",))
 login_button.grid(row=5, column=2, columnspan=2, pady=5, padx=2)



 window.mainloop()





import bs4
from bs4 import BeautifulSoup
import pandas as pd





import requests
def webscraper(url3):






 # url = 'https://www.amazon.in/s?k=gaming+laptop&crid=153EKVYN0DW3L&sprefix=gaming+%2Caps%2C375&ref=nb_sb_ss_ts-doa-p_2_7'
 # url2 = 'https://www.amazon.in/s?k=sport+shoes&crid=3DA21Z8GZTEHH&sprefix=sport+shoes%2Caps%2C402&ref=nb_sb_noss_1'

 url= url3
 r = requests.get(url)



#print(r)  response 503

 HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36', 'Accept-language': 'en-Us, en;q=0.5'})
 r = requests.get(url, headers=HEADERS)
 print(r) # https request was successful <Response[200]>
 soup = BeautifulSoup(r.content, 'html.parser')
 links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal','target' : '_blank'})
 i=0
#print("the string of links is",links)

 links.append(None)    #to iterate unti it reaches none;

 product_list=[]
 link=''

 while(links[i]!=None):
  link=links[i].get('href')       #gets you one link, similar to string slice option

  product_list.insert(i, "https://www.amazon.in"+ link) #[i] = "https://www.amazon.in"+ link   #appends that string to original link[0] as it dosent contains that
  i=i+1

 print("the product list is as follows:",product_list)  #same page check for amazon


 product_title=[]    #declarations for the csv file addition
 product_price=[]
 product_review=[]
 i=0


 while(i!=15):
  new_r = requests.get(product_list[i], headers=HEADERS)
 #print(new_r)   #response 200
  new_soup = BeautifulSoup(new_r.content, "html.parser")


  product_title.insert(i, new_soup.find("span", attrs={"id":"productTitle"}))
  if(product_title[i]!=None):
    product_title[i]=product_title[i].text.strip()
  print(product_title[i])


  product_price.insert(i, new_soup.find("span", attrs={"class":"a-price-whole"}))    #to handle duplicates .find("span"
  if (product_price[i] != None):
    product_price[i] = product_price[i].text.strip()
  print(product_price[i])



  product_review.insert(i,new_soup.find("span", attrs={"class":"a-icon-alt"}))
  if (product_review[i] != None):
    product_review[i] = product_review[i].text.strip()
  print(product_review[i])
  i=i+1


 # final=tk.Tk()
 # output_panel1 = tk.Text(final, width=30, font='5')
 # output_panel1.config(state='disabled')
 # output_panel1.grid(row=9, column=1, columnspan=2, pady=5, padx=0)
 #
 # for item in product_title:
 #  output_panel1.config(state='normal')
 #  output_panel1.insert(tk.END, str(item)+ "\n")
 #  output_panel1.config(state='disabled')
 #
 # output_panel2 = tk.Text(final, width=10)
 # output_panel2.grid(row=9, column=2, columnspan=2, pady=5, padx=0)
 #
 # output_panel3 = tk.Text(final, width=10)
 # output_panel3.grid(row=9, column=3, columnspan=2, pady=5, padx=0)
 #
 #
 #
 # final.mainloop()
 dbms=str(input("do you wish to continue?"))

 if(dbms=='yes'):
  columns=['Product title', 'Product Price', 'Product Review']
  dataf=pd.DataFrame(list(zip(product_title, product_price, product_review)), columns=columns)
  print(dataf)
  dataf.to_csv('GamingLTamazon.csv')
