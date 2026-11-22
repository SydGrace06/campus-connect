"use strict";
/// <reference types="leaflet" />
/// <reference path="./filters.ts" />
// Grove City College location directory
// Events will be loaded from the Flask API
let events = [];
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
    function updateEventTable(filteredEvents) {
        const tableBody = document.getElementById("event-table-body");
        if (!tableBody) {
            return;
        }
        // Remove the old table rows
        tableBody.innerHTML = "";
        // Display a message if no events match the filters
        if (filteredEvents.length === 0) {
            const row = document.createElement("tr");
            const cell = document.createElement("td");
            cell.colSpan = 6;
            cell.className = "text-center";
            cell.textContent = "No events found.";
            row.appendChild(cell);
            tableBody.appendChild(row);
            return;
        }
        // Create a table row for each filtered event
        filteredEvents.forEach((event) => {
            const row = document.createElement("tr");
            const values = [
                event.title,
                event.category,
                event.date,
                event.time,
                event.location.name,
                event.club ?? "—"
            ];
            values.forEach((value) => {
                const cell = document.createElement("td");
                cell.textContent = value;
                row.appendChild(cell);
            });
            // Create the Actions column
            const actionsCell = document.createElement("td");
            // Favorite club button
            const favoriteButton = document.createElement("button");
            favoriteButton.type = "button";
            favoriteButton.textContent = "☆ Favorite Club";
            favoriteButton.className = "btn btn-outline-primary btn-sm";
            // Disable favorite if the event has no club
            if (!event.club) {
                favoriteButton.disabled = true;
                favoriteButton.title = "This event has no associated club";
            }
            // RSVP button
            const rsvpButton = document.createElement("button");
            rsvpButton.type = "button";
            rsvpButton.textContent = "RSVP";
            rsvpButton.className = "btn btn-outline-success btn-sm";
            actionsCell.appendChild(favoriteButton);
            actionsCell.appendChild(document.createTextNode(" "));
            actionsCell.appendChild(rsvpButton);
            row.appendChild(actionsCell);
            tableBody.appendChild(row);
        });
    }
    function updateMapMarkers() {
        const searchInput = document.getElementById("search");
        const categoryInput = document.getElementById("category");
        const dateInput = document.getElementById("date-range");
        // Filter events using the current search and dropdown values
        const filteredEvents = filterEvents(events, searchInput.value, categoryInput.value, dateInput.value);
        updateEventTable(filteredEvents);
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
