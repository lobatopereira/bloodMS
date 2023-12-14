
var endpoint = '/api/g/patient/sex/blood-group/bank/'
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
                backgroundColor: 'rgba(0, 10, 219, 0.5)',
                borderWidth: 1
            },
            ]
        };
        
        const config_patientsexbloodgroupbank = {
            type: 'bar',
            data: dt,
            options: groupoption
        };
        const patientsexbloodgroupbank_data = new Chart(
            document.getElementById('patientsexbloodgroupbank_data'),
            config_patientsexbloodgroupbank
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
