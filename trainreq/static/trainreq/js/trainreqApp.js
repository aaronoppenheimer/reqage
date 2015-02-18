var app = angular.module('trainreqApp', ['ngRoute', 'ngCookies'])

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.value("appLexId",14);


// service to hold the current to-level lex
// app.service('CurrentLex', function ($http) {
//     //     Just hold the current Lex so anyone who needs it can get it
// 
//     var that = this;
//     that.lex = {content:'hiya woo',pk:0};
//         
//     this.setLex = function(l) {
//         $http.get("/reqage/api/lex/"+l)
//             .success(function(response) {
//                 that.lex = response;
//         });
//     };
//         
//     this.getLex = function() {
//         return this.lex;
//     }
//     
//     this.setLex(14); // initial node - the 'projects' node
// });
