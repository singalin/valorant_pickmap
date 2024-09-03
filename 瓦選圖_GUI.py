import random
import time
import tkinter

global maplist
maplist = list("天漠之峽 日落之城 劫境之地 深海遺珠 深窟幽境 極地寒港 義境空島 熱帶樂園 蓮華古城 遺落境地 雙塔迷城".split())

global banlist
banlist=['' for i in range(11)]

def pickmap(banlist):
    result = random.choice(maplist)
    if result in banlist:
        return pickmap(banlist)
    else: 
        return result

def pick():
    global banlist
    answer = pickmap(banlist)
    label2["text"]="抽出的結果是："+answer
    for i in range(11):
        print(maplist[i])
        if maplist[i] == answer:
            match i:
                case 0:
                    button_0['bg'] = "yellow"
                    break
                case 1:
                    button_1['bg'] = "yellow"
                    break
                case 2:
                    button_2['bg'] = "yellow"
                    break
                case 3:
                    button_3['bg'] = "yellow"
                    break
                case 4:
                    button_4['bg'] = "yellow"
                    break
                case 5:
                    button_5['bg'] = "yellow"
                    break
                case 6:
                    button_6['bg'] = "yellow"
                    break
                case 7:
                    button_7['bg'] = "yellow"
                    break
                case 8:
                    button_8['bg'] = "yellow"
                    break
                case 9:
                    button_9['bg'] = "yellow"
                    break
                case 10:
                    button_10['bg'] = "yellow"
                    break
                case _:
                    print("bug")
def addbanlist0():
    global banlist
    if banlist[0] == '天漠之峽':
        banlist[0]=''
        label["text"]=renewbanlistname()
        button_0['bg']=default_color
    else:
        banlist[0]="天漠之峽"
        label["text"]=renewbanlistname()
        button_0['bg']="red"

def addbanlist1():
    global banlist
    if banlist[1] == '日落之城':
        banlist[1]=''
        label["text"]=renewbanlistname()
        button_1['bg']=default_color
    else:
        banlist[1]="日落之城"
        label["text"]=renewbanlistname()
        button_1['bg']="red"

def addbanlist2():
    global banlist
    if banlist[2] == '劫境之地':
        banlist[2]=''
        label["text"]=renewbanlistname()
        button_2['bg']=default_color
    else:
        banlist[2]="劫境之地"
        label["text"]=renewbanlistname()
        button_2['bg']="red"

def addbanlist3():
    global banlist
    if banlist[3] == '深海遺珠':
        banlist[3]=''
        label["text"]=renewbanlistname()
        button_3['bg']=default_color
    else:
        banlist[3]="深海遺珠"
        label["text"]=renewbanlistname()
        button_3['bg']="red"
        
def addbanlist4():
    global banlist
    if banlist[4] == '深窟幽境':
        banlist[4]=''
        label["text"]=renewbanlistname()
        button_4['bg']=default_color
    else:
        banlist[4]="深窟幽境"
        label["text"]=renewbanlistname()
        button_4['bg']="red"

def addbanlist5():
    global banlist
    if banlist[5] == '極地寒港':
        banlist[5]=''
        label["text"]=renewbanlistname()
        button_5['bg']=default_color
    else:
        banlist[5]="極地寒港"
        label["text"]=renewbanlistname()
        button_5['bg']="red"

def addbanlist6():
    global banlist
    if banlist[6] == '義境空島':
        banlist[6]=''
        label["text"]=renewbanlistname()
        button_6['bg']=default_color
    else:
        banlist[6]="義境空島"
        label["text"]=renewbanlistname()
        button_6['bg']="red"

def addbanlist7():
    global banlist
    if banlist[7] == '熱帶樂園':
        banlist[7]=''
        label["text"]=renewbanlistname()
        button_7['bg']=default_color
    else:
        banlist[7]="熱帶樂園"
        label["text"]=renewbanlistname()
        button_7['bg']="red"
        
def addbanlist8():
    global banlist
    if banlist[8] == '蓮華古城':
        banlist[8]=''
        label["text"]=renewbanlistname()
        button_8['bg']=default_color
    else:
        banlist[8]="蓮華古城"
        label["text"]=renewbanlistname()
        button_8['bg']="red"

def addbanlist9():
    global banlist
    if banlist[9] == '遺落境地':
        banlist[9]=''
        label["text"]=renewbanlistname()
        button_9['bg']=default_color
    else:
        banlist[9]="遺落境地"
        label["text"]=renewbanlistname()
        button_9['bg']="red"

def addbanlist10():
    global banlist
    if banlist[10] == '雙塔迷城':
        banlist[10]=''
        label["text"]=renewbanlistname()
        button_10['bg']=default_color
    else:
        banlist[10]="雙塔迷城"
        label["text"]=renewbanlistname()
        button_10['bg']="red"

def renewbanlistname():
    #print(banlist)
    temp=list()
    emp=True
    for i in banlist:
        if i!='':
            temp.append(i)
            emp=False
    strreturn="目前已禁用地圖："+"、".join(temp)
    if emp:
        strreturn="目前沒有禁用圖"
    #for i in banlist:
        #if i=='天漠之峽':
            #strreturn+=str(i)
        #elif i!=[] or i=='':
            #strreturn+="、"
            #strreturn+=str(i)
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
button_0 = tkinter.Button(text="天漠之峽",command=addbanlist0)
button_0.place(x=20,y=150)
button_1 = tkinter.Button(text="日落之城",command=addbanlist1)
button_1.place(x=100,y=150)
button_2 = tkinter.Button(text="劫境之地",command=addbanlist2)
button_2.place(x=180,y=150)
button_3 = tkinter.Button(text="深海遺珠",command=addbanlist3)
button_3.place(x=260,y=150)
button_4 = tkinter.Button(text="深窟幽境",command=addbanlist4)
button_4.place(x=20,y=200)
button_5 = tkinter.Button(text="極地寒港",command=addbanlist5)
button_5.place(x=100,y=200)
button_6 = tkinter.Button(text="義境空島",command=addbanlist6)
button_6.place(x=180,y=200)
button_7 = tkinter.Button(text="熱帶樂園",command=addbanlist7)
button_7.place(x=260,y=200)
button_8 = tkinter.Button(text="蓮華古城",command=addbanlist8)
button_8.place(x=20,y=250)
button_9 = tkinter.Button(text="遺落境地",command=addbanlist9)
button_9.place(x=100,y=250)
button_10 = tkinter.Button(text="雙塔迷城",command=addbanlist10)
button_10.place(x=180,y=250)
default_color = button_0.cget('bg')

root.mainloop()
#待新增
#*背景圖*
#*按鈕變色*
