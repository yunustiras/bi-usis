DROP DATABASE biusis;
CREATE DATABASE IF NOT EXISTS biusis;
USE biusis;

# create user for biusis database
DROP USER 'biusis'@'localhost';
CREATE USER 'biusis'@'localhost' IDENTIFIED BY 'biusis';

# grant permission biusis user for database
GRANT ALL PRIVILEGES ON biusis.* TO 'biusis'@'localhost';

# Roles Table
DROP TABLE IF EXISTS roles;
CREATE TABLE roles (
  id    INT AUTO_INCREMENT UNIQUE NOT NULL,
  name  VARCHAR(15) NOT NULL,
  PRIMARY KEY (id)
);

# Role-Funcs Table
DROP TABLE IF EXISTS role_funcs;
CREATE TABLE role_funcs (
  id          INT AUTO_INCREMENT UNIQUE NOT NULL,
  func_name   VARCHAR(15),
  role_id     INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (role_id) REFERENCES roles(id)
);


# Users Table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id          INT AUTO_INCREMENT UNIQUE NOT NULL,
  username    VARCHAR(8) NOT NULL,
  password    VARCHAR(256) NOT NULL,
  first_name  VARCHAR(25) NOT NULL, # Ilk Adı -
  middle_name VARCHAR(25),          # Ortanca Adı --
  surname     VARCHAR(25) NOT NULL, # Soyadi ---
  role_id     INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

