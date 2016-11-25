/**
 * Created by slawomir on 24/11/16.
 */
var administrator = false;
var logintimee = null;
var oldPassword = " ";
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
    } else {
        var settings = {
            "admin": administrator,
            "email": $('#email').val(),
            "fname": $('#fname').val(),
            "lname": $('#lname').val(),
            "logintime": logintimee,
            "password": $('#NewPassword').val()
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
            url: '/api/Users/1',
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
            if ( key == "fname" ) {
                $('#fname').val(data["objects"][k][key]);
            } else if ( key == "lname" ) {
                $('#lname').val(data["objects"][k][key]);
            } else if ( key == "email" ) {
                $('#email').val(data["objects"][k][key]);
            } else if ( key == "admin" ) {
                administrator = data["objects"][k][key];
            } else if ( key == "logintime" ) {
                logintimee = data["objects"][k][key];
            } else if ( key == "password" ) {
                oldPassword = data["objects"][k][key];
            }
        }
    //}
}

