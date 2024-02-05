import requests
import json
from timeconvert import time_convertor
from login import get_sess_key



def api_request(time_from, time_to):
    sess_key,MoodleSession,MOODLEID1_ = get_sess_key()
    url = f"https://lms.klh.edu.in/lib/ajax/service.php?sesskey={sess_key}&info=core_calendar_get_action_events_by_timesort"
    main_data=[]
    payload = json.dumps([
      {
        "index": 0,
        "methodname": "core_calendar_get_action_events_by_timesort",
        "args": {
          "limitnum": 6,
          "timesortfrom": time_from,
          "timesortto": time_to,
          "limittononsuspendedevents": True
        }
      }
    ])
    headers = {
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
      'Connection': 'keep-alive',
      'Content-Type': 'application/json',
      'Cookie': f'MoodleSession={MoodleSession};MOODLEID1_={MOODLEID1_}',
      'Origin': 'https://lms.klh.edu.in',
      'Referer': 'https://lms.klh.edu.in/my/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    for hw in response:
        for event in hw['data']['events']:

            date = time_convertor(event['timestart'])
            temp={
                "id":event['id'],
                "name":event['activityname'],
                "subject":event['course']['shortname'],
                "description":event['description'],
                "date":date,
                "url":event['action']['url']
            }

            main_data.append(temp)
    return main_data
