var tableData = myData;

var $tbody = d3.select("tbody");
var button = d3.select("#filter-btn");
var inputFieldDate = d3.select("#player");
//var inputFieldCity = d3.select("#city");
var columns = ["player", "rounds", "fairway_percentage", "year", "avg_distance", "gir", "avg_putts", "avg_scrambling", "avg_score", "points", "wins", "top_10s", "avg_sg_putts", "avg_sg_total", "sg_ott", "sg_apr", "sg_arg", "money"   ]

var addData = (dataInput) => {
    dataInput.forEach(playerStats => {
        var row = $tbody.append("tr");
        columns.forEach(column => row.append("td").text(playerStats[column])
        )
    });
}

addData(tableData);

button.on("click", () => {

    d3.event.preventDefault();
    
    var inputDate = inputFieldDate.property("value").trim();
    
    var filterDate = tableData.filter(tableData => tableData.player === inputDate);
    
    $tbody.html("");

    let response = {
        filterDate
    }

    if(response.filterDate.length !== 0) {
        addData(filterDate);
    }
            
    else {
            $tbody.append("tr").append("td").text("No Data :/");
        }
})
