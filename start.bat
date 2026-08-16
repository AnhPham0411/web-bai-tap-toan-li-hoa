@echo off
rem Mo web Toan 10 tren trinh duyet (can Python hoac Node).
setlocal
set PORT=8080

where python >nul 2>nul
if %errorlevel%==0 (
    echo Dang chay server tai http://localhost:%PORT%
    start "" http://localhost:%PORT%
    python -m http.server %PORT% --bind 127.0.0.1
    goto :eof
)

where npx >nul 2>nul
if %errorlevel%==0 (
    echo Dang chay server tai http://localhost:%PORT%
    start "" http://localhost:%PORT%
    npx --yes serve -l %PORT% .
    goto :eof
)

echo Khong tim thay Python hoac Node.js.
echo Hay cai mot trong hai, hoac dung tien ich Live Server cua VS Code.
pause
