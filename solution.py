# first let's take an input and organize it into a suitable data type 
number_wires=int(input())
number_of_birds=list(map(int,input().split()))
number_of_shoots=int(input())
pos_shot=[]
for i in range(number_of_shoots):
    bird_pos=tuple(map(int,input().split()))
    pos_shot.append(bird_pos)
def main_func(number_of_birds,pos_shot,number_of_shoots):
   
    for i in range(number_of_shoots):
        wire,bird=pos_shot[i]
       
        index=wire-1
        left_bird=bird-1
        right_bird=number_of_birds[index]-bird 
        
        if index-1>=0 :
            number_of_birds[index-1]+=left_bird
        if index+1<len(number_of_birds) :
            number_of_birds[index+1]+=right_bird
        number_of_birds[index]=0
        
    for i in number_of_birds:
        print(i)
main_func(number_of_birds,pos_shot,number_of_shoots)
        
    
    
