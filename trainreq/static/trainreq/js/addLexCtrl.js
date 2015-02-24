// Controller for adding a lex
//
// ao 2015-02-15


app.controller('addLexCtrl', function($scope,$http,LexMaster) {

    $scope.isVisible=false;
    $scope.show=function() {
        $scope.isVisible=true;
    };    
    $scope.hide=function() {
        $scope.isVisible=false;
    };    
    
    $scope.isActive=false;
    $scope.makeActive=function() {
        $scope.isActive = true;
    }; 
    $scope.makeInactive=function() {
        $scope.isActive = false;
    }; 
    
    $scope.newThing = '';
    $scope.submit = function(sibling) {
    
        data={};
        data['content'] = $scope.newThing;
        data['sibling'] = sibling;
        data['lextype'] = 'Requirement';
        //submit the data to the server
        $http.post('/reqage/api/lex/', data)
        .success(function(response) {
            LexMaster.addedChild(response.parent_info.id);
        });
    
        $scope.newThing='';
        $scope.isActive=false;
    }
//   this.submit = function(isValid, data) {
//     if(!isValid) return;
// 
//     data.parent=CurrentLex.lex.pk;
// 
//     //submit the data to the server
//     $http.post('/reqage/api/lex/', data)
//     .success(function(response) {
//         CurrentLex.setLex(data.parent);
//     });
//     $scope.data={};
//   }
});