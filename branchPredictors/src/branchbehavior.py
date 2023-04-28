from conversions import Conversions

class InvalidLength (Exception):
    print("Out of length")
    pass

class bb():
    def _init_(self) -> None:
        pass

    def initialize(file_name,type_text,lines, bits):
        """
        Initialize in zero the registers depending on the amount of lines and bit that the register has.
        """
        with open(file_name+'.'+type_text,'w') as file:
            lista=[]
            for i in range (0,lines):
                data=""
                for j in range(0,bits):
                    data=data+"0"
                if (lines==1):
                    file.write(data)
                else:
                    file.write(data+"\n")

    def insertErrorbit(binary_number, position_bit,activate_error):
        """
        Flips a bit in a especific position from a binary number.
        """
        random_bit=int(not (bool(int(binary_number[position_bit]))))
        binary_number_out=""
        if(activate_error):
            if(len(binary_number)>=position_bit):
                binary_number_out= binary_number[0:position_bit]+str(random_bit)+binary_number[position_bit+1::]
            else:
                binary_number_out=binary_number
                raise InvalidLength()         
        else:
            binary_number_out=binary_number

        return binary_number_out

    def getPredictionFromCounter(self,pht_file,index_pht,was_taken,prediction,activate_error_bit0, activate_error_bit1):
        """
        From the pattern history file checks the counter and define a prediction.
        """
        is_wrong=was_taken ^ prediction
        flag_branch_taken=False
        with open(pht_file+'.txt','r+') as f:
            lines = f.readlines()    
            pht_reg_bin=lines[index_pht].split('\n')[0]

            pht_reg_bin=self.insertErrorbit(pht_reg_bin,0,activate_error_bit0)
            pht_reg_bin=self.insertErrorbit(pht_reg_bin,1,activate_error_bit1)

            pht_reg_int=Conversions.binary_to_decimal(pht_reg_bin)

            flag_st3= pht_reg_int<3 #flag when reg is smaller than 3
            flag_bt0= pht_reg_int>0 #flag when reg is bigger than 0

            if (is_wrong):
                if(flag_st3 and was_taken):
                    pht_reg_int+=1
                elif (flag_bt0 and not was_taken):
                    pht_reg_int-=1
                pht_reg_bin=Conversions.decimal2bin(pht_reg_int)
                f.seek(0)
                lines[index_pht]=Conversions.format2bits(pht_reg_bin) +'\n'
                f.writelines(lines)  
            flag_branch_taken= bool(int(lines[index_pht][0]))

        return flag_branch_taken

    def updateBranchHistoryTable(bht_file,was_taken,addr_width):
        """
        Updates the branch history table, adds one bit at the end.
        """
        with open(bht_file+'.txt','r+') as bht:
            bht.seek(0)
            lines= bht.readlines()
            if was_taken:
                lines[0]=lines[0] + "1"
            else:
                lines[0]=lines[0] + "0"
        
            if (len(lines[0])>addr_width):
                lines[0]=lines[0][-addr_width:]
                new_data= lines
            else:
                new_data= lines

            bht.seek(0)
            bht.writelines(new_data)