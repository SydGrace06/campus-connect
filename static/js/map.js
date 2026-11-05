"use strict";
/// <reference types="leaflet" />
/// <reference path="./filters.ts" />
// Grove City College location directory
// Events will be loaded from the Flask API
let events = [];
// const campusLocations = {
//     "breen-student-union": {
//         name: "Breen Student Union (STU)",
//         latitude: 41.154852,
//         longitude: -80.077983
//     },
//     "buhl-library": {
//         "name": "Henry Buhl Library",
//         "latitude": 41.154125,
//         "longitude": -80.079378
//     },
//     "map-north": {
//         "name": "MAP North Hall",
//         "latitude": 41.157150,
//         "longitude": -80.079335
//     },
//     "map-south": {
//         "name": "MAP South Hall",
//         "latitude": 41.156387,
//         "longitude": -80.079882
//     },
//     "hicks-hall": {
//         "name": "Hicks Hall",
//         "latitude": 41.153358,
//         "longitude": -80.078439
//     },
//     "ketler-hall": {
//         "name": "Ketler Hall",
//         "latitude": 41.155454,
//         "longitude": -80.080569
//     }
// };
// // Dummy events point to a location ID rather than storing coordinates
// const dummyEvents: CampusEvent[] = [
//     {
//         title: "Coding Club Meetup",
//         category: "Academic/Professional",
//         date: "2026-11-02",
//         time: "6:00 PM",
//         locationId: "breen-student-union"
//     },
//     {
//         title: "Study Group",
//         category: "Academic/Professional",
//         date: "2026-11-03",
//         time: "4:00 PM",
//         locationId: "buhl-library"
//     },
//     {
//         title: "Residence Hall Game Night",
//         category: "Social",
//         date: "2026-11-04",
//         time: "7:00 PM",
//         locationId: "map-north"
//     },
//     {
//         title: "Campus Ministry Fair",
//         category: "Ministry",
//         date: "2026-11-05",
//         time: "5:30 PM",
//         locationId: "hicks-hall"
//     },
//     {
//         title: "Student Club Planning",
//         category: "Regular",
//         date: "2026-11-06",
//         time: "6:30 PM",
//         locationId: "ketler-hall"
//     },
//     {
//         title: "Art Club Social",
//         category: "Arts",
//         date: "2026-11-14",
//         time: "2:00 PM",
//         locationId: "map-south"
//     },
//     {
//         title: "Phi Sigma Chi Popcorn Party",
//         category: "Social",
//         date: "2026-10-31",
//         time: "6:00 PM",
//         locationId: "map-south"
//     },
//     {
//         title: "All Campus Worship",
//         category: "Social",
//         date: "2026-11-01",
//         time: "9:00 AM",
//         locationId: "breen-student-union"
//     }
// ];
const mapElement = document.getElementById("map");
if (mapElement) {
    // Center the map around Grove City College
    const map = L.map(mapElement).setView([41.155353, -80.079024], 17);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">' +
            'OpenStreetMap</a> contributors'
    }).addTo(map);
    const markerLayer = L.layerGroup().addTo(map);
    function updateMapMarkers() {
        const searchInput = document.getElementById("search");
        const categoryInput = document.getElementById("category");
        const dateInput = document.getElementById("date-range");
        // if (!searchInput || !categoryInput || !dateInput) {
        //     console.error("One or more filter controls are missing.");
        //     return;
        // }
        // Filter events using the current search and dropdown values
        const filteredEvents = filterEvents(events, searchInput.value, categoryInput.value, dateInput.value);
        // Remove the old markers
        markerLayer.clearLayers();
        // Add markers for the filtered events
        filteredEvents.forEach((event) => {
            L.marker([
                event.location.latitude,
                event.location.longitude
            ])
                .addTo(markerLayer)
                .bindPopup(`<strong>${event.title}</strong><br>` +
                `Category: ${event.category}<br>` +
                `Date: ${event.date}<br>` +
                `Time: ${event.time}<br>` +
                `Location: ${event.location.name}`);
        });
    }
    async function loadEvents() {
        try {
            const response = await fetch("/api/events");
            if (!response.ok) {
                throw new Error("Failed to load events");
            }
            events = await response.json();
            updateMapMarkers();
        }
        catch (error) {
            console.error("Error loading events:", error);
        }
    }
    // Update markers when the user changes a filter
    document.getElementById("search")?.addEventListener("input", updateMapMarkers);
    document.getElementById("category")?.addEventListener("change", updateMapMarkers);
    document.getElementById("date-range")?.addEventListener("change", updateMapMarkers);
    document.getElementById("clear-filters")?.addEventListener("click", () => {
        const searchInput = document.getElementById("search");
        const categoryInput = document.getElementById("category");
        const dateInput = document.getElementById("date-range");
        searchInput.value = "";
        categoryInput.value = "";
        dateInput.value = "all";
        updateMapMarkers();
    });
    // Load events from Flask
    loadEvents();
}
