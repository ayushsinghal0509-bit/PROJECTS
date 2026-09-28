

module hamming_wrapper (
    input  wire        clk,
    input  wire [15:0] sw,
    output wire [15:0] led,
    output wire [3:0]  an,
    output wire [6:0]  seg,
    output wire        dp
);

    wire [7:0] switch_val = sw[7:0];
    wire       sel        = sw[8];
    wire [3:0] threshold  = sw[12:9];

    wire [7:0] opA, opB;

    operand_capture capture_inst (
        .clk        (clk),
        .switch_val (switch_val),
        .sel        (sel),
        .regA       (opA),
        .regB       (opB)
    );

    wire [7:0] diff;
    wire       equal;
    wire       within_threshold;
    wire [3:0] distance;

    hamming hd_inst (
        .A                 (opA),
        .B                 (opB),
        .threshold         (threshold),
        .difference               (diff),
        .equal             (equal),
        .within_threshold  (within_threshold),
        .distance          (distance)
    );

    assign led[7:0]   = diff;
    assign led[13:8]  = 6'b0;             
    assign led[14]    = within_threshold;
    assign led[15]    = equal;



    display_driver disp_inst (
        .clk    (clk),
        .digit3 (4'd10),    
        .digit2 (4'd10),
        .digit1 (4'd0),
        .digit0 (distance),
        .an     (an),
        .seg    (seg)
    );

    assign dp = 1'b1;         

endmodule