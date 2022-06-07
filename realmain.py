import datetime
import cv2
from PIL import Image
import pytesseract
from jamo import h2j, j2hcj
none = [0, 0, 0, 0, 0, 0,]
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

ek= [0, 1, 0, 0, 0, 0]
dhs= [0, 1, 0, 0, 1, 1]
tmf= [0, 1, 0, 0, 1, 0]
anf= [0, 1, 1, 0, 0, 1]
alx= [0, 0, 1, 0, 0, 1]
sm= [0, 1, 1, 0, 1, 0]

capture = cv2.VideoCapture(0)

width = int(capture.get(3))  # 가로

height = int(capture.get(4))  # 세로값 가져와서

while (capture.isOpened):

    ret, frame = capture.read()

    if ret == False:
        break

    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    key = cv2.waitKey(33)  # 1) & 0xFF

    if key == 27:  # esc 종료
        cv2.IMREAD_UNCHANGED

        cv2.imwrite("C:/Users/user/PycharmProjects/Tesseract/cap" + ".jpg", frame)
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

        text_d = pytesseract.image_to_string(Image.open('cap.jpg'), lang="kor")

        text_a = text_d[0:-2]
        text_b = text_a.replace(" ", "")
        text_c = text_b.splitlines()
        while '' in text_c:
            text_c.remove('')
        text_e = "".join(text_c)
        lenth = len(text_e)
        ib=1
        personallist = []
        for i in range(0,lenth):
            ibc = text_e[i:ib]
            personallist.insert(i,ibc)
            ib = ib+1
        print(personallist)
        for k in range(0,lenth):

            jamodata = j2hcj(h2j(personallist[k]))
            print(jamodata)
            cho = jamodata[0:1]
            jung = jamodata[1:2]
            jong = jamodata[2:3]
            if cho == 'ㄱ':
                cho = cㄱ
            if cho == 'ㄴ':
                cho = cㄴ
            if cho == 'ㄷ':
                cho = cㄷ
            if cho == 'ㄹ':
                cho = cㄹ
            if cho == 'ㅁ':
                cho = cㅁ
            if cho == 'ㅂ':
                cho = cㅂ
            if cho == 'ㅅ':
                cho = cㅅ
            if cho == 'ㅇ':
                cho = cㅇ
            if cho == 'ㅈ':
                cho = cㅈ
            if cho == 'ㅊ':
                cho = cㅊ
            if cho == 'ㅋ':
                cho = cㅋ
            if cho == 'ㅌ':
                cho = cㅌ
            if cho == 'ㅍ':
                cho = cㅍ
            if cho == 'ㅎ':
                cho = cㅎ
            if cho == '1':
                cho = one
            if cho == '2':
                cho = two
            if cho == '3':
                cho = three
            if cho == '4':
                cho = four
            if cho == '5':
                cho = five
            if cho == '6':
                cho = six
            if cho == '7':
                cho = seven
            if cho == '8':
                cho = eight
            if cho == '9':
                cho = nine
            if cho == '0':
                cho = zero
            if cho == 'ㄲ':
                cho = cㄲ
            if cho == 'ㄸ':
                cho = cㄸ
            if cho == 'ㅃ':
                cho = cㅃ
            if cho == 'ㅆ':
                cho = cㅆ
            if cho == 'ㅉ':
                cho = cㅉ
            if cho == ',':
                cho = ek
            if cho == '.':
                cho = dhs
            if cho == '-':
                cho = tmf
            if cho == '?':
                cho = anf
            if cho == '_':
                cho = alx
            if cho == '!':
                cho = sm
            if cho == '':
                cho = none
            if cho == '1':
                cho = one
            if cho == '2':
                cho = two
            if cho == '3':
                cho = three
            if cho == '4':
                cho = four
            if cho == '5':
                cho = five
            if cho == '6':
                cho = six
            if cho == '7':
                cho = seven
            if cho == '8':
                cho = eight
            if cho == '9':
                cho = nine
            if cho == '0':
                cho = zero
            if cho == 'ㄲ':
                cho = cㄲ
            if cho == 'ㄸ':
                cho = cㄸ
            if cho == 'ㅃ':
                cho = cㅃ
            if cho == 'ㅆ':
                cho = cㅆ
            if cho == 'ㅉ':
                cho = cㅉ
            if cho == ',':
                cho = ek
            if cho == '.':
                cho = dhs
            if cho == '-':
                cho = tmf
            if cho == '?':
                cho = anf
            if cho == '_':
                cho = alx
            if cho == '!':
                cho = sm
            if cho == 'ㅏ':
                cho = jㅏ
            if cho == 'ㅑ':
                cho = jㅑ
            if cho == 'ㅓ':
                cho = jㅓ
            if cho == 'ㅕ':
                cho = jㅕ
            if cho == 'ㅗ':
                cho = jㅗ
            if cho == 'ㅛ':
                cho = jㅛ
            if cho == 'ㅜ':
                cho = jㅜ
            if cho == 'ㅠ':
                cho = jㅠ
            if cho == 'ㅡ':
                cho = jㅡ
            if cho == 'ㅣ':
                cho = jㅣ
            if cho == 'ㅐ':
                cho = jㅐ
            if cho == 'ㅔ':
                cho = jㅔ
            if cho == 'ㅒ':
                cho = jㅒ
            if cho == 'ㅖ':
                cho = jㅖ
            if cho == 'ㅘ':
                cho = jㅘ
            if cho == 'ㅙ':
                cho = jㅙ
            if cho == 'ㅚ':
                cho = jㅚ
            if cho == 'ㅝ':
                cho = jㅝ
            if cho == 'ㅞ':
                cho = jㅞ
            if cho == 'ㅟ':
                cho = jㅟ
            if cho == 'ㅢ':
                cho = jㅢ
            if cho == 'ㄳ':
                cho = butㄳ
            if cho == 'ㄵ':
                cho = butㄵ
            if cho == 'ㄶ':
                cho = butㄶ
            if cho == 'ㄺ':
                cho = butㄺ
            if cho == 'ㄻ':
                cho = butㄻ
            if cho == 'ㄼ':
                cho = butㄼ
            if cho == 'ㄽ':
                cho = butㄽ
            if cho == 'ㄾ':
                cho = butㄾ
            if cho == 'ㅀ':
                cho = butㅀ
            if cho == 'ㅄ':
                cho = butㅄ

            if jung == 'ㅏ':
                jung = jㅏ
            if jung == 'ㅑ':
                jung = jㅑ
            if jung == 'ㅓ':
                jung = jㅓ
            if jung == 'ㅕ':
                jung = jㅕ
            if jung == 'ㅗ':
                jung = jㅗ
            if jung == 'ㅛ':
                jung = jㅛ
            if jung == 'ㅜ':
                jung = jㅜ
            if jung == 'ㅠ':
                jung = jㅠ
            if jung == 'ㅡ':
                jung = jㅡ
            if jung == 'ㅣ':
                jung = jㅣ
            if jung == 'ㅐ':
                jung = jㅐ
            if jung == 'ㅔ':
                jung = jㅔ
            if jung == 'ㅒ':
                jung = jㅒ
            if jung == 'ㅖ':
                jung = jㅖ
            if jung == 'ㅘ':
                jung = jㅘ
            if jung == 'ㅙ':
                jung = jㅙ
            if jung == 'ㅚ':
                jung = jㅚ
            if jung == 'ㅝ':
                jung = jㅝ
            if jung == 'ㅞ':
                jung = jㅞ
            if jung == 'ㅟ':
                jung = jㅟ
            if jung == 'ㅢ':
                jung = jㅢ
            if jung == '':
                jung = none

            if jong == 'ㄱ':
                jong = butㄱ
            if jong == 'ㄴ':
                jong = butㄴ
            if jong == 'ㄷ':
                jong = butㄷ
            if jong == 'ㄹ':
                jong = butㄹ
            if jong == 'ㅁ':
                jong = butㅁ
            if jong == 'ㅂ':
                jong = butㅂ
            if jong == 'ㅅ':
                jong = butㅅ
            if jong == 'ㅇ':
                jong = butㅇ
            if jong == 'ㅈ':
                jong = butㅈ
            if jong == 'ㅊ':
                jong = butㅊ
            if jong == 'ㅋ':
                jong = butㅋ
            if jong == 'ㅌ':
                jong = butㅌ
            if jong == 'ㅍ':
                jong = butㅍ
            if jong == 'ㅎ':
                jong = butㅎ
            if jong == 'ㄲ':
                jong = butㄲ
            if jong == 'ㄳ':
                jong = butㄳ
            if jong == 'ㄵ':
                jong = butㄵ
            if jong == 'ㄶ':
                jong = butㄶ
            if jong == 'ㄺ':
                jong = butㄺ
            if jong == 'ㄻ':
                jong = butㄻ
            if jong == 'ㄼ':
                jong = butㄼ
            if jong == 'ㄽ':
                jong = butㄽ
            if jong == 'ㄾ':
                jong = butㄾ
            if jong == 'ㅀ':
                jong = butㅀ
            if jong =='ㅄ':
                jong = butㅄ
            if jong == 'ㅆ':
                jong = butㅆ
            if jong == '':
                jong = none
            chor1 = cho[0]
            chor2 = cho[1]
            chor3 = cho[2]
            chol1 = cho[3]
            chol2 = cho[4]
            chol3 = cho[5]
            print(chor1, chol1)
            print(chor2, chol2)
            print(chor3, chol3)
            print(' ')
            if len(cho) >=7:
                tchor1 = cho[6]
                tchor2 = cho[7]
                tchor3 = cho[8]
                tchol1 = cho[9]
                tchol2 = cho[10]
                tchol3 = cho[11]
                print(tchor1, tchol1)
                print(tchor2, tchol2)
                print(tchor3, tchol3)
                print(' ')


            jungr1 = jung[0]
            jungr2 = jung[1]
            jungr3 = jung[2]
            jungl1 = jung[3]
            jungl2 = jung[4]
            jungl3 = jung[5]
            print(jungr1, jungl1)
            print(jungr2, jungl2)
            print(jungr3, jungl3)
            print(' ')

            if len(jung) >=7:
                tjungr1 = jung[6]
                tjungr2 = jung[7]
                tjungr3 = jung[8]
                tjungl1 = jung[9]
                tjungl2 = jung[10]
                tjungl3 = jung[11]
                print(tjungr1, tjungl1)
                print(tjungr2, tjungl2)
                print(tjungr3, tjungl3)
                print(' ')

            jongr1 = jong[0]
            jongr2 = jong[1]
            jongr3 = jong[2]
            jongl1 = jong[3]
            jongl2 = jong[4]
            jongl3 = jong[5]
            print(jongr1, jongl1)
            print(jongr2, jongl2)
            print(jongr3, jongl3)
            print(' ')
            if len(jong) >=7:
                tjongr1 = jong[6]
                tjongr2 = jong[7]
                tjongr3 = jong[8]
                tjongl1 = jong[9]
                tjongl2 = jong[10]
                tjongl3 = jong[11]
                print(tjongr1, tjongl1)
                print(tjongr2, tjongl2)
                print(tjongr3, tjongl3)
                print(' ')









    if key == 26:  # ctrl + z

        break
capture.release()

cv2.destroyAllWindows()