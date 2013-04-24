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
      }

      function calcRoute() {

        var start = document.getElementById('start').value;
        var end = document.getElementById('end').value;
        var waypts = [];
        var attractions = document.getElementById('my_div');

        for (var i = 0; i < my_div.childNodes.length; i++) {
           if(my_div.childNodes[i].tagName == "INPUT")
           {
               var textValue = my_div.childNodes[i].value;
               waypts.push({
               location:textValue,
               stopover:true});
              
           }
           
           /* waypts.push({
                location:checkboxArray[i].value,
                stopover:true});*/
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
            getRecommendation();
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

      function getRecommendation()
      {

          var attractions = '';
          for (var i = 1; i < currentRoute.legs.length; i++) {
              attractions += currentRoute.legs[i].start_address;
              if (i != currentRoute.legs.length - 1)
              {
                  attractions += "__";
              }
          }
          $.getJSON(
          "/recommendfor/" + attractions,
          function (data) {
$.each(data, function(key, val) {
        var tag = document.getElementById('recommendation');
tag.innerHTML = "You might also be interested in visiting " + val + ".";

});
         
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
          var save_button = document.getElementById("save_button");
save_button.className = "btn btn-info";
save_button.disabled = true;
          }
          ); 
      }

      function updateSavedRoute()
      {
          $.getJSON("/viewroutes", function(data) {


          var routeDisplay = document.getElementById("route_display_panel");
          routeDisplay.innerHTML = "";
          var count = 0;
          routeDisplay.innerHTML += "<div class=\"row-fluid\">"
          $.each(data, function(key, val) {
              count = count +1;
              var line = "";
              $.each(val, function(key1, val1) {
              line += key1 + ': ' + val1 + " </br> ";
              });

              routeDisplay.innerHTML += "<div class=\"span3\">\n<h2> Route"+count+"</h2>\n <p>" + line +"</p>\n<p><a class=\"btn\" href=\"#\">View details &raquo;</a></p>\n</div><!--/span-->\n";
              if(count%3 == 0){
                  routeDisplay.innerHTML += "</div> <div class=\"row-fluid\">";
              }
          });
          routeDisplay.innerHTML += "</div>"

          
           });
      }

