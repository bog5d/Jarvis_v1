#NoEnv
#SingleInstance Force
#Persistent
SetBatchLines, -1
CoordMode, Pixel, Screen
CoordMode, Mouse, Screen

global ClickCount := 0
SetTimer, CheckButtons, 600
Menu, Tray, Tip, VS Code 按钮点击器 (修正版)
return

CheckButtons:
    if !WinActive("ahk_exe Code.exe")
        return
    
    WinGetPos, wx, wy, ww, wh, A
    
    ; 只搜索中心区域，排除标题栏
    sx1 := wx + (ww // 4)
    sy1 := wy + 100
    sx2 := wx + (ww * 3 // 4)
    sy2 := wy + (wh * 3 // 4)
    
    PixelSearch, px, py, sx1, sy1, sx2, sy2, 0x0078D4, 20, Fast RGB
    if (ErrorLevel = 0)
    {
        Click, %px%, %py%
        ClickCount++
        TrayTip, OK, 点击 %ClickCount%, 1
        Sleep, 2000
    }
return

F1::MsgBox, 点击: %ClickCount%
F12::ExitApp
