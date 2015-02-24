// Controller for a lex
//
// ao 2015-02-15

app.controller("lexCtrl", function($scope,$http,LexMaster) {

    var that=this;
    
    $scope.isTopLevel = false;
    
    $scope.myLex = null; // my current lex

    $scope.isOpen = false; // whether to display myself as open or not    
    $scope.toggleOpen = function() {
        $scope.isOpen = !$scope.isOpen;
    };
    
    $scope.showingInfo = false; // whether to display my info panel
    $scope.toggleInfo = function() {
        $scope.showingInfo = !$scope.showingInfo;
    };


    $scope.mouseIsOver = false;
    $scope.mouseEnter = function() {
        $scope.mouseIsOver = true;
    };
    $scope.mouseLeave = function() {
        $scope.mouseIsOver = false;
    };

    // if we need to change the top-level lex, use the emit structure
    $scope.retarget = function(newLexId) {
        $scope.$emit('retarget',newLexId);
    };
    
    $scope.remove = function() {
        parent=$scope.myLex.parent_info.id;
        data={};
        data['pk'] = $scope.myLex.pk;
        //submit the data to the server
        $http.delete('/reqage/api/lex/'+$scope.myLex.pk, data)
        .success(function(response) {
            LexMaster.addedChild(parent);
        });
        
    };
    
    $scope.fetchLex = function(id) {
        if ($scope.myLex) {
            LexMaster.stopUpdatingMe($scope, $scope.myLex.pk);
        }
        LexMaster.updateMe($scope,id);
    }
    
    $scope.updateLex = function(lex) {
        $scope.myLex = lex;
    }
            
    $scope.setTop = function(id) {
        $scope.isTopLevel = true;
        $scope.$on('retarget', function(event, data) { $scope.fetchLex(data); });
        $scope.fetchLex(id);
    }
    
    $scope.$on('$destroy', function iVeBeenDismissed() {
        LexMaster.stopUpdatingMe($scope, $scope.myLex.pk);
    });
});