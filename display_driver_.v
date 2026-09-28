

module display_driver (
    input        clk,
    input  [3:0] digit3,
    input  [3:0] digit2,
    input  [3:0] digit1,
    input  [3:0] digit0,
    output [3:0] an,
    output [6:0] seg
);

    reg [17:0] counter = 18'd0;
    always @(posedge clk)
        counter <= counter + 1'b1;

    wire [1:0] digit_select = counter[17:16];

    reg [3:0] current_code;
    reg [3:0] an_reg;

    always @(*) begin
        case (digit_select)
            2'b00: begin current_code = digit0; an_reg = 4'b1110; end 
            2'b01: begin current_code = digit1; an_reg = 4'b1101; end
            2'b10: begin current_code = digit2; an_reg = 4'b1011; end
            2'b11: begin current_code = digit3; an_reg = 4'b0111; end 
        endcase
    end

    assign an = an_reg;

    seven_seg_decoder decoder_inst (
        .code (current_code),
        .seg  (seg)
    );

endmodule