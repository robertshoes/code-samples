// SERVICES

myApp.service('forecastService', function(){
    
    var self = this;
    self.city = 'New York, NY';

});

myApp.service('weatherService', ['$resource', function($resource){
    
    this.getWeather = function(city, days){
        var weatherAPI = $resource("http://api.openweathermap.org/data/2.5/forecast/daily", 
                                  {callback:'JSON_CALLBACK'}, {get:{method:"JSONP"}});
        var weatherResponse = weatherAPI.get({q: city, cnt: days});
        return weatherResponse;
    }

}]);

