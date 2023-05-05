from conversions import Conversions
from branchbehavior import bb
import time
import matplotlib.pyplot as plt
import random
import os


start = time.time()

#debug variables
accuracy_by_addr_width = [] #x
addw = [] #y
time_exec_by_addr_width=[] #z
cont_error=[]

#real variables
addr_width_list=[4]

for addr_width in addr_width_list:

    #real variables
    index_pht=0
    total_addr_program= 10000 #3771696 #9999 #500 #9999
    porcentage_error=0.15

    prediction=False
    was_taken=False
    activate_error_bit0=False
    activate_error_bit1=False
    position_bit=0

    #files variables
    pht_file_name="memory/pattern_history_table"
    bht_file_name="memory/branch_history_table"
    addr_program_file_name="dataset/int_1_new_0"
    real_predictions_file_name="dataset/int_1_new_1"
    
    #debug variables
    cont_lista_errores=0
    counter_error=0
    list_reg_num_error_bit0=[]
    list_reg_num_error_bit1=[]
    cant_errors=int((total_addr_program+1)*porcentage_error)
    inputNumbers =range(0,total_addr_program)
    list_reg_num_error_bit0=random.sample(inputNumbers, cant_errors)
    list_reg_num_error_bit1=random.sample(inputNumbers, cant_errors)

    #initialization
    bb.initialize(pht_file_name,'txt',2**addr_width,2)
    bb.initialize(bht_file_name,'txt',1,addr_width)

    with open(addr_program_file_name +".txt",'r+') as registros:
        with open(bht_file_name+".txt",'r+') as bht:
            with open(real_predictions_file_name+".txt",'r+') as results:
                branch_history= bht.readlines()
                lines_reg=registros.readlines()
                results_data=results.readlines()

                for i in range(0,total_addr_program):

                    #fetch addr
                    binaryreg=bin(int(lines_reg[i].replace("\n",""), 16))[2:].zfill(8)
                    decimalreg=Conversions.binary_to_decimal(binaryreg)

                    #branch predictor schemes

                    #gshare-----------------------------------------------------------------
                    # binarybht=branch_history[0].replace("\n","")
                    # decimalbht=Conversions.binary_to_decimal(binarybht)

                    # xor_decimal= decimalreg ^ decimalbht
                    # xor_binary=Conversions.decimal2bin(xor_decimal)

                    # #get index for pht 
                    # index_pht=Conversions.binary_to_decimal(xor_binary[-addr_width:])
                    #end of gshare---------------------------------------------------------


                    #bimodal---------------------------------------------------------------
                    #get index for pht 
                    index_pht=Conversions.binary_to_decimal(binaryreg[-addr_width:])
                    #end of bimodal --------------------------------------------------------
                    
                   

                    #get real values
                    result_data_str=results_data[i].replace("\n","")
                    was_taken=bool(int(result_data_str))

                    if i in list_reg_num_error_bit0:
                        cont_lista_errores+=1
                        activate_error_bit0=True
                    else:
                        activate_error_bit0=False

                    if i in list_reg_num_error_bit1:
                        cont_lista_errores+=1
                        activate_error_bit1=True
                    else:
                        activate_error_bit1=False
                    
                    #make prediction
                    prediction=bb.getPredictionFromCounter(bb,pht_file_name,index_pht,was_taken,prediction,False,False)

                    #calculate accuracy
                    if (was_taken!=prediction):
                        counter_error+=1
                    
                    #Update branch history table
                    bb.updateBranchHistoryTable(bht_file_name,was_taken,addr_width)

    accuracy_by_addr_width.append((total_addr_program+1-counter_error)/(total_addr_program+1))
    addw.append(addr_width)
    print("accuracy:",(total_addr_program+1-counter_error)/(total_addr_program+1)," addr_width:",addr_width)

    end = time.time()
    time_exec_by_addr_width.append(round(end - start, 2))
    print(end - start, "seconds")

    print(cont_lista_errores)



with open("results/results" +".txt",'r+') as finales:
    finales.seek(0, os.SEEK_END)
    finales.write("gshare, no error")
    finales.writelines(str(accuracy_by_addr_width))
    finales.writelines(str(addw))
