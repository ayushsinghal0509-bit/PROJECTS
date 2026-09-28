`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/11/2026 01:52:11 PM
// Design Name: 
// Module Name: hamming
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


module hamming(
input wire [7:0] A,
input wire [7:0] B,
input wire [3:0] threshold,
output wire [7:0] difference,
output wire [3:0] distance,
output wire equal,
output wire within_threshold
    );
    wire [1:0] u,v,w,x;
    wire [7:0] t;
    assign t = A^B;
    half_adder f0( .a(t[0]), .b(t[1]), .s(u[0]) , .c(u[1]));
    half_adder f1( .a(t[2]), .b(t[3]), .s(v[0]) , .c(v[1]));
    half_adder f2( .a(t[4]), .b(t[5]), .s(w[0]) , .c(w[1]));
    half_adder f3( .a(t[6]), .b(t[7]), .s(x[0]) , .c(x[1]));
    wire [2:0]p,q;
    full_adder_2bit f4(.x(u),.y(v),.total(p[1:0]),.cout(p[2]));
    full_adder_2bit f5(.x(w),.y(x),.total(q[1:0]),.cout(q[2]));
    full_adder_3bit f6(.x(p),.y(q),.total(distance[2:0]),.cout(distance[3]));
    assign difference=t;
    comptr4bit f7(.a(distance),.b(threshold),.in_threshold(within_threshold));
    comparator8bit f8(.x(A),.y(B),.eq(equal));
    
endmodule
