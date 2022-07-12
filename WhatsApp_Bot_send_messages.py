# MADE BY HASH-002

import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# Function to search the contact which is not present in the recent List
def new_chat(user_name):

    # Click on the List
    search_chat = chrome_browser.find_element_by_class_name('_1UWac ')
    search_chat.click()

    # Search the Contact
    new_user = chrome_browser.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(1)  # pause to get the content loaded

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()


if __name__ == '__main__':

    # load web driver for selenium : chrome
    chrome_browser = webdriver.Chrome(executable_path="D:\Study Folder\chromedriver_win32\chromedriver.exe")
    chrome_browser.get('https://web.whatsapp.com/')

    time.sleep(20)  # wait to scan QR code

    # List of the users you want to respond
    user_name_list = ['Kaushik']

    # Message you want to send to the user
    msg = 'I am a WhatsApp Bot\n' + 'This is a random Message'

    for user_name in user_name_list:
        try:
            user_name = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user_name.click()
        except NoSuchElementException:
            new_chat(user_name)

        # Type the message at correct place
        msg_chat =chrome_browser.find_element_by_class_name('p3_M1')
        msg_chat.click()
        # message_box = chrome_browser.find_element_by_xpath('//div')
        message = chrome_browser.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')
        message.send_keys(msg)


        # Send the message
        button = chrome_browser.find_element_by_xpath('//button[@class="_4sWnG"]')
        button.click()

    chrome_browser.close()