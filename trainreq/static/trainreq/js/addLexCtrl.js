// Controller for adding a lex
//
// ao 2015-02-15


app.controller('addLexCtrl', function($scope,$http,CurrentLex) {
  this.submit = function(isValid, data) {
    if(!isValid) return;

    data.parent=CurrentLex.lex.pk;

    //submit the data to the server
    $http.post('/reqage/api/lex/', data)
    .success(function(response) {
        CurrentLex.setLex(data.parent);
    });
    $scope.data={};
  }
});