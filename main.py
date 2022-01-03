from tkinter import *
import requests

#creates gui window -Alex
root = Tk()
var1 = StringVar(root)
var2 = StringVar(root)

#initializes the variables -Alex
var1.set("Currency")
var2.set("Currency")

#function to get real time data from API - Darlin
#Alpha Vantage API
def RealTimeCurrencyConversion():
    from_currency = var1.get()
    to_currency = var2.get()
    api_key = "RKAO2GP95DXBIUJ4"
    #beginning of link
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    #main_url which combines all the variables
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    req_ob = requests.get(main_url)
    #https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CAD&apikey=RKAO2GP95DXBIUJ4

    #result contains list of nested dictionaries
    result = req_ob.json()

    #Takes the exchange rate and changes it from a string to a float
    exchange_rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])

    #Making amount equal whatever value we put in
    amount = float(Amount1_field.get())

    #Converts the amount to the new amount and rounds it to two decimal points
    new_amount = round(amount * exchange_rate, 2)

    #Puts final amount in the bottom box
    Amount2_field.insert(0, str(new_amount))

# Function for clearing the Entry field - Mario
def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)

#global variable that will explicity run the program -Alex
if __name__ == "__main__":
    #sets background color
    root.configure(background='gray50')
    #sets width & height of gui window
    root.geometry("400x200")
    headlabel = Label(root, text="Currency Boyz' Real Time Currency Exchange", fg='black', bg="gray80")
    amtlabel = Label(root, text="Amount: ", fg='black', bg='magenta2')
    fromcurrencylabel = Label(root, text="From Currency: ", fg='black', bg='magenta2')
    tocurrencylabel = Label(root, text="To Currency: ", fg='black', bg='magenta2')
    convertedamtlabel = Label(root, text="Converted Amount: ", fg='black', bg='magenta2')

    # Create a text entry box - Jay & Mario
    #sets placement of labels
    headlabel.grid(row=0, column=1)
    amtlabel.grid(row=1, column=0)
    fromcurrencylabel.grid(row=2, column=0)
    tocurrencylabel.grid(row=3, column=0)
    convertedamtlabel.grid(row=5, column=0)


    # Create a text entry box - Jay & Mario
    # for filling or typing the information.
    Amount1_field = Entry(root)
    Amount2_field = Entry(root)

    # ipadx keyword argument set width of entry space.
    Amount1_field.grid(row=1, column=1, ipadx="25")
    Amount2_field.grid(row=5, column=1, ipadx="25")

    # list of currency codes
    CurrencyCode_list = ["USD", "EUR", "CAD", "GBP", "JPY", "AUD", "RUB", "INR", "MXN"]

    # create a drop down menu using OptionMenu function
    # which takes window name, variable and choices as
    # an argument. use * befor the name of the list,
    # to unpack the values
    FromCurrency_option = OptionMenu(root, var1, *CurrencyCode_list)
    ToCurrency_option = OptionMenu(root, var2, *CurrencyCode_list)

    FromCurrency_option.grid(row=2, column=1, ipadx=10)
    ToCurrency_option.grid(row=3, column=1, ipadx=10)

    # Create a Convert Button and attached
    # with RealTimeCurrencyExchangeRate function
    button1 = Button(root, text="Convert", bg="magenta2", fg="black",command=RealTimeCurrencyConversion)

    button1.grid(row=4, column=1)

    # Create a Clear Button and attached
    # with delete function
    button2 = Button(root, text="Clear", bg="magenta2",fg="black", command=clear_all)
    button2.grid(row=6, column=1)

    # Start the GUI
    root.mainloop()