pyinstaller --noconfirm --onefile --name "Reddit" .\with_search.py && move ".\dist\Reddit.exe" ".\" && rmdir /s /q ".\dist" && rmdir /s /q ".\build" && del ".\Reddit.spec"

pyinstaller --noconfirm --onefile --name "RedditNoSearch" .\without_search.py && move ".\dist\RedditNoSearch.exe" ".\" && rmdir /s /q ".\dist" && rmdir /s /q ".\build" && del ".\RedditNoSearch.spec"