from task_09_02_metadata import Emails, Employees, Salary

# clean-up
Emails.truncate_table()
Salary.truncate_table()
query = Employees.delete()
query.execute()

lst = [
    (1, 'Шершуков', 'Виктор', 'Кузьмич',),
    (2, 'Битова', 'Анастасия', 'Юрьевна',),
    (3, 'Кириллов', 'Валентин', 'Владиславович',),
    (4, 'Игнатьев', 'Игорь', 'Дмитриевич',),
]
for emp in lst:
    db_emp = Employees(Id=emp[0], LastName=emp[1],
                       FirstName=emp[2], Patronymic=emp[3])
    db_emp.save(force_insert=True)

emails = [
    (1, 1, 'shershuko@mail.ru',),
    (2, 1, 'shershuko-v@mail.ru',),
    (3, 2, 'bitova@mail.ru',),
    (4, 2, 'bitova@mail.ru',),
    (5, 3, 'kirillov@mail.ru',),
    (6, 3, 'kirillov@mail.ru',),
]
for itm in emails:
    db_itm = Emails(Id=itm[0], Employee=itm[1], Email=itm[2])
    db_itm.save(force_insert=True)

salary_facts = [
    (1, '2019-12-01', 'salary', 50000),
    (1, '2020-01-01', 'salary', 50000),
    (1, '2020-02-01', 'salary', 50000),
    (1, '2020-03-01', 'salary', 50000),
    (1, '2020-04-01', 'salary', 50000),
    (1, '2020-05-01', 'salary', 50000),
    (1, '2020-06-01', 'salary', 53000),
    (1, '2020-07-01', 'salary', 53000),
    (1, '2020-08-01', 'salary', 53000),
    (1, '2020-09-01', 'salary', 53000),
    (1, '2020-10-01', 'salary', 53000),
    (1, '2020-11-01', 'salary', 53000),
    (1, '2020-12-01', 'salary', 53000),
    (1, '2021-01-01', 'salary', 53000),
    (1, '2019-12-01', 'bonus', 10000),
    (1, '2020-01-01', 'bonus', 10000),
    (1, '2020-02-01', 'bonus', 9000),
    (1, '2020-03-01', 'bonus', 11000),
    (1, '2020-04-01', 'bonus', 10000),
    (1, '2020-05-01', 'bonus', 5000),
    (1, '2020-06-01', 'bonus', 10000),
    (1, '2020-07-01', 'bonus', 10000),
    (1, '2020-08-01', 'bonus', 10000),
    (1, '2020-09-01', 'bonus', 10000),
    (1, '2020-10-01', 'bonus', 10000),
    (1, '2020-11-01', 'bonus', 10000),
    (1, '2020-12-01', 'bonus', 10000),
    (1, '2021-01-01', 'bonus', 10000),
    (2, '2019-12-01', 'salary', 60000),
    (2, '2020-01-01', 'salary', 60000),
    (2, '2020-02-01', 'salary', 60000),
    (2, '2020-03-01', 'salary', 62000),
    (2, '2020-04-01', 'salary', 62000),
    (2, '2020-05-01', 'salary', 62000),
    (2, '2020-06-01', 'salary', 62000),
    (2, '2020-07-01', 'salary', 62000),
    (2, '2020-08-01', 'salary', 62000),
    (2, '2020-09-01', 'salary', 62000),
    (2, '2020-10-01', 'salary', 65000),
    (2, '2020-11-01', 'salary', 65000),
    (2, '2020-12-01', 'salary', 65000),
    (2, '2021-01-01', 'salary', 65000),
    (2, '2019-12-01', 'bonus', 10000),
    (2, '2020-01-01', 'bonus', 10000),
    (2, '2020-02-01', 'bonus', 9000),
    (2, '2020-03-01', 'bonus', 11000),
    (2, '2020-04-01', 'bonus', 10000),
    (2, '2020-05-01', 'bonus', 5000),
    (2, '2020-06-01', 'bonus', 10000),
    (2, '2020-07-01', 'bonus', 7000),
    (2, '2020-08-01', 'bonus', 7000),
    (2, '2020-09-01', 'bonus', 7000),
    (2, '2020-10-01', 'bonus', 7000),
    (2, '2020-11-01', 'bonus', 7000),
    (2, '2020-12-01', 'bonus', 7000),
    (2, '2021-01-01', 'bonus', 7000),
    (3, '2019-12-01', 'salary', 60000),
    (3, '2020-01-01', 'salary', 60000),
    (3, '2020-02-01', 'salary', 60000),
    (3, '2020-03-01', 'salary', 60000),
    (3, '2020-04-01', 'salary', 60000),
    (3, '2020-05-01', 'salary', 60000),
    (3, '2020-06-01', 'salary', 60000),
    (3, '2020-07-01', 'salary', 60000),
    (3, '2020-08-01', 'salary', 60000),
    (3, '2020-09-01', 'salary', 60000),
    (3, '2020-10-01', 'salary', 60000),
    (3, '2020-11-01', 'salary', 64000),
    (3, '2020-12-01', 'salary', 64000),
    (3, '2021-01-01', 'salary', 64000),
    (4, '2019-12-01', 'salary', 61000),
    (4, '2020-01-01', 'salary', 61000),
    (4, '2020-02-01', 'salary', 61000),
    (4, '2020-03-01', 'salary', 61000),
    (4, '2020-04-01', 'salary', 61000),
    (4, '2020-05-01', 'salary', 63000),
    (4, '2020-06-01', 'salary', 63000),
    (4, '2020-07-01', 'salary', 63000),
    (4, '2020-08-01', 'salary', 63000),
    (4, '2020-09-01', 'salary', 63000),
    (4, '2020-10-01', 'salary', 63000),
    (4, '2020-11-01', 'salary', 63000),
    (4, '2020-12-01', 'salary', 63000),
    (4, '2021-01-01', 'salary', 63000),
    (4, '2019-12-01', 'bonus', 7000),
    (4, '2020-01-01', 'bonus', 7000),
    (4, '2020-02-01', 'bonus', 7000),
    (4, '2020-03-01', 'bonus', 7000),
    (4, '2020-04-01', 'bonus', 7000),
    (4, '2020-05-01', 'bonus', 7000),
    (4, '2020-06-01', 'bonus', 7000),
    (4, '2020-07-01', 'bonus', 7000),
    (4, '2020-08-01', 'bonus', 7000),
    (4, '2020-09-01', 'bonus', 7000),
    (4, '2020-10-01', 'bonus', 7000),
    (4, '2020-11-01', 'bonus', 7000),
    (4, '2020-12-01', 'bonus', 7000),
    (4, '2021-01-01', 'bonus', 7000),
]

for itm in salary_facts:
    db_itm = Salary(Employee=itm[0], Dt=itm[1],
                    Salary_Type=itm[2], Amount=itm[3])
    db_itm.save(force_insert=True)
