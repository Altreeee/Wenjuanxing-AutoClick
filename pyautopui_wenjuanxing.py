#尝试使用pyautogui控制鼠标自动点击填写问卷
#别再忘了复制网址了！！！！！

from time import sleep
import pyautogui
from random import *
import winsound

#循环次数
#每个13秒
num = 200

for i in range(num):

    pyautogui.FAILSAFE = False
    #pyautogui.PAUSE = 1   

    #第一题 
    pyautogui.moveTo(x=902,y=506,duration=0.25)
    pyautogui.click(x=902,y=506,button='left')
    sleep(0.1)

    pyautogui.moveTo(x=817,y=793,duration=0.25)
    pyautogui.click(817,793,button='left')

    '''#移动到空白处点击
    pyautogui.moveRel(-500,0,duration=0.1)   # 第一个参数是左右移动像素值，第二个是上下，
    pyautogui.click(pyautogui.position())'''

    #第二题
    #pyautogui.moveTo(x=736,y=707,duration=0.25)
    pyautogui.click(x=736,y=707,button='left')
    q2 = random()
    if 0 <= q2 <= 0.2:  #初中
        pyautogui.click(732,793,button='left')
    elif 0.16 < q2 <= 0.4:  #高中
        pyautogui.click(732,859,button='left')
    elif 0.4 < q2 <=0.5:    #大专
        pyautogui.click(732,906,button='left')
    elif 0.5 < q2 <=0.9:    #benke
        pyautogui.click(732,943,button='left')
    else:   #研究生
        pyautogui.click(732,987,button='left')
    

    #第三题
    q3 = random()
    if 0 <= q3 <= 0.3:
        pyautogui.click(x=577,y=894,button='left')
    else:
        pyautogui.click(574,944,button='left')

    #拖动进度条
    pyautogui.moveTo(x=2146,y=367,duration=0.25)
    pyautogui.dragTo(2150,469,duration=0.5)   #上下距离469-367=102

    #第四题
    q4 = random()
    if 0 <= q4 <= 0.2:
        pyautogui.click(x=577,y=898,button='left')
    else:
        pyautogui.click(577,953,button='left')

    pyautogui.moveTo(x=2145,y=447,duration=0.25)
    pyautogui.dragTo(2150,447+102,duration=0.5)   #两项上下距离469-367=102

    
    #5
    q5 = random()
    if 0 <= q5 <=0.3:
        pyautogui.click(x=577,y=909,button='left')
    elif 0.3 < q5 <=0.5:
        pyautogui.click(577,959,button='left')
    else:
        pyautogui.click(577,1019,button='left')


    pyautogui.moveTo(x=2145,y=606,duration=0.25)
    pyautogui.dragTo(2150,606+137,duration=0.5)   #三项上下距离137

    #6
    pyautogui.click(x=577,y=894,button='left')
    pyautogui.moveTo(x=2145,y=697,duration=0.25)
    pyautogui.dragTo(2150,697+137,duration=0.5)   #三项上下距离137

    #点7挪8
    pyautogui.click(x=577,y=894,button='left')
    pyautogui.moveTo(x=2145,y=775,duration=0.25)
    pyautogui.dragTo(2150,775+137,duration=0.5)   #三项上下距离137

    #8
    pyautogui.click(x=577,y=894,button='left')
    pyautogui.moveTo(x=2145,y=856,duration=0.25)
    pyautogui.dragTo(2150,856+137,duration=0.5)   #三项上下距离137

    q9 = random()
    if 0 <= q9 <= 0.4:
        pyautogui.click(573,856,button='left')
    else:
        pyautogui.click(576,902,button='left')
    sleep(0.2)

    q10 = random()
    if 0 <= q10 <= 0.3:
        pyautogui.click(575,1105,button='left')
    else:
        pyautogui.click(577,1144,button='left')
    sleep(0.2)

    pyautogui.click(1051,1319,button='left')
    sleep(2)
    
    #点击智能验证按钮
    pyautogui.click(897,1107,button='left')
    sleep(4)

    #滑动滑块
    #模拟人先滑过缺口，再滑回来的动作
    pyautogui.mouseDown()
    pyautogui.moveTo(900,1107,duration=1, tween=pyautogui.easeInQuad)
    pyautogui.moveTo(1200,1107,duration=1, tween=pyautogui.easeOutQuad)
    pyautogui.mouseUp()
    

    #点击取消
    pyautogui.click(904,839,button='left')
    sleep(random())

    pyautogui.click(611,77,button='left')
    pyautogui.hotkey('ctrl','v')
    pyautogui.typewrite('\n')  
    sleep(1)

    pyautogui.moveTo(321,642,duration=0.25)
    pyautogui.scroll(2000)  # 向上滚动；
    sleep(0.5)

delay = 2000  # 3000毫秒即3秒
freq = 390  # 设置响声频率

# 闹钟响起
winsound.Beep(freq, delay)
  

    
    

        


    







'''

'''









