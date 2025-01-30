document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('.sidebar-link');
    const mainContent = document.querySelector('.main-content');

    // Function to handle dynamic content fetching
    const fetchContent = (event, url) => {
        event.preventDefault(); // Prevent the default action of the link (page redirection)

        console.log('Attempting to fetch content from:', url); // Log the URL for debugging

        // Fetch the content without refreshing the page
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    console.error('Failed to fetch content:', response.status); // Log errors
                    return;
                }
                return response.text();
            })
            .then(html => {
                // Update the main content section with the fetched HTML
                mainContent.innerHTML = ''; // Clear current content
                mainContent.innerHTML = html; // Insert new content
            })
            .catch(error => {
                console.error('Error fetching content:', error); // Handle fetch errors
            });
    };

    // Add click event listener to each sidebar link
    links.forEach(link => {
        link.addEventListener('click', (event) => {
            const url = link.getAttribute('href'); // Get the URL from the link
            fetchContent(event, url); // Fetch and inject the content
        });
    });

    // Ensure sidebar remains visible and fixed
    const sidebar = document.querySelector('.sidebar');
    if (sidebar) {
        sidebar.style.display = 'block'; // Make sure the sidebar is always visible
    }
});
