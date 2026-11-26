class Train:
    def __init__(self, train_no, train_name, source, destination):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination

    def display(self):
        print("Train Number:", self.train_no)
        print("Train Name:", self.train_name)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("-------------------")


t1 = Train(101, "Rajdhani Express", "Delhi", "Mumbai")
t2 = Train(102, "Shatabdi Express", "Ahmedabad", "Mumbai")
t3 = Train(103, "Vande Bharat", "Surat", "Mumbai")
t4 = Train(104, "Duronto Express", "Pune", "Delhi")
t5 = Train(105, "Garib Rath", "Jaipur", "Delhi")

t1.display()
t2.display()
t3.display()
t4.display()
t5.display()