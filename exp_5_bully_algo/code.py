class Process:
    def __init__(self, _id, is_alive):
        self.id = _id
        self.is_alive = is_alive
        self.status = "active" if is_alive else "inactive"

class BullyAlgorithm:
   def __init__(self, n, processes):
     self.n = n
     self.processes = processes
     self.messages = []
     self.responses = []

   def initiate_election(self, initiator_id, is_initiator):
      self.messages.append(f"\nProcess with ID {initiator_id} initiates the election!")
      election_messages = []
      for i in range(initiator_id + 1, self.n + 1):
         if i <= self.n:
            election_messages.append((initiator_id, i))
            self.messages.append(f"Process {initiator_id} sends Election({initiator_id}) message to process {i}")
            
      for sender, receiver in election_messages:
         if self.processes[receiver- 1].is_alive:
            if not is_initiator or (is_initiator and receiver != initiator_id):
               self.responses.append((receiver, initiator_id))
    
      if self.responses:
         elected_coord = max(self.responses)[0]
      else:
         elected_coord = initiator_id
      
      return elected_coord
   
   def run_election(self, initiator_id):
      elected_coord = initiator_id
      
      for i in range(initiator_id- 1, self.n):
         if self.processes[i].is_alive:
            if self.processes[i].id != initiator_id:
               elected_coord = self.initiate_election(self.processes[i].id, False)
            else:
               elected_coord = self.initiate_election(initiator_id, True)
      print('\n'.join(self.messages))
      print("\nResponses:")
      for response in self.responses:
         print(f"Process {response[0]} responds with OK({response[1]}) message")
      print(f"\nProcess {elected_coord} becomes the Coordinator!")


if __name__ == "__main__":
   n =int(input("Enter the total number of processes: "))
   binary_string = input("Enter the binary string indicating which processes are alive (1) or dead (0): ")
   processes = [Process(i + 1, int(bit)) for i, bit in enumerate(binary_string)]
   print("\nProcesses:")
   for process in processes:
      print(f"Process {process.id}- {'Alive' if process.is_alive else 'Dead'}")
   initiator_id = int(input(f"\nEnter the process ID that initiates the election (1-{n}): "))
   bully_algorithm = BullyAlgorithm(n, processes)
   bully_algorithm.run_election(initiator_id)
