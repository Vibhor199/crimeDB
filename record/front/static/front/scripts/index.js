$(document).ready(function () {
  document.getElementById('cityselect').addEventListener('change',function() {
    var text=$("#cityselect option:selected").text();
    $.ajax({
      type:'POST',
      url:'cityreq',
      data:{
        city: text,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(resp){
        console.log(resp)
        $('#shown').append("<li>"+text+"</li><br>");
      }
    });
  });
});


document.addEventListener("DOMContentLoaded", function(event) {
fetch(api)
    .then(function(response) { return response.json(); })
    .then(function(data) {
        var parsedData = parseData(data);
        console.log(parsedData)
        drawChart(parsedData);
    })
    .catch(function(err) { console.log(err); })
});

/**
 * Parse data into key-value pairs
 * @param {object} data Object containing historical data of BPI
 */
function parseData(data) {
    var arr = [];
    for (var i in data) {
        arr.push({
            year: +i, //date
            value: +data[i] //convert string to number
        });
    }
    return arr;
}

/**
 * Creates a chart using D3
 * @param {object} data Object containing historical data of BPI
 */
function drawChart(data) {
var svgWidth = 640, svgHeight = 450;
var margin = { top: 10, right: 60, bottom: 80, left: 50 };
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleLinear()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.year)})
    .y(function(d) { return y(d.value)})
    x.domain(d3.extent(data, function(d) { return d.year }));
    y.domain(d3.extent(data, function(d) { return d.value }));

g.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .attr("class","xax");

g.append("g")
    .call(d3.axisLeft(y))
    .attr("class","yax")
    .append("text")
    .attr("fill", "#fff")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", "0.71em")
    .attr("text-anchor", "end")
    .text("Reports");

g.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "#f1e6b2")
    .attr("stroke-linejoin", "round")
    .attr("stroke-linecap", "round")
    .attr("stroke-width", 3)
    .attr("d", line);
}
