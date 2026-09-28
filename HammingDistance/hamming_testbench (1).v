`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/11/2026 03:00:19 PM
// Design Name: 
// Module Name: hamming_testbench
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


module hamming_testbench();
        reg [7:0] A;
        reg [7:0] B;
        reg [3:0] threshold ;
        reg [7:0] X ;
        reg [3:0] distance;
        reg equal ;
        reg within_threshold;
        wire [7:0] diff_out;
        wire [3:0]dist_out;
        wire eql_out;
        wire wt_out;
    hamming uut(.A(A),.B(B),.threshold(threshold),.difference(diff_out),.distance(dist_out),.equal(eql_out),.within_threshold(wt_out));
    integer errors = 0;
    integer i, j, t;
    initial begin
          
          for( i = 0; i <= 256; i = i+  1)begin 
                A = i[7:0];
                for ( j = 0; j <= 256 ;j = j+ 1)begin
                    B = j[7:0];
                    for ( t = 0; t <= 15; t = t + 1)begin
                        threshold = t[3:0];
                        X=A^B;
                        distance=X[0]+X[1]+X[2]+X[3]+X[4]+X[5]+X[6]+X[7];
                        equal = &(~(A^B));
                        within_threshold = (distance <= threshold);
                        #10
                        
                        if(distance != dist_out)begin
                            errors = errors +1;
                             $display("FAILED:Hamming distance doesnt match");
                        end
                        if(equal != eql_out )begin
                            errors = errors + 1;
                             $display("FAILED:doesnt detect equality correctly");
                        end
                        if(within_threshold != wt_out)begin
                            errors= errors +1;
                             $display("FAILED:doesnt keep up with threshold");
                        end
                        if( X != diff_out)begin
                            errors= errors + 1;
                             $display("FAILED: calculated wrong diff_string");
                        end
                    end
                end
          end
          if (errors==0) begin
            $display("PASSED");
          end
          else begin
            $display("FAILED, errors:%0d",errors);
          end
          
          
           $finish;
    end
endmodule
