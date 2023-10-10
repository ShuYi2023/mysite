function syncToCWithScroll() {
    // Get the ToC div
    let toc = document.getElementById("ToC");

    // Get the ToC list items
    let tocItems = toc.querySelectorAll("li");

    // Get the headers (h2 and h3)
    let headers = document.querySelectorAll("h2, h3");

    // Create an array to store the header positions
    let headerPositions = [];

    // Get the positions of each header
    for (let i = 0; i < headers.length; i++) {
        let headerPosition = headers[i].offsetTop;
        headerPositions.push(headerPosition);
    }

    // Function to update the active ToC item based on scroll position
    function updateActiveToCItem() {
        // Get the current scroll position
        let currentPosition = window.pageYOffset;

        // Find the index of the header closest to the current scroll position
        let activeIndex = headerPositions.findIndex(
            position => position > currentPosition
        );

        // If no header is found, set the active index to the last item
        if (activeIndex === -1) {
            activeIndex = headers.length - 1;
        }

        // Remove the "active" class from all ToC items
        tocItems.forEach(item => item.classList.remove("active"));

        // Add the "active" class to the corresponding ToC item
        tocItems[activeIndex].classList.add("active");
    }

    // Call the updateActiveToCItem function on scroll
    window.addEventListener("scroll", updateActiveToCItem);
}

// Call the syncToCWithScroll function to enable synchronization
syncToCWithScroll();