; ============================================
; Auto Clicker for Remote Desktop
; 自动点击器 - 用于远程桌面场景
; 
; 功能：监控常见弹窗并自动点击"Yes"/"Allow"按钮
; 适用场景：通过Tailscale远程连接时，避免在手机小屏幕上点击困难
; ============================================

#NoEnv
#SingleInstance Force
#Persistent
SetTitleMatchMode, 2  ; 窗口标题部分匹配
SetControlDelay, -1

; ============================================
; 配置部分
; ============================================

; 调试模式：设置为1显示调试信息，0关闭
DEBUG_MODE := 0

; 检查间隔（毫秒）
CHECK_INTERVAL := 1000

; 需要监控的窗口和控件列表
; 格式：窗口标题, 控件文本, 控件类
; 窗口标题可以使用部分匹配
; 控件文本是按钮上显示的文字
; 控件类可以是Button、Button1、Button2等

MonitorList := []

; 1. Visual Studio Code - 信任作者弹窗
MonitorList.Push({WindowTitle: "Visual Studio Code"
    , ControlText: "Yes"
    , ControlClass: "Button"
    , Description: "VS Code信任作者弹窗"})

; 2. 浏览器下载弹窗 - Chrome
MonitorList.Push({WindowTitle: "Chrome"
    , ControlText: "允许"
    , ControlClass: "Button"
    , Description: "Chrome下载允许弹窗"})

MonitorList.Push({WindowTitle: "Chrome"
    , ControlText: "Allow"
    , ControlClass: "Button"
    , Description: "Chrome下载允许弹窗(英文)"})

; 3. 浏览器下载弹窗 - Edge
MonitorList.Push({WindowTitle: "Microsoft Edge"
    , ControlText: "允许"
    , ControlClass: "Button"
    , Description: "Edge下载允许弹窗"})

MonitorList.Push({WindowTitle: "Microsoft Edge"
    , ControlText: "Allow"
    , ControlClass: "Button"
    , Description: "Edge下载允许弹窗(英文)"})

; 4. 浏览器下载弹窗 - Firefox
MonitorList.Push({WindowTitle: "Mozilla Firefox"
    , ControlText: "允许"
    , ControlClass: "Button"
    , Description: "Firefox下载允许弹窗"})

MonitorList.Push({WindowTitle: "Mozilla Firefox"
    , ControlText: "Allow"
    , ControlClass: "Button"
    , Description: "Firefox下载允许弹窗(英文)"})

; 5. Windows安全警告弹窗
MonitorList.Push({WindowTitle: "Windows 安全"
    , ControlText: "允许"
    , ControlClass: "Button"
    , Description: "Windows安全警告弹窗"})

MonitorList.Push({WindowTitle: "Windows Security"
    , ControlText: "Allow"
    , ControlClass: "Button"
    , Description: "Windows安全警告弹窗(英文)"})

; 6. 用户账户控制(UAC)弹窗
MonitorList.Push({WindowTitle: "用户账户控制"
    , ControlText: "是"
    , ControlClass: "Button"
    , Description: "用户账户控制弹窗"})

MonitorList.Push({WindowTitle: "User Account Control"
    , ControlText: "Yes"
    , ControlClass: "Button"
    , Description: "用户账户控制弹窗(英文)"})

; ============================================
; 全局变量
; ============================================

; 记录已处理的窗口，避免重复点击
ProcessedWindows := {}

; ============================================
; 主监控循环
; ============================================

SetTimer, MonitorWindows, %CHECK_INTERVAL%
return

MonitorWindows:
    ; 遍历所有需要监控的窗口类型
    for index, monitor in MonitorList
    {
        WindowTitle := monitor.WindowTitle
        ControlText := monitor.ControlText
        ControlClass := monitor.ControlClass
        Description := monitor.Description
        
        ; 查找窗口
        WinGet, windowId, ID, %WindowTitle%
        
        if (windowId)
        {
            ; 构建窗口唯一标识符
            windowKey := WindowTitle . "|" . windowId
            
            ; 检查是否已经处理过这个窗口
            if (ProcessedWindows.HasKey(windowKey))
            {
                if (DEBUG_MODE)
                    DebugLog("跳过已处理的窗口: " . Description . " (ID: " . windowId . ")")
                continue
            }
            
            if (DEBUG_MODE)
                DebugLog("找到窗口: " . Description . " (ID: " . windowId . ")")
            
            ; 尝试查找并点击按钮
            if (ClickButtonInWindow(windowId, ControlText, ControlClass))
            {
                ; 记录已处理的窗口
                ProcessedWindows[windowKey] := A_Now
                DebugLog("✅ 自动点击成功: " . Description)
                
                ; 播放成功提示音
                SoundPlay, *64
            }
            else
            {
                if (DEBUG_MODE)
                    DebugLog("未找到按钮: " . ControlText . " 在窗口: " . Description)
            }
        }
    }
    
    ; 清理过期的记录（30秒前的记录）
    CleanupProcessedWindows()
