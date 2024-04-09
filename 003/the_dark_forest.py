print('''
   ad88                                                     
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888
                               __
                             .d$$b
                           .' TO$;.
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |.
                /   "      .d$$$P' |.^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (.      .-(.
   ..--""              `-.(./;`
     _.                      :
                             ;`-
                            :.
                            ;  
''')
print("Welcome to the Dark Forest.")
print("Your mission is to find the secret of the forest.") 

step1 = input('At the beginning of the path, you can choose to go left and enter the forest, or go right and avoid the path through the forest. Where do you want to go? \n Type "left" or "right"\n').lower()
if step1 == "left":
  step2 = input('You enter the dark forest and come across a cave. Do you enter the cave, or do you skip it and continue along the path through the forest? \n Type "cave" or "skip"\n').lower()
  if step2 == "cave":
    step3 = input('You enter a cave where you have 3 paths to choose from. A torch lights the left path, the middle is overgrown with bushes, and the right is completely dark. Which one do you choose? \n Type "left", "mid" or "right"\n').lower()
    if step3 == "left":
      print('You encounter a giant ogre who is having his dinner. He eats you for dessert. Game over.')
      print('''
               __,='`````'=/__
              '//  (o) .(o) | `'         _,-,
              //|     ,_)   (`.      ,-'`_,-.
            ,-~~~.  `'==='  /-,      |==```` .__
           /        `----'     `.     |       ./
        ,-`                  ,   .  ,.-|       .
       /      ,               .,-`.`_,-`|_,..--'.
      ,`    ,/,              ,>,   )     |--`````.
      (      `.`---'`  `-,-'`_,<   .      ._,.--'`
       `.      `--. _,-'`_,-`  |    .
        [`-.___   <`_,-'`------(    /
        (`` _,-.   . --`````````|--`
         >-`_,-`.,-` ,          |
       <`_,'     ,  /|          /
        `  ./.,-/ `/  ./`._/V._/
           (  ._. )    ( .__. )
           |      |    |      |
            |,---_|    |_---.|
            ooOO(_)    (_)OOoo
      ''')
    if step3 == "mid":
      step4 = input('You discover a mysterious portal hidden by the forest dwellers. The portal emits a bright light. Do you decide to enter? \n Type "go" or "stay"\n').lower()
      if step4 == "go":
        print('You won! You discovered the secret of the dark forest! The portal has taken you to a dimension where dreams and desires come true.')
        print('''
        ,--.::::::::::::::::::::::::::::::::::::....:::::::
            )::::::::::::::::::::::::::::::::..      ..::::
         _'-. _:::::::::::::::::::::::::::..   ,--.   ..::
         (    ) ),--.::::::::::::::::::::::.   (    )   .::
                     )-._::::::::::::::::::..   `--'   ..::
        _________________):::::::::::::::::::..      ..::::
        ::::::::::::::::::::::::::::::::::::::::....:::::::
        :::::::::::::::::: Aaaah. Much better :) ::::::::::
        ::::::::_o/ :`:::::::::::::::::::::::::::::::::::::
        !:!:!:!: () !:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!:!
        !!!!!!!! /| !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        |!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|!|
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I|I
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        ''')
      else:
        print('The forest dwellers find you and lock you in a cell. Game over.')
        print('''
        ____________________
        _]|  |  |  |  |  |[_
        _]|==|==|==|==|==|[_
        _]|_ _  |  |  |  |[_
        _]|_|_[ |  |  |  |[_
        _]|_|_[ |  |  |  |[_
        _]|  |  |  |  |  |[_
        _]|  |  |  |  |  |[_
        _]|==|==|==|==|==|[_
        _]|  |  |.-|--|  |[_
        _]|  |  | `.  |  |[_
        _]|  |  |  |`.|  |[_
        _]|  |  |  |  |`.|[_
        _]|  |  |  |  |  |[_
        _]|==|==|==|==|==|[_
        _]|__|__|__|__|__|[_
        ''')
    else: 
      print('Stones fall on you and you die. Game over.')
  else:
    print('You encounter wolves which devour you. Game over.')
    print('''      
        /^.      /^.
        |  .    /  |
        ||. |../ /||
        )'        `(
       ,;`w,    ,w';,
       ;,  ) __ (  ,;
        ;  |(..)/  ;;
       ;|  |vwwv|    ``-...
        ;  `lwwl'   ;      ```''-.
       ;| ; `""' ; ;              `.
        ;         ,   ,          , |
        '  ;      ;   l    .     | |
        ;    ,  ,    |,-,._|      .;
         ;  ; `' ;   '    . `.     .;
         |  |    |  |     |   |    |;
         |  ;    ;  |      .   .   (;
         | |      | l       | | .  |
         | |      | |       | |  ) |
         | |      | ;       | |  | |
         ; ,      : ,      ,_.'  | |
        :__'      | |           ,_.'
                 `--'
    ''')
else:
  print('Mission failed. You were supposed to uncover the secret of the dark forest!')