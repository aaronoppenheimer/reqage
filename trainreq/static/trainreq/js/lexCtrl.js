// Controller for a lex
//
// ao 2015-02-15

app.controller("lexCtrl", function($scope,$http) {

    var that=this;
    
    $scope.isTopLevel = false;
    
//     $scope.lexId = null;
    $scope.myLex = null; // my current lex
    complete = false;

    $scope.isOpen = false; // whether to display myself as open or not    
    $scope.toggleOpen = function() {
        $scope.isOpen = !$scope.isOpen;
    };
    
    $scope.showingInfo = false; // whether to display my info panel
    $scope.toggleInfo = function() {
        $scope.showingInfo = !$scope.showingInfo;
    };

    // if we need to change the top-level lex, use the emit structure
    $scope.retarget = function(newLexId) {
        console.log('scope '+$scope.$id+' emitting change to '+newLexId);
        $scope.$emit('retarget',newLexId);
    };
    
    // fetch complete lex
    $scope.fetchLex = function(id) {
        console.log('scope '+$scope.$id+' fetching lex #'+id);
        $http.get("/reqage/api/lex/"+id)
            .success(function(response) {
                $scope.myLex = response;
            that.complete = true;
        });
    };
        
    $scope.setTop = function(id) {
        console.log('scope '+$scope.$id+' is top level');
        $scope.isTopLevel = true;
        $scope.$on('retarget', function(event, data) { $scope.fetchLex(data); });
        $scope.fetchLex(id);
    }
        
    init = function() {
//         console.log('scope '+$scope.$id+' has lexId '+$scope.lexId);
//         if ($scope.lexId) {
//             $scope.fetchLex($scope.lexId);
//             // I'm not the highest level so I shouldn't listen to re-targeting messages
//         } else {
//             // we haven't been given a lexId, so we should use the global one
//             if (appLexId) {
//                 console.log('scope '+$scope.$id+' is highest level');
//                 $scope.fetchLex(appLexId);
//                 // I'm the highest level lex, so I listen for re-targeting
//                 $scope.$on('retarget', function(event, data) { $scope.fetchLex(data); });
//             } else {
//                 alert('no lex id set');
//             }
//         }
    };
    
    init();
    
});