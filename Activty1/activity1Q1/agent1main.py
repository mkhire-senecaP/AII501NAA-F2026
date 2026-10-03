
from email import policy
from email.parser import BytesParser

allowList = ["gmail.com","hotmail.com","outlook.com"]
badwordList = ["spam","scam","bad"] # reads content in body, if either word appears on the count of 5, move email to spam
restrictList = ["test.com"]
spamDir = []
emailDir = []

email_rules = [
    (lambda s: s in restrictList, "SPAM"),
    (lambda s: s in allowList ,     "EMAIL"),
    (lambda s: True,     "NONE"),
]

class EmailSimpleReflexAgent:
    
    def __init__(self,rules):
        self.rules = rules
    
    def read_address_and_act(self,rules):
            
        with open("emailFile2.eml","rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        print("From:", msg["From"])
        print("To:", msg["To"])
        print("Subject:", msg["Subject"])
        print("Date:", msg["Date"])


        body = msg.get_body(preferencelist=("plain","html"))
        if body is not None:
            print("Body:", body.get_content())
        else:
            print("Body: (No Text Body Found)")

        count = {word: 0 for word in badwordList}
        
        fromHead = msg["From"]
        if fromHead and fromHead.addresses:
            domain = fromHead.addresses[0].domain.lower()
            if domain in restrictList:
                print("Bad")
                if body is not None and "spam" in body.get_content().lower():
                    count = {word: 0 for word in badwordList}
                    for line in body.get_content().splitlines():
                        words = line.lower().strip().split()
                            
                        for word in words:
                            if word in count:
                                count[word] += 1
                    total = sum(count.values())
                    print("Bad Word Count:", count)
                    if total >= 5:
                        spamDir.append(msg)
            elif domain in allowList:
                print("good")
                emailDir.append(msg)
        return domain

agent = EmailSimpleReflexAgent(rules=email_rules)

print("Start Simulation")
for step in range(4):
    print(f"\nStep {step + 1}:")
    agent.read_address_and_act(email_rules)
print("Spam List:", spamDir)
print("Email List:",emailDir)
