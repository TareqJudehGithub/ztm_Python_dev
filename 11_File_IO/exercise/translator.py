# write a program that translate words in foreign languages stored in a separate file.

# Solution 1:
# using package Translate

# $ pip install translate

# from translate import Translator
#
#
# def translator_func():
#     translator = Translator(from_lang='fr', to_lang='en')
#
#     try:
#         with open('file_to_trans.txt', mode='r') as file:
#             file1 = file.read()
#             translation = translator.translate(file1)
#     except FileNotFoundError as err:
#         raise err
#     else:
#         with open('trans_to.txt', mode='w') as file:
#             file.write(translation)
#
#
# translator_func()
# =================================

# Solution 2:
# using package googletrans  * This is recommended

# pip install googletrans==4.0.0-rc1

from googletrans import Translator

# instantiating from Translator class
translator = Translator()


def google_translator():
    try:
        with open('french_article.txt', mode='r') as file:
            read_file = file.read()
            translation = translator.translate(
                text=read_file,
                src='fr',
                dest='en'
            )

    except FileNotFoundError as err:
        raise err

    else:
        with open('trans_to.txt', mode='w') as file:
            file.write(translation.text)

        print('File created successfully!')


google_translator()