Q: Inheritance example

  class father():
    def action(self):
        print("he brought me a cycle")
  class son(father):
      def action(self):
          print("Riding a cycle")
          
  nithish=son()
  nithish.action()
  karunkar=father()
  karunkar.action()

output: 

  Riding a cycle
  he brought me a cycle

  
