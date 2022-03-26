from Source.Computer import Computer
from Source.Pre_Built_Gates.Power import Power

def bool_to_int(a):
        x=0
        for i in range(15,0,-1):
            x+=int(a[i])*(2**(15-i))
        if a[0]==True:
            x=x-32768
        return x

def main():
    reset=Power(True)
    computer=Computer(reset,"Source/ROM_Data.txt")
    reset.out=False
    computer.Memory.log_memory()
    while(True):
        computer()
        computer.Memory.log_memory()
        a_reg=[str(int(computer.CPU.A_register.out[i].out)) for i in range(16)]
        d_reg=[str(int(computer.CPU.D_register.out[i].out)) for i in range(16)]
        clock=[str(int(computer.CPU.PC.out[i].out)) for i in range(16)]
        command=[str(int(computer.CPU.instruction.out[i].out)) for i in range(16)]
        print("A Register: "+ "".join(a_reg) + " " + str(bool_to_int(a_reg)))
        print("D Register: "+ "".join(d_reg) + " " + str(bool_to_int(d_reg)))
        print("Clock cycle: "+ "".join(clock) + " " + str(bool_to_int(clock)))
        print("Command: "+ "".join(command))
        print()

if __name__ == "__main__":
    main()