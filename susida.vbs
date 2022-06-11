set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep (5000)
Dim a
a = 0
Do Until a = 600
WScript.Sleep (100)
  WshShell.SendKeys "abcdefghijklmnopqrstuvwxyz"
a = a + 1
Loop 
