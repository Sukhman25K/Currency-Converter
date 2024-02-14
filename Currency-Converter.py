from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import requests, json
from Constants import API_KEY


Currencies = ['AED-UAE Dirham','AFN-Afghan Afghani','ALL-Albanian Lek',
              'AMD-Armenian Dram','ANG-Netherlands Antillean Gulden',
              'AOA-Angolan Kwanza','ARS-Argentine Peso','AUD-Australian Dollar',
              'AWG-Aruban Florin','AZN-Azerbaijani Manat','BAM-Bosnia And Herzegovina Konvertibilna Marka',
              'BBD-Barbadian Dollar','BDT-Bangladeshi Taka','BGN-Bulgarian Lev',
              'BHD-Bahraini Dinar','BIF-Burundi Franc','BMD-Bermudan Dollar',
              'BND-Brunei Dollar','BOB-Bolivian Boliviano','BRL-Brazilian Real',
              'BSD-Bahamian Dollar','BTC-Bitcoin','BTN-Bhutanese Ngultrum',
              'BWP-Botswana Pula','BYN-New Belarusian Ruble','BYR-Belarusian Ruble',
              'BZD-Belize Dollar','CAD-Canadian Dollar','CDF-Congolese Franc',
              'CHF-Swiss Franc','CLF-Chilean Unit Of Account','CLP-Chilean Peso',
              'CNY-Chinese Yuan','COP-Colombian Peso','CRC-Costa Rican Colon',
              'CUC-Cuban Convertible Peso','CUP-Cuban Peso','CVE-Cape Verdean Escudo',
              'CZK-Czech Koruna','DJF-Djiboutian Franc','DKK-Danish Krone',
              'DOP-Dominican Peso','DZD-Algerian Dinar','EGP-Egyptian Pound',
              'ERN-Eritrean Nakfa','ETB-Ethiopian Birr','EUR-Euro','FJD-Fijian Dollar',
              'FKP-Falkland Islands Pound','GBP-British Pound','GEL-Georgian Lari',
              'GGP-Guernsey Pound','GHS-Ghanaian Cedi','GIP-Gibraltar Pound',
              'GMD-Gambian Dalasi','GNF-Guinean Franc','GTQ-Guatemalan Quetzal',
              'GYD-Guyanese Dollar','HKD-Hong Kong Dollar','HNL-Honduran Lempira',
              'HRK-Croatian Kuna','HTG-Haitian Gourde','HUF-Hungarian Forint',
              'IDR-Indonesian Rupiah','ILS-Israeli New Sheqel','IMP-Manx pound',
              'INR-Indian Rupee','IQD-Iraqi Dinar','IRR-Iranian Rial','ISK-Icelandic Krona',
              'JEP-Jersey Pound','JMD-Jamaican Dollar','JOD-Jordanian Dinar','JPY-Japanese Yen',
              'KES-Kenyan Shilling','KGS-Kyrgyzstani Som','KHR-Cambodian Riel',
              'KMF-Comorian Franc','KPW-North Korean Won','KRW-South Korean Won',
              'KWD-Kuwaiti Dinar','KYD-Cayman Islands Dollar','KZT-Kazakhstani Tenge',
              'LAK-Lao Kip','LBP-Lebanese Lira','LKR-Sri Lankan Rupee',
              'LRD-Liberian Dollar','LSL-Lesotho Loti','LVL-Latvian Lats','LYD-Libyan Dinar',
              'MAD-Moroccan Dirham','MDL-Moldovan Leu','MGA-Malagasy Ariary','MKD-Macedonian Denar',
              'MMK-Myanma Kyat','MNT-Mongolian Tugrik','MOP-Macanese Pataca',
              'MRO-Mauritanian Ouguiya','MUR-Mauritian Rupee','MVR-Maldivian Rufiyaa',
              'MWK-Malawian Kwacha','MXN-Mexican Peso','MYR-Malaysian Ringgit',
              'MZN-Mozambican Metical','NAD-Namibian Dollar','NGN-Nigerian Naira',
              'NIO-Nicaraguan Cordoba','NOK-Norwegian Krone','NPR-Nepalese Rupee',
              'NZD-New Zealand Dollar','OMR-Omani Rial','PAB-Panamanian Balboa',
              'PEN-Peruvian Nuevo Sol','PGK-Papua New Guinean Kina','PHP-Philippine Peso',
              'PKR-Pakistani Rupee','PLN-Polish Zloty','PYG-Paraguayan Guarani',
              'QAR-Qatari Riyal','RON-Romanian Leu','RSD-Serbian Dinar','RUB-Russian Ruble',
              'RWF-Rwandan Franc','SAR-Saudi Riyal','SBD-Solomon Islands Dollar',
              'SCR-Seychellois Rupee','SDG-Sudanese Pound','SEK-Swedish Krona',
              'SGD-Singapore Dollar','SHP-Saint Helena Pound','SLL-Sierra Leonean Leone',
              'SOS-Somali Shilling','SRD-Surinamese Dollar','STD-Sao Tome And Principe Dobra',
              'SVC-Salvadoran Colon','SYP-Syrian Pound','SZL-Swazi Lilangeni',
              'THB-Thai Baht','TJS-Tajikistani Somoni','TMT-Turkmenistan Manat',
              'TND-Tunisian Dinar','TOP-Paanga','TRY-Turkish New Lira',
              'TTD-Trinidad and Tobago Dollar','TWD-New Taiwan Dollar',
              'TZS-Tanzanian Shilling','UAH-Ukrainian Hryvnia','UGX-Ugandan Shilling',
              'USD-United States Dollar','UYU-Uruguayan Peso','UZS-Uzbekistani Som',
              'VEF-Venezuelan Bolivar','VND-Vietnamese Dong','VUV Vanuatu Vatu',
              'WST-Samoan Tala','XAF-Central African','CFA-Franc',
              'XAG-Silver (troy ounce)','XCD-East Caribbean Dollar',
              'XDR-Special Drawing Rights','XOF-West African CFA Franc',
              'XPF-CFP Franc','YER-Yemeni Rial','ZAR-South African Rand',
              'ZMK-Old Zambian Kwacha','ZMW-Zambian Kwacha','ZWL-Zimbabwean Dollar']

