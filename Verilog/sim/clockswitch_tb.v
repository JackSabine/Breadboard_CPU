module clockswitch_tb();

reg clk0, clk1, sel, rst_n;
wire clk_out;


clockswitch DUT(
    .clk0(clk0),
    .clk1(clk1),
    .sel(sel),
    .rst_n(rst_n),
    .sys_clk(clk_out)
);

initial begin
    rst_n   =   1'b0;
    sel     =   0;
    #10;
    rst_n   =   1'b1;
end

initial clk0 = 0;
always  #23  clk0 <= ~clk0;

initial clk1 = 0;
always  #1   clk1 <= ~clk1;

initial begin
    #100;
    #57;    sel = 1;
    #83;    sel = 0;
    #22;    sel = 1;
    #293;   sel = 0;
    #223;   sel = 1;
    #64;    sel = 0;
    #100;
end


endmodule