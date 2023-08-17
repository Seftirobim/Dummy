import time,os,datetime
utc_now = datetime.datetime.utcnow()
indonesia_offset = datetime.timedelta(hours=7)
indonesia_time = utc_now + indonesia_offset

def drawLine(symbol):
    rows, columns = os.get_terminal_size()
    i = symbol
    for x in range(2, rows):
        i += symbol
    return i

def clearTerminal() :

   if os.name == "nt" :
      return os.system("cls")
   elif os.name == "posix" or os.name == "macOS" :
      return os.system("clear")

print(f"Waktu sekarang di Indonesia {indonesia_time.hour}:{indonesia_time.minute}")
print(drawLine("="))
print("Masukan waktu Menyala (format 24 jam)")
print(drawLine("="))
jam_nyala = int(input("Masukan Jam : "))
min_nyala = int(input("Masukan Menit : "))
clearTerminal()

print(drawLine("="))
print("Masukan waktu Mati (format 24 jam)")
print(drawLine("="))
jam_mati = int(input("Masukan Jam : "))
min_mati = int(input("Masukan Menit : "))
clearTerminal()


print_nyala = f"Jam Nyala : {str(jam_nyala)}:0{str(min_nyala)}" if len(str(min_nyala)) == 1 else f"Jam Nyala : {str(jam_nyala)}:{str(min_nyala)}"
print_mati = f"Jam Mati : {str(jam_mati)}:0{str(min_mati)}" if len(str(min_mati)) == 1 else f"Jam Mati : {str(jam_mati)}:{str(min_mati)}"

def title() :
   print("Setting waktu (format 24 jam)")
   print(drawLine("-"))
   print(print_nyala)
   print(print_mati)
   print(drawLine("="))

title()
print("Tunggu .......")

while True :
    utc_now = datetime.datetime.utcnow()
    indonesia_offset = datetime.timedelta(hours=7)
    indonesia_time = utc_now + indonesia_offset
    jam = indonesia_time.hour
    menit = indonesia_time.minute
    print_status_nyala = f"Lampu sudah Nyala jam : [{str(jam)}:0{str(menit)}]" if len(str(min_nyala)) == 1 else f"Lampu sudah nyala jam : [{str(jam)}:{str(menit)}]"
    print_status_mati = f"Lampu sudah Mati jam : [{str(jam)}:0{str(menit)}]" if len(str(min_mati)) == 1 else f"Lampu sudah mati jam : [{str(jam)}:{str(menit)}]"
    if jam == jam_nyala and menit == min_nyala:
       clearTerminal()
       title()
       print(print_status_nyala)
       print("Menunggu waktu berikutnya....")
    elif jam == jam_mati and menit == min_mati:
       clearTerminal()
       title()
       print(print_status_mati)
       print("Menunggu waktu berikutnya....")
    else:
       pass
    time.sleep(1)
