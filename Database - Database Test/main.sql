DESCRIBE ALL TABLES;

select episodeTitle, showName, maxViewers, episodeDate 
from Episode, Show
where Episode.showID = Show.showID
group by episodeID;

select showName as "Show", episodeTitle as "Episode"
from Episode, show
where Episode.showID = Show.showID;

select * 
from show;

update Timeslot
set startTime = "19:30"
where showID = 2;

select*
from Timeslot;

select showName, count(ratingValue) as "Total Ratings"
from Show, ViewerRating, Episode
where ViewerRating.episodeID = Episode.episodeID 
and Episode.ShowID = Show.ShowID 
group by show.showID
order by count(ratingValue) desc;
