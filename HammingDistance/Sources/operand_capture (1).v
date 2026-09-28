
module operand_capture (
    input        clk,
    input  [7:0] switch_val,
    input        sel,
    output reg [7:0] regA,
    output reg [7:0] regB
);

    wire [7:0] muxA_out;
    wire [7:0] muxB_out;

    mux2to1_8bit muxA (
        .in0 (switch_val),
        .in1 (regA),
        .sel (sel),
        .out (muxA_out)
    );

    mux2to1_8bit muxB (
        .in0 (regB),
        .in1 (switch_val),
        .sel (sel),
        .out (muxB_out)
    );

    always @(posedge clk) begin
        regA <= muxA_out;
        regB <= muxB_out;
    end

endmodule
