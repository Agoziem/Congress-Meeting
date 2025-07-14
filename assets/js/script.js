function truncateText(selector, maxLength) {
  const elements = document.querySelectorAll(selector);

  elements.forEach((element) => {
    let fullText = element.textContent;
    if (fullText.length > maxLength) {
      let truncatedText = fullText.substring(0, maxLength) + "...";
      element.setAttribute("data-full-text", fullText);
      element.textContent = truncatedText;
    }
  });
}

function setupShowMoreButtons(maxlength) {
  const buttons = document.querySelectorAll(".show-more");

  buttons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const container = event.target.closest(".event-description-container");
      const description = container.querySelector(".event-description");

      if (description.textContent.endsWith("...")) {
        description.textContent = description.getAttribute("data-full-text");
        event.target.textContent = "Show Less";
      } else {
        const fullText = description.getAttribute("data-full-text");
        const maxLength = maxlength || 500;
        description.textContent = fullText.substring(0, maxLength) + "...";
        event.target.textContent = "Show More";
      }
    });
  });
}

// Initialize truncation and button functionality
truncateText(".event-description", 900); // Adjust 50 to your desired length
setupShowMoreButtons(900);

var countDownDate = new Date("Aug 1, 2025 15:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function () {
  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("days").innerHTML = days + "d ";
  document.getElementById("hours").innerHTML = hours + "h ";
  document.getElementById("minutes").innerHTML = minutes + "m ";
  document.getElementById("seconds").innerHTML = seconds + "s ";

  // If the count down is finished, write some text

  if (distance <= 0) {
    clearInterval(x);
    if (seconds === 0) {
      document.getElementById(
        "TmerDisplay"
      ).innerHTML = `<span class="text-success fw-bold mx-2" > The Congress is Live Now </span>`;
    } else {
      document.getElementById(
        "TmerDisplay"
      ).innerHTML = `<span class="text-success fw-bold mx-2" > The Congress is Live Now </span>`;
    }
  }
}, 1000);

// var myModal = document.getElementById('myModal')
// var myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', function () {
//   myInput.focus()
// })

var subform = document.getElementById("sub_form");

subform.addEventListener("submit", function (e) {
  e.preventDefault();
  submitsubformdata();
});

function submitsubformdata() {
  var userdata = {
    email: subform.email.value,
  };

  var url = "/subscription/";
  fetch(url, {
    method: "POST",
    headers: {
      "content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ userdata: userdata }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      var successAlert = document.querySelector("#sub_form_alert_success");
      successAlert.style.display = "flex";
      subform.reset();
      setTimeout(function () {
        successAlert.style.display = "none";
      }, 3000);
      console.log("Data :", data);
    });
}
