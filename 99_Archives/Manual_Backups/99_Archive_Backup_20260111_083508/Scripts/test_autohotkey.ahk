; 测试脚本 - 验证AutoHotkey是否正常工作
#NoEnv
#SingleInstance Force

MsgBox, 0, 测试成功, AutoHotkey 安装成功！`n`n自动点击器已准备就绪。`n`n点击确定后，脚本将退出。

; 显示系统信息
ahkVersion := A_AhkVersion
osVersion := A_OSVersion
scriptDir := A_ScriptDir

infoMsg =
(
AutoHotkey 版本: %ahkVersion%
操作系统: %osVersion%
脚本目录: %scriptDir%

自动点击器功能:
- 监控 VS Code 信任弹窗
- 监控浏览器下载弹窗
- 监控 Windows 安全警告
- 监控 UAC 弹窗

按 F1 显示状态
按 F12 退出脚本
)

MsgBox, 0, 系统信息, %infoMsg%

ExitApp