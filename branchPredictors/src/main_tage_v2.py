from conversions import Conversions
from branchbehavior import bb
import time
import matplotlib.pyplot as plt
import random
import os



#update tag
def updateTaginTable(file_tag_name, index_tag, tag):
    with open(file_tag_name +".txt",'r+') as reg_tag:
        lines = reg_tag.readlines()  
        reg_tag.seek(0)
        lines[index_tag]=tag+"\n"
        reg_tag.writelines(lines)

def updateUcounter(file_u_name,index_tag, reset):
    with open(file_u_name +".txt",'r+') as reg_u:
        lines = reg_u.readlines()   
        decimal_u_counter=Conversions.binary_to_decimal(lines[index_tag].replace("\n","")) 

        if (reset):
            decimal_u_counter=0
        else:
            if(decimal_u_counter<3):
                decimal_u_counter+=1
        binary_u_counter=Conversions.decimal2bin(decimal_u_counter)

        reg_u.seek(0)
        lines[index_tag]=binary_u_counter+"\n"
        reg_u.writelines(lines)

def getUcounter(file_u_name,index_tag):
    with open(file_u_name +".txt",'r+') as reg_u:
        update_tag=False
        lines = reg_u.readlines()   
        decimal_u_counter=Conversions.binary_to_decimal(lines[index_tag].replace("\n","")) 

        if decimal_u_counter>0:
            update_tag=False
        else:
            update_tag=True

        return update_tag

def getTag(file_tag_name, index_tag):
    with open(file_tag_name +".txt",'r+') as reg_tag:
        lines = reg_tag.readlines()  
        return lines[index_tag].replace("\n","")
    



start = time.time()

#debug variables
accuracy_by_addr_width = [] #x
addw = [] #y
time_exec_by_addr_width=[] #z
cont_error=[]

#real variables
addr_width_list=[16]
#tage variables
addr_bht_width=32
addr_tag_width=16

