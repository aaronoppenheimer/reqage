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
    $scope.isActiveChild=false;
    $scope.isActiveSibling=false;    
    $scope.makeSibling=function() {
        $scope.isActive = true;
        $scope.isActiveSibling = true;
        $scope.isActiveChild = false;
    }; 
    $scope.makeChild=function() {
        $scope.isActive = true;
        $scope.isActiveSibling = false;
        $scope.isActiveChild = true;
    }; 
    $scope.makeInactive=function() {
        $scope.isActive = false;
        $scope.isActiveSibling = false;
        $scope.isActiveChild = false;
    }; 
    
    $scope.newThing = '';
    $scope.submitSibling = function(sibling) {
    
        data={};
        data['content'] = $scope.newThing;
        data['sibling'] = sibling;
        data['parent'] = 0;
        data['lextype'] = 'Requirement';
        //submit the data to the server
        $http.post('/reqage/api/lex/', data)
        .success(function(response) {
            LexMaster.addedChild(response.parent_info.id);
        });
    
        $scope.newThing='';
        $scope.makeInactive();
    }

    $scope.submitChild = function(parent) {
    
        data={};
        data['content'] = $scope.newThing;
        data['parent'] = parent;
        data['sibling'] = 0;
        data['lextype'] = 'Requirement';
        //submit the data to the server
        $http.post('/reqage/api/lex/', data)
        .success(function(response) {
            LexMaster.addedChild(response.parent_info.id);
        });
    
        $scope.newThing='';
        $scope.makeInactive();
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