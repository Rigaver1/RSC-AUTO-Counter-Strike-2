# 🔫 Auto Weapon Switch for AHK MultiScript | Pean's RCS  
### 💡 https://www.unknowncheats.me/forum/counter-strike-2-releases/605440-ahk-multiscript-peans-rcs.html

---

## 📝 Introduction

Hello to all fans of AHK MultiScript and Pean's RCS!

I've always admired this project, and I decided to implement one important feature — **automatic weapon switching**.

> ❗ **Problem**: If you try to do this purely with AHK, you'd need to read the game’s memory, which brings a **100% risk of a VAC ban**.  
> ✅ **Solution**: Use Valve's official feature — **Game State Integration (GSI)**.

With [CounterStrike2GSI](https://github.com/antonpup/CounterStrike2GSI), we can receive weapon data directly from the game — **without touching memory**!

---

## ⚙️ What the Script Does

- Connects to CS2's GSI port using Python  
- Reads the current weapon info in real-time  
- Sends a command to the AHK script to activate the correct RCS pattern  

---

## 🌟 Features

- Holding an AK-47? The correct RCS pattern turns on automatically  
- Knife, pistol, or grenade? RCS turns off  
- Out of ammo? RCS is disabled until you reload  

---

## 📦 Installation

### 1. Download and extract the archive to any convenient folder.

---

### . Install P

### . Configure Game State Integration

1. Copy `GameStateIntegration_MyCS2.cfg` from the archive  
2. In Steam: **Right-click CS2 → Properties → Installed Files → Browse**  
3. Navigate to this folder:

```
...\game\csgo\cfg
```

. Paste the `.cfg` file into that directory

---





---

### 5. Launch the Scripts

1. Run `RCS AUTO.exe`  

---

## ❗ Important Notes

### 🚫 Do *not* enable the “Auto Weapon Detection” checkbox in the GUI

This will break the auto-switch system.

---

### 🔄 If switching stops working:
After the change, save and press F2 to restart the script 

![image](https://github.com/user-attachments/assets/59d628fa-14bc-4c44-85fa-18d89fad72be)

  


 
3. Still not working? Restart both the scripts **and** the game

---

## 💬 Feedback






