
module mux2to1_8bit (
    input  [7:0] in0,
    input  [7:0] in1,
    input        sel,
    output [7:0] out
);

    assign out = (in1 & {8{sel}}) | (in0 & {8{~sel}});

endmodule