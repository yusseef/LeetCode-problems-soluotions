# Write your MySQL query statement below
select e.employee_id from employees e  left join salaries s on e.employee_id=s.employee_id where s.salary is null
union 
select s.employee_id from salaries s  left join employees e on e.employee_id=s.employee_id where e.name is null
order by employee_id;
