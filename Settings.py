import subprocess
import os
from flask import Flask, request
import threading
import tkinter as tk
from tkinter import ttk
import win32gui
import time
import socket  # Для проверки порта



# Глобальные данные
latest_weapons = {}
active_weapon_text = "Ожидание данных..."
last_launched_weapon = None  # Чтобы не запускать повторно один и тот же файл
send_status = "Ожидание отправки..."  # Статус отправки AHK команд

# Список оружий и их уникальные параметры для AHK
weapon_params = {
    "weapon_m4a1_silencer": {"wparam": 1, "lparam": 100},   # Параметры для M4A1
    "weapon_p90": {"wparam": 4, "lparam": 200},              # Параметры для P90
    "weapon_mp5sd": {"wparam": 3, "lparam": 300},            # Параметры для MP5
    "weapon_ak47": {"wparam": 2, "lparam": 400},             # Параметры для AK47
    "weapon_m4a1": {"wparam": 5, "lparam": 500},             # Параметры для M4A1
    "weapon_famas": {"wparam": 6, "lparam": 600},            # Параметры для FAMAS
    "weapon_galilar": {"wparam": 7, "lparam": 700},          # Параметры для Galil
    "weapon_aug": {"wparam": 9, "lparam": 800},              # Параметры для AUG
    "weapon_sg556": {"wparam": 10, "lparam": 900},           # Параметры для SG556
    "weapon_mac10": {"wparam": 12, "lparam": 1100},          # Параметры для MAC10
    "weapon_ump45": {"wparam": 14, "lparam": 1200},          # Параметры для MAC10
    "weapon_mp9": {"wparam": 14, "lparam": 1300},            # Параметры для MAC10
    "weapon_cz75a": {"wparam": 15, "lparam": 1400},          # Параметры для MAC10
}

# AHK параметры
WINDOW_TITLE = "MyAHKScriptWindow"
MESSAGE_ID = 0x8888

def send_message(wparam, lparam):
    """Функция для отправки сообщения в AHK-скрипт с параметрами для каждого оружия"""
    global send_status  # Используем глобальную переменную статуса
    try:
        print(f"[{time.strftime('%H:%M:%S')}] Ищем окно с заголовком: '{WINDOW_TITLE}'...")
        hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
        if hwnd:
            print(f"[{time.strftime('%H:%M:%S')}] Окно найдено! HWND: {hwnd}")
            print(f"[{time.strftime('%H:%M:%S')}] Отправка сообщения: msg=0x{MESSAGE_ID:X}, wParam={wparam}, lParam={lparam}")
            result = win32gui.PostMessage(hwnd, MESSAGE_ID, wparam, lparam)
            if result != 0:  # Проверяем успешность отправки
                send_status = "Сообщение отправлено успешно!"  # Обновляем статус
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Сообщение отправлено. Результат: {result}")
            else:
                send_status = "Ошибка при отправке сообщения."  # Обновляем статус
                print(f"[{time.strftime('%H:%M:%S')}] ❌ Сообщение НЕ было отправлено в AHK. Результат: {result}")
        else:
            send_status = "Окно AHK не найдено!"  # Обновляем статус
            print(f"[{time.strftime('%H:%M:%S')}] ❌ Окно AHK не найдено! Сообщение не отправлено.")
    except Exception as e:
        send_status = f"Ошибка: {str(e)}"  # Логируем ошибку
        print(f"[ОШИБКА] {e}")

# Flask-сервер
app = Flask(__name__)

@app.route("/", methods=["POST"])
def gsi():
    global latest_weapons, active_weapon_text, last_launched_weapon
    try:
        data = request.json
        if not data:
            print(f"[ERROR] Пустой запрос получен")
            return "Неверный запрос", 400  # Возвращаем ошибку 400 (Bad Request)

        weapons = data.get("player", {}).get("weapons", {})
        latest_weapons = weapons

        if not weapons:
            print(f"[ERROR] Оружие не найдено в данных запроса")
            return "Оружие не найдено", 400  # Ошибка, если оружие не найдено

        # Найти активное оружие
        found_weapon = None
        for weapon in weapons.values():
            if weapon.get("state") == "active":
                weapon_name = weapon.get("name")
                if weapon_name in weapon_params:
                    found_weapon = weapon_name
                    break

        # Проверка патронов в магазине (ammo_clip)
        if found_weapon:
            ammo_clip = weapon.get('ammo_clip', 0)  # Получаем количество патронов в магазине
            if ammo_clip == 0:  # Если патронов от 1 до 14, вызываем команду
                send_message(0, 1300)
                print(f"[INFO] Патроны в магазине: {ammo_clip}. Отправляем команду с параметрами wparam=0, lparam=1300.")

        if found_weapon:
            # Если оружие изменилось и оно активно
            if last_launched_weapon != found_weapon:
                try:
                    # Получаем параметры для конкретного оружия
                    wparam = weapon_params[found_weapon]["wparam"]
                    lparam = weapon_params[found_weapon]["lparam"]
                    print(f"[INFO] Отправка команды в AHK для оружия: {found_weapon}")
                    send_message(wparam, lparam)  # Отправляем команду в AHK с параметрами
                    last_launched_weapon = found_weapon
                    print(f"[INFO] Оружие {found_weapon} активировано.")
                except Exception as e:
                    print(f"[ОШИБКА] Не удалось отправить команду в AHK для {found_weapon}: {e}")
        else:
            # Если оружие не найдено в списке, отправляем команду с параметрами wparam = 0 и lparam = 1300
            if last_launched_weapon != "unknown_weapon":
                print(f"[INFO] Оружие не найдено. Отправляем команду с параметрами wparam=0, lparam=1300")
                send_message(0, 1300)
                last_launched_weapon = "unknown_weapon"

        # Обновление текста активного оружия
        if found_weapon:
            name = found_weapon
            wtype = "Неизвестный тип"  # Возможно, можно добавить логику для типов
            ammo = f"{weapon.get('ammo_clip', '')}/{weapon.get('ammo_clip_max', '')}" if "ammo_clip" in weapon else ""
            reserve = f" | запас: {weapon.get('ammo_reserve', '')}" if "ammo_reserve" in weapon else ""
            active_weapon_text = f"Активное оружие: {name} [{wtype}] {ammo}{reserve}"
        else:
            active_weapon_text = "Активное оружие: —"
            
    except Exception as e:
        latest_weapons = {"error": str(e)}
        active_weapon_text = f"[Ошибка]: {e}"
        print(f"[ERROR] Ошибка на сервере: {e}")
        return "Ошибка на сервере", 500  # Возвращаем ошибку 500 (Internal Server Error)

    return "", 200

