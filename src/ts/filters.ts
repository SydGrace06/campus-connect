interface CampusEvent {
    title: string;
    category: string;
    date: string;
    time: string;
    locationId: string;
}

function filterEvents(
    events: CampusEvent[],
    searchText: string,
    selectedCategory: string,
    selectedDate: string
): CampusEvent[] {
    return events.filter((event) => {
        const matchesSearch = event.title
            .toLowerCase()
            .includes(searchText.toLowerCase());

        const matchesCategory =
            selectedCategory === "" ||
            event.category === selectedCategory;

        const matchesDate =
            selectedDate === "" ||
            event.date === selectedDate;

        return matchesSearch && matchesCategory && matchesDate;
    });
}
