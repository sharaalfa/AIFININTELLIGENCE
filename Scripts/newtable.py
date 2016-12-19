import perebor as gh
import pandas as pd
kv2 = pd.DataFrame({#'Чистые ошибки и пропуски(С)':gh.gh('Чистые ошибки и пропуски(С)'), #*gh.gh('Чистые ошибки и пропуски(С)'),
                    #'Чистые ошибки и пропуски':gh.gh('Чистые ошибки и пропуски'),#*gh.gh('Чистые ошибки и пропуски'),
                    'Ошибки и пропуски': gh.gh('Ошибки и пропуски'),#*gh.gh('Ошибки и пропуски'),
                    'Абс. чоп':gh.gh('Абс. чоп'),#*gh.gh('Абс. чоп'),
                    #'Индекс сред.':gh.gh('Индекс сред.')*gh.gh('Индекс сред.')*gh.gh('Индекс сред.'),
                    #'Индекс мин':gh.gh('Индекс мин')*gh.gh('Индекс мин')*gh.gh('Индекс мин'),
                    'Индекс макс':gh.gh('Индекс макс'),#*gh.gh('Индекс макс'),#*gh.gh('Индекс макс'),
                    #'Индекс медиана':gh.gh('Индекс медиана')*gh.gh('Индекс медиана')*gh.gh('Индекс медиана'),
                    'РЕПО мин': gh.gh('РЕПО мин'),#*gh.gh('РЕПО мин'),
                    'РЕПО медиана': gh.gh('РЕПО медиана'),#*gh.gh('РЕПО медиана'),
                    #'РЕПО средняя': gh.gh('РЕПО средняя')*gh.gh('РЕПО средняя'),
                    #'РЕПО макс': gh.gh('РЕПО макс')*gh.gh('РЕПО макс'),
                    #'сред. vol':gh.gh('сред. vol')*gh.gh('сред. vol')*gh.gh('сред. vol'),
                    'vol мин':gh.gh('vol мин'),#*gh.gh('vol мин')*gh.gh('vol мин'),
                    'vol макс':gh.gh('vol макс'),#*gh.gh('vol макс')*gh.gh('vol макс'),
                    #'vol медиана':gh.gh('vol медиана')*gh.gh('vol медиана')*gh.gh('vol медиана'),
                    'Прирост чоп(с)':gh.gh('Прирост чоп(с)'),#*gh.gh('Прирост чоп(с)'),
                    'Прирост чоп':gh.gh('Прирост чоп'),#*gh.gh('Прирост чоп'),
                    'Прирост абс чоп(с)': gh.gh('Ошибки и пропуски'),#*gh.gh('Ошибки и пропуски'),
                    'Прирост абс чоп':gh.gh('Абс. чоп'),#*gh.gh('Абс. чоп'),
                    #'Прирост инд сред':
                        #h.gh('Прирост инд сред')*gh.gh('Прирост инд сред')*gh.gh('Прирост инд сред'),
                    #'Прирост инд мин':
                        #gh.gh('Прирост инд мин')*gh.gh('Прирост инд мин')*gh.gh('Прирост инд мин'),
                    'Прирост инд макс':
                        gh.gh('Прирост инд макс'),#*gh.gh('Прирост инд макс'),#*gh.gh('Прирост инд макс'),
                    #'Прирост инд медиана':
                        #gh.gh('Прирост инд медиана')*gh.gh('Прирост инд медиана')*gh.gh('Прирост инд медиана'),
                    #'Прирост сред. vol':
                       # gh.gh('Прирост сред. vol')*gh.gh('Прирост сред. vol')*gh.gh('Прирост сред. vol'),
                    'Прирост vol мин':
                        gh.gh('Прирост vol мин'),#*gh.gh('Прирост vol мин'),#*gh.gh('Прирост vol мин'),
                    'Прирост vol макс':
                        gh.gh('Прирост vol макс'),#*gh.gh('Прирост vol макс'),#*gh.gh('Прирост vol макс'),
                    #'Прирост vol медиана':
                        #gh.gh('Прирост vol медиана')*gh.gh('Прирост vol медиана')*gh.gh('Прирост vol медиана'),
                    #'об макс-мин':gh.gh('об макс-мин')*gh.gh('об макс-мин'),#*gh.gh('об макс-мин'),
                    #'об сред-мин':gh.gh('об сред-мин')*gh.gh('об сред-мин')*gh.gh('об сред-мин'),
                    #'об мед-мин':gh.gh('об мед-мин')*gh.gh('об мед-мин')*gh.gh('об мед-мин'),
                    #'об макс-сред':gh.gh('об макс-сред')*gh.gh('об макс-сред')*gh.gh('об макс-сред'),
                    #'об мед-сред':gh.gh('об мед-сред')*gh.gh('об мед-сред')*gh.gh('об мед-сред'),
                    #'Прирост об макс/мед':
                       # gh.gh('Прирост об макс/мед')*gh.gh('Прирост об макс/мед')*gh.gh('Прирост об макс/мед'),
                    #'Инд макс-мин':gh.gh('Инд макс-мин')*gh.gh('Инд макс-мин')*gh.gh('Инд макс-мин'),
                    #'Инд сред-мин':gh.gh('Инд сред-мин')*gh.gh('Инд сред-мин')*gh.gh('Инд сред-мин'),
                    #'Инд мед-мин':gh.gh('Инд мед-мин')*gh.gh('Инд мед-мин')*gh.gh('Инд мед-мин'),
                    #'Инд макс-сред':gh.gh('Инд макс-сред')*gh.gh('Инд макс-сред')*gh.gh('Инд макс-сред'),
                    #'Прирост макс/мед':
                       # gh.gh('Прирост макс/мед')*gh.gh('Прирост макс/мед')*gh.gh('Прирост макс/мед'),
                    #'Инд макс*мин':gh.gh('Инд макс*мин')*gh.gh('Инд макс*мин')*gh.gh('Инд макс*мин'),
                    #'volmin*indmax':gh.gh('volmin*indmax')*gh.gh('volmin*indmax'),#*gh.gh('volmin*indmax'),
                    #'volmax*indmax':gh.gh('volmax*indmax')*gh.gh('volmax*indmax'),#*gh.gh('volmax*indmax'),
                    'чоп':gh.gh('чоп'),#*gh.gh('чоп'),
                    'чоп(с)':gh.gh('чоп(с)'),#*gh.gh('чоп(с)'),
                    'Р/П чоп(с)':gh.gh('Р/П чоп(с)'),#*gh.gh('Р/П чоп(с)'),
                    'Р/П чоп':gh.gh('Р/П чоп'),#*gh.gh('Р/П чоп'),
                    'Р/П абс чоп(с)': gh.gh('Р/П абс чоп(с)'),#*gh.gh('Р/П абс чоп(с)'),
                    'Р/П абс чоп':gh.gh('Р/П абс чоп'),#*gh.gh('Р/П абс чоп'),
                    #'Р/П Инд сред':gh.gh('Р/П Инд сред')*gh.gh('Р/П Инд сред')*gh.gh('Р/П Инд сред'),
                    'Р/П Индекс мин':gh.gh('Р/П Индекс мин'),#*gh.gh('Р/П Индекс мин')*gh.gh('Р/П Индекс мин'),
                    'Р/П Индекс макс':gh.gh('Р/П Индекс макс'),#*gh.gh('Р/П Индекс макс'),#*gh.gh('Р/П Индекс макс'),
                    'Р/П РЕПО медиана':gh.gh('Р/П РЕПО медиана'),
                    'Р/П РЕПО мин':gh.gh('Р/П РЕПО мин'),
                    #'Р/П Индекс медиана':
                       # gh.gh('Р/П Индекс медиана')*gh.gh('Р/П Индекс медиана')*gh.gh('Р/П Индекс медиана'),
                    #'Р/П сред. vol':gh.gh('Р/П сред. vol')*gh.gh('Р/П сред. vol')*gh.gh('Р/П сред. vol'),
                    'Р/П vol мин':gh.gh('Р/П vol мин'),#*gh.gh('Р/П vol мин'),#*gh.gh('Р/П vol мин'),
                    'Р/П vol макс':gh.gh('Р/П vol макс'),#*gh.gh('Р/П vol макс'),#*gh.gh('Р/П vol макс'),
                    #'Р/П vol медиана':gh.gh('Р/П vol медиана')*gh.gh('Р/П vol медиана')*gh.gh('Р/П vol медиана')
                    })


kv2.to_excel('D:\work\data1\Data_mlv_rost_multireg_perebor.xlsx')