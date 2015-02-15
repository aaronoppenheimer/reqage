// Controller for a lex
//
// ao 2015-02-15

app.controller("lexCtrl", function($scope,$http) {
    $scope.id = 0;
    $scope.lex = '';
    
    $scope.change_lex = function(newlexid) {
        $scope.id = newlexid;
        $http.get("/reqage/api/lex/"+$scope.id)
        .success(function(response) {
            $scope.lex = response;
        });
    }
    
    $scope.init = function() {
        $scope.change_lex(14); // TOP LEVEL NODE
    }
    
    $scope.init();
});