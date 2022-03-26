from Source.Pre_Built_Gates.Not import Not
from Source.Pre_Built_Gates.And import And
from Source.Pre_Built_Gates.Or import Or
from Source.Pre_Built_Gates.Power import Power
from Source.Logic_Gates.Mux16 import Mux16
from Source.Components.Boolean_Arithmetic.ALU import ALU
from Source.Components.Sequential_Logic.Register import Register
from Source.Components.Sequential_Logic.PC import PC

class CPU:
    def __init__(self,inM,instruction,reset) -> None:
        self.inM=inM
        self.instruction=instruction
        self.reset=reset
        self.out=[Power([Power(False) for _ in range(16)]),Power(False),Power([Power(False) for _ in range(15)]),Power([Power(False) for _ in range(15)])]
        self.mux=Power([Power(False) for _ in range(16)])
        self.ALUout=Power([Power(False) for _ in range(16)])
        self.a_load=Power(False)
        self.d_load=Power(False)
        self.PC_load=Power(False)
        self.A_register=Register(self.mux,self.a_load)
        self.D_register=Register(self.ALUout,self.d_load)
        self.PC=PC(self.A_register,self.PC_load,Power(True),self.reset)
        self()
    def __call__(self) -> None:
        not1=Not(self.instruction.out[0])
        mux1=Mux16(self.ALUout,self.instruction,not1)
        for i in range(16):
            self.mux.out[i].out=mux1.out[i].out
        a_load=Or(not1,self.instruction.out[10])
        self.a_load.out=a_load.out
        self.A_register()
        and1=And(self.instruction.out[0],self.instruction.out[3])
        mux2=Mux16(self.A_register,self.inM,and1)
        d_load=And(self.instruction.out[0],self.instruction.out[11])
        self.d_load.out=d_load.out
        alu=ALU(self.D_register,mux2,self.instruction.out[4],self.instruction.out[5],self.instruction.out[6],self.instruction.out[7],self.instruction.out[8],self.instruction.out[9])
        for i in range(16):
            self.ALUout.out[i].out=alu.out[0].out[i].out
        self.D_register()
        and3=And(self.instruction.out[0],self.instruction.out[12])
        poz=Not(alu.out[2])
        non_zero=Not(alu.out[1])
        jgt=And(self.instruction.out[0],self.instruction.out[15])
        poz_non_zero=And(poz,non_zero)
        jmp1=And(jgt,poz_non_zero)
        jeq=And(self.instruction.out[0],self.instruction.out[14])
        jmp2=And(jeq,alu.out[1])
        jlt=And(self.instruction.out[0],self.instruction.out[13])
        jmp3=And(jlt,alu.out[2])
        jmp4=Or(jmp1,jmp2)
        jmp5=Or(jmp4,jmp3)
        self.PC_load.out=jmp5.out
        self.PC()
        for i in range(16):
            self.out[0].out[i].out=alu.out[0].out[i].out
        self.out[1].out=and3.out
        for i in range(15):
            self.out[2].out[i].out=self.A_register.out[i+1].out
            self.out[3].out[i].out=self.PC.out[i+1].out