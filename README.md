# Bank-Queue
Problem description:
            There are 'n' peoples standing outside the bank to put cash into their accounts,after increased the interest rates by 42%.Bank manager makes decision he picks up some people in the queue,total amount of cash of that people is big as possible.All people have some other jobs to do,not much time to spend on standing in the queue.
            And there is only one counter is open on the bank,it takes 1 minute for 1 person to put cash.Bank manager will serve the selected people before they leave also they had more money to put.
      
Input:
4 4
1000 1
2000 2
500 2
1200 0
Task:
      Our aim is to help the manager to take more money from the selected people according to their waiting time.
  
Input definition:
            First 4 defines no.of peoples in the queue,second 4 is that much time only bank will open,after 4 minutes bank closes.
            1000 is first person's amount and after space 1 minute is that person's waiting time,after that he leaves the bank
            
 Logic:
          Taking 1 list appending the cost in the list ,where to append in the list is(i.e Index is) people's waiting time ,if the cost is already in the list don't take that cost (that person leaves tha bank).
                      
 Output:
        4200
 Adding according to my logic-->1200+1000+2000=4200.
