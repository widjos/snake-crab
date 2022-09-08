from Enum.typeExpression import typeExpression


#SUMA, RESTA ,  DIVISION , MODULO 
Dominant = [
            #INT64                  #FLOAT64                #BOOL                   #CHAR                       #STRING                       ERROR                      nothing                            objeto
                  
    #INT64 
    [
            typeExpression.INT,    typeExpression.FLOAT,   typeExpression.INT,    typeExpression.CHAR,        typeExpression.ERROR,        typeExpression.ERROR,     typeExpression.NOTHING,        typeExpression.ERROR      
    ],
    #FLOAT64
    [
             typeExpression.FLOAT,  typeExpression.FLOAT,   typeExpression.ERROR,  typeExpression.ERROR,        typeExpression.ERROR,       typeExpression.ERROR,       typeExpression.ERROR,        typeExpression.ERROR
    ],
    #BOOL
    [
            typeExpression.INT,     typeExpression.FLOAT,   typeExpression.INT ,  typeExpression.CHAR ,         typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR   
    ],
    #CHAR
    [
            typeExpression.INT,     typeExpression.ERROR ,   typeExpression.CHAR,  typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
    ],
    #STRING 
    [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR,  typeExpression.ERROR,       typeExpression.ERROR,         typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
    ],
    #Error
    [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR    
    ],
    #NOthing
    [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR    
    ],
        #Struct
    [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR    
    ]


]

#Dominante 2 
# MULT POTENCIA 
Dominant2 = [
                #INT64                  #FLOAT64                #BOOL                   #CHAR                       #STRING 

        #INT64
        [
                typeExpression.INT,     typeExpression.FLOAT ,  typeExpression.INT,   typeExpression.ERROR,   typeExpression.ERROR, typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR 
        ],
        #FLOAT64
        [
                typeExpression.FLOAT,   typeExpression.FLOAT,  typeExpression.FLOAT,  typeExpression.ERROR,    typeExpression.ERROR, typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR 
        ],
        #BOOL
        [
                typeExpression.INT,     typeExpression.FLOAT,   typeExpression.INT,  typeExpression.ERROR,      typeExpression.ERROR, typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
        ],
        #CHAR
        [
                typeExpression.ERROR,   typeExpression.ERROR,   typeExpression.ERROR, typeExpression.ERROR,    typeExpression.ERROR, typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
        ],
        #STRING
        [
                typeExpression.STRING, typeExpression.ERROR ,   typeExpression.ERROR, typeExpression.ERROR,   typeExpression.STRING, typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
        ],
        #ERROR
         [
                 typeExpression.ERROR, typeExpression.ERROR,  typeExpression.ERROR, typeExpression.ERROR , typeExpression.ERROR,  typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
    #NOthing
        [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR   
        ],
        #Struct
        [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR     
        ]       
         
]


RelationalDominant = [
                #INT               #FLOAT                  #BOOL              #CHAR                       #STRING                     #ERROR  
         #INT
         [
                typeExpression.BOOL, typeExpression.BOOL, typeExpression.BOOL , typeExpression.ERROR , typeExpression.ERROR,     typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
         #FLOAT 
         [
                 typeExpression.BOOL,typeExpression.BOOL , typeExpression.BOOL , typeExpression.ERROR,  typeExpression.ERROR,    typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
         #BOOL
         [
                 typeExpression.BOOL, typeExpression.BOOL , typeExpression.BOOL , typeExpression.ERROR, typeExpression.ERROR,    typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
         #CHAR
         [
                 typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.BOOL, typeExpression.ERROR,    typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
         #STRING 
         [
                 typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.BOOL,     typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
         #ERROR
         [
                 typeExpression.ERROR, typeExpression.ERROR,  typeExpression.ERROR, typeExpression.ERROR , typeExpression.ERROR,  typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
    #NOthing
        [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR    
        ],
        #Struct
        [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR     
        ]       
 
]

#Dominant Logical
LogicDominant =  [
                #INT               #FLOAT                  #BOOL              #CHAR                       #STRING                     #ERROR  
         #INT
         [
                typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR , typeExpression.ERROR , typeExpression.ERROR,     typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR  
         ],
         #FLOAT 
         [
                 typeExpression.ERROR,typeExpression.ERROR , typeExpression.ERROR , typeExpression.ERROR,  typeExpression.ERROR,    typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR
         ],
         #BOOL
         [
                 typeExpression.ERROR , typeExpression.ERROR , typeExpression.BOOL , typeExpression.ERROR, typeExpression.ERROR,    typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR        
         ],
         #CHAR
         [
                 typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR,    typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR        
         ],
         #STRING 
         [
                 typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR, typeExpression.ERROR,     typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR       
         ],
         #ERROR
         [
                 typeExpression.ERROR, typeExpression.ERROR,  typeExpression.ERROR, typeExpression.ERROR , typeExpression.ERROR,  typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR         
         ],
    #NOthing
        [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR          
        ],
        #Object 
        [
            typeExpression.ERROR,   typeExpression.ERROR ,  typeExpression.ERROR, typeExpression.ERROR ,       typeExpression.ERROR,          typeExpression.ERROR,        typeExpression.ERROR,        typeExpression.ERROR  
        ]         
 


]
