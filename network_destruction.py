
def destroy_node(mygraph,nodekey): 
    temp_copy=mygraph[nodekey].copy() #temporarily create a copy of the graph,so delete works correctly
    for neighbor_nodes in temp_copy: 
             mygraph[neighbor_nodes].remove(nodekey)
    del adjacency_list[nodekey]

#uball(i,r)=set of nodes whose shortest path from node i is exactly r.
def uBall(mygraph,node,radius): 
    list_of_neighbors=[] 
    tempset=set() 
    list_of_neighbors.append([node]) 
    for r in range(0,radius):
        tempset=set() 
        for mynode in list_of_neighbors[r]:   
            for mynode_neighbors in mygraph[mynode]:
                tempset.add(mynode_neighbors)
        list_of_neighbors.append(list(tempset)) 
    for i in range(0,radius-1): 
        for elements_to_be_deleted in list_of_neighbors[i]:
            try:
                list_of_neighbors[radius-1].remove(elements_to_be_deleted)
            except:
                pass
    return list_of_neighbors[radius-1]
        
#create a list of the collective influence of each node
def create_score_list(adjacency_list,radius): 
    total_score_list=[]
    for mynode in adjacency_list:
        list_of_uball=uBall(adjacency_list,mynode,radius+1) 
        total_kj=0 
        for uball_nodes in list_of_uball:
            total_kj=total_kj+len(adjacency_list[uball_nodes])-1 
        ki=len(adjacency_list[mynode])
        total_score= (ki-1)*total_kj
        total_score_list.append([total_score,mynode])
    return total_score_list 
        
        
            

#create the graph from file.
input_file=input("name of file to create graph:")
adjacency_list={} 
myfile=open(input_file) 
for line in myfile:
    linestr=line.split() 
    try:
        adjacency_list[linestr[0]].add(linestr[1])
    except:
        adjacency_list[linestr[0]]=set()
        adjacency_list[linestr[0]].add(linestr[1])
    try:
        adjacency_list[linestr[1]].add(linestr[0])
    except:
        adjacency_list[linestr[1]]=set()
        adjacency_list[linestr[1]].add(linestr[0])
myfile.close()

#collective influence
radius=int(input("radius of ball:")) 
number_of_nodes_to_del=int(input("number of nodes to delete:"))
for i in range(0,number_of_nodes_to_del):
    score_list=create_score_list(adjacency_list,radius) 
    score_list.sort(key=lambda x: (x[0],-int(x[1])),reverse=True)
    print("destroying node:",score_list[0][1],"with collective influence:",score_list[0][0]) 
    destroy_node(adjacency_list,score_list[0][1])    
    

