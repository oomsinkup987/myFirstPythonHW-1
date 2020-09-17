
#ฟังชั่นดึงข้อมูลน้ำมันจากเว็บ
def OilPrice():
    from suds.client import Client
    import xmltodict, json
    # pip install xmltodict

    client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
    OilPrice = client.service.CurrentOilPrice(Language='thai')
    OilPrice1 = xmltodict.parse(OilPrice)  # ได้ผลลัพธ์เป็น json ในสตริง
    Price = eval(json.dumps(OilPrice1))  # เรียกใช้งาน json ในสตริง

    data = {}
    #สร้างตัวแปร data เพื่อเก็บข้อมูลราคาน้ำมันที่เป็น list

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

    # ให้กรอกจำนวนเงิน
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
    # แสดงหนา้จอให้กรอกจำนวนลิตร
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

    # ให้กรอกจำนวน ลิตร
    mony = float(input("จำนวนลิตร (บาท) : "))

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
def menu1(data) :
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
    data = OilPrice()
    for n in range(len(data)):
        print(f"#                        {n + 1} {data[n + 1]['product']} ราคา {data[n + 1]['price']} BAHT                        #")
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

data = OilPrice()
#สร้างตัวแปร data เพื่อเก็บข้อมูลที่เป็น list จาก ฟังก์ชั่น oilPrice()


status = 'true'

#ตัวแปร tab กำหนดความกว้างมาตราฐานของขอบบน
tab = "###############################################################################"
tab0 = "#                                                                             #"

while status != 'exit':
    # เงื่อนไขการทำงานซ้ำของโปรแกรมและหยุดการทำงาน
    tp1 = 0
    menu1(data)
    tp = 0
    status = True
    i=0

    # ตรวจสอบข้อมูลที่ผู้ใช้กรอกเข้ามา
    while not(tp in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']) :
        if tp in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14'] and  status == True:
            status = True
        else :
            status = False
            if i > 0 :
                print('ข้อมูลไม่ถูกต้อง')
        i+=1
        tp = input("กรุณาเลือกชนิดของเชื้อเพลง : ")
    tp = int(tp)
    menu2()


    # ตรวจสอบข้อมูลที่ผู้ใช้กรอกเข้ามา
    pt1 = 0
    while not(pt1 in ['1','2']):
        pt1 = input("กรุณาเลือกฟังชั่นการทำงาน : ")
    pt1 = int(pt1)

    # การคำนวนของโปรแกรม
    if pt1 == 1:
        a1(float(data[tp]['price']))
    else:
        a2(float(data[tp]['price']))

    # เปลี่ยนค่าในตัวแปร status เพื่อเข้าเงือนไขการทำงานซ้ำของโปรแกรม
    status = input().strip()
