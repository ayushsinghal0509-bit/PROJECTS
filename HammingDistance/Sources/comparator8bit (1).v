`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/11/2026 01:57:21 PM
// Design Name: 
// Module Name: comparator8bit
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


module comparator8bit(
    input wire [7:0] x,
    input wire [7:0] y,
    output eq
    );
    wire [7:0] xnor_bits;
    assign xnor_bits = ~(x^ y);
    assign eq = &xnor_bits;   
endmodule
