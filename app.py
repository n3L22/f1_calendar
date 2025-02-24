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
        "date": "2025-03-14",
        "end_date": "2025-03-16",
        "display_date": "14 March - 16 March",
        "schedule": {
            "race": {
                "date": "16 March",
                "calc_date": "2025-03-16",
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
            }
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
    },
    {
        "round": 3,
        "name": "Japanese Grand Prix",
        "circuit": "Suzuka International Racing Course",
        "location": "Suzuka",
        "date": "2025-04-04",
        "end_date": "2025-04-06",
        "display_date": "4 April - 6 April",
        "schedule": {
            "race": {
                "date": "6 April",
                "calc_date": "2025-04-06",
                "time": "06:00"
            },
            "qualifying": {
                "date": "5 April",
                "calc_date": "2025-04-05",
                "time": "07:00 - 08:00"
            },
            "practice1": {
                "date": "4 April",
                "calc_date": "2025-04-04",
                "time": "03:30 - 04:30"
            },
            "practice2": {
                "date": "4 April",
                "calc_date": "2025-04-04",
                "time": "07:00 - 08:00"
            },
            "practice3": {
                "date": "5 April",
                "calc_date": "2025-04-05",
                "time": "03:30 - 04:30"
            }
        },
        "sprint": False,
        "image": "static/images/japan.jpg"
    },
    {
        "round": 4,
        "name": "Bahrain Grand Prix",
        "circuit": "Bahrain International Circuit",
        "location": "Sakhir",
        "date": "2025-04-11",
        "end_date": "2025-04-13",
        "display_date": "11 April - 13 April",
        "schedule": {
            "race": {
                "date": "13 April",
                "calc_date": "2025-04-13",
                "time": "16:00"
            },
            "qualifying": {
                "date": "12 April",
                "calc_date": "2025-04-12",
                "time": "16:00 - 17:00"
            },
            "practice1": {
                "date": "11 April",
                "calc_date": "2025-04-11",
                "time": "13:30 - 14:30"
            },
            "practice2": {
                "date": "11 April",
                "calc_date": "2025-04-11",
                "time": "17:00 - 18:00"
            },
            "practice3": {
                "date": "12 April",
                "calc_date": "2025-04-12",
                "time": "13:30 - 14:30"
            }
        },
        "sprint": False,
        "image": "static/images/bahrain.jpg"
    },
    {
        "round": 5,
        "name": "Saudi Arabian Grand Prix",
        "circuit": "Jeddah Corniche Circuit",
        "location": "Jeddah",
        "date": "2025-04-18",
        "end_date": "2025-04-20",
        "display_date": "18 April - 20 April",
        "schedule": {
            "race": {
                "date": "20 April",
                "calc_date": "2025-04-20",
                "time": "17:00"
            },
            "qualifying": {
                "date": "19 April",
                "calc_date": "2025-04-19",
                "time": "17:00 - 18:00"
            },
            "practice1": {
                "date": "18 April",
                "calc_date": "2025-04-18",
                "time": "13:30 - 14:30"
            },
            "practice2": {
                "date": "18 April",
                "calc_date": "2025-04-18",
                "time": "17:00 - 18:00"
            },
            "practice3": {
                "date": "19 April",
                "calc_date": "2025-04-19",
                "time": "13:30 - 14:30"
            }
        },
        "sprint": False,
        "image": "static/images/jeddah.jpg"
    },
    {
        "round": 6,
        "name": "Miami Grand Prix",
        "circuit": "Miami International Autodrome",
        "location": "Miami",
        "date": "2025-05-02",
        "end_date": "2025-05-04",
        "display_date": "2 May - 4 May",
        "schedule": {
            "race": {
                "date": "4 May",
                "calc_date": "2025-05-04",
                "time": "19:30"
            },
            "qualifying": {
                "date": "3 May",
                "calc_date": "2025-05-03",
                "time": "21:00 - 22:00"
            },
            "sprint": {
                "date": "3 May",
                "calc_date": "2025-05-03",
                "time": "17:00 - 18:00"
            },
            "sprint_qualifying": {
                "date": "2 May",
                "calc_date": "2025-05-02",
                "time": "21:30 - 22:14"
            },
            "practice1": {
                "date": "2 May",
                "calc_date": "2025-05-02",
                "time": "17:30 - 18:30"
            }
        },
        "sprint": True,
        "image": "static/images/miami.jpg"
    },
    {
        "round": 7,
        "name": "Emilia Romagna Grand Prix",
        "circuit": "Autodromo Enzo e Dino Ferrari",
        "location": "Imola",
        "date": "2025-05-16",
        "end_date": "2025-05-18",
        "display_date": "16 May - 18 May",
        "schedule": {
            "race": {
                "date": "18 May",
                "calc_date": "2025-05-18",
                "time": "14:00"
            },
            "qualifying": {
                "date": "17 May",
                "calc_date": "2025-05-17",
                "time": "14:00 - 15:00"
            },
            "practice1": {
                "date": "16 May",
                "calc_date": "2025-05-16",
                "time": "12:30 - 13:30"
            },
            "practice2": {
                "date": "16 May",
                "calc_date": "2025-05-16",
                "time": "16:00 - 17:00"
            },
            "practice3": {
                "date": "17 May",
                "calc_date": "2025-05-17",
                "time": "11:30 - 12:30"
            }
        },
        "sprint": False,
        "image": "static/images/imola.jpg"
    },
    {
        "round": 8,
        "name": "Monaco Grand Prix",
        "circuit": "Circuit de Monaco",
        "location": "Monaco",
        "date": "2025-05-23",
        "end_date": "2025-05-25",
        "display_date": "23 May - 25 May",
        "schedule": {
            "race": {
                "date": "25 May",
                "calc_date": "2025-05-25",
                "time": "14:00"
            },
            "qualifying": {
                "date": "24 May",
                "calc_date": "2025-05-24",
                "time": "14:00 - 15:00"
            },
            "practice1": {
                "date": "23 May",
                "calc_date": "2025-05-23",
                "time": "12:30 - 13:30"
            },
            "practice2": {
                "date": "23 May",
                "calc_date": "2025-05-23",
                "time": "16:00 - 17:00"
            },
            "practice3": {
                "date": "24 May",
                "calc_date": "2025-05-24",
                "time": "11:30 - 12:30"
            }
        },
        "sprint": False,
        "image": "static/images/monaco.jpg"
    }
]

