document.addEventListener("DOMContentLoaded", function() {
  const usernameField = document.querySelector('input[name="username"]');
  usernameField.addEventListener("click", function() {
    const username = usernameField.value;
    console.log(`Username clicked: ${username}`); // Log the username clicked
    if (username) {
      fetch(`/get_user_details?username=${username}`)
        .then(response => {
          console.log(`Response status: ${response.status}`); // Log the response status
          return response.json();
        })
        .then(data => {
          console.log(`Fetched data:`, data); // Log the fetched data
          document.querySelector('input[name="first_name"]').value = data.first_name;
          document.querySelector('input[name="last_name"]').value = data.last_name;
        })
        .catch(error => console.error('Error fetching user details:', error));
    }
  });
});
