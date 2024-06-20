CREATE TYPE "task_type" AS ENUM (
  'cleaning',
  'cooking',
  'delivery',
  'other'
);

CREATE TYPE "task_status" AS ENUM (
  'pending',
  'bided',
  'done'
);

CREATE TYPE "task_timing" AS ENUM (
  'immidiate',
  'day',
  'week'
);

CREATE TABLE "users" (
  "id" serial PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "neighborhood_id" int,
  "phone_number" varchar,
  "rewards" int,
  "created_at" timestamp DEFAULT (now())
);

CREATE TABLE "tasks" (
  "id" serial PRIMARY KEY,
  "helpee_id" int,
  "category" task_type,
  "neighborhood_id" int,
  "task_details" text,
  "task_time" task_timing,
  "status" task_status,
  "executing_helper_id" int,
  "created_at" timestamp DEFAULT (now())
);

CREATE TABLE "help_suggestions" (
  "id" serial PRIMARY KEY,
  "user_id" int,
  "help_sentance" text
);

CREATE TABLE "matches" (
  "task_id" int,
  "suggestion_id" int,
  "match_score" float
);

CREATE TABLE "photos" (
  "user_id" int,
  "photo" bytea
);

ALTER TABLE "tasks" ADD FOREIGN KEY ("helpee_id") REFERENCES "users" ("id");

ALTER TABLE "tasks" ADD FOREIGN KEY ("executing_helper_id") REFERENCES "users" ("id");

ALTER TABLE "help_suggestions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "matches" ADD FOREIGN KEY ("task_id") REFERENCES "tasks" ("id");

ALTER TABLE "matches" ADD FOREIGN KEY ("suggestion_id") REFERENCES "help_suggestions" ("id");

ALTER TABLE "photos" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
