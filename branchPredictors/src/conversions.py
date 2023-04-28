import numpy as np

class InvalidPositArgException (Exception):
    pass

class ValueException (Exception):
    pass

class BinaryOperations():
    def _init_(self) -> None:
        pass

    def twosComplement(binaryNumber):
        n=len(binaryNumber)
        i = n - 1
        while(i >= 0):
            if (binaryNumber[i] == '1'):
                break
            i -= 1
        if (i == -1):
            return '1'+ binaryNumber
 
        k = i - 1
        while(k >= 0):
            if (binaryNumber[k] == '1'):
                binaryNumber = list(binaryNumber)
                binaryNumber[k] = '0'
                binaryNumber = ''.join(binaryNumber)
            else:
                binaryNumber = list(binaryNumber)
                binaryNumber[k] = '1'
                binaryNumber = ''.join(binaryNumber)
    
            k -= 1

        return binaryNumber  

        

class Conversions():
    def _init_(self) -> None:
        pass

    def decimal2bin(decimal_number):
        binary=""
        if (decimal_number<0):
            bin_str = bin(abs(decimal_number))
            binary=bin_str.replace("0b", "")
            binary=BinaryOperations.twosComplement(binary)
        else:
            bin_str=bin(decimal_number)
            binary=bin_str.replace("0b", "")

        return binary

        
    def float2bin(float_number,num_bits):
        cadena_final=""
        value= str(float_number)
        for i in range(0,num_bits):

            el_punto=value.find(".")
            value_arr= float("0."+value[el_punto+1::])
            result= value_arr*2
            front_point = str(int(result))
            cadena_final=cadena_final+front_point

            el_punto2=(str(result)).find(".")
            value= str("0."+str(result)[el_punto2+1::])

        return cadena_final
    
    def binary_to_decimal(string_binary):
        posicion = 0
        decimal = 0
        string_binary = string_binary[::-1]
        for digito in string_binary:
            # Elevar 2 a la posición actual
            multiplicador = 2**posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal
    
    def binary_to_significant(string_binary):
        posicion = 1
        significant = 0
        for digito in string_binary:
            # Elevar 2 a la posición actual
            multiplicador = 2**(-1*posicion)
            significant += int(digito) * multiplicador
            posicion += 1
        return significant
    
    def format2bits(string_binary):
        binary_format="00"
        if (len(string_binary) ==1):
            binary_format="0"+string_binary
        else:
            binary_format=string_binary
        return binary_format
            
   

def sign(decimal):
        if decimal<0 :
            return 1
        else:
            return 0

class Configfiles():
    def _init_(self) -> None:
        pass

    def removeHexaFormat(file_name, type_file_abreviation):
        with open(file_name,'r+') as original_file: #+'.'+type_file_abreviation
            with open(file_name+'_new.'+type_file_abreviation,'w') as new_file:
                lines = original_file.readlines()
                for line in lines:
                    new_line= line.replace("0x","")
                    new_file.write(new_line)
    
    def textToColumns(file_name,type_file_abreviation,delimiters):
        cant_columns=0
        with open(file_name+'.'+type_file_abreviation,'r+') as original_file:
            lines = original_file.readlines()
            for i in range(0,len(lines)):
                data_separate= lines[i].split(delimiters)
                cant_columns=len(data_separate)
                for j in range(0,cant_columns):
                    if i==0:
                        globals()[f"data_{j}"]=[]
                        if "\n" in str(data_separate[j]):
                            globals()[f"data_{j}"].append(str(data_separate[j]))
                        else:
                            globals()[f"data_{j}"].append(str(data_separate[j])+"\n")
                    else:
                        if "\n" in str(data_separate[j]):
                            globals()[f"data_{j}"].append(str(data_separate[j]))
                        else:
                            globals()[f"data_{j}"].append(str(data_separate[j])+"\n")
        
        
        for h in range(0, cant_columns):
            with open(file_name+"_"+str(h)+'.'+type_file_abreviation,'w') as f:
                f.seek(0)
                f.writelines(globals()[f"data_{h}"])
                
            


                
            

