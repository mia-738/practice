set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep (3000)
Dim a
a = 0

Do
b = InputBox("")
Loop Until IsNumeric(ip)

Do 
WScript.Sleep (100)
WshShell.SendKeys "{F5}"
a = a + 1
Loop Until a = b
