class Amitabh_bachchan:
    def __init__(self):
        self.__questions = [
            {
                "question": "Which planet is known as the Red Planet?",
                "answer": "Mars",
                "hint": "It is the 4th planet from the Sun.",
                "options": ["Earth", "Venus", "Mars", "Jupiter"],
                "fifty_fifty": ["Mars", "Venus"]
            },
            {
                "question": "Who invented the light bulb?",
                "answer": "Thomas Edison",
                "hint": "His initials are T.E.",
                "options": ["Nikola Tesla", "Albert Einstein", "Isaac Newton", "Thomas Edison"],
                "fifty_fifty": ["Nikola Tesla", "Thomas Edison"]
            },
            {
                "question": "Which is the largest ocean on Earth?",
                "answer": "Pacific Ocean",
                "hint": "It starts with P.",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
                "fifty_fifty": ["Atlantic Ocean", "Pacific Ocean"]
            },
            {
                "question": "Which language is used to create web pages?",
                "answer": "HTML",
                "hint": "It stands for HyperText Markup Language.",
                "options": ["HTML", "Python", "Java", "C++"],
                "fifty_fifty": ["HTML", "Java"]
            },
            {
                "question": "Which country is famous for the Great Wall?",
                "answer": "China",
                "hint": "It's in Asia.",
                "options": ["India", "China", "Japan", "Russia"],
                "fifty_fifty": ["China", "India"]
            }
        ]

    def get_questions(self):
        return self.__questions


class Danish(Amitabh_bachchan):
    def __init__(self):
        Amitabh_bachchan.__init__(self)
        self.score = 0
        self.hint = 1
        self.fifty_fifty = 1

    def start_game(self):
        print("Welcome to kon banega crorepati ke season 7 me")
        print("Aaj hamere first contestant he Mr. Danish Khatri")
        print("Danish ji apke paas 1 Hint or 1 Fifty-Fifty Lifeline he \n")
        print("To chaliye shuru krte he apne pehle sawal se")
        print("Danish ji apka pehla sawal he ye:")

        questions = self.get_questions() # question print karane ke liye


        # question print hoga with options
        for q in questions:
            print(f"\n {q['question']}")
            print("Options:")
            for opt in q["options"]:
                print("-", opt)


            while self.hint > 0 or self.fifty_fifty > 0:
                use_lifeline = input("Danish ji kya aap life_line lena chahenge (yes/no): ")

                if use_lifeline == "no":
                    break
                if use_lifeline == "yes":
                  print("1. 50-50")
                  print("2. Hint")
                choice = input("apke paas 2 life_line ka option he abhi (1/2):")

                if choice == "1" and self.fifty_fifty > 0:
                  print("Fifty-Fifty diya jaye Danish ji ko")
                  print("Remaining Options:")
                  for opt in q["fifty_fifty"]:
                     print("-", opt)
                  self.fifty_fifty -= 1

                elif choice == "2" and self.hint > 0:
                  print("Hint diya jaye Danish ji ko")
                  print("Hint:", q["hint"])
                  self.hint -= 1
                else:
                  print("mujhe maaf karna lekin ab apke paas Lifeline available nhi he.")
                break

            Danish_ans = input("Danish ji aap apna jawab bata sakte he ab: ")

            if Danish_ans == q["answer"]:
                self.score += 1
                print("7 crore")
                print("Mubarak ho Danish ji aap jeet te he 7 crore")
            else:
                print("mujhe afsos he Danish ji lekin apka jawab galat he, ye game yehi pe samapt hota he.")
                break

player = Danish()
player.start_game()