/**
 * Created by slawomir on 24/11/16.
 */
var administrator = false;
var logintimee = null;
var oldPassword = "";
var emaill = "";
var fnamee = " ";
var lnamee = " ";
var userid = 1;

// var settings = {
//                     "admin": true,
//                     "fname": $('#fname').val(),
//                     "lname": $('#lname').val(),
//                     "password": $('#password').val(),
//                     "email": $('#email').val(),
//                     "logintime": null,
//                     "password": null
//                 }


// wroks
// var settings = {
//   "admin": true,
//   "email": "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT.com",
//   "fname": "robbbb",
//   "lname": "ssstttttttttsss",
//   "logintime": null,
//   "password": "1234"
// }

function callSettings() {
    if ( $('#NewPassword').val() != $('#ConfirmNewPassword').val() ) {
        var settings = {
            "admin": administrator,
            "email": $('#email').val(),
            "fname": $('#fname').val(),
            "lname": $('#lname').val(),
            "logintime": logintimee,
            "password": oldPassword
        }
    } else if ( oldPassword == $('#password').val() ) {
        var settings = {
            "admin": administrator,
            "email": $('#email').val(),
            "fname": $('#fname').val(),
            "lname": $('#lname').val(),
            "logintime": logintimee,
            "password": $('#NewPassword').val()
        }
    } else {
        var settings = {
            "admin": administrator,
            "email": emaill,
            "fname": fnamee,
            "lname": lnamee,
            "logintime": logintimee,
            "password": oldPassword
        }
    }
    return settings;
}

$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/api/Users',
        // data: x,  data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            populateInputBoxes(getData);
        }
    });

    $('#SaveButton').click(function(){
        callSettings();
        $.ajax({
            type: 'PUT',
            contentType:"application/json",
            url: '/api/Users/' + userid,
            data: JSON.stringify(callSettings()),  // data passed to db
            dataType: 'json',
            success: function (getData) { // y is waht the get returns
                alert("Profile Updated");
            }
        });
    });
});

function populateInputBoxes(data) {
    var k = 0;
    //for (var i = 0; i < data["num_results"]; i++ ) {
        // how to get value for key id data["objects"][i]["id"];

        //for ( var key in data.objects[i]) {
        for ( var key in data.objects[k]) {
            switch (key) {
                case "fname":
                    namee = data["objects"][k][key];
                    $('#fname').val(data["objects"][k][key]);
                    break;
                case "lname":
                    lnamee = data["objects"][k][key];
                    $('#lname').val(data["objects"][k][key]);
                    break;
                case "email":
                    emaill = data["objects"][k][key];
                    $('#email').val(data["objects"][k][key]);
                    break;
                case "admin":
                    administrator = data["objects"][k][key];
                    break;
                case "logintime":
                    logintimee = data["objects"][k][key];
                    break;
                case "password":
                    oldPassword = data["objects"][k][key];
                    break;
                case "id":
                    userid = data["objects"][k][key];
                    break;
            }
        }
    //}
}

