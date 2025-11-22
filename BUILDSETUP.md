# BUILD STEP


```bash

pyinstaller --noconfirm --onefile --windowed ^
  --add-data "assets/fonts;assets/fonts" ^
  main.py

```
## Folder

Windows: dùng dấu ;

Linux/macOS: dùng dấu :

--add-data sẽ copy folder assets/fonts vào thư mục tạm của PyInstaller khi chạy EXE.
```bash

project/
│ main.py
└─ assets/
   └─ fonts/
       └─ Roboto-Regular.ttf
```