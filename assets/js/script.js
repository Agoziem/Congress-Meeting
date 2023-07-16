function theFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

var countDownDate = new Date("Aug 4, 2023 15:00:00").getTime();

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
  document.getElementById("minutes").innerHTML = minutes + "m " ;
  document.getElementById("seconds").innerHTML = seconds + "s ";
  document.getElementById("day").innerHTML = days ;

  

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);





// var myModal = document.getElementById('myModal')
// var myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', function () {
//   myInput.focus()
// })

var subform = document.getElementById('sub_form');

subform.addEventListener('submit', function (e) {
  e.preventDefault()
  submitsubformdata()
})

function submitsubformdata() {
  var userdata = {
    'email': subform.email.value,
  }

  var url = '/subscription/'
  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ 'userdata': userdata })
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      var successAlert = document.querySelector('#sub_form_alert_success');
      successAlert.style.display = 'flex';
      subform.reset();
      setTimeout(function() {
        successAlert.style.display = 'none';
      }, 3000);
      console.log('Data :', data)
    })
}