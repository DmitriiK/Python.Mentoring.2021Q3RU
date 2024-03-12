from peewee import Model,  PrimaryKeyField, ForeignKeyField,\
    CompositeKey, CharField, DateField,  DoubleField, SqliteDatabase
import datetime

# db = PostgresqlDatabase('postgres', user="postgres", password=***)
db = SqliteDatabase('testdb.db')


class Employees(Model):
    Id = PrimaryKeyField(null=False)
    FirstName = CharField()
    LastName = CharField()
    Patronymic = CharField()

    class Meta:
        database = db


class Salary(Model):
    Employee = ForeignKeyField(Employees, null=False, backref='SalaryFacts')
    Dt = DateField(null=False, default=datetime.date.today)  # Дата выплаты
    Salary_Type = CharField(max_length=10, null=False)
    Amount = DoubleField(null=False)  # выплаченная сумма

    class Meta:
        database = db
        primary_key = CompositeKey('Employee', 'Dt', 'Salary_Type')


class Emails(Model):
    Id = PrimaryKeyField(null=False)
    Employee = ForeignKeyField(Employees, null=False, backref='Emails')
    Email = CharField(max_length=50, null=False)

    class Meta:
        database = db


if __name__ == '__main__':
    Employees.create_table()
    Salary.create_table()
    Emails.create_table()
