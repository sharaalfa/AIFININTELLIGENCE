import perebor as gh
import pandas as pd
kv2 = pd.DataFrame({'Чистые ошибки и пропуски(С)':gh.gh('Чистые ошибки и пропуски(С)'),
                    'Чистые ошибки и пропуски':gh.gh('Чистые ошибки и пропуски'),
                    'Ошибки и пропуски': gh.gh('Ошибки и пропуски'),
                    'Абс. чоп':gh.gh('Абс. чоп'),
                    'Индекс сред.':gh.gh('Индекс сред.'),
                    'Индекс мин':gh.gh('Индекс мин'),
                    'Индекс макс':gh.gh('Индекс макс'),
                    'Индекс медиана':gh.gh('Индекс медиана'),
                    '1':gh.gh('Индекс макс')-gh.gh('Индекс мин'),
                    '2':gh.gh('Индекс сред.')-gh.gh('Индекс мин'),
                    '3':gh.gh('Индекс медиана')-gh.gh('Индекс мин'),
                    '4':gh.gh('Индекс макс')-gh.gh('Индекс сред.'),
                    '5':gh.gh('Индекс медиана')-gh.gh('Индекс сред.'),
                    '6':gh.gh('Индекс макс')-gh.gh('Индекс медиана'),
                    '7':(gh.gh('Индекс макс')-gh.gh('Индекс мин'))/gh.gh('Индекс мин'),
                    '8':(gh.gh('Индекс сред.')-gh.gh('Индекс мин'))/gh.gh('Индекс мин'),
                    '9':(gh.gh('Индекс медиана')-gh.gh('Индекс мин'))/gh.gh('Индекс мин'),
                    '10':(gh.gh('Индекс макс')-gh.gh('Индекс сред.'))/gh.gh('Индекс сред.'),
                    '11':(gh.gh('Индекс медиана')-gh.gh('Индекс сред.'))/gh.gh('Индекс сред.'),
                    '12':gh.gh('Индекс макс')-gh.gh('Индекс медиана')/gh.gh('Индекс медиана'),
                    '13':gh.gh('Индекс медиана')+gh.gh('Индекс макс')
                         +gh.gh('Индекс мин')+gh.gh('Индекс сред.'),
                    '14':(gh.gh('Индекс мин')+gh.gh('Индекс макс'))/gh.gh('Индекс сред.'),
                    '15':(gh.gh('Индекс мин')+gh.gh('Индекс макс'))/gh.gh('Индекс медиана'),
                    '16':gh.gh('Индекс макс')/gh.gh('Индекс мин'),
                    '17':gh.gh('Индекс медиана')/gh.gh('Индекс мин'),
                    '18':gh.gh('Индекс сред.')/gh.gh('Индекс мин'),
                    '19':gh.gh('Индекс макс')/gh.gh('Индекс сред.'),
                    '20':gh.gh('Индекс медиана')/gh.gh('Индекс сред.'),
                    '21':gh.gh('Индекс макс')/gh.gh('Индекс медиана'),
                    '22':gh.gh('Индекс макс')*gh.gh('Индекс мин'),
                    'neo':gh.gh('Чистые ошибки и пропуски')/gh.gh('Абс. чоп'),
                    'neo+':gh.gh('Чистые ошибки и пропуски(С)')/gh.gh('Ошибки и пропуски'),
                    'neo-':gh.gh('Чистые ошибки и пропуски')-gh.gh('Абс. чоп'),
                    'neo+-':gh.gh('Чистые ошибки и пропуски(С)')-gh.gh('Ошибки и пропуски'),
                    'neo-/':(gh.gh('Чистые ошибки и пропуски')-gh.gh('Абс. чоп'))/gh.gh('Абс. чоп'),
                    'neo+-/':(gh.gh('Чистые ошибки и пропуски(С)')-gh.gh('Ошибки и пропуски'))
                             /gh.gh('Ошибки и пропуски')
                    })


kv2.to_excel('D:\work\data\Data_mod_sum+++.xlsx')