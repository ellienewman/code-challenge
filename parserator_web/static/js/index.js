/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

"use strict"

//parse address using views.py
function pyParse (addr) {
  $.ajax({
    type: "GET",
    url: 'api/parse/',
    dataType: "json",
    data: { request: addr },
    statusCode: {
      400: function (response) {
        $("#table-data").empty()
        $("#parse-type").empty()
        $("#parse-type").append(response.responseJSON.detail)
      },          
    }, 
    success: function callback (response) {
      var parsedData = response
      var type = parsedData['address_type']
      //clear table before adding new data
      $("#table-data").empty()
      $("#parse-type").empty()
      $("#parse-type").append(type)
      $.each(parsedData['address_components'], function (tag, component) {
        var row = $('<tr>').append($('<td>').text(component)).append($('<td>').text(tag))
        $("#table-data").append(row)
      })
    }
  })
}

//get user input
function getAddr () {
  var input = document.getElementById("address").value
  pyParse(input)
}

//when submit button clicked, parse address
document.getElementById("submit").onclick = function () {getAddr()}
