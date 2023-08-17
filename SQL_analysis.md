# Analysing Data using SQL

#### Task 1. How many values are there in the given dataset.
<pre>
SELECT COUNT(*)
FROM patients
</pre>

#### Task 2. Count the number of appointments for each day in the given dataset.
<pre>
SELECT AppointmentDay, COUNT(*) AS Appointments
FROM patients
GROUP BY AppointmentDay
</pre>

#### Task 3. Calculate the average number of appointments(Set to nearest whole number) per day in the given dataset.
<pre>
WITH T1
AS (SELECT AppointmentDay, COUNT(*) AS Appointments
FROM patients
GROUP BY AppointmentDay)
SELECT ROUND(AVG(Appointments), 0)
FROM T1
</pre>

#### Task 4. Find the day with the highest number of appointments in the given dataset.
<pre>
SELECT AppointmentDay, COUNT(*) AS Appoitments
FROM patients
GROUP BY AppointmentDay
ORDER BY 2 DESC
LIMIT 1
</pre>

#### Task 5. Calculate the monthly average number of appointments in the given dataset.
<pre>
SELECT
  Date_Format(AppointmentDay, '%Y-%m') AS month,
  COUNT(*) AS count
FROM patients
GROUP BY month
</pre>

#### Task 6. Find the month with the highest number of appointments in the given dataset.
<pre>
SELECT
  Date_Format(AppointmentDay, '%Y-%m') AS month,
  COUNT(*) AS count
FROM patients
GROUP BY month
ORDER BY 2 DESC
LIMIT 1
</pre>

#### Task 7. Calculate the weekly average number of appointments in the given dataset.
<pre>
WITH WeeklyAppointments AS (
  SELECT EXTRACT(YEAR FROM AppointmentDay) AS Year,
         EXTRACT(WEEK FROM AppointmentDay) AS Week,
         COUNT(*) AS Appointments_Count
  FROM patients
  GROUP BY Year, Week
)
SELECT Year, Week, Round(AVG(Appointments_Count),0) AS Avg_Appointments
FROM WeeklyAppointments
GROUP BY Year, Week
ORDER BY Year, Week
</pre>

#### Task 8. Find the week with the highest number of appointments in the given dataset.
<pre>
WITH WeeklyAppointments AS (
  SELECT EXTRACT(YEAR FROM AppointmentDay) AS Year,
         EXTRACT(WEEK FROM AppointmentDay) AS Week,
         COUNT(*) AS Appointments_Count
  FROM patients
  GROUP BY Year, Week
)
SELECT Year, Week, Round(AVG(Appointments_Count),0) AS Avg_Appointments
FROM WeeklyAppointments
GROUP BY Year, Week
ORDER BY 3 DESC
LIMIT 1
</pre>

#### Task 9. What is the distribution of appointments based on gender in the dataset?
<pre>
SELECT Gender, COUNT(*)
FROM patients
GROUP BY Gender
</pre>

#### Task 10. Calculate the number of appointments per weekday in the given dataset. Order the appointment counts in descending.
<pre>
SELECT
  DAYNAME(AppointmentDay) AS day_name,
  COUNT(*)
FROM patients
GROUP BY day_name
</pre>

#### Task 11. Calculate the average time between scheduling and the appointment day in the given dataset. Set to nearest whole number
<pre>
SELECT
  ROUND (AVG (DATEDIFF (AppointmentDay, ScheduledDay)), 0)
FROM patients
</pre>
