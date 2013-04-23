var directionDisplay;
      var directionsService = new google.maps.DirectionsService();
      var map;

var currentRoute;

      function add()
      {
          my_div=document.getElementById("my_div");
          if (my_div.childNodes.length < 9){
	      my_div.innerHTML = my_div.innerHTML +"<br><input type='text'  name='mytext'+ i>";
          }

       }

      function initialize() {
        directionsDisplay = new google.maps.DirectionsRenderer();
        var chicago = new google.maps.LatLng(41.850033, -87.6500523);
        var mapOptions = {
          zoom: 6,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          center: chicago
        }
        map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        directionsDisplay.setMap(map);
        updateSavedRoute();
      }
      function initializeMapOnly() {
        directionsDisplay = new google.maps.DirectionsRenderer();
        var chicago = new google.maps.LatLng(41.850033, -87.6500523);
        var mapOptions = {
          zoom: 6,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          center: chicago
        }
        map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        directionsDisplay.setMap(map);
      }

      function calcRoute(start, end, attractions)
 {
        var waypts = [];
        for (var i = 0; i < attractions.length; i++) {
               waypts.push({
               location:attractions[i],
               stopover:true});
        }

        var request = {
            origin: start,
            destination: end,
            waypoints: waypts,
            optimizeWaypoints: true,
            travelMode: google.maps.DirectionsTravelMode.DRIVING
        };
        directionsService.route(request, function(response, status) {
          if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
            document.getElementById('save_button').disabled = false;
            var route = response.routes[0];
            currentRoute = route;
            var summaryPanel = document.getElementById('directions_panel');
            summaryPanel.innerHTML = '';
            // For each route, display summary information.
            for (var i = 0; i < route.legs.length; i++) {
              var routeSegment = i + 1;
              summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment + '</b><br>';
              summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
              summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
              summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
            }
          }
        });
      }

      function saveRoute() {
updateSavedRoute();
          var route = '';
          for (var i = 0; i < currentRoute.legs.length; i++) {
              route += currentRoute.legs[i].start_address + "__";
              if(i == currentRoute.legs.length-1)
              {
                route += currentRoute.legs[i].end_address;
              }
          }
          $.getJSON(
          "/saveroute/" + route,
          function (data) {
$.each(data, function(key, val) {
  });
          }
          ); 
      }

      function showSavedRoute(id)
      {
          $.getJSON("/getrouteforid/"+id, function(data) {
 $.each(data, function(key, val) {

var start = val[0];
var attractions = [];
for(i = 1; i < val.length-1; i++)
{
attractions.push(val[i]);
}
var end = val[val.length-1];
calcRoute(start, end, attractions);


var currentDisplay = document.getElementById("current_display_route");

currentDisplay.innerHTML = "";

line = "<h4>" + start + " </h4> ";
line += "<ul>";
for(i = 0; i < attractions.length; i++)
{
line += "<li><p>" + attractions[i] + "</p> ";
}
line += "</ul>";
line += "<h4>" + end + " </h4> ";
currentDisplay.innerHTML += line;

          });
          });

      }

      function deleteRoute(id)
      {
          $.getJSON("/deleterouteforid/"+id, function(data) {
                        updateSavedRoute();
          });
      }
      function updateSavedRoute()
      {
          $.getJSON("/viewroutes", function(data) {


          var routeDisplay = document.getElementById("route_display_panel");
          routeDisplay.innerHTML = "";
          var count = 0;
          routeDisplay.innerHTML += "<div class=\"row\">"
          $.each(data, function(key, val) {
              count = count +1;
              var line = "";
              for(var i = 0; i < val.length; i++)
              {
                  if(i == 0){
                      line += "<h4>" + val[i] + " </h4><ul>";
                  }
                  else if(i == val.length-1){
                      line += "</ul><h4>" + val[i] + " </h4> ";
                  }
                  else{
                      line += "<li><p>" + val[i] + " </p> ";
                  }
              }

/*
              $.each(val, function(key1, val1) {
              line += "<h4>" + val1 + " </h4> ";
              });*/

              routeDisplay.innerHTML += "<div class=\"well span3\">\n <p>" + line +"</p>\n<p>           <a class=\"btn btn-small btn-info\" href=\"#\" onClick=\"showSavedRoute("+key+")\">View</a>         <a class=\"btn btn-small btn-danger\" onClick=\"deleteRoute("+key+")\">Delete</a></p>\n</div><!--/span-->\n";

       

              if(count%3 == 0){
                  routeDisplay.innerHTML += "</div> <div class=\"row\">";
              }
          });
          routeDisplay.innerHTML += "</div>"

          
           });
      }

