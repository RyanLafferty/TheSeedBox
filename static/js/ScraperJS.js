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
    console.log("begin");
    console.log(data);
    var  storeNameList = [];
    var storeString = "";
    for (var i = 0; i < data["num_results"]; i++ ) {
        for ( var key in data.objects[i]) {
            if ( key == "dayofweek" ) {
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
            } else if ( key == "time" ) {
                $('#timeField').val(data["objects"][k][key]);
            } else if ( key == "metro_enabled" ) {
                if ( data["objects"][i][key] == 1 ) {
                    storeNameList.push( "metro" );
                }
            } else if ( key == "nofrills_enabled" )  {
                if ( data["objects"][i][key] == 1 ) {
                    storeNameList.push( "nofrills" );
                }
            }
            console.log($('#day').val());
        }

        // add retialers to current savings
        for ( var j in storeNameList ) {
            storeString = storeString + j;
        }
        $('#storesList').val( storeString );

            // newCell.innerHTML = data["objects"][i][key];

    }

}





// populate the current settings
$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/api/ScraperSettings',
        // data: x,  data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            createJsonChangeSettings(getData);
        }
    });
});