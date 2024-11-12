DELETE FROM Tracks 
WHERE track_id = 5;

DELETE FROM Artists 
WHERE artist_id BETWEEN 20 AND 25;

INSERT INTO Genres (genre_id, genre_name) 
VALUES (21, 'Jazz');

INSERT INTO Tracks (track_id, track_name, artist_id, album_id, genre_id, duration_ms) 
VALUES (54, 'New Track', 4, 4, 1, 180000), 
       (55, 'Another Track', 5, 5, 2, 200000);

UPDATE Albums 
SET release_year = 2021 
WHERE album_id = 3;

UPDATE Artists 
SET artist_name = 'New Artist Name' 
WHERE artist_id IN (1, 2, 3);

select *
from Tracks;

select *
from Artists;

select *
from Genres;

select * 
from Albums;


delete from Albums 
where album_id < 10;

select * 
from Albums;

insert into Artists (artist_id, artist_name)
values (34, 'Noah Kahan');

select *
from Artists;

update Tracks 
set duration_ms = 200000
where track_id = 2;

select * 
from Tracks;

delete from tracks 
where duration_ms < 120000;

select * 
from Tracks;