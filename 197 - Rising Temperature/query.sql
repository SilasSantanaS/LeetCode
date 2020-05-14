# Write your MySQL query statement below
SELECT l.Id AS 'Id' FROM Weather l JOIN  Weather r ON DATEDIFF(l.RecordDate, r.RecordDate) = 1 AND l.Temperature > r.Temperature