# Функция для проверки доступности порта
def is_server_available(host="127.0.0.1", port=59873):
    """Проверка, доступен ли сервер на указанном порту"""
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"[INFO] Порт {port} доступен.")
            return True
    except (socket.timeout, socket.error):
        print(f"[INFO] Порт {port} не доступен.")
        return False

# Функция для попытки подключения
def attempt_connection():
    """Попытка подключения к серверу. Если сервер недоступен, будет повторять попытки."""
    while not is_server_available():
        print(f"[INFO] Сервер на порту 59873 не доступен. Пытаемся снова...")
        time.sleep(5)  # Задержка перед повторной попыткой

    print("[INFO] Сервер доступен. Подключение установлено!")

# Запуск Flask-сервера в отдельном потоке
def start_flask():
    print("[GSI] Сервер запущен на http://127.0.0.1:59873")  # Порт изменен на 59873
    app.run(port=59873, threaded=True)  # Запуск Flask с параметром threaded=True

# Функция для перезагрузки кода
def restart_code():
    """Перезапуск всего кода с помощью subprocess"""
    print("[INFO] Перезапуск кода...")
    subprocess.Popen(["python", os.path.realpath(__file__)])  # Запуск текущего скрипта
    exit()  # Закрываем текущий процесс



# GUI
def start_gui():
    def update_display():
        active_label_var.set(active_weapon_text)
        listbox.delete(0, tk.END)
        if "error" in latest_weapons:
            listbox.insert(tk.END, f"[Ошибка]: {latest_weapons['error']}")
        else:
            for slot_key, weapon in sorted(latest_weapons.items()):
                name = weapon.get("name", "unknown")
                wtype = weapon.get("type", "")
                state = weapon.get("state", "")
                ammo = f"{weapon.get('ammo_clip', '')}/{weapon.get('ammo_clip_max', '')}" if "ammo_clip" in weapon else ""
                reserve = f" | запас: {weapon.get('ammo_reserve', '')}" if "ammo_reserve" in weapon else ""
                line = f"{'🟢' if state == 'active' else '  '} [{slot_key}] {name} [{wtype}] {ammo}{reserve}"
                listbox.insert(tk.END, line)

        # Отображение статуса отправки
        status_label_var.set(f"Статус отправки: {send_status}")
        
        root.after(1000, update_display)  # Обновляем интерфейс раз в секунду

    root = tk.Tk()
    root.title("CS2 GSI - Инвентарь оружия")
    root.geometry("540x460")
    root.configure(bg="#1e1e1e")

    ttk.Style().configure("TLabel", background="#1e1e1e", foreground="#00ff99", font=("Consolas", 12))

    active_label_var = tk.StringVar()
    active_label = ttk.Label(root, textvariable=active_label_var, style="TLabel", anchor="center")
    active_label.pack(pady=(10, 5))

    ttk.Label(root, text="Инвентарь игрока:", style="TLabel").pack(pady=(0, 5))

    listbox = tk.Listbox(root, bg="#2b2b2b", fg="#e6e6e6", font=("Consolas", 10), selectbackground="#444")
    listbox.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

    # Кнопка перезагрузки кода
    restart_button = ttk.Button(root, text="Перезагрузить код", command=restart_code)
    restart_button.pack(pady=10)

    # Статус отправки AHK
    status_label_var = tk.StringVar()
    status_label = ttk.Label(root, textvariable=status_label_var, style="TLabel", anchor="center")
    status_label.pack(pady=(10, 5))

    update_display()
    root.mainloop()

# Создаем потоки для Flask и GUI
flask_thread = threading.Thread(target=start_flask, daemon=True)
flask_thread.start()

# Запуск GUI
start_gui()
