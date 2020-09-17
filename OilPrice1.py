#ฟังชั่นแปลงเงินเป็นลิตร
def a1(i):
    # แสดงหน้าจอให้กรอกจำนวนเงิน
    print(tab)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print('#                               กรุณากรอกจำนวนเงิน                              #')
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab)

    #ให้กรอกจำนวนเงิน
    mony = float(input("จำนวนเงิน (บาท) : "))

    # แสดงหน้าจอสรุปผล
    print(tab)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print('#                    จำนวนเงิน ', mony, ' บาท เท่ากับ ', round(mony / i, 2), ' ลิตร                  #')
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab)

#ฟังชั่นแปลงลิตรเป็นเงิน
def a2(i):

    #แสดงหนา้จอให้กรอกจำนวนลิตร
    print(tab)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print('#                               กรุณากรอกจำนวนลิตร                              #')
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab)

    #ให้กรอกจำนวน ลิตร
    mony = float(input("จำนวนลิตร (บาท) : "))

    #แสดงหน้าจอสรุปผล
    print(tab)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print('#                    จำนวน ', mony, ' ลิตร เท่ากับ ', round(mony * i, 2), ' บาท                    #')
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab)


#ฟังชั่นแสดงน้ำมันเชื้อเพลิงทั้งหมด
def menu1() :
    print(tab)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print("#                               ประเภทเชื้อเพลิงและราคา                          #")
    print(tab0)
    print(tab0)
    print("#                        1 Gasoline 95 ราคา 29.16 BAHT                        #")
    print("#                        2 Gasoline 91 ราคา 25.30 BAHT                        #")
    print("#                        3 Gasohol 91 ราคา 21.68 BAHT                         #")
    print("#                        4 Gasohol E20 ราคา 20.2 BAHT                         #")
    print("#                        5 Gasohol 95 ราคา 21.2 BAHT                          #")
    print("#                        6 Diesel ราคา 21.1 BAHT                              #")
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab)

#ฟังชั่นเลือกการทำงาน
def menu2() :
    print(tab)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print("#                               ฟังก์ชั่นการทำงาน                                 #")
    print(tab0)
    print(tab0)
    print("#                           1 คำนวนจากเงินเป็นลิตร                               #")
    print("#                           2 คำนวนจากลิตรเป็นเงิน                               #")
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab0)
    print(tab)

status = 'true'
#สร้างตัวแปร status เพื่อกำหนดเงื่อนไขการทำงานซ้ำของโปรแกรม
tab = "###############################################################################"
#ตัวแปร tab กำหนดความกว้างมาตราฐานของขอบบน
tab0 = "#                                                                             #"

while status != 'exit':
#เงื่อนไขการทำงานซ้ำของโปรแกรมและหยุดการทำงาน
    tp1 = 0
    menu1()
    tp = 0
    status = True
    i=0

    #ตรวจสอบข้อมูลที่ผู้ใช้กรอกเข้ามา
    while not(tp in ['1','2','3','4','5','6']) :
        if tp in ['1','2','3','4','5','6'] and  status == True:
            status = True
        else :
            status = False
            if i > 0 :
                print('False')
        i+=1
        tp = input("กรุณาเลือกชนิดของเชื้อเพลง : ")
    tp = int(tp)
    menu2()
    pt1 = 0

    #ตรวจสอบข้อมูลที่ผู้ใช้กรอกเข้ามา
    while not(pt1 in ['1','2']):
        pt1 = input("กรุณาเลือกฟังชั่นการทำงาน : ")
    pt1 = int(pt1)

    #เงื่อนไขการคำนวนของโปรแกรม
    if tp == 1:
        if pt1 == 1:
            a1(29.16)
        else:
            a2(29.16)
    elif tp == 2:
        if pt1 == 1:
            a1(25.30)
        else:
            a2(25.30)
    elif tp == 3:
        if pt1 == 1:
            a1(21.68)
        else:
            a2(21.68)
    elif tp == 4:
        if pt1 == 1:
            a1(20.2)
        else:
            a2(20.2)
    elif tp == 5:
        if pt1 == 1:
            a1(21.2)
        else:
            a2(21.2)
    else:
        if pt1 == 1:
            a1(21.1)
        else:
            a2(21.1)

    status = input().strip()
    #เปลี่ยนค่าในตัวแปร status เพื่อเข้าเงือนไขการทำงานซ้ำของโปรแกรม