@app.route('/')
def home():
    now = datetime.now(timezone.utc)
    upcoming_races = []
    past_races = []
    next_event = None
    
    # Create testing schedule
    testing_schedule = {
        "name": "F1 Aramco Pre-Season Testing 2025",
        "location": "Bahrain International Circuit, Sakhir",
        "date": "2025-02-26",
        "end_date": "2025-02-28",
        "display_date": "26 February - 28 February",
        "schedule": {
            "day1": {
                "date": "26 February",
                "calc_date": "2025-02-26",
                "time": "07:00 - 16:00"
            },
            "day2": {
                "date": "27 February",
                "calc_date": "2025-02-27",
                "time": "07:00 - 16:00"
            },
            "day3": {
                "date": "28 February",
                "calc_date": "2025-02-28",
                "time": "07:00 - 16:00"
            }
        },
        "image": "static/images/testing.jpg"
    }
    
    # Check if testing is upcoming
    testing_datetime = None
    for day in ["day1", "day2", "day3"]:
        test_date = testing_schedule["schedule"][day]["calc_date"]
        test_time = testing_schedule["schedule"][day]["time"].split(" - ")[0]
        test_datetime = datetime.strptime(f"{test_date} {test_time}", '%Y-%m-%d %H:%M')
        test_datetime = pytz.UTC.localize(test_datetime)
        
        if test_datetime > now:
            testing_datetime = test_datetime
            testing_schedule["datetime"] = test_datetime
            testing_schedule["next_day"] = day
            break
    
    # Check races
    for race in f1_races:
        race_datetime = datetime.strptime(f"{race['schedule']['race']['calc_date']} {race['schedule']['race']['time'].split(' - ')[0]}", '%Y-%m-%d %H:%M')
        race_datetime = pytz.UTC.localize(race_datetime)
        
        if race_datetime > now:
            if next_event is None or (testing_datetime and testing_datetime < race_datetime):
                next_event = race.copy()
                next_event['datetime'] = race_datetime
                next_event['type'] = 'race'
            upcoming_races.append(race)
        else:
            past_races.append(race)
    
    # Compare testing with races to find next event
    if testing_datetime and (next_event is None or testing_datetime < next_event['datetime']):
        next_event = testing_schedule
        next_event['type'] = 'testing'
    
    # Check if testing is in the past
    is_testing_past = testing_datetime is None or testing_datetime < now
    
    return render_template('index.html', 
                         upcoming_races=upcoming_races,
                         past_races=past_races,
                         next_event=next_event,
                         testing_schedule=testing_schedule,
                         is_testing_past=is_testing_past)
if __name__ == '__main__':
    app.run(debug=True)