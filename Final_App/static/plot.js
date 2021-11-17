function createPlot(data) {
  
    var data = JSON.parse(data);
    let trace1 = {
      x: data.xs,
      y: data.ys,
      type: 'bar'
  
    };
  
    let traces = [trace1];
  
    let layout = {
      title: "Players Per Year"
    };
  
    Plotly.newPlot("plot", traces, layout);
  
  }


  function otherPlot(data) {
  
    var data = JSON.parse(data);
    let trace2 = {
      x: data.sc,
      y: data.yr,
      type: 'bar'
  
    };
  
    let traces3 = [trace2];
  
    let layout2 = {
      title: "Scoring AVG Per Year"
    };
  
    Plotly.newPlot("plot2", traces3, layout2);
  
  }