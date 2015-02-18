// Controller for a lex
//
// ao 2015-02-15

app.controller("lexCtrl", function($scope,$http,appLexId) {

    var that=this;
    
    myLexId = null;

    $scope.myLex = null; // my current lex

    $scope.retarget = function(newLexId) {
        console.log('scope '+$scope.$id+' emitting retarget to '+newLexId);
        $scope.$emit('retarget',newLexId);
    };
    
    $scope.changeLex = function(id) {
        console.log('scope '+$scope.$id+' changing lex to #'+id);
        $http.get("/reqage/api/lex/"+id)
            .success(function(response) {
                $scope.myLex = response;
        });
    };
        
    $scope.doRetarget = function(event, data) {
        console.log('scope '+$scope.$id+' received message');
        console.log('  event.targetScope='+event['targetScope'].$id);
        console.log('  event.currentScope='+event['currentScope'].$id);
        $scope.changeLex(data);
    };
    
    init = function() {
        console.log('new lexCtrl, scope='+$scope.$id);
        if ($scope.lexId) {
            $scope.changeLex($scope.lexId);
            // I'm not the highest level so I shouldn't listen to re-targeting messages
            console.log('scope '+$scope.$id +' not setting listener with lex '+$scope.lexId);
        } else {
            // we haven't been given a lexId, so we should use the global one
            if (appLexId) {
                $scope.changeLex(appLexId);
                // I'm the highest level lex, so I listen for re-targeting
                $scope.$on('retarget', function(event, data) { $scope.doRetarget(event, data); });
                console.log('scope '+$scope.$id +' set listener with lex '+appLexId);
            } else {
                alert('no lex id set');
            }
        }
    };
    
    init(14);
});