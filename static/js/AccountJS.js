/**
 * Created by slawomir on 24/11/16.
 */
// var settings = {
//                     "admin": true,
//                     "fname": $('#fname').val(),
//                     "lname": $('#lname').val(),
//                     "password": $('#password').val(),
//                     "email": $('#email').val(),
//                     "logintime": null,
//                     "password": null
//                 }

var settings = {
  "admin": true,
  "email": "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT.com",
  "fname": "robbbb",
  "lname": "ssstttttttttsss",
  "logintime": null,
  "password": "1234"
}


$( document ).ready(function() {
    console.log(settings);
    $.ajax({
        type: 'GET',
        url: '/api/Users',
        // data: x,  data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            populateInputBoxes(getData);
        }
    });
    console.log(settings);
    $('#SaveButton').click(function(){
        $.ajax({
            type: 'PUT',
            contentType:"application/json",
            url: '/api/Users/1',
            data: JSON.stringify(settings),  // data passed to db
            dataType: 'json',
            success: function (getData) { // y is waht the get returns
                alert("Profile Updated");
                console.log("putsuccess");
            }
        });
        console.log(settings);
        console.log("put");
    });
});

function populateInputBoxes(data) {

    //for (var i = 0; i < data["num_results"]; i++ ) {
        // how to get value for key id data["objects"][i]["id"];

        //for ( var key in data.objects[i]) {
        for ( var key in data.objects[1]) {
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

