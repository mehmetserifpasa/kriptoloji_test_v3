import sys,random



a = 1919191919
aa = "a"

b = 1191919191
bb = "b"

c = 1119191919
cc = "c"

ç = 1111919191
çç = "ç"

d = 1111191919
dd = "d"

e = 1111119191
ee = "e"

f = 1111111911
ff = "f"

g = 1111111191
gg = "g"

ğ = 1111111119
ğğ = "ğ"

h = 9119191919
hh = "h"

ı = 9919191919
ıı = "ı"

i = 9991919191
ii = "i"

j = 9999191919
jj = "j"

k = 9999919191
kk = "k"

l = 9999991919
ll = "l"

m = 9999999191
mm = "m"

n = 9999999919
nn = "n"

o = 9999999991
oo = "o"

ö = 9999999999
öö = "ö"


p = 1911199911
pp = "p"

r = 1911911911
rr = "r"

s = 9911911911
ss = "s"

ş = 1911199911
şş = "ş"

t = 1911111911
tt = "t"

u = 1911111911
uu = "u"

ü = 1911111911
üü = "ü"


v = 1911911911
vv = "v"

y = 1911191911
yy = "y"

z = 191111911
zz = "z"



text = "satranç"
sifre = []

for tx in text:
    if tx == aa:
        sifre.append(a)
    if tx == bb:
        sifre.append(b)
    if tx == cc:
        sifre.append(c)
    if tx == çç:
        sifre.append(ç)
    if tx == dd:
        sifre.append(d)
    if tx == ee:
        sifre.append(e)
    if tx == ff:
        sifre.append(f)
    if tx == gg:
        sifre.append(g)
    if tx == ğğ:
        sifre.append(ğ)
    if tx == hh:
        sifre.append(h)
    if tx == ıı:
        sifre.append(ı)
    if tx == ii:
        sifre.append(i)
    if tx == jj:
        sifre.append(j)
    if tx == kk:
        sifre.append(k)
    if tx == ll:
        sifre.append(l)
    if tx == mm:
        sifre.append(m)
    if tx == nn:
        sifre.append(n)
    if tx == oo:
        sifre.append(o)
    if tx == öö:
        sifre.append(ö)
    if tx == pp:
        sifre.append(p)
    if tx == rr:
        sifre.append(r)
    if tx == ss:
        sifre.append(s)
    if tx == şş:
        sifre.append(ş)
    if tx == tt:
        sifre.append(t)
    if tx == uu:
        sifre.append(u)
    if tx == üü:
        sifre.append(ü)
    if tx == vv:
        sifre.append(v)
    if tx == yy:
        sifre.append(y)
    if tx == zz:
        sifre.append(z)



dosya = open("sifre.txt","w")
for sf in sifre:
    dosya.writelines(str(sf))













