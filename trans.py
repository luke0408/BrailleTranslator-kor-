import datetime
import cv2
from PIL import Image
import pytesseract
from jamo import h2j, j2hcj
import matplotlib.pyplot as plt
none = [2, 2, 2, 2, 2, 2]
cㄱ= [0, 0, 0, 1, 0, 0]
cㄴ= [1, 0, 0, 1, 0, 0]
cㄷ= [0, 1, 0, 1, 0, 0]
cㄹ= [0, 0, 0, 0, 1, 0]
cㅁ= [1, 0, 0, 0, 1, 0]
cㅂ= [0, 0, 0, 1, 1, 0]
cㅅ= [0, 0, 0, 0, 0, 1]
cㅇ= [1, 1, 0, 1, 1, 0]
cㅈ= [0, 0, 0, 1, 0, 1]
cㅊ= [0, 0, 0, 0, 1, 1]
cㅋ= [1, 1, 0, 1, 0, 0]
cㅌ= [1, 1, 0, 0, 1, 0]
cㅍ= [1, 0, 0, 1, 1, 0]
cㅎ= [0, 1, 0, 1, 1, 0]
cㄲ= [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
cㄸ= [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
cㅃ= [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0]
cㅆ= [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
cㅉ= [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1]

jㅏ= [1, 1, 0, 0, 0, 1]
jㅑ= [0, 0, 1, 1, 1, 0]
jㅓ= [0, 1, 1, 1, 0, 0]
jㅕ= [1, 0, 0, 0, 1, 1]
jㅗ= [1, 0, 1, 0, 0, 1]
jㅛ= [0, 0, 1, 1, 0, 1]
jㅜ= [1, 0, 1, 1, 0, 0]
jㅠ= [1, 0, 0, 1, 0, 1]
jㅡ= [0, 1, 0, 1, 0, 1]
jㅣ= [1, 0, 1, 0, 1, 0]
jㅐ= [1, 1, 1, 0, 1, 0]
jㅔ= [1, 0, 1, 1, 1, 0]
jㅒ= [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
jㅖ= [0, 0, 1, 1, 0, 0]
jㅘ= [1, 1, 1, 0, 0, 1]
jㅙ= [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0]
jㅚ= [1, 0, 1, 1, 1, 1]
jㅝ= [1, 1, 1, 1, 0, 0]
jㅞ= [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0]
jㅟ= [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0]
jㅢ= [0, 1, 0, 1, 1, 1]

butㄱ= [1, 0, 0, 0, 0, 0]
butㄴ= [0, 1, 0, 0, 1, 0]
butㄷ= [0, 0, 1, 0, 1, 0]
butㄹ= [0, 1, 0, 0, 0, 0]
butㅁ= [0, 1, 0, 0, 0, 1]
butㅂ= [1, 1, 0, 0, 0, 0]
butㅅ= [0, 0, 1, 0, 0, 0]
butㅇ= [0, 1, 1, 0, 1, 1]
butㅈ= [1, 0, 1, 0, 0, 0]
butㅊ= [0, 1, 1, 0, 0, 0]
butㅋ= [0, 1, 1, 0, 1, 0]
butㅌ= [0, 1, 1, 0, 0, 1]
butㅍ= [0, 1, 0, 0, 1, 1]
butㅎ= [0, 0, 1, 0, 1, 1]
butㄲ= [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
butㄳ= [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
butㄵ= [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
butㄶ= [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1]
butㄺ= [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
butㄻ= [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
butㄼ= [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
butㄽ= [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
butㄾ= [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]
butㄿ= [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]
butㅀ= [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
butㅄ= [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
butㅆ= [0, 0, 1, 1, 0, 0]
one= [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
two= [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
three= [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0]
four= [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
five= [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0]
six= [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]
seven= [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
eight= [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
nine= [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0]
zero= [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0]
tchor1 = 0
tchor2 = 0
tchor3 = 0

tjungr1 = 0
tjungr2 = 0
tjungr3 = 0

tjongr1 = 0
tjongr2 = 0
tjongr3 = 0

tjungl1 = 0
tjungl2 = 0
tjungl3 = 0

tjongl1 = 0
tjongl2 = 0
tjongl3 = 0
ek= [0, 1, 0, 0, 0, 0]
dhs= [0, 1, 0, 0, 1, 1]
tmf= [0, 1, 0, 0, 1, 0]
anf= [0, 1, 1, 0, 0, 1]
alx= [0, 0, 1, 0, 0, 1]
sm= [0, 1, 1, 0, 1, 0]
xbdata = []
ybdata = []
xwdata = []
ywdata = []
twoxbdata = []
twoxwdata = []
twoybdata = []
twoywdata = []
f = -1
xy = 0
addnum = 0
twoaddnum = 0
r42 = 42
r41 = 41
r40 = 40
kb = 0
kbc = 0
skif = 15

print("210자 이내의 문장을 입력해주세요:")
text_e = input()
text_f = text_e.replace(' ', '')
lenth = len(text_f)
print(lenth)
print(text_e)
ib = 1
personallist = []
for i in range(0, lenth):
    ibc = text_e[i:ib]
    personallist.insert(i, ibc)
    ib = ib + 1


for k in range(0,lenth):

    jamodata = j2hcj(h2j(personallist[k]))

    cho = jamodata[0:1]
    jung = jamodata[1:2]
    jong = jamodata[2:3]
    if cho == 'ㄱ':
        cho = cㄱ
    elif cho == 'ㄴ':
        cho = cㄴ
    elif cho == 'ㄷ':
        cho = cㄷ
    elif cho == 'ㄹ':
        cho = cㄹ
    elif cho == 'ㅁ':
        cho = cㅁ
    elif cho == 'ㅂ':
        cho = cㅂ
    elif cho == 'ㅅ':
        cho = cㅅ
    elif cho == 'ㅇ':
        cho = cㅇ
    elif cho == 'ㅈ':
        cho = cㅈ
    elif cho == 'ㅊ':
        cho = cㅊ
    elif cho == 'ㅋ':
        cho = cㅋ
    elif cho == 'ㅌ':
        cho = cㅌ
    elif cho == 'ㅍ':
        cho = cㅍ
    elif cho == 'ㅎ':
        cho = cㅎ
    elif cho == '1':
        cho = one
    elif cho == '2':
        cho = two
    elif cho == '3':
        cho = three
    elif cho == '4':
        cho = four
    elif cho == '5':
        cho = five
    elif cho == '6':
        cho = six
    elif cho == '7':
        cho = seven
    elif cho == '8':
        cho = eight
    elif cho == '9':
        cho = nine
    elif cho == '0':
        cho = zero
    elif cho == 'ㄲ':
        cho = cㄲ
    elif cho == 'ㄸ':
        cho = cㄸ
    elif cho == 'ㅃ':
        cho = cㅃ
    elif cho == 'ㅆ':
        cho = cㅆ
    elif cho == 'ㅉ':
        cho = cㅉ
    elif cho == ',':
        cho = ek
    elif cho == '.':
        cho = dhs
    elif cho == '-':
        cho = tmf
    elif cho == '?':
        cho = anf
    elif cho == '_':
        cho = alx
    elif cho == '!':
        cho = sm
    elif cho == 'ㅏ':
        cho = jㅏ
    elif cho == 'ㅑ':
        cho = jㅑ
    elif cho == 'ㅓ':
        cho = jㅓ
    elif cho == 'ㅕ':
        cho = jㅕ
    elif cho == 'ㅗ':
        cho = jㅗ
    elif cho == 'ㅛ':
        cho = jㅛ
    elif cho == 'ㅜ':
        cho = jㅜ
    elif cho == 'ㅠ':
        cho = jㅠ
    elif cho == 'ㅡ':
        cho = jㅡ
    elif cho == 'ㅣ':
        cho = jㅣ
    elif cho == 'ㅐ':
        cho = jㅐ
    elif cho == 'ㅔ':
        cho = jㅔ
    elif cho == 'ㅒ':
        cho = jㅒ
    elif cho == 'ㅖ':
        cho = jㅖ
    elif cho == 'ㅘ':
        cho = jㅘ
    elif cho == 'ㅙ':
        cho = jㅙ
    elif cho == 'ㅚ':
        cho = jㅚ
    elif cho == 'ㅝ':
        cho = jㅝ
    elif cho == 'ㅞ':
        cho = jㅞ
    elif cho == 'ㅟ':
        cho = jㅟ
    elif cho == 'ㅢ':
        cho = jㅢ
    elif cho == 'ㄳ':
        cho = butㄳ
    elif cho == 'ㄵ':
        cho = butㄵ
    elif cho == 'ㄶ':
        cho = butㄶ
    elif cho == 'ㄺ':
        cho = butㄺ
    elif cho == 'ㄻ':
        cho = butㄻ
    elif cho == 'ㄼ':
        cho = butㄼ
    elif cho == 'ㄽ':
        cho = butㄽ
    elif cho == 'ㄾ':
        cho = butㄾ
    elif cho == 'ㅀ':
        cho = butㅀ
    elif cho =='ㅄ':
        cho = butㅄ
    else:
        cho = none

    if jung == 'ㅏ':
        jung = jㅏ
    elif jung == 'ㅑ':
        jung = jㅑ
    elif jung == 'ㅓ':
        jung = jㅓ
    elif jung == 'ㅕ':
        jung = jㅕ
    elif jung == 'ㅗ':
        jung = jㅗ
    elif jung == 'ㅛ':
        jung = jㅛ
    elif jung == 'ㅜ':
        jung = jㅜ
    elif jung == 'ㅠ':
        jung = jㅠ
    elif jung == 'ㅡ':
        jung = jㅡ
    elif jung == 'ㅣ':
        jung = jㅣ
    elif jung == 'ㅐ':
        jung = jㅐ
    elif jung == 'ㅔ':
        jung = jㅔ
    elif jung == 'ㅒ':
        jung = jㅒ
    elif jung == 'ㅖ':
        jung = jㅖ
    elif jung == 'ㅘ':
        jung = jㅘ
    elif jung == 'ㅙ':
        jung = jㅙ
    elif jung == 'ㅚ':
        jung = jㅚ
    elif jung == 'ㅝ':
        jung = jㅝ
    elif jung == 'ㅞ':
        jung = jㅞ
    elif jung == 'ㅟ':
        jung = jㅟ
    elif jung == 'ㅢ':
        jung = jㅢ
    else :
        jung = none

    if jong == 'ㄱ':
        jong = butㄱ
    elif jong == 'ㄴ':
        jong = butㄴ
    elif jong == 'ㄷ':
        jong = butㄷ
    elif jong == 'ㄹ':
        jong = butㄹ
    elif jong == 'ㅁ':
        jong = butㅁ
    elif jong == 'ㅂ':
        jong = butㅂ
    elif jong == 'ㅅ':
        jong = butㅅ
    elif jong == 'ㅇ':
        jong = butㅇ
    elif jong == 'ㅈ':
        jong = butㅈ
    elif jong == 'ㅊ':
        jong = butㅊ
    elif jong == 'ㅋ':
        jong = butㅋ
    elif jong == 'ㅌ':
        jong = butㅌ
    elif jong == 'ㅍ':
        jong = butㅍ
    elif jong == 'ㅎ':
        jong = butㅎ
    elif jong == 'ㄲ':
        jong = butㄲ
    elif jong == 'ㄳ':
        jong = butㄳ
    elif jong == 'ㄵ':
        jong = butㄵ
    elif jong == 'ㄶ':
        jong = butㄶ
    elif jong == 'ㄺ':
        jong = butㄺ
    elif jong == 'ㄻ':
        jong = butㄻ
    elif jong == 'ㄼ':
        jong = butㄼ
    elif jong == 'ㄽ':
        jong = butㄽ
    elif jong == 'ㄾ':
        jong = butㄾ
    elif jong == 'ㅀ':
        jong = butㅀ
    elif jong =='ㅄ':
        jong = butㅄ
    elif jong == 'ㅆ':
        jong = butㅆ
    else:
        jong = none
    chor1 = cho[0]
    chor2 = cho[1]
    chor3 = cho[2]
    chol1 = cho[3]
    chol2 = cho[4]
    chol3 = cho[5]

    if len(cho) >=7:
        tchor1 = cho[6]
        tchor2 = cho[7]
        tchor3 = cho[8]
        tchol1 = cho[9]
        tchol2 = cho[10]
        tchol3 = cho[11]



    jungr1 = jung[0]
    jungr2 = jung[1]
    jungr3 = jung[2]
    jungl1 = jung[3]
    jungl2 = jung[4]
    jungl3 = jung[5]


    if len(jung) >=7:
        tjungr1 = jung[6]
        tjungr2 = jung[7]
        tjungr3 = jung[8]
        tjungl1 = jung[9]
        tjungl2 = jung[10]
        tjungl3 = jung[11]


    jongr1 = jong[0]
    jongr2 = jong[1]
    jongr3 = jong[2]
    jongl1 = jong[3]
    jongl2 = jong[4]
    jongl3 = jong[5]

    if len(jong) >=7:
        tjongr1 = jong[6]
        tjongr2 = jong[7]
        tjongr3 = jong[8]
        tjongl1 = jong[9]
        tjongl2 = jong[10]
        tjongl3 = jong[11]

    choxr = 6 * kb + 1 + addnum
    choxl = 6 * kb + 2 + addnum

    if chor1 == 1:
        xbdata.insert(xy, choxr)
        ybdata.insert(xy, r42)
        xy = xy + 1
    if chor2 == 1:
        xbdata.insert(xy, choxr)
        ybdata.insert(xy, r41)
        xy = xy + 1
    if chor3 == 1:
        xbdata.insert(xy, choxr)
        ybdata.insert(xy, r40)
        xy = xy + 1

    if chol1 == 1:
        xbdata.insert(xy, choxl)
        ybdata.insert(xy, r42)
        xy = xy + 1
    if chol2 == 1:
        xbdata.insert(xy, choxl)
        ybdata.insert(xy, r41)
        xy = xy + 1
    if chol3 == 1:
        xbdata.insert(xy, choxl)
        ybdata.insert(xy, r40)
        xy = xy + 1

    if chor1 == 0:
        xwdata.insert(xy, choxr)
        ywdata.insert(xy, r42)
        xy = xy + 1
    if chor2 == 0:
        xwdata.insert(xy, choxr)
        ywdata.insert(xy, r41)
        xy = xy + 1
    if chor3 == 0:
        xwdata.insert(xy, choxr)
        ywdata.insert(xy, r40)
        xy = xy + 1

    if chol1 == 0:
        xwdata.insert(xy, choxl)
        ywdata.insert(xy, r42)
        xy = xy + 1
    if chol2 == 0:
        xwdata.insert(xy, choxl)
        ywdata.insert(xy, r41)
        xy = xy + 1
    if chol3 == 0:
        xwdata.insert(xy, choxl)
        ywdata.insert(xy, r40)
        xy = xy + 1

    if len(cho) >= 7:
        addnum = addnum + 2
        choxr = choxr + 2
        choxl = choxl + 2
        if tchor1 == 1:
            xbdata.insert(xy, choxr)
            ybdata.insert(xy, r42)
            xy = xy + 1
        if tchor2 == 1:
            xbdata.insert(xy, choxr)
            ybdata.insert(xy, r41)
            xy = xy + 1
        if tchor3 == 1:
            xbdata.insert(xy, choxr)
            ybdata.insert(xy, r40)
            xy = xy + 1

        if tchol1 == 1:
            xbdata.insert(xy, choxl)
            ybdata.insert(xy, r42)
            xy = xy + 1
        if tchol2 == 1:
            xbdata.insert(xy, choxl)
            ybdata.insert(xy, r41)
            xy = xy + 1
        if tchol3 == 1:
            xbdata.insert(xy, choxl)
            ybdata.insert(xy, r40)
            xy = xy + 1

        if tchor1 == 0:
            xwdata.insert(xy, choxr)
            ywdata.insert(xy, r42)
            xy = xy + 1
        if tchor2 == 0:
            xwdata.insert(xy, choxr)
            ywdata.insert(xy, r41)
            xy = xy + 1
        if tchor3 == 0:
            xwdata.insert(xy, choxr)
            ywdata.insert(xy, r40)
            xy = xy + 1

        if tchol1 == 0:
            xwdata.insert(xy, choxl)
            ywdata.insert(xy, r42)
            xy = xy + 1
        if tchol2 == 0:
            xwdata.insert(xy, choxl)
            ywdata.insert(xy, r41)
            xy = xy + 1
        if tchol3 == 0:
            xwdata.insert(xy, choxl)
            ywdata.insert(xy, r40)
            xy = xy + 1

    juxr = 6 * kb + 3 + addnum
    juxl = 6 * kb + 4 + addnum
    if jungr1 == 1:
        xbdata.insert(xy, juxr)
        ybdata.insert(xy, r42)
        xy = xy + 1
    if jungr2 == 1:
        xbdata.insert(xy, juxr)
        ybdata.insert(xy, r41)
        xy = xy + 1
    if jungr3 == 1:
        xbdata.insert(xy, juxr)
        ybdata.insert(xy, r40)
        xy = xy + 1

    if jungl1 == 1:
        xbdata.insert(xy, juxl)
        ybdata.insert(xy, r42)
        xy = xy + 1
    if jungl2 == 1:
        xbdata.insert(xy, juxl)
        ybdata.insert(xy, r41)
        xy = xy + 1
    if jungl3 == 1:
        xbdata.insert(xy, juxl)
        ybdata.insert(xy, r40)
        xy = xy + 1

    if jungr1 == 0:
        xwdata.insert(xy, juxr)
        ywdata.insert(xy, r42)
        xy = xy + 1
    if jungr2 == 0:
        xwdata.insert(xy, juxr)
        ywdata.insert(xy, r41)
        xy = xy + 1
    if jungr3 == 0:
        xwdata.insert(xy, juxr)
        ywdata.insert(xy, r40)
        xy = xy + 1

    if jungl1 == 0:
        xwdata.insert(xy, juxl)
        ywdata.insert(xy, r42)
        xy = xy + 1
    if jungl2 == 0:
        xwdata.insert(xy, juxl)
        ywdata.insert(xy, r41)
        xy = xy + 1
    if jungl3 == 0:
        xwdata.insert(xy, juxl)
        ywdata.insert(xy, r40)
        xy = xy + 1

    if len(jung) >= 7:
        addnum = addnum + 2
        juxr = juxr + 2
        juxl = juxl + 2
        if tjungr1 == 1:
            xbdata.insert(xy, juxr)
            ybdata.insert(xy, r42)
            xy = xy + 1
        if tjungr2 == 1:
            xbdata.insert(xy, juxr)
            ybdata.insert(xy, r41)
            xy = xy + 1
        if tjungr3 == 1:
            xbdata.insert(xy, juxr)
            ybdata.insert(xy, r40)
            xy = xy + 1

        if tjungl1 == 1:
            xbdata.insert(xy, juxl)
            ybdata.insert(xy, r42)
            xy = xy + 1
        if tjungl2 == 1:
            xbdata.insert(xy, juxl)
            ybdata.insert(xy, r41)
            xy = xy + 1
        if tjungl3 == 1:
            xbdata.insert(xy, juxl)
            ybdata.insert(xy, r40)
            xy = xy + 1

        if tjungr1 == 0:
            xwdata.insert(xy, juxr)
            ywdata.insert(xy, r42)
            xy = xy + 1
        if tjungr2 == 0:
            xwdata.insert(xy, juxr)
            ywdata.insert(xy, r41)
            xy = xy + 1
        if tjungr3 == 0:
            xwdata.insert(xy, juxr)
            ywdata.insert(xy, r40)
            xy = xy + 1

        if tjungl1 == 0:
            xwdata.insert(xy, juxl)
            ywdata.insert(xy, r42)
            xy = xy + 1
        if tjungl2 == 0:
            xwdata.insert(xy, juxl)
            ywdata.insert(xy, r41)
            xy = xy + 1
        if tjungl3 == 0:
            xwdata.insert(xy, juxl)
            ywdata.insert(xy, r40)
            xy = xy + 1

    joxr = 6 * kb + 5 + addnum
    joxl = 6 * kb + 6 + addnum
    if jongr1 == 1:
        xbdata.insert(xy, joxr)
        ybdata.insert(xy, r42)
        xy = xy + 1
    if jongr2 == 1:
        xbdata.insert(xy, joxr)
        ybdata.insert(xy, r41)
        xy = xy + 1
    if jongr3 == 1:
        xbdata.insert(xy, joxr)
        ybdata.insert(xy, r40)
        xy = xy + 1

    if jongl1 == 1:
        xbdata.insert(xy, joxl)
        ybdata.insert(xy, r42)
        xy = xy + 1
    if jongl2 == 1:
        xbdata.insert(xy, joxl)
        ybdata.insert(xy, r41)
        xy = xy + 1
    if jongl3 == 1:
        xbdata.insert(xy, joxl)
        ybdata.insert(xy, r40)
        xy = xy + 1

    if jongr1 == 0:
        xwdata.insert(xy, joxr)
        ywdata.insert(xy, r42)
        xy = xy + 1
    if jongr2 == 0:
        xwdata.insert(xy, joxr)
        ywdata.insert(xy, r41)
        xy = xy + 1
    if jongr3 == 0:
        xwdata.insert(xy, joxr)
        ywdata.insert(xy, r40)
        xy = xy + 1

    if jongl1 == 0:
        xwdata.insert(xy, joxl)
        ywdata.insert(xy, r42)
        xy = xy + 1
    if jongl2 == 0:
        xwdata.insert(xy, joxl)
        ywdata.insert(xy, r41)
        xy = xy + 1
    if jongl3 == 0:
        xwdata.insert(xy, joxl)
        ywdata.insert(xy, r40)
        xy = xy + 1

    if len(jong) >= 7:
        addnum = addnum + 2
        joxr = joxr + 2
        joxl = joxl + 2
        if tjongr1 == 1:
            xbdata.insert(xy, joxr)
            ybdata.insert(xy, r42)
            xy = xy + 1
        if tjongr2 == 1:
            xbdata.insert(xy, joxr)
            ybdata.insert(xy, r41)
            xy = xy + 1
        if tjongr3 == 1:
            xbdata.insert(xy, joxr)
            ybdata.insert(xy, r40)
            xy = xy + 1

        if tjongl1 == 1:
            xbdata.insert(xy, joxl)
            ybdata.insert(xy, r42)
            xy = xy + 1
        if tjongl2 == 1:
            xbdata.insert(xy, joxl)
            ybdata.insert(xy, r41)
            xy = xy + 1
        if tjongl3 == 1:
            xbdata.insert(xy, joxl)
            ybdata.insert(xy, r40)
            xy = xy + 1

        if tjongr1 == 0:
            xwdata.insert(xy, joxr)
            ywdata.insert(xy, r42)
            xy = xy + 1
        if tjongr2 == 0:
            xwdata.insert(xy, joxr)
            ywdata.insert(xy, r41)
            xy = xy + 1
        if tjongr3 == 0:
            xwdata.insert(xy, joxr)
            ywdata.insert(xy, r40)
            xy = xy + 1

        if tjongl1 == 0:
            xwdata.insert(xy, joxl)
            ywdata.insert(xy, r42)
            xy = xy + 1
        if tjongl2 == 0:
            xwdata.insert(xy, joxl)
            ywdata.insert(xy, r41)
            xy = xy + 1
        if tjongl3 == 0:
            xwdata.insert(xy, joxl)
            ywdata.insert(xy, r40)
            xy = xy + 1
    kb = kb+1
    if k >= skif:
        kb = 0
        addnum = 0
        r42 = r42 - 3
        r41 = r41 - 3
        r40 = r40 - 3
        kbc = kbc + 1
        skif = skif + 15

figx = [-1, 83]
figy = [-1, 43]
plt.figure(figsize=(12, 12))
plt.scatter(figx, figy, c='w', s=10)
plt.scatter(xbdata, ybdata, c='k', s=10)
plt.scatter(xwdata, ywdata, c='w', s=10)
plt.axis('off')
plt.show()
