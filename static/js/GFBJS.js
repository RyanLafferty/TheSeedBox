/**
 * Created by slawomir on 24/11/16.
 */
function createGFBTableHeader(data) {
    //var tableHeaders = ['Item', 'Price ($)', 'Quantity', 'Savings (%)', 'Total ($)', ];

    var tableHeaderElement = document.getElementById("table-header");
    var newRow = document.createElement('tr');
    if ( data["num_results"] != 0) {
        for (var key in data.objects[0]) {
            if ( key == "id" ) {
                continue;
            }
            var newCell = document.createElement('th');
            var info = document.createTextNode(key);
            newCell.appendChild(info);
            newRow.appendChild(newCell);
        }
    }
    tableHeaderElement.appendChild(newRow);
}

function addDataToGFB(data) {
    var tableBodyElement = document.getElementById('table-body');

    for (var i = 0; i < data["num_results"]; i++ ) {
        var newRow = document.createElement('tr');
        newRow.id = data["objects"][i]["id"];

        for ( var key in data.objects[i]) {
            if ( key == "id" ) {
                continue;
            }
            var newCell = document.createElement('td');
            newCell.id = key;

            if ( key == 'quantity' ) {
                var selector = document.createElement('select');
                for ( var k = 0; k <= 50; k++) {
                    var option = document.createElement('option');
                    option.innerHTML = k;
                    option.value = k;
                    selector.appendChild(option);
                }
                newCell.appendChild(selector);
            } else {
                newCell.innerHTML = data["objects"][i][key];
            }
            newRow.appendChild(newCell);
        }
        tableBodyElement.appendChild(newRow);
    }

    // // create empty rows in table
    // for ( var i = parseInt(data["num_results"]); i < 20; i++ ) {
    //     var newRow = document.createElement('tr');
    //
    //     for ( var j = 0; j < 5; j++) {
    //         var newCell = document.createElement('td');
    //         newCell.innerHTML = " ";
    //         newRow.appendChild(newCell);
    //     }
    //     tableBodyElement.appendChild(newRow);
    // }
}

$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});


//        var send = {
//          "num_results": 1,
//          "objects": [
//            {
//              "id": 1,
//              "item": apple,
//              "price": 1.01,
//              "quantity": 0,
//              "savings": 10,
//              "total": 0
//            }
//          ],
//          "page": 1,
//          "total_pages": 1
//        }

//            $.ajax({
//                type: 'POST',
//                url: '/api/GFB',
//                data: send, // data passed to db
//                dataType: 'json',
//                success: function (y) {
//                    console.log(y);
//                }
//            });



$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/api/GFB',
        // data: x,  data passed to db
        dataType: 'json',
        success: function (getData) { // y is waht the get returns
            createGFBTableHeader(getData);
            addDataToGFB(getData);
        }
    });

    $('#gfb-search').keypress(function(e){
		if (e.keyCode == 13){
			item = $('#gfb-search').val();
			
			newUrl = '/api/GFB'
			$.ajax({
				type: 'GET',
				url: '/api/GFB',
				dataType: 'json',
				data: {
					"val":item,
					"op":"LIKE"
				},
				success: function(data){
					console.log(data)
				},
				error: function(data){
					console.log(data)
				}
			});
		}
	});


});

