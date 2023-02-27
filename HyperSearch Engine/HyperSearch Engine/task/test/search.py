
"""
SearchEngine
This module does searching for positions of tokens in database
"""
from test.tokenizator import Tokenizator
from test.windows import Context_Window


class SearchEngine(object):
    """
    class SearchEngine
    """
    
    def __init__(self):
        
        self.tokenizator = Tokenizator()
        
          
    def get_dict (self, database, tok_str):
        """
        This function performs searching for positions of a given token
        @param tok_str: str containing token
        @return: dictionary, where a key is a filename
        and a value is a list of positions
        """
        
        if  not isinstance(tok_str,str):
            raise TypeError('Input has an unappropriate type!')
        if  not isinstance(database,dict):
            raise TypeError('Input has an unappropriate type!')

        if tok_str in database:
            return database[tok_str]
        else:
            return {}


    def get_dict_many_tokens(self, database, tok_str):
        """
        This function performs searching for positions of given tokens
        @param tok_str: str containing tokens
        @return: dictionary, where a key is a filename
        and a value is a list of positions of all tokens     
        """

        if not isinstance(tok_str, str):
            raise TypeError('Input has an unappropriate type!')
        if not tok_str:
            return {}
        big_dict_files = []
        for token in self.tokenizator.token_gen(tok_str):
            big_dict_files.append(self.get_dict(database,token.s))
            
        files = set(big_dict_files[0])    
        for file_dict in big_dict_files[1:]:
            files = files.intersection(set(file_dict))

        output_dict = {} 
        for filename in files:
            for token in self.tokenizator.token_gen(tok_str):
               output_dict.setdefault(filename,[]).extend(database[token.s][filename])
            output_dict[filename].sort()
        return output_dict

    
    def get_dict_many_tokens_limit_offset(self, database, tok_str, limit, offset):
        """
        This function performs searching for positions of given tokens
        @param tok_str: str containing tokens
        @param limit: number of files to be returned
        @param offset: from which file to start
        @return: dictionary, where a key is a filename
        @database: a database where we search
        and a value is a list of positions of all tokens     
        """

        if not isinstance(tok_str, str):
            raise TypeError('Input has an unappropriate type!')
        
        if not isinstance(limit, int) or not isinstance (offset, int):
            raise TypeError('Input has an unappropriate type!')
        
        if not tok_str:
            return {}
        
        if offset < 0:
            offset = 0
            
        big_dict_files = []
        for token in self.tokenizator.token_gen(tok_str):
            big_dict_files.append(self.get_dict(database, token.s))  
            
        files = set(big_dict_files[0])    
        for file_dict in big_dict_files[1:]:
            files = files.intersection(set(file_dict))
               
        resulted_files = sorted(files)[offset: limit+offset]
        output_dict = {}
        for filename in resulted_files:
            for token in self.tokenizator.token_gen(tok_str):
               output_dict.setdefault(filename,[]).extend(database[token.s][filename])
            output_dict[filename].sort()
        return output_dict
    
    def get_formated_result(self, database, tok_str, limit, offset):
        result = self.get_dict_many_tokens_limit_offset(database, tok_str, limit=3, offset=0)
        formated_result = '; '.join([f'{key}: {value}' for key, value in result.items()])
        return formated_result


    def get_modified_search(self, database, query, window_size, limit, offset):
        simple_search_dict = self.get_dict_many_tokens_limit_offset(database, query, limit, offset)
        windows = {}
        for filename, positions_lists in simple_search_dict.items():
            win_array = []
            for position in positions_lists:
                window = Context_Window.get_window(filename, position, window_size)
                win_array.append(window)
            windows.setdefault(filename,[]).extend(win_array)                                                   
        for filename, win_array in windows.items():
            for window in win_array:
                window.extend_window()
        for filename, win_array in windows.items():
            i = 0
            while i < len(win_array)-1:
                if win_array[i].is_crossed(win_array[i+1]):
                    win_array[i].get_united_window(win_array[i+1])
                    win_array.remove(win_array[i+1])
                else:
                    i+=1
        output_dictionary = {}
        for filename, win_array in windows.items():
            win_string_list = []
            for window in win_array:
                win_string = window.string.strip() + '|' + str(window.positions) + '|' + str(window.win_start) + '|' + str(window.win_end)
                win_string_list.append(win_string)
            output_dictionary.setdefault(filename,[]).extend(win_string_list)
        return output_dictionary
