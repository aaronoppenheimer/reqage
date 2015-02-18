// Controller for a lex child
//
// ao 2015-02-15

app.controller("lexChildCtrl", function($scope) {

    $scope.isOpen = false; // whether to display myself as open or not
    
    $scope.toggleOpen = function() {
        $scope.isOpen = !$scope.isOpen;
    }
});