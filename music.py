from hub import light_matrix
import runloop
from hub import sound
from time import sleep_ms

l = 150

c=523
d=587
e=659
f=698
f2 = 740
g=784
a=880
a2=932
b=988

#ドはドーナツのド
melody = [
    (c,750),
    (d,250),
    (e,750),
    (c,250),
    (e,500),
    (c,500),
    (e,1000)
]

#かわいいだけじゃだめですか
kawaii = [
    (d, l),
    (e, l),
    (f2, l),
    (g, l),
    (a, l),
    (g, l),
    (f2, l),
    (e, l),
    (d, l),
    (0, l),
    (d*2, l),
    (0, l),
    (d, l),

    #さび
    (d, l),
    (g, l),
    (a, l),
    (b, l),
    (a2, l),
    (a,l),
    (g, l*2),
    (d, l),
    (g, l),
    (a, l),
    (b, l),
    (a2, l),
    (a, l),
    (g, l*2),
    (d, l),
    (e, l),
    (g, l),
    (a, l),
    (a, l),
    (a, l),
    (g, l),
    (f2, l),
    (c*2, l),
    (b, l),
    (g, l*2),
    (g, l),
    (a, l*2),
    (b, l),
    (d, l),
    (g, l),
    (a, l),
    (b, l),
    (a2, l),
    (a, l),
    (g, l*2),
    (d, l),
    (d*2, l),
    (d*2, l),
    (d*2, l),
    (c*2, l),
    (b, l),
    (g, l*2),
    (a2, l),
    (a, l),
    (g, l),
    (0, l),
    (a2, l),
    (a, l),
    (g, l),
    (g, l),
    (d, l),
    (a, l),
    (g, l*5),

    (0, l),

    (d, l),
    (g, l),
    (a, l),
    (b, l),
    (a2, l),
    (a,l),
    (g, l*2),
    (d, l),
    (g, l),
    (a, l),
    (b, l),
    (a2, l),
    (a, l),
    (g, l*2),
    (d, l),
    (e, l),
    (g, l),
    (a, l),
    (a, l),
    (a, l),
    (g, l),
    (f2, l),
    (c*2, l),
    (b, l),
    (g, l*2),
    (g, l),
    (a, l*2),
    (b, l),
    (d, l),
    (g, l),
    (a, l),
    (b, l),
    (a2, l),
    (a, l),
    (g, l*2),
    (d, l),
    (d*2, l),
    (d*2, l),
    (d*2, l),
    (c*2, l),
    (b, l),
    (g, l*2),
    (a2, l),
    (a, l),
    (g, l),
    (0, l),
    (a2, l),
    (a, l),
    (g, l),
    (a2, l),
    (a, l),
    (g, l),
    (d*2, l*2),
    (d*2, l),
    (d*2, l),
    (d*2, l),
    (d*2, l),
    (g, l),
    (a, l),
    (g, l*2)
]




async def play_melody():
    for freq, dur in kawaii:
        await sound.beep(freq, dur)# ← 修正：キーワード引数ではなく位置引数
        await runloop.sleep_ms(50)# 少し休符

async def main():
    await play_melody()

runloop.run(main())
