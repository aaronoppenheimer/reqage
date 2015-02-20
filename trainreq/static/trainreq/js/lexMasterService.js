// service to hold lex info from the server

app.service('LexMaster', function ($http) {
    // hold the lex content

    var interestList = {}
    
    var theLexes = {}

    updateInteresteds = function(id) {
        if (theLexes[id]) {
            if (interestList[id]) {
                list = interestList[id];
                for (i=0; i< list.length; i++) {
                    obj = list[i]
                    console.log('telling scope '+obj.$id);
                    obj.updateLex(theLexes[id])
                }
            }
        } else {
            // we don't have it - go get it.
            console.log('LexMaster cache miss - going to fetch #'+id);
            fetchLex(id);
        }            
    }

    fetchLex = function(theLexId) {
        console.log('LexMaster fetching lex #'+theLexId);
        $http.get("/reqage/api/lex/"+theLexId)
            .success(function(response) {
                console.log('LexMaster received lex '+response.pk);
                theLexes[response.pk] = response;
                updateInteresteds(response.pk);
        });
    };
        

    return {
                // keep an array of controllers who are interested in a particular lex
                updateMe : function(object, theLexId) {
                    if (interestList[theLexId]) {
                        interestList[theLexId].push(object);
                    } else {
                        interestList[theLexId] = [object];
                    }
                    console.log('LexMaster added object watching lex '+theLexId);

                    updateInteresteds(theLexId);
                },
                stopUpdatingMe : function(object, theLexId) {
                    if (interestList[theLexId]) {
                        var i = interestList[theLexId].indexOf(object);
                        if(i != -1) {
                            interestList[theLexId].splice(i, 1);
                        }
                    }
                    console.log('LexMaster removed object watching lex '+theLexId);
                }
        };  
});
