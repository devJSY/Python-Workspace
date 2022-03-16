from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") 

listbox = Listbox(root, selectmode="extended", height=0) 
# selectmode="extended" 여러개선택가능 , selectmode="single" 한개만 선택가능
# height=0 - 리스트가 포함된값 전부 띄어줌, height=3 - 3개만 보여줌

listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) # 맨앞항목삭제 - 0 , 맨끝항목삭제 - END
    
    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")
    
    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째 부터 3번째까지의 항목 : ", listbox.get(0,2))
    
    # 선택된 항목 확인 (위치로 반환 (ex) (1,2,3) )
    print("선택된 항목 : ", listbox.curselection())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()