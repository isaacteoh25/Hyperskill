import unicodedata
"""
Tokenizator
This module performs the morphological analyses of a text and extracts tokens
"""
class Token(object):
    """
    Class of tokens taken from a given text
    """
    def __init__(self,position,s):
        """
        Consrtuctor for token.
        @param self: self is an odject(here:token) with attributes
        @param position: position is an index of the first element of token
        @param s: s is a string view of a token
        @return: token
        """
        self.position=position  
        self.s=s
        
    def __repr__(self):
        """
        The way the programm returns the final result.
        """
        return self.s+'_'+str(self.position)
    

    
class Token_Type(Token):
    """
    Class of tokens taken from a given text
    """
    def __init__(self,s,tp,position):
        """
        Consrtuctor for token.
        @param self: self is an odject(here:token) with attributes
        @param s: s is a string view of a token
        @param tp: tp is a type of a token
        @return: token with it's type
        """
        self.s=s
        self.tp=tp
        self.position=position
        
    def __repr__(self):
        """
        The way the programm returns the final result.
        """
        return self.s+ '_' + self.tp+'_'+ str(self.position)
        
    
    
class Tokenizator(object):
    """
    Class that returns tokens
    """
    def tokenize(self,stream):
        """
        This is a function.
        @param stream:stream is a text given
        @return: a list of tokens from the given text
        """
        if  not isinstance(stream,str):
            raise ValueError('Input has an unappropriate type, it should be str')
        tokensback = []
        for i,c in enumerate(stream): 
            if c.isalpha() and (not stream[i-1].isalpha() or i==0):   
                position=i
            if not c.isalpha()and i>0 and stream[i-1].isalpha():   
                s=stream[position:i]
                t=Token(position,s)                        
                tokensback.append(t)      
        if c.isalpha():                   
            s=stream[position:i+1]
            t=Token(position,s)
            tokensback.append(t)
        return tokensback
    
    def tokens_generator(self, stream):
        """
        This is a generator.
        @param stream:stream is a text given
        @return: tokens from the given text
        """
        if  not isinstance(stream, str):
            raise ValueError('Input has an unappropriate type, it should be str')
        for i,c in enumerate(stream):  
            if c.isalpha() and (not stream[i-1].isalpha() or i == 0):   
                position = i
            if not c.isalpha()and i>0 and stream[i-1].isalpha():   
                s = stream[position:i]
                t = Token(position, s)                        
                yield(t)    
        if c.isalpha():                   
            s = stream[position:i+1]
            t = Token(position, s)
            yield(t)
           
    @staticmethod
    def tokens_type_definition(x):
       """
       This is a static method, which defines a type of a token
       @return: type of a token
       """
       tp = 'type' 
       if x.isalpha():
           tp = 'alpha'
       if x.isdigit():
           tp = 'digit'
       if x.isspace():
           tp = 'space'
       if unicodedata.category(x)[0] == 'P':
           tp = 'punct'
       return tp      
      
    def tokens_generator_plus_type (self, stream):
        """
        This is a generator.
        @param stream:stream is a text given
        @return: tokens from the given text plus their type
        """
        if  not isinstance(stream, str):
            raise ValueError('Input has an unappropriate type, it should be str')
        position=0
        for i,c in enumerate(stream):  
            if self.tokens_type_definition(c) != self.tokens_type_definition(stream[i-1]) and i>0:
                tp = self.tokens_type_definition(stream[i-1])
                s = stream[position:i]
                position = i
                t = Token_Type(s,tp,position)                        
                yield(t)      
        if self.tokens_type_definition(c):
            tp = self.tokens_type_definition(c)
            s = stream[position:i+1]
            t = Token_Type(s,tp,position)
            yield(t)
            
    def tokens_generator_plus_type_optimized (self, stream):
        """
        This is a generator.
        @param stream:stream is a text given
        @return: tokens from the given text plus their type
        """
        if  not isinstance(stream, str):
            raise ValueError('Input has an unappropriate type, it should be str')
        position=0
        tp_of_c=self.tokens_type_definition(stream[0])
        for i,c in enumerate(stream): 
            if i>0 and self.tokens_type_definition(c) != tp_of_c:
                tp = tp_of_c
                tp_of_c = self.tokens_type_definition(c)
                s = stream[position:i]
                t = Token_Type(s,tp,position)  
                position = i
                yield(t)    
        tp = self.tokens_type_definition(c)
        s = stream[position:i+1]
        t = Token_Type(s,tp,position)
        yield(t)
        
    def token_gen(self, stream):
        if not stream:
            print('None')
        if len(stream) == 0:
            yield None
        for token in self.tokens_generator_plus_type_optimized(stream):
            if token.tp == 'alpha' or token.tp == 'digit':
                yield(token)

    def token_gen_format(self, stream):
        token_string = ''
        for token in self.tokens_generator_plus_type_optimized(stream):
            if token.tp == 'alpha' or token.tp == 'digit':
                token_format = token.s+'_'+token.tp+'_'+ str(token.position)
                token_string+= token_format+'\n'
        return token_string
       
if __name__ == '__main__':
    x=Tokenizator()
    
