def __caesarify__(dictionary, key, text):
    power = len(dictionary)
    map = {} 
    
    for i in range(len(dictionary)):
        y = (i + key) % power 
        map[dictionary[i]] = dictionary[y]
    
    result = '' 
    for i in range(len(text)):
        letter = text[i]
        if letter.lower() in map:
            mapped = map[letter.lower()]
            result += mapped.upper() if letter.isupper() else mapped
        else:
            result += letter
    
    return result

def caesarify_en(text, key):
    dictionary = 'abcdefghijklmnopqrstuvwxyz'
    return __caesarify__(dictionary, key, text)  
    
def caesarify_ru(text, key):
    dictionary = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return __caesarify__(dictionary, key, text)  

#text = input('Введите текст: ')
text = 'Съешь же ещё этих мягких французских булок да выпей чаю.'
print(caesarify_ru(text, 3))
#Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.

text = 'The quick brown fox jumps over the lazy dog.'
print(caesarify_en(text, -3))
#Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.

