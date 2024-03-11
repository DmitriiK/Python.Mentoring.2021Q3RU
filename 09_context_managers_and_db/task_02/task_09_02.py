import datetime
from task_09_02_metadata import Emails, Employees, Salary
from peewee import Value, fn, JOIN


def print_report():
    # 1, Шершуков Виктор Кузьмич,  51750 .0, 9583.33, sh@mail.ru
    dt_format = '%Y-%m-%d'
    dt_from = datetime.datetime.strptime('2020-01-01', dt_format).date()
    dt_to = datetime.datetime.strptime('2021-01-01', dt_format).date()
    """ calculated column definitions
    main_salary = Case(Salary.Salary_Type, (('salary', Salary.Amount),), 0)
    bonus = Case(Salary.Salary_Type, (('bonus', Salary.Amount),), 0)
    """
    aggr_salary = (Salary.select(Salary.Employee.alias('EmpId'),
                                 Salary.Salary_Type,
                                 fn.Avg(Salary.Amount).alias('AvgAmount')
                                 )
                   .where(Salary.Dt >= dt_from, Salary.Dt < dt_to)
                   .group_by(Salary.Employee, Salary.Salary_Type)
                   .cte('aggr_salary')
                   )

    main_salary = (aggr_salary.select(aggr_salary.c.EmpId,
                                      aggr_salary.c.AvgAmount)
                   .where(aggr_salary.c.Salary_Type == 'salary')
                   .with_cte(aggr_salary)
                   .cte('main_salary')
                   )

    bonus = (aggr_salary.select(aggr_salary.c.EmpId, aggr_salary.c.AvgAmount)
             .where(aggr_salary.c.Salary_Type == 'bonus')
             .with_cte(aggr_salary)
             .cte('bonus')
             )

    final_query = (Employees
                   .select(Employees, Value(Emails.Email).alias('Email'),
                           Value(main_salary.c.AvgAmount).alias('Salary'),
                           Value(bonus.c.AvgAmount).alias('Bonus'))
                   .join(Emails, JOIN.LEFT_OUTER)
                   .join(main_salary, JOIN.LEFT_OUTER,
                         on=(Employees.Id == main_salary.c.EmpId))
                   .join(bonus, JOIN.LEFT_OUTER,
                         on=(Employees.Id == bonus.c.EmpId))
                   .with_cte(aggr_salary, main_salary, bonus))
    # sql = final_query.sql()

    print('  ID FIO                                   Salary'
          '         Bonus     Email')
    for row in final_query:
        empl_id = row.Id
        fio = f'{row.LastName} ' \
              f'{row.FirstName} ' \
              f'{row.Patronymic}'
        row_bonus = 0 if row.Bonus is None else row.Bonus
        print(f'{empl_id:3} {fio:35}  {row.Salary:10.2f}   '
              f' {row_bonus:10.2f}   {row.Email}')


if __name__ == '__main__':
    print_report()
