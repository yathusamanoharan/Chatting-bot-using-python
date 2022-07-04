import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty ('voices')
engine.setProperty('voices', voices[1].id)

def talk_function(text):
    engine.say(text)
    engine.runAndWait()



while True:

    user_input = input("User:")
    user_input = user_input.lower()

    if user_input == "hello":
        talk_function("Hey, hello");

    elif user_input == "how are you":
        talk_function("I am fine");
       
    elif user_input == "what is your name":
        talk_function("My name is Yathu-assistant");

    elif user_input == "do you like chatting":
        talk_function("yes,I like it");

    elif user_input == "can you help me now":
        talk_function("Yes");

    elif user_input == "how old are you":
        talk_function("I am 21 years old");

    elif user_input == "where are you from":
        talk_function("I am from Mavadivembu");

    elif user_input == "what are you doing now":
        talk_function("I am learning DreamSpace Academy");

    elif user_input == "what is your hobby":
        talk_function("singing, reading and watching cartoons");

    elif user_input == "what is your favourite color":
        talk_function("red");

    elif user_input == "do you have many friends":
        talk_function("yes, I have lot of boy and girl friends");

    elif user_input == "what is your pet":
        talk_function("cat");

    elif user_input == "when were you born":
        talk_function("I born 2001");

    elif user_input == "where did you grow up?":
        talk_function("I grew in Kandy");

    elif user_input == "What was your favourite activity as a child?":
        talk_function("playing games");


    elif user_input == "what was your favourite place as a child?":
        talk_function("beach");


    elif user_input == "who were your friends as child?":
        talk_function("kirushanth and dilakshan");

    elif user_input == "what was high school like for you?":
        talk_function("Bt/kk/vantharumoolai madya maha vidyalaya");

         
    elif user_input == "tell me about your most memorable birthday?":
        talk_function("my 20th birthday was unforgottable");


    elif user_input == "who taught you to drive?":
        talk_function("my younger brother");

    elif user_input == "who inspired you as you mature?":
        talk_function("my mother");       


    elif user_input == "what was the hardest part about growing up?":
        talk_function("my a/l studying period");


    elif user_input == "what job has been your favourite? ":
        talk_function("doctor");
        
    elif user_input == "tell me about your bestfriend's name":
        talk_function("praveena");

        
    elif user_input == "what you usually do on the weekend":
        talk_function("I do my homeworks and play chess");


    elif user_input == "what are your biggest strengths?":
        talk_function("self-confident");

        
    elif user_input == "what are your biggest weakness":
        talk_function("my angry");
        
    elif user_input == "why are you intersted in dreamspace":
        talk_function("It gives many opportunities");
        
    elif user_input == "what is your favourite actor?":
        talk_function("sivakarthikeyan");
        
    elif user_input == "what is your favourite actress?":
        talk_function("saipallavi");

    elif user_input == "what kind of music do you listen to?":
        talk_function("melody songs");

    elif user_input == "what is your favourite game?":
        talk_function("bedminton");

    elif user_input == "what is you favourite food?":
        talk_function("string hopper and chicken curry");

    elif user_input == "who is your favourite singer?":
        talk_function("singer shreya korsel");

    elif user_input == "what is your favourite place in sri lanka?":
        talk_function("kandy");
        
    elif user_input == "please tell me a poem":
        talk_function("Johny johny yes papa,  eating sugar no papa, telling lie no papa ,open your mouth ha ha ha!");       
        

    else:
        talk_function("I don't understand");