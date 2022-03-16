from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") 

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # 여러줄가능

e = Entry(root, width=30) # 한줄만가능 로그인창
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # 1번째 줄의 0번째 column위치 부터 END 까지 가져오라는뜻
    print(e.get())
    
    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()