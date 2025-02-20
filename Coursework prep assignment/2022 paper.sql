-- 2. b)
select forename, surname, planner.plannerNo, count(walk.walkerNo) as total_participants 
from planner, route, walk 
where route.plannerNo = planner.PlannerNo 
and route.routeID = walk.routeID
group by planner.forename, planner.surname, planner.plannerNo
order by total_participants desc;

--2. c)
select walker.walkerNo, forename, surname, telNo
from walker, walk, route 
where walker.walkerNo = walk.walkerNo 
and route.routeID = walk.RouteID 
and route.routeID like "dev001"
group by walker.walkerNo;

--2. d)
select route.routeID, woodname, description  
from route
where footwear like "trail shoes" 
or footwear like "waterproof shoes"
or footwear like "walking shoes";

select route.routeID, woodname, description 
from route
where footwear like "% shoes";