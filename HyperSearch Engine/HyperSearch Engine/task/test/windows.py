
"""
Context_Windows
This module returns context windows for each query word
"""
from test.tokenizator import Tokenizator
import re

PATTERN_RIGHT = re.compile(r'[\.!?] [A-ZА-Яa-zа-я]') 
PATTERN_LEFT = re.compile(r'[A-ZА-Яa-zа-я] [\.!?]')

class Context_Window(object):
    """
    class Context_Window 
    """
    tokenizator = Tokenizator()
    
    def __init__(self, string, positions, win_start, win_end):
        """
        Constructor of a context window
        @param positions: positions of tokens
        @param string: string representation of a token
        @param win_start: position where window starts
        @param win_end: position where window ends
        """

        self.string = string
        self.positions = positions
        self.win_start = win_start
        self.win_end = win_end
        
        

    def __eq__(self, window):

         return self.string == window.string and self.positions == window.positions and self.win_start == window.win_start and self.win_end == window.win_end
        
    def __repr__(self):
        
        return str(self.string) + ' ' + str(self.positions) + ' ' + str(self.win_start) + ' ' + str(self.win_end)
        
    @classmethod
    def get_window(cls, filename, position, win_size):
        """
        This function returns a context window of a given token's position
        @param filename: a name of a file where token is to be found
        @param position: a position of a token
        @param win_size: desirable size of the context window
        @return: a context window
        """
        if not isinstance(filename, str) or not isinstance(win_size, int):
            raise TypeError('Input has an unappropriate type! %s, %s' % (filename, win_size))
        positions = []
        position = [position.lnumber,position.start,position.end]
        positions.append(position)
        win_end = 0
        win_start = 0
        string = None
        str_num = position[0]
        my_file = open(filename)
        for lnumber,my_string in enumerate(my_file):
            if lnumber == str_num:
                string = my_string
                break
            
        if string == None:
            my_file.close() 
            raise TypeError('This string was not found!')
            
        for tok_num,token in enumerate (cls.tokenizator.token_gen(string[position[1]:])):
            if tok_num == 0:
                win_end = position[2]
            if tok_num == win_size:
                win_end = token.position + len(token.s) + position[1]
                break
            
        for tok_num,token in enumerate (cls.tokenizator.token_gen(string[:position[2]][::-1])):
            if tok_num == win_size:
                win_start = position[2] - token.position - len(token.s)   
                break
            
        my_file.close()    
        return cls(string, positions, win_start, win_end)
    
    @classmethod
    def get_formated_result(cls, filename, position, win_size):
        if win_size != 0:
            result = cls.get_window(filename, position, win_size)
            string = result.string
            positions = str(result.positions)
            start = str(result.win_start)
            end = str(result.win_end)
            formated_result = string.strip()+'|'+positions+'|'+start+'|'+end
            return formated_result
        else:
            return ''

    def get_formated_window(self, w2):
        if not isinstance(w2, Context_Window):
            raise TypeError('Input has an unappropriate type!')
        if self.is_crossed(w2):
            self.get_united_window(w2)
            self.extend_window()
            highlighted = self.highlight_window()
            formated_window = highlighted.strip()+'|'+str(self.positions)+'|'+str(self.win_start)+'|'+str(self.win_end)
            return formated_window
        else:
            self.extend_window()
            w2.extend_window()
            highlighted_win1 = self.highlight_window()
            highlighted_win2 = w2.highlight_window()
            formated_win1 = highlighted_win1.strip()+'|'+str(self.positions)+'|'+str(self.win_start)+'|'+str(self.win_end)
            formated_win2 = highlighted_win2.strip()+'|'+str(w2.positions)+'|'+str(w2.win_start)+'|'+str(w2.win_end)
            result = formated_win1 + '\n ' + formated_win2
            return result
        
    def is_crossed(self, window_B):
        '''
        This function checks if windows are crossed
        @param window_B: the second window
        @return: True or False
        '''
        if not isinstance(window_B, Context_Window):
            raise TypeError('Input has an unappropriate type!')
        if self.win_start <= window_B.win_end and self.win_end >= window_B.win_start and self.positions[0][0] == window_B.positions[0][0]:
            return True
        if self.win_start == window_B.win_start and self.win_end == window_B.win_end and self.positions[0][0] == window_B.positions[0][0]:
            return True
        else:
            return False
        
    def get_united_window(self, window_B):
        
        '''
        This function unites two windows
        @param window_B: the second window
        It changes self so that is has new positions and returns nothing!!
        '''
        
        if not isinstance(window_B, Context_Window):
            raise TypeError('Input has an unappropriate type!')
        
        self.positions.extend(window_B.positions)
        self.win_start = min(window_B.win_start,self.win_start)
        self.win_end = max(window_B.win_end,self.win_end)
       

    def extend_window(self):
        '''
        This function extends a given window to sentence
        @return: an extended window
        ''' 
        to_right = self.string[self.win_end:]
        to_left = self.string[:self.win_start+1][::-1]
        left = PATTERN_LEFT.search(to_left)
        right = PATTERN_RIGHT.search(to_right)
        if left is None:
            self.win_start = 0
        else:
            self.win_start -= left.start()
        if right is None:
            self.win_end = len(self.string)
        else:
            self.win_end += right.start() + 1
                       

    def highlight_window(self):
        '''
        This function takes a substring of window string,
        which corresponds to the window size and highlights it 
        '''
        win_string = self.string[self.win_start:self.win_end]
        fin = '</b>'
        st = '<b>'
        for position in reversed(self.positions):
            end = position[2] - self.win_start
            begin = position[1] - self.win_start
            win_string_one = win_string[:end] + fin + win_string[end:]
            win_string = win_string_one[:begin] + st + win_string_one[begin:]
        return win_string


