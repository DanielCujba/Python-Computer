from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import *
from Source.Computer import Computer
from Source.Pre_Built_Gates.Power import Power
from Source.Hack_Assembler.Main import Assembler
from Source.VM_To_Assembly.VM_Compiler import VirtualMachineCompiler
from main import bool_to_int


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Hack Computer")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.power=Power(True)
        self.path="Source/ROM_Data.txt"
        self.computer=Computer(self.power,self.path)
        self.assembler=Assembler()
        self.power.out=False
        self.create_widgets()
    def create_widgets(self):
        left_frame = Frame(self, width=400, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = Frame(self, width=350, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # Create frames and labels in left_frame
        Label(left_frame, text="Registers").grid(row=0, column=0, padx=5, pady=5)

        # load image to be "edited"
        registers = Frame(left_frame, width=300, height=185)
        registers.grid(row=1, column=0, padx=5, pady=5)

        a_register = Label(registers, text="A Register", relief=RAISED)
        a_register.grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        
        self.a_register_data = Label(registers, text="0000000000000000 0")
        self.a_register_data.grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        d_register = Label(registers, text="D Register", relief=RAISED)
        d_register.grid(row=2, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        self.d_register_data = Label(registers, text="0000000000000000 0")
        self.d_register_data.grid(row=3, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        clock_cycle = Label(registers, text="Clock Cycle", relief=RAISED)
        clock_cycle.grid(row=4, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        self.clock_cycle_data = Label(registers, text="0000000000000000 0")
        self.clock_cycle_data.grid(row=5, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        command = Label(registers, text="Command", relief=RAISED)
        command.grid(row=6, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        self.command_data = Label(registers, text="0000000000000000 0")
        self.command_data.grid(row=7, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        # Display image in right_frame
        self.ram = ScrolledText(right_frame)
        self.ram.grid(row=0, column=0, padx=5, pady=5)

        # Create tool bar frame
        tool_bar = Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        # Example labels that could be displayed under the "Tool" menu
        Button(tool_bar, text="Load ROM", command=self.loadROM).grid(row=1, column=0, padx=5, pady=5)
        Button(tool_bar, text="Compile VM", command=self.compileVM).grid(row=2, column=0, padx=5, pady=5)
        Button(tool_bar, text="Compile ASM",command=self.compileASM).grid(row=3, column=0, padx=5, pady=5)
        Button(tool_bar, text="Step",command=self.step).grid(row=4, column=0, padx=5, pady=5)
        Button(tool_bar, text="Reset",command=self.reset).grid(row=5, column=0, padx=5, pady=5)
    
    def step(self):
        self.computer()
        self.computer.Memory.log_memory()
        a_reg=[str(int(self.computer.CPU.A_register.out[i].out)) for i in range(16)]
        d_reg=[str(int(self.computer.CPU.D_register.out[i].out)) for i in range(16)]
        clock=[str(int(self.computer.CPU.PC.out[i].out)) for i in range(16)]
        command=[str(int(self.computer.CPU.instruction.out[i].out)) for i in range(16)]
        a_reg = "".join(a_reg) + " " + str(bool_to_int(a_reg))
        d_reg = "".join(d_reg) + " " + str(bool_to_int(d_reg))
        clock = "".join(clock) + " " + str(bool_to_int(clock))
        command = "".join(command) + " " + str(bool_to_int(command))
        self.a_register_data.config(text=a_reg)
        self.d_register_data.config(text=d_reg)
        self.clock_cycle_data.config(text=clock)
        self.command_data.config(text=command)
        self.ram.delete(1.0,END)
        with open("Source/RAM_Log.txt") as f:
            i=0
            for line in f:
                self.ram.insert(INSERT,f"{i}: "+line)
                i+=1
            

    def reset(self):
        self.power.out=True
        self.step()
        self.power.out=False
    
    def loadROM(self):
        path = filedialog.askopenfilename()
        if path == () or path == "":
            return
        i=0
        with open(path,"r") as f:
            with open("Source/ROM_Data.txt","w") as g:
                for j in f:
                    i+=1
                    g.write(j)
                while i < 32768:
                    i+=1
                    g.write("\n0000000000000000")
        self.computer.ROM.loadROM("Source/ROM_Data.txt")
        

    def compileVM(self):
        path = filedialog.askdirectory()
        if path == () or path == "":
            return
        compiler = VirtualMachineCompiler(path)
        compiler.parser_module()
        compiler.code_writer_module()
    
    def compileASM(self):
        if path == () or path == "":
            return
        path = filedialog.askopenfilename()
        self.assembler.assemble_file(path)
        




if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()