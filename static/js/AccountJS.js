/**
 * Created by slawomir on 24/11/16.
 */
var settings = {
                    "admin": true,
                    "fname": $('#fname').val(),
                    "lname": $('#lname').val(),
                    "password": $('#password').val(),
                    "email": $('#email').val(),
                    "logintime": null,
                    "password": null
                }

var id = "1";

$("#SaveButton").click(function(){
    console.log("put);
    $.ajax({
        type: 'PUT',
        url: '/api/Users' + id,
        data: settings,  // data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            alert("Profile Updated");
        }
    });
});

$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/api/Users',
        // data: x,  data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            populateInputBoxes(getData);
            console.log(getData);
        }
    });
});

function populateInputBoxes(data) {

    for (var i = 0; i < data["num_results"]; i++ ) {
        // how to get value for key id data["objects"][i]["id"];

        //for ( var key in data.objects[i]) {
        for ( var key in data.objects[0]) {
            if ( key == "fname" ) {
                $('#fname').val(data["objects"][i][key]);
            } else if ( key == "lname" ) {
                $('#lname').val(data["objects"][i][key]);
            } else if ( key == "email" ) {
                $('#email').val(data["objects"][i][key]);
            }
        }
    }
    console.log("get");
}