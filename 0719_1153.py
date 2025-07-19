import runloop
import motor
from hub import port
from hub import light_matrix
from time import sleep_ms as sleep
import motor_pair

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)
WHEEL = motor_pair.PAIR_1 #タイヤ
NAKAHARA = port.C
IMAI = port.E
MV_DG = motor.run_for_degrees #角度を指定して進むやつ
MV_P_DG = motor_pair.move_for_degrees #角度を指定して進むやつのペア
SLEEP = runloop.sleep_ms

#変数設定
#モーターのスピード
FAST = 750
MID = 500
LOW = 100

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
    await SLEEP(800)
    print("done turn!")

#中原
async def nakahara(d, v):
    await MV_DG(NAKAHARA, d, v)
    #await SLEEP(1000)
    print("done nakahara!")

#テスト
async def test():
    #MV_DG(MOTOR1, 1000, FAST)
    #motor.run(port.A, 1000)
    #await straight(100, FAST)
    print("done test!")    

#赤色黄色棒
async def stickProcess():
    #オブジェクトまで行く
    await straight(100, FAST)
    #全部取る
    await nakahara(-115, MID)
    #下がって旋回
    await straight(-400, FAST)
    await turn(-263, MID) 
    #置き場まで行く
    await straight(1300,FAST)
    await turn(263, MID)
    #黄色を指定の場所にセット
    await turn(131, MID)
    await straight(450, FAST)
    #赤色だけをとる
    await nakahara(115, MID)
    await straight(-100, FAST)
    await nakahara(-115, MID)
    #下がる
    await straight(-200, FAST)
    #赤色を指定の場所にセット
    await turn(-255, MID)
    await straight(350, FAST)
    await nakahara(115, MID)
    print("done stickProcess!")

#引くやつ
def pullProcess():
    #オブジェクトまで行く
    #引く
    #旋回
    print("done pullProcess!")

#ボルトの色を読み取る
def readColor():
    #ボルト置き場に行く
    #読み取る
    
    print("done readColor!")

#閉めるやつ
def closeProcess():
    #オブジェクトまで行く
    #通り過ぎるときに閉める
    print("done closeProcess!")

#正方形のオブジェクト
def squareProcess():
    #オブジェクトまで行く
    #とる
    #旋回
    #向きを整える
    #置き場まで行く
    #置く
    print("done squareProcess!")

#ボルト
def boltProcess():
    print("done boltProcess!")

#旗
def flagProcess():
    print("done flagProcess!")

#メイン処理
async def main():
    
    await stickProcess()
    
    sleep(10)

    
runloop.run(main())
