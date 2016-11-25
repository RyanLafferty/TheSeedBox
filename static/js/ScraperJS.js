/**
 * Created by slawomir on 24/11/16.
 */
$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});

//--------------------------------------------------------------------------------------
// {
//   "num_results": 1,
//   "objects": [
//     {
//       "dayofweek": 2,
//       "id": 1,
//       "metro_enabled": 1,
//       "nofrills_enabled": 1,
//       "time": "18:00",
//       "user_id": 1
//     }
//   ],
//   "page": 1,
//   "total_pages": 1
// }


// change settings
// FYI the day of week enum is: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] have monday be 0, etc
function createJsonChangeSettings(data) {

    for (var i = 0; i < data["num_results"]; i++ ) {
        for ( var key in data.objects[i]) {
            console.log(key);
            if ( key == "dayofweek" ) {
                console.log("dropdown");
                if ( data["objects"][i][key] == 0 ) {
                    $('#day').val( 'Mon' );
                } else if ( data["objects"][i][key] == 1 ) {
                    $('#day').val( 'Tues' );
                } else if ( data["objects"][i][key] == 2 ) {
                    $('#day').val( 'Wed' );
                } else if ( data["objects"][i][key] == 3 ) {
                    $('#day').val( 'Thu' );
                } else if ( data["objects"][i][key] == 4 ) {
                    $('#day').val( 'Fri' );
                } else if ( data["objects"][i][key] == 5 ) {
                    $('#day').val( 'Sat' );
                } else if ( data["objects"][i][key] == 6 ) {
                    $('#day').val( 'Sun' );
                }
            }
            }

            // newCell.innerHTML = data["objects"][i][key];

    }

}





// populate the current settings
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
});