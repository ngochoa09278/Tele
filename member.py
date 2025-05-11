import telebot
import datetime
import time
import os,sys,re
import subprocess
import requests
import datetime

bot_token = '6595882622:###' 
bot = telebot.TeleBot(bot_token)
processes = []
ADMIN_ID = '#####'

def TimeStamp():
    now = str(datetime.date.today())
    return now

@bot.message_handler(commands=['getkey'])
def startkey(message):
    bot.reply_to(message, text='VUI LÒNG ĐỢI TRONG GIÂY LÁT!')
    key = "hoang" + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    key = "https://key--hoanglo126.repl.co/?key=" + key
    api_token = ''
    url = requests.get(f'https://link4m.co/api-shorten/v2?api={api_token}&url={key}').json()
    url_key = url['shortenedUrl']
    text = f'''
- LINK LẤY KEY {TimeStamp()} LÀ: {url_key} -
- KHI LẤY KEY XONG, DÙNG LỆNH /key <key> ĐỂ TIẾP TỤC -
    '''
    bot.reply_to(message, text)


@bot.message_handler(commands=['key'])
def key(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP KEY.')
        return

    user_id = message.from_user.id

    key = message.text.split()[1]
    username = message.from_user.username
    expected_key = "hoang" + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    if key == expected_key:
        bot.reply_to(message, 'KEY HỢP LỆ. BẠN ĐÃ ĐƯỢC PHÉP SỬ DỤNG LỆNH /spam.')
        fi = open(f'./user/{datetime.date.today().day}/{user_id}.txt',"w")
        fi.write("")
        fi.close()
    else:
        bot.reply_to(message, 'KEY KHÔNG HỢP LỆ.')
@bot.message_handler(commands=['superspam'])
def superspam(message):
  user_id = message.from_user.id
  if not os.path.exists(f"./vip/{user_id}.txt"):
    bot.reply_to(message, 'Bạn chưa đăng ký vip vui lòng liên hệ admin')
    return
  fo = open(f"./vip/{user_id}.txt")
  data = fo.read().split("|")
  qua_khu = data[0].split('-')
  qua_khu = datetime.date(int(qua_khu[0]), int(qua_khu[1]), int(qua_khu[2]))
  ngay_hien_tai = datetime.date.today()
  so_ngay = int((ngay_hien_tai - qua_khu).days)
  if so_ngay < 0:
      bot.reply_to(message, 'Key Vip Cài Vào ngày khác')
      return
  if so_ngay >= int(data[1]):
    bot.reply_to(message, 'Key Vip Hết Hạn Vui Lòng ib Admin ')
    os.remove(f"./vip/{user_id}.txt")
    return
  if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
  if len(message.text.split()) == 2:
    bot.reply_to(message, 'Thiếu dữ kiện !!!')
    return
  lap = message.text.split()[2]
  if not lap.isnumeric():
    bot.reply_to(message,"Sai dữ kiện !!!")
    return
  phone_number = message.text.split()[1]
  if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
    bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
    return
  if phone_number in ["0365956335"]:
    bot.reply_to(message,"Spam cái đầu buồi tao huhu")
    return
  file_path = os.path.join(os.getcwd(), "sms.py")
  process = subprocess.Popen(["python", file_path, phone_number, lap])
  processes.append(process)
  bot.reply_to(message, f'🚀 Gửi Yêu Cầu Tấn Công Thành Công 🚀 \n+ Bot 👾: @Hoanglo126_bot \n+ Số Tấn Công 📱: [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Chủ sở hữu 👑: @hoanglovl\n+ Zalo : https://zalo.me/g/keyysg946\n+ Key : vip')
  
  
  
@bot.message_handler(commands=['spam'])
def spam(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Thiếu dữ kiện !!!')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
      if not (int(lap) > 0 and int(lap) <= 40):
        bot.reply_to(message,"Vui lòng spam trong khoảng 1-40. Nếu nhiều hơn mua vip để sài :))")
        return
    else:
      bot.reply_to(message,"Sai dữ kiện !!!")
      return
    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ["0365956335"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"Spam cái đầu buồi tao huhu")
        return

    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f'🚀 Gửi Yêu Cầu Tấn Công Thành Công 🚀 \n+ Bot 👾: @Hoanglo126_bot \n+ Số Tấn Công 📱: [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Chủ sở hữu 👑: @hoanglovl\n+ Zalo : https://zalo.me/g/keyysg946\n+ Key : free')
  
@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''
Danh sách lệnh:
- /getkey: Lấy key để sử dụng các lệnh.
- /key {key}: Kiểm tra key và xác nhận quyền sử dụng các lệnh.
- /spam {số điện thoại} {so lan}: Gửi tin nhắn SMS Call.
- /superspam {số điện thoại} {so lan}: Gửi tin nhắn SMS Call.(vip)
- /help: Danh sách lệnh.
- /mua : Mua Bot
- /status (admin)
- /restart (admin)
- /stop (admin)
- /them (admin)
'''
    bot.reply_to(message, help_text)
    
# status
@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')



# khoir dong lai bot
@bot.message_handler(commands=['restart'])
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    bot.reply_to(message, 'Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)


# stop chuongw trinhf
@bot.message_handler(commands=['stop'])
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát...')
    time.sleep(2)
    bot.stop_polling()
@bot.message_handler(commands=['them'])
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    idvip = message.text.split(" ")[1]
    ngay = message.text.split(" ")[2]
    hethan = message.text.split(" ")[3]
    fii = open(f"./vip/{idvip}.txt","w")
    fii.write(f"{ngay}|{hethan}")
    bot.reply_to(message, f'Thêm Thành Công {idvip} Làm Vip')

# mua
@bot.message_handler(commands=['mua'])
def mua(message):
    reply_text = 'Giá cả của các gói dịch vụ tất cả đều chát admin:\n\n'
    reply_text += '- Gói /spam: 20k/1 tháng\n'
    reply_text += '- Gói /spam: 60k/6 tháng\n'
    reply_text += '- Gói /spam: 350k/1 năm\n'
    reply_text += '- Gói /spam: 555k/ Không giới hạn\n'
    reply_text += '- Mua suộc bot giống bot 150k Không giới hạn\n'
    bot.reply_to(message, reply_text)


# lenh lo 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh.')

bot.polling()
