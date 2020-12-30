select user.id, user.username, ab.type, ab.career, ab.institution 
from lablab.user as user join lablab.academic_background as ab
where user.id = ab.user_id and ab.type = "undergrad";