//get data, make AJAX call API. */

function processForm(evt) {
  evt.preventDefault();

  $.ajax({
    method: "POST",
    url: "/api/get-lucky-num",
    contentType: "application/json",
    data: JSON.stringify({
      name: $("#name").val(),
      email: $("#email").val(),
      year: $("#year").val(),
      color: $("#color").val(),
    }),
    success: handleResponse
  });
}

// handleResponse: deal with response from lucky-num API. */

function handleResponse(resp) {
  if ("errors" in resp) {
    
    // API errors: put each error in representaive feild

    for (let fld in resp.errors) {
      $(`#${fld}-err`).text(resp.errors[fld]);
    }
  }

  else {
    // success from API provides result message

    let {num, year} = resp;
    let msg = `Your lucky number is ${num.num} (${num.fact}).
    Your birth year (${year.year}) fact is ${year.fact}.`;

    $("#lucky-results").text(msg);
  }
}


$("#lucky-form").on("submit", processForm);
