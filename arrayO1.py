storage=[]	# array for storing values
deleted=[]	# array for deleted indexes
next_indexes=[]  # array for indexes of greater elements
prev_indexes=[]  # arrays for indexes of smaller elements
max_value_index=-1
min_value_index=-1

def addElement(el):
	global deleted
	global storage
	global max_value_index
	global min_value_index
	global next_indexes
	global prev_indexes
	
	if len(deleted)>0:
		ind = deleted.pop()
		storage[ind] = el
	else:
		storage.append(el)
		ind = len(storage)-1
		next_indexes.append(ind)
		prev_indexes.append(ind)
	
	if max_value_index==-1:
		max_value_index=ind
		min_value_index=ind
		return ind
	
	if storage[max_value_index] <= el:
		next_indexes[max_value_index]=ind
		prev_indexes[ind]=max_value_index
		
		max_value_index = ind
		return ind
		
	if storage[min_value_index] >= el:
		prev_indexes[min_value_index]=ind
		next_indexes[ind]=min_value_index
		
		min_value_index = ind
		return ind

	ind_next = min_value_index
	while ind_next != max_value_index:
		if storage[ind_next]<=storage[ind] and storage[next_indexes[ind_next]]>=storage[ind]:
			next_indexes[ind]=next_indexes[ind_next]
			next_indexes[ind_next]=ind
			
			prev_indexes[ind]=ind_next
			prev_indexes[next_indexes[ind_next]]=ind
			break
			
		ind_next=next_indexes[ind_next]
	
	return ind
	
def deleteElement(ind):
	global deleted
	global storage
	global max_value_index
	global min_value_index
	global next_indexes
	global prev_indexes
	
	if storage[ind]==-1:
		return -1
	
	storage[ind]=-1
	deleted.append(ind)
	
	if min_value_index==max_value_index:
		min_value_index=-1
		max_value_index=-1
		return ind
	if ind==min_value_index:
		min_value_index=next_indexes[min_value_index]
		return ind
	if ind==max_value_index
		max_value_index=prev_indexes[max_value_index]
		return ind
	
	next_indexes[prev_indexes[ind]]=next_indexes[ind]
	prev_indexes[next_indexes[ind]]=prev_indexes[ind]
	return ind
	
def deleteMaxElement():
	ind = deleteElement(max_value_index)
	return ind
	
def deleteMinElement():
	ind = deleteElement(min_value_index)
	return ind