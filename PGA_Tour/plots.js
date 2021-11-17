let name = 'Travis Taylor'

let title = `${name}'s First Plotly Chart`

let books = [results.results]

let timesRead = [results.rounds]

let trace1 = {
  x: books,
  y: timesRead,
  type: 'bar'
};

let data = [trace1];

let layout = {
  title: title
};

Plotly.newPlot("plot", data, layout);