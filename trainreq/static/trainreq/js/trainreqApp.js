var app = angular.module('trainreqApp', ['ngCookies'])

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


// service to hold the current lex
app.service('CurrentLex', function ($http) {
    //     Just hold the current Lex so anyone who needs it can get it

    var that = this;
    that.lex = {content:'hiya woo',pk:0};
        
    this.setLex = function(l) {
        $http.get("/reqage/api/lex/"+l)
            .success(function(response) {
                that.lex = response;
        });
    };
        
    this.getLex = function() {
        return this.lex;
    }
});
