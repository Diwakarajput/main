from tkinter import*
import requests
import json

pycrypto=Tk()
pycrypto.title("my crypto portfolio")
def font_color(amount):
    if amount>=0:
        return "green"
    else:
        return "red"
    
def my_portfolio():
    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=c0a9fcab-e111-480b-8a41-e42a55021d23")
    api=json.loads(api_request.content)
    coins=[
        {
            "symbol":"BTC",
            "amount_owned":2,
            "price_per_coin":3200
            },
        {
            "symbol":"ETH",
            "amount_owned":100,
            "price_per_coin":2.75
            }
        ]
    total_pl=0
    coin_row=1
    for i in range(0,300):
        for coin in coins:
            if api["data"][i]["symbol"]==coin["symbol"]:
                total_paid=coin["amount_owned"] * coin["price_per_coin"]
                current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_pl_coin=pl_percoin*coin["amount_owned"]
                total_pl=total_pl+total_pl_coin
                print(api["data"][i]["symbol"])
                print("price",(api["data"][i]["quote"]["USD"]["price"]))
                print("number of coin",coin["amount_owned"])
                print("total amount",(total_paid))
                print("current value","${0:.2f}".format(current_value))
                print("P/L per coin","${0:.2f}".format(pl_percoin))
                print(" total P/L per coin","${0:.2f}".format(total_pl_coin))
               
                name=Label(pycrypto,text=api["data"][i]["symbol"], bg="white", fg="black")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                price=Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="grey", fg="black")
                price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                no_coin=Label(pycrypto,text=coin["amount_owned"],bg="white", fg="black")
                no_coin.grid(row=coin_row,column=2,sticky=N+S+E+W)

                amount_paid=Label(pycrypto,text="${0:.2f}".format(total_paid), bg="grey", fg="black")
                amount_paid.grid(row=coin_row,column=3,sticky=N+S+E+W)

                current_val=Label(pycrypto,text="${0:.2f}".format(current_value), bg="white", fg=font_color(float("{0:.2f}".format(current_value))))
                current_val.grid(row=coin_row,column=4,sticky=N+S+E+W)

                pl_coin=Label(pycrypto,text="${0:.2f}".format(pl_percoin), bg="grey", fg="black")
                pl_coin.grid(row=coin_row,column=5,sticky=N+S+E+W)

                totalpl=Label(pycrypto,text="${0:.2f}".format(total_pl_coin), bg="white", fg="black")
                totalpl.grid(row=coin_row,column=6,sticky=N+S+E+W)
                
                
                
                update=Button(pycrypto,text="update", bg="white", fg="black", command=my_portfolio)
                update.grid(row=coin_row+1,column=6,sticky=N+S+E+W)
                
                
                coin_row=coin_row+1
                
                print(" total P/L ","${0:.2f}".format(total_pl))
                
                
                
                name=Label(pycrypto,text="coin name", bg="#142E54", fg="white",font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
                name.grid(row=0, column=0, sticky=N+S+E+W)

                price=Label(pycrypto,text="price", bg="#142E54", fg="white",font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
                price.grid(row=0,column=1,sticky=N+S+E+W)               

no_coin=Label(pycrypto,text="coin owned", bg="#142E54", fg="white", font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
no_coin.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid=Label(pycrypto,text="total amount paid", bg="#142E54", fg="white", font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_val=Label(pycrypto,text="current value", bg="#142E54", fg="white",font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
current_val.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin=Label(pycrypto,text="P/L per coin", bg="#142E54", fg="white",font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

totalpl=Label(pycrypto,text="total P/L with coin", bg="#142E54", fg="white",font="Lato 12 bold" ,padx="5", pady="5",borderwidth=2,relief="groove")
totalpl.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()
           
               