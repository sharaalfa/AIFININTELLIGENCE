
import ml_otbor as mmmm
import ml_otbor as repo

def rol(oo,y):



    a=mmmm.mmmm(oo,"D1:D2037",11.5,0.00365,
                y,'CLOSE',0.014777,9.36,"C1:C2770",
                'Close',1.41,5.92,0.125,"C1:C1972",1.7)



    return a


def vol(oo,y):


    a=mmmm.mmmm(oo,"E1:E2037",11.5,0.00365,
       y,'VALUE',0.014777,9.36,"D1:D2770",
       'Volume',1.41,5.92,0.125,"D1:D1972",1.7)


    return a



def rprp(oo,y):


    a=repo.repo(oo,
                "A1:A2750","A1:A2060","A1:A2085",
                "A1:A2032",y,'CLOSE')


    return a
