#!/usr/bin/env python
# coding: utf-8

# In[22]:


import csv

with open('Nov-2018_kayako.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    alerter_count = 0
    critical_count = 0
    error_count = 0
    warn_count = 0
    big_list = []
    big_list_critical = []
    error_msg_list = []
    critical_host_list  = []
    for row in csv_reader:
        if row['Department'] == 'Tech Support':
            line_count += 1
        if row['Email'] == 'alerter@steadfast.logicmonitor.com':
            alerter_count += 1
            if 'critical -' in row['Subject']:
                critical_count += 1
            if 'error -' in row['Subject']:
                error_count += 1
            if 'warn -' in row['Subject']:
                warn_count += 1
            if 'LMD' in row['Subject']:
                subject = row['Subject'].split(' - ')
                if 'critical' in subject[0]:
                    big_list_critical.extend(subject)
                    host_error_msg = subject[1]
                    error_msg = ' '.join(host_error_msg.split()[1:])
                    error_msg_list.append(error_msg)
            if ('LMD' and 'critical') in row['Subject']:
                subject = row['Subject'].split(' - ')
                if 'critical' in subject[0]:
                    host_error = subject[1].split()
                    critical_host_list.append(host_error[0])                  
    
    print('List of critical error and fecuency of them\n')
    
    def frec(lista):
        frec = {}
        for i in lista:
            if i in frec:
                frec[i] += 1
            else:
                frec[i] = 1
        for k, v in frec.items():
            print('%s : %d'%(k, v))
        sum_dict_loop = sum(frec.values())
        check_sum = sum_dict_loop == critical_count
        print('Both sum are: ', check_sum)
        print('Numero de Key: ', len(frec))
        print('Fin del loop\n')
    
    frec(error_msg_list)
    frec(critical_host_list)
    print(' ')
    print('Number of LogicMonitor tickets: ' + str(line_count))
    print('Total number of tickets Nov 2018: ' + str(alerter_count))
    print('LM - critical: ' + str(critical_count))
    print('LM - error: ' + str(error_count))
    print('LM - warn: ' + str(warn_count))


# In[ ]:





# In[ ]:




