pyinstaller.exe --onefile --noconsole main.py
pyinstaller.exe --onefile --noconsole readExcel.py
rmdir build
del *.spec