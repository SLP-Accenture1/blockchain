import hashlib

class AirToken:
    def __init__(self, previous_block_hash, transaction_list):
        
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
 
t1 = "Log Maintenance Details"
t2 = "Date: "
t3 = "Aircraft: "
t4 = "Recording Tach Time: "
t5 = "Today's Flight: "
t6 = "Total Time in Service: "
t7 = "Name of Logger: "
t8 = "Certificate No. of Technician or Repair Facility: "
t9 = "Description of Inspections, Tests, Repairs and Alterations: "
t10 = "Parts replaced/fixed/upgraded: "

print(" ")

x = input("Type 'x' to exit the program ")

count = 0

while(x != 'x'): 

    hash = "firstblock"

    if(count == 0):

        date = input(t2)
        t2 = t2 + date

        aircraft = input(t3)
        t3 = t3 + aircraft

        tachTime = input(t4)
        t4 = t4 + tachTime

        todayFlight = input(t5)
        t5 = t5 + todayFlight

        serviceTime = input(t6)
        t6 = t6 + serviceTime

        logger = input(t7)
        t7 = t7 + logger

        credential = input(t8)
        t8 = t8 + credential

        description = input(t9)
        t9 = t9 + description

        parts = input(t10)
        t10 = t10 + parts

        block1 = AirToken('firstblock', [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10])
        print("Block 1 data: " + block1.block_data + "\n")
        print("Block 1 hash: " + block1.block_hash + "\n")
        hash = block1.block_hash

    else:
        t1 = "Log Maintenance Details"
        t2 = "Date: "
        t3 = "Aircraft: "
        t4 = "Recording Tach Time: "
        t5 = "Today's Flight: "
        t6 = "Total Time in Service: "
        t7 = "Name of Logger: "
        t8 = "Certificate No. of Technician or Repair Facility: "
        t9 = "Description of Inspections, Tests, Repairs and Alterations: "
        t10 = "Parts replaced/fixed/upgraded: "

        date = input(t2)
        t2 = t2 + date

        aircraft = input(t3)
        t3 = t3 + aircraft

        tachTime = input(t4)
        t4 = t4 + tachTime

        todayFlight = input(t5)
        t5 = t5 + todayFlight

        serviceTime = input(t6)
        t6 = t6 + serviceTime

        logger = input(t7)
        t7 = t7 + logger

        credential = input(t8)
        t8 = t8 + credential

        description = input(t9)
        t9 = t9 + description

        parts = input(t10)
        t10 = t10 + parts

        hash = block1.block_hash
        block1 = AirToken(hash, [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10])
        print("Block 2 data: " + block1.block_data + "\n")
        print("Block 2 hash: " + block1.block_hash + "\n")
        
    count = count+1

    x = input("Type 'x' to exit the program ")