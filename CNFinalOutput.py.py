import networkx as nx
import pylab
import matplotlib.pyplot as plt
from matplotlib.pyplot import pause
pylab.ion()

import warnings
warnings.filterwarnings("ignore")
list=["Server Sends Equal Unique Parts of Data to Each Node","Nodes Disconnect from Server","Nodes Exchange data And Retransmit Error Frames","Transfer Complete"]
g = nx.MultiDiGraph()
ack=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]





def node():
    colors = []
    #weight1 = []
    progress=0
    
    for n in range(1,6):
            g.add_node(n)
    g.add_node("Server 1")
    g.add_node("Server 2")         

    for i in range(1,13):
        pos=nx.spring_layout(g)
    

        if i == 1:
            g.add_edge("Server 1",1,color='g',weight=3)
            
           
           
            ack[0][0]=1
            g.add_edge("Server 1",2,color='g',weight=3)
            
           
            ack[1][1]=1
            g.add_edge("Server 1",3,color='g',weight=3)
            ack[2][2]=1
            g.add_edge("Server 2",4,color='g',weight=3) 
            ack[3][3]=1
            g.add_edge("Server 2",5,color='g',weight=3)
            ack[4][4]=1
            g.add_edge("Server 2",6,color='g',weight=3)
            ack[5][5]=1

            
            
        
        if i == 2:
            g.remove_edge("Server 1",1)
            g.remove_edge("Server 1",2)
            g.remove_edge("Server 1",3)
            g.remove_edge("Server 2",4)          
            g.remove_edge("Server 2",5) 
            g.remove_edge("Server 2",6) 
            g.remove_node("Server 1")
            g.remove_node("Server 2")
           
            
        if i==3:
            g.add_edge(1,2,color='g',weight=8)
            ack[1][0]=1
            g.add_edge(2,4,color='r',weight=8)
            
            g.add_edge(5,3,color='g',weight=8)
            ack[2][4]=1
            g.add_edge(2,3,color='g',weight=8)
            ack[2][1]=1
            g.add_edge(6,5,color='g',weight=8)
            ack[4][5]=1
            g.add_edge(4,1,color='r',weight=8)
            g.add_edge(3,6,color='g',weight=8)
            ack[5][2]=1
            progress+=1
            
        if i==4:
            g.remove_edge(1,2)
            g.remove_edge(2,3)
            #g.remove_edge(2,4)
            g.remove_edge(5,3)
            g.remove_edge(6,5)
           # g.remove_edge(4,1)
            g.remove_edge(3,6)
            
        if i==5:    
            g.remove_edge(4,1)
            ack[0][3]=1
            g.remove_edge(2,4)
            ack[3][1]=1
            
            g.add_edge(2,1,color='g',weight=4)
            ack[0][1]=1
            g.add_edge(3,4,color='g',weight=4)
            ack[3][2]=1
            g.add_edge(1,6,color='r',weight=4)
            g.add_edge(6,4,color='r',weight=4)
            g.add_edge(5,4,color='g',weight=4)
            ack[3][4]=1
            g.add_edge(4,2,color='g',weight=4)
            ack[1][3]=1
            
            progress+=1
           
  
        if i==6:    
            g.remove_edge(2,1)
            g.remove_edge(3,4)
           # g.remove_edge(1,6)
            #g.remove_edge(6,4)
            g.remove_edge(5,4)
            g.remove_edge(4,2)
            
            
            
        if i==7:
            g.remove_edge(1,6)
            g.remove_edge(6,4)
            ack[5][0]=1
            ack[3][5]=1
            
            g.add_edge(1,3,color='g',weight=4)
            ack[2][0]=1
            g.add_edge(2,5,color='g',weight=4)
            ack[4][1]=1
            g.add_edge(3,2,color='r',weight=4)
            g.add_edge(4,3,color='r',weight=4)
            g.add_edge(5,2,color='r',weight=4)
            g.add_edge(6,3,color='g',weight=4)
            ack[2][5]=1
            progress+=1
           
  
        if i==8:    
            g.remove_edge(1,3)
            g.remove_edge(2,5)
            #g.remove_edge(3,2)
            #g.remove_edge(4,3)
            #g.remove_edge(5,2)
            g.remove_edge(6,3) 
            
            
            
            
        if i==9:  
            g.remove_edge(3,2)
            ack[1][2]=1
            g.remove_edge(4,3)
            ack[2][3]=1
            g.remove_edge(5,2)
            ack[1][4]=1
            g.add_edge(4,5,color='r',weight=4)
            
            g.add_edge(1,4,color='g',weight=4)
            ack[3][0]=1
            g.add_edge(2,4,color='g',weight=4)
            ack[3][1]=1
            g.add_edge(6,1,color='g',weight=4)
            ack[0][5]=1
            g.add_edge(5,6,color='g',weight=4)
            ack[5][4]=1
            g.add_edge(3,5,color='g',weight=4)    
            ack[4][2]=1
            progress+=1
           
  
        if i==10:    
           
            g.remove_edge(1,4)
            g.remove_edge(2,4)
            g.remove_edge(6,1)
            g.remove_edge(5,6)
            g.remove_edge(3,5)
            
            
            
        if i==11: 
            g.remove_edge(4,5)
            ack[4][3]=1
            g.add_edge(5,1,color='g',weight=4)
            ack[0][4]=1
            g.add_edge(1,5,color='g',weight=4)
            ack[4][0]=1
            g.add_edge(2,6,color='g',weight=4)
            ack[5][1]=1
            g.add_edge(3,1,color='g',weight=4)
            ack[0][2]=1
            g.add_edge(4,6,color='g',weight=4)
            ack[5][3]=1
            g.add_edge(6,2,color='g',weight=4)  
            ack[1][5]=1
            g.add_edge(1,5,color='g',weight=4)  
            ack[4][0]=1
            g.add_edge(3,1,color='g',weight=4)  
            ack[0][2]=1
            progress+=1
           
  
        if i==12:    
            g.remove_edge(5,1)
            g.remove_edge(1,5)
            g.remove_edge(2,6)
            g.remove_edge(3,1)
            g.remove_edge(4,6)
            g.remove_edge(6,2)
            g.remove_edge(1,5) 
            g.remove_edge(3,1) 
            
            
            
            

        
        plt.clf()
        colors = []
        #weight1 = []
        

        for (u,v,attrib_dict) in (g.edges.data()):
            colors.append(attrib_dict['color'])
            #weight1.append(attrib_dict['weight'])
            
        if i < 3:
          plt.title(list[i-1])
        elif i==12:  
          plt.title(list[3])  
          
        else:
          plt.title(list[2]) 
        c=0
        plt.text(1,0,s='Green=Successful Transmission\nRed=Unsuccesful Transmission' ,bbox=dict(facecolor='green', alpha=0.5))
        if  i>=3:
             for j in range(1,7):
                    x,y=pos[j]
                    c=c+0.1
                    #plt.text(x,y+0.1,s='Progress='+str(progress)+'/5', bbox=dict(facecolor='green', alpha=0.5),horizontalalignment='center')
                    plt.text(1,1-c,s='Node No. '+str(j)+' Ack Array='+str(ack[j-1]), bbox=dict(facecolor='green', alpha=0.5))

          
          
  
        if i==12:
            nx.draw(g, pos=nx.circular_layout(g),with_labels=True,node_color='#03fc07',edge_color=colors)
                    
        else:           
             nx.draw(g, pos=nx.circular_layout(g), with_labels=True,edge_color=colors)        
        pause(5)
        pylab.show()
        #pylab.savefig("output{y}.png".format(y=i))
        
        
        
if __name__ == '__main__':
     node()
     