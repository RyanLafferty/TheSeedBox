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
    var totalSaved = 0;
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
                /*selector.addEventListener('change', updateTotal(selector), false);*/
                /*selector.onchange = function(){updateTotal(selector)};*/
            } else if (key == 'item') {
                newCell.innerHTML = data["objects"][i][key];
            } else {
                newCell.innerHTML = parseFloat(data["objects"][i][key]);
            }
            newRow.appendChild(newCell);
/*            if (key == 'price') {
                totalSaved += parseFloat(data["objects"][i][key]);
            }*/
        }
        tableBodyElement.appendChild(newRow);
    }
    document.getElementById('totalValue').value = '$' + totalSaved;

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

function updateTotal(table) {
    var totalSavings = 0;
    var totalValue = 0;
    /*document.getElementById('savingsTotal').value  = table.rows[0].cells[3].innerHTML;
    console.log(table.rows[0].cells[3].value);*/
    for (var i = 0; i < table.rows.length; i++) {
        totalSavings = totalSavings + parseInt(table.rows[i].cells[3].innerHTML);
        totalValue = totalValue + parseInt(table.rows[i].cells[4].innerHTML);
    }
    console.log(totalSavings);
    document.getElementById('savingsTotal').value = '$' + totalSavings;
    document.getElementById('totalValue').value = '$' + totalValue;
    
    /*var currentValue = element.options[element.selectedIndex].value;
    console.log(currentValue); */


    /*var oldValue = +(temp.value) || 0;
    temp.value = parseInt(temp.value,10);
    temp.value = oldValue;
    var value = parseInt(1);
    temp.value += value;*/


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


function sendSearch() {
    var request = {
        "name": "item",
        "val": "apple",
        "op": "like"
    }
    return request;
}


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
        console.log( "begin" );
		if (e.keyCode == 13){
            event.preventDefault();
			$.ajax({
				type: 'GET',
                contentType:"application/json",
				url: '/api/GFB',
                data: JSON.stringify(sendSearch()),
				dataType: 'json',

				success: function(data){
                    console.log("success");
					console.log(data)
				},
				error: function(data){
                    console.log("error");
					console.log(data)
				}
			});
		}
	});
    console.log("end");


});

