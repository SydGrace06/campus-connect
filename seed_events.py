# dummy data
from datetime import date, time
from models import EventCategory

CAMPUS_EVENTS = [
    {
        #1
        "title": "ACM Game Night",
        "category": EventCategory.SOCIAL,
        "date": date(2027, 1, 12),
        "time": time(19, 0),
        "locationId": 29,
        "club_id": 6
    },
    {
        #2
        "title": "Editing Night",
        "category": EventCategory.ARTS,
        "date": date(2027, 1, 14),
        "time": time(20, 0),
        "locationId": 10,
        "club_id": 37
    },
    {
        #3
        "title": "Valentine's Dance",
        "category": EventCategory.SOCIAL,
        "date": date(2027, 2, 14),
        "time": time(18, 0),
        "locationId": 37,
        "club_id": 36
    },
    {
        #4
        "title": "Women's Self Defense Seminar",
        "category": EventCategory.SERVICE,
        "date": date(2027, 1, 26),
        "time": time(15, 0),
        "locationId": 9,
        "club_id": 95
    },
    {
        #5
        "title": "Cocoa Readings",
        "category": EventCategory.ARTS,
        "date": date(2027, 2, 10),
        "time": time(20, 0),
        "locationId": 3,
        "club_id": 34
    },
    {
        #6
        "title": "Valentine's Welding",
        "category": EventCategory.SOCIAL,
        "date": date(2027, 2, 13),
        "time": time(19, 0),
        "locationId": 11,
        "club_id": 24
    },
    {
        #7
        "title": "Field Hockey Game",
        "category": EventCategory.COMPETITION,
        "date": date(2027, 1, 28),
        "time": time(17, 0),
        "locationId": 31,
        "club_id": 99
    },
    {
        #8
        "title": "ACM Resume Review Night",
        "category": EventCategory.ACADEMIC_PROFESSIONAL,
        "date": date(2027, 1, 29),
        "time": time(19, 0),
        "locationId": 29,
        "club_id": 6
    },
    {
        #9
        "title": "Stargazing",
        "category": EventCategory.REGULAR,
        "date": date(2027, 2, 6),
        "time": time(22, 0),
        "locationId": 24,
        "club_id": 7
    },
    {
        #10
        "title": "Performance Poetry - Open Mic Night",
        "category": EventCategory.ARTS,
        "date": date(2027, 2, 2),
        "time": time(19, 0),
        "locationId": 12,
        "club_id": 34
    },
    {
        #11
        "title": "Pop-Up Cards Workshop",
        "category": EventCategory.ARTS,
        "date": date(2027, 2, 7),
        "time": time(10, 0),
        "locationId": 12,
        "club_id": 32
    },
    {
        #12
        "title": "Rugby Game",
        "category": EventCategory.COMPETITION,
        "date": date(2027, 2, 27),
        "time": time(19, 0),
        "locationId": 30,
        "club_id": 98
    },
    {
        #13
        "title": "Story Swap",
        "category": EventCategory.ARTS,
        "date": date(2027, 2, 26),
        "time": time(14, 0),
        "locationId": 10,
        "club_id": 37
    }
]