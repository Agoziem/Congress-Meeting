function myFunction() {
    var x = document.getElementById("status").value;
    var studentcontainer = document.getElementById("stucontainer");
    if( x === 'Student'){
      
      studentcontainer.style.display='block';
    } else{
      studentcontainer.style.display='none';
    }
  }

  var Regform = document.getElementById('Reg_Form');

Regform.addEventListener('submit', function (e) {
  e.preventDefault()
  submitsubformdata()
})

function submitsubformdata() {
  var userdata = {
    'name': Regform.Name.value,
    'gender': Regform.gender.value,
    'Phonenumber': Regform.Phonenumber.value,
    'Emailaddress': Regform.Emailaddress.value,
    'address': Regform.address.value,
    'church': Regform.church.value,
    'zone': Regform.zone.value,
    'status': Regform.status.value,
    'School': Regform.School.value,
    'level': Regform.level.value,
  }

  var url = '/registration/Submitregistrationform/'
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
      var successAlert = document.querySelector('#subregform');
      successAlert.style.display = 'flex';
      Regform.reset();
      setTimeout(function() {
        successAlert.style.display = 'none';
      }, 3000);
      console.log('Data :', data)
    })
}