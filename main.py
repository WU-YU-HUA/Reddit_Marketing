from with_search import with_main
from without_search import without_main
from utilize import run_bat
import threading

event = threading.Event()
titles = []
social = input("Please Enter Parameter1: ") #Plz Enter Social Name (e.g. OLED_Gaming): 
time = input("Please Enter Parameter2: ") #Plz Enter SortedTime (e.g. day): 
sorted = input("Please Enter Parameter3: ") #Plz Enter Sorted (e.g. top, best): 
keyword = input("Please Enter Parameter4: ") #Plz Enter Keyword you want: 

run_bat()

if keyword.strip() == "":
    without_main(social, time, sorted)
else:
    with_main(social, time, sorted, keyword)
