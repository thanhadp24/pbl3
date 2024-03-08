INSERT INTO career(`name`)
VALUES ('IT hardware - Network - Telecommunication'),
	   ('Business'),
       ('Finance - Investment'),
       ('Marketing'),
       ('Auditing');

INSERT INTO career(`name`)
VALUES ('IT software'),
	   ('Design - Creative Arts'),
       ('HealthCare');
 
SELECT * FROM career ORDER BY ID ASC;
SELECT * FROM position;
SELECT * FROM company;
SELECT * FROM info_recruitment_detail where JOB_NAME = 'Miền Trung_Nhân Viên Tư Vấn Tài Chính Thị Trường';