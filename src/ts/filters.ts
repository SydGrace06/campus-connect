type EventCategory =
    | "Academic"
    | "Social"
    | "Music"
    | "Clubs"
    | "Arts"
    | "Career"
    | "Sports";

type DateRange = "all" | "today" | "week";

interface CampusEvent {
    title: string;
    category: EventCategory;
    date: string;
    time: string;
    locationId: string;
}

function getLocalDateString(date: Date): string {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");

    return `${year}-${month}-${day}`;
}

function filterEvents(
    events: CampusEvent[],
    searchText: string,
    selectedCategory: string,
    selectedDateRange: DateRange
): CampusEvent[] {
    const today = new Date();

    const todayString = getLocalDateString(today);

    // Find Monday of the current week.
    const monday = new Date(today);
    const dayOfWeek = monday.getDay();
    const daysSinceMonday = (dayOfWeek + 6) % 7;
    monday.setDate(monday.getDate() - daysSinceMonday);

    // Find Sunday of the current week.
    const sunday = new Date(monday);
    sunday.setDate(monday.getDate() + 6);

    // Convert the week boundaries into local date strings.
    const mondayString = getLocalDateString(monday);
    const sundayString = getLocalDateString(sunday);

    return events.filter((event) => {
        const matchesSearch = event.title
            .toLowerCase()
            .includes(searchText.toLowerCase());

        const matchesCategory =
            selectedCategory === "" ||
            event.category === selectedCategory;

        // Convert the event's date string into a Date object.
        const eventDate = new Date(`${event.date}T00:00:00`);

        let matchesDate = true;

        if (selectedDateRange === "all") {
            matchesDate = eventDate >= new Date(`${todayString}T00:00:00`);
        } else if (selectedDateRange === "today") {
            matchesDate =
                getLocalDateString(eventDate) === todayString;
        } else if (selectedDateRange === "week") {
            const eventDateString = getLocalDateString(eventDate);

            matchesDate =
                eventDateString >= mondayString &&
                eventDateString <= sundayString;
        }

        return matchesSearch && matchesCategory && matchesDate;
    });
}
