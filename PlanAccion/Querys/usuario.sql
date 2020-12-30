select user.id as user_id, concat(user.firstname," ",user.lastname) as full_name, user.username as RUT
from lablab.user as user where user.deletedAt is null;