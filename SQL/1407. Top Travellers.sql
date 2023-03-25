# Write your MySQL query statement below
SELECT Users.name AS name, SUM(Rides.distance) AS travelled_distance
FROM Users
LEFT JOIN Rides
ON Users.id = Rides.user_id
GROUP BY name
ORDER BY travelled_distance DESC, name ASC