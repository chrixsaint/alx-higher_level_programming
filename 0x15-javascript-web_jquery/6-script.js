// Wait for the DOM to be fully loaded before executing the script
$(document).ready(function() {
  // Make an AJAX GET request to the API URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Extract the character name from the response
    var characterName = data.name;

    // Display the character name in the div with ID 'character'
    $('#character').text(characterName);
  });
});
