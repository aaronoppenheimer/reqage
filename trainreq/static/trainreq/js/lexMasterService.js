// service to hold lex info from the server

app.service('LexMaster', function ($http) {
    // hold the lex content

    var interestList = {}
    
    var theLexes = {}

    fetchLex = function(theLexId) {
        console.log('LexMaster fetching lex #'+theLexId);
        $http.get("/reqage/api/lex/"+theLexId)
            .success(function(response) {
                console.log('LexMaster received lex '+response.pk);
                theLexes[response.pk] = response;
                if (interestList[response.pk]) {
                    list = interestList[response.pk];
                    for (i=0; i< list.length; i++) {
                        obj = list[i]
                        obj.updateLex(response)
                    }
                }
        });
    };
        

    return {
        // keep an array of controllers who are interested in a particular lex
        updateMe : function(object, theLex) {
            if (interestList[theLex]) {
                interestList[theLex].push(object);
            } else {
                interestList[theLex] = [object];
            }
            console.log('LexMaster added object watching lex '+theLex);
    
            if (theLexes[theLex]) {
                object.updateLex(theLexes[theLex]);
            } else {
                fetchLex(theLex);
            }
        }
    };  

});
