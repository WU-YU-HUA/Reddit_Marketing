pyinstaller --noconfirm --onefile --name "Reddit" .\with_search.py && move ".\dist\Reddit.exe" ".\" && rmdir /s /q ".\dist" && rmdir /s /q ".\build" && del ".\Reddit.spec"

pyinstaller --noconfirm --onefile --name "RedditNoSearch" .\without_search.py && move ".\dist\RedditNoSearch.exe" ".\" && rmdir /s /q ".\dist" && rmdir /s /q ".\build" && del ".\RedditNoSearch.spec"


Param1: Enter Social Name (e.g. OLED_Gaming): 
Param2: Enter SortedTime (e.g. day): 
Param3: Enter Sorted (e.g. top, best): 
Param4: Enter Keyword you want: 