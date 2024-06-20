-- Insert sample users
INSERT INTO "users" ("username", "email", "neighborhood_id", "phone_number", "rewards") VALUES
('avraham15', 'user1@example.com', 71, '052-1234567', 0),
('ruben63', 'user2@example.com', 71, '053-2345678', 0),
('sarah17', 'user3@example.com', 71, '054-3456789', 0);

-- Insert sample tasks
INSERT INTO "tasks" ("helpee_id", "category", "neighborhood_id", "task_details", "task_time", "status", "executing_helper_id") VALUES
(1, 'delivery', 71, 'להביא חלב וביצים מהמכולת', 'immidiate', 'pending', NULL),
(1, 'other', 71, 'להוציא את הכלב', 'day', 'pending', NULL),
(3, 'other', 72, 'לעזור לסחוב ארון יד שנייה', 'week', 'pending', NULL),
(3, 'delivery', 71, 'לאסוף כביסה מהמכבסה', 'week', 'pending', NULL),
(2, 'cooking', 71, 'לעזור להתיקן מדף', 'week', 'pending', NULL),


-- Insert sample help suggestions
INSERT INTO "help_suggestions" ("user_id", "help_sentance") VALUES
(1, 'יכול לעזור בניקיון'),
(1, 'עם רכב ויכול לנסוע לאן שצריך'),
(2, ' יכול לעזור בשיפוצים ועבודות בבית'),
(3, 'אנייכולה לעשות משלוחים');

-- -- Insert sample matches
-- INSERT INTO "matches" ("task_id", "suggestion_id", "match_score") VALUES
-- (1, 1, 0.9),
-- (2, 2, 0.85),
-- (3, 3, 0.95);

-- Insert sample photos
INSERT INTO "photos" ("user_id", "photo") VALUES
(1, decode('89504e470d0a1a0a0000000d4948445200000010000000100802000000909168970000000467414d410000b18f0bfc6105000000097048597300000ec400000ec401952b0e1b0000001974455874536f6674776172650041646f626520496d616765526561647971c9653c0000019b4944415478da62fcffcf80c41650002331b006096d30433f1a5c00154f70d8103030340305cc30000000049454e44ae426082', 'hex')),
(2, decode('89504e470d0a1a0a0000000d4948445200000010000000100802000000909168970000000467414d410000b18f0bfc6105000000097048597300000ec400000ec401952b0e1b0000001974455874536f6674776172650041646f626520496d616765526561647971c9653c0000019b4944415478da62fcffcf80c41650002331b006096d30433f1a5c00154f70d8103030340305cc30000000049454e44ae426082', 'hex')),
(3, decode('89504e470d0a1a0a0000000d4948445200000010000000100802000000909168970000000467414d410000b18f0bfc6105000000097048597300000ec400000ec401952b0e1b0000001974455874536f6674776172650041646f626520496d616765526561647971c9653c0000019b4944415478da62fcffcf80c41650002331b006096d30433f1a5c00154f70d8103030340305cc30000000049454e44ae426082', 'hex'));
