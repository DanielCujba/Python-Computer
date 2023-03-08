from Source.Components.Sequential_Logic.RAM32K import RAM32K

class Memory(RAM32K):
    def log_memory(self):
        f=open("Source/RAM_Log.txt","w")
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    for d in range(8):
                        for e in range(8):
                            string="".join([str((int(self.ram.out[a].ram.out[b].ram.out[c].ram.out[d].registers.out[e].out[i].out))) for i in range(16)])
                            string=string+" "+str(int(string[1:16],2) if string[0]=="0" else int(string[1:16],2)-32768)+"\n"
                            f.write(string)
        f.close()
