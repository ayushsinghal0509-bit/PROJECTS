`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/11/2026 02:45:09 PM
// Design Name: 
// Module Name: comptr4bit
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


module comptr4bit(
    input wire [3:0]a,b,
    output in_threshold
    );
    wire [3:0]x;
    assign x = ~(a^ b);
    assign in_threshold = &x | (b[3]&(~a[3])) | (x[3]&b[2]&(~a[2])) | (x[3]&x[2]&b[1]&(~a[1])) | (x[3]&x[2]&x[1]&b[0]&(~a[0]));
   
endmodule
