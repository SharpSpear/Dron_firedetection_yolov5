@echo off
"../myenv/Scripts/python.exe" "detect.py" --weights best.pt --source rtsp://192.168.2.119:554 --view-img --nosave
pause