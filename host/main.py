
path = './raw/'
path_out = './data/'
raw_list = ['ssupervisor_ping.txt', 'ssupervisor_sinfo3.txt','ssupervisor_dfh1.txt','ssupervisor_sinfo1.txt','ssupervisor_sinfo2.txt','ssupervisor_squeue1.txt']
raw_list_email = ['ssupervisor_ping.txt', 'ssupervisor_sinfo3.txt']


while True:
	data_dictionary = readRaw(raw_list,raw_list_email,path,path_out)	
	
	downnodes = data_dictionary['email_dictionary'].get('ssupervisor_sinfo3',0)
	pingresult = data_dictionary['email_dictionary'].get('ssupervisor_ping',None)
	
	