from random import randint


def login(username):
    # send username to db
    var = randint(0,1)
    if var == 1:
        return {"exists": True,"requests" : 
                [{"task_details":"I need someone to pet my dog", "time_remaining": 5, "status": 2, "executing_username":"amit"},
                 {"task_details":"Connect to my db bls", "time_remaining": 5, "status": 1}],
                  "suggestions": [{"task_details": "I want to pet someone's dog"}], "location" : 1}
    else:
        return {"exists":False}


def register(username, phone_number, location, suggestions, photo=None):
    # check if user is in db
    var = randint(0, 1)
    if var == 1:
        # run language model on suggestions
        # insert new user to db
        return {"inserted": True,
                "suggestions": [{"task_details": "I want to pet someone's dog"}], "location": 1}
    else:
        return {"inserted": False}


def upload_task(username, task_description, category=None, time_to_execute=None):
    # check if user is in db
    var = randint(0, 1)
    if var == 1:
        # run language model on task
        # insert new task to db
        return {"inserted": True, "task id": 1}
    else:
        return {"inserted": False}


def get_matches(username=None, location=None, suggestions=None, task_time=None):
    pass