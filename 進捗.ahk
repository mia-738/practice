#SingleInstance
  SetTimer, rChangeButtonNames, 50
  MsgBox, 0x4, 進捗, 進捗だめです
return
 
rChangeButtonNames: 
  IfWinNotExist, 進捗
    return ; MsgBox が表示されるのを待ちます
  SetTimer, rChangeButtonNames, Off
  WinActivate
  ControlSetText, Button1, 了解(&A)
  ControlSetText, Button2, はい(&D)
return