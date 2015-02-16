// Controller for a lex
//
// ao 2015-02-15

app.controller("lexCtrl", function($scope,CurrentLex) {
    
    $scope.curLex = CurrentLex;
    
    $scope.changeLex = function(id) {
        CurrentLex.setLex(id);
    };


    $scope.init = function() {
       CurrentLex.setLex(14); // TOP LEVEL NODE
    };
    
    $scope.init();
});