return

; ============================================
; 函数：在窗口中点击按钮
; ============================================

ClickButtonInWindow(windowId, buttonText, controlClass)
{
    ; 激活窗口（但不抢焦点，避免干扰用户）
    ; WinActivate, ahk_id %windowId%
    
    ; 等待窗口激活
    ; WinWaitActive, ahk_id %windowId%, , 0.5
    
    ; 查找包含指定文本的按钮
    ControlGet, controlList, List, , , ahk_id %windowId%
    
    ; 方法1：使用ControlClick通过文本查找
    try
    {
        ControlClick, %buttonText%, ahk_id %windowId%
        return 1
    }
    
    ; 方法2：使用ControlClick通过类名查找
    try
    {
        ControlClick, %controlClass%, ahk_id %windowId%
        return 1
    }
    
    ; 方法3：使用更精确的控件查找
    WinGet, controlList, ControlList, ahk_id %windowId%
    
    Loop, Parse, controlList, `n
    {
        controlId := A_LoopField
        ControlGetText, controlText, %controlId%, ahk_id %windowId%
        
        ; 检查控件文本是否包含目标文本
        if (InStr(controlText, buttonText))
        {
            ControlClick, %controlId%, ahk_id %windowId%
            return 1
        }
        
        ; 检查控件类名
        ControlGet, controlClassNN, ClassNN, %controlId%, ahk_id %windowId%
        if (InStr(controlClassNN, controlClass))
        {
            ControlClick, %controlId%, ahk_id %windowId%
            return 1
        }
    }
    
    return 0
}

; ============================================
; 函数：清理过期的窗口记录
; ============================================

CleanupProcessedWindows()
{
    global ProcessedWindows
    currentTime := A_Now
    threshold := 30  ; 30秒
    
    for windowKey, timestamp in ProcessedWindows.Clone()
    {
        ; 计算时间差（秒）
        timeDiff := (currentTime - timestamp) * 86400
        
        if (timeDiff > threshold)
        {
            ProcessedWindows.Delete(windowKey)
            if (DEBUG_MODE)
                DebugLog("清理过期记录: " . windowKey)
        }
    }
}

; ============================================
; 函数：调试日志
; ============================================

DebugLog(message)
{
    global DEBUG_MODE
    if (DEBUG_MODE)
    {
        FormatTime, currentTime, , yyyy-MM-dd HH:mm:ss
        FileAppend, [%currentTime%] %message%`n, %A_ScriptDir%\auto_clicker.log
    }
}

; ============================================
; 函数：显示状态信息
; ============================================

ShowStatus()
{
    global ProcessedWindows, MonitorList
    statusMsg := "自动点击器状态`n`n"
    statusMsg .= "监控的弹窗类型:`n"
    
    for index, monitor in MonitorList
    {
        statusMsg .= "  • " . monitor.Description . "`n"
    }
    
    statusMsg .= "`n已处理的窗口: " . ProcessedWindows.Count() . "`n"
    
    MsgBox, %statusMsg%
}

; ============================================
; 热键配置
; ============================================

; F1: 显示状态
F1::
    ShowStatus()
return

; F2: 切换调试模式
F2::
    global DEBUG_MODE
    DEBUG_MODE := !DEBUG_MODE
    if (DEBUG_MODE)
        MsgBox, 调试模式已开启
    else
        MsgBox, 调试模式已关闭
return

; F3: 清空已处理记录
F3::
    global ProcessedWindows
    ProcessedWindows := {}
    MsgBox, 已清空处理记录
return

; F4: 重新加载脚本
F4::
    Reload
return

; F12: 退出脚本
F12::
    MsgBox, 自动点击器正在退出...
    ExitApp
return

; ============================================
; 启动信息
; ============================================

MsgBox, 0, 自动点击器已启动, 
(
自动点击器已启动！

功能：自动点击常见弹窗的"Yes"/"Allow"按钮
适用：通过Tailscale远程连接时，避免在手机小屏幕上点击困难

热键说明：
• F1: 显示状态
• F2: 切换调试模式
• F3: 清空处理记录
• F4: 重新加载脚本
• F12: 退出脚本

脚本将静默运行在系统托盘。
)

; 隐藏主窗口
#NoTrayIcon
return