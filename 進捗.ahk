#SingleInstance
  SetTimer, rChangeButtonNames, 50
  MsgBox, 0x4, �i��, �i�����߂ł�
return
 
rChangeButtonNames: 
  IfWinNotExist, �i��
    return ; MsgBox ���\�������̂�҂��܂�
  SetTimer, rChangeButtonNames, Off
  WinActivate
  ControlSetText, Button1, ����(&A)
  ControlSetText, Button2, �͂�(&D)
return