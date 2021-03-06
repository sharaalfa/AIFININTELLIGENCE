import rost as b1
import rost as b
import rost as b2
import pandas as pd
from pylab import *
kv2 = pd.DataFrame({'Чистые ошибки и пропуски(С)':b1.b1('Чистые ошибки и пропуски(С)'),
                    'Чистые ошибки и пропуски':b1.b1('Чистые ошибки и пропуски'),
                    'Ошибки и пропуски': b1.b1('Ошибки и пропуски'),
                    'Абс. чоп':b1.b1('Абс. чоп'),
                    #'Индекс сред.':b1.b1('Индекс сред.'),
                    'Индекс мин':b1.b1('Индекс мин'),
                    'Индекс макс':b1.b1('Индекс макс'),
                    #'Индекс медиана':b1.b1('Индекс медиана'),
                    'РЕПО мин': b1.b1('РЕПО мин'),
                    'РЕПО медиана': b1.b1('РЕПО медиана'),
                    'РЕПО средняя': b1.b1('РЕПО средняя'),
                    'РЕПО макс': b1.b1('РЕПО макс'),
                    #'сред. vol':b1.b1('сред. vol'),
                    'vol мин':b1.b1('vol мин'),
                    'vol макс':b1.b1('vol макс'),
                    #'vol медиана':b1.b1('vol медиана'),
                    'Прирост чоп(с)':b2.b2('Чистые ошибки и пропуски(С)'),
                    'Прирост чоп':b2.b2('Чистые ошибки и пропуски'),
                    'Прирост абс чоп(с)': b2.b2('Ошибки и пропуски'),
                    'Прирост абс чоп':b2.b2('Абс. чоп'),
                    #'Прирост инд сред':b2.b2('Индекс сред.'),
                    'Прирост инд мин':b2.b2('Индекс мин'),
                    'Прирост инд макс':b2.b2('Индекс макс'),
                    'Прирост РЕПО медиана':b2.b2('РЕПО медиана'),
                    'Прирост РЕПО мин':b2.b2('РЕПО мин'),
                    #'Прирост инд медиана':b2.b2('Индекс медиана'),
                    #'Прирост сред. vol':b2.b2('сред. vol'),
                    'Прирост vol мин':b2.b2('vol мин'),
                    'Прирост vol макс':b2.b2('vol макс'),
                    #'Прирост vol медиана':b2.b2('vol медиана'),
                    'об макс-мин':b1.b1('vol макс')-b1.b1('vol мин'),
                    'РЕПО мед-мин':b1.b1('РЕПО медиана')-b1.b1('РЕПО мин'),
                    #'об сред-мин':b1.b1('сред. vol')-b1.b1('vol мин'),
                    #'об мед-мин':b1.b1('vol медиана')-b1.b1('vol мин'),
                    #'об макс-сред':b1.b1('vol макс')-b1.b1('сред. vol'),
                    #'об мед-сред':b1.b1('vol медиана')-b1.b1('сред. vol'),
                    #'Прирост об макс/мед':b1.b1('vol макс')-b1.b1('vol медиана')/b1.b1('vol медиана'),
                    'Инд макс-мин':b1.b1('Индекс макс')-b1.b1('Индекс мин'),
                    #'Инд сред-мин':b1.b1('Индекс сред.')-b1.b1('Индекс мин'),
                    #'Инд мед-мин':b1.b1('vol медиана')-b1.b1('Индекс мин'),
                    #'Инд макс-сред':b1.b1('Индекс макс')-b1.b1('Индекс сред.'),
                    #'Прирост макс/мед':b1.b1('Индекс макс')-b1.b1('Индекс медиана')/b1.b1('Индекс медиана'),
                    'Инд макс*мин':b1.b1('Индекс макс')*b1.b1('Индекс мин'),
                    'volmin*indmax':b1.b1('vol мин')*b1.b1('Индекс макс'),
                    'volmax*indmax':b1.b1('vol макс')*b1.b1('Индекс макс'),
                    'чоп':b1.b1('Чистые ошибки и пропуски')/b1.b1('Абс. чоп'),
                    'чоп(с)':b1.b1('Чистые ошибки и пропуски(С)')/b1.b1('Ошибки и пропуски'),
                    'Р/П чоп(с)':b.b('Чистые ошибки и пропуски(С)')/abs(b.b('Чистые ошибки и пропуски(С)')),
                    'Р/П чоп':b.b('Чистые ошибки и пропуски')/abs(b.b('Чистые ошибки и пропуски')),
                    'Р/П абс чоп(с)': b.b('Ошибки и пропуски')/abs(b.b('Ошибки и пропуски')),
                    'Р/П абс чоп':b.b('Абс. чоп')/abs(b.b('Абс. чоп')),
                    #'Р/П Инд сред':b.b('Индекс сред.')/abs(b.b('Индекс сред.')),
                    'Р/П Индекс мин':b.b('Индекс мин')/abs(b.b('Индекс мин')),
                    'Р/П Индекс макс':b.b('Индекс макс')/abs(b.b('Индекс макс')),
                    'Р/П РЕПО медиана':b.b('РЕПО медиана')/abs(b.b('РЕПО медиана')),
                    'Р/П РЕПО мин':b.b('РЕПО мин')/abs(b.b('РЕПО мин')),
                    #'Р/П Индекс медиана':b.b('Индекс медиана')/abs(b.b('Индекс медиана')),
                    #'Р/П сред. vol':b.b('сред. vol')/abs(b.b('сред. vol')),
                    'Р/П vol мин':b.b('vol мин')/abs(b.b('vol мин')),
                    'Р/П vol макс':b.b('vol макс')/abs(b.b('vol макс')),
                    #'Р/П vol медиана':b.b('vol медиана')/abs(b.b('vol медиана'))
                    })



kv2.to_excel('D:\work\data1\Data_mlv_rost_multireg.xlsx')

def polyfit(x, y, degree):
    results={}

    coeffs=np.polyfit(x, y, degree)
     # Polynominal Coefficients
    results['polynominal']=coeffs.tolist()

   # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results



a = b1.b1('Ошибки и пропуски')
b = b1.b1('Индекс макс')



print(polyfit(b, a, 10))

