import argparse
def find_max_connections(mygraph): 
    tempkeylist=set() 
    maxvalue=-1 
    for element in mygraph:
        if len(mygraph[element])>maxvalue: 
            maxvalue=len(mygraph[element])
            tempkeylist=set() 
            tempkeylist.add(int(element)) 
        if len(mygraph[element])==maxvalue:
            tempkeylist.add(int(element))
    return tempkeylist

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
        
        
            
            
    
parser=argparse.ArgumentParser()
parser.add_argument("-c",action="store_true") 
parser.add_argument("-r",action="append") 
parser.add_argument("number_of_nodes",type=int) 
parser.add_argument("input_file") 
args=parser.parse_args()



adjacency_list={} 
myfile=open(args.input_file) 
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


if args.c: #influence= number of connections of a node
    for i in range(0,args.number_of_nodes): 
        minkey=min(find_max_connections(adjacency_list))
        print(minkey,len(adjacency_list[str(minkey)])) 
        destroy_node(adjacency_list,str(minkey)) 
else:#influnce= collective influence of a node
    radius=int(args.r[0]) 
    for i in range(0,args.number_of_nodes):
        score_list=create_score_list(adjacency_list,radius) 
        score_list.sort(key=lambda x: (x[0],-int(x[1])),reverse=True)
        print(score_list[0][1],score_list[0][0]) 
        destroy_node(adjacency_list,score_list[0][1])
        
    

