SELECT artist_name 
FROM Artists 
WHERE artist_name LIKE 'T%';

SELECT album_name, release_year 
FROM Albums 
WHERE release_year >= 2015 
ORDER BY release_year DESC;

SELECT a.album_name AS Album, a.release_year Year 
FROM Albums a 
WHERE a.release_year > 2010 
ORDER BY a.release_year;

SELECT artist_name, LENGTH(artist_name) AS Name_Length 
FROM Artists 
WHERE artist_name LIKE '_a%';

select artist_name 
from Artists
where artist_name like '%o%';

select album_name
from Albums
order by length(album_name) desc;

select track_name as Tracks_with_A
from tracks
where tracks_with_A like '%a%';

select track_name
from tracks
where track_name like 's%e';

select album_name, (2024 - release_year) as age 
from albums
where release_year > 2010;

select artist_name, length(artist_name) as name_length
from artists 
where length(artist_name) > 5;
