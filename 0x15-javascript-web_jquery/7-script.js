// Wait for the DOM to be fully loaded before executing the script
$(document).ready(function() {
  // Make an AJAX GET request to the API URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(data) {
      // Extract the character name from the response
      var characterName = data.name;

      // Display the character name in the div with ID 'character'
      $('#character').text(characterName);
    },
    error: function() {
      // Handle any error that may occur during the request
      $('#character').text('Error: Unable to fetch character name');
    }
  });
});
