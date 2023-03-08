class ParserModule:
    def parse_file(self,file_name):
        #Reads the content of a file, deletes the comments and white space, 
        #labels each line base on the command type and separates it into usefull chunks
        assembly_file=open(file_name,"r")
        segmented_file=[]
        for line in assembly_file:
            command=[None,None]
            line=line[:line.find("//")]
            if line =="":
                 continue
            line = line.strip()
            if "(" in line:
                command[0]="L"
                command[1]=line.strip("()")
            elif "@" in line:
                command[0]="A"
                command[1]=line.strip("@")
            else:
                command[0]="C"
                c_command=[None,None,None]
                start=0
                end=len(line)
                if "=" in line:
                    c_command[0]=line.split("=")[0]
                    start=line.index("=")+1
                if ";" in line:
                    c_command[2]=line.split(";")[1]
                    end = line.index(";")
                c_command[1]=line[start:end]
                command[1]=c_command
            segmented_file.append(command)
        assembly_file.close()
        return segmented_file

class SymbolTableModule:
    def __init__(self):
        self.c_commands=[{None:"000","M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"},{"0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000","!D":"0001101","!A":"0110001","-D":"0001111","-A":"0110011","D+1":"0011111","A+1":"0110111","D-1":"0001110","A-1":"0110010","D+A":"0000010","D-A":"0010011","A-D":"0000111","D&A":"0000000","D|A":"0010101","M":"1110000","!M":"1110001","-M":"1110011","M+1":"1110111","M-1":"1110010","D+M":"1000010","D-M":"1010011","M-D":"1000111","D&M":"1000000","D|M":"1010101"},{None:"000","JGT":"001","JEG":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}]
        self.a_commands={"SP":"0000000000000000","LCL":"0000000000000001","ARG":"0000000000000010","THIS":"0000000000000011","THAT":"0000000000000100","R0":"0000000000000000","R1":"0000000000000001","R2":"0000000000000010","R3":"0000000000000011","R4":"0000000000000100","R5":"0000000000000101","R6":"0000000000000110","R7":"0000000000000111","R8":"0000000000001000","R9":"0000000000001001","R10":"0000000000001010","R11":"0000000000001011","R12":"0000000000001100","R13":"0000000000001101","R14":"0000000000001110","R15":"0000000000001111","SCREEN":"0100000000000000","KBD":"0110000000000000"}
        self.counter=16
    def translate_l_commands(self,assembly_array):
        #Maps each symbol label to a certain place in ROM
        line_idx=0
        for command in assembly_array:
            if not command[0] == "L":
                line_idx+=1
            if command[0] == "L" and not self.a_commands.get(command[1]):
                self.a_commands[command[1]]=self.decimal_to_binary(line_idx)
    
    def translate_a_commands(self,assembly_array):
        #Maps each symbol label to a certain place in RAM
        for command in assembly_array:
            if command[0] == "A" and not self.a_commands.get(command[1]):
                if not command[1].isdecimal(): 
                    self.a_commands[command[1]]=self.decimal_to_binary(self.counter)
                    self.counter+=1
                    continue
                self.a_commands[command[1]]=self.decimal_to_binary(int(command[1]))


    def check_command(self,command_array):
        #Returns the equivalent machine code for the assembly command
        command_type,command=command_array
        if command_type == "A":
            return self.a_commands.get(command)
        if command_type == "C":
            return "111"+self.c_commands[1].get(command[1])+self.c_commands[0].get(command[0])+self.c_commands[2].get(command[2])
        return None
    
    def decimal_to_binary(self,value):
        #Transforms a decimal value into a 16-bit binary number
        binary_power=16
        binary_array=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
        while value > 0:
            if(value>=2**binary_power):
                value-=2**binary_power
                binary_array[15-binary_power]="1"
            binary_power-=1
        return "".join(binary_array)

class Assembler:
    def __init__(self):
        self.parser=ParserModule()
        self.symbol_table=SymbolTableModule()
    def assemble_file(self,file_name):
        #Uses the ParserModule and SymbolTableModule to create a machine code file 
        #in the same directory as the assembly file.
        assembly_array=self.parser.parse_file(file_name)
        self.symbol_table.translate_l_commands(assembly_array)
        self.symbol_table.translate_a_commands(assembly_array)
        machine_code_array=[]
        for item in assembly_array:
            machine_code_line=self.symbol_table.check_command(item)
            if machine_code_line != None:
                machine_code_array.append(machine_code_line)
        file_content="\n".join(machine_code_array)
        machine_code_file=open(file_name[:file_name.find(".")]+".hack","w")
        machine_code_file.write(file_content)
        machine_code_file.close()

if __name__ == "__main__":
    assembler=Assembler()
    assembler.assemble_file(input("File Path: "))