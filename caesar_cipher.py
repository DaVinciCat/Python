def __caesarify__(dictionary, key, text, decode=False):
    power = len(dictionary)
    map = {} 
    
    for index in range(len(dictionary)):
        offset = (index + key) % power 
        if not decode:
            map[dictionary[index]] = dictionary[offset]
        else:
            map[dictionary[offset]] = dictionary[index]
    
    result = '' 
    for index in range(len(text)):
        letter = text[index]
        mapped = map.get(letter.lower())
        if mapped is not None:    
            result += mapped.upper() if letter.isupper() else mapped
        else:
            result += letter
    
    return result

dictionary_en = 'abcdefghijklmnopqrstuvwxyz'
dictionary_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encode_en(text, key):
    return __caesarify__(dictionary_en, key, text)

def decode_en(text, key):
    return __caesarify__(dictionary_en, key, text, decode=True)		  
    
def encode_ru(text, key):
    return __caesarify__(dictionary_ru, key, text)  

def decode_ru(text, key):
    return __caesarify__(dictionary_ru, key, text, decode=True)

def encode(s, rotn):
    return encode_en(s, rotn)     

def decode(s, rotn):
    return decode_en(s, rotn)  

text = 'Съешь же ещё этих мягких французских булок да выпей чаю.'
print(encode_ru(text, 3))
#Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.

text = 'Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.'
print(decode_ru(text, 3))
#Съешь же ещё этих мягких французских булок да выпей чаю.

text = 'The quick brown fox jumps over the lazy dog.'
print(encode_en(text, -3))
#Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.

text = 'Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.'
print(decode_en(text, -3))
#The quick brown fox jumps over the lazy dog.


#Требуется реализовать две функции для работы с шифром Цезаря.
#Напишите функцию encode(s, rotn), которая принимает два аргумента: исходный текст и значение сдвига, выполняет кодирование и возвращает закодированный текст.
#Напишите функцию decode(s, rotn), которая принимает два аргумента: закодированный текст и значение сдвига, выполняет декодирование и возвращает оригинальный текст.
#Кодируются только буквы алфавита, числа, символы пунктуации и другие символы не кодируются.
#Сдвиг - это целое число, он цикличен и его максимальное значение равно количеству букв алфавита. В задаче используется только латинский алфавит, поэтому значение сдвига может быть от 0 до 25 (всего 26 символов).
#Нужно учитывать регистр символов, a со смещением 1, возвращает b, а A - возвращает B.
#В решении задачи вам пригодятся строковые функции/методы вашего ЯП, а также функции для работы с ASCII-кодами символов.
#Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

