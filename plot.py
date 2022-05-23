# Script_plot
# To execute follow this: $ python3 nist_2_plot_risk.py library_name.csv
# wait seconds and look the plot in image PNG at the current cirectory of script
# Coded by CoolerVoid
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

def main():
 hashlist= { 'Critical':0, 'High':0, 'Medium':0, 'Low':0}
 count = 0
 rule1=False
	
 input_file=sys.argv[1]
 file1 = open(input_file,  'r',encoding="utf8", errors='ignore')
 Lines = file1.readlines()

 for line in Lines:
  str_line=str(line)
  lists=str_line.split('|')
  # split CSV pattern in chunks like Hack the ripper: "name|datetime|cve|url|risk1|risk2|description\n"
  name=lists[0]
  datetime=lists[1]
  cve=lists[2]
  url=lists[3]
  risk1=lists[4]
  risk2=str(lists[5])
	 
  if "NULL" in risk2:
   risk2=risk1
   
  if "LOW" in risk2: 
   hashlist['Low']+=1
		    
  if "MEDIUM" in risk2: 
   hashlist['Medium']+=1
		    
  if "HIGH" in risk2: 
   hashlist['High']+=1
		    
  if "CRITICAL" in risk2: 
   hashlist['Critical']+=1
  count += 1


 print("Risk table list:")
 print(hashlist)

 values_list=list(hashlist.values())
 keys_list=list(hashlist.keys())
 y_pos = np.arange(len(keys_list))

 # Create horizontal bars, share array of numbers
 plt.barh(y_pos, values_list,color=['red', 'orange', 'yellow', 'green'],align='center')
	 
 # Create names on the x-axis, share array of names
 plt.yticks(y_pos, keys_list)
	 
 # render image and save. Note: 
 # I prefer GnuPlot...    ^¯\_(ツ)_/¯^
 input_file_img=input_file.replace(".csv","_risk.png")
 plt.rcParams['font.size'] = '10'
 plt.ylabel('Risk levels ')
 plt.xlabel('Total risk for last '+str(count)+' issues')
 fig = plt.gcf(); 
 fig.suptitle("Overview in "+input_file+" risk")
 fig.tight_layout()
 fig.savefig(input_file_img,format='png',dpi=800)
#fig.close(input_file_img)

if __name__=="__main__":
    try:
        # TODO add clean arg parse or getopt and soon
        if len(sys.argv[1])<=0:
         print("Error!\n Please follow the example:\n$ python3 plot.py list.csv\n")
         exit(0)
        main()
    except Exception as e:
        traceback.print_exc()
        print(" log error in config parser rules: "+str(e))
        exit(0)
    main()
