import runloop
import motor
from hub import port
from hub import light_matrix
from time import sleep_ms as sleep
import motor_pair
import color_sensor
import color

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
WHEEL = motor_pair.PAIR_1 #タイヤ
NAKAHARA = port.C
IMAI = port.E
MV_DG = motor.run_for_degrees #角度を指定して進むやつ
MV_P_DG = motor_pair.move_for_degrees #角度を指定して進むやつのペア
SLEEP = runloop.sleep_ms

#変数設定
#モーターのスピード
FAST = 1500
MID = 1000
LOW = 300
#色
colors = []

#関数
#まっすぐ進む
async def straight(d, v):
    await MV_P_DG(WHEEL, d, 0, velocity=v)
    #await SLEEP(1000)
    print("done straight!")

#曲がる
async def turn(d, v):
    MV_DG(port.B, -d, v)
    MV_DG(port.A, -d, v)
    await SLEEP(500)
    print("done turn!")

#中原
async def nakahara(d, v):
    await MV_DG(NAKAHARA, d, v)
    #await SLEEP(1000)
    print("done nakahara!")

#色読み取り
async def readColor():
    #r, g, b, i = 0, 0, 0, 0
    
    #for k in range(10):
        #colors = color_sensor.rgbi(port.F)
        #r += colors[0] 
        #g += colors[1] 
        #b += colors[2]
        #i += colors[3]
        #await SLEEP(100)
    #r = r//10
    #g = g//10
    #b = b//10
    #i = i//10
    #print(r,g,b,i)
    #色振り分け
    #if r >= 100 and g >= 100:
        #print("yellow")
    #elif r >= g and r >= b:
        #print("red")
    #elif g >= r and g >= b:
        #print("green")
    #elif b >= r and b >= g:
        #print("blue")
    await SLEEP(500)
    if color_sensor.color(port.F) is color.RED:
        print("赤色だよ")
        return "red"
    elif color_sensor.color(port.F) is color.YELLOW:
        print("黄色だよ")
        return "yellow"
    elif color_sensor.color(port.F) is color.BLUE:
        print("青色だよ")
        return "blue"
    elif color_sensor.color(port.F) is color.GREEN:
        print("緑色だよ")
        return "green"

    print("done readColor!")

#テスト
async def test():
    #MV_DG(MOTOR1, 1000, FAST)
    #motor.run(port.A, 1000)
    #await straight(100, FAST)
    #await straight(-500, FAST)
    await turn(526, MID)
    print("done test!")    

#つなぎ0
async def jumper0():
    #壁あて
    await straight(-350, LOW)
    await straight(3650, FAST)
    await turn(-263, MID)
    await straight(-300, LOW)
    await straight(160, FAST)
    await turn(263, MID)
    await straight(200, FAST)
    print("done jumper0!")

#赤色黄色棒
async def stickProcess():
    #オブジェクトまで行く
    await straight(100, FAST)
    #全部取る
    await nakahara(-115, MID)
    await SLEEP(500)
    #下がって旋回
    await straight(-400, FAST)
    await turn(-263, MID) 
    #置き場まで行く
    await straight(1300,FAST)
    await turn(263, MID)
    #黄色を指定の場所にセット
    await turn(131, MID)
    await straight(435, FAST)
    #赤色だけをとる
    await nakahara(115, MID)
    await straight(-100, FAST)
    await nakahara(-115, MID)
    #下がる
    await straight(-170, FAST)
    #赤色を指定の場所にセット
    await turn(-255, MID)
    await straight(360, FAST)
    await nakahara(115, MID)
    print("done stickProcess!")

#つなぎ１
async def jumper1():
    await straight(-1200, FAST)
    await turn(-131, MID)
    print("done jumper1!")

#引くやつ
async def pullProcess():
    #オブジェクトまで行く
    await straight(200, FAST)
    #引く
    await nakahara(-105, MID)
    await straight(-330, FAST)
    await straight(50, FAST)
    await nakahara(105, MID)
    await straight(-50, FAST)
    print("done pullProcess!")

#つなぎ2
async def jumper2():
    #旋回
    await turn(263, MID)
    #目的地に行く
    await straight(-490, FAST)
    await turn(263, MID)
    await straight(-1000, FAST)
    await straight(-300, LOW)
    print("done jumper2!")

