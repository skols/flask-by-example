(function () {
    'use strict';
    
    angular.module('WordcountApp', [])
    
    .controller('WordcountController', ['$scope', '$log', '$http', '$timeout', function($scope, $log, $http, $timeout) {
        $scope.getResults = function() {
            $log.log("Angular test");
            
            // Get the URL from the input
            var userInput = $scope.url;
            
            // Fire the API request
            $http.post('/start/', {"url": userInput}).
                success(function(results) {
                    $log.log(results);
                    getWordCount(results);
                }).
                error(function(error) {
                    $log.log(error);
                });
        };
        
        function getWordCount(jobID) {
            var timeout = "";
            
            var poller = function() {
                // Fire another request
                $http.get('/results/'+jobID).
                    success(function(data, status, headers, config) {
                        if(status === 202){
                            $log.log(data,status);
                        } else if(status === 200) {
                            $log.log(data);
                            $scope.wordcounts = data;
                            $timeout.cancel(timeout);
                            return false;
                        }
                        // Continue to call the poller function every 2 seconds until the timeout is cancelled
                        timeout = $timeout(poller, 2000);
                    });
            };
            poller();
        }
    }
    ]);
}());