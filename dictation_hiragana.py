import playsound as play
from gtts import gTTS
import json
import random as ran
from PIL import Image
import time
import pyautogui

# get json
def Getjson(filepath):
    with open(filepath, 'r') as fp:
        return json.load(fp)


# import hiragana dictionary
hiragana_dic = Getjson('/home/vannak/github/pycharmproject/learn_Japanese/hiragana.json')


flag = []


def voice_with_picture():

    from pynput.keyboard import Key, Listener

    answer_list_alphabet = []
    answer_list_sound = []

    # show the pinyin and play sound randomly
    def random_hiragana():
        hiragana_key = list(hiragana_dic)
        random_hiragana_key = ran.choice(hiragana_key)
        print(random_hiragana_key)
        im = Image.open(random_hiragana_key)
        im.show()
        time.sleep(0.5)
        print(hiragana_dic[random_hiragana_key][0])
        play.playsound(hiragana_dic[random_hiragana_key][0])
        answer_list_alphabet.append(hiragana_dic[random_hiragana_key][1])
        answer_list_sound.append(hiragana_dic[random_hiragana_key][0])
        del hiragana_dic[random_hiragana_key]

    # handle voice assistant
    def assistant():
        mytext = user_input + 'alphabets of Hiragana will be called randomly. ' \
                              'Now let\'s get started.' \
                              'If you are ready? click enter.'
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save('assistant.mp3')

    # intro
    user_input = input('I wanna try: ')
    if user_input == 'all':
    	user_input = len(hiragana_dic)
    try:
    	assistant()
    	play.playsound('assistant.mp3')
    except:
    	play.playsound('handle_assistant.mp3')
   
    # start random
    count = []
    count_for_an = []
    # random_hiragana()

    def detect_key_press(key):
        if key == Key.enter and len(count)/2 < int(user_input):
            print('count1', len(count) / 2)
            pyautogui.press('esc')
            random_hiragana()
        elif key == Key.enter and len(count)/2 == int(user_input):
            pyautogui.press('esc')
            play.playsound('answer.mp3')
        elif key == Key.enter and len(count)/2 > int(user_input):
            print('count2', len(count) / 2)
            pyautogui.press('esc')
            print(answer_list_alphabet[len(count_for_an)])
            im = Image.open(answer_list_alphabet[len(count_for_an)])
            im.show()
            play.playsound(answer_list_sound[len(count_for_an)])
            count_for_an.append('0')

    def detect_key_release(key):
        count.append(0)
        if len(count)/2 == int(user_input) * 2 + 1:
            print('count3',len(count)/2)
            return False

    with Listener(on_press=detect_key_press,
                  on_release=detect_key_release) as Listener:
        Listener.join()

    time.sleep(0.5)
    pyautogui.press("esc")
    play.playsound('conclusion.mp3')
    restart = input("Would you like to try again? :")
    if restart == 'yes'.lower():
        flag.append(0)
    else:
        exit()


def voice_without_picture():
    from pynput.keyboard import Key, Listener

    answer_list_alphabet = []
    answer_list_sound = []
    replay_list = []

    # show the pinyin and play sound randomly
    def random_hiragana():
        hiragana_key = list(hiragana_dic)
        random_hiragana_key = ran.choice(hiragana_key)
        im = Image.open("Webp.net-resizeimage.png")
        im.show()
        time.sleep(0.5)
        play.playsound(hiragana_dic[random_hiragana_key][0])
        answer_list_alphabet.append(hiragana_dic[random_hiragana_key][1])
        answer_list_sound.append(hiragana_dic[random_hiragana_key][0])
        replay_list.append(hiragana_dic[random_hiragana_key][0])
        del hiragana_dic[random_hiragana_key]

    # handle voice assistant
    def assistant():
        mytext = user_input + ' alphabets of Hiragana will be called randomly.\n ' \
                              'Now let\'s get started.\n' \
                              'If you are ready? Click enter!\n' \
                              'To replay! click space!'
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save('assistant.mp3')


    # intro
    user_input = input('I wanna try: ')
    if user_input == 'all':
    	user_input = len(hiragana_dic)
    try:
        assistant()
        play.playsound('assistant.mp3')
    except: # in case no connection
        play.playsound('handle_assistant.mp3')

    count = []

    def detect_key_press(key):
        if key == Key.enter and len(count) % 2 == 0:
            pyautogui.press('esc')
            replay_list.clear()
            random_hiragana()
            print('count1', len(count) / 2)
        elif key == Key.enter and len(count) % 2 != 0:
            pyautogui.press('esc')
            replay_list.clear()
            im = Image.open(answer_list_alphabet[0])
            im.show()
            answer_list_alphabet.clear()
        elif key == Key.space:
            try:
                time.sleep(0.2)
                play.playsound(replay_list[0])
            except:
                play.playsound('nothingTOreplay.mp3')

    def detect_key_release(key):
        if key == Key.enter:
            count.append(0)
        if len(count) / 2 == int(user_input):
            print('count3', len(count) / 2)
            return False

    with Listener(on_press=detect_key_press,
                  on_release=detect_key_release) as Listener:
        Listener.join()

    time.sleep(1)
    pyautogui.press("esc")
    play.playsound('conclusion.mp3')


def start():
    play.playsound('intro.mp3')
    print("1. with picture\n2. without picture")
    with_pic = 'with picture'
    without_pic = 'without picture'
    user_input = input('Voice ')
    if user_input == with_pic or user_input == '1':
        play.playsound('/home/vannak/github/pycharmproject/learn_Japanese/introFor1mode.mp3')
        voice_with_picture()
    elif user_input == without_pic or user_input == '2':
        play.playsound('/home/vannak/github/pycharmproject/learn_Japanese/introFor2mode.mp3')
        voice_without_picture()
        
start()
exit()







