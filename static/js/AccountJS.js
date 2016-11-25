/**
 * Created by slawomir on 24/11/16.
 */


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

    //for (var i = 0; i < data["num_results"]; i++ ) {
        // how to get value for key id data["objects"][i]["id"];

        //for ( var key in data.objects[i]) {
        for ( var key in data.objects[1]) {
            console.log(key);
            if ( key == "fname" ) {
                $('#fname').val(data["objects"][1][key]);
            } else if ( key == "lname" ) {
                $('#lname').val(data["objects"][1][key]);
            } else if ( key == "email" ) {
                $('#email').val(data["objects"][1][key]);
            }
        }
    //}
    console.log("get");
}

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

// $("#SaveButton").click(function(){
//     $.ajax({
//         type: 'PUT',
//         url: '/api/Users' + id,
//         data: settings,  // data passed to db
//         dataType: 'json',
//         success: function (getData) { // y is waht the get returns
//             alert("Profile Updated");
//         }
//     });
//     console.log("put");
// });