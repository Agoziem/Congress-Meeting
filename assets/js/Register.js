let updateState = true;

// ---------------------------------------
// Function to update the UI based on the current state
// ---------------------------------------
function updateUI() {
  if (updateState) {
    document.getElementById("successdiv").style.display = "none";
    document.getElementById("updateBtn").style.display = "none";
    document.getElementById("newEntrybtn").style.display = "block";
    document.getElementById("searchcontainer").style.display = "block";
    document.getElementById("Reg_Form").style.display = "none";
  } else {
    document.getElementById("successdiv").style.display = "none";
    document.getElementById("updateBtn").style.display = "block";
    document.getElementById("newEntrybtn").style.display = "none";
    document.getElementById("searchResults").style.display = "none";
    document.getElementById("searchcontainer").style.display = "none";
    document.getElementById("Reg_Form").reset(); // Reset form fields
    document.getElementById("Reg_Form").style.display = "block"; // Show the form
  }
}

// Initial UI update on DOM load
document.addEventListener("DOMContentLoaded", updateUI);


// ---------------------------------------
// Function to handle Students details input
// ---------------------------------------
function myFunction() {
  var x = document.getElementById("status").value;
  var studentcontainer = document.getElementById("stucontainer");
  if (x === "Student") {
    studentcontainer.style.display = "block";
  } else {
    studentcontainer.style.display = "none";
  }
}

var Regform = document.getElementById("Reg_Form");
var successDIV = document.getElementById("successdiv");

Regform.addEventListener("submit", function (e) {
  e.preventDefault();
  submitsubformdata();
});

// ---------------------------------------
// Function to submit form data
// ---------------------------------------
function submitsubformdata() {
  var genderValue = document.querySelector('input[name="gender"]:checked').value;
  var userdata = {
    name: Regform.Name.value,
    gender: genderValue,
    Phonenumber: Regform.Phonenumber.value,
    Emailaddress: Regform.Emailaddress.value,
    address: Regform.address.value,
    church: Regform.church.value,
    zone: Regform.zone.value,
    status: Regform.status.value,
    School: Regform.School.value,
    level: Regform.level.value,
  };
  var url = "/registration/Submitregistrationform/";
  fetch(url, {
    method: "POST",
    headers: {
      "content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(userdata),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      Regform.reset();
      Regform.style.display = "none";
      successDIV.style.display = "block";
      document.getElementById("searchName").value = "";
    });
}

// ---------------------------------------
// Function to search by name
// ---------------------------------------
function searchByName() {
  const searchName = document.getElementById("searchName").value.trim();

  // Make AJAX request to Django view to fetch data
  fetch(`/registration/search/?name=${encodeURIComponent(searchName)}`)
    .then((response) => response.json())
    .then((data) => {
      const resultsList = document.getElementById("resultsList");
      resultsList.innerHTML = ""; // Clear previous results

      if (data.length > 0) {
        data.forEach((item) => {
          const li = document.createElement("li");
          li.textContent = item.name;
          li.addEventListener("click", () => showDetails(item.id));
          resultsList.appendChild(li);
        });
        document.getElementById("searchResults").style.display = "block";
      } else {
        alert("No results found.");
        document.getElementById("searchResults").style.display = "none";
      }
    })
    .catch((error) => {
      console.error("Error fetching search results:", error);
    });
}

// ---------------------------------------
// Function to show details in form
// ---------------------------------------
function showDetails(userId) {
  // Make AJAX request to fetch user details by ID
  fetch(`/registration/user-details/${userId}/`)
    .then((response) => response.json())
    .then((userdata) => {
      // Populate form fields with fetched data
      document.getElementById("name").value = userdata.name;
      const genderRadios = document.getElementsByName("gender");
      genderRadios.forEach((radio) => {
        radio.checked = radio.value === userdata.gender;
      });
      document.getElementById("Phone").value = userdata.phonenumber;
      document.getElementById("email").value = userdata.emailaddress;
      document.getElementById("address").value = userdata.address;
      document.getElementById("church").value = userdata.church;
      document.getElementById("zone").value = userdata.zone;
      document.getElementById("status").value = userdata.occupation;
      if (userdata.occupation === "Student") {
        document.getElementById("stucontainer").style.display = "block";
        document.getElementById("School").value = userdata.school;
        document.getElementById("level").value = userdata.level;
      } else {
        document.getElementById("stucontainer").style.display = "none";
      }
      // Show the form
      document.getElementById("Reg_Form").style.display = "block";
      document.getElementById("searchResults").style.display = "none";
      document.getElementById("searchcontainer").style.display = "none";
      document.getElementById("updateBtn").style.display = "block";
    })
    .catch((error) => {
      console.error("Error fetching user details:", error);
    });
}

// ---------------------------------------
// Function to clear form for new entry
// ---------------------------------------
function clearForm() {
  updateState = false;
  updateUI();
}

// ---------------------------------------
// Function to switch to update mode
// ---------------------------------------
function switchToUpdateMode() {
  updateState = true;
  updateUI();
}
