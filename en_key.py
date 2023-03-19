# Программа позволяет изменить текст, если пользователь ошибся раскладкой клавиатуры
en_keys = "`qwertyuiop[]asdfghjkl;'zxcvbnm,."
ru_keys = "ёйцукенгшщзхъфывапролджэячсмитьбю"

inp_text = 'fuf yf cfvjv ltkt j[etyyj vj;yj yt gthtrk.xfnm hfcrkflre'
result = ''

if inp_text[0].lower() in en_keys:
    for i in inp_text.lower():
        if i in en_keys:
            result += ru_keys[en_keys.index(i)]
        else:
            result += i
else:
    for i in inp_text.lower():
        if i in ru_keys:
            result += en_keys[ru_keys.index(i)]
        else:
            result += i

print(result)
