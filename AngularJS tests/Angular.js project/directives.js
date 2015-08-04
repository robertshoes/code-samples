
// DIRECTIVES

myApp.directive('forecastResults',function(){
    return {
        templateUrl: 'directives/forecastresults.htm',
        replace: true,
        scope: {
            cityWeather: '=',
            convertDateFunc: '&',
            convertToFahrenheitTemp: '&',
            dateFormat: '@'

        }
        
    }
});

