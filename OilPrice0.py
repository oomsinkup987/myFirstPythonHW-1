def a1(i):
    mony = float(input("จำนวนเงิน (บาท) : "))
    print("------------------------------------------------")
    print('จำนวนเงิน ', mony, ' บาท เท่ากับ ', round(mony / i, 2), ' ลิตร')
    print("------------------------------------------------\n")


def a2(i):
    mony = float(input("จำนวนลิตร (บาท) : "))
    print("------------------------------------------------")
    print('จำนวน ', mony, ' ลิตร เท่ากับ ', round(mony * i, 2), ' บาท')
    print("------------------------------------------------\n")


status = 'true'
while status != 'exit':
    tp1 = 0
    print("# ประเภทเชื้อเพลิงและราคา #")
    print("----------------------------------")
    print("1\tGasoline 95 ราคา 29.16 BAHT")
    print("2\tGasoline 91 ราคา 25.30 BAHT")
    print("3\tGasohol 91 ราคา 21.68 BAHT")
    print("4\tGasohol E20 ราคา 20.2 BAHT")
    print("5\tGasohol 95 ราคา 21.2 BAHT")
    print("6\tDiesel ราคา 21.1 BAH")
    print("----------------------------------")
    tp = int(input("กรุณาเลือกชนิดของเชื้อเพลง : "))
    print("#ฟังก์ชั่นการทำงาน #")
    print("------------------------")
    print("1\tคำนวนจากเงินเป็นลิตร")
    print("2\tคำนวนจากลิตรเป็นเงิน")
    print("------------------------")
    pt1 = int(input("กรุณาเลือกฟังชั่นการทำงาน : "))
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