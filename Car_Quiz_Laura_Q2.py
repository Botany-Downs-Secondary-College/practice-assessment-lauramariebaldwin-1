def q2
    v = -9 
    ans = "" 

    ans_list = [] 

    questions = ["Pick a random car", "An older one?", "Pick a JDM car", "Pick a European car", "What brand?", "What type of car?", "How farst?", "Pick a colour" "Price?", "Electric?"]

    A_opt = ["Toyota Prius", "Chevrolet Impala", "Mazda RX7", "Aston Martin", "Lamborghini", "SUV", "180KMPH", "Black", "5K", "Yes, of course"]
    B_opt = ["Ford Ranger", "Corvette Sting Ray", "Honda NSX", "Mercedes", "Nissan", "Sport", "240KMPH", "Red", "20K", "Maybe"]
    C_opt = ["VW Golf", "Maserati Ghibli", "Toyota Supra", "BMW", "Bugatti", "Hatch Back", "280KMPH", "Blue", "50K", "No"]
    D_opt = ["Tesla Model X", "Porsche 911", "Nissan Skyline", "Ferrari", "Holden", "Sedan", "Ludicrous", "White", "200K", "Hybrid"]
   
    end = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"]
#=============================================================================================================================================
    
    blank()
    
    print("~ >  { + }  < ~") # <- decal
    print("Cars")
    print()
    enter()
    print()
    for i in range(0, 10):
        blank()
        #asks question in relation to i
        print("{}?".format(questions[i]))
        print()
        #displays answers in relation to i
        print("A: {}".format(A_opt[i]))
        print("B: {}".format(B_opt[i]))
        print("C: {}".format(C_opt[i]))
        print("D: {}".format(D_opt[i]))
        ans = input(": ")
        ans = ans.upper()
        ans_list.append(ans)
    for i in range(0, len(ans_list)):
        if ans_list[i] == answers[0]:
            v = v + 1
        if ans_list[i] == answers[1]:
            v = v + 2
        if ans_list[i] == answers[2]:
            v = v + 3
        if ans_list[i] == answers[3]:
            v = v + 4  
    for i in range(0, len(v_opt)):
        if v in v_opt[i]:
            blank()
            print("~ >  { + }  < ~~ >  { + }  < ~~ >  { + }  < ~")
            print("Your {} is, based on your decisions".format(end[i]))
            print("I hope you enjoyed doing my EPIC quiz for EPIC kidz")
            input()
        if v in v_loser:
            blank()
            print("~ >  { + }  < ~~ >  { + }  < ~~ >  { + }  < ~")
            print("You messed up during the answering process, I hope")
            print("You Die, I hope you enjoyed doing my EPIC quiz for EPIC kidz") 
            input()
            return
        
        