for addr_width in addr_width_list:

    #real variables
    index_pht=0
    total_addr_program=10000 #3771696 #9999 #500 #9999
    porcentage_error=0.15

    prediction=False

    #tage variables
    prediction_1=False
    prediction_2=False
    index_pht_tags=0

    was_taken=False
    activate_error_bit0=False
    activate_error_bit1=False
    position_bit=0

    #files variables
    pht_file_name="memory/pattern_history_table"
    bht_file_name="memory/branch_history_table"
    addr_program_file_name="dataset/int_1_new_0"
    real_predictions_file_name="dataset/int_1_new_1"

    #tage variables
    pht_file_name_1="memory/pattern_history_table_1"
    pht_file_name_2="memory/pattern_history_table_2"
    tag_file_name_1="memory/tag1"
    tag_file_name_2="memory/tag2"
    u_file_name_1="memory/u1"
    u_file_name_2="memory/u2"

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
    bb.initialize(bht_file_name,'txt',1,addr_bht_width)

    #initialization tage 
    bb.initialize(pht_file_name_1,'txt',2**addr_width,2)
    bb.initialize(pht_file_name_2,'txt',2**addr_width,2)
    bb.initialize(tag_file_name_1,'txt',2**addr_width,addr_tag_width)
    bb.initialize(tag_file_name_2,'txt',2**addr_width,addr_tag_width)
    bb.initialize(u_file_name_1,'txt',2**addr_width,2)
    bb.initialize(u_file_name_2,'txt',2**addr_width,2)


    #por las dudas
    cont_tag_2=0
    with open(addr_program_file_name +".txt",'r+') as registros:
        with open(bht_file_name+".txt",'r+') as bht:
            with open(real_predictions_file_name+".txt",'r+') as results:
                branch_history= bht.readlines()
                lines_reg=registros.readlines()
                results_data=results.readlines()

                for i in range(0,total_addr_program):
                    
                    bht.seek(0)
                    branch_history=bht.readlines()
                    #print(results_data[i])

                    #fetch addr
                    binaryreg=bin(int(lines_reg[i].replace("\n",""), 16))[2:].zfill(8)
                    decimalreg=Conversions.binary_to_decimal(binaryreg)

                    #branch predictor schemes

                    #gshare-----------------------------------------------------------------
                    #binarybht=branch_history[0].replace("\n","")
                    #decimalbht=Conversions.binary_to_decimal(binarybht)

                    # xor_decimal= decimalreg ^ decimalbht
                    # xor_binary=Conversions.decimal2bin(xor_decimal)

                    # #get index for pht 
                    # index_pht=Conversions.binary_to_decimal(xor_binary[-addr_width:])
                    #end of gshare---------------------------------------------------------


                    #bimodal---------------------------------------------------------------
                    #get index for pht 
                    index_pht=Conversions.binary_to_decimal(binaryreg[-addr_width:])
                    #end of bimodal --------------------------------------------------------


                    #print("index", index_pht)

                    #tage-------------------------------------------------------------------
                    binarybht=branch_history[0].replace("\n","")
                    decimalbht=Conversions.binary_to_decimal(binarybht)

                    xor_decimal= decimalreg ^ decimalbht
                    xor_binary=Conversions.decimal2bin(xor_decimal) #this is always my index
                    

                    #create tags
                    #tag 1 and tag2
                    slices_bht=[]
                    slices_pc=[]
                    for j in range(0,addr_tag_width):
                        binario_bht_temp= binarybht[addr_bht_width-addr_tag_width-(addr_tag_width*j):addr_bht_width-(j*addr_tag_width)]
                        decimal_bht_temp=Conversions.binary_to_decimal(binario_bht_temp)
                        slices_bht.append(decimal_bht_temp)

                        len_pc=len(binaryreg)
                        binario_pc_temp= binaryreg[len_pc-addr_tag_width-(addr_tag_width*j):len_pc-(j*addr_tag_width)]
                        decimal_pc_temp=Conversions.binary_to_decimal(binario_pc_temp)
                        slices_pc.append(decimal_pc_temp)
                    
                    
                    decimal_tag1=slices_bht[len(slices_bht)-1]^slices_bht[len(slices_bht)-2] ^ slices_pc[len(slices_pc)-1]^slices_pc[len(slices_pc)-2]
                    decimal_tag2= decimal_tag1^slices_bht[len(slices_bht)-3]^slices_bht[len(slices_bht)-4] ^ slices_pc[len(slices_pc)-3]^slices_pc[len(slices_pc)-4]
                    
                    binary_tag1=Conversions.decimal2bin(decimal_tag1)
                    binary_tag2=Conversions.decimal2bin(decimal_tag2)
                    

                    slices_bht=[]
                    slices_pc=[]
                    width_burn=16
                    for k in range(0,len(binarybht)):
                        binario_bht_temp= binarybht[addr_bht_width-width_burn-(width_burn*k):addr_bht_width-(k*width_burn)]
                        decimal_bht_temp=Conversions.binary_to_decimal(binario_bht_temp)
                        slices_bht.append(decimal_bht_temp)

                        len_pc=len(binaryreg)
                        binario_pc_temp= binaryreg[len_pc-width_burn-(width_burn*k):len_pc-(k*width_burn)]
                        decimal_pc_temp=Conversions.binary_to_decimal(binario_pc_temp)
                        slices_pc.append(decimal_pc_temp)
                    
                    # decimal_index_t1=slices_bht[len(slices_bht)-1]^slices_bht[len(slices_bht)-2] ^slices_bht[len(slices_bht)-3] ^ slices_pc[len(slices_pc)-1]^slices_pc[len(slices_pc)-2] ^slices_pc[len(slices_pc)-3]
                    # decimal_index_t2= decimal_tag1^slices_bht[len(slices_bht)-5]^slices_bht[len(slices_bht)-6] ^ slices_pc[len(slices_pc)-5]^slices_pc[len(slices_pc)-6]
                    
                    # decimal_index_t1=slices_bht[len(slices_bht)-1]^slices_bht[len(slices_bht)-2]  ^ slices_pc[len(slices_pc)-1]^slices_pc[len(slices_pc)-2] 
                    # decimal_index_t2= decimal_tag1^slices_bht[len(slices_bht)-3]^slices_bht[len(slices_bht)-4] ^ slices_pc[len(slices_pc)-3]^slices_pc[len(slices_pc)-4]
                    
                    decimal_index_t1=slices_bht[len(slices_bht)-1] ^ slices_pc[len(slices_pc)-1]
                    decimal_index_t2= decimal_tag1^slices_bht[len(slices_bht)-2] ^slices_pc[len(slices_pc)-2]
                    

                    index_pht_tags=Conversions.binary_to_decimal(xor_binary[-addr_width:])
                

                    u1_updatetag_bool= getUcounter(u_file_name_1,decimal_index_t1)
                    u2_updatetag_bool= getUcounter(u_file_name_2,decimal_index_t2)
                    
                    
                    tag1_from_table=getTag(tag_file_name_1,decimal_index_t1)
                    tag2_from_table=getTag(tag_file_name_2,decimal_index_t2)

                    bool_match_tag1=False
                    bool_match_tag2=False

                    if (tag1_from_table==binary_tag1):
                        bool_match_tag1=True
                    else:
                        bool_match_tag1=False

                    if (tag2_from_table==binary_tag2):
                        bool_match_tag2=True
                        cont_tag_2+=1
                    else:
                        bool_match_tag2=False

                

                    #get real values
                    #print("aqui", results_data[i])
                    result_data_str=results_data[i].replace("\n","")
                    #print(results_data[i],result_data_str)
                    was_taken=bool(int(result_data_str))
                    
                    #make prediction
                    prediction=bb.getPredictionFromCounter(bb,pht_file_name,index_pht,was_taken,prediction,False,False)

                    #print("prediction:", prediction, "was taken", was_taken )

                    if (bool_match_tag1):
                        #print("here")
                        prediction_1=bb.getPredictionFromCounter(bb,pht_file_name_1,decimal_index_t1,was_taken,prediction_1,False,False)
                        prediction=prediction_1
                    
                    if (bool_match_tag2):
                        prediction_2=bb.getPredictionFromCounter(bb,pht_file_name_2,decimal_index_t2,was_taken,prediction_2,False,False)
                        prediction=prediction_2

                    if (not bool_match_tag1 and not bool_match_tag2):
                        if (u1_updatetag_bool):
                            updateTaginTable(tag_file_name_1,decimal_index_t1,Conversions.formatByBits(binary_tag1,addr_tag_width))

                        if (u2_updatetag_bool):
                            updateTaginTable(tag_file_name_2,decimal_index_t2,Conversions.formatByBits(binary_tag2,addr_tag_width))


                    #calculate accuracy
                    if (was_taken!=prediction):
                        counter_error+=1

                    if (was_taken==prediction):
                        if(bool_match_tag2):
                            updateUcounter(u_file_name_2,decimal_index_t1,False)
                        elif(bool_match_tag1):
                            updateUcounter(u_file_name_1,decimal_index_t2,False)

                    if (i%512==0):
                        bb.initialize(u_file_name_1,'txt',2**addr_width,2)
                        bb.initialize(u_file_name_2,'txt',2**addr_width,2)

                        
                    
                    #Update branch history table
                    bb.updateBranchHistoryTable(bht_file_name,was_taken,addr_bht_width)

    accuracy_by_addr_width.append((total_addr_program+1-counter_error)/(total_addr_program+1))
    addw.append(addr_width)
    print("accuracy:",(total_addr_program+1-counter_error)/(total_addr_program+1)," addr_width:",addr_width)

    end = time.time()
    time_exec_by_addr_width.append(round(end - start, 2))
    print(end - start, "seconds")

    print(cont_lista_errores)
    print(cont_tag_2)



with open("results/results" +".txt",'r+') as finales:
    finales.seek(0, os.SEEK_END)
    finales.write("gshare, no error")
    finales.writelines(str(accuracy_by_addr_width))
    finales.writelines(str(addw))
