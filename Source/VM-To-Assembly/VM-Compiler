from os import listdir
class VirtualMachineCompiler:
    def __init__(self,file_path):
        self.file_path=file_path
        self.files=[]
        self.files_content=[]
        self.is_folder=True
        if ".vm" in file_path:
            self.is_folder=False
            self.files.append(file_path)
        self.assembly_commands={
            None:"",
            "add":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=D+M\n",
            "sub":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=M-D\n",
            "neg":"@SP\nA=M-1\nM=-M\n",
            "eq":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nD=M-D\nM=-1\n@LABEL{number}\nD;JEQ\n@SP\nA=M-1\nM=0\n(LABEL{number})\n",
            "gt":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nD=M-D\nM=-1\n@LABEL{number}\nD;JGT\n@SP\nA=M-1\nM=0\n(LABEL{number})\n",
            "lt":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nD=M-D\nM=-1\n@LABEL{number}\nD;JLT\n@SP\nA=M-1\nM=0\n(LABEL{number})\n",
            "and":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=D&M\n",
            "or":"@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=D|M\n",
            "not":"@SP\nA=M-1\nM=!M\n",
            "push":"{m_arg}@SP\nM=M+1\nA=M-1\nM=D\n",
            "pop":"{m_arg}D=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
            "label":"({l_arg})\n",
            "goto":"@{l_arg}\n0;JMP\n",
            "if-goto":"@SP\nAM=M-1\nD=M\n@{l_arg}\nD;JNE\n",
            "function":"({f_arg})\n",
            "call":"@{r_address}\nD=A\n@SP\nM=M+1\nA=M-1\nM=D\n@LCL\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@ARG\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@THIS\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@THAT\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@SP\nD=M\n@5\nD=D-A\n@{arg2}\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@{c_arg}\n0;JMP\n({r_address})\n",
            "return":"@LCL\nD=M\n@R14\nM=D\n@R5\nA=D-A\nD=M\n@R15\nM=D\n@ARG\nAD=M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n@R14\nAM=M-1\nD=M\n@THAT\nM=D\n@R14\nAM=M-1\nD=M\n@THIS\nM=D\n@R14\nAM=M-1\nD=M\n@ARG\nM=D\n@R14\nAM=M-1\nD=M\n@LCL\nM=D\n@R15\nA=M\n0;JMP\n"
        }
        self.arguments={
            None:"",
            "argument":"@ARG\nD=M\n@{arg2}\nA=D+A\nD=M\n",
            "local":"@LCL\nD=M\n@{arg2}\nA=D+A\nD=M\n",
            "static":"@{s_arg}\nD=M\n",
            "constant":"@{arg2}\nD=A\n",
            "this":"@THIS\nD=M\n@{arg2}\nA=D+A\nD=M\n",
            "that":"@THAT\nD=M\n@{arg2}\nA=D+A\nD=M\n",
            "pointer":"@R3\nD=A\n@{arg2}\nA=D+A\nD=M\n",
            "temp":"@R5\nD=A\n@{arg2}\nA=D+A\nD=M\n"
        }
        self.label_number=0
    def folder_search(self):
        for item in listdir(self.file_path):
            if ".vm" in item:
                self.files.append(self.file_path+"\\"+item)
    def parser_module(self):
        if self.is_folder:
            self.folder_search()
        for file in self.files:
            file_content=open(file)
            file_array=[]
            for line in file_content:
                command=[None,None,None]
                line=line[:line.find("//")]
                line = line.strip()
                if line =="":
                     continue
                line_array=line.split()
                for index in range(len(line_array)):
                    command[index]=line_array[index]
                file_array.append(command)
            self.files_content.append(file_array)
            file_content.close()
    def code_writer_module(self):
        file_path=self.file_path+"\\"+self.file_path.split("\\")[-1]
        bootstrap_code="@256\nD=A\n@SP\nM=D\n@BOOT\nD=A\n@SP\nM=M+1\nA=M-1\nM=D\n@LCL\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@ARG\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@THIS\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@THAT\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n@SP\nD=M\n@5\nD=D-A\n@0\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@Sys.init\n0;JMP\n(BOOT)\n"
        if not self.is_folder:
            file_path=self.file_path[:file_path.find(".")]
            bootstrap_code=""
        assembly_file=open(file_path+".asm","w")
        assembly_file.write(bootstrap_code)
        for file in range(len(self.files_content)):
            current_function=""
            for line in self.files_content[file]:
                assembly_command=self.assembly_commands[line[0]]
                if line[0]=="function":
                    current_function=line[1]
                    assembly_command=assembly_command.format(f_arg=line[1])+"@SP\nM=M+1\nA=M-1\nM=0\n"*int(line[2])
                elif "m_arg" in assembly_command:
                    m_argument=self.arguments[line[1]]
                    if line[1] == "static":
                        current_file=self.files[file].split("\\")[-1]
                        m_argument=m_argument.format(s_arg=current_file[:current_file.find(".")]+"."+line[2])
                    else:
                        m_argument=m_argument.format(arg2=line[2])
                    assembly_command=assembly_command.format(m_arg=m_argument)
                elif "l_arg" in assembly_command:
                    assembly_command=assembly_command.format(l_arg=current_function+"$"+line[1])
                elif "c_arg" in assembly_command:
                    assembly_command=assembly_command.format(r_address="RETURN"+str(self.label_number),arg2=line[2],c_arg=line[1])
                    self.label_number+=1
                else:
                    assembly_command=assembly_command.format(number=str(self.label_number))
                    self.label_number+=1
                assembly_file.write(assembly_command)
        assembly_file.close()

if __name__ == "__main__":
    a=VirtualMachineCompiler(input("Enter path: "))
    a.parser_module()
    a.code_writer_module()
