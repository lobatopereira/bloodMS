
var endpoint = '/api/g/blood/stock/bank/'
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
                    '#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462'
                ],
                borderWidth: 1
            }]
        };
        
        const config_bloodstockbank = {
            type: 'pie',
            data: dt,
            // options: myoption
        };
        const bloodstockbankChart_data = new Chart(
            document.getElementById('bloodstockbankChart_data'),
            config_bloodstockbank
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
