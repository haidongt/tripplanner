var directionDisplay;
      var directionsService = new google.maps.DirectionsService();
      var map;

      function add()
      {
          var i = 1;
          //my_div=document.getElementById("my_div");
	    my_div.innerHTML = my_div.innerHTML +"<br><input type='text'  name='mytext'+ i>"

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
               stopover:false});
              
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
            var route = response.routes[0];
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
