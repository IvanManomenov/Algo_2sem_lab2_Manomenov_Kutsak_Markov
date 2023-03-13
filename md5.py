from math import *


def to_bin(a, k):
    b = ""
    nums = ['0', '1']
    for i in a:
        ch = ""
        for j in range(k):
            ch += nums[i % 2]
            i //= 2
        b += ch
    return b


def from_bin(b):
    ln = 0
    k = len(b)
    for i in range(k):
        ln += (2 ** (k - i - 1)) * int(b[i])
    return ln


def to_hex(a, k):
    h = ""
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in a:
        ch = ""
        for j in range(k):
            ch += nums[i % 16]
            i //= 16
        h += ch
    return h


K = [int(2 ** 32 * abs(sin(i + 1))) for i in range(64)]
s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15,
     21]
a0 = 0x67452301
b0 = 0xefcdab89
c0 = 0x98badcfe
d0 = 0x10325476

st = input()
ms = [ord(i) for i in st]
bs = to_bin(ms, 8)
n = len(bs) % (2 ** 64)
bn = to_bin([n], 64)
bs += '1'
while len(bs) % 512 != 448:
    bs += '0'
bs += bn

for _ in range(0, len(bs), 512):
    M = [from_bin(bs[512 * _ + 32 * i: 512 * _ + 32 * (i + 1)]) for i in range(16)]
    for j in range(16):
        A = a0
        B = b0
        C = c0
        D = d0
        for i in range(64):
            if i < 16:
                F = (B & C) | ((~B) & D)
                g = i
            elif i < 32:
                F = (D & B) | ((~D) & C)
                g = (5 * i + 1) % 16
            elif i < 48:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | (~D))
                g = (7 * i) % 16
            F = F + A + K[i] + M[g]
            # print(F)
            A = D % (2 ** 128)
            D = C % (2 ** 128)
            C = B % (2 ** 128)
            B = (B + (F << s[i]))
        a0 += A
        b0 += B
        c0 += C
        d0 += D
print(to_hex([a0, b0, c0, d0], 8))
