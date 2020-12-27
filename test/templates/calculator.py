import tkinter as tk
 
calc = tk.Tk()
calc.title("Calculator")
calc.geometry("300x300")
 
def calculate(event):   # func함수이름을 calculate로 바꿔줬습니다. 호출하는 부분도 같이 바꿔주세요.
    value = tk.Entry.get(display)
    if value != '':
        result = eval(value)
        print(result)
        display.delete(0,tk.END)
        display.insert(0,result)
 
def clear(event):            # C 버튼과 Esc 키를 위한 함수 입니다.
    display.delete(0,tk.END)  # 내용 삭제
     
display = tk.Entry(calc, width=20)
display.pack()
 
button_e = tk.Button(calc, text='=', width=5)  # = 버튼 추가
button_e.bind('<Button-1>',calculate)          # 버튼에 클릭 이벤트 추가
button_e.pack()
 
button_c = tk.Button(calc, text='c', width=5)  # C버튼추가. text속성은 버튼에 표시할 문자입니다.
button_c.bind('<Button-1>',clear)           # <Button-1> 이벤트는 마우스 왼쪽클릭 이벤트입니다.
button_c.pack()
 
calc.bind('<Return>', calculate)
calc.bind('<Escape>', clear)  # Esc 키도 C버튼과 통일한 기능을 하도록 연결해줬습니다.
 
calc.mainloop()