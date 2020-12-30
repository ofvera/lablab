SELECT user.id as User_ID, CONCAT(user.firstname," ",user.lastname) as Nombre, user.username as RUT, program.name as Programa,
(SELECT job_manager_tab.title FROM lablab.job_manager_tab WHERE job_manager_tab.id = job_manager_item_history.job_manager_tab_id) as Etapa,
job_manager_item_history.created as Fecha_cambio, job_offer.title as Oferta, job_offer.company as Empresa, job_offer.source as Origen, job_offer.url as URL 
FROM lablab.job_manager_item as job_manager_item
JOIN lablab.user as user ON job_manager_item.user_id = user.id 
JOIN lablab.job_manager_item_history ON lablab.job_manager_item.id = job_manager_item_history.job_manager_item_id
JOIN lablab.job_offer ON lablab.job_manager_item.joboffer_id = job_offer.id
JOIN lablab.program ON program_id = program.id
WHERE (user.deletedAt is null) AND (user.enabled = 1) AND (job_manager_item_history.created >= '2020-01-01') and user.deletedAt is null;