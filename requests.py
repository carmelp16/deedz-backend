from random import randint

def login(username):
    #send username to db
    var = randint(0,1)
    if var == 1:
        return {"exists": True,"requests" : 
                [{"task_details":"I need someone to pet my dog", "time_remaining": 5, "status": 2, "executing_username":"amit"},
                 {"task_details":"Connect to my db bls", "time_remaining": 5, "status": 1}],
                  "suggestions": [{"task_details": "I want to pet someone's dog"}], "location" : 1}
    else:
        return {"exists":False}
