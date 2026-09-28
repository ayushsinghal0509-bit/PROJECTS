`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/11/2026 02:32:38 PM
// Design Name: 
// Module Name: full_adder_3bit
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module full_adder_3bit(
    input wire[2:0] x,
    input wire[2:0] y,
    output wire [2:0] total,
    output cout
    );
    wire tempc;
    full_adder_2bit  f0(
    .x(x[1:0]),
    .y(y[1:0]),
    .total(total[1:0]),
    .cout(tempc)
    );
    full_adder f1(
    .a(x[2]),
    .b(y[2]),
    .cin(tempc),
    .s(total[2]),
    .cout(cout)
    );
    
    
endmodule
