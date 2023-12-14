
var endpoint = '/api/g/blood-banked-used-out/stock/bank/by-year/'
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        const dt = {
            labels: data.label,
            datasets: [
            {
                label: data.obj1a,
                data: data.obj1,
                backgroundColor: 'rgba(225, 92, 92, 1)',
                borderWidth: 1
            },
            {
                label: data.obj2a,
                data: data.obj2,
                backgroundColor: 'rgba(0, 0, 9, 0.5)',
                borderWidth: 1
            },
            {
                label: data.obj3a,
                data: data.obj3,
                backgroundColor: 'rgba(19, 220, 0, 0.5)',
                borderWidth: 1
            },
            {
                label: data.obj4a,
                data: data.obj4,
                backgroundColor: 'rgba(255, 228, 0, 0.5)',
                borderWidth: 1
            },
            ]
        };
        
        const config_gbloodbankedusedoutstockbankbyyear = {
            type: 'bar',
            data: dt,
            options: groupoption
        };
        const gbloodbankedusedoutstockbankbyyear_data = new Chart(
            document.getElementById('gbloodbankedusedoutstockbankbyyear_data'),
            config_gbloodbankedusedoutstockbankbyyear
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
