import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

    The two strings to the right of the in keyword above are equal
    *semantically*,
    but not equal *representationally*.
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for us,
    making foreign languages "just work" a little bit easier.
    '''
    def __init__(self, text, normal_form='NFC'):
        self.text = text
        self.normal_form = normal_form
        self.normalized = unicodedata.normalize(self.normal_form, self.text)
        self.n = len(self.normalized)

    def __repr__(self):
        '''
        The string returned by the __repr__ function should be valid python
        code that can be substituted directly into the python interpreter to
        reproduce an equivalent object.
        '''
        normalized = unicodedata.normalize(self.normal_form, self.text)
        return 'NormalizedStr(\'' + normalized + '\', \'' + \
               self.normal_form + '\')'

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a regular string object.
        The output is similar, but not exactly the same, as the __repr__
        function.
        '''
        normalized = unicodedata.normalize(self.normal_form, self.text)
        return normalized

    def __len__(self):
        '''
        Returns the length of the string.
        The expression `len(a)` desugars to a.__len__().
        '''
        count = 0
        normalized = unicodedata.normalize(self.normal_form, self.text)
        for i in normalized:
            count += 1
        return count

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained within `self`.
        The expression `a in b` desugars to `b.__contains__(a)`.

        HINT:
        You should normalize the `substr` variable to ensure that the
        comparison is done semantically and not syntactically.
        '''
        normalized = ascii(unicodedata.normalize('NFC', self.text))
        norm_substr = ascii(unicodedata.normalize('NFC', substr))
        count = 0
        for i in range(len(normalized)):
            if normalized[i] == norm_substr[0]:
                frac_normalized = normalized[i:]
                for j in range(len(norm_substr)):
                    try:
                        if frac_normalized[j] == norm_substr[j]:
                            count += 1
                    except Exception:
                        break
                if count == len(norm_substr):
                    return True
        return False

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        The expression `a[b]` desugars to `a.__getitem__(b)`.
        '''
        normalized_list = list(unicodedata.normalize(self.normal_form,
                                                     self.text))
        return normalized_list[index]

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''
        normalized = unicodedata.normalize(self.normal_form, self.text)
        return normalized.lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
        normalized = unicodedata.normalize(self.normal_form, self.text)
        return normalized.upper()

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        The expression `a + b` gets desugared into `a.__add__(b)`.

        HINT:
        The addition of two normalized strings is not guaranteed to
        stay normalized.
        Therefore, you must renormalize the strings after adding them together.
        '''
        normalized_self = unicodedata.normalize(self.normal_form,
                                                str(self.text))
        normalized_b = unicodedata.normalize(self.normal_form, str(b))
        combined = normalized_self + normalized_b
        normalized_combined = unicodedata.normalize(self.normal_form,
                                                    combined)
        return NormalizedStr(normalized_combined)

    def __iter__(self):
        '''
        HINT:
        Recall that the __iter__ method returns a class, which is the
        iterator object.
        You'll need to define your own iterator class with the appropriate
        magic methods,
        and return an instance of that class here.
        '''
        return NormalizedStrIter(self.normalized, self.n)


class NormalizedStrIter:
    '''
    Class that stores the information about a current iteration through the
    data structure
    '''
    def __init__(self, text, n):
        self.text = text
        self.n = n
        self.i = 0

    def __next__(self):
        '''
        Purpose of this function is to return the next list element in
        the string
        '''
        while self.i < self.n:
            self.i += 1
            return self.text[self.i - 1]
        raise StopIteration
