import tst_nugu
import tst_face
import requests

while True:
    condi = tst_face.isSick()

    if condi:
        print('It seems ouccupants is sick')
        nugu_res = tst_nugu.toNUGU()[0]

        if nugu_res:
            print('NUGU RESPONSE')
        else:
            print('EMERGENCY')
            pass
    else:
        print('It is OK')
   

