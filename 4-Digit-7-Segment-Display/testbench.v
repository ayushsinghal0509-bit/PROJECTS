`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/21/2026 02:34:46 PM
// Design Name: 
// Module Name: test3
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


module test3();
    reg [0:13] sw;
    wire [0:7] cathode;
    wire [0:3] anode;
    reg clk;
    
    dig47seg UUT (
       .clk(clk),
       .sw(sw),
       .cathode(cathode),
       .anode(anode)    
    );

initial begin
    clk = 0;
    sw =  14'b00000000000000;
    #100    
    sw = 14'b00010000000001;
    #20
    sw= 14'b01000000000010;
    # 50;
    sw=~14'b00100000000100;
    #34
    sw=~14'b00010000001000;
    $finish;
end
always begin
    #5 clk=~clk;
end
 
endmodule
