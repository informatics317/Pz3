'''Шифр Цезаря'''
class SdvigDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj.__dict__.get('_' + self.name)

    def __set__(self, obj, value):
        if type(value) != int:
            raise TypeError('Ключ шифра должен быть целым числом')
        obj.__dict__['_' + self.name] = value

class CaesarShifr:
    sdvig = SdvigDescriptor()
    def __init__(self, sdvig):
        self.alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.sdvig = sdvig

    def process(self, symbol, napravlenie):
        if 'а' <= symbol <= 'я':
            start = ord('а')
            index = ord(symbol) - start
            new_index = (index + napravlenie * self.sdvig) % 32
            return chr(start + new_index)
        elif 'А' <= symbol <= 'Я':
            start = ord('А')
            index = ord(symbol) - start
            new_index = (index + napravlenie * self.sdvig) % 32
            return chr(start + new_index)
        else:
            return symbol

    def encode(self, text):
        result = []
        for symbol in text:
            result.append(self.process(symbol, 1))
        return ''.join(result)

    def decode(self, text):
        result = []
        for symbol in text:
            result.append(self.process(symbol, -1))
        return ''.join(result)


print('Шифр Цезаря')
shifr = CaesarShifr(4)
print(f'Ключ шифра: {shifr.sdvig}')

text = 'Скоро каникулы!'
print('Исходный текст:', text)
print(f'Шифровка: {shifr.encode(text)}')
print(f'Дешифровка: {shifr.decode(shifr.encode(text))}')

print()


'''Шифр Атбаш'''
class AlphabetDescriptor:
    def __get__(self, obj, cl):
        return 'abcdefghijklmnopqrstuvwxyz'

class AtbashShifr:
    alphabet = AlphabetDescriptor()

    def encode(self, text):
        result = ''
        for symbol in text:
            if 'a' <= symbol <= 'z':
                index = ord(symbol) - ord('a')
                new_index = 25 - index
                new_symbol = chr(ord('a') + new_index)
                result += new_symbol
            elif 'A' <= symbol <= 'Z':
                index = ord(symbol) - ord('A')
                new_index = 25 - index
                new_symbol = chr(ord('A') + new_index)
                result += new_symbol
            else:
                result += symbol
        return result
    decode = encode


print('Шифр Атабаш')
text = 'Happy New Year to all of you!'
print('Исходный текст:', text)
print(f'Шифровка: {AtbashShifr().encode(text)}')
print(f'Дешифровка: {AtbashShifr().decode(shifr.encode(text))}')








