# ฟังชั่นแสดงผลหน้าจออัตโนมัติ
def display_auto(lists):

    def Square(col):
        for i in range(col):
            print("#", end='')
    print('')

    def Space(col):
        col = col-2
        print('#', end='')
        for i in range(col):
            print(" ", end='')
        print('#')

    def print_line(line, col):
        line_print = line
        GasNameLength = len(line_print)
        print('#', end='')
        startSpace = col//2 - 1 - len(line_print)
        endSpace = col - 2 - startSpace - GasNameLength
        for i in range(startSpace):
            print(" ", end='')
        print(line_print, end='')
        for i in range(endSpace):
            print(" ", end='')
        print('#')

    def printOilMenu(data, spaceItemsUpper, spaceItemsLower, col, row):
        Square(col)
        for i in range(spaceItemsUpper):
            Space(col)
        j = 0
        for i in data:
            print_line(i, col)
            j += 1
        for i in range(spaceItemsLower):
            Space(col)

        Square(col)

    def main(lists):
        import shutil
        cols, rows = shutil.get_terminal_size()
        row = int(rows)
        col = int(cols)
        productItems = len(lists)
        spaceItems1 = row - 2 - productItems
        spaceItemsUpper = spaceItems1//2
        spaceItemsLower = row - 2 - spaceItemsUpper - productItems - 1
        printOilMenu(lists, spaceItemsUpper, spaceItemsLower, col, row)
    main(lists)

# ฟังชั่นดึงข้อมูลน้ำมันจากเว็บ


def OilPrice():
    from suds.client import Client
    import xmltodict
    import json
    # pip install xmltodict

    client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
    OilPrice = client.service.CurrentOilPrice(Language='thai')
    OilPrice1 = xmltodict.parse(OilPrice)  # ได้ผลลัพธ์เป็น json ในสตริง
    Price = eval(json.dumps(OilPrice1))  # เรียกใช้งาน json ในสตริง

    data = {}
    # สร้างตัวแปร data เพื่อเก็บข้อมูลราคาน้ำมันที่เป็น list
    for i in range(len(Price['PTTOR_DS']['FUEL'])):
        # print(Price['PTTOR_DS']['FUEL'][i])
        if len(Price['PTTOR_DS']['FUEL'][i]) == 3:
            data[i + 1] = {
                'product': Price['PTTOR_DS']['FUEL'][i]['PRODUCT'],
                'price': Price['PTTOR_DS']['FUEL'][i]['PRICE']
            }
        else:
            data[i + 1] = {
                'product': Price['PTTOR_DS']['FUEL'][i]['PRODUCT'],
                'price': 25.30
            }
    return data
# ฟังชั่นแปลงเงินเป็นลิตร


def a1(i):
    # แสดงหน้าจอให้กรอกจำนวนเงิน
    lists = [
        'กรุณากรอกจำนวนเงิน',
    ]
    display_auto(lists)

    # ให้กรอกจำนวนเงิน
    mony = float(input("จำนวนเงิน (บาท) : "))

    # แสดงหน้าจอสรุปผล
    lists = [
        'จำนวนเงิน {} บาท เท่ากับ {} ลิตร'.format(mony, round(mony / i, 2))
    ]
    display_auto(lists)


# ฟังชั่นแปลงลิตรเป็นเงิน
def a2(i):
    # แสดงหนา้จอให้กรอกจำนวนลิตร
    lists = [
        'กรุณากรอกจำนวนลิตร',
    ]
    display_auto(lists)

    # ให้กรอกจำนวน ลิตร
    mony = float(input("จำนวนลิตร (บาท) : "))

    # แสดงหน้าจอสรุปผล
    lists = [
        'กรุณากรอกจำนวนลิตร',
        "จำนวน {}  ลิตร เท่ากับ {} บาท".format(mony, round(mony * i, 2))
    ]
    display_auto(lists)


# ฟังชั่นแสดงน้ำมันเชื้อเพลิงทั้งหมด
def menu1(data):

    data = OilPrice()
    lists = [
        'ประเภทเชื้อเพลิงและราคา',
    ]
    for n in range(len(data)):
        lists.append(
            f"{n + 1} {data[n + 1]['product']} ราคา {data[n + 1]['price']} BAHT")
    display_auto(lists)

# ฟังชั่นเลือกการทำงาน


def menu2():
    lists = [
        'ฟังก์ชั่นการทำงาน',
        '1 คำนวนจากเงินเป็นลิตร ',
        '2 คำนวนจากลิตรเป็นเงิน'
    ]
    display_auto(lists)


data = OilPrice()
# สร้างตัวแปร data เพื่อเก็บข้อมูลที่เป็น list จาก ฟังก์ชั่น oilPrice()


status = 'true'

# ตัวแปร tab กำหนดความกว้างมาตราฐานของขอบบน

while status != 'exit':
    # เงื่อนไขการทำงานซ้ำของโปรแกรมและหยุดการทำงาน
    tp1 = 0
    menu1(data)
    tp = 0
    status = True
    i = 0

    # ตรวจสอบข้อมูลที่ผู้ใช้กรอกเข้ามา
    while not(tp in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']):
        if tp in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'] and status == True:
            status = True
        else:
            status = False
            if i > 0:
                print('ข้อมูลไม่ถูกต้อง')
        i += 1
        tp = input("กรุณาเลือกชนิดของเชื้อเพลง : ")
    tp = int(tp)
    menu2()
    pt1 = 0

    # ตรวจสอบข้อมูลที่ผู้ใช้กรอกเข้ามา
    while not(pt1 in ['1', '2']):
        pt1 = input("กรุณาเลือกฟังชั่นการทำงาน : ")
    pt1 = int(pt1)

    # การคำนวนของโปรแกรม
    if pt1 == 1:
        a1(float(data[tp]['price']))
    else:
        a2(float(data[tp]['price']))

    # เปลี่ยนค่าในตัวแปร status เพื่อเข้าเงือนไขการทำงานซ้ำของโปรแกรม
    status = input().strip()
