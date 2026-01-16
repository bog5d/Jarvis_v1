Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\Start_Jarvis_HUD.bat" & chr(34), 0
WshShell.Run chr(34) & "C:\Users\王波\OneDrive - Personal\my_system\Jarvis_v1\Start_Jarvis_Dashboard.bat" & chr(34), 0
Set WshShell = Nothing