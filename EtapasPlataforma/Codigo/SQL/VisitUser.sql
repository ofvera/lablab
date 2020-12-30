SELECT visit.user_id as user_id, 
visit.date as date, 
visit.route as route,
visit.url as url,
user.firstname as firstname,
user.lastname as lastname,
user.username as rut,
user.email as email
FROM lablab.visit as visit 
LEFT JOIN lablab.user as user ON user.id = visit.user_id
WHERE date >= '2020-01-01 00:00:00' and user_id IS NOT NULL
and (visit.route = 'frontend_job' or visit.route = 'frontend_job_search' or visit.route = 'frontend_job_show');