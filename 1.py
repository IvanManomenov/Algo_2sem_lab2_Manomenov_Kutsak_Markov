from math import *


def h1(s, n):
    a = []
    for i in s:
        a.append(ord(i) % n)
    return a


def h2(s, m):
    a = []
    for i in s:
        a.append(ord(i) % (m - 1) + 1)
    return a


def hash(s, m):  # Составление хеш-таблицы при помощи двойного хеширования (во избежание коллизий)
    if len(s) == 1:
        return [s[0]]
    if len(s) == 0:
        return []
    table = [None for i in range(m)]
    a1 = h1(s, m)
    a2 = h2(s, m)
    a = []
    for i in range(len(s)):
        x = a1[i]
        y = a2[i]
        f = 0
        for j in range(m):
            if table[x] == None or table[x] == s[i]:
                table[x] = s[i]
                f = 1
                break
            x = (x + y) % m
        if f == 0:
            return hash(s, 2 * m)
    return table


def to_dict(table):  # Составление словаря по хеш-таблице
    d = {}
    for i in range(len(table)):
        if table[i] != None:
            d[table[i]] = i
    return d


def to_bin(a, table):  # перевод массива закодированных символов в двоичную строку
    b = ""
    k = int(log(len(table), 2))
    for i in a:
        ch = ""
        for j in range(k):
            if i >= 2 ** (k - j - 1):
                ch += '1'
                i -= 2 ** (k - j - 1)
            else:
                ch += '0'
        b += ch
    return b


def from_bin(b, table):  # извлечение массива закодированных символов из двоичной строки
    a = []
    k = int(log(len(table), 2))
    for i in range(0, len(b), k):
        n = 0
        for j in range(k):
            n += (2 ** (k - j - 1)) * int(b[i + j])
        a.append(n)
    print(a)
    return a


def code(s, d, table):  # Кодирование сообщения
    a = []
    for i in s:
        a.append(d[i])
    print(a)
    return to_bin(a, table)


def decode(b, table):  # Расшифровка сообщения
    s = ""
    a = from_bin(b, table)
    for i in a:
        s += table[i]
    return s


s = input()
tab = hash(s, 2)
print("Хеш - таблица:", tab)
diction = to_dict(tab)
print("Словарь:", diction)
q = code(s, diction, tab)
print("Закодированное сообщение:", q)
new_s = decode(q, tab)
print("Расшифровка:", new_s)
