<<<<<<< HEAD
DESCRIBE ALL TABLES;

SELECT Event.eventName as "Event Name", Shop.name as "Shop Name" , Event.maxAttendees as "Max Attendees", Event.eventDate as "Event Date"
FROM Shop, Event
WHERE Event.shopID = Shop.shopID
GROUP BY Event.eventID
ORDER BY Event.eventID;

SELECT Shop.name as "Shop Name", Event.eventName as "Event Name"
FROM Shop, Event
WHERE Event.eventDate = "2024-12-25" 
AND Event.shopID = Shop.shopID;

UPDATE Openingtime
SET closeTime = "19:00"
WHERE date = "2024-12-24" 
AND shopID = (
    SELECT shopID 
    FROM shop 
    WHERE Shop.name = "Zara");

SELECT *
FROM Openingtime;

SELECT Shop.name as "Shop Name", count(Booking.bookingID) as "Total Bookings"
From Shop, Booking, Event
WHERE shop.shopID = Event.shopID 
AND Event.eventID = Booking.eventID
GROUP BY shop.name;
=======
>>>>>>> a8ee91c (Added Class Test)
