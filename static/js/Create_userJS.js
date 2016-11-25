/**
 * Created by slawomir on 25/11/16.
 */
$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});

function createUser() {
    var email = document.getElementById('email');
    var password = document.getElementById('password');
    var confirmPass = document.getElementById('confirmPass');
    var isAdmin = (document.getElementById('user').checked ? false : true);
    var response = document.getElementById('response');

    if (email.value == "")
        response.innerHTML = "Please enter an email";
    if (email.value.search(/[a-z0-9-_.]+@[a-z0-9]+\.[a-z][a-z]+/i) != 0)
        response.innerHTML = "Email is not valid";
    else if (password.value == "")
        response.innerHTML = "Please enter a password";
    else if (password.value != confirmPass.value)
        response.innerHTML = "Passwords do not match";
    else {
        //Send data to API
        var settings = {
           "admin": isAdmin,
           "fname": null,
           "lname": null,
           "password": password.value,
           "email": email.value,
           "logintime": null
       };

       $.ajax({
           type: 'POST',
           contentType:"application/json",
           url: '/api/Users',
           data: JSON.stringify(settings),
           dataType: 'json',
           success: function (data) {
               alert("Profile Added");
           }
       });
    }
}
