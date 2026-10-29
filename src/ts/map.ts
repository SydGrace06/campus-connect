/// <reference types="leaflet" />

// Grove City College location directory.
// Coordinates are approximate demo positions; verify before final use.
const campusLocations = {
    "breen-student-union": {
        name: "Breen Student Union (STU)",
        latitude: 41.154852,
        longitude: -80.077983
    },
    "buhl-library": {
        "name": "Henry Buhl Library",
        "latitude": 41.154125,
        "longitude": -80.079378
    },
    "map-north": {
        "name": "MAP North Hall",
        "latitude": 41.157150,
        "longitude": -80.079335
    },
    "map-south": {
        "name": "MAP South Hall",
        "latitude": 41.156387,
        "longitude": -80.079882
    },
    "hicks-hall": {
        "name": "Hicks Hall",
        "latitude": 41.153358,
        "longitude": -80.078439
    },
    "ketler-hall": {
        "name": "Ketler Hall",
        "latitude": 41.155454,
        "longitude": -80.080569
    }
};

// Dummy events point to a location ID rather than storing coordinates.
const dummyEvents = [
    {
        title: "Coding Club Meetup",
        category: "Academic",
        date: "2026-11-02",
        time: "6:00 PM",
        locationId: "breen-student-union"
    },
    {
        title: "Study Group",
        category: "Academic",
        date: "2026-11-03",
        time: "4:00 PM",
        locationId: "buhl-library"
    },
    {
        title: "Residence Hall Game Night",
        category: "Social",
        date: "2026-11-04",
        time: "7:00 PM",
        locationId: "map-north"
    },
    {
        title: "Campus Music Meetup",
        category: "Music",
        date: "2026-11-05",
        time: "5:30 PM",
        locationId: "hicks-hall"
    },
    {
        title: "Student Club Planning",
        category: "Clubs",
        date: "2026-11-06",
        time: "6:30 PM",
        locationId: "ketler-hall"
    },
    {
        title: "Art Club Social",
        category: "Arts",
        date: "2026-11-07",
        time: "2:00 PM",
        locationId: "map-south"
    }
];

const mapElement = document.getElementById("map");

if (mapElement) {
    // Center the map around Grove City College.
    const map = L.map(mapElement).setView(
        [41.1568, -80.0859], 17
    );

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">' +
            'OpenStreetMap</a> contributors'
    }).addTo(map);

    dummyEvents.forEach((event) => {
        const location =
            campusLocations[
                event.locationId as keyof typeof campusLocations
            ];

        if (!location) {
            return;
        }

        L.marker([location.latitude, location.longitude])
            .addTo(map)
            .bindPopup(
                `<strong>${event.title}</strong><br>` +
                `Category: ${event.category}<br>` +
                `Date: ${event.date}<br>` +
                `Time: ${event.time}<br>` +
                `Location: ${location.name}`
            );
    });
}