#ボルトと正方形の色を読み取る
async def readColorProcess():
    #読み取る
    colors.append(await readColor())
    #旋回
    await straight(500, FAST)
    await turn(263, MID)
    await straight(220, FAST)
    await turn(263, MID)
    await straight(250, FAST)
    #読み取る
    colors.append(await readColor())
    await straight(150, FAST)
    colors.append(await readColor())
    #color4を定義
    if "red" not in colors:
        colors.append("red")
    elif "blue" not in colors:
        colors.append("blue")
    elif "yellow" not in colors:
        colors.append("yellow")
    elif "green" not in colors:
        colors.append("green")
    #正方形の色を読み取る
    await straight(-800, FAST)
    await MV_DG(port.B, -200, MID)
    await MV_DG(port.A, 200, MID)
    await MV_DG(port.B, 200, MID)
    await MV_DG(port.A, -200, MID)
    colors.append(await readColor())
    print(colors)
    print("done readColorProcess!")

#つなぎ3
async def jumper3():
    #壁あて
    await straight(-900, FAST)
    await straight(-300, LOW)
    #旋回
    await straight(250, FAST)
    await turn(263, MID)
    #壁あて
    await straight(-2200, FAST)
    await straight(-300, LOW)

#-----ここから分岐-----
#正方形のオブジェクト
#青の時
async def sBlue():
    #旋回
    await straight(250, FAST)
    await turn(-263, MID)
    await straight(300, FAST)
    #とる
    await nakahara(-115, MID)
    #旋回
    await straight(470, FAST)
    await turn(263, MID)
    await straight(-300, LOW)
    
    print("done sBlue")

#赤の時
async def sRed():
    #旋回
    await straight(700, FAST)
    await turn(-263, MID)
    await straight(465, FAST)
    await turn(-263, MID)
    await straight(300, FAST)
    #とる
    await nakahara(-110, MID)
    #旋回
    await turn(263, MID)
    await straight(310, FAST)
    await turn(263, MID)
    await straight(-500, LOW)
    print("done sRed!")

#黄の時
async def sYellow():
    #旋回
    await straight(700, FAST)
    await turn(-263, MID)
    await straight(900, FAST)
    await turn(-263, MID)
    await straight(475, FAST)
    await turn(-263,FAST)
    await straight(300, FAST)
    #とる
    await nakahara(-115, MID)
    #旋回
    await straight(-155, FAST)
    await turn(-263, MID)
    await straight(-300, FAST)
    print("done sYellow!")

#緑色の時
async def sGreen():
    #旋回
    await straight(250, FAST)
    await turn(-263, MID)
    await straight(300, FAST)
    #とる
    await nakahara(-115, MID)
    #旋回
    await turn(263, MID)
    await straight(200, FAST)
    #離す
    await nakahara(110, MID)
    #旋回
    await straight(-200, FAST)
    await turn(-263, MID)
    await straight(400, FAST)
    await turn(263, MID)
    await straight(400, FAST)
    await turn(263, MID)
    await straight(300, FAST)
    #つかむ
    await nakahara(-110, MID)
    #旋回
    await straight(-343, FAST)
    await turn(-263, MID)
    await straight(-500, FAST)
    await straight(-250, LOW)

    print("done sGreen!")

#正方形のオブジェクトメイン処理
async def squareProcess():
    if colors[4] == "red":
        await sRed()
    elif colors[4] == "blue":
        await sBlue()
    elif colors[4] == "yellow":
        await sYellow()
    elif colors[4] == "green":
        await sGreen()
    else:
        await sBlue()
    #置き場まで行く
    await straight(1000, FAST)
    await nakahara(110, MID)
    await straight(580, FAST)
    print("done squareProcess!")

#ボルト
async def boltProcess():
    print("done boltProcess!")

#旗
async def flagProcess():
    print("done flagProcess!")

#閉めるやつ
async def closeProcess():
    #オブジェクトまで行く
    await readColor()
    #通り過ぎるときに閉める
    print("done closeProcess!")

#メイン処理
async def main():
    #await test()
    await jumper0()
    await stickProcess()
    await jumper1()
    await pullProcess()
    await jumper2()
    await readColorProcess()
    await jumper3()
    await squareProcess()
    print("done all process!")

    
runloop.run(main())
