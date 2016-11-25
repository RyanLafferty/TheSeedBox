/**
 * Created by slawomir on 24/11/16.
 */
$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});

// // change settings
// function createJsonChangeSettings(data) {
//
// }
//
// // populate the current settings
// $( document ).ready(function() {
//     $.ajax({
//         type: 'GET',
//         url: '/api/Users',
//         // data: x,  data passed to db
//         dataType: 'json',
//         success: function (getData) { // y is waht the get returns
//             populateInputBoxes(getData);
//         }
//     });
// });