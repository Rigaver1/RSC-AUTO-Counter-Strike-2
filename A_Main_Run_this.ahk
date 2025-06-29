#NoEnv
#MaxThreadsPerHotkey 9999
#SingleInstance Force
DetectHiddenWindows, On
SetTitleMatchMode, 2
WinSetTitle, % "MyAHKScriptWindow"
; 👇 ДОБАВЬ ЭТО
Gui, +AlwaysOnTop +ToolWindow -SysMenu -Caption
Gui, Add, Text,, Control Window for Python
Gui, Show, Hide, MyAHKScriptWindow
OnMessage(0x8888, "ExternalTrigger")

#KeyHistory 0
#MaxMem 99999999999
#MaxThreads 255
#MaxThreadsBuffer On
#InstallMouseHook
#InstallKeybdHook
Process, Priority, , H
ListLines Off
SetWorkingDir %A_ScriptDir%
SetKeyDelay, -1
SetControlDelay, -1
SetBatchLines, -1

; ---------------- GLOBALS ----------------
Global Center_X := (A_ScreenWidth // 2) + 1
Global Center_Y := (A_ScreenHeight // 2) + 1

Global sens := 1.80
Global Zoomsens := 0.75
Global reaction_min := 25
Global reaction_max := 100
Global RFL := 50
Global RFH := 80
Global Speed := 1

Global CrossHairTrans := 220
Global SelectedCrosshair := "+"
Global CrossHairSize := 20
Global CrossHairColor := "Green"

Global Magnifier := False
Global Zoom := 1
Global Size := 30
Global Delay := 10
Global MagnifierTrans := 220


Global Key_AK            := "f1"
Global Key_M4A1          := "f2"
Global Key_M4A4          := "f3"
Global Key_Famas         := "f4"
Global Key_Galil         := "f5"
Global Key_UMP           := "f6"
Global Key_AUG           := "f7"
Global Key_SG            := "f8"
Global Key_Mac10         := "f9"
Global Key_CZ75          := "f10"
Global Key_P90           := "f11"
Global Key_MP5           := "f12"
Global Key_UniversalRCS  := "Numpad9"
Global Key_RCoff         := "Numpad0"

Global key_180 := "v"
Global Key_shoot := "LButton"
Global Key_Zoom := "Alt"
Global Key_RapidFire := "XButton2"
Global Key_PixelBot := "XButton1"
Global Key_BHOP := "x"
Global Key_Safety := "n"

Global humanizer
Global waitdivider

Global GuiVisible := False
Global BHOPT := False
Global RapidFireT := False
Global TriggerBotT := False
Global TurnAroundT := False
Global AcceptT := False
Global CrosshairT := False
Global ReturnMouseT := True
Global RCSNotification := True
Global TriggerBotNotification := True
Global RecoilSafety := False
Global UniversalRCS := False
Global Legit := False
Global Perfect := False
Global ScrollWheel := False
Global SpeechT := False
Global CounterStrafeT := False
Global HumanizeUniversal := False
Global ReloadT := False
Global SniperQQ := False

Global RCSPercentX := 100
Global RCSPercentY := 100
Global UniversalRCSPercentY := 100
Global UniversalRCSPercentX := 100

global GunPattern := "Recoil Off", pattern

Global yOffset := 0, xOffset := 0

gosub ReadAllsettings
gosub GunKeys

scripts := ["counterstrafe_B.exe", "counterstrafe_F.exe", "counterstrafe_L.exe", "counterstrafe_R.exe"]

ch1 := Chr(84), ch2 := Chr(72), ch3 := Chr(73), ch4 := Chr(83), ch5 := Chr(32), ch6 := Chr(83), ch7 := Chr(82), ch8 := Chr(73), ch9 := Chr(80), ch10 := Chr(84), ch11 := Chr(32), ch12 := Chr(73), ch13 := Chr(83), ch14 := Chr(32), ch15 := Chr(70), ch16 := Chr(82), ch17 := Chr(69), ch18 := Chr(69), pair1 := ch1 . ch2, pair2 := ch3 . ch4, pair3 := ch5 . ch6, pair4 := ch7 . ch8, pair5 := ch9 . ch10, pair6 := ch11 . ch12, pair7 := ch13 . ch14, pair8 := ch15 . ch16, pair9 := ch17 . ch18, str1 := pair1 . pair2, str2 := pair3 . pair4, str3 := pair5 . pair6, str4 := pair7 . pair8, str5 := pair9, temp1 := str1 . str2, temp2 := str3 . str4, temp3 := temp1 . temp2, e1 := temp3 . str5


Version := "V1.13"
/*
Removed download msg with bar
removed useless code / comments causing errors
Updated Zoom to properly work with hotkeys
updated A Main to not have error on launch
Updated Default CS hotkeys
Updated Gun notification to be a GUI Display. No longer a tooltip
Updated Extras GUI

ToDo:  | New GUI | bug when pressing hotkeys and clicking checkbox for Mag and Cross | Redo Saving/Reading to reduce code | | | | RapidFire More GUI options | | | | | | Find Way to Auto Select Weapon
*/

VarSetCapacity(INPUT, 28)
VarSetCapacity(MOUSEINPUT, 24)
VarSetCapacity(KEYBDINPUT, 16)
VarSetCapacity(HARDWAREINPUT, 8)
VarSetCapacity(INPUT_union, 24)


Gosub StartSequence
#Include Subroutes.AHK
#Include Functions.AHK
#Include Zoom.AHK
#Include Crosshair.AHK
; ---------------- Внешний вызов через OnMessage ----------------
OnMessage(0x8888, "ExternalTrigger")

ExternalTrigger(wParam, lParam, msg, hwnd) {
    if (wParam = 1) {
        GunSelection("M4A1", GunConfigs["M4A1"].sense, GunConfigs["M4A1"].zoom)
pattern := GunConfigs["M4A1"].pattern
  }
    else if (wParam = 2) {
        GunSelection("AK", GunConfigs["AK"].sense, GunConfigs["AK"].zoom)
        pattern := GunConfigs["AK"].pattern
  }
   else if (wParam = 3) {
        GunSelection("MP5", GunConfigs["MP5"].sense, GunConfigs["MP5"].zoom)
        pattern := GunConfigs["MP5"].pattern
 }
   else if (wParam = 4) {
        GunSelection("P90", GunConfigs["P90"].sense, GunConfigs["P90"].zoom)
        pattern := GunConfigs["P90"].pattern
 }
   else if (wParam = 5) {
        GunSelection("M4A4", GunConfigs["M4A4"].sense, GunConfigs["M4A4"].zoom)
        pattern := GunConfigs["M4A4"].pattern
 }
   else if (wParam = 6) {
        GunSelection("FAMAS", GunConfigs["FAMAS"].sense, GunConfigs["FAMAS"].zoom)
        pattern := GunConfigs["FAMAS"].pattern
 }
   else if (wParam = 7) {
        GunSelection("GALIL", GunConfigs["GALIL"].sense, GunConfigs["GALIL"].zoom)
        pattern := GunConfigs["GALIL"].pattern
 }
   else if (wParam = 8) {
        GunSelection("UMP", GunConfigs["UMP"].sense, GunConfigs["UMP"].zoom)
 }
   else if (wParam = 9) {
        GunSelection("AUG", GunConfigs["AUG"].sense, GunConfigs["AUG"].zoom)
        pattern := GunConfigs["AUG"].pattern
 }
   else if (wParam = 10) {
        GunSelection("SG", GunConfigs["SG"].sense, GunConfigs["SG"].zoom)
        pattern := GunConfigs["SG"].pattern

 }
   else if (wParam = 12) {
        GunSelection("Mac10", GunConfigs["Mac10"].sense, GunConfigs["Mac10"].zoom)
        pattern := GunConfigs["Mac10"].pattern
}
   else if (wParam = 14) {
        GunSelection("UMP", GunConfigs["UMP"].sense, GunConfigs["UMP"].zoom)
        pattern := GunConfigs["UMP"].pattern
       
 }
   else if (wParam = 0) {
        GunSelection("Recoil OFF", GunConfigs["Recoil OFF"].sense, GunConfigs["Recoil OFF"].zoom)
        pattern := GunConfigs["Recoil OFF"].pattern
}
   else if (wParam = 15) {
        GunSelection("CZ75", GunConfigs["CZ75"].sense, GunConfigs["CZ75"].zoom)
        pattern := GunConfigs["CZ75"].pattern
    
       
        
    }
   
}

; ---------------- HOTKEYS & LABELS ----------------
~$*+F1::Goto ToggleGUI
~$*+F2::Goto MagnifierToggler
~$*+F3::Goto CrosshairToggler
~$*+F4::Goto CounterStrafe
~$*+F5::Goto Toggle_Accept
~$r::Goto ReloadGun

; LButton with RCS
~$*LButton::
if GetKeyState(key_shoot, "P") && !GUIVISIBLE {
	If !RecoilSafety {
		goto RCS
	} Else {
		If GetKeyState(Key_Safety, "P") {
			goto RCS
		}
	}
}
Return

; Right-click for SniperQQ
~$*RButton::
if SniperQQ {
  IfWinActive, ahk_exe CS2.exe
    SetTimer, SniperQQ, 25
}
Return

Pause:: Goto, Pause

#r::Goto, ReloadScript

End::Goto, ExitScript

; ---------------- MAIN LOOP ----------------
MainLoop()
{
	loop {
	;StartTime := A_TickCount
    Sleep, 20
		; Check for CS2 guns
		IfWinActive, ahk_exe CS2.exe 
		{
			for k,gunName in GunKeyMap {
				if GetKeyState(k,"P") {
				  if (GunPattern != gunName) {
					test := GunSelection(gunName, GunConfigs[gunName].sense, GunConfigs[gunName].zoom)
					pattern := GunConfigs[gunName].pattern
					;tooltip  % gunName " , " GunConfigs[gunName].sense " , " GunConfigs[gunName].zoom
				  }
				  Sleep, 200
				}
			}
		}
    
    ; TriggerBot
    While (TriggerBotT && GetKeyState(Key_PixelBot, "P")) {
      MouseGetPos, mx, my
      PixelGetColor, colorPB, mx+1, my+1, Fast
      PixelSearch,,, mx+1, my+1, mx+1, my+1, colorPB, 1, Fast
      if (colorPB != "0xFFFFFFFF" && ErrorLevel=1) {
        Sleep, PilgrimMites(reaction_min, reaction_max)
        Click()
        Sleep, 300
      }
    }
	
    ; BHOP
	While (BHOPT && GetKeyState(Key_BHOP, "D")) {
		
		; Your existing BHOP code (jump logic, etc.)
		if ScrollWheel {
			Sleep, 2
			MouseClick, WheelDown
			Sleep, 2
			MouseClick, WheelUp
			Sleep, 2
		} else if Perfect {
			Sleep, 10
			Send {Space Down}
			Sleep, 10
			Send {Space Up}
			Sleep, 10
		} else if Legit {
			Sleep, 15
			Send {Space Down}
			Sleep, Random(30, 70)
			Send {Space Up}
			Sleep, 15
		}
		
		if !GetKeyState(Key_BHOP, "P")
			Break
	}
    
	; RapidFire
    While (RapidFireT && GetKeyState(Key_RapidFire, "P") && !GuiVisible ) {
		Gosub RapidFire
	}
	
    ; 180 Turn
    While (TurnAroundT && GetKeyState(key_180,"P")) {
      Random, chance, 0.0, 1.0
      PosNeg := chance<=0.49 ? -1 : 1
      DllCall("mouse_event","UInt",0x01,"UInt",(PosNeg*227),"UInt",0)
      Sleep, 1
      Loop, 10 {
        DllCall("mouse_event","UInt",0x01,"UInt",(PosNeg*432),"UInt",0)
        Sleep,1
      }
	  
      Sleep, Random(300,500)
    }
    
    ; Universal RCS or Recoil OFF hotkeys
    If GetKeyState(key_UniversalRCS,"P") && (GunPattern != "UniversalRCS") {
      GunSelection("UniversalRCS",0,0)
	  }
    If GetKeyState(Key_RCoff,"P") && (GunPattern != "Recoil OFF") {
      GunSelection("Recoil OFF",0,0)
	  }
    ;Elapsed := A_TickCount - StartTime
	;Tooltip, Elapsed Time: %Elapsed% ms
	}
}