############### STUDENT
DROP TABLE IF EXISTS student_general_info;
CREATE TABLE student_general_info (
  id                   INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id              INT NOT NULL,
  tc                   VARCHAR(11) NOT NULL, # TC --
  nationality          VARCHAR(25) NOT NULL, # Uyruğu
  gender               VARCHAR(8) NOT NULL,  # Cinsiyet
  birthplace           VARCHAR(20) NOT NULL, # Dogum yeri --
  birthdate            DATE NOT NULL,        # Dogum tarihi --
  pension_fund         BOOLEAN NOT NULL,     # Emekli Sandığı (Yok,Var)
  military_service     BOOLEAN NOT NULL,     # Askerlik Hizmeti (Yapıldı, Yapılmadı)
  disability_status    VARCHAR(25) NOT NULL, # Özür Durumu
  is_want_scholarship  BOOLEAN NOT NULL,     # Burs İstiyor Mu? (Evet Hayır)
  preference_order     INT(4) NOT NULL,      # YTÜ Bilgisayar Tercih Sırası
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS student_highschool_info; # Mezun Olunan Lise Bilgileri
CREATE TABLE student_highschool_info (
  id                    INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id               INT NOT NULL,
  school_name           VARCHAR(25) NOT NULL, # Mezun Olunan Lise --
  school_department     VARCHAR(25) NOT NULL, # Mezun Olunan Bölüm --
  diploma_success_note  VARCHAR(11) NOT NULL, # Diploma Başarı Notu --
  diploma_course_branch VARCHAR(25) NOT NULL, # Diploma Kolu / Branşı --
  foreign_language      VARCHAR(8) NOT NULL,  # Yabanci Dil --
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS student_population_info; # Nüfus Bilgileri
CREATE TABLE student_population_info (
  id                          INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id                     INT NOT NULL,
  neighborhoodNvillage        VARCHAR(25) NOT NULL, # Mahalle / Köy --
  population_administration   VARCHAR(25) NOT NULL, # Verildiği Nüfus İdaresi --
  c_no                        INT(11) NOT NULL,     # Cilt No
  id_card_no                  INT(11) NOT NULL,     # Nüfus Cüzdanı No --
  family_queue_no             INT(4) NOT NULL,      # Aile Sıra No --
  queue_no                    INT(4) NOT NULL,      # Sıra No --
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS student_university_info;
CREATE TABLE student_university_info (
  id                       INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id                  INT NOT NULL,
  university_student_no    INT(11) NOT NULL,     # Üniversite Öğrenci No
  faculty                  VARCHAR(25) NOT NULL, # Fakülte / MYO
  department               VARCHAR(25) NOT NULL, # Bölüm / Program
  teaching_style           VARCHAR(10) NOT NULL, # Öğretim Şekli --
  student_score            INT(4) NOT NULL,      # Öss Puanı --
  completed_yok            VARCHAR(25) NOT NULL, # Tamamlanan Yök --
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS student_university_preferences;
CREATE TABLE student_university_preferences (
  id                INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id           INT NOT NULL,
  preference_name   VARCHAR(25) NOT NULL, # Tercih edilen universite
  preference_index  INT NOT NULL,         # Tercih sirasi
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS student_interests;
CREATE TABLE student_interests (
  id              INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id         INT NOT NULL,
  interest_name   VARCHAR(25) NOT NULL, # Ilgisi | Select ile secilirse iyi olur.
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

#################### Family
DROP TABLE IF EXISTS student_family;
CREATE TABLE student_family (
  id                     INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id                INT NOT NULL,
  monthly_income_level   VARCHAR(25) NOT NULL,  # Aile Aylık Gelir Düzeyi
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS other_person_types;
CREATE TABLE other_person_types (
	id      INT AUTO_INCREMENT UNIQUE NOT NULL,
  name    VARCHAR(15) NOT NULL,  # Baba, Anne, Kardes
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS other_persons;
CREATE TABLE other_persons (
  id                     INT AUTO_INCREMENT UNIQUE NOT NULL,
  family_id              INT NOT NULL,
  name                   VARCHAR(25) NOT NULL,  # Isim
  type_id                INT NOT NULL,          # Ogrencinin neyi
  job                    VARCHAR(256) NOT NULL, # Isi
  gender                 VARCHAR(8) NOT NULL,   # Cinsiyeti
  marial_status          VARCHAR(8) NOT NULL,   # Evlilik durumu
  education_state        VARCHAR(256) NOT NULL, # Ogretim durumu
  phone_no               INT(12),               # Telefon numarasi
  email                  VARCHAR(25),           # Email adresi
  birth_date             DATE NOT NULL,         # Dogum tarihi
  death_date             DATE NOT NULL,         # Olum tarihi
  PRIMARY KEY (id),
  FOREIGN KEY (family_id) REFERENCES student_family(id),
  FOREIGN KEY (type_id) REFERENCES other_person_types(id)
);

############ Emails, Phones, Addresses
DROP TABLE IF EXISTS person_type; # user, family, near to family,
CREATE TABLE  person_type (
  id       INT AUTO_INCREMENT UNIQUE NOT NULL,
  name     VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS emails;
CREATE TABLE emails (
  id          INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id     INT NOT NULL,
  type_id     INT NOT NULL,
  value       VARCHAR(50) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (type_id) REFERENCES person_type(id)
);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
  id          INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id     INT NOT NULL,
  type_id     INT NOT NULL,
  value       VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (type_id) REFERENCES person_type(id)
);

DROP TABLE IF EXISTS phones;
CREATE TABLE phones (
  id          INT AUTO_INCREMENT UNIQUE NOT NULL,
  user_id     INT NOT NULL,
  type_id     INT NOT NULL,
  value       VARCHAR(11) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (type_id) REFERENCES person_type(id)
);

############# Gorusler, Danismanlik ve Danismanlik gorusmeleri
DROP TABLE IF EXISTS consultancy;
CREATE TABLE consultancy (
  id          INT AUTO_INCREMENT UNIQUE NOT NULL,
  teacher_id 	INT NOT NULL,
  student_id  INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (teacher_id) REFERENCES users(id),
  FOREIGN KEY (student_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS opinion;
CREATE TABLE opinion (
  id               INT AUTO_INCREMENT UNIQUE NOT NULL,
  consultancy_id   INT NOT NULL,
  content          VARCHAR(256) NOT NULL,
  create_date      DATE NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (consultancy_id) REFERENCES  consultancy(id)
);

DROP TABLE IF EXISTS meetings;
CREATE TABLE meetings (
  id              INT AUTO_INCREMENT UNIQUE NOT NULL,
  consultancy_id  INT NOT NULL,   # Danismanlik id
  who             INT NOT NULL,   # Kim
  to_who          INT NOT NULL,   # Kime
  comment         VARCHAR(256) NOT NULL,
  created_date    DATE NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (consultancy_id) REFERENCES consultancy(id),
  FOREIGN KEY (who) REFERENCES users(id),
  FOREIGN KEY (to_who) REFERENCES users(id)
);

DROP TABLE IF EXISTS log;
CREATE TABLE log (
  id              INT AUTO_INCREMENT UNIQUE NOT NULL,
  table_name      VARCHAR(15) NOT NULL,
  column_name     VARCHAR(15) NOT NULL,
  row_id          INT NOT NULL,
  old_value       VARCHAR(15) NOT NULL,
  modified_time   DATE NOT NULL,
  who_modified    INT NOT NULL,
  ip_addr         VARCHAR(15) NOT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS form_questions;
CREATE TABLE form_questions (
  id              INT AUTO_INCREMENT UNIQUE NOT NULL,
  question        VARCHAR(256) UNIQUE NOT NULL,

  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS form_names;
CREATE TABLE form_names (
  id              INT AUTO_INCREMENT UNIQUE NOT NULL,
  form_name       VARCHAR(256) UNIQUE NOT NULL,

  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS form_content;
CREATE TABLE form_content (
  id                INT AUTO_INCREMENT UNIQUE NOT NULL,
  form_name_id      INT NOT NULL,
  form_question_id  INT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_name_id) REFERENCES form_names(id),
  FOREIGN KEY (form_question_id) REFERENCES form_questions(id)
);

DROP TABLE IF EXISTS form_answers;
CREATE TABLE form_answers (
  id              INT AUTO_INCREMENT UNIQUE NOT NULL,
  form_name       VARCHAR(256) NOT NULL,
  question        VARCHAR(256) NOT NULL,
  answer          VARCHAR(256) NOT NULL,
  who_answered    INT NOT NULL,
  answer_time     DATE NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_name) REFERENCES form_names(id),
  FOREIGN KEY (question) REFERENCES form_questions(id),
  FOREIGN KEY (who_answered) REFERENCES user(id)
);
