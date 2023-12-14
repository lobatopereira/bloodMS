
var endpoint = '/api/g/blood/banked/used/stock/bank/'
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        const dt = {
            labels: data.label,
            datasets: [{
                label: 'Total Pakote',
                data: data.obj,
                backgroundColor: [
                    '#dd2020d9','#544a4ae3','#bebada','#fb8072','#80b1d3','#fdb462'
                ],
                borderWidth: 1
            }]
        };
        
        const config_bloodbankedusedstockbank = {
            type: 'pie',
            data: dt,
            // options: myoption
        };
        const bloodbankedusedstockbankChart_data = new Chart(
            document.getElementById('bloodbankedusedstockbankChart_data'),
            config_bloodbankedusedstockbank
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
