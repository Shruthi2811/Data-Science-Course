function basketcourt(space_width, space_height, court1_width, court1_height, x, y)
{
	
var margin = {top: 50, right: 0, bottom: 0, lefty: 600};

var svg = d3.select("body").append("svg")
						.attr("width", space_width)
						.attr("height", space_height)
						.append("g")
						.attr("transform", "translate(" + margin.lefty + "," + margin.top + ")");

//Draw the outer rectangle of the basketball court
var outer_rect = svg.append("rect")
                            .attr("x", x)
                            .attr("y", y)
                            .attr("width", court1_width)
                            .attr("height", court1_height)
							.attr("fill", "none")
							.attr("stroke", "black")
							.attr("stroke-width", 4);
		
// Draw the basket hoop which is at the center
var hoop = svg.append("circle")
						.attr("cx", x + 250)
						.attr("cy", y + 47.5)
						.attr("r", 7.5)
						.attr("fill", "none")
						.attr("stroke", "black")
						.attr("stroke-width", 2);
						
// Draw the backboard of the basket
var backboard = svg.append("rect")
							.attr("x", x + 220)
							.attr("y", y + 40)
							.attr("width", 60)
							.attr("height", 1)
							.attr("fill", "black")
							.attr("stroke", "black")
							.attr("stroke-width", 2);
							
// Draw the outer box of the three sec area
var outer_sec = svg.append("rect")
							.attr("x", x + 170)
							.attr("y", y)
							.attr("width", 160)
							.attr("height", 190)
							.attr("fill", "none")
							.attr("stroke", "black")
							.attr("stroke-width", 2);
						
// Draw the inner box of the three sec area
var outer_sec = svg.append("rect")
							.attr("x", x + 190)
							.attr("y", y)
							.attr("width", 120)
							.attr("height", 190)
							.attr("fill", "none")
							.attr("stroke", "black")
							.attr("stroke-width", 2);
							
// Draw the left side three point line
var left_line = svg.append("line")
							.attr("x1", x + 30)
							.attr("y1", y)
							.attr("x2", x + 30)
							.attr("y2", 45 - y)
							.attr("stroke", "black")
							.attr("stroke-width", 3);
							

// Draw the right side three point line
var right_line = svg.append("line")
							.attr("x1", -30 -x)
							.attr("y1", y)
							.attr("x2", -30 -x)
							.attr("y2", 45 - y)
							.attr("stroke", "black")
							.attr("stroke-width", 3);

// Draw the three point arc
var three_point_arc = svg.append("path")
							.attr("d", "M " + parseInt(x+30) + " " + parseFloat(45-y) + " C " + parseInt(180+x) + " " + parseInt(252.5 - y) + ", " + parseInt(-180-x) + " " + parseInt(252.5-y) + ", " + parseInt(-x-30) + " " + parseFloat(45 - y))
							.attr("stroke", "black")
							.attr("stroke-width", 3)
							.attr("fill", "none");
							
// Draw the center circle
var center_circle = svg.append("circle")
								.attr("cx", x + 250)
								.attr("cy", 470 + y)
								.attr("r", 60)
								.attr("fill", "none")
								.attr("stroke", "blacK")
								.attr("stroke-width", 3);
								
// Draw the restraining cirlce
var rest_circle = svg.append("circle")
								.attr("cx", x + 250)
								.attr("cy", 470 + y)
								.attr("r", 20)
								.attr("fill", "none")
								.attr("stroke", "black")
								.attr("stroke-width", 3);
								
// Draw the free throw circle
var free_throw_circle = svg.append("circle")
								.attr("cx", x + 250)
								.attr("cy", 187.5 + y)
								.attr("r", 60)
								.attr("fill", "none")
								.attr("stroke", "black")
								.attr("stroke-width", 3);
								
// Draw the restricted area 
var res_area = svg.append("circle")
						.attr("cx", x + 250)
						.attr("cy", y + 47.5)
						.attr("r", 40)
						.attr("fill", "none")
						.attr("stroke", "black")
						.attr("stroke-dasharray", "8 5")
						.attr("stroke-width", 3);
						

return svg
}

