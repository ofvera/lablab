select user.id, user.username, contact.company, contact.name, plan.created_at, plan.updated_at,
plan_stage.name, plan_stage.terminal, plan_stage.position, plan_stage.tag, plan.deletedAt
from lablab.user as user  
join lablab.networking_plan as plan 
join lablab.networking_plan_stage as plan_stage
join lablab.networking_company_contact as company_contact
join lablab.networking_contact as contact
where plan.user_id = user.id and plan.stage_id = plan_stage.id and plan.company_contact_id = company_contact.id 
and company_contact.contact_id = contact.id and plan.deletedAt is null and user.deletedAt is null;