select forename, surname, plannerNo, count(walk.walkerID) as total paricipants 
from planner, route, walk
where route.plannerNo = planner.plannerNo and route.routeID = walk.routeID
group by planner.forname, planner.surname, planne.plannerNo
order by total paricipants (desc);

