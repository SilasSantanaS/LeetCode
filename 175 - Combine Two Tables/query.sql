# Write your MySQL query statement below
SELECT l.FirstName, l.LastName, r.City, r.State FROM Person l left join Address r on l.PersonId = r.PersonId
