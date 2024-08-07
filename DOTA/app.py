from flask import Flask, render_template, request, jsonify, url_for
import webbrowser
import threading

app = Flask(__name__, template_folder='templates', static_folder='static')

# Словарь с информацией о героях
heroes_data = {
    "Bristleback":  {
        "pros": ["Танк", "В файтах впереди"],
        "cons": ["Нет инициации", "Герой для лоу ПТС"],
        "counters": [
            {"name": "Viper", "image_url": "static/images/Viper_icon.webp"},
            {"name": "Timbersaw", "image_url": "static/images/Timbersaw_icon.webp"},
            {"name": "Necrophos", "image_url": "static/images/Necrophos_icon.webp"},
            {"name": "Monkey King", "image_url": "static/images/Monkey_King_icon.webp"},
            {"name": "Ancient Apparition", "image_url": "static/images/Ancient_Apparition_icon.webp"}
        ],
        "counter_items": [
            {"name": "Silver Edge", "image_url": "static/images/Silver_Edge_icon.webp"},
            {"name": "Spirit Vessel", "image_url": "static/images/Spirit_Vessel_icon.webp"},
            {"name": "Eye of Skadi", "image_url": "static/images/Eye_of_Skadi_icon.webp"},
            {"name": "Diffusal Blade", "image_url": "static/images/Diffusal_Blade_1_icon.webp"}
        ],
        "image_url": "images/Bristleback_icon.webp"
    },

    "Abaddon":  {
        "pros": ["Хороший лайнер", "Долго живет", "Танк"],
        "cons": ["Нет дизейбла", "Тяжело набить пассивку"],
        "counters": [
            {"name": "Viper", "image_url": "static/images/Viper_icon.webp"},
            {"name": "Phantom Assasin", "image_url": "static/images/Phantom_Assassin_icon.webp"},
            {"name": "Doom", "image_url": "static/images/Doom_icon.webp"},
            {"name": "Shadow Demon", "image_url": "static/images/Shadow_Demon_icon.webp"},
            {"name": "Hoodwink", "image_url": "static/images/Hoodwink_icon.webp"},
            {"name": "Lina", "image_url": "static/images/Lina_icon.webp"},
            {"name": "Lion", "image_url": "static/images/Lion_icon.webp"}
        ],
        "counter_items": [
            {"name": "Silver Edge", "image_url": "static/images/Silver_Edge_icon.webp"},
            {"name": "Radiance", "image_url": "static/images/Radiance_29_icon.webp"},
            {"name": "Heaven Halberd", "image_url": "static/images/HeavenHalberd_icon.webp"},
            {"name": "Euls Scepter of Divinity", "image_url": "static/images/Eul_Scepter_of_Divinity_icon.webp"}
        ],
        "image_url": "images/Abaddon_icon.webp"
    },

    "Alchemist": {
        "pros": ["Быстро фармит", "Дарит аганимы", "Есть дизейбл"],
        "cons": ["Нет искейпа", "Уязвим без ульты", "Не выигрывает без тимы"],
        "counters": [
            {"name": "Slark", "image_url": "static/images/Viper_icon.webp"},
            {"name": "Necrophos", "image_url": "static/images/Necrophos_icon.webp"},
            {"name": "Ancient Apparition", "image_url": "static/images/Doom_icon.webp"},
            {"name": "Lifestealer", "image_url": "static/images/Lifestealer_icon.webp"}
        ],
        "counter_items": [
            {"name": "Spirit Vessel", "image_url": "static/images/Spirit_Vessel_icon.webp"},
            {"name": "Butterfly", "image_url": "static/images/Butterfly_icon.webp"},
            {"name": "Heaven Halberd", "image_url": "static/images/HeavenHalberd_icon.webp"},
            {"name": "Ethereal", "image_url": "static/images/Ethereal_Blade_icon.webp"}
        ],
        "image_url": "images/Alchemist_icon.webp"
    },

    "Ancient Apparition": {
        "pros": ["Контрпик ХП регена"],
        "cons": ["Средний лайн", "Тонкий", "Трудный дизейбл"],
        "counters": [
            {"name": "Spectre", "image_url": "static/images/Spectre_icon.webp"},
            {"name": "Riki", "image_url": "static/images/Riki_icon.webp"},
            {"name": "Phantom Assasin", "image_url": "static/images/Phantom_Assassin_icon.webp"},
            {"name": "Clinkz", "image_url": "static/images/Clinkz_icon.webp"},
            {"name": "Bounty Hunter", "image_url": "static/images/Bounty_Hunter_icon.webp"},
            {"name": "Legion Commander", "image_url": "static/images/Legion_Commander_icon.webp"}
        ],
        "counter_items": [
            {"name": "Pipe of Insight", "image_url": "static/images/Pipe_of_Insight_icon.webp"},
            {"name": "Eternal_Shroud", "image_url": "static/images/Eternal_Shroud_icon.webp"},
            {"name": "Force Staff", "image_url": "static/images/Force_Staff_icon.webp"},
            {"name": "Glimmer Cape", "image_url": "static/images/Glimmer_Cape_icon.webp"}
        ],
        "image_url": "images/Ancient_Apparition_icon.webp"
    },

    "Anti-Mage": {
        "pros": ["Фарм из-за блинка", "Хорошо сплитит", "Сильный в лейте"],
        "cons": ["Слабый лайн", "Долгий разгон", "Поздно подключается"],
        "counters": [
            {"name": "Doom", "image_url": "static/images/Doom_icon.webp"},
            {"name": "Meepo", "image_url": "static/images/Meepo_icon.webp"},
            {"name": "Phantom Assasin", "image_url": "static/images/Phantom_Assassin_icon.webp"},
            {"name": "Lion", "image_url": "static/images/Lion_icon.webp"},
            {"name": "Shadow Shaman", "image_url": "static/images/Shadow_Shaman_icon.webp"},
            {"name": "Bane", "image_url": "static/images/Bane_icon.webp"},
            {"name": "Legion Commander", "image_url": "static/images/Legion_Commander_icon.webp"}
        ],
        "counter_items": [
            {"name": "Scythe Of Vyse", "image_url": "static/images/Scythe_of_Vyse_icon.webp"},
            {"name": "Heaven Halberd", "image_url": "static/images/HeavenHalberd_icon.webp"},
            {"name": "Force Staff", "image_url": "static/images/Force_Staff_icon.webp"},
            {"name": "Ethereal", "image_url": "static/images/Ethereal_Blade_icon.webp"}
        ],
        "image_url": "images/Anti-Mage_icon.webp"
    },

    "Axe": {
        "pros": ["Идеален против ближников", "Не жадный", "Инициация и танк"],
        "cons": ["Слабый без команды", "Боится контроля", "Плох против ренжевиков"],
        "counters": [
            {"name": "Viper", "image_url": "static/images/Viper_icon.webp"},
            {"name": "Timbersaw", "image_url": "static/images/Timbersaw_icon.webp"},
            {"name": "Phantom Assasin", "image_url": "static/images/Phantom_Assassin_icon.webp"},
            {"name": "Outworld Destroyer", "image_url": "static/images/Outworld_Destroyer_icon.webp"}
        ],
        "counter_items": [
            {"name": "Euls Scepter of Divinity", "image_url": "static/images/Eul_Scepter_of_Divinity_icon.webp"},
            {"name": "Silver Edge", "image_url": "static/images/Silver_Edge_icon.webp"},
            {"name": "AEONDisk ", "image_url": "static/images/Aeon_Disk_icon.webp"}
        ],
        "image_url": "images/Axe_icon.webp"
    },

    "Bane": {
        "pros": ["Много контроля", "Сильные спеллы", "Универсал"],
        "cons": ["Важна позиционка", "Зависит от командного скилла"],
        "counters": [
            {"name": "Slark", "image_url": "static/images/Slark_icon.webp"},
            {"name": "Riki", "image_url": "static/images/Riki_icon.webp"},
            {"name": "Spectre", "image_url": "static/images/Spectre_icon.webp"}
        ],
        "counter_items": [
            {"name": "Linken Sphere", "image_url": "static/images/Linken_Sphere_icon.webp"},
            {"name": "Lotus Orb", "image_url": "static/images/Lotus_Orb_icon.webp"},
            {"name": "AEONDisk ", "image_url": "static/images/Aeon_Disk_icon.webp"}
        ],
        "image_url": "images/Bane_icon.webp"
    },
    # Добавьте сюда информацию о других героях
}

# Функция для получения информации о герое
def get_hero_info(hero_name):
    hero_info = heroes_data.get(hero_name)
    if hero_info:
        return {
            "hero_name": hero_name,
            "pros": hero_info["pros"],
            "cons": hero_info["cons"],
            "counters": hero_info["counters"],
            "counter_items": hero_info["counter_items"],
            "image_url": url_for('static', filename=hero_info["image_url"])
        }
    else:
        return {"error": "Hero not found"}

# Основная страница, которая будет отображаться в браузере
@app.route("/")
def index():
    hero_names = list(heroes_data.keys())
    return render_template("index.html", hero_names=hero_names)

# API endpoint для получения информации о герое
@app.route("/get_hero_info", methods=["POST"])
def get_hero_info_api():
    data = request.get_json()
    hero_name = data.get("hero_name")
    print(f"Received request for hero: {hero_name}")  # Debug output
    return jsonify(get_hero_info(hero_name))

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
