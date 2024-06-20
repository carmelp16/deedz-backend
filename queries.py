USER_QUERY = """
SELECT id, username, neighborhood_id
FROM users
WHERE username = %s;"""

TASKS_BY_HELPEE = """
SELECT *
FROM tasks
WHERE helpee_id = %s
JOIN users
ON (users.id == tasks.executing_helper_id); """


SUGGESTIONS_BY_HELPER = """
SELECT id, help_sentence
FROM help_suggestions
WHERE user_id = %s; """

UPDATE_TASK_STATUS = """
UPDATE tasks
SET status = %s,
    executing_helper_id = %s,
WHERE helpee_id = %s;
"""

INSERT_USER = """
INSERT INTO "users" ("username", "email", "neighborhood_id", "phone_number", "rewards") VALUES
(%s, %s, %s, %s, 0)
RETURNING id;
"""

INSERT_SUGGESTION = """
INSERT INTO "help_suggestions" ("user_id", "help_sentance") VALUES
(%s, %s);
RETURNING id;
"""

INSERT_TASK = """
INSERT INTO "tasks" ("helpee_id", "category", "neighborhood_id", "task_details", "task_time", "status", "executing_helper_id") VALUES
(%s, %s, %s, %s, %s, 'pending', NULL)
RETURNING id; """

INSERT_MATCH = """
INSERT INTO "matches" ("task_id", "suggestion_id", "match_score") VALUES
(%s, %s, %s);
"""