// Controller for adding a lex
//
// ao 2015-02-15


app.controller('addLexCtrl', function($http) {
  this.submit = function(isValid, data) {
    if(!isValid) return;

    alert("woo!");
    //submit the data to the server
//     $http.post('/api/submit', data);
  }
});