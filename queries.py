USER_QUERY_BY_ID = """
SELECT id, username, neighborhood_id
FROM users
WHERE id = %s;"""


USER_QUERY_BY_NAME = """
SELECT id, username, neighborhood_id
FROM users
WHERE username = %s;"""

ACTIVE_TASKS_BY_LOCATION = """
SELECT *
FROM tasks
WHERE status != 'done'
AND location = %s
"""

ALL_SUGGESTIONS = """
SELECT *
FROM help_suggestions
"""


TASKS_BY_HELPEE = """
with data as (SELECT users.id as user_id,
users.username,
users.neighborhood_id,
tasks.id as task_id,
tasks.task_time,
tasks.created_at as task_creation,
tasks.task_details,
tasks.status,
tasks.executing_helper_id
FROM users
JOIN tasks
ON users.id = tasks.helpee_id
WHERE users.id = %s
)
SELECT data.*, users.username as helper_username
FROM data
LEFT JOIN users
ON data.executing_helper_id = users.id;
"""

SUGGESTIONS_BY_HELPER = """
SELECT users.id as user_id,
users.username,
users.neighborhood_id,
help_suggestions.id as suggestion_id,
help_sentence,
embedding
FROM users
JOIN help_suggestions
ON users.id = help_suggestions.user_id
WHERE users.id = %s;
"""

UPDATE_TASK_STATUS = """
UPDATE tasks
SET status = %s,
    executing_helper_id = %s
WHERE id = %s
RETURNING id;
"""

INSERT_USER = """
INSERT INTO "users" ("username", "neighborhood_id", "phone_number", "rewards") VALUES
(%s, %s, %s, 0)
RETURNING id;
"""

INSERT_SUGGESTION = """
INSERT INTO "help_suggestions" ("user_id", "help_sentence", "embedding") VALUES
(%s, %s, %s)
RETURNING id;
"""

INSERT_TASK = """
INSERT INTO "tasks" ("helpee_id", "category", "neighborhood_id", "task_details", "task_time", "status", "executing_helper_id", "embedding") VALUES
(%s, %s, %s, %s, %s, 'pending', NULL, %s)
RETURNING id; """

INSERT_MATCH = """
INSERT INTO "matches" ("task_id", "suggestion_id", "match_score") VALUES
(%s, %s, %s);
"""

INSERT_PHOTO = """
INSERT INTO "photos" ("user_id", "photo") VALUES
(%s, %s);
"""
