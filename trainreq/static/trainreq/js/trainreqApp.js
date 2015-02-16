var app = angular.module('myApp', ['ngCookies'])

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.service('CurrentLex', function () {
    //     Just hold the current Lex so anyone who needs it can get it
    var currentLex = 0;

    return {
        setLex: function(l) {
            currentLex = l;
        },
        getLex: function() {
            return currentLex;
        }
    };

});