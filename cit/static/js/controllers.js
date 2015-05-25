app.controller('LogoutCtrl', ['$scope', '$http', '$location', LogoutController]);
	function LogoutController($scope, $http, $location) {
			  $scope.logout = function(path){
				$http.get('/auth/logout/').
				success(function(data) {								
					window.location.reload();													
  				});
			};			
		}


app.controller('GalleryCtrl',['$scope','$location',function($scope, $location) {
	$scope.showContext = true;
	$scope.$watch(function() { 
					return $location.url(); 
			}, 
			function() {
				if($location.url() == '/' || $location.path() == '' ||$location.path() == '/_=_' || $location.path() == '/auth/logout/'  ) {
					 $scope.showContext = true;
						
     		}
				else
					 $scope.showContext = false;
     		});	
				

			var host = $location.host();
			var port = $location.port();
			var path = $location.path();
			console.log('hosttt', host, 'pooort', port, 'paath', typeof path);
}]);

//Get Names of organizations and from show them in profile form
app.controller('OrganizationCtrl', ['$scope', '$http', '$location', getOrganization]);
function getOrganization($scope, $http) {
				$http.get('/auth/organizations/').
				success(function(data) {
					$scope.ogranization = data
					console.log($scope.ogranization);
       			});
		}
		