"""
Indexator
This module performs indexing of a text in a given file
"""
from test.tokenizator import Tokenizator
from functools import total_ordering
import os

class Position(object):
    """
    Class Position
    Cointains positions of each token
    """

    def __init__(self, start, end):
        """
        @param start: position on the 1st element of a token
        @param end: position on the last element of a token
        """ 
        self.start = start
        self.end = end
        
    def __eq__(self, position):
      
        return self.start == position.start and self.end == position.end

    def __repr__(self):

        return str(self.start) + ',' + str(self.end)

@total_ordering
class Position_Plus(Position):
    """
    Class Position
    Cointains positions of each token
    """

    def __init__(self, lnumber, start, end):
        """
        @param start: position on the 1st element of a token
        @param end: position on the last element of a token
        @param lnumber: number of a line in a given text
        """
        
        self.start = start
        self.end = end
        self.lnumber = lnumber
        
    def __eq__(self, position):

        return self.lnumber == position.lnumber and self.start == position.start and self.end == position.end 

    def __lt__(self, other_pos):
        '''
        This function compares two positions, i.e. their parameters
        and returns the result of this comparison
        @param other_pos: position that is to be compared with self
        @return: comparison_result, i.e. True or False if one position less than another
        '''
        return ((self.lnumber < other_pos.lnumber)
                or ((self.lnumber == other_pos.lnumber)
                and (self.start < other_pos.start)))

    def __repr__(self):

        return str(self.lnumber) + ','+ str(self.start) + ',' + str(self.end)
        
class Indexer_Dict(object):
    def __init__(self):
        
        self.tokenizator = Tokenizator()
    
    def get_index_dict(self, filedir):
        """
        This function performs indexing of a text in a given file
        """
        if not isinstance(filedir, str):
            raise TypeError('Input has an unappropriate type!')
        for filename in os.listdir(filedir):
            filename = os.path.join(filedir, filename)
            my_file = open(filename)
            output_dict = {}
            for lnumber,line in enumerate(my_file):
                if not line:
                    lnumber +=1
                for token in self.tokenizator.token_gen(line):
                    start = token.position
                    end = start + len(token.s)
                    pos = Position_Plus(lnumber, start, end)
                    output_dict.setdefault(token.s, {}).setdefault(filename, []).append(pos)
                lnumber +=1
            my_file.close()
            return output_dict
    
    def get_formated_result(self, filename):
        result = self.get_index_dict(filename)
        formated_result = '; '.join([f'{key}: {value}' for key, value in result.items()])
        return formated_result
