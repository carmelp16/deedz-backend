from random import randint
import utils
import queries
from datetime import datetime
from task_similarity import SemanticSim
from typing import List
import requests
import base64

HOST = "dpg-cpa811tds78s73ct2q20-a.frankfurt-postgres.render.com"
USERNAME = "uza"
PASSWORD = "rF2Tj4BOHkn9JDJRgJpVWWhpn5MsUdUr"
DB_NAME = "taub"

TIME_DICT = {
    'immidiate': 4,
    'day': 24,
    'week': 168
}

def generate_face_pic():
    url = "https://thispersondoesnotexist.com/"
    response = requests.get(url)

    return base64.b64encode(response.content).decode('utf-8')\

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


def register(username, email, phone_number, location, suggestions, photo=None):
    # check if user is in db
    user = utils.execute_query(queries.USER_QUERY, HOST, DB_NAME, USERNAME, PASSWORD, params=username)
    if user:
        return {"inserted": False}
    else:
        new_user_id = utils.execute_query(queries.INSERT_USER, HOST, DB_NAME, USERNAME, PASSWORD,
                                          params=(username, email, location, phone_number))
        utils.execute_query(queries.INSERT_PHOTO, HOST, DB_NAME, USERNAME, PASSWORD,
                            params=(new_user_id, photo))
        for suggestion in suggestions:
            utils.execute_query(queries.INSERT_SUGGESTION, HOST, DB_NAME, USERNAME, PASSWORD,
                                params=(new_user_id, suggestion))
        return {"inserted": True, "user id": new_user_id, "requests": [],
                "suggestions": suggestions, "location": location, "photo": photo}
    

def compare_task_to_suggestions(task_id):
    # query all suggestions
    suggestions = utils.execute_query(queries.ALL_SUGGESTIONS, HOST, DB_NAME, USERNAME, PASSWORD)
    sug_vectors = [sug['embeddings'] for sug in suggestions]

    #query task embedding
    task = utils.execute_query(queries.TA, HOST, DB_NAME, USERNAME, PASSWORD)
    task_vector = []
    
    # compare to task
    semantic = SemanticSim()
    res = semantic.calc_cosine_sim_with_lists([task_description], sug_list)

    ### TODO: finish insertion back

def compare_user_to_tasks(user_id: str, user_suggestions: List[str]):
    # query all active tasks
    tasks = utils.execute_query(queries.ALL_TASKS, HOST, DB_NAME, USERNAME, PASSWORD)
    task_list = [task['task_details'] for task in tasks]

    # compare to user suggestions 
    semantic = SemanticSim()
    res = semantic.calc_cosine_sim_with_lists(user_suggestions,  task_list)

    ### TODO: finish insertion back


def upload_task(user_id, task_description, category=None, time_to_execute=None):
    semantic = SemanticSim()
    vec = semantic.create_emmbedings([task_description])[0]
    task = utils.execute_query(queries.INSERT_TASK, HOST, DB_NAME, USERNAME, PASSWORD,
                                params=(user_id, category, 0, task_description, time_to_execute ))
    if not task:
        return {"inserted": False}
    
    task_id = task[0]["id"]
    compare_task_to_suggestions(task_id, task_description)
    return {'inserted' : True}



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
    # update task id and status. set executing user id.
    update = utils.execute_query(queries.UPDATE_TASK_STATUS, HOST, DB_NAME, USERNAME, PASSWORD, params=(status, executing_user_id, task_id))
    if update:
        return {"updated": True, "task_id": task_id}
    return {"updated": False, "task_id": task_id}