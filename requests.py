from random import randint
import utils
import queries
from datetime import datetime

HOST = "dpg-cpa811tds78s73ct2q20-a.frankfurt-postgres.render.com"
USERNAME = "uza"
PASSWORD = "rF2Tj4BOHkn9JDJRgJpVWWhpn5MsUdUr"
DB_NAME = "taub"

TIME_DICT = {
    'hours': 4,
    'day': 24,
    'week': 168
}


def login(username):
    # send username to db
    user = utils.execute_query(queries.USER_QUERY_BY_NAME, HOST, DB_NAME, USERNAME, PASSWORD, params=(username, ))
    if not user:
        return {"exists": False}
    else:
        user = user[0]
        user_id = user["id"]
        tasks = utils.execute_query(queries.TASKS_BY_HELPEE, HOST, DB_NAME, USERNAME, PASSWORD, params=(user_id, ))
        suggestions = utils.execute_query(queries.SUGGESTIONS_BY_HELPER, HOST, DB_NAME, USERNAME, PASSWORD,
                                          params=(user_id, ))

        requests = []
        for task in tasks:
            request = {"task_details": task["task_details"]}

            given_time = task["task_creation"]
            time_difference = datetime.now() - given_time
            difference_in_hours = time_difference.total_seconds() / 3600
            request["time_remaining"] = TIME_DICT[task["task_time"]] - difference_in_hours

            request["status"] = task["status"]
            request["executing_username"] = task["helper_username"]
            requests.append(request)

        suggestions_list = [{"task_details": sug["help_sentence"]} for sug in suggestions]

        return {"exists": True, "user id": user_id, "requests":
                requests, "suggestions": suggestions_list, "location": user["neighborhood_id"],
                "photo": "base64string"}


def register(username, phone_number, location, suggestions, photo=None):
    # check if user is in db
    var = randint(0, 1)
    if var == 1:
        # run language model on suggestions
        # insert new user to db
        return {"inserted": True, "user id": 1234,
                "suggestions": [{"task_details": "I want to pet someone's dog"}], "location": 1, "photo": "base64string"}
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
            "suggestions": [{"task_details": "I want to pet someone's dog"}], "location": 1, "photo": "base64string"}


def upload_help_suggestion(user_id, suggestions):
    # run language model on new suggestions
    # insert new suggestions to db
    return {"inserted": True}


def update_task_status(task_id, status, executing_user_id=None):
    update = utils.execute_query(queries.UPDATE_TASK_STATUS, HOST, DB_NAME, USERNAME, PASSWORD, params=(status, executing_user_id, task_id))
    if update:
    # update task id and status. set executing user id.
        return {"updated": True, "task_id": task_id}
    return {"updated": False, "task_id": task_id}


if __name__ == "__main__":
    res = update_task_status(1, 'done', 3)
    print(res)