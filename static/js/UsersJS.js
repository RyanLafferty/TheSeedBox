/**
 * Created by slawomir on 25/11/16.
 */
$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});

var rownum = 0;
var headerAlreadyExists = false;
function checkAll()
{
    var newValue = document.getElementById('master_cb').checked;
    var i;

    for (i = 0; i < rownum; i++)
    {
      document.getElementById('user' + i).checked = newValue;
    }
}
function fillTable(data) {
    rownum = 0;
    var tableData = data.objects;

    var tableElement = document.getElementById("table-header");

    var newRow = document.createElement('tr');

    if ( headerAlreadyExists == false ) {
        //Create Header
        var newCell = document.createElement('th');
        newCell.width = '10px';
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = 'master_cb';
        //checkbox.onchange = checkAll;
        newCell.appendChild(checkbox);
        newRow.appendChild(newCell);

        for (var title in tableData[0]) {
            newCell = document.createElement('th');
            var info = document.createTextNode(title);
            newCell.appendChild(info);
            newRow.appendChild(newCell);
        }
        tableElement.appendChild(newRow);
        headerAlreadyExists = true;
    }
    //Create Body
    tableElement = document.getElementById('table-body');
    for (var nextRow in tableData) {
        newRow = document.createElement('tr');
        newRow.id = 'user' + tableData[nextRow]["id"];

        newCell = document.createElement('td');
        newCell.width = '10px';
        checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        //checkbox.id = 'user' + rownum;

        checkbox.id = tableData[nextRow]["id"]; // ised in delete, very important line

        rownum += 1;
        newCell.appendChild(checkbox);
        newRow.appendChild(newCell);

        for (var key in tableData[nextRow]) {
            var value = tableData[nextRow][key];

            newCell = document.createElement('td');
            newCell.id = key;
            var info = document.createTextNode(value);
            newCell.appendChild(info);
            newRow.appendChild(newCell);
        }
        tableElement.appendChild(newRow);
    }
}

function deleteUser(id){
    $('table#usersTable tr#user' + id).remove();
    $.ajax({
        type: 'DELETE',
        url: '/api/Users/' + id,
        dataType: 'json',
        success: function (data) {
            console.log("Deleted user" + id);
        }
    });

}

function deleteSelectedUser(data) {
    for (var i = 0; i < data["num_results"]; i++ ) {
        for ( var key in data.objects[i]) {
            if ( key == "id" ) {
                if ( $('#' + data["objects"][i][key]).is(":checked") ) {
                    deleteUser(data["objects"][i][key]);
                } else {
                 }// else skip
            }
        }

    }
}

function deleteSelectedUserGetTTable() {
    $.ajax({
        type: 'GET',
        url: '/api/Users',
        dataType: 'json',
        success: function (data) {
            deleteSelectedUser(data);
            alert( "Selected Users Deleted" );
        }
    });
}

function sendSearch() {
    var request = {
        "name": "email",
        "val": document.getElementById('user-search').value,
        "op": "like"
    }
    return request;
}

$( document ).ready(function() {

    $.ajax({
        type: 'GET',
        url: '/api/Users',
        dataType: 'json',
        success: function (data) {
            fillTable(data);
        }
    });


    $('#user-search').keypress(function(e){
        console.log( "begin" );
		if (e.keyCode == 13){
            e.preventDefault();
			$.ajax({
				type: 'GET',
                contentType:"application/json",
				url: '/api/Users',
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

    $('#deleteUserButton').click(function(){
        deleteSelectedUserGetTTable();
    });
})

