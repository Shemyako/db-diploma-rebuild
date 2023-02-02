CREATE TABLE "types_of_lesson" (
	"id" serial NOT NULL,
	"name" varchar(100) NOT NULL,
	"client_price" float8,
	"staff_payment" float8,
	"is_actual" bool NOT NULL,
	CONSTRAINT "types_of_lesson_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "dogs" (
	"id" serial NOT NULL,
	"name" varchar(20) NOT NULL,
	"breed" varchar(20) NOT NULL,
	"is_learning" bool NOT NULL,
	"staff_id" int,
	"place_id" int,
	CONSTRAINT "dogs_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "user_dog" (
	"id" serial NOT NULL,
	"staff_id" int,
	"dog_id" int,
	CONSTRAINT "users_dog_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "lessons" (
	"id" serial NOT NULL,
	"date" TIMESTAMP NOT NULL,
	"dog_id" int NOT NULL,
	"place_id" int NOT NULL,
	"type_of_lesson_id" int NOT NULL,
	"staff_id" int NOT NULL,
	CONSTRAINT "lesson_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "staff" (
	"id" serial NOT NULL,
	"name" varchar(20) NOT NULL,
	"role" int NOT NULL,
	"phone" varchar(15) NOT NULL,
	"date_of_birth" DATE,
	"tg_id" int,
	"e_mail" varchar(100),
	CONSTRAINT "staff_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "places" (
	"id" serial NOT NULL,
	"address" varchar(255) NOT NULL,
	"name" varchar(30) NOT NULL,
	"is_actual" bool NOT NULL,
	CONSTRAINT "places_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "advertisements" (
	"id" serial NOT NULL,
	"name" varchar(20) NOT NULL,
	"created_by" int NOT NULL,
	"date_to_post" TIMESTAMP NOT NULL,
	"topic" varchar(100) NOT NULL,
	"text" varchar(255) NOT NULL,
	"send_to" varchar(2) NOT NULL,
	CONSTRAINT "advertisement_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "users" (
	"id" serial NOT NULL,
	"password" varchar(100) NOT NULL,
	"staff_id" int NOT NULL,
	CONSTRAINT "user_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "courses" (
	"id" serial NOT NULL,
	"name" varchar(100) NOT NULL,
	"lesson_amount" int NOT NULL,
	"price" float4 NOT NULL,
	"is_actual" bool NOT NULL,
	CONSTRAINT "courses_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "dog_course" (
	"id" serial NOT NULL,
	"dog_id" int NOT NULL,
	"course_id" int NOT NULL,
	"date" DATE NOT NULL,
	CONSTRAINT "dog_cours_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "sessions" (
	"id" serial NOT NULL,
	"user_id" int NOT NULL,
	"token" varchar(40),
	"time" bigint NOT NULL,
	"ip" varchar(40) NOT NULL,
	"mac" varchar(20) NOT NULL,
	CONSTRAINT "sessions_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "dogs" ADD CONSTRAINT "dogs_fk0" FOREIGN KEY ("staff_id") REFERENCES "staff"("id");
ALTER TABLE "dogs" ADD CONSTRAINT "dogs_fk1" FOREIGN KEY ("place_id") REFERENCES "places"("id");

ALTER TABLE "user_dog" ADD CONSTRAINT "users_dog_fk0" FOREIGN KEY ("staff_id") REFERENCES "staff"("id");
ALTER TABLE "user_dog" ADD CONSTRAINT "users_dog_fk1" FOREIGN KEY ("dog_id") REFERENCES "dogs"("id");

ALTER TABLE "lessons" ADD CONSTRAINT "lesson_fk0" FOREIGN KEY ("dog_id") REFERENCES "dogs"("id");
ALTER TABLE "lessons" ADD CONSTRAINT "lesson_fk1" FOREIGN KEY ("place_id") REFERENCES "places"("id");
ALTER TABLE "lessons" ADD CONSTRAINT "lesson_fk2" FOREIGN KEY ("type_of_lesson_id") REFERENCES "types_of_lesson"("id");
ALTER TABLE "lessons" ADD CONSTRAINT "lesson_fk3" FOREIGN KEY ("staff_id") REFERENCES "staff"("id");



ALTER TABLE "advertisements" ADD CONSTRAINT "advertisement_fk0" FOREIGN KEY ("created_by") REFERENCES "staff"("id");

ALTER TABLE "users" ADD CONSTRAINT "user_fk0" FOREIGN KEY ("staff_id") REFERENCES "staff"("id");


ALTER TABLE "dog_course" ADD CONSTRAINT "dog_cours_fk0" FOREIGN KEY ("dog_id") REFERENCES "dogs"("id");
ALTER TABLE "dog_course" ADD CONSTRAINT "dog_cours_fk1" FOREIGN KEY ("course_id") REFERENCES "courses"("id");

ALTER TABLE "sessions" ADD CONSTRAINT "sessions_fk0" FOREIGN KEY ("user_id") REFERENCES "user"("id");











