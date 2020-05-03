# Write your MySQL query statement below
SELECT l.Name AS 'Employee' FROM Employee l JOIN Employee r ON l. ManagerId = r. Id AND l.Salary > r.Salary
