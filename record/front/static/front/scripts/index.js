
document.addEventListener("DOMContentLoaded", function(event) {

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
        var parsedData = parseData(JSON.parse(resp));
        var color=getRandomColor()
        drawChart(parsedData,color);
        $('#shown').append("<li style='color:"+color+";'>"+text+"</li>");
      }
    });
  });
  function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  var svgWidth = 640, svgHeight = 450;
  var margin = { top: 10, right: 60, bottom: 80, left: 50 };
  var width = svgWidth - margin.left - margin.right;
  var height = svgHeight - margin.top - margin.bottom;
  var x = d3.scaleLinear()
      .rangeRound([0, width]);
  var y = d3.scaleLinear()
      .rangeRound([height, 0]);
  var svg = d3.select('svg')
          .attr("width", svgWidth)
          .attr("height", svgHeight);
  var g = svg.append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


fetch(api)
    .then(function(response) { return response.json(); })
    .then(function(data) {
        var parsedData = parseData(data);
        console.log(parsedData)
        drawXY(parsedData);
    })
    .catch(function(err) { console.log(err); })

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
    function drawXY(data) {
      x.domain(d3.extent(data, function(d) { return d.year }));
      y.domain([0,40]);
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


    }

    function drawChart(data,color) {


    var line = d3.line()
            .x(function(d) { return x(d.year)})
            .y(function(d) { return y(d.value)})


    g.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", color)
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 3)
        .attr("d", line);
    }




});
