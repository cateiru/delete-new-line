import pyperclip
import time


def main():
  buffer_text = ''
  text = ''
  formated_text = ''

  while(True):
    text = pyperclip.paste()
    if(buffer_text != text):
      formated_text = text.replace('\n', '')
      print('Success conversion!')
      print(formated_text)
      pyperclip.copy(formated_text)
      buffer_text = formated_text
    time.sleep(1)


if __name__ == "__main__":
  main()
