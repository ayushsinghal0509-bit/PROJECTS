`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/21/2026 01:25:08 PM
// Design Name: 
// Module Name: dig47seg
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




module dig47seg(
    input clk,
    input [0:13] sw,
    output wire [0:3] anode,
    output reg [0:7] cathode);
    reg [0:9] dataout0 = 0;
    reg [0:9] dataout1 = 0;
    reg [0:9] dataout2 = 0;
    reg [0:9] dataout3 = 0;
    reg [0:16] counter=0;
    reg [0:1] active_anode= 0;
    reg [0:9] currdig = 0;
    

       always @(*) begin
        if (currdig[9]) begin
            cathode=~8'b11110111;
        end
       else if(currdig[8]) begin
            cathode=~8'b11111111;
       end
       else if(currdig[7])begin
            cathode=~8'b11100001;
       end
       else if(currdig[6]) begin
            cathode=~8'b10111111;
       end
       else if(currdig[5])begin
            cathode=~8'b10110111;
       end
       else if(currdig[4])begin
            cathode=~8'b01100111;
       end
       else if(currdig[3])begin
            cathode=~8'b11110011;
       end
       else if(currdig[2]) begin
            cathode=~8'b11011011;
       end
       else if(currdig[1]) begin
            cathode=~8'b01100001;
       end
       else begin
            cathode=~8'b11111101;
        end
       
       
       end
       
//       always @(posedge clk) begin
//            counter=counter+1;
//            if (counter ==17'd99999)begin
//                anode=anode<<1;
                
        
//            end
//        end

    always @(posedge clk) begin
        if (sw[10]) begin
        dataout0[0:9] <= sw[0:9];
        end
        if (sw[11]) begin
        dataout1[0:9] <= sw[0:9]; // Sample switches when sw10 is high
        end
        if (sw[12]) begin
        dataout2[0:9] <= sw[0:9]; // Sample switches when sw10 is high
        end
        if (sw[13]) begin
        dataout3[0:9] <= sw[0:9]; // Sample switches when sw10 is high
        end
        
        // If sw10 is OFF, dataout0 holds its value
    end
    always @(posedge clk) begin // Increment cycle counter every clock
        counter <= counter + 1;
        // After 100,000 cycles (1 ms), move to the next signal
        if (counter == 17'd99999) begin
        counter <= 0;
        
        active_anode <= (active_anode == 2'd3) ?
        2'd0 : active_anode + 1;
        // active_anode can wrap around if it is 2 bits wide
        end
        if (active_anode== 2'd0) begin
            currdig <= dataout0;
        end
        else if (active_anode== 2'd1)begin
            currdig <=dataout1;
        end
        else if (active_anode==2'd2)begin
            currdig <=dataout2;
        end
        else begin
            currdig <=dataout3;
        end
        
    end
    


    // Activate the anodes based on counter value
    assign anode[0] = ~(active_anode == 2'd0);
    assign anode[1] = ~(active_anode == 2'd1);
    assign anode[2] = ~(active_anode == 2'd2);
    assign anode[3] = ~(active_anode == 2'd3);
    
endmodule
