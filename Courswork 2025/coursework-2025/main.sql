DESCRIBE ALL TABLES;
-- Question 2. c)
SELECT (avg(valuation)) as average
FROM Comic;

SELECT comicTitle, issue, publisherName
FROM Comic, Publisher
WHERE Comic.publisherID = Publisher.publisherID
AND valuation >= 510.46;


-- Question 2. d) 
SELECT characterName, Sum(Valuation)
FROM ComicCharacter, CharacterInfo, Comic
Where ComicCharacter.characterID = CharacterInfo.characterID
AND ComicCharacter.comicID = Comic.comicID
AND characterName LIKE "%Duck%"
AND ComicCharacter.mainCharacter = 1 
GROUP BY characterName
ORDER BY Sum(valuation) DESC;


-- Question 2. e) 
SELECT comicTitle, issue, publisherName, valuation as [double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE series.seriesName = "The OK Seven"
AND characterName = "Starlordly"
AND comic.publisherID = Publisher.publisherID
AND Comic.SeriesID = Series.SeriesID
AND CharacterInfo.characterID = ComicCharacter.characterID
GROUP BY Comic.comicTitle;

