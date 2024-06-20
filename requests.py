from random import randint


def login(username):
    # send username to db
    var = randint(0,1)
    if var == 1:
        return {"exists": True, "user id": 1234, "requests" :
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
        return {"inserted": True, "user id": 1234,
                "suggestions": [{"task_details": "I want to pet someone's dog"}], "location": 1}
    else:
        return {"inserted": False}


def upload_task(user_id, task_description, category=None, time_to_execute=None):
    # check if user is in db
    var = randint(0, 1)
    if var == 1:
        # run language model on task
        # insert new task to db
        return {"inserted": True, "task id": 1}
    else:
        return {"inserted": False}


def get_matches(user_id=None, location=None, suggestions=None, task_time=None, status=None):
    if suggestions:
        # run language model on new suggestions
        pass
    # query tasks table according to the values provided
    return {"matched_tasks": [{"task_details": "I need someone to pet my dog", "requesting_user": 1234,
                               "time_remaining": 5, "status": 2, "executing_username":"amit"},
                 {"task_details": "Connect to my db bls", "requesting_user": 1234, "time_remaining": 5, "status": 1}]}


def get_user_by_id(user_id):
    # fetch user from db. also fetch tasks and suggestions for this user.
    return {"exists": True, "requests":
        [{"task_details": "I need someone to pet my dog", "time_remaining": 5, "status": 2,
          "executing_username": "amit"},
         {"task_details": "Connect to my db bls", "time_remaining": 5, "status": 1}],
            "suggestions": [{"task_details": "I want to pet someone's dog"}], "location": 1}


def upload_help_suggestion(user_id, suggestions):
    # run language model on new suggestions
    # insert new suggestions to db
    return {"inserted": True}


def update_task_status(task_id, status, executing_user_id=None):
    # update task id and status. set executing user id.
    pass

