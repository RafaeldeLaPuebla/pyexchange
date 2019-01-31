from tkinter import *
from tkinter import ttk

currencies = {
    'EUR': 1,
    'USD':0.9,
    'CAD': 0.75
}

#currencies = ['EUR', 'USD', 'CAD'] #me creo variable global para toda la aplicación.
#tipos = [1, 0.9, 0.75]


class CurrencyConverter(ttk.Frame):

    __oldValueinQuantity = None

    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height =args['height'], width=args['width'])#cojo el valor height del diccionario, de todos los que me ofrece el **args

        #Variables de control
        self.inQuantity = DoubleVar(value=0)
        self.__strInQuantity = StringVar(value="") #vamos a controlar que sólo se pueden entrar números y una coma. Es privado porque es sólo para el control interno del entry.
        self.__oldValueinQuantity = '0'
        self.__strInQuantity.trace('w', self.validateQuantity) #cada vez que se produzca una cambio en la escritura, me vas a coger y vas a llamar a validateQuantity y quiero un cambio de escritura.
        self.outQuantity = 0.0
        self.inCurrency = StringVar()
        self.inCurrency.trace('w', self.convertirDivisas)
        self.outCurrency = StringVar()
        self.outCurrency.trace('w', self.convertirDivisas)


        currency_keys = []
        for key in currencies.keys():
            currency_keys.append(key)

        self.inQuantityEntry = ttk.Entry(self, font =('Helvetica', 24, 'bold'), width= 10, textvariable=self.__strInQuantity). place(x=38, y=23) #Es el control de entrada. Lo meto en una variable, en un atributo.
        self.inCurrencyCombo = ttk.Combobox(self, width=10, height=5, values = currencies_keys, textvariable=self.inCurrency).place(x=38, y=71) #Siguiente control. Va a ser un combobox
        ttk.Label(self, text='⥮').place(x=102, y=98)  #Creamos la label. Pero no la asignamos a ninguna variable porque luego no se va a utilizar.
        self.outCurrencyCombo = ttk.Combobox(self, width=10, height=5, values=currencies_keys, textvariable =self.outCurrency).place(x=38, y=120)
        self.outQuantityLabel = ttk.Label(self, width=10, font=('Helvetica', 24), text='0000000000').place(x=38, y=166)


    def convertirDivisas(self):
        _amount = self.__strInQuantity.get()
        _from = self.inCurrency.get()
        _to = self.outCurrency.get()

        resultado = 0
        if amount !="" and _from != "" and _to !="":
            if _to == 'EUR':   #hacer cálculo, llamar a la API y pintar el resultado que devuelve la API
                resultado = float(_amount) * currencies[_from]
            elif _from == 'EUR':
                resultado = float(_amount) / currencies[_to]
            else:
                resultado = float(_amount) * currencies[_from] / currencies[_to]
            
            self.outQuantityLabel.config(text=str(resultado))


    def validateQuantity(self, *args):
        try:
            if self.__strInQuantity.get() !="":
                v = self.__strInQuantity.get() #es el valor de lo que tiene, lo escrito.
                valorParaOld = v #Creamos una variable. Podemos crear todas las variables que necesitemos.
                v = v.replace('.', '@')
                v = v.replace(',', '.')
                float(v)
                self.__oldValueInQuantity = valorParaOld
                self.convertirDivisas
        except:
            self.__strInQuantity.set(self.__oldValueInQuantity) #si el valor no es válido, se queda el valor antes del cambio.



class MainApp(Tk):
    __currencyConverter = None

    def __init__(self):
        Tk.__init__(self)
        self.title("Convertidor de divisas")
        self.geometry("378x229")
        self.__currencyConverter = CurrencyConverter(self, width=378, height=229).place(x=0, y=0) #me creo una instancia de CurrencyConverter

    def start(self):
        self.mainloop()


if __name__ == '__main__': #Creo una instancia de main app
    app = MainApp()
    app.start()
    