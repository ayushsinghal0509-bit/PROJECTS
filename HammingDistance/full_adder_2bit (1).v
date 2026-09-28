`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/11/2026 02:03:52 PM
// Design Name: 
// Module Name: full_adder_2bit
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


module full_adder_2bit(
    input wire[1:0] x,
    input wire[1:0] y,

    output wire [1:0] total,
    output wire cout
    );
    wire tempc;
    full_adder f0 (
    .a(x[0]),
    .b(y[0]),
    .cin(0),
    .s(total[0]),
    .cout(tempc)
    );
    full_adder f1 (
    .a(x[1]),
    .b(y[1]),
    .cin(tempc),
    .s(total[1]),
    .cout(cout)
    );
    
endmodule
