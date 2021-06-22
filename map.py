# Note: Create validator function that checks a whole map after it has been 
# created. Check if there are any concepts where one links to the other but 
# not the other way around. This should be a function like origin() that belongs
# to class Map

# Trace back through tuples to print out conditionality, expand line 103 with 
# a recursive for loop which find the links of each link, then apply links_str

# Create __repr__ for Map

#==============================================================================
# Map Class
#==============================================================================

class Map:
    def __init__(self, concepts):
        self.concepts = self.is_valid_concepts(concepts)

    # Validate inputs.
    def is_valid_concepts(self, concepts):

        if isinstance(concepts, list) == False:
            raise ValueError("concepts must be a list")

        if all([isinstance(concepts, Concept) for concepts in concepts]) == False:
            raise ValueError("all items in concepts list must be of type Concept")

        return concepts

    def origin(self):
        for i in range(len(self.concepts)):
            concepts_links = [concept.links for concept in self.concepts]
            if (concepts_links[i] == None):
                print(self.concepts[i].signifier)

#==============================================================================
# Concept Class
#==============================================================================

# Note: Add logic checks in operator classes. If the operator is contains, then
# it can only have certain concepts attached to it, etc.

class Concept: 
    def __init__(self, signifier, signified, links):
        self.signifier  = self.is_valid_signified(signifier)
        self.signified  = self.is_valid_signified(signified)
        self.links      = self.is_valid_links(links)

    # Validate inputs.
    def is_valid_signifier(self, signifier):
        if isinstance(signifier, str) == False:
            raise ValueError("signifier must be a string.")
        return signifier

    def is_valid_signified(self, signified):
        if isinstance(signified, str) == False:
            raise ValueError("signified must be a string.")
        return signified

    def is_valid_links(self, links):

        if links is not None: 

            if isinstance(links, list) == False:
                raise ValueError("""links must be a list of tuples or None:
                links = [(Concept, Operator), (Concept, Operator)]""")

            if all([isinstance(links, tuple) for links in links]) == False:
                raise ValueError("""all items in links list must be tuples:
                links = [(Concept, Operator), (Concept, Operator)]""")

            if max([len(links) for links in links]) != 2:
                raise ValueError("""all tuples in links list must have two items:
                links = [(Concept, Operator), (Concept, Operator)]""")

            if all([isinstance(links[0], Concept) for links in links]) == False:
                raise ValueError("""the first item in links tuple must be a Concept:
                links = [(Concept, Operator), (Concept, Operator)]""")

            if all([isinstance(links[1], Operator) for links in links]) == False:
                raise ValueError("""the second item in links tuple must be an Operator:
                links = [(Concept, Operator), (Concept, Operator)]""")

        return(links)

    # String representation of links for __repr__.
    def links_str(self, links):
        if links is not None:
            links_str = str([(links[0].signifier, links[1].signifier)
                for links in links])
        if links is None:
            links_str = 'Origin'
        return links_str
            
    def __repr__(self):
        return str('\nSignifier: ' + self.signifier + 
                   '\nSignified: ' + self.signified +
                   '\nLinks: '     + self.links_str(self.links) +
                   '\n')

    # Test for conditionality.
    def conditions(self):

        immediate_links = self.links_str(self.links)

#==============================================================================
# Operator Class
#==============================================================================

class Operator: 
    def __init__(self, signifier, signified):
        self.signifier  = self.is_valid_signified(signifier)
        self.signified  = self.is_valid_signified(signified)

    def is_valid_signifier(self, signifier):
        if isinstance(signifier, str) == False:
            raise ValueError('signifier must be a string.')
        return signifier

    def is_valid_signified(self, signified):
        if isinstance(signified, str) == False:
            raise ValueError('signified must be a string.')
        return signified

    def __repr__(self):
        return str('\nSignifier: ' + self.signifier + 
                   '\nSignified: ' + self.signified)


#==============================================================================
# Operators
#==============================================================================

Seems_to_Be = Operator(
    signifier = 'Seems to Be',
    signified = "The latter signifier seems to be the case",
)

Requires = Operator(
    signifier = 'Requires',
    signified = "The prior signifier requires that the latter signifier exist."
)

Opens_To = Operator(
    signifier = 'Opens To',
    signified = """The existence of the prior signifier allows existence of the 
    latter signifier."""
)

#==============================================================================
# Concepts
#==============================================================================

T_Origin_Limit = Concept(
    signifier = 'Tautology Origin Limit',
    signified = """There exists anything at all, or there does not exist 
    anything at all.""",
    links = None
)

Rule1 = Concept(
    signifier = 'Rule1',
    signified = "There is existence at all.",
    links = [(T_Origin_Limit, Seems_to_Be)]
)

Perceptive_Agent = Concept(
    signifier = 'Perceptive Agent',
    signified = "An agent who inaccurately perceives the universe.",
    links = [(Rule1, Opens_To)]
)

Void = Concept(
    signifier = 'Void',
    signified = "A lack of pre-defined meaning.",
    links = [(Rule1, Requires)]
)

#==============================================================================
# Map
#==============================================================================

map1 = Map([T_Origin_Limit, Rule1, Perceptive_Agent, Void])

map1.origin()









