\* transportationProblem *\
Minimize
OBJ: 10 AndersonAsheville + 8 AndersonCola + 5 AndersonGreenville
 + 4 AndersonMtRest + 15 AndersonPumpkintown + 9 AndersonTR
 + 9 PendletonAsheville + 7 PendletonCola + 6 PendletonGreenville
 + 9999 PendletonMtRest + 11 PendletonPumpkintown + 8 PendletonTR
 + 5 PickensAsheville + 10 PickensCola + 7 PickensGreenville + 8 PickensMtRest
 + 4 PickensPumpkintown + 6 PickensTR + 12 TownsvilleAsheville
 + 9999 TownsvilleCola + 10 TownsvilleGreenville + 6 TownsvilleMtRest
 + 8 TownsvillePumpkintown + 10 TownsvilleTR
Subject To
_C1: 60 PickensCola <= 5000
_C10: AndersonCola + PendletonCola + PickensCola + TownsvilleCola >= 4000
_C2: 60 PickensCola <= 8000
_C3: 60 PickensCola <= 6500
_C4: 60 PickensCola <= 9500
_C5: AndersonPumpkintown + PendletonPumpkintown + PickensPumpkintown
 + TownsvillePumpkintown >= 3000
_C6: AndersonAsheville + PendletonAsheville + PickensAsheville
 + TownsvilleAsheville >= 2500
_C7: AndersonTR + PendletonTR + PickensTR + TownsvilleTR >= 4500
_C8: AndersonGreenville + PendletonGreenville + PickensGreenville
 + TownsvilleGreenville >= 1500
_C9: AndersonMtRest + PendletonMtRest + PickensMtRest + TownsvilleMtRest
 >= 6500
Bounds
0 <= AndersonAsheville
0 <= AndersonCola
0 <= AndersonGreenville
0 <= AndersonMtRest
0 <= AndersonPumpkintown
0 <= AndersonTR
0 <= PendletonAsheville
0 <= PendletonCola
0 <= PendletonGreenville
0 <= PendletonMtRest
0 <= PendletonPumpkintown
0 <= PendletonTR
0 <= PickensAsheville
0 <= PickensCola
0 <= PickensGreenville
0 <= PickensMtRest
0 <= PickensPumpkintown
0 <= PickensTR
0 <= TownsvilleAsheville
0 <= TownsvilleCola
0 <= TownsvilleGreenville
0 <= TownsvilleMtRest
0 <= TownsvillePumpkintown
0 <= TownsvilleTR
Generals
AndersonAsheville
AndersonCola
AndersonGreenville
AndersonMtRest
AndersonPumpkintown
AndersonTR
PendletonAsheville
PendletonCola
PendletonGreenville
PendletonMtRest
PendletonPumpkintown
PendletonTR
PickensAsheville
PickensCola
PickensGreenville
PickensMtRest
PickensPumpkintown
PickensTR
TownsvilleAsheville
TownsvilleCola
TownsvilleGreenville
TownsvilleMtRest
TownsvillePumpkintown
TownsvilleTR
End
