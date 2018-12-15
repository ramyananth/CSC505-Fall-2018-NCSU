%Creatures come in two types: humans and birds.
edge(human, ako, creature).
edge(bird, ako, creature).

%One type of human is a man.
edge(man, ako, human).

%One type of bird is a turkey.
edge(turkey, ako, bird).

%Louis is a man.
edge(louis, isa, man).

%Albert is a man.
edge(albert, isa, man).

%Frank is a turkey.
edge(frank, isa, turkey).

%Humans normally have two legs
property(human, legs, two).

%Birds can normally fly
property(bird, fly, yes).

%Louis has one leg
property(louis, legs, one).

%Turkeys cannot fly.
property(turkey, fly, nope).

%rel(SourceNode, RelationshipType, DestinationNode)
rel(A, Relationship, B):- edge(A, Relationship, B).
rel(A, Relationship, B):- edge(A, Relationship, C), rel(C, isa, B).
rel(A, Relationship, B):- edge(A, Relationship, C), rel(C, ako, B).

%Overriding the properties
PropCheck(A, Prop, Value):- property(A, Prop, Value).
%PropCheck(A, Prop, Value):- edge(A, isa, C), PropCheck(C, Prop, Value), \+ property(A, Prop, _). 
%PropCheck(A, Prop, Value):- edge(A, ako, C), PropCheck(C, Prop, Value), \+ property(A, Prop, _). 
PropCheck(A, Prop, Value):- edge(A,Prop,C), PropCheck(C, isa, Value).
PropCheck(A, Prop, Value):- edge(A,Prop,C), PropCheck(C, ako, Value).