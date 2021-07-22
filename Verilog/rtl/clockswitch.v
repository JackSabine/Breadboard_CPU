module clockswitch(
    input wire clk0, clk1, sel, rst_n,
    output wire sys_clk
);

wire CrossFB0_1, CrossFB1_0, Link1, Link0, Inp1, Inp0, sel_n, clk0_n, clk1_n, selbuf1, selbuf0, selgate1, selgate0;

not(sel_n, sel);
not(clk0_n, clk0);
not(clk1_n, clk1);

and(Inp1, sel,      CrossFB0_1);
and(Inp0, sel_n,    CrossFB1_0);

dff U1(
    .d(Inp1),
    .clk(clk1),
    .rst_n(rst_n),
    .q(Link1),
    .q_n()
);

dff U2(
    .d(Link1),
    .clk(clk1_n),
    .rst_n(rst_n),
    .q(selbuf1),
    .q_n(CrossFB1_0)
);

dff U3(
    .d(Inp0),
    .clk(clk0),
    .rst_n(rst_n),
    .q(Link0),
    .q_n()
);

dff U4(
    .d(Link0),
    .clk(clk0_n),
    .rst_n(rst_n),
    .q(selbuf0),
    .q_n(CrossFB0_1)
);

and(selgate1, selbuf1, clk1);
and(selgate0, selbuf0, clk0);

or(sys_clk, selgate1, selgate0);



endmodule

module dff(
    input wire d, clk, rst_n,
    output reg q, q_n
);

always @(posedge clk or negedge rst_n) begin
    if(rst_n == 1'b0) begin
        q   <=  1'b0;
        q_n <=  1'b1;
    end
    else begin
        q   <=  d;
        q_n <= ~d;
    end
end

endmodule