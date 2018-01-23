from mapmyfitness import MapMyFitness

z = MapMyFitness(api_key='vd9aadfjcrd6ncae2wx92mc8tm4zfnx2',
                 access_token='21933fbf63aad3d8a49dde82d703fbbff3dbc727')
print z.user.find("self/")
