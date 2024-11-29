SELECT * 
FROM Tracks 
WHERE album_id IN (
  SELECT album_id 
  FROM Albums 
  WHERE release_year > 2018
 );
 
 SELECT T.track_name, A.album_name 
 FROM Tracks T, Albums A
 WHERE T.album_id = A.album_id
   AND A.release_year > 2020;

SELECT T.track_name, A.album_name 
FROM Tracks T 
JOIN Albums A ON T.album_id = A.album_id 
WHERE A.release_year > 2020;

SELECT A.artist_name, COUNT(T.track_id) 
FROM Artists A 
JOIN Tracks T ON A.artist_id = T.artist_id 
GROUP BY A.artist_name;

SELECT * 
FROM Tracks 
WHERE album_id IN (
  SELECT album_id 
  FROM Albums 
  WHERE album_name LIKE '%t%');

SELECT AL.album_name, artist_name
FROM Albums AL
JOIN tracks t ON t.album_id = AL.album_id
JOIN artists AR ON t.Artist_id = AR.Artist_id
WHERE AL.release_year > 2015
group by Album_name;

SELECT A.artist_name, sum(T.track_id), min(T.track_id), avg(T.track_id)
FROM Artists A 
JOIN Tracks T ON A.artist_id = T.artist_id 
GROUP BY A.artist_name;

Select track_name as 'Songs by Lizzo'
from tracks T 
join artists a on T.artist_id = A.artist_id
where artist_name = 'Lizzo';

select track_name, genre_name
from tracks T 
join genres G on G.genre_id = T.genre_id;

select track_name, genre_name, album_name 
from tracks T 
join genres G on G.genre_id = T.genre_id 
join albums A on A.album_id = T.album_id 
where release_year >2017;