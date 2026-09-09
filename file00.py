select id, count(*)
from emp
group by id
having count(*) > 1
sudha updated