class CurrencyConverter():
    def __init__(self,Window):
        self.Window = Window 
        self.WindowDimensions()
        self.CanvasSetUp()
        self.lblTitle = Label(self.Window,text='Currency Convertor',bg='blue',fg='black',font=('algerian',20,'underline')).place(anchor='center',rely=0.1,relx=0.5)
        self.lblAmount = Label(self.Window,text='Amount:',bg='blue',fg='white',font=('Courier New',20)).place(x=100,y=110)
        self.entryAmount = Entry(self.Window,font=('Calibri',16),width=36)
        self.entryAmount.place(x=104,y=150)
        self.lblFrom = Label(self.Window,text='From:',bg='blue',fg='white',font=('Courier New',20)).place(x=100,y=190)
        self.combFirstCurrency = ttk.Combobox(self.Window,values=Currencies,width=34,font=('Calibri',16))
        self.combFirstCurrency.bind('<KeyRelease>',lambda e : self.Search(e,1))
        self.combFirstCurrency.place(x=104,y=240)
        self.lblTo = Label(self.Window,text='To:',bg='blue',fg='white',font=('Courier New',20)).place(x=100,y=280)
        self.combSecondCurrency = ttk.Combobox(self.Window,values=Currencies,width=34,font=('Calibri',16))
        self.combSecondCurrency.bind('<KeyRelease>',lambda e : self.Search(e,2))
        self.combSecondCurrency.place(x=104,y=330)
        self.btnConvert = Button(self.Window,text='Convert',command=self.Convert,bd=0,bg='black',fg='white',activebackground='blue',width=7,font=('Berlin Sans fb demi',20)).place(anchor='center',relx=0.5,rely=0.85)

    def WindowDimensions(self):
        screenWidth = self.Window.winfo_screenwidth()                
        screenHeight = self.Window.winfo_screenheight()                 
        x = (screenWidth - 600) / 2                                   
        y = (screenHeight - 600) / 2
        self.Window.geometry('%dx%d+%d+%d' % (600,600,x,y))
        self.Window.resizable(0,0)

    def CanvasSetUp(self):
        self.BackCanvas = Canvas(Window,background = 'blue',highlightthickness=0)
        self.BackCanvas.place(x=0,y=0,width = 600,height = 600)
    
    def Search(self,event,combobox):
        value = event.widget.get()
        if value == '':
            self.combFirstCurrency['values'] = Currencies
        else:
            Data = []
            for item in Currencies:
                if value.lower() in item.lower():
                    Data.append(item) 
            if combobox == 1:
                self.combFirstCurrency['values'] = Data
            else:
                self.combSecondCurrency['values'] = Data
            

    def Convert(self):
        if self.Validate():
            value = self.API(self.entryAmount.get(),self.combSecondCurrency.get()[0:3],self.combFirstCurrency.get()[0:3])
            data = json.loads(value)
            Amount = data['new_amount']
            self.lblConverted = Label(self.Window,font=('Arial Rounded MT Bold',32),text=(f"{Amount} {self.combSecondCurrency.get().split()[-1]}s"),bg='blue',fg='black').place(anchor='center',rely=0.7,relx=0.5)
  

    def Validate(self):
        if not self.entryAmount.get() or not self.entryAmount.get().isdigit():
            messagebox.showerror('Error','Invalid amount')
            return False
        elif not self.combFirstCurrency.get():
            messagebox.showerror('Error','No initial currency choosed')
            return False
        elif not self.combSecondCurrency.get():
            messagebox.showerror('Error','No currency to be exchanged to choosed')
            return False
        elif self.combSecondCurrency.get() == self.combFirstCurrency.get():
            messagebox.showerror('Error','Same currencies choosed')
            return False
        else:
            return True
        
    def API(self,Amount,FirstCurrency,SecondCurrency):
        api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want={}&have={}&amount={}'.format(FirstCurrency, SecondCurrency, Amount)
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error:", response.status_code, response.text)
            messagebox.showerror('Error','Server problem, try again later')


if __name__ == '__main__':
    Window = Tk()
    CurrencyConv = CurrencyConverter(Window)
    Window.mainloop()
