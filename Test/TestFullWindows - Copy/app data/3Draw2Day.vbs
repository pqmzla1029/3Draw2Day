Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c 3Draw2Day.bat"
oShell.Run strArgs, 0, false