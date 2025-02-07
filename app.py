from flask import Flask, render_template
from datetime import datetime, timezone
import pytz

app = Flask(__name__)

f1_races = [
    {
        "round": 1,
        "name": "Australian Grand Prix",
        "circuit": "Melbourne Grand Prix Circuit",
        "location": "Melbourne",
        "date": "2025-03-14",  # For calculations
        "end_date": "2025-03-16",  # For calculations
        "display_date": "14 March - 16 March",  # For display
        "schedule": {
            "race": {
                "date": "16 March",  # For display
                "calc_date": "2025-03-16",  # For calculations
                "time": "04:00"
            },
            "qualifying": {
                "date": "15 March",
                "calc_date": "2025-03-15",
                "time": "05:00 - 06:00"
            },
            "practice1": {
                "date": "14 March",
                "calc_date": "2025-03-14",
                "time": "01:30 - 02:30"
            },
            "practice2": {
                "date": "14 March",
                "calc_date": "2025-03-14",
                "time": "05:00 - 06:00"
            },
            "practice3": {
                "date": "15 March",
                "calc_date": "2025-03-15",
                "time": "01:30 - 02:30"
            },
            
        },
        "sprint": False,
        "image": "static/images/melbourne.jpg"
    }, 
    {
    "round": 2,
    "name": "Chinese Grand Prix",
    "circuit": "Shanghai International Circuit",
    "location": "Shanghai",
    "date": "2025-03-21",
    "end_date": "2025-03-23",
    "display_date": "21 March - 23 March",
    "schedule": {
        "race": {
            "date": "23 March",
            "calc_date": "2025-03-23",
            "time": "07:00"
        },
        "qualifying": {
            "date": "22 March",
            "calc_date": "2025-03-22",
            "time": "07:00 - 08:00"
        },
        "sprint": {
            "date": "22 March",
            "calc_date": "2025-03-22",
            "time": "03:00 - 04:00"
        },
        "sprint_qualifying": {
            "date": "21 March",
            "calc_date": "2025-03-21",
            "time": "07:30 - 08:14"
        },
        "practice1": {
            "date": "21 March",
            "calc_date": "2025-03-21",
            "time": "03:30 - 04:30"
        }
    },
    "sprint": True,
    "image": "static/images/shanghai.jpg"
}
]

@app.route('/')
def home():
    now = datetime.now(timezone.utc)
    upcoming_races = []
    past_races = []
    next_race = None
    
    for race in f1_races:
        # Use calc_date for datetime comparisons
        race_datetime = datetime.strptime(f"{race['schedule']['race']['calc_date']} {race['schedule']['race']['time'].split(' - ')[0]}", '%Y-%m-%d %H:%M')
        race_datetime = pytz.UTC.localize(race_datetime)
        
        if race_datetime > now:
            if next_race is None:
                next_race = race.copy()
                next_race['datetime'] = race_datetime
            upcoming_races.append(race)
        else:
            past_races.append(race)
    
    return render_template('index.html', 
                         upcoming_races=upcoming_races,
                         past_races=past_races,
                         next_race=next_race)
if __name__ == '__main__':
    app.run(debug=True)