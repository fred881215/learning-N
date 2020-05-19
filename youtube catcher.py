import requests as re
import tkinter as tk
from bs4 import BeautifulSoup

window=tk.Tk()
window.title('Youtube Catcher')
window.geometry('800x600')

header_label=tk.Label(window,text='test')
header_label.pack()

url_frame=tk.Frame(window)
url_frame.pack(side=tk.TOP)
url_label=tk.Label(url_frame,text='網址')
url_label.pack(side=tk.LEFT)
url_entry=tk.Entry(url_frame)
url_entry.pack(side=tk.LEFT)

r = re.get(url_entry)

result_label=tk.Label(window)
result_label.pack()

calculate_btn=tk.Button(window,text='載入')
calculate_btn.pack()

window.mainloop()