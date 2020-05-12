import time
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import pyautogui as pag
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

monthes ={
'01':'января','02':'февраля','03':'марта','04':'апреля','05':'мая','06':'июня','07':'июля','08':'августа','09':'сентября','10':'октября','11':'ноября','12':'декабря'
}
letters = {
'q':'й','w':'ц','e':'у','r':'к','t':'е','y':'н','u':'г','i':'ш','o':'щ','p':'з','[':'х',']':'ъ','a':'ф','s':'ы','d':'в','f':'а','g':'п','h':'р','j':'о','k':'л','l':'д',';':'ж',"'":'э','z':'я','x':'ч','c':'с','v':'м','b':'и','n':'т','m':'ь',',':'б','.':'ю',' ':' '
}
commands = {
    "vasya": ('вася','васечка','васюня','василий','василиса'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "calc": ('сколько будет','посчитай'),
    "open": ('открой','запусти','включи'),
    "google": ('загугли','найди в гугле','найди в гугле что такое', 'поищи в гугле слово', 'забей в гугле что такое', 'забей в гугле','что такое'),
    "ctime": ('текущее время','сколько сейчас времени','сколько времени','который час'),
    "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
    "cursor":('перемести', 'передвинь', 'переставь', 'перенести', 'перевести'),
    "cursor1":('курсор на' , 'мышь на', 'мышку на' )
}
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(commands["vasya"]):
            cmd = voice
            for x in commands['vasya']:
                cmd = cmd.replace(x, "").strip()

            if cmd.startswith(commands["open"]):
                for x in commands['open']:
                    cmd = cmd.replace(x, "").strip()
                if cmd == 'калькулятор':
                    os.startfile("C:\\Users\\gusev\\OneDrive\\Рабочий стол\\Калькулятор")
                if cmd == 'вконтакте' or cmd == 'вк':
                    webbrowser.open('https://vk.com/feed')
                if cmd == 'ютубчик' or cmd == 'youtube':
                    webbrowser.open('https://www.youtube.com')
                if cmd == 'этот проект на гитхабе':
                    webbrowser.open('https://github.com/gusev-iliya/Vasya_voice-assistant')
                sites = open("sites.txt", "r")
                for line in sites:
                    cm, link = line.split(' ')
                    if cmd==cm:
                        webbrowser.open(link)
                sites.close()
                l=False
                apps = open("apps.txt", "r")
                for line in apps:
                    if l==True:
                        os.startfile(str(line).strip())
                        l=False
                    if line.strip() == cmd.strip():
                        l=True
                apps.close()
            if cmd.startswith(commands["google"]):
                for x in commands['google']:
                    cmd = cmd.replace(x, "").strip()
                webbrowser.open('https://www.google.com/search?q=%s' %cmd)
            if cmd=='новый сайт':
                print('команда')
                cm=input()
                print('ссылка')
                link=input()
                new = open("commands.txt", "a")
                new.write('%s %s\n' %(cm, link))
                new.close()
            if cmd == 'новое приложение':
                print('команда')
                c=input()
                print('путь к приложению')
                path=input()
                new = open("apps.txt", "a")
                new.write('%s\n%s\n' %(c, path))
                new.close()
            if cmd.startswith(commands["calc"]):
                for x in commands['calc']:
                    cmd = cmd.replace(x, "").strip()
                c=1
                a = ''
                b = ''
                oper = 1
                for i in cmd:
                    if oper != 1 and i!=' ':
                        b +=i
                    if c==2:
                        oper=i
                        c=3
                    if i == ' ' and c==1:
                        c=2
                    if c == 1:
                        a +=i
                if oper=='x':
                    result=int(a)*int(b)
                    print('ответ: ',str(result) )
                if oper=='/':
                    result=int(a)/int(b)
                    print('ответ: ',str(result) )
                if oper=='+':
                    result=int(a)+int(b)
                    print('ответ: ',str(result) )
                if oper=='-':
                    result=int(a)-int(b)
                    print('ответ: ',str(result) )
            if cmd.startswith(commands["ctime"]):
                print('Сейчас ', datetime.datetime.today().strftime('%H:%M'))
            if cmd == 'какое сегодня число' or cmd == 'какой сегодня день':
                for key in monthes:
                    if key==datetime.datetime.today().strftime('%m'):
                        print('Сегодня ', datetime.datetime.today().strftime('%d'), monthes[key])
            if cmd.startswith(commands["cursor"]):
                for x in commands['cursor']:
                    cmd = cmd.replace(x, "").strip()
                if cmd.startswith(commands["cursor1"]):
                    for x in commands['cursor1']:
                        cmd = cmd.replace(x, "").strip()
                    s = cmd.split()
                    if len(s)>2:
                        x1,x2,y1,y2=cmd.split(' ')
                        pag.moveTo(int(x1),int(y1), 0.5)
                    else:
                        x1,y1 = cmd.split(' ')
                        if y1 == 'вниз':
                            pag.move(0, int(x1), 0.5)
                        elif y1 == 'вверх' or y1 == 'верх':
                            pag.move(0, -(int(x1)), 0.5)
                        elif y1 == 'вправо' or y1 == 'вправа':
                            pag.move(int(x1),0, 0.5)
                        elif y1 == 'влево' or y1 == 'налево':
                            pag.move(-(int(x1)),0, 0.5)
            if cmd == 'нажми' or cmd == 'тыкни':
                pag.click()
            elif cmd.startswith('нажми на'):
                cmd = cmd.replace('нажми на','').strip()
                x1,x2,y1,y2 = cmd.split(' ')
                pag.click(x=int(x1), y=int(y1))
            elif cmd.startswith('нажми правой кнопкой мыши'):
                pag.click(button='right')
            if cmd.startswith('выдели до'):
                cmd = cmd.replace('выдели до', '')
                cmd = cmd.strip()
                x1,x2,y1,y2 = cmd.split(' ')
                pag.dragTo(int(x1),int(y1),0.5)
            if cmd.startswith('вверх'):
                cmd = cmd.replace('вверх', '')
                pag.scroll(int(cmd))
            if cmd.startswith('вниз'):
                cmd = cmd.replace('вниз', '')
                pag.scroll(-(int(cmd)))
            if cmd.startswith('напиши') or cmd.startswith('напечатай'):
                cmd = cmd.replace('напиши','')
                cmd = cmd.replace('напечатай','')
                st = ''
                for x in cmd:
                    for key in letters:
                        if x == letters[key]:
                            st+=key
                pag.write(st, interval=0.1)
            if cmd == 'поменяй язык':
                pag.hotkey('shift','ctrl')
            if cmd == 'скопируй':
                pag.hotkey('ctrl','V')
            if cmd == 'вставь':
                pag.hotkey('ctrl','C')
            if cmd == 'позиция':
                print(pag.position())
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

speak("Добрый день, повелитель")
speak("Вася слушает")

stop_listening = r.listen_in_background(m, callback)
while True:time.sleep(0.001)
