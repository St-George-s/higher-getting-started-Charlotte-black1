DESCRIBE ALL TABLES;
-- Question 2. c)
SELECT comicTitle, issue, publisherName, valuation
FROM Comic, Publisher
WHERE Comic.publisherID = Publisher.publisherID
AND valuation >= 300 + (
    SELECT (avg(valuation)) 
    FROM Comic)
GROUP BY comicTitle;


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
SELECT comicTitle, issue, publisherName, valuation*2 as [double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE seriesName = "The OK Seven"
AND CharacterInfo.characterName = "Starlordly"
AND comic.publisherID = Publisher.publisherID
AND Comic.SeriesID = Series.SeriesID
AND CharacterInfo.characterID = ComicCharacter.characterID
And ComicCharacter.comicID = Comic.comicID
GROUP BY Comic.comicTitle;

