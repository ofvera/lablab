select id, contact_id, name, interest, deletedAt, user_id, plan_stage_id, stage_order, not_company 
from lablab.networking_target_company where deletedAt is null;