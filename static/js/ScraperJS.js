/**
 * Created by slawomir on 24/11/16.
 */
$.get("menu_admin.html", function(data){
    $("#menu-placeholder").replaceWith(data);
});