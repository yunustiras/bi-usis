# Roles Default data
INSERT INTO roles (name)
VALUES ("idari_personel"),
       ("teacher"),
       ("student");

# Users Default data
INSERT INTO users (username, password, first_name, middle_name, surname, role_id)
VALUES ("00000001", "123", 'yunus', null, 'yunus', 3),
       ("00000002", "321", 'admin', null, 'admin', 2),
       ("00000003", "213", 'emre', null, 'emre', 1);


       INSERT INTO form_questions (question)
       VALUES ("Ders planina gore hoca haftalik programa uydu"),
              ("Hoca derse zamaninda geldi"),
              ("Verdigi odevler dersi anlama acisindan ogretici idi");

       INSERT INTO form_names (form_name)
       VALUES  ("Ders degerlendirme formu");

       INSERT INTO form_content (form_name_id,form_question_id)
       VALUES  (1,1),
               (1,2),
               (1,3);

       INSERT INTO form_answers (form_name,question,answer, who_answered, answer_time)
       VALUES  (1,1,"evet",1,"2018-5-5"),
               (1,2,"evet",1,"2018-5-5"),
               (1,3,"evet",1,"2018-5-5");
