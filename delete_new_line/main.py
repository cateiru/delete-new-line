import pyperclip


def main():
  text = pyperclip.paste()

  if(text == ''):
    raise('Clipboard is empty.')

  formated_text = text.replace('\n', '')
  print('Success conversion!')
  print(formated_text)
  pyperclip.copy(formated_text)


if __name__ == "__main__":
  main()
