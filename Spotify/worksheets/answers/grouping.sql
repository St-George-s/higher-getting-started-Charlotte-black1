SELECT COUNT(*)
FROM Tracks;

SELECT genre_id, COUNT(*)
FROM Tracks 
GROUP BY genre_id;

SELECT genre_id, AVG(duration_ms)
FROM Tracks 
GROUP BY genre_id;

select count(track_id)
from tracks;

select album_id, count(*)
from tracks 
group by genre_id;

select genre_id, max(duration_ms)
from tracks 
group by genre_id;

select album_id, sum(duration_ms) as total_duration
from tracks
group by album_id;


with sum(duration_ms) as total_duration
select album,id max(total_duration) 
from tracks;

(not right will fix later)






