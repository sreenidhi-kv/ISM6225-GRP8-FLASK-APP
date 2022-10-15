//  Empty Field
function empty_form() {
  if (
    document.getElementById("name").value == "" ||
    document.getElementById("email").value == "" ||
    document.getElementById("msg").value == ""
  ) {
    alert("There are missing fields.");
  } else {
    document.getElementById("form").submit();
    alert("Your inquiry has been received!");
  }
}
