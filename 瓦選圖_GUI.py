import random
import time
import tkinter

maplist = list("天漠之峽 日落之城 劫境之地 深海遺珠 深窟幽境 極地寒港 義境空島 熱帶樂園 蓮華古城 遺落境地 雙塔迷城".split())
banlist=['' for i in range(11)]

def pickmap():
    map_ok = [item for item in maplist if item not in banlist]
    return random.choice(map_ok)

def pick():
    for i in button_list:
        if i['bg']=='yellow':
            i['bg']=default_color
    answer = pickmap()
    label2["text"]="抽出的結果是："+answer
    button_list[maplist.index(answer)]['bg']='yellow'

def addbanlist(map_num):
    global banlist
    global maplist
    print("%s,%s"%(banlist[map_num],maplist[map_num]))
    if banlist[map_num] == maplist[map_num]:
        banlist[map_num] = ''
        label["text"]=renewbanlistname()
        button_list[map_num]['bg']=default_color
    else:
        banlist[map_num] = maplist[map_num]
        label["text"]=renewbanlistname()
        button_list[map_num]['bg']="red"


def renewbanlistname():
    temp=list()
    emp=True
    for i in banlist:
        if i!='':
            temp.append(i)
            emp=False
    strreturn="目前已禁用地圖："+"、".join(temp)
    if emp:
        strreturn="目前沒有禁用圖"
    return strreturn
        
root = tkinter.Tk()
root.title("特戰英豪選圖器")
root.geometry("400x400")
label = tkinter.Label(root,text="目前沒有禁用圖")
label.place(x=20,y=10)
label2 = tkinter.Label(root,text="抽出的結果是：")
label2.place(x=20,y=55)
button = tkinter.Button(text="抽圖",command=pick)
button.place(x=20,y=100)

button_list=[]
for i in range(11):
    new_button = tkinter.Button(text=maplist[i],command=lambda i=i: addbanlist(i))
    new_button.place(x=20+80*(i%4),y=150+50*(i//4))
    button_list.append(new_button)
default_color = button_list[0].cget('bg')

root.mainloop()
#待新增
#*背景圖*
#*按鈕變色*
