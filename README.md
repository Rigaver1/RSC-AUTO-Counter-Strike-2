# 🔫 Auto Weapon Switch for AHK MultiScript | Pean's RCS  
### 💡 Enhanced by PilgrimMites

---

## 📝 Introduction

Hello to all fans of AHK MultiScript and Pean's RCS!
https://github.com/PilgrimMitesV2/AHK-MultiScript/tree/main

I've always admired this project, and I decided to implement one important feature — **automatic weapon switching**.

> ❗ **Problem**: If you try to do this purely with AHK, you'd need to read the game’s memory, which brings a **100% risk of a VAC ban**.  
> ✅ **Solution**: Use Valve's official feature — **Game State Integration (GSI)**.

With [CounterStrike2GSI](https://github.com/antonpup/CounterStrike2GSI), we can receive weapon data directly from the game — **without touching memory**!

---

## ⚙️ What the Script Does

- Connects to CS2's GSI port using Python.
- Reads the current weapon info in real-time.
- Sends a command to the AHK script to activate the correct RCS pattern.

---

## 🌟 Features

- If you're holding an AK-47 — the proper RCS pattern is enabled.
- If it's a knife, pistol, or grenade — RCS is disabled.
- When ammo runs out — RCS is also disabled.

---

## 📦 Installation

### 1. Download and extract the archive to a convenient folder.

---

### 2. Install Python

- Go to the [official Python website](https://www.python.org/downloads)
- During installation, check these two boxes:

☑ Add Python to PATH
☑ Install pip

yaml
Копировать
Редактировать

---

### 3. Install required libraries

Open `CMD` (`Win + R → cmd`) and run:

```bash
pip install flask pywin32
4. Configure Game State Integration
Copy GameStateIntegration_MyCS2.cfg from the archive.

In Steam, right-click CS2 → Properties → Installed Files → Browse.

Navigate to:

Копировать
Редактировать
...\game\csgo\cfg
Paste the .cfg file into that directory.

5. Run the Project
Launch RCS AUTO.bat

Then launch A_Main_Run_this.ahk

❗ Important Notes
🚫 Do not enable the “Auto Weapon Detection” checkbox in the GUI
It will break automatic switching.

🔄 If auto-switching doesn't work after weapon change:
Close the AHK script.

Relaunch A_Main_Run_this.ahk.

If it still doesn't work, restart both the game and the scripts.

💬 Feedback
If you enjoy this enhancement, consider starring the project ⭐ and leaving a comment.
Your feedback helps improve the tool and motivates future development! 🙌


Russian 

# 🔫 Автоматическое переключение оружия для AHK MultiScript | Pean's RCS  
### 💡 Доработка от PilgrimMites

---

## 📝 Введение

Привет всем фанатам AHK MultiScript и Pean's RCS!
https://github.com/PilgrimMitesV2/AHK-MultiScript/tree/main
Меня давно вдохновляет этот проект, и я решил реализовать одну важную функцию — **автоматическое переключение оружия**.

> ❗ Проблема: если реализовать это на чистом AHK, придётся читать память игры. Это **100% риск VAC-бана**.  
> ✅ Решение: использовать официальную систему от Valve — **Game State Integration (GSI)**.

С помощью [CounterStrike2GSI](https://github.com/antonpup/CounterStrike2GSI) можно получать информацию об оружии из самой игры — **без вмешательства в память**!

---

## ⚙️ Что делает скрипт

- Подключается к GSI-порту CS2 через Python.
- Получает текущую информацию об оружии игрока.
- Отправляет команду в AHK-скрипт для включения нужного паттерна.

---

## 🌟 Особенности

- Если в руках AK-47 — включается нужный RCS.
- Если нож, граната или пистолет — RCS выключается.
- Когда магазин пуст — RCS также отключается.

---

## 📦 Установка

### 1. Скачайте архив с проектом и распакуйте в удобную папку.

---

### 2. Установите Python

- Перейдите на [официальный сайт Python](https://www.python.org/downloads)
- При установке поставьте галочки:

```
☑ Add Python to PATH
☑ Install pip
```

---

### 3. Установите библиотеки

Откройте `CMD` (`Win + R → cmd`) и введите:

```bash
pip install flask pywin32
```

---

### 4. Настройте Game State Integration

1. Скопируйте `GameStateIntegration_MyCS2.cfg` из архива.
2. В Steam нажмите **ПКМ по CS2 → Свойства → Установленные файлы → Обзор**.
3. Перейдите в папку:

```
...\game\csgo\cfg
```

4. Вставьте файл `.cfg` в эту директорию.

---

### 5. Запуск

1. Запустите `RCS AUTO.bat`
2. Затем запустите `A_Main_Run_this.ahk`

---

## ❗ Важные замечания

### 🚫 Не включайте функцию “Auto Weapon Detection” в GUI

Это сломает работу автоматического переключения.

---

### 🔄 Если автомат не работает после смены оружия

1. Закройте AHK-скрипт.
2. Перезапустите `A_Main_Run_this.ahk`
3. Если всё ещё не работает — перезапустите игру и все скрипты.

---

## 💬 Обратная связь

Если тебе понравилась доработка — поддержи проект звёздочкой ⭐ и напиши комментарий.  
Ваш фидбэк помогает развивать проект и добавлять новые фичи! 🙌

# 🔫 Автоматическое переключение оружия для AHK MultiScript | Pean's RCS  
### 💡 Доработка от PilgrimMites

---

## 📝 Введение

Привет всем фанатам AHK MultiScript и Pean's RCS!

Меня давно вдохновляет этот проект, и я решил реализовать одну важную функцию — **автоматическое переключение оружия**.

> ❗ Проблема: если реализовать это на чистом AHK, придётся читать память игры. Это **100% риск VAC-бана**.  
> ✅ Решение: использовать официальную систему от Valve — **Game State Integration (GSI)**.

С помощью [CounterStrike2GSI](https://github.com/antonpup/CounterStrike2GSI) можно получать информацию об оружии из самой игры — **без вмешательства в память**!

---

## ⚙️ Что делает скрипт

- Подключается к GSI-порту CS2 через Python.
- Получает текущую информацию об оружии игрока.
- Отправляет команду в AHK-скрипт для включения нужного паттерна.

---

## 🌟 Особенности

- Если в руках AK-47 — включается нужный RCS.
- Если нож, граната или пистолет — RCS выключается.
- Когда магазин пуст — RCS также отключается.

---

## 📦 Установка

### 1. Скачайте архив с проектом и распакуйте в удобную папку.

---

### 2. Установите Python

- Перейдите на [официальный сайт Python](https://www.python.org/downloads)
- При установке поставьте галочки:

```
☑ Add Python to PATH
☑ Install pip
```

---

### 3. Установите библиотеки

Откройте `CMD` (`Win + R → cmd`) и введите:

```bash
pip install flask pywin32
```

---

### 4. Настройте Game State Integration

1. Скопируйте `GameStateIntegration_MyCS2.cfg` из архива.
2. В Steam нажмите **ПКМ по CS2 → Свойства → Установленные файлы → Обзор**.
3. Перейдите в папку:

```
...\game\csgo\cfg
```

4. Вставьте файл `.cfg` в эту директорию.

---

### 5. Запуск

1. Запустите `RCS AUTO.bat`
2. Затем запустите `A_Main_Run_this.ahk`

---

## ❗ Важные замечания

### 🚫 Не включайте функцию “Auto Weapon Detection” в GUI

Это сломает работу автоматического переключения.

---

### 🔄 Если автомат не работает после смены оружия

1. Закройте AHK-скрипт.
2. Перезапустите `A_Main_Run_this.ahk`
3. Если всё ещё не работает — перезапустите игру и все скрипты.

---

## 💬 Обратная связь

Если тебе понравилась доработка — поддержи проект звёздочкой ⭐ и напиши комментарий.  
Ваш фидбэк помогает развивать проект и добавлять новые фичи! 🙌


