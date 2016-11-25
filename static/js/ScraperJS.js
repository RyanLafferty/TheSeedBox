/**
 * Created by slawomir on 24/11/16.
 */
$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});

//--------------------------------------------------------------------------------------
var id = 0;

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
    var  storeNameList = [];
    var storeString = " ";
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
                $('#timeField').val(data["objects"][i][key]);
            } else if ( key == "metro_enabled" ) {
                if ( data["objects"][i][key] == 1 ) {
                    storeNameList.push( "metro" );
                }
            } else if ( key == "nofrills_enabled" )  {
                if ( data["objects"][i][key] == 1 ) {
                    storeNameList.push( "nofrills" );
                }
            } else if ( key == "id" ) {
                id = data["objects"][i][key];
            }
        }

        // add retialers to current savings
        for ( var j = 0; j < storeNameList.length; j++ ) {
            storeString += storeNameList[j];
            if ( j <  ( storeNameList.length - 1 ) ) {
                storeString += ", ";
            }
        }
        $('#stores').val( storeString );
    }

}

function dayToIntDropdown() {
    if ( $('#DayDropdown').val() == "Monday") {
        return 0;
    } else if ( $('#DayDropdown').val() == "Tuesday") {
        return 1;
    } else if ( $('#DayDropdown').val() == "Wednesday") {
        return 2;
    } else if ( $('#DayDropdown').val() == "Thursday") {
        return 3;
    } else if ( $('#DayDropdown').val() == "Friday") {
        return 4;
    } else if ( $('#DayDropdown').val() == "Saturday") {
        return 5;
    } else if ( $('#DayDropdown').val() == "Sunday") {
        return 6;
    } else {
        return 11;
    }
}

function isCheckedNoFrills() {
    if ( $('#NoFrills').is(":checked") ) {
        return 1;
    } else {
        return 0;
    }
}

function isCheckedMetro() {
    if ( $('#Metro').is(":checked") ) {
        return 1;
    } else {
        return 0;
    }
}

function getTimeInput() {
    var t = $("#time").val();

    return text(t);
}

function changeScrapaerSettings() {

    var settings = {
        "dayofweek": dayToIntDropdown(),
        "metro_enabled": isCheckedMetro(),
        "nofrills_enabled": isCheckedNoFrills(),
        "time": "18:00",
        "user_id": 0
    }

    console.log( dayToIntDropdown());
    console.log( isCheckedMetro());
    console.log( isCheckedNoFrills());
    console.log( getTimeInput());
    console.log( 0);
    return settings;
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

    $('#changeSettingsButton').click(function(){
    $.ajax({
        type: 'PUT',
        contentType:"application/json",
        url: '/api/ScraperSettings/' + id,
        data: JSON.stringify(changeScrapaerSettings()),  // data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            alert("Settings Updated");
        }
    });
